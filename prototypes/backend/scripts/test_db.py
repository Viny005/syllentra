"""Isolierte PostgreSQL-Testdatenbanken pro Testlauf (Mission 12/27/27B/27C/27D).

Jeder Lauf erzeugt eine eigene Datenbank ``syllentra_t_<12 Hex>`` mit einem Eigentumsvermerk
(Datenbankkommentar mit zufälligem Token) und hält über eine persistente Maintenance-Verbindung
einen exklusiven Session-Advisory-Lock.

Parcours A: Normale Löschung durch den aktiven Besitzer (erfordert gehaltenen Lock auf lock_conn).
Parcours B: Kontrollierte Übernahme und Bereinigung verwaister Läufe (sweep / reclaim).

Gemeinsame Datenbanken (``syllentra_test``, ``syllentra_prototype``) werden hier nie verändert.
"""

import json
import logging
import math
import re
import secrets
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from uuid import uuid4

import psycopg
from psycopg import sql

from scripts.migrate import migrate

ROOT = Path(__file__).resolve().parents[1]
RUN_NAME = re.compile(r"syllentra_t_[0-9a-f]{12}")
TOKEN_HEX = re.compile(r"[0-9a-f]{32}")
MARK = "syllentra-test-run:v1"
SWEEP_LOCK_KEY = 0x53594C4C_54444201  # Syllentra Test DB Sweep advisory lock
# Reihenfolge ist unkritisch (FK-Kaskaden), die Liste ist ausdrücklich konstant.
WIPE_TABLES = (
    "security_events",
    "identity_budgets",
    "identity_challenges",
    "recovery_codes",
    "sessions",
    "notes",
    "devices",
    "accounts",
)


class OwnershipError(RuntimeError):
    """Ein zerstörender Zugriff auf eine nicht verifizierte Datenbank wurde verweigert."""


@dataclass(frozen=True)
class RunDatabase:
    run_id: str
    name: str
    comment: str = field(repr=False)
    admin_url: str = field(repr=False)
    runtime_url: str = field(repr=False)
    maintenance_url: str = field(repr=False)
    lock_conn: Any = field(default=None, repr=False)


def _lock_key(run_id: str) -> int:
    """Deterministischer 64-Bit-Advisory-Lock-Key für den Besitzerprozess eines Runs."""
    return (0x5359 << 48) | int(run_id, 16)


def _lock_parts(key: int) -> tuple[int, int]:
    """Teilt einen 64-Bit-Key in classid (obere 32 Bit) und objid (untere 32 Bit) für pg_locks."""
    return (key >> 32) & 0xFFFFFFFF, key & 0xFFFFFFFF


def _validate_hours(older_than_hours: float) -> float:
    if isinstance(older_than_hours, bool) or not isinstance(older_than_hours, (int, float)):
        raise ValueError("Stundenwert muss eine endliche Zahl >= 0 sein.")
    hours = float(older_than_hours)
    if not math.isfinite(hours) or hours < 0:
        raise ValueError("Stundenwert muss eine endliche Zahl >= 0 sein.")
    return hours


def _credentials() -> dict[str, str]:
    data = json.loads((ROOT / ".local/database.json").read_text())
    return {"migration": str(data["migration_url"]), "runtime": str(data["runtime_url"])}


def _expected_comment(run_id: str, created: int, token: str) -> str:
    return f"{MARK}:{run_id}:{created}:{token}"


def _parse_comment(name: str, comment: str | None) -> tuple[str, int, str] | None:
    if not comment or not RUN_NAME.fullmatch(name):
        return None
    parts = comment.split(":")
    if len(parts) != 5 or f"{parts[0]}:{parts[1]}" != MARK:
        return None
    run_id, ts_raw, token = parts[2], parts[3], parts[4]
    if run_id != name.removeprefix("syllentra_t_"):
        return None
    if not ts_raw.isdigit() or not TOKEN_HEX.fullmatch(token):
        return None
    return run_id, int(ts_raw), token


def _same_owner(name: str, actual: str | None, expected: str) -> bool:
    if actual is None or not expected:
        return False
    parsed_actual = _parse_comment(name, actual)
    parsed_expected = _parse_comment(name, expected)
    if not parsed_actual or not parsed_expected:
        return False
    return parsed_actual == parsed_expected


def _database_in_use(conn: psycopg.Connection[tuple[object, ...]], name: str) -> bool:
    row = conn.execute(
        "SELECT EXISTS ("
        "SELECT 1 FROM pg_stat_activity WHERE datname = %s AND pid <> pg_backend_pid()"
        ")",
        (name,),
    ).fetchone()
    return bool(row and row[0])


def create_run_database() -> RunDatabase:
    """Neue leere Lauf-Datenbank erzeugen, migrieren und mit exklusivem Besitz-Lock versehen."""
    creds = _credentials()
    run_id = uuid4().hex[:12]
    name = f"syllentra_t_{run_id}"
    assert RUN_NAME.fullmatch(name)
    comment = _expected_comment(run_id, int(time.time()), secrets.token_hex(16))
    maintenance = creds["migration"] + "postgres"

    # 1. Persistente Maintenance-Verbindung öffnen und exklusiven Run-Lock VOR der DB-Erstellung
    lock_conn = psycopg.connect(maintenance, autocommit=True)
    created_db = False
    try:
        lock_key = _lock_key(run_id)
        acquired = lock_conn.execute(
            "SELECT pg_try_advisory_lock(%s)", (lock_key,)
        ).fetchone()
        if not acquired or not acquired[0]:
            raise OwnershipError(
                "Besitz-Lock für die neue Lauf-Datenbank konnte nicht erworben werden."
            )
        # 2. Datenbank anlegen
        lock_conn.execute(
            sql.SQL("CREATE DATABASE {} TEMPLATE template0").format(sql.Identifier(name))
        )
        created_db = True

        # 3. Eigentumsvermerk setzen (während der Lock bereits gehalten wird)
        lock_conn.execute(
            sql.SQL("COMMENT ON DATABASE {} IS {}").format(
                sql.Identifier(name), sql.Literal(comment)
            )
        )
    except Exception as create_exc:
        # Falls DB bereits erzeugt wurde, unter gehaltenem Lock aufräumen
        if created_db:
            try:
                lock_conn.execute(
                    sql.SQL("DROP DATABASE {}").format(sql.Identifier(name))
                )
            except Exception as drop_exc:
                logging.getLogger("syllentra.test_db").error(
                    "Partielle Testdatenbank %s konnte nicht bereinigt werden.", name
                )
                lock_conn.close()
                raise create_exc from drop_exc
        lock_conn.close()
        raise

    run = RunDatabase(
        run_id,
        name,
        comment,
        creds["migration"] + name,
        creds["runtime"] + name,
        maintenance,
        lock_conn=lock_conn,
    )
    # 4. Migration anwenden; bei Fehlschlag sauber aufräumen und Primärfehler erhalten
    try:
        migrate(run.admin_url)
    except Exception as migrate_exc:
        try:
            drop_run_database(run)
        except Exception as drop_exc:
            logging.getLogger("syllentra.test_db").error(
                "Lauf-Datenbank %s konnte nach Migrationsfehler nicht gelöscht werden.", name
            )
            raise migrate_exc from drop_exc
        raise
    return run


def _owned_comment(conn: psycopg.Connection[tuple[object, ...]], name: str) -> str | None:
    row = conn.execute(
        "SELECT shobj_description(oid, 'pg_database') FROM pg_database WHERE datname = %s",
        (name,),
    ).fetchone()
    return str(row[0]) if row and row[0] else None


def assert_owned(run: RunDatabase, url: str | None = None) -> None:
    """Verweigert jede Aktion, falls Verbindung/Name/Eigentumsvermerk nicht zu ``run`` passen."""
    if not RUN_NAME.fullmatch(run.name):
        raise OwnershipError("Kein zulässiger Lauf-Datenbankname.")
    if run.lock_conn is None or run.lock_conn.closed:
        raise OwnershipError("Besitz-Verbindung der Lauf-Datenbank fehlt oder wurde geschlossen.")
    key = _lock_key(run.run_id)
    classid, objid = _lock_parts(key)
    pid = run.lock_conn.info.backend_pid
    # Gemäß PostgreSQL-Doku: bigint-Locks haben classid = obere 32 Bit, objid = untere 32 Bit
    # und objsubid = 1, locktype = 'advisory' auf der Maintenance-Datenbank.
    row = run.lock_conn.execute(
        "SELECT EXISTS ("
        "SELECT 1 FROM pg_locks "
        "WHERE locktype = 'advisory' "
        "AND classid = %s "
        "AND objid = %s "
        "AND objsubid = 1 "
        "AND pid = %s "
        "AND granted = true "
        "AND database = (SELECT oid FROM pg_database WHERE datname = current_database())"
        ")",
        (classid, objid, pid),
    ).fetchone()
    if not row or not row[0]:
        raise OwnershipError("Besitz-Lock der Lauf-Datenbank ging verloren.")
    with psycopg.connect(run.maintenance_url) as conn:
        if not _same_owner(run.name, _owned_comment(conn, run.name), run.comment):
            raise OwnershipError("Eigentumsvermerk der Lauf-Datenbank stimmt nicht überein.")
    if url is not None:
        with psycopg.connect(url) as conn:
            current = conn.execute("SELECT current_database()").fetchone()
            if not current or current[0] != run.name:
                raise OwnershipError("Verbindung zeigt nicht auf die eigene Lauf-Datenbank.")


def wipe(run: RunDatabase) -> None:
    """Testdaten der *eigenen* Lauf-Datenbank leeren (DELETE nur nach Eigentumsprüfung)."""
    assert_owned(run, run.admin_url)
    with psycopg.connect(run.admin_url) as db:
        for table in WIPE_TABLES:
            db.execute(sql.SQL("DELETE FROM {}").format(sql.Identifier(table)))
        db.execute(
            "UPDATE capabilities SET mode='available', allowed_kind='user' WHERE name='notes'"
        )


def drop_run_database(run: RunDatabase) -> None:
    """Eigene Lauf-Datenbank löschen (Parcours A); erfordert aktiven Besitz-Lock."""
    assert_owned(run)

    # Nutze die bestehende lock_conn, die den Lock bereits hält
    for _ in range(5):
        if not _database_in_use(run.lock_conn, run.name):
            break
        time.sleep(0.05)
    else:
        raise OwnershipError("Lauf-Datenbank wird noch aktiv verwendet.")
    try:
        run.lock_conn.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(run.name)))
    except psycopg.errors.ObjectInUse as exc:
        # Besitz-Verbindung bleibt offen und geschützt!
        raise OwnershipError("Lauf-Datenbank wird noch aktiv verwendet.") from exc
    # Erst nach erfolgreichem DROP Verbindung schließen (gibt Lock frei)
    run.lock_conn.close()


def reclaim_orphaned_database(name: str) -> None:
    """Verwaiste Lauf-Datenbank kontrolliert übernehmen und löschen (Parcours B)."""
    if not RUN_NAME.fullmatch(name):
        raise OwnershipError("Kein zulässiger Lauf-Datenbankname.")
    creds = _credentials()
    maintenance = creds["migration"] + "postgres"
    with psycopg.connect(maintenance, autocommit=True) as db:
        comment = _owned_comment(db, name)
        parsed = _parse_comment(name, comment)
        if not parsed:
            raise OwnershipError(
                "Datenbank ist nicht als verwaister Syllentra-Testlauf verifiziert."
            )
        run_id, _, _ = parsed
        run_key = _lock_key(run_id)
        acquired = db.execute(
            "SELECT pg_try_advisory_lock(%s)", (run_key,)
        ).fetchone()
        if not acquired or not acquired[0]:
            raise OwnershipError(
                "Lauf-Datenbank wird noch von einem aktiven Prozess besessen."
            )
        try:
            rechecked = _parse_comment(name, _owned_comment(db, name))
            if not rechecked or rechecked != parsed:
                raise OwnershipError(
                    "Eigentumsvermerk hat sich während der Übernahme verändert."
                )
            if _database_in_use(db, name):
                raise OwnershipError("Lauf-Datenbank hat noch aktive Verbindungen.")
            try:
                db.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(name)))
            except psycopg.errors.ObjectInUse as exc:
                raise OwnershipError("Lauf-Datenbank wird noch aktiv verwendet.") from exc
        finally:
            db.execute("SELECT pg_advisory_unlock(%s)", (run_key,))


def sweep(older_than_hours: float, *, apply: bool) -> list[str]:
    """Verwaiste, nicht aktiv genutzte Lauf-Datenbanken auflisten (optional löschen)."""
    hours = _validate_hours(older_than_hours)
    threshold_seconds = hours * 3600.0
    creds = _credentials()
    maintenance = creds["migration"] + "postgres"
    found: list[str] = []
    with psycopg.connect(maintenance, autocommit=True) as db:
        if apply:
            locked = db.execute(
                "SELECT pg_try_advisory_lock(%s)", (SWEEP_LOCK_KEY,)
            ).fetchone()
            if not locked or not locked[0]:
                return []
        try:
            names = [r[0] for r in db.execute("SELECT datname FROM pg_database").fetchall()]
            for name in names:
                if not RUN_NAME.fullmatch(name):
                    continue
                parsed = _parse_comment(name, _owned_comment(db, name))
                if not parsed:
                    continue  # nicht von diesem Werkzeug markiert: niemals anfassen
                run_id, generation, _ = parsed
                age = time.time() - generation
                if age < 0 or age < threshold_seconds:
                    continue

                # Koordinationsprotokoll: Prüfen, ob der Besitzerprozess noch aktiv ist.
                run_key = _lock_key(run_id)
                acquired = db.execute(
                    "SELECT pg_try_advisory_lock(%s)", (run_key,)
                ).fetchone()
                if not acquired or not acquired[0]:
                    # Besitzerprozess ist aktiv: niemals auflisten oder löschen!
                    continue
                try:
                    if _database_in_use(db, name):
                        continue
                    if not apply:
                        found.append(name)
                        continue
                    # Re-Check unmittelbar vor dem Drop zur Minimierung von TOCTOU-Fenstern
                    rechecked = _parse_comment(name, _owned_comment(db, name))
                    if not rechecked or rechecked != parsed:
                        continue
                    rechecked_age = time.time() - rechecked[1]
                    if rechecked_age < 0 or rechecked_age < threshold_seconds:
                        continue
                    if _database_in_use(db, name):
                        continue
                    try:
                        # Ohne WITH (FORCE): bricht ab, falls Verbindung geöffnet wurde
                        db.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(name)))
                        found.append(name)
                    except (psycopg.errors.ObjectInUse, psycopg.errors.InvalidCatalogName):
                        continue
                finally:
                    db.execute("SELECT pg_advisory_unlock(%s)", (run_key,))
        finally:
            if apply:
                db.execute("SELECT pg_advisory_unlock(%s)", (SWEEP_LOCK_KEY,))
    return found


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["sweep"] and len(args) in {2, 3} and (len(args) == 2 or args[2] == "--apply"):
        try:
            hours = float(args[1])
            _validate_hours(hours)
        except ValueError as err:
            raise SystemExit(f"Ungültiger Stundenwert: {err}") from err
        names = sweep(hours, apply=len(args) == 3)
        print("\n".join(names) or "keine verwaisten Lauf-Datenbanken")
        return
    raise SystemExit("Aufruf: python -m scripts.test_db sweep <Stunden> [--apply]")
