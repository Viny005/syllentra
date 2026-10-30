"""Regressionstests für ci_test_db.py ohne Docker-Daemon.

Prüft alle Fehlerpfade, Timeouts, Fail-Closed-Verhalten, Eigentumsbindungen
und Schutzmechanismen für fremde Dateien und Container ausschließlich über Mocks.
"""

import json
import os
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from scripts import ci_test_db
from scripts.ci_test_db import CIPostgresError

DEFAULT_TEST_TOKEN = "test_invocation_token_1234567890"


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
    monkeypatch.setenv(ci_test_db.ENV_TOKEN_KEY, DEFAULT_TEST_TOKEN)

    return tmp_path


def _make_completed(
    returncode: int = 0, stdout: str = "", stderr: str = ""
) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess(
        args=["docker"], returncode=returncode, stdout=stdout, stderr=stderr
    )


# 1. Erfolgreicher Start und vollständiger Cleanup
def test_successful_start_and_stop(mock_ci_env: Path) -> None:
    token_captured = []
    created_container_name = []

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            for a in args:
                if a.startswith("syllentra.owner_token="):
                    token_captured.append(a.split("=")[1])
            # Container-Name merken
            idx = args.index("--name")
            created_container_name.append(args[idx + 1])
            return _make_completed(0, "container-id-123\n")
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(0)
        if args[0] == "exec" and "psql" in args:
            return _make_completed(0)
        if args[0] == "inspect":
            t = token_captured[0]
            labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": t})
            return _make_completed(0, f"container-id-123|{labels}|running\n")
        if args[0] == "stop":
            return _make_completed(0)
        if args[0] == "rm":
            return _make_completed(0)
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run) as mock_docker:
        ci_test_db.start()
        assert ci_test_db.STATE.exists()
        assert ci_test_db.META_FILE.exists()

        inspect_count = 0
        c_name = created_container_name[0]

        def fake_run_stop(
            args: list[str],
            timeout: float = 15.0,
            input_text: str | None = None,
            env: dict[str, str] | None = None,
        ) -> subprocess.CompletedProcess[str]:
            nonlocal inspect_count
            if args[0] == "inspect":
                inspect_count += 1
                if inspect_count == 1:
                    t = token_captured[0]
                    labels = json.dumps({"syllentra.ci": "true", "syllentra.owner_token": t})
                    return _make_completed(0, f"container-id-123|{labels}|running\n")
                return _make_completed(1, stderr=f"Error: No such container: {c_name}")
            return _make_completed(0)

        mock_docker.side_effect = fake_run_stop
        ci_test_db.stop()

        assert not ci_test_db.STATE.exists()
        assert not ci_test_db.META_FILE.exists()


# 2. Fehlendes oder unzureichendes Invocation-Token
def test_missing_or_invalid_invocation_token(
    mock_ci_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv(ci_test_db.ENV_TOKEN_KEY, raising=False)
    with pytest.raises(CIPostgresError, match="Ungültiges oder fehlendes Invocation-Token"):
        ci_test_db.get_current_invocation_token()

    monkeypatch.setenv(ci_test_db.ENV_TOKEN_KEY, "short_tok")
    with pytest.raises(CIPostgresError, match="Ungültiges oder fehlendes Invocation-Token"):
        ci_test_db.get_current_invocation_token()


# 3. Fehler bei docker run
def test_docker_run_failure(mock_ci_env: Path) -> None:
    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            return _make_completed(1, stderr="port is already allocated")
        if args[0] == "inspect":
            name = args[-1]
            return _make_completed(1, stderr=f"Error: No such container: {name}")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="docker run fehlgeschlagen"):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()
        assert not ci_test_db.META_FILE.exists()


# 4. PostgreSQL Healthcheck Timeout
def test_healthcheck_timeout(mock_ci_env: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(ci_test_db, "READY_TIMEOUT", 0.1)
    monkeypatch.setattr(ci_test_db, "READY_INTERVAL", 0.01)

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            return _make_completed(0, "container-id-123\n")
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(1, stderr="rejecting connections")
        if args[0] == "inspect":
            name = args[-1]
            return _make_completed(1, stderr=f"Error: No such container: {name}")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="nicht innerhalb von .* bereit"):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()


# 5. Fehler bei Rolleninitialisierung
def test_role_initialization_failure(mock_ci_env: Path) -> None:
    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "run":
            return _make_completed(0, "container-id-123\n")
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(0)
        if args[0] == "exec" and "psql" in args:
            return _make_completed(1, stderr="syntax error in SQL")
        if args[0] == "inspect":
            name = args[-1]
            return _make_completed(1, stderr=f"Error: No such container: {name}")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(
            CIPostgresError, match="PostgreSQL-Rolleninitialisierung fehlgeschlagen"
        ):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()


# 6. Container existiert nach rm weiterhin (Fail-Closed)
def test_stop_fails_container_still_exists(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )
    ci_test_db.STATE.write_text("{}")

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            labels = json.dumps(
                {"syllentra.ci": "true", "syllentra.owner_token": DEFAULT_TEST_TOKEN}
            )
            return _make_completed(0, f"container-id-test01|{labels}|running\n")
        if args[0] == "stop":
            return _make_completed(1, stderr="stop timeout")
        if args[0] == "rm":
            return _make_completed(1, stderr="cannot remove container: in use")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(
            CIPostgresError,
            match="Container-Cleanup fehlgeschlagen: Container .* existiert weiterhin",
        ):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()
        assert ci_test_db.STATE.exists()


# 7. Docker Daemon nicht erreichbar
def test_docker_daemon_unreachable(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return _make_completed(
            1, stderr="Cannot connect to the Docker daemon at unix:///var/run/docker.sock"
        )

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Docker-Daemon nicht erreichbar"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 8. docker inspect scheitert an Permission Denied
def test_docker_permission_denied(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return _make_completed(
            1, stderr="permission denied while trying to connect to the Docker daemon socket"
        )

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Docker-Zugriff verweigert"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 9. Nachweislich nicht vorhandener Container
def test_container_already_gone(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )
    ci_test_db.STATE.write_text("{}")

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            return _make_completed(1, stderr="Error: No such container: syllentra-ci-pg-test01")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        ci_test_db.stop()
        assert not ci_test_db.META_FILE.exists()
        assert not ci_test_db.STATE.exists()


# 10. Container mit falschem Docker-Label
def test_container_with_wrong_label(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            labels = json.dumps(
                {"syllentra.ci": "true", "syllentra.owner_token": "different_token_1234"}
            )
            return _make_completed(0, f"container-id-test01|{labels}|running\n")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run) as mock_docker:
        with pytest.raises(
            CIPostgresError,
            match="Teardown verweigert: Container .* besitzt nicht passende Eigentums-Labels",
        ):
            ci_test_db.stop()

        called_cmds = [call[0][0][0] for call in mock_docker.call_args_list]
        assert "stop" not in called_cmds
        assert "rm" not in called_cmds
        assert ci_test_db.META_FILE.exists()


# 11. Start verweigert wegen vorhandener fremder Dateien
def test_start_refused_when_files_exist(mock_ci_env: Path) -> None:
    ci_test_db.STATE.write_text('{"fremd": true}')
    with pytest.raises(CIPostgresError, match="Start verweigert: .* existiert bereits"):
        ci_test_db.start()

    ci_test_db.STATE.unlink()
    ci_test_db.META_FILE.write_text('{"fremd": true}')
    with pytest.raises(CIPostgresError, match="Start verweigert: .* existiert bereits"):
        ci_test_db.start()


# 12. Teardown nach verweigertem Start schützt fremden Zustand
def test_teardown_after_refused_start_protects_foreign_state(mock_ci_env: Path) -> None:
    ci_test_db.STATE.write_text('{"important": "local_dev"}')

    with patch.object(ci_test_db, "_run_docker") as mock_docker:
        with pytest.raises(
            CIPostgresError, match="Teardown verweigert: .* Fremde Instanz geschützt"
        ):
            ci_test_db.stop()

        assert ci_test_db.STATE.exists()
        assert ci_test_db.STATE.read_text() == '{"important": "local_dev"}'
        mock_docker.assert_not_called()


# 13. Teardown verweigert bei Token-Mismatch (Mission-45-Kernanforderung)
def test_teardown_refused_when_token_mismatch_with_meta(
    mock_ci_env: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    # Metadaten gehören einem früheren / anderen Lauf
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-foreign99",
                "owner_token": "foreign_run_token_abcdef123456",
                "container_id": "foreign-id-99",
            }
        )
    )
    ci_test_db.STATE.write_text('{"db": "foreign"}')

    # Aktueller Lauf hat ein anderes Token
    monkeypatch.setenv(ci_test_db.ENV_TOKEN_KEY, "current_run_token_987654321012")

    with patch.object(ci_test_db, "_run_docker") as mock_docker:
        with pytest.raises(
            CIPostgresError,
            match="Teardown verweigert: Aktuelles Invocation-Token stimmt nicht mit Besitzer-Token",
        ):
            ci_test_db.stop()

        # Weder docker stop noch docker rm dürfen aufgerufen werden
        mock_docker.assert_not_called()
        # Dateien bleiben zum Schutz der fremden Ressource erhalten
        assert ci_test_db.META_FILE.exists()
        assert ci_test_db.STATE.exists()


# 14. Teardown verweigert bei Mismatch der Container-ID
def test_teardown_refused_when_container_id_mismatch(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "saved-container-id-aaa",
            }
        )
    )

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            labels = json.dumps(
                {"syllentra.ci": "true", "syllentra.owner_token": DEFAULT_TEST_TOKEN}
            )
            # Dämon meldet andere ID
            return _make_completed(0, f"different-id-bbb|{labels}|running\n")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run) as mock_docker:
        with pytest.raises(
            CIPostgresError,
            match="Teardown verweigert: Container-ID .* weicht von gespeicherter ID ab",
        ):
            ci_test_db.stop()

        called_cmds = [call[0][0][0] for call in mock_docker.call_args_list]
        assert "stop" not in called_cmds
        assert "rm" not in called_cmds
        assert ci_test_db.META_FILE.exists()


# 15. Partiell gestarteter Container wird bei Startfehler aufgeräumt
def test_partial_start_error_attempts_cleanup(mock_ci_env: Path) -> None:
    inspect_calls = 0

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        nonlocal inspect_calls
        if args[0] == "run":
            return _make_completed(0, "container-id-partial123\n")
        if args[0] == "exec" and "pg_isready" in args:
            return _make_completed(0)
        if args[0] == "exec" and "psql" in args:
            return _make_completed(1, stderr="fatal sql error")
        if args[0] == "inspect":
            inspect_calls += 1
            if inspect_calls == 1:
                labels = json.dumps(
                    {"syllentra.ci": "true", "syllentra.owner_token": DEFAULT_TEST_TOKEN}
                )
                return _make_completed(0, f"container-id-partial123|{labels}|running\n")
            name = args[-1]
            return _make_completed(1, stderr=f"Error: No such container: {name}")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(
            CIPostgresError, match="PostgreSQL-Rolleninitialisierung fehlgeschlagen"
        ):
            ci_test_db.start()

        assert not ci_test_db.STATE.exists()
        assert not ci_test_db.META_FILE.exists()


# 16. Wiederholter Cleanup und idempotentes Verhalten bei fehlendem State
def test_idempotent_cleanup_when_no_state(mock_ci_env: Path) -> None:
    with patch.object(ci_test_db, "_run_docker") as mock_docker:
        ci_test_db.stop()
        mock_docker.assert_not_called()


# 17. Timeout eines Docker-Befehls
def test_docker_command_timeout(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )

    def fake_subprocess_run(cmd: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
        raise subprocess.TimeoutExpired(cmd=cmd, timeout=15.0)

    with patch("subprocess.run", side_effect=fake_subprocess_run):
        with pytest.raises(CIPostgresError, match="Docker-Befehl lief in Timeout"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 18. Schutz und Erhalt der Wiederherstellungsinformationen bei Cleanup-Fehlern
def test_recovery_info_preserved_on_cleanup_failure(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-fail01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-fail01",
            }
        )
    )
    ci_test_db.STATE.write_text('{"runtime_url": "sensitive"}')

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            labels = json.dumps(
                {"syllentra.ci": "true", "syllentra.owner_token": DEFAULT_TEST_TOKEN}
            )
            return _make_completed(0, f"container-id-fail01|{labels}|running\n")
        if args[0] == "rm":
            return _make_completed(1, stderr="device or resource busy")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(CIPostgresError, match="Container-Cleanup fehlgeschlagen"):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()
        assert ci_test_db.STATE.exists()


# 19. Beschädigte oder unvollständige Metadatendatei verweigert Teardown
def test_corrupt_or_incomplete_metadata_refuses_teardown(mock_ci_env: Path) -> None:
    # Fall A: Leere Datei
    ci_test_db.META_FILE.write_text("")
    with pytest.raises(CIPostgresError, match="Metadatendatei .* ist leer oder beschädigt"):
        ci_test_db.stop()

    # Fall B: Ungültiges JSON
    ci_test_db.META_FILE.write_text("{bad json...")
    with pytest.raises(CIPostgresError, match="Metadatendatei .* ist kein gültiges JSON"):
        ci_test_db.stop()

    # Fall C: Fehlende Pflichtfelder (z.B. container_id fehlt)
    ci_test_db.META_FILE.write_text(
        json.dumps({"container_name": "syllentra-ci-pg-01", "owner_token": DEFAULT_TEST_TOKEN})
    )
    with pytest.raises(CIPostgresError, match="Metadatendatei .* enthält unvollständige Felder"):
        ci_test_db.stop()


# 20. Mehrdeutiger Docker-Fehler wird als fail-closed behandelt (nicht als Abwesenheit)
def test_ambiguous_docker_error_treated_as_fail_closed(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            # Unspezifischer Fehler mit 'not found', aber kein No such container: <name>
            return _make_completed(1, stderr="Error response: default network bridge not found")
        if args[0] == "ps":
            # docker ps schlägt ebenfalls fehl
            return _make_completed(1, stderr="communication error")
        return _make_completed(0)

    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with pytest.raises(
            CIPostgresError, match="Unerwarteter Fehler bei Überprüfung von Container"
        ):
            ci_test_db.stop()

        assert ci_test_db.META_FILE.exists()


# 21. Dateilöschfehler bei database.json oder .ci_pg_meta.json wirft Fehler (Fail-Closed)
def test_state_or_meta_unlink_failure_raises_error(mock_ci_env: Path) -> None:
    ci_test_db.META_FILE.write_text(
        json.dumps(
            {
                "container_name": "syllentra-ci-pg-test01",
                "owner_token": DEFAULT_TEST_TOKEN,
                "container_id": "container-id-test01",
            }
        )
    )
    ci_test_db.STATE.write_text("{}")

    def fake_run(
        args: list[str],
        timeout: float = 15.0,
        input_text: str | None = None,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        if args[0] == "inspect":
            return _make_completed(1, stderr="Error: No such container: syllentra-ci-pg-test01")
        return _make_completed(0)

    # Test A: STATE unlink schlägt fehl
    with patch.object(ci_test_db, "_run_docker", side_effect=fake_run):
        with patch.object(Path, "unlink", side_effect=OSError("Disk write protected")):
            with pytest.raises(CIPostgresError, match="Cleanup unvollständig: Konnte .* nicht"):
                ci_test_db.stop()


# 22. Sanitization von Passwörtern und Token in Fehlerausgaben
def test_secrets_sanitization() -> None:
    secret_pass = "super_secret_db_password_123"
    secret_token = "secret_invocation_token_xyz"
    raw_error = (
        f"FATAL: password authentication failed for user '{secret_pass}' with {secret_token}"
    )

    sanitized = ci_test_db._sanitize_output(raw_error, secret_pass, secret_token)
    assert secret_pass not in sanitized
    assert secret_token not in sanitized
    assert "[REDACTED]" in sanitized
