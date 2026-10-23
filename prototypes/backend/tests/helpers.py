"""Gemeinsame Hilfen für Identitätstests (ausschließlich synthetische Daten)."""

from typing import Any

from fastapi.testclient import TestClient

from syllentra_backend.identity import DEVICE, SESSION

PASSWORD = "synthetic-password-for-tests"
NEW_PASSWORD = "different-synthetic-password"


def registration(e: Any, c: TestClient, email: str = "alice@example.test") -> str:
    r = c.post("/auth/register", json={"email": email, "password": PASSWORD})
    assert r.status_code == 202 and set(r.json()) == {"status", "challenge_id"}
    return str(r.json()["challenge_id"])


def verify(e: Any, c: TestClient, ref: str) -> None:
    code = e["mail"].take(ref)
    r = c.post("/auth/verify", json={"challenge_id": ref, "code": code})
    assert r.status_code == 200 and code not in r.text
    assert c.cookies.get(DEVICE) and not c.cookies.get(SESSION)


def account(e: Any, c: TestClient, email: str = "alice@example.test") -> None:
    verify(e, c, registration(e, c, email))
    assert c.post("/auth/login", json={"login": email, "password": PASSWORD}).status_code == 200
