"""CI-spezifischer temporärer Test-PostgreSQL-Lebenszyklus.

Verwendet einen eindeutigen Container, flüchtiges tmpfs, bindet ausschließlich an 127.0.0.1:55439,
erzeugt die Rolle syllentra_runtime und schreibt .local/database.json mit 0600.
"""

import json
import os
import secrets
import subprocess
import sys
import time
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".local" / "database.json"
IMAGE = "postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27"
CONTAINER_PREFIX = "syllentra-ci-pg-"
PORT = 55439


def _get_container_name() -> str:
    name_file = ROOT / ".local" / ".ci_container_name"
    if name_file.exists():
        return name_file.read_text(encoding="utf-8").strip()
    return ""


def start() -> None:
    if STATE.exists():
        raise SystemExit(".local/database.json existiert bereits. Start verweigert.")

    container_id = uuid4().hex[:12]
    name = f"{CONTAINER_PREFIX}{container_id}"
    password = secrets.token_urlsafe(32)
    runtime_password = secrets.token_urlsafe(32)

    ROOT.joinpath(".local").mkdir(mode=0o700, exist_ok=True)
    name_file = ROOT / ".local" / ".ci_container_name"
    name_file.write_text(name, encoding="utf-8")
    name_file.chmod(0o600)

    env = dict(os.environ, POSTGRES_PASSWORD=password)
    subprocess.run(
        [
            "docker",
            "run",
            "--detach",
            "--name",
            name,
            "--label",
            "syllentra.ci=true",
            "--label",
            "syllentra.synthetic=true",
            "--publish",
            f"127.0.0.1:{PORT}:5432",
            "--tmpfs",
            "/var/lib/postgresql/data:rw",
            "--memory",
            "512m",
            "--cpus",
            "1",
            "--env",
            "POSTGRES_PASSWORD",
            IMAGE,
        ],
        env=env,
        check=True,
    )

    ready = False
    for _ in range(60):
        probe = subprocess.run(
            ["docker", "exec", name, "pg_isready", "-U", "postgres"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if probe.returncode == 0:
            ready = True
            break
        time.sleep(0.5)

    if not ready:
        stop()
        raise SystemExit("PostgreSQL im CI-Container wurde nicht innerhalb von 30s bereit.")

    # Initialisierung der Rollen und Template-/Testdatenbanken
    sql = (
        f"CREATE ROLE syllentra_runtime LOGIN PASSWORD '{runtime_password}';\n"
        "CREATE DATABASE syllentra_prototype;\nCREATE DATABASE syllentra_test;\n"
    )
    subprocess.run(
        ["docker", "exec", "-i", name, "psql", "-v", "ON_ERROR_STOP=1", "-U", "postgres"],
        input=sql,
        text=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )

    fd = os.open(STATE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(
            {
                "migration_url": f"postgresql://postgres:{password}@127.0.0.1:{PORT}/",
                "runtime_url": f"postgresql://syllentra_runtime:{runtime_password}@127.0.0.1:{PORT}/",
            },
            f,
        )
    print(f"CI-PostgreSQL erfolgreich gestartet: {name}")


def stop() -> None:
    name = _get_container_name()
    if not name or not name.startswith(CONTAINER_PREFIX):
        print("Kein CI-spezifischer Containername gefunden. Kein Docker-Stopp ausgeführt.")
        return

    # Prüfe ob der Container die Syllentra-CI-Labels trägt
    inspect = subprocess.run(
        ["docker", "inspect", "--format", '{{index .Config.Labels "syllentra.ci"}}', name],
        capture_output=True,
        text=True,
    )
    if inspect.returncode == 0 and inspect.stdout.strip() == "true":
        subprocess.run(
            ["docker", "stop", "--time", "5", name],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        subprocess.run(
            ["docker", "rm", "--force", name],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"CI-Container sicher gestoppt und entfernt: {name}")
    else:
        print(f"Container {name} ist kein verifizierter CI-Container. Entfernen übersprungen.")

    if STATE.exists():
        STATE.unlink(missing_ok=True)
    name_file = ROOT / ".local" / ".ci_container_name"
    if name_file.exists():
        name_file.unlink(missing_ok=True)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["start", "stop"]:
        raise SystemExit("Aufruf: python scripts/ci_test_db.py [start|stop]")
    if sys.argv[1] == "start":
        start()
    else:
        stop()
