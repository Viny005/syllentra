"""CI-spezifischer temporärer Test-PostgreSQL-Lebenszyklus mit Fail-Closed-Härtung.

Verwendet einen eindeutigen Container, flüchtiges tmpfs, bindet ausschließlich an 127.0.0.1:55439,
bindet den Container an ein kryptografisches Eigentumstoken und schützt alle Zustandsdateien.
Keine Docker-Fehler werden ignoriert; alle kritischen Operationen besitzen Timeouts.
"""

import json
import logging
import os
import secrets
import subprocess
import sys
import time
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / ".local" / "database.json"
META_FILE = ROOT / ".local" / ".ci_pg_meta.json"
IMAGE = "postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27"
CONTAINER_PREFIX = "syllentra-ci-pg-"
PORT = 55439

# Timeouts in Sekunden
DOCKER_CMD_TIMEOUT = 15.0
READY_TIMEOUT = 30.0
READY_INTERVAL = 0.5


class CIPostgresError(RuntimeError):
    """Fehler während des CI-PostgreSQL-Lebenszyklus."""


def _run_docker(
    args: list[str],
    timeout: float = DOCKER_CMD_TIMEOUT,
    input_text: str | None = None,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Führt einen Docker-Befehl mit kontrolliertem Timeout und erfasster Ausgabe aus."""
    try:
        return subprocess.run(
            ["docker", *args],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
            env=env,
        )
    except subprocess.TimeoutExpired as exc:
        raise CIPostgresError(
            f"Docker-Befehl lief in Timeout ({timeout}s): docker {' '.join(args)}"
        ) from exc
    except FileNotFoundError as exc:
        raise CIPostgresError("Docker-CLI ('docker') nicht gefunden.") from exc


def _read_meta() -> dict[str, str] | None:
    """Liest die geschützten Metadaten des aktuellen CI-Laufs."""
    if not META_FILE.exists():
        return None
    try:
        data = json.loads(META_FILE.read_text(encoding="utf-8"))
        if isinstance(data, dict) and "container_name" in data and "owner_token" in data:
            return {
                "container_name": str(data["container_name"]),
                "owner_token": str(data["owner_token"]),
            }
    except Exception as exc:
        logging.warning("Konnte CI-Metadaten nicht parsen: %s", exc)
    return None


def _check_container_exists(name: str) -> tuple[bool, str, dict[str, str]]:
    """Prüft verlässlich, ob der Container existiert, erreichbar ist und welche Labels er trägt.

    Rückgabe: (exists, status_detail, labels_dict)
    """
    res = _run_docker(["inspect", "--format", "{{json .Config.Labels}}|{{.State.Status}}", name])
    if res.returncode == 0:
        out = res.stdout.strip()
        if "|" in out:
            labels_json, status = out.split("|", 1)
            try:
                labels = json.loads(labels_json) or {}
            except Exception:
                labels = {}
            return True, status, labels
        return True, "running", {}

    stderr = res.stderr.lower()
    # Eindeutige Abwesenheit erkennen
    if "no such container" in stderr or "no such object" in stderr or "not found" in stderr:
        return False, "not_found", {}

    # Daemon- oder Berechtigungsfehler
    if "cannot connect to the docker daemon" in stderr or "is the docker daemon running" in stderr:
        raise CIPostgresError(f"Docker-Daemon nicht erreichbar: {res.stderr.strip()}")
    if "permission denied" in stderr:
        msg = f"Docker-Zugriff verweigert (Permission denied): {res.stderr.strip()}"
        raise CIPostgresError(msg)

    # Unklarer Fehler: fail-closed behandeln
    raise CIPostgresError(f"Unerwarteter Fehler bei docker inspect: {res.stderr.strip()}")


def start() -> None:
    """Startet den isolierten CI-PostgreSQL-Container mit strikter Eigentumsbindung."""
    # 1. Schutz bestehender Zustandsdateien
    if STATE.exists():
        raise CIPostgresError(
            f"Start verweigert: {STATE} existiert bereits. "
            "Bestehende Datenbank darf nicht überschrieben werden."
        )
    if META_FILE.exists():
        raise CIPostgresError(
            f"Start verweigert: {META_FILE} existiert bereits. Ein aktiver CI-Zustand liegt vor."
        )

    container_id = uuid4().hex[:12]
    name = f"{CONTAINER_PREFIX}{container_id}"
    owner_token = secrets.token_hex(16)  # 32 Hex-Zeichen
    password = secrets.token_urlsafe(32)
    runtime_password = secrets.token_urlsafe(32)

    ROOT.joinpath(".local").mkdir(mode=0o700, exist_ok=True)

    # Metadaten-Datei atomar mit 0600 anlegen, BEVOR der Container gestartet wird
    fd_meta = os.open(META_FILE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd_meta, "w", encoding="utf-8") as f_meta:
        json.dump({"container_name": name, "owner_token": owner_token}, f_meta)

    # 2. Container starten mit strikten Eigentums-Labels
    env = dict(os.environ, POSTGRES_PASSWORD=password)
    run_args = [
        "run",
        "--detach",
        "--name", name,
        "--label", "syllentra.ci=true",
        "--label", "syllentra.synthetic=true",
        "--label", f"syllentra.owner_token={owner_token}",
        "--publish", f"127.0.0.1:{PORT}:5432",
        "--tmpfs", "/var/lib/postgresql/data:rw",
        "--memory", "512m",
        "--cpus", "1",
        "--env", "POSTGRES_PASSWORD",
        IMAGE,
    ]

    try:
        run_res = _run_docker(run_args, timeout=20.0, env=env)
        if run_res.returncode != 0:
            raise CIPostgresError(
                f"docker run fehlgeschlagen (Code {run_res.returncode}): {run_res.stderr.strip()}"
            )

        # 3. Healthcheck mit monotoner Frist (READY_TIMEOUT)
        # PostgreSQL führt beim ersten Start oft einen internen Restart durch.
        # Wir verlangen 2 aufeinanderfolgende erfolgreiche Probes.
        start_time = time.monotonic()
        consecutive_ok = 0
        ready = False
        while time.monotonic() - start_time < READY_TIMEOUT:
            probe = _run_docker(["exec", name, "pg_isready", "-U", "postgres"], timeout=3.0)
            if probe.returncode == 0:
                consecutive_ok += 1
                if consecutive_ok >= 2:
                    ready = True
                    break
            else:
                consecutive_ok = 0
            time.sleep(READY_INTERVAL)

        if not ready:
            raise CIPostgresError(
                f"PostgreSQL im CI-Container wurde nicht innerhalb von {READY_TIMEOUT}s bereit."
            )

        # 4. Rollen- und Datenbank-Initialisierung mit Retries
        sql = (
            f"CREATE ROLE syllentra_runtime LOGIN PASSWORD '{runtime_password}';\n"
            "CREATE DATABASE syllentra_prototype;\nCREATE DATABASE syllentra_test;\n"
        )
        init_success = False
        init_err = ""
        for _ in range(5):
            init_res = _run_docker(
                ["exec", "-i", name, "psql", "-v", "ON_ERROR_STOP=1", "-U", "postgres"],
                input_text=sql,
                timeout=10.0,
            )
            if init_res.returncode == 0:
                init_success = True
                break
            init_err = init_res.stderr.strip()
            time.sleep(1.0)

        if not init_success:
            raise CIPostgresError(
                f"PostgreSQL-Rolleninitialisierung fehlgeschlagen: {init_err}"
            )

        # 5. Konfiguration atomar schreiben (0600)
        fd = os.open(STATE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "migration_url": f"postgresql://postgres:{password}@127.0.0.1:{PORT}/",
                    "runtime_url": (
                        f"postgresql://syllentra_runtime:{runtime_password}@127.0.0.1:{PORT}/"
                    ),
                },
                f,
            )
        print(f"CI-PostgreSQL erfolgreich gestartet: {name}")

    except Exception as exc:
        print(f"Fehler während CI-PostgreSQL-Start: {exc}", file=sys.stderr)
        # Kontrollierten Teardown für den soeben angelegten Container versuchen
        try:
            stop()
        except Exception as stop_exc:
            print(
                f"Zusätzlicher Fehler beim Teardown nach Start-Abbruch: {stop_exc}",
                file=sys.stderr,
            )
        raise


def stop() -> None:
    """Stoppt und entfernt den CI-Container mit fail-closed Überprüfung der Eigentümerschaft."""
    meta = _read_meta()
    if meta is None:
        # Falls keine Meta-Datei existiert, aber eine STATE-Datei: Gefahr, fremde DB zu berühren!
        if STATE.exists():
            raise CIPostgresError(
                f"Teardown verweigert: {STATE} existiert, aber keine gültige CI-Metadaten-Datei "
                f"{META_FILE}. Fremde Instanz geschützt."
            )
        print("Kein CI-Zustand vorhanden. Teardown nicht erforderlich.")
        return

    name = meta["container_name"]
    expected_token = meta["owner_token"]

    if not name.startswith(CONTAINER_PREFIX):
        raise CIPostgresError(
            f"Teardown verweigert: Containername '{name}' entspricht nicht dem CI-Namenspräfix."
        )

    # 1. Existenz und Eigentümerschaft prüfen
    exists, status, labels = _check_container_exists(name)
    if exists:
        # Labels validieren
        if (
            labels.get("syllentra.ci") != "true"
            or labels.get("syllentra.owner_token") != expected_token
        ):
            raise CIPostgresError(
                f"Teardown verweigert: Container '{name}' besitzt nicht die erforderlichen "
                f"Eigentums-Labels (syllentra.ci={labels.get('syllentra.ci')}, "
                f"owner_token={labels.get('syllentra.owner_token')})."
            )

        # 2. Container stoppen
        stop_res = _run_docker(["stop", "--time", "5", name], timeout=15.0)

        # 3. Container entfernen
        rm_res = _run_docker(["rm", "--force", name], timeout=15.0)

        # 4. Abwesenheit nachweislich verifizieren
        post_exists, post_status, _ = _check_container_exists(name)
        if post_exists:
            # Container ist IMMER NOCH da -> FAIL CLOSED!
            # Zustandsdateien NICHT löschen, Fehler werfen
            raise CIPostgresError(
                f"Container-Cleanup fehlgeschlagen: Container '{name}' existiert weiterhin "
                f"(Status: {post_status}). Stop-Output: {stop_res.stderr.strip()}; "
                f"Rm-Output: {rm_res.stderr.strip()}"
            )

        print(f"CI-Container nachweislich entfernt: {name}")
    else:
        print(f"CI-Container '{name}' existiert nicht mehr (bereits entfernt).")

    # 5. Erst NACH nachgewiesener Abwesenheit Zustandsdateien aufräumen
    if STATE.exists():
        try:
            STATE.unlink()
        except OSError as e:
            print(f"Warnung beim Löschen von {STATE}: {e}", file=sys.stderr)

    if META_FILE.exists():
        try:
            META_FILE.unlink()
        except OSError as e:
            print(f"Warnung beim Löschen von {META_FILE}: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["start", "stop"]:
        raise SystemExit("Aufruf: python scripts/ci_test_db.py [start|stop]")
    try:
        if sys.argv[1] == "start":
            start()
        else:
            stop()
    except Exception as err:
        print(f"CI-PostgreSQL-Fehler: {err}", file=sys.stderr)
        sys.exit(1)
