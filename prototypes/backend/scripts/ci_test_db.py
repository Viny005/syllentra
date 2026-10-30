"""CI-spezifischer temporärer Test-PostgreSQL-Lebenszyklus mit Fail-Closed-Härtung.

Verwendet einen eindeutigen Container, flüchtiges tmpfs, bindet ausschließlich an 127.0.0.1:55439.
Jede Programminvokation benötigt ein unabhängig bereitgestelltes Invocation-Token.
Eine gespeicherte Containeridentität allein berechtigt niemals eine neue Invocation zur Löschung.
Keine Geheimnisse, Passwörter oder Token erscheinen in Fehlertexten oder Logs.
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
META_FILE = ROOT / ".local" / ".ci_pg_meta.json"
IMAGE = "postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27"
CONTAINER_PREFIX = "syllentra-ci-pg-"
PORT = 55439
ENV_TOKEN_KEY = "SYLLENTRA_CI_INVOCATION_TOKEN"

# Timeouts in Sekunden
DOCKER_CMD_TIMEOUT = 15.0
READY_TIMEOUT = 30.0
READY_INTERVAL = 0.5


class CIPostgresError(RuntimeError):
    """Fehler während des CI-PostgreSQL-Lebenszyklus."""


def get_current_invocation_token() -> str:
    """Liest und validiert das Invocation-Token der aktuellen Ausführung."""
    token = os.environ.get(ENV_TOKEN_KEY, "").strip()
    if not token or len(token) < 16:
        raise CIPostgresError(
            f"Ungültiges oder fehlendes Invocation-Token in Umgebungsvariable {ENV_TOKEN_KEY}. "
            "Jede Ausführung muss vorab ein unabhängiges Token erhalten."
        )
    return token


def _sanitize_output(text: str, *sensitive_values: str) -> str:
    """Entfernt sensible Werte (Passwörter, Token) aus Fehlerausgaben."""
    clean = text
    for val in sensitive_values:
        if val and len(val) >= 4:
            clean = clean.replace(val, "[REDACTED]")
    return clean.strip()


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
        safe_args = " ".join(args[:2])  # Keine vollständigen Argumente protokollieren
        raise CIPostgresError(
            f"Docker-Befehl lief in Timeout ({timeout}s): docker {safe_args}..."
        ) from exc
    except FileNotFoundError as exc:
        raise CIPostgresError("Docker-CLI ('docker') nicht gefunden.") from exc


def _read_meta() -> dict[str, str] | None:
    """Liest und validiert die geschützten Metadaten des aktuellen CI-Laufs.

    Unterscheidet sauber zwischen 'Datei existiert nicht' (None)
    und 'Datei existiert, ist aber beschädigt/ungültig' (CIPostgresError).
    """
    if not META_FILE.exists():
        return None

    try:
        content = META_FILE.read_text(encoding="utf-8").strip()
        if not content:
            raise CIPostgresError(
                f"Metadatendatei {META_FILE} ist leer oder beschädigt. "
                "Teardown verweigert; fremde Ressourcen geschützt."
            )
        data = json.loads(content)
        if (
            isinstance(data, dict)
            and "container_name" in data
            and "owner_token" in data
            and "container_id" in data
        ):
            return {
                "container_name": str(data["container_name"]),
                "owner_token": str(data["owner_token"]),
                "container_id": str(data["container_id"]),
            }
        raise CIPostgresError(
            f"Metadatendatei {META_FILE} enthält unvollständige Felder. "
            "Teardown verweigert; fremde Ressourcen geschützt."
        )
    except json.JSONDecodeError as exc:
        raise CIPostgresError(
            f"Metadatendatei {META_FILE} ist kein gültiges JSON: {exc}. "
            "Teardown verweigert; fremde Ressourcen geschützt."
        ) from exc
    except OSError as exc:
        raise CIPostgresError(
            f"Metadatendatei {META_FILE} konnte nicht gelesen werden: {exc}."
        ) from exc


def _check_container_exists(name: str) -> tuple[bool, str, dict[str, str], str]:
    """Prüft verlässlich, ob der Zielcontainer existiert und welche Labels er trägt.

    Unterscheidet präzise zwischen:
    A. Existenz bestätigt (True, status, labels, full_id)
    B. Abwesenheit des konkreten Zielcontainers eindeutig bestätigt (False, 'not_found', {}, '')
    C. Daemon nicht erreichbar / Permission Denied / unklarer Fehler (CIPostgresError)
    """
    fmt = "{{.Id}}|{{json .Config.Labels}}|{{.State.Status}}"
    res = _run_docker(["inspect", "--format", fmt, name])
    if res.returncode == 0:
        out = res.stdout.strip()
        parts = out.split("|", 2)
        if len(parts) == 3:
            full_id, labels_json, status = parts[0], parts[1], parts[2]
            try:
                labels = json.loads(labels_json) or {}
            except Exception:
                labels = {}
            return True, status, labels, full_id
        return True, "running", {}, ""

    stderr = res.stderr.strip()
    stderr_lower = stderr.lower()

    # Daemon- oder Berechtigungsfehler MÜSSEN vor jeder Textprüfung abgefangen werden
    if (
        "cannot connect to the docker daemon" in stderr_lower
        or "is the docker daemon running" in stderr_lower
    ):
        raise CIPostgresError(f"Docker-Daemon nicht erreichbar: {stderr}")
    if "permission denied" in stderr_lower:
        raise CIPostgresError(f"Docker-Zugriff verweigert (Permission denied): {stderr}")

    # Präzise Abwesenheitsprüfung: Docker gibt 'Error: No such container: <name>' zurück
    if (
        ("no such container" in stderr_lower or "no such object" in stderr_lower)
        and name.lower() in stderr_lower
    ):
        return False, "not_found", {}, ""

    # Falls der Fehlertext nur unspezifisches 'not found' enthält: docker ps -a
    ps_res = _run_docker(["ps", "-a", "--filter", f"name=^/{name}$", "--format", "{{.Names}}"])
    if ps_res.returncode == 0 and not ps_res.stdout.strip():
        return False, "not_found", {}, ""

    # Unklarer oder mehrdeutiger Fehler: Immer FAIL CLOSED!
    raise CIPostgresError(f"Unerwarteter Fehler bei Überprüfung von Container '{name}': {stderr}")


def start() -> None:
    """Startet den isolierten CI-PostgreSQL-Container mit strikter Invocation-Bindung."""
    # 1. Unabhängig bereitgestelltes Invocation-Token einfordern
    invocation_token = get_current_invocation_token()

    # 2. Schutz bestehender Zustandsdateien
    if STATE.exists():
        raise CIPostgresError(
            f"Start verweigert: {STATE} existiert bereits. "
            "Bestehende Datenbank darf nicht überschrieben werden."
        )
    if META_FILE.exists():
        raise CIPostgresError(
            f"Start verweigert: {META_FILE} existiert bereits. "
            "Ein aktiver oder verwaister CI-Zustand liegt vor."
        )

    container_uid = uuid4().hex[:12]
    name = f"{CONTAINER_PREFIX}{container_uid}"
    password = secrets.token_urlsafe(32)
    runtime_password = secrets.token_urlsafe(32)

    ROOT.joinpath(".local").mkdir(mode=0o700, exist_ok=True)

    # 3. Metadaten atomar anlegen (.tmp -> rename), BEVOR der Container erzeugt wird
    tmp_meta = ROOT / ".local" / f".ci_pg_meta_{container_uid}.tmp"
    fd_meta = os.open(tmp_meta, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd_meta, "w", encoding="utf-8") as f_meta:
        json.dump(
            {
                "container_name": name,
                "owner_token": invocation_token,
                "container_id": "",
            },
            f_meta,
        )
    os.replace(tmp_meta, META_FILE)

    # 4. Container starten mit strikten Eigentums-Labels
    env = dict(os.environ, POSTGRES_PASSWORD=password)
    run_args = [
        "run",
        "--detach",
        "--name", name,
        "--label", "syllentra.ci=true",
        "--label", "syllentra.synthetic=true",
        "--label", f"syllentra.owner_token={invocation_token}",
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
            err_msg = _sanitize_output(run_res.stderr, password, invocation_token)
            raise CIPostgresError(
                f"docker run fehlgeschlagen (Code {run_res.returncode}): {err_msg}"
            )

        container_long_id = run_res.stdout.strip()

        # Container-ID in Metadaten atomar aktualisieren
        tmp_meta_update = ROOT / ".local" / f".ci_pg_meta_up_{container_uid}.tmp"
        fd_up = os.open(tmp_meta_update, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd_up, "w", encoding="utf-8") as f_up:
            json.dump(
                {
                    "container_name": name,
                    "owner_token": invocation_token,
                    "container_id": container_long_id,
                },
                f_up,
            )
        os.replace(tmp_meta_update, META_FILE)

        # 5. Healthcheck mit Frist (READY_TIMEOUT)
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
                f"PostgreSQL im CI-Container wurde nicht innerhalb von ca. {READY_TIMEOUT}s bereit."
            )

        # 6. Rollen- und Datenbank-Initialisierung (sicher idempotent mit IF NOT EXISTS)
        sql = (
            "DO $$ BEGIN\n"
            "  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'syllentra_runtime') THEN\n"
            f"    CREATE ROLE syllentra_runtime LOGIN PASSWORD '{runtime_password}';\n"
            "  END IF;\n"
            "END $$;\n"
            "SELECT 'CREATE DATABASE syllentra_prototype' WHERE NOT EXISTS "
            "(SELECT FROM pg_database WHERE datname = 'syllentra_prototype')\\gexec\n"
            "SELECT 'CREATE DATABASE syllentra_test' WHERE NOT EXISTS "
            "(SELECT FROM pg_database WHERE datname = 'syllentra_test')\\gexec\n"
        )
        init_res = _run_docker(
            ["exec", "-i", name, "psql", "-v", "ON_ERROR_STOP=1", "-U", "postgres"],
            input_text=sql,
            timeout=10.0,
        )
        if init_res.returncode != 0:
            clean_err = _sanitize_output(init_res.stderr, runtime_password, password)
            raise CIPostgresError(f"PostgreSQL-Rolleninitialisierung fehlgeschlagen: {clean_err}")

        # 7. Konfiguration atomar schreiben (.tmp -> rename mit 0600)
        tmp_state = ROOT / ".local" / f"database_{container_uid}.tmp"
        fd_state = os.open(tmp_state, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd_state, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "migration_url": f"postgresql://postgres:{password}@127.0.0.1:{PORT}/",
                    "runtime_url": (
                        f"postgresql://syllentra_runtime:{runtime_password}@127.0.0.1:{PORT}/"
                    ),
                },
                f,
            )
        os.replace(tmp_state, STATE)
        print(f"CI-PostgreSQL erfolgreich gestartet: {name}")

    except Exception as exc:
        print(f"Fehler während CI-PostgreSQL-Start: {exc}", file=sys.stderr)
        # Kontrollierten Teardown NUR für den soeben autorisierten aktuellen Lauf versuchen
        try:
            stop()
        except Exception as stop_exc:
            print(
                f"Zusätzlicher Fehler beim Teardown nach Start-Abbruch: {stop_exc}",
                file=sys.stderr,
            )
        raise


def stop() -> None:
    """Stoppt und entfernt den CI-Container mit fail-closed Autorisierung."""
    current_token = get_current_invocation_token()

    meta = _read_meta()
    if meta is None:
        if STATE.exists():
            raise CIPostgresError(
                f"Teardown verweigert: {STATE} existiert, aber keine gültige CI-Metadaten-Datei "
                f"{META_FILE}. Fremde Instanz geschützt."
            )
        print("Kein CI-Zustand vorhanden. Teardown nicht erforderlich.")
        return

    name = meta["container_name"]
    stored_token = meta["owner_token"]
    stored_id = meta.get("container_id", "")

    # STRIKTE AUTORISIERUNG:
    # Die aktuelle Invocation darf NUR löschen, wenn das übergebene Invocation-Token
    # exakt mit dem in den Metadaten gespeicherten Token übereinstimmt!
    if current_token != stored_token:
        raise CIPostgresError(
            "Teardown verweigert: Aktuelles Invocation-Token stimmt nicht mit "
            "Besitzer-Token überein. Ressourcen eines anderen oder älteren Laufs "
            "dürfen nicht gelöscht werden!"
        )

    if not name.startswith(CONTAINER_PREFIX):
        raise CIPostgresError(
            f"Teardown verweigert: Containername '{name}' entspricht nicht dem CI-Namenspräfix."
        )

    # 1. Existenz und Eigentümerschaft am Docker-Dämon verifizieren
    exists, status, labels, full_id = _check_container_exists(name)
    if exists:
        # Labels validieren
        if (
            labels.get("syllentra.ci") != "true"
            or labels.get("syllentra.owner_token") != current_token
        ):
            raise CIPostgresError(
                f"Teardown verweigert: Container '{name}' besitzt nicht passende Eigentums-Labels."
            )

        # Falls eine Container-ID hinterlegt war, muss sie übereinstimmen
        if (
            stored_id
            and full_id
            and not full_id.startswith(stored_id)
            and not stored_id.startswith(full_id)
        ):
            raise CIPostgresError(
                f"Teardown verweigert: Container-ID '{full_id}' weicht von gespeicherter ID ab."
            )

        # 2. Container stoppen
        stop_res = _run_docker(["stop", "--time", "5", name], timeout=15.0)

        # 3. Container entfernen
        rm_res = _run_docker(["rm", "--force", name], timeout=15.0)

        # 4. Abwesenheit nachweislich verifizieren
        post_exists, post_status, _, _ = _check_container_exists(name)
        if post_exists:
            # Container ist IMMER NOCH da -> FAIL CLOSED!
            # Metadaten MÜSSEN für Recovery erhalten bleiben!
            clean_err = _sanitize_output(f"{stop_res.stderr} {rm_res.stderr}", current_token)
            raise CIPostgresError(
                f"Container-Cleanup fehlgeschlagen: Container '{name}' existiert weiterhin "
                f"(Status: {post_status}). Fehlerausgabe: {clean_err}"
            )

        print(f"CI-Container nachweislich entfernt: {name}")
    else:
        print(f"CI-Container '{name}' existiert nicht mehr (bereits abwesend).")

    # 5. Erst NACH nachgewiesener Abwesenheit Zustandsdateien aufräumen
    # Reihenfolge: zuerst database.json, dann META_FILE
    # Fehler beim Löschen müssen als echter Fehler gemeldet werden!
    if STATE.exists():
        try:
            STATE.unlink()
        except OSError as e:
            raise CIPostgresError(
                f"Cleanup unvollständig: Konnte {STATE} nicht löschen: {e}"
            ) from e

    if META_FILE.exists():
        try:
            META_FILE.unlink()
        except OSError as e:
            raise CIPostgresError(
                f"Cleanup unvollständig: Konnte {META_FILE} nicht löschen: {e}"
            ) from e


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
