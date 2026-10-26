"""Isolation der Testläufe und Grenzen zwischen Test- und Normalumgebung (Mission 12/27/27B)."""

import os
import secrets
import subprocess  # noqa: S404 -- feste Argumentliste, nur eigener pytest-Prozess
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any

import psycopg
import pytest
from helpers import account
from psycopg import sql

from scripts.migrate import urls
from scripts.test_db import (
    RUN_NAME,
    OwnershipError,
    RunDatabase,
    _same_owner,
    assert_owned,
    create_run_database,
    drop_run_database,
    sweep,
    wipe,
)
from syllentra_backend.delivery import MemoryChannel
from syllentra_backend.identity import SESSION, LocalIdentity

BACKEND = Path(__file__).resolve().parents[1]
INSERT_ACCOUNT = (
    "INSERT INTO accounts (id,login,password_hash,kind,verification,status) "
    "VALUES (gen_random_uuid(), %s, 'x', 'user', 'pending', 'active')"
)


def count_accounts(url: str) -> int:
    with psycopg.connect(url) as db:
        row = db.execute("SELECT count(*) FROM accounts").fetchone()
        assert row
        return int(row[0])


def test_run_database_is_unique_and_owned(run_db: RunDatabase) -> None:
    assert RUN_NAME.fullmatch(run_db.name)
    assert_owned(run_db, run_db.admin_url)
    assert_owned(run_db, run_db.runtime_url)
    with psycopg.connect(run_db.runtime_url) as db:
        row = db.execute("SELECT current_database(), current_user").fetchone()
        assert row == (run_db.name, "syllentra_runtime")


def test_two_runs_do_not_share_data_and_wipe_only_hits_its_own_database(
    run_db: RunDatabase,
) -> None:
    other = create_run_database()
    try:
        assert other.name != run_db.name
        for target in (run_db, other):
            with psycopg.connect(target.admin_url) as db:
                db.execute(INSERT_ACCOUNT, ("a@example.test",))
        wipe(run_db)
        assert count_accounts(run_db.admin_url) == 0
        assert count_accounts(other.admin_url) == 1
    finally:
        drop_run_database(other)


def test_destructive_operations_refuse_unverified_databases(run_db: RunDatabase) -> None:
    decoy = create_run_database()
    try:
        with psycopg.connect(decoy.admin_url) as db:
            db.execute(INSERT_ACCOUNT, ("keep@example.test",))
        forged_comment = replace(decoy, comment="syllentra-test-run:v1:forged:0:forged")
        shared = replace(decoy, name="syllentra_test")
        system = replace(decoy, name="postgres")
        for forged in (forged_comment, shared, system):
            with pytest.raises(OwnershipError):
                assert_owned(forged)
            with pytest.raises(OwnershipError):
                wipe(forged)
            with pytest.raises(OwnershipError):
                drop_run_database(forged)
        with pytest.raises(OwnershipError):  # Verbindung zeigt auf eine andere Datenbank
            assert_owned(run_db, decoy.admin_url)
        assert count_accounts(decoy.admin_url) == 1  # nichts wurde angetastet
    finally:
        drop_run_database(decoy)


def test_database_name_allowlist_for_scripts() -> None:
    bad_names = [
        "postgres",
        "syllentra_prod",
        "syllentra_t_ABCDEF123456",
        "syllentra_t_abc",
        'x";--',
    ]
    for bad in bad_names:
        with pytest.raises(ValueError, match="Datenbankname"):
            urls(database=bad)
    assert urls(database="syllentra_t_0123456789ab")[0].endswith("/syllentra_t_0123456789ab")
    assert urls(test=True)[0].endswith("/syllentra_test")  # ausschließlich Browserprüfungen


def test_sweep_lists_only_marked_old_databases() -> None:
    decoy = create_run_database()
    unmarked = "syllentra_t_" + secrets.token_hex(6)
    try:
        with psycopg.connect(decoy.maintenance_url, autocommit=True) as db:
            db.execute(f'CREATE DATABASE "{unmarked}" TEMPLATE template0')  # noqa: S608
        # Solange decoy aktiv ist, schützt der Besitz-Lock die Datenbank:
        assert decoy.name not in sweep(0, apply=False)
        # Wenn der Besitzerprozess endet (Verbindung schließt), wird sie als verwaist erkannt:
        if decoy.lock_conn and not decoy.lock_conn.closed:
            decoy.lock_conn.close()
        assert decoy.name not in sweep(1, apply=False)  # frisch (< 1 Stunde)
        listed = sweep(0, apply=False)
        assert decoy.name in listed
        assert unmarked not in listed  # ohne Eigentumsvermerk: niemals anfassen
    finally:
        with psycopg.connect(decoy.maintenance_url, autocommit=True) as db:
            db.execute(sql.SQL('DROP DATABASE IF EXISTS {}').format(sql.Identifier(unmarked)))
        drop_run_database(decoy)


def test_identity_mode_accepts_only_local_allowlisted_databases(run_db: RunDatabase) -> None:
    config = LocalIdentity(secrets.token_bytes(32), MemoryChannel(), MemoryChannel())
    config.validate(run_db.runtime_url)
    host = "127.0.0.1:55439"
    for bad in [
        f"postgresql://u:p@{host}/postgres",
        f"postgresql://u:p@{host}/syllentra_t_xyz",
        f"postgresql://u:p@{host}/syllentra_t_0123456789abc",
        "postgresql://u:p@127.0.0.1:5432/syllentra_t_0123456789ab",
        "postgresql://u:p@db.example.com:55439/syllentra_t_0123456789ab",
        f"postgresql://u:p@{host}/syllentra_t_0123456789ab?host=evil",
    ]:
        with pytest.raises(ValueError, match="Identitätsprobe"):
            config.validate(bad)


def test_backend_tests_never_touch_shared_browser_database() -> None:
    forbidden = ("urls(test=True)", "syllentra_test")
    here = {Path(__file__).name, "conftest.py"}
    for path in (BACKEND / "tests").glob("*.py"):
        if path.name in here:
            continue
        text = path.read_text(encoding="utf-8")
        assert not any(token in text for token in forbidden), path.name


def test_external_wipe_makes_session_reads_fail_mechanism(env: Any) -> None:
    """Mechanismus (nicht Ursache des Altvorfalls): fremdes DELETE => 401 direkt nach Login."""
    c = env["browser"]()
    account(env, c)
    assert c.get("/session").status_code == 200
    wipe(env["run"])  # simuliert eine andere Suite, die dieselbe Datenbank leert
    assert c.get("/session").status_code == 401
    assert c.cookies.get(SESSION)  # Cookie unverändert vorhanden, Zeile fehlt serverseitig


@pytest.mark.skipif(os.environ.get("SYLLENTRA_NESTED") == "1", reason="keine Rekursion")
def test_two_pytest_processes_run_in_parallel_without_interference() -> None:
    selection = "two_proof_recovery or concurrent_otp or multiple_sessions or parallel_session"
    command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "-k", selection]
    environment = dict(os.environ, SYLLENTRA_NESTED="1")
    target = "tests/test_identity.py"
    procs = [
        subprocess.Popen(  # noqa: S603
            [*command, target],
            cwd=BACKEND,
            env=environment,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        for _ in range(2)
    ]
    outputs = [p.communicate(timeout=900)[0] for p in procs]
    assert [p.returncode for p in procs] == [0, 0], "\n".join(outputs)
    assert all("passed" in o and "failed" not in o for o in outputs)


def test_same_owner_validates_both_markers_and_rejects_malformed_or_divergent() -> None:
    name = "syllentra_t_0123456789ab"
    valid = "syllentra-test-run:v1:0123456789ab:1000:" + "a" * 32
    valid_diff_gen = "syllentra-test-run:v1:0123456789ab:2000:" + "a" * 32
    valid_diff_token = "syllentra-test-run:v1:0123456789ab:1000:" + "b" * 32

    # Gültiger identischer Vermerk
    assert _same_owner(name, valid, valid) is True

    # Malformierte Marker werden selbst bei Identität abgewiesen
    assert _same_owner(name, "forged", "forged") is False
    assert _same_owner(name, "syllentra-test-run:v1:x:0:y", "syllentra-test-run:v1:x:0:y") is False
    assert _same_owner(name, None, valid) is False
    assert _same_owner(name, valid, "") is False

    # Abweichende Generation oder abweichender Token wird sicher abgewiesen
    assert _same_owner(name, valid_diff_gen, valid) is False
    assert _same_owner(name, valid_diff_token, valid) is False


def test_sweep_rejects_invalid_negative_or_non_finite_hours() -> None:
    for invalid in [-1, -0.0001, float("nan"), float("inf"), float("-inf"), True, False, "1"]:
        with pytest.raises(ValueError, match="Stundenwert"):
            sweep(invalid, apply=False)  # type: ignore[arg-type]


def test_active_run_without_open_connections_is_protected_at_zero_threshold(
    run_db: RunDatabase,
) -> None:
    # Der Besitz-Lock auf lock_conn schützt die Datenbank selbst bei 0 offenen Runtime-Verbindungen
    # und Schwellenwert 0 Stunden:
    listed = sweep(0, apply=False)
    assert run_db.name not in listed
    # Auch ein sweep --apply berührt den aktiven Run niemals:
    swept = sweep(0, apply=True)
    assert run_db.name not in swept
    assert_owned(run_db)


def test_loss_of_possession_lock_fails_closed(run_db: RunDatabase) -> None:
    decoy = create_run_database()
    try:
        assert_owned(decoy)
        # Wenn der Besitz-Lock verloren geht (z. B. Verbindungsabbruch):
        if decoy.lock_conn:
            decoy.lock_conn.close()
        with pytest.raises(OwnershipError, match="Besitz-Verbindung"):
            assert_owned(decoy)
        with pytest.raises(OwnershipError, match="Besitz-Verbindung"):
            wipe(decoy)
    finally:
        drop_run_database(decoy)


def test_drop_refuses_actively_used_database(run_db: RunDatabase) -> None:
    decoy = create_run_database()
    try:
        with psycopg.connect(decoy.runtime_url) as conn:
            conn.execute("SELECT 1")
            with pytest.raises(OwnershipError, match="aktiv verwendet"):
                drop_run_database(decoy)
    finally:
        drop_run_database(decoy)
