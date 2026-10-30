"""Regressionstests für ci_test_db.py ohne Docker-Daemon.

Prüft alle Fehlerpfade, Timeouts, Fail-Closed-Verhalten, Eigentumsbindungen
und Schutzmechanismen für fremde Dateien und Container ausschließlich über Mocks.
"""

import json
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from scripts import ci_test_db
from scripts.ci_test_db import CIPostgresError


@pytest.fixture()
def mock_ci_env(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Isoliert ROOT, STATE und META_FILE in ein temporäres Verzeichnis."""
    local_dir = tmp_path / ".local"
    local_dir.mkdir(mode=0o700, exist_ok=True)
    state_file = local_dir / "database.json"
    meta_file = local_dir / ".ci_pg_meta.json"

    monkeypatch.setattr(ci_test_db, "ROOT", tmp_path)
    monkeypatch.setattr(ci_test_db, "STATE", state_file)
    monkeypatch.setattr(ci_test_db, "META_FILE", meta_file)

    return tmp_path


def _make_completed(returncode: int = 0, stdout: str = "", stderr: str = "") -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(args=["docker"], returncode=returncode, stdout=stdout, stderr=stderr)


# 1. Erfolgreicher Start und vollständiger Cleanup
def test_successful_start_and_stop(mock_ci_env: Path) -> None:
    token_captured = []

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            # Extract owner_token from label
            for a in args:
                if a.startswith("syllentra.owner_token="):
                    token_captured.append(a.split("=")[1])
            return _make_completed(0, "container-id-123\n")
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(0)
        if args[0] == "exec" and "psql" in args:
            return _make_completed(0)
        if args[0] == "inspect":
            t = token_captured[0]
            labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": t})
            return _make_completed(0, f"{labels}|running\n")
        if args[0] == "stop":
            return _make_completed(0)
        if args[0] == "rm":
            return _make_completed(0)
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run) as mock_docker:
        ci_test_db.start()
        assert ci_test_db.STATE.exists()
        assert ci_test_db.META_FILE.exists()

        # Stop ausführen
        # Bei zweiter inspect-Abfrage (nach rm) soll not_found kommen
        inspect_count = 0

        def fake_run_stop(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
            nonlocal inspect_count
            if args[0] == "inspect":
                inspect_count += 1
                if inspect_count == 1:
                    t = token_captured[0]
                    labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": t})
                    return _make_completed(0, f"{labels}|running\n")
                return _make_completed(1, stderr="Error: No such container")
            return _make_completed(0)

        mock_docker.side_effect = fake_run_stop
        ci_test_db.stop()

        assert not ci_test_db.STATE.exists()
        assert not ci_test_db.META_FILE.exists()


# 2. Fehler bei docker run
def test_docker_run_failure(mock_ci_env: Path) -> None:
    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            return _make_completed(1, stderr="port is already allocated")
        if args[0] == "inspect":
            return _make_completed(1, stderr="No such container")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="docker run fehlgeschlagen"):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()
        assert not ci_test_db.META_FILE.exists()


# 3. PostgreSQL Healthcheck Timeout
def test_healthcheck_timeout(mock_ci_env: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ci_test_db, "READY_TIMEOUT", 0.1)
    monkeypatch.setattr(ci_test_db, "READY_INTERVAL", 0.01)

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            return _make_completed(0)
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(1, stderr="rejecting connections")
        if args[0] == "inspect":
            return _make_completed(1, stderr="No such container")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="nicht innerhalb von .* bereit"):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()


# 4. Fehler bei Rolleninitialisierung
def test_role_initialization_failure(mock_ci_env: Path) -> None:
    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            return _make_completed(0)
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(0)
        if args[0] == "exec" and "psql" in args:
            return _make_completed(1, stderr="syntax error in SQL")
        if args[0] == "inspect":
            return _make_completed(1, stderr="No such container")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Rolleninitialisierung fehlgeschlagen"):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()


# 5 & 6. docker stop schlägt fehl, aber rm gelingt / rm schlägt fehl (Fail-Closed)
def test_stop_fails_but_rm_fails_container_still_exists(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-test01", "owner_token": "token123"}))
    ci_test_db.STATE.write_text("{}")

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": "token123"})
            return _make_completed(0, f"{labels}|running\n")
        if args[0] == "stop":
            return _make_completed(1, stderr="stop timeout")
        if args[0] == "rm":
            return _make_completed(1, stderr="cannot remove container: in use")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Container-Cleanup fehlgeschlagen: Container .* existiert weiterhin"):
            ci_test_db.stop()

        # Metadaten und State MÜSSEN für Recovery erhalten bleiben!
        assert ci_test_db.META_FILE.exists()
        assert ci_test_db.STATE.exists()


# 7. Docker Daemon nicht erreichbar
def test_docker_daemon_unreachable(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-test01", "owner_token": "token123"}))

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        return _make_completed(1, stderr="Cannot connect to the Docker daemon at unix:///var/run/docker.sock")

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Docker-Daemon nicht erreichbar"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 8. docker inspect scheitert an Permission Denied
def test_docker_permission_denied(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-test01", "owner_token": "token123"}))

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        return _make_completed(1, stderr="permission denied while trying to connect to the Docker daemon socket")

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Docker-Zugriff verweigert"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 9. Nachweislich nicht vorhandener Container
def test_container_already_gone(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-test01", "owner_token": "token123"}))
    ci_test_db.STATE.write_text("{}")

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            return _make_completed(1, stderr="Error: No such container: syllentra-ci-pg-test01")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        ci_test_db.stop()
        assert not ci_test_db.META_FILE.exists()
        assert not ci_test_db.STATE.exists()


# 10 & 11. Container mit falschem Label oder falschem Owner-Token
def test_container_with_wrong_owner_or_label(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-test01", "owner_token": "token-a"}))

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            # Token stimmt NICHT überein!
            labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": "token-b"})
            return _make_completed(0, f"{labels}|running\n")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run) as mock_docker:
        with pytest.raises(CIPostgresError, match="Teardown verweigert: Container .* besitzt nicht die erforderlichen Eigentums-Labels"):
            ci_test_db.stop()

        # Sicherstellen, dass kein stop oder rm auf fremdem Container ausgeführt wurde!
        called_cmds = [call[0][0][0] for call in mock_docker.call_args_list]
        assert "stop" not in called_cmds
        assert "rm" not in called_cmds
        assert ci_test_db.META_FILE.exists()


# 12 & 13. Start verweigert wegen vorhandener fremder Marker- oder Konfigurationsdatei
def test_start_refused_when_files_exist(mock_ci_env: Path) -> None:
    ci_test_db.STATE.write_text("{\"fremd\": true}")
    with pytest.raises(CIPostgresError, match="Start verweigert: .* existiert bereits"):
        ci_test_db.start()

    ci_test_db.STATE.unlink()
    ci_test_db.META_FILE.write_text("{\"fremd\": true}")
    with pytest.raises(CIPostgresError, match="Start verweigert: .* existiert bereits"):
        ci_test_db.start()


# 14. Nachfolgender Teardown nach verweigertem Start schützt fremden Zustand
def test_teardown_after_refused_start_protects_foreign_state(mock_ci_env: Path) -> None:
    # Nur STATE existiert (z.B. von einem lokalen Entwicklungslauf), keine CI-Metadaten
    ci_test_db.STATE.write_text("{\"important\": \"local_dev\"}")

    with patch.object(ci_test_db, "_run_docker") as mock_docker:
        with pytest.raises(CIPostgresError, match="Teardown verweigert: .* Fremde Instanz geschützt"):
            ci_test_db.stop()

        assert ci_test_db.STATE.exists()
        assert ci_test_db.STATE.read_text() == "{\"important\": \"local_dev\"}"
        mock_docker.assert_not_called()


# 15. Partiell gestarteter Container wird bei Startfehler aufgeräumt
def test_partial_start_error_attempts_cleanup(mock_ci_env: Path) -> None:
    # docker run gelingt, aber psql schlägt fehl -> sauberer Teardown
    inspect_calls = 0

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        nonlocal inspect_calls
        if args[0] == "run":
            return _make_completed(0)
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(0)
        if args[0] == "exec" and "psql" in args:
            return _make_completed(1, stderr="fatal error")
        if args[0] == "inspect":
            inspect_calls += 1
            if inspect_calls == 1:
                meta = json.loads(ci_test_db.META_FILE.read_text())
                labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": meta["owner_token"]})
                return _make_completed(0, f"{labels}|running\n")
            return _make_completed(1, stderr="No such container")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="PostgreSQL-Rolleninitialisierung fehlgeschlagen"):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()
        assert not ci_test_db.META_FILE.exists()


# 16. Wiederholter Cleanup und idempotentes Verhalten
def test_idempotent_cleanup_when_no_state(mock_ci_env: Path) -> None:
    # Weder META_FILE noch STATE existieren
    with patch.object(ci_test_db, "_run_docker") as mock_docker:
        ci_test_db.stop()
        mock_docker.assert_not_called()


# 17. Timeout eines Docker-Befehls
def test_docker_command_timeout(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-test01", "owner_token": "token123"}))

    def fake_subprocess_run(cmd: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        raise subprocess.TimeoutExpired(cmd=cmd, timeout=15.0)

    with patch("subprocess.run", side_effect=fake_subprocess_run):
        with pytest.raises(CIPostgresError, match="Docker-Befehl lief in Timeout"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 18. Schutz und Erhalt der Wiederherstellungsinformationen bei Cleanup-Fehlern
def test_recovery_info_preserved_on_cleanup_failure(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(json.dumps({"container_name": "syllentra-ci-pg-fail01", "owner_token": "secret_token_1"}))
    ci_test_db.STATE.write_text("{\"runtime_url\": \"sensitive\"}")

    def fake_run(args: list[str], timeout: float = 15.0, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": "secret_token_1"})
            return _make_completed(0, f"{labels}|running\n")
        if args[0] == "rm":
            return _make_completed(1, stderr="device or resource busy")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Container-Cleanup fehlgeschlagen"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()
        assert ci_test_db.STATE.exists()
