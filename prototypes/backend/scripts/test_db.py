"""Isolierte PostgreSQL-Testdatenbanken pro Testlauf (Mission 12).

Jeder Lauf erzeugt eine eigene Datenbank ``syllentra_t_<12 Hex>`` mit einem Eigentumsvermerk
(Datenbankkommentar mit zufälligem Token). Zerstörende Operationen (DELETE/DROP) werden nur
ausgeführt, wenn Name *und* Eigentumsvermerk der konkreten Lauf-Datenbank bestätigt sind.
Gemeinsame Datenbanken (``syllentra_test``, ``syllentra_prototype``) werden hier nie verändert.
"""

import json
import re
import secrets
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from uuid import uuid4

import psycopg
from psycopg import sql

from scripts.migrate import migrate

ROOT = Path(__file__).resolve().parents[1]
RUN_NAME = re.compile(r"syllentra_t_[0-9a-f]{12}")
MARK = "syllentra-test-run:v1"
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


def _credentials() -> dict[str, str]:
    data = json.loads((ROOT / ".local/database.json").read_text())
    return {"migration": str(data["migration_url"]), "runtime": str(data["runtime_url"])}


def _expected_comment(run_id: str, created: int, token: str) -> str:
    return f"{MARK}:{run_id}:{created}:{token}"


def create_run_database() -> RunDatabase:
    """Neue leere Lauf-Datenbank erzeugen, migrieren und mit Eigentumsvermerk versehen."""
    creds = _credentials()
    run_id = uuid4().hex[:12]
    name = f"syllentra_t_{run_id}"
    assert RUN_NAME.fullmatch(name)
    comment = _expected_comment(run_id, int(time.time()), secrets.token_hex(16))
    maintenance = creds["migration"] + "postgres"
    with psycopg.connect(maintenance, autocommit=True) as db:
        # template0: kein Konflikt mit parallelen Läufen, die template1 geöffnet halten könnten.
        db.execute(sql.SQL("CREATE DATABASE {} TEMPLATE template0").format(sql.Identifier(name)))
        db.execute(
            sql.SQL("COMMENT ON DATABASE {} IS {}").format(
                sql.Identifier(name), sql.Literal(comment)
            )
        )
    run = RunDatabase(
        run_id, name, comment, creds["migration"] + name, creds["runtime"] + name, maintenance
    )
    migrate(run.admin_url)
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
    with psycopg.connect(run.maintenance_url) as conn:
        if _owned_comment(conn, run.name) != run.comment:
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
    """Eigene Lauf-Datenbank löschen; verweigert bei unbestätigtem Eigentum."""
    assert_owned(run)
    with psycopg.connect(run.maintenance_url, autocommit=True) as db:
        db.execute(sql.SQL("DROP DATABASE {} WITH (FORCE)").format(sql.Identifier(run.name)))


def sweep(older_than_hours: float, *, apply: bool) -> list[str]:
    """Verwaiste, von diesem Werkzeug markierte Lauf-Datenbanken auflisten (optional löschen)."""
    creds = _credentials()
    maintenance = creds["migration"] + "postgres"
    found: list[str] = []
    with psycopg.connect(maintenance, autocommit=True) as db:
        names = [r[0] for r in db.execute("SELECT datname FROM pg_database").fetchall()]
        for name in names:
            if not RUN_NAME.fullmatch(name):
                continue
            comment = _owned_comment(db, name) or ""
            parts = comment.split(":")
            if not comment.startswith(MARK + ":") or len(parts) != 5 or not parts[3].isdigit():
                continue  # nicht von diesem Werkzeug markiert: niemals anfassen
            if time.time() - int(parts[3]) < older_than_hours * 3600:
                continue
            found.append(name)
            if apply:
                db.execute(sql.SQL("DROP DATABASE {} WITH (FORCE)").format(sql.Identifier(name)))
    return found


def main() -> None:
    args = sys.argv[1:]
    if args[:1] == ["sweep"] and len(args) in {2, 3} and (len(args) == 2 or args[2] == "--apply"):
        names = sweep(float(args[1]), apply=len(args) == 3)
        print("\n".join(names) or "keine verwaisten Lauf-Datenbanken")
        return
    raise SystemExit("Aufruf: python -m scripts.test_db sweep <Stunden> [--apply]")


if __name__ == "__main__":
    main()
