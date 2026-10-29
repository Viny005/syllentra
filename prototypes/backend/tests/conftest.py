"""Isolierte Lauf-Datenbank und gemeinsame Identitäts-Testumgebung (Mission 12).

pytest nutzt niemals die gemeinsame Datenbank ``syllentra_test`` (reserviert für Browserprüfungen):
jeder Prozess erzeugt eine eigene Datenbank mit Eigentumsvermerk und löscht nur diese.
"""

import secrets
from collections.abc import Iterator
from datetime import UTC, datetime
from typing import Any

import pytest
from fastapi.testclient import TestClient
from private_fixtures import PrivateEnvironment

from scripts.test_db import RunDatabase, create_run_database, drop_run_database, wipe
from syllentra_backend.api import create_app
from syllentra_backend.delivery import MemoryChannel
from syllentra_backend.identity import LocalIdentity


@pytest.fixture(scope="session")
def run_db() -> Iterator[RunDatabase]:
    run = create_run_database()
    try:
        yield run
    finally:
        drop_run_database(run)


@pytest.fixture()
def env(run_db: RunDatabase) -> Iterator[Any]:
    wipe(run_db)
    now = [datetime(2026, 10, 22, tzinfo=UTC)]
    mail, offline = MemoryChannel(), MemoryChannel()
    config = LocalIdentity(secrets.token_bytes(32), mail, offline)
    app = create_app(run_db.runtime_url, identity=config, clock=lambda: now[0])
    clients: list[TestClient] = []

    def browser() -> TestClient:
        c = TestClient(app, base_url="https://testserver")
        csrf = c.get("/auth/csrf").json()["csrf_token"]
        c.headers.update({"Origin": config.origin, "X-CSRF-Token": csrf})
        clients.append(c)
        return c

    yield PrivateEnvironment(
        admin=run_db.admin_url,
        runtime=run_db.runtime_url,
        now=now,
        mail=mail,
        offline=offline,
        browser=browser,
        app=app,
        config=config,
        run=run_db,
    )
    for c in clients:
        c.close()
