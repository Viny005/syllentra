"""Nur isolierte synthetische PostgreSQL-Probe; keine Cloud und keine Echtdaten."""

import json
import os
import secrets
import subprocess
import sys
import time
from pathlib import Path

IMAGE = "postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27"
STATE = Path(__file__).resolve().parents[1] / ".local" / "database.json"
NAME = "syllentra-mission9-local"


def main() -> None:
    if sys.argv[1:] != ["start"]:
        raise SystemExit("Aufruf: python scripts/local_db.py start; keine automatische Löschung")
    if STATE.exists():
        raise SystemExit(
            "Lokaler Zustand vorhanden; bestehenden Container prüfen, nicht überschreiben."
        )
    password = secrets.token_urlsafe(32)
    runtime_password = secrets.token_urlsafe(32)
    env = dict(os.environ, POSTGRES_PASSWORD=password)
    subprocess.run(
        [
            "docker",
            "run",
            "--detach",
            "--name",
            NAME,
            "--label",
            "syllentra.synthetic=true",
            "--publish",
            "127.0.0.1:55439:5432",
            "--tmpfs",
            "/var/lib/postgresql/data:rw",
            "--memory",
            "384m",
            "--cpus",
            "1",
            "--env",
            "POSTGRES_PASSWORD",
            IMAGE,
        ],
        env=env,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    for _ in range(60):
        ready = subprocess.run(
            ["docker", "exec", NAME, "pg_isready", "-U", "postgres"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if ready.returncode == 0:
            break
        time.sleep(0.5)
    else:
        raise SystemExit("Datenbank nicht bereit; Containerzustand prüfen.")
    # Zufällige Credentials gelangen nur über stdin bzw. geschützte lokale Datei, nie ins Git.
    sql = (
        f"CREATE ROLE syllentra_runtime LOGIN PASSWORD '{runtime_password}';\n"
        "CREATE DATABASE syllentra_prototype;\nCREATE DATABASE syllentra_test;\n"
    )
    subprocess.run(
        ["docker", "exec", "-i", NAME, "psql", "-v", "ON_ERROR_STOP=1", "-U", "postgres"],
        input=sql,
        text=True,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    STATE.parent.mkdir(mode=0o700, exist_ok=True)
    fd = os.open(STATE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump(
            {
                "migration_url": f"postgresql://postgres:{password}@127.0.0.1:55439/",
                "runtime_url": f"postgresql://syllentra_runtime:{runtime_password}@127.0.0.1:55439/",
            },
            f,
        )
    print("Isolierter lokaler PostgreSQL gestartet; Credentials nur in .local/database.json.")


if __name__ == "__main__":
    main()
