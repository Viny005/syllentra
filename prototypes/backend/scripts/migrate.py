"""Versionierte, atomare Vorwärtsmigration; bestehende Prüfsumme muss übereinstimmen."""

import hashlib
import json
import sys
from pathlib import Path

import psycopg

ROOT = Path(__file__).resolve().parents[1]


def urls(test: bool = False) -> tuple[str, str]:
    data = json.loads((ROOT / ".local/database.json").read_text())
    name = "syllentra_test" if test else "syllentra_prototype"
    return str(data["migration_url"]) + name, str(data["runtime_url"]) + name


def migrate(url: str) -> None:
    with psycopg.connect(url) as db:
        db.execute("SELECT pg_advisory_xact_lock(91239001)")
        db.execute(
            "CREATE TABLE IF NOT EXISTS schema_migrations "
            "(version text PRIMARY KEY, sha256 text NOT NULL)"
        )
        for file in sorted((ROOT / "migrations").glob("*.sql")):
            sql = file.read_text()
            digest = hashlib.sha256(sql.encode()).hexdigest()
            previous = db.execute(
                "SELECT sha256 FROM schema_migrations WHERE version = %s", (file.name,)
            ).fetchone()
            if previous:
                if previous[0] != digest:
                    raise RuntimeError("Bereits angewandte Migration verändert; sicher gestoppt.")
                continue
            db.execute(sql)
            db.execute("INSERT INTO schema_migrations VALUES (%s, %s)", (file.name, digest))
        db.execute("REVOKE ALL ON SCHEMA public FROM PUBLIC")
        db.execute("GRANT USAGE ON SCHEMA public TO syllentra_runtime")
        db.execute("GRANT SELECT ON accounts, devices, capabilities TO syllentra_runtime")
        db.execute("REVOKE ALL ON sessions, notes FROM syllentra_runtime")
        db.execute("GRANT SELECT, INSERT ON sessions TO syllentra_runtime")
        db.execute("GRANT UPDATE (revoked) ON sessions TO syllentra_runtime")
        db.execute(
            "GRANT INSERT (id,login,password_hash,verification,status) ON accounts "
            "TO syllentra_runtime"
        )
        db.execute(
            "GRANT UPDATE (password_hash,verification,security_epoch) ON accounts "
            "TO syllentra_runtime"
        )
        db.execute("REVOKE INSERT, UPDATE ON devices FROM syllentra_runtime")
        db.execute(
            "GRANT INSERT (id,account_id,proof_hash,authorized,expires_at,security_epoch) "
            "ON devices TO syllentra_runtime"
        )
        db.execute(
            "GRANT UPDATE (authorized,expires_at,security_epoch) ON devices TO syllentra_runtime"
        )
        db.execute(
            "GRANT SELECT, INSERT, UPDATE, DELETE ON identity_challenges, recovery_codes, "
            "identity_budgets, security_events TO syllentra_runtime"
        )
        db.execute("GRANT SELECT ON notes TO syllentra_runtime")
        db.execute("GRANT UPDATE (title, body, deleted_at) ON notes TO syllentra_runtime")


if __name__ == "__main__":
    migrate(urls(test=sys.argv[1:] == ["--test"])[0])
    print("Migration erfolgreich; kein Konto angelegt.")
