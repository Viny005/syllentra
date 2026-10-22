"""Negative API-/PostgreSQL-Prüfungen mit ausschließlich künstlichen Konten."""

import secrets
from collections.abc import Iterator
from datetime import UTC, datetime, timedelta
from typing import Any
from uuid import uuid4

import psycopg
import pytest
from fastapi.testclient import TestClient

from scripts.migrate import migrate, urls
from syllentra_backend.api import create_app
from syllentra_backend.security import PASSWORDS, LoginBudget, digest, verify_password

PASSWORD = "synthetic-test-password-only"
NOW = datetime(2026, 10, 22, tzinfo=UTC)


@pytest.fixture()
def setup() -> Iterator[dict[str, Any]]:
    admin_url, runtime_url = urls(test=True)
    assert admin_url.endswith("/syllentra_test")
    migrate(admin_url)
    migrate(admin_url)  # Wiederholung darf weder Daten zurücksetzen noch Schema duplizieren.
    ids = {key: uuid4() for key in ["a", "b", "pending", "admin", "da", "db", "na", "nb"]}
    proof = secrets.token_urlsafe(32)
    with psycopg.connect(admin_url) as db:
        for table in ["sessions", "notes", "devices", "accounts"]:
            db.execute(f"DELETE FROM {table}")  # noqa: S608 -- ausschließlich konstante Tabellenliste
        db.execute(
            "UPDATE capabilities SET mode = 'available', allowed_kind = 'user' WHERE name = 'notes'"
        )
        encoded = PASSWORDS.hash(PASSWORD)
        for key in ["a", "b", "pending", "admin"]:
            db.execute(
                "INSERT INTO accounts VALUES (%s, %s, %s, %s, %s, 'active')",
                (
                    ids[key],
                    key,
                    encoded,
                    "administrator" if key == "admin" else "user",
                    "pending" if key == "pending" else "verified",
                ),
            )
        for key in ["a", "b"]:
            db.execute(
                "INSERT INTO devices VALUES (%s, %s, %s, true)",
                (ids["d" + key], ids[key], digest(proof + key)),
            )
            db.execute(
                "INSERT INTO notes VALUES (%s, %s, %s, %s, NULL)",
                (ids["n" + key], ids[key], "Notiz " + key, "Synthetischer Inhalt " + key),
            )
    app = create_app(runtime_url, synthetic_test_harness=True, clock=lambda: NOW)
    with TestClient(app) as client:
        yield {
            "client": client,
            "ids": ids,
            "proof": proof,
            "admin_url": admin_url,
            "runtime_url": runtime_url,
            "app": app,
        }


def login(setup: dict[str, Any], account: str = "a") -> dict[str, str]:
    response = setup["client"].post(
        "/auth/login",
        json={"login": account, "password": PASSWORD, "device_proof": setup["proof"] + account},
    )
    assert response.status_code == 200, response.text
    return {"Authorization": "Bearer " + response.json()["access_token"]}


def test_password_hash_and_budget() -> None:
    encoded = PASSWORDS.hash(PASSWORD)
    assert encoded.startswith("$argon2id$") and PASSWORD not in encoded
    assert verify_password(encoded, PASSWORD)
    assert not verify_password(encoded, "wrong")
    assert not verify_password("invalid-hash", PASSWORD)
    budget = LoginBudget()
    assert all(budget.allow() for _ in range(10))
    assert not budget.allow()


def test_default_runtime_has_no_login_or_seed(setup: dict[str, Any]) -> None:
    with TestClient(create_app(setup["runtime_url"])) as client:
        assert (
            client.post(
                "/auth/login",
                json={"login": "a", "password": PASSWORD, "device_proof": setup["proof"] + "a"},
            ).status_code
            == 503
        )
        assert client.get("/health").json()["authentication"] == "unavailable"
    with pytest.raises(ValueError, match="Testharness"):
        create_app("postgresql://localhost/production", synthetic_test_harness=True)


@pytest.mark.parametrize("path", ["/session", "/notes", "/capabilities", "/administration"])
@pytest.mark.parametrize(
    "authorization", [None, "Bearer invalid", "Basic wrong", "Bearer " + "a" * 43]
)
def test_anonymous_invalid_token(
    setup: dict[str, Any], path: str, authorization: str | None
) -> None:
    headers = {"Authorization": authorization} if authorization else {}
    response = setup["client"].get(path, headers=headers)
    assert response.status_code == 401
    assert response.headers["Cache-Control"] == "no-store"
    assert "password_hash" not in response.text


@pytest.mark.parametrize("account", ["pending", "admin", "unknown"])
def test_unverified_admin_unknown_login_denied(setup: dict[str, Any], account: str) -> None:
    result = setup["client"].post(
        "/auth/login",
        json={"login": account, "password": PASSWORD, "device_proof": setup["proof"] + account},
    )
    assert result.status_code == 401 and result.json() == {"detail": "unauthorized"}


def test_password_device_rate_limit_and_no_echo(setup: dict[str, Any]) -> None:
    for i in range(11):
        r = setup["client"].post(
            "/auth/login",
            json={
                "login": "a",
                "password": PASSWORD,
                "device_proof": "wrong-device-proof-not-authorized-000",
            },
        )
        assert r.status_code == (401 if i < 10 else 429)
        assert PASSWORD not in r.text
    r = setup["client"].post("/auth/login", json={"password": PASSWORD, "token": "private-probe"})
    assert r.status_code == 422 and "private-probe" not in r.text and PASSWORD not in r.text


def test_sessions_hash_expiry_revocation_and_no_secrets(setup: dict[str, Any]) -> None:
    headers = login(setup)
    client = setup["client"]
    me = client.get("/session", headers=headers)
    assert set(me.json()) == {"account_id", "kind", "assurance"}
    assert client.get("/capabilities", headers=headers).json() == {
        "notes": "available",
        "assistant": "unavailable",
    }
    token = headers["Authorization"][7:]
    assert token not in me.text
    with psycopg.connect(setup["admin_url"]) as db:
        row = db.execute("SELECT token_hash FROM sessions").fetchone()
        assert row and row[0] == digest(token) and row[0] != token
        db.execute("UPDATE sessions SET expires_at = %s", (NOW - timedelta(seconds=1),))
    assert client.get("/notes", headers=headers).status_code == 401
    headers = login(setup)
    assert client.post("/auth/logout", headers=headers).status_code == 204
    assert client.get("/session", headers=headers).status_code == 401
    assert client.post("/auth/logout", headers=headers).status_code == 401


def test_owner_read_update_delete_and_cross_account(setup: dict[str, Any]) -> None:
    client, ids = setup["client"], setup["ids"]
    a, b = login(setup), login(setup, "b")
    assert [n["id"] for n in client.get("/notes", headers=a).json()] == [str(ids["na"])]
    foreign = "/notes/" + str(ids["nb"])
    assert client.get(foreign, headers=a).status_code == 404
    assert (
        client.patch(foreign, headers=a, json={"title": "Attack", "body": "x"}).status_code == 404
    )
    assert (
        client.delete(foreign, headers={**a, "X-Confirm-Delete": str(ids["nb"])}).status_code == 404
    )
    assert client.get(foreign, headers=b).json()["title"] == "Notiz b"
    own = "/notes/" + str(ids["na"])
    assert (
        client.patch(own, headers=a, json={"title": "Korrigiert", "body": "Nur Test"}).status_code
        == 200
    )
    assert client.get(own, headers=a).json()["title"] == "Korrigiert"
    assert client.delete(own, headers=a).status_code == 409
    assert client.delete(own, headers={**a, "X-Confirm-Delete": str(ids["na"])}).status_code == 204
    assert client.get(own, headers=a).status_code == 404
    with psycopg.connect(setup["admin_url"]) as db:
        assert db.execute("SELECT deleted_at FROM notes WHERE id = %s", (ids["na"],)).fetchone()[0]


@pytest.mark.parametrize("field", ["account_id", "owner_id", "id", "kind", "verification"])
def test_client_cannot_choose_identity(setup: dict[str, Any], field: str) -> None:
    a, ids, client = login(setup), setup["ids"], setup["client"]
    r = client.patch(
        "/notes/" + str(ids["na"]),
        headers=a,
        json={"title": "x", "body": "x", field: str(ids["b"])},
    )
    assert r.status_code == 422
    assert client.get("/session", headers={**a, "X-Account-ID": str(ids["b"])}).json()[
        "account_id"
    ] == str(ids["a"])
    assert client.get("/notes?account_id=" + str(ids["b"]), headers=a).json()[0]["id"] == str(
        ids["na"]
    )


@pytest.mark.parametrize("mode", ["hidden", "unavailable"])
def test_flags_enforced_directly(setup: dict[str, Any], mode: str) -> None:
    a = login(setup)
    with psycopg.connect(setup["admin_url"]) as db:
        db.execute("UPDATE capabilities SET mode = %s WHERE name = 'notes'", (mode,))
    client, path = setup["client"], "/notes/" + str(setup["ids"]["na"])
    assert client.get("/notes", headers=a).status_code == 403
    assert client.get(path, headers=a).status_code == 403
    assert client.patch(path, headers=a, json={"title": "x", "body": "x"}).status_code == 403
    assert client.delete(path, headers=a).status_code == 403
    with psycopg.connect(setup["admin_url"]) as db:
        db.execute("UPDATE capabilities SET mode = 'available' WHERE name = 'assistant'")
    capabilities = client.get("/capabilities", headers=a).json()
    assert capabilities["assistant"] == "unavailable"

    assert ("notes" not in capabilities) if mode == "hidden" else capabilities["notes"] == mode


@pytest.mark.parametrize("change", ["suspend", "unverify", "device", "role", "flag_role"])
def test_current_permissions_after_session_change(setup: dict[str, Any], change: str) -> None:
    a, b = login(setup), login(setup, "b")
    ids = setup["ids"]
    with psycopg.connect(setup["admin_url"]) as db:
        if change == "suspend":
            db.execute("UPDATE accounts SET status = 'suspended' WHERE id = %s", (ids["a"],))
        elif change == "unverify":
            db.execute("UPDATE accounts SET verification = 'pending' WHERE id = %s", (ids["a"],))
        elif change == "device":
            db.execute("UPDATE devices SET authorized = false WHERE id = %s", (ids["da"],))
        elif change == "role":
            db.execute("UPDATE accounts SET kind = 'administrator' WHERE id = %s", (ids["a"],))
        else:
            db.execute(
                "UPDATE capabilities SET allowed_kind = 'administrator' WHERE name = 'notes'"
            )
    r = setup["client"].get("/notes", headers=a)
    assert r.status_code == (403 if change in ["role", "flag_role"] else 401)
    assert setup["client"].get("/administration", headers=a).status_code in [401, 403]
    if change != "flag_role":
        assert setup["client"].get("/notes", headers=b).status_code == 200


def test_admin_never_gets_private_content(setup: dict[str, Any]) -> None:
    # Bereits vorhandene künstliche Adminsession prüft selbst ohne erlaubten Adminlogin die Grenze.
    token = secrets.token_urlsafe(32)
    with psycopg.connect(setup["admin_url"]) as db:
        device = uuid4()
        db.execute(
            "INSERT INTO devices VALUES (%s, %s, %s, true)",
            (device, setup["ids"]["admin"], digest(secrets.token_urlsafe(32))),
        )
        db.execute(
            "INSERT INTO sessions VALUES (%s, %s, %s, %s, false)",
            (digest(token), setup["ids"]["admin"], device, NOW + timedelta(minutes=1)),
        )
    h = {"Authorization": "Bearer " + token}
    assert setup["client"].get("/administration", headers=h).status_code == 403
    assert setup["client"].get("/notes", headers=h).status_code == 403
    with psycopg.connect(setup["admin_url"]) as db:
        db.execute("UPDATE capabilities SET allowed_kind = 'administrator' WHERE name = 'notes'")
    assert setup["client"].get("/notes", headers=h).status_code == 403
    assert setup["client"].get("/capabilities", headers=h).json()["notes"] == "unavailable"


def test_validation_origin_and_failure_redaction(setup: dict[str, Any]) -> None:
    a = login(setup)
    client = setup["client"]
    assert client.get("/notes/not-a-uuid", headers=a).status_code == 422
    assert client.patch(
        "/notes/" + str(setup["ids"]["na"]), headers=a, json={"title": " ", "body": "private-body"}
    ).json() == {"detail": "invalid_input"}
    assert (
        client.get("/session", headers={**a, "Origin": "https://attacker.invalid"}).status_code
        == 403
    )
    assert client.get("/health", headers={"Host": "attacker.invalid"}).status_code == 400
    with TestClient(create_app("postgresql://127.0.0.1:1/unavailable")) as broken:
        response = broken.get("/session", headers=a)
        assert response.status_code == 503 and response.json() == {"detail": "service_unavailable"}
        assert "postgresql" not in response.text


def test_database_constraints_and_runtime_privileges(setup: dict[str, Any]) -> None:
    with psycopg.connect(setup["runtime_url"]) as db:
        assert db.execute("SELECT current_user").fetchone()[0] == "syllentra_runtime"
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            db.execute("UPDATE accounts SET kind = 'administrator'")
    with psycopg.connect(setup["admin_url"]) as db:
        with pytest.raises(psycopg.errors.CheckViolation):
            db.execute("UPDATE capabilities SET mode = 'arbitrary-code'")
    with psycopg.connect(setup["admin_url"]) as db:
        with pytest.raises(psycopg.errors.ForeignKeyViolation):
            db.execute(
                "INSERT INTO sessions VALUES (%s, %s, %s, %s, false)",
                (digest("wrong-owner"), setup["ids"]["a"], setup["ids"]["db"], NOW),
            )


def test_wrong_password_and_missing_identity_flows(setup: dict[str, Any]) -> None:
    client = setup["client"]
    response = client.post(
        "/auth/login",
        json={
            "login": "a",
            "password": "wrong-password-long",
            "device_proof": setup["proof"] + "a",
        },
    )
    assert response.status_code == 401
    for path in [
        "/auth/verify",
        "/auth/register",
        "/auth/recover",
        "/auth/mfa",
        "/admin/bootstrap",
    ]:
        assert client.post(path, json={"account_id": str(setup["ids"]["a"])}).status_code == 404
    response = client.post("/auth/login", content=b"x" * 17000)
    assert response.status_code == 413 and response.json() == {"detail": "input_too_large"}


def test_revision_rejection(setup: dict[str, Any], tmp_path: Any, monkeypatch: Any) -> None:
    import scripts.migrate as migration

    directory = tmp_path / "migrations"
    directory.mkdir()
    original = migration.ROOT / "migrations/001_foundation.sql"
    (directory / original.name).write_text(original.read_text() + "\n-- nachträglich verändert\n")
    monkeypatch.setattr(migration, "ROOT", tmp_path)
    with pytest.raises(RuntimeError, match="Migration verändert"):
        migration.migrate(setup["admin_url"])


def test_ownership_immutable_in_runtime_db(setup: dict[str, Any]) -> None:
    with psycopg.connect(setup["runtime_url"]) as db:
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            db.execute(
                "UPDATE notes SET account_id = %s WHERE id = %s",
                (setup["ids"]["b"], setup["ids"]["na"]),
            )


def test_authentication_not_enabled_by_client_data(setup: dict[str, Any]) -> None:
    with TestClient(create_app(setup["runtime_url"])) as client:
        response = client.post(
            "/auth/login?synthetic_test_harness=true",
            json={"login": "a", "password": PASSWORD, "device_proof": setup["proof"] + "a"},
            headers={"X-Test-Harness": "true", "X-Verified": "true"},
        )
        assert response.status_code == 503


def test_openapi_snapshot_matches(setup: dict[str, Any]) -> None:
    import json
    from pathlib import Path

    expected = json.loads((Path(__file__).resolve().parents[1] / "openapi.json").read_text())
    assert expected == setup["app"].openapi()
