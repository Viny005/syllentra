"""Lokale Endabläufe: PostgreSQL und getrennte interne OTP-/Offlinekanäle."""

import secrets
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from typing import Any

import psycopg
import pytest
from fastapi.testclient import TestClient
from helpers import NEW_PASSWORD, PASSWORD, account, registration, verify

from syllentra_backend.identity import DEVICE, PREAUTH, SESSION


def test_registration_duplicate_normalization_and_no_privileges(env: Any) -> None:
    owner, other = env["browser"](), env["browser"]()
    ref = registration(env, owner, "  Alice@EXAMPLE.TEST ")
    assert owner.get("/notes").status_code == 401
    for _ in range(2):
        assert (
            other.post(
                "/auth/register", json={"email": "alice@example.test", "password": NEW_PASSWORD}
            ).status_code
            == 202
        )
    with psycopg.connect(env["admin"]) as db:
        rows = db.execute("SELECT login,kind,verification,password_hash FROM accounts").fetchall()
        assert len(rows) == 1 and rows[0][:3] == ("alice@example.test", "user", "pending")
        assert rows[0][3].startswith("$argon2id$")
    verify(env, owner, ref)
    assert (
        owner.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    assert (
        other.post(
            "/auth/register",
            json={"email": "evil@example.test", "password": PASSWORD, "kind": "administrator"},
        ).status_code
        == 422
    )


@pytest.mark.parametrize("case", ["wrong", "expired", "another_browser", "reused"])
def test_otp_failures(env: Any, case: str) -> None:
    c = env["browser"]()
    ref = registration(env, c)
    code = env["mail"].take(ref)
    if case == "wrong":
        code = "00000000" if code != "00000000" else "11111111"
    elif case == "expired":
        env["now"][0] += timedelta(minutes=6)
    elif case == "another_browser":
        c = env["browser"]()
    else:
        verify(env, c, ref)
    assert c.post("/auth/verify", json={"challenge_id": ref, "code": code}).status_code == 400
    assert c.get("/notes").status_code == 401


def test_attempt_counter_commits_and_resend_cannot_reset(env: Any) -> None:
    c = env["browser"]()
    ref = registration(env, c)
    code = env["mail"].take(ref)
    wrong = "00000000" if code != "00000000" else "11111111"
    for _ in range(5):
        assert c.post("/auth/verify", json={"challenge_id": ref, "code": wrong}).status_code == 400
    with psycopg.connect(env["admin"]) as db:
        assert (
            db.execute("SELECT attempts FROM identity_challenges WHERE id=%s", (ref,)).fetchone()[0]
            == 5
        )
    env["now"][0] += timedelta(seconds=61)
    count = len(env["mail"].messages)
    assert c.post("/auth/resend", json={"challenge_id": ref}).status_code == 202
    assert len(env["mail"].messages) == count
    assert c.post("/auth/verify", json={"challenge_id": ref, "code": code}).status_code == 400


def test_resend_replaces_code_and_limits_sends(env: Any) -> None:
    c = env["browser"]()
    ref = registration(env, c)
    old = env["mail"].take(ref)
    assert c.post("/auth/resend", json={"challenge_id": ref}).status_code == 202
    assert len(env["mail"].messages) == 1
    for _ in range(3):
        env["now"][0] += timedelta(seconds=61)
        assert c.post("/auth/resend", json={"challenge_id": ref}).status_code == 202
    assert len(env["mail"].messages) == 3
    latest = env["mail"].take(ref)
    assert old != latest
    assert c.post("/auth/verify", json={"challenge_id": ref, "code": old}).status_code == 400
    verify(env, c, ref)


def test_concurrent_otp_single_use(env: Any) -> None:
    original = env["browser"]()
    ref = registration(env, original)
    code = env["mail"].take(ref)
    clients = [env["browser"](), env["browser"]()]
    for c in clients:
        c.cookies.set(PREAUTH, original.cookies.get(PREAUTH), domain="testserver.local", path="/")
    with ThreadPoolExecutor(max_workers=2) as pool:
        statuses = list(
            pool.map(
                lambda c: (
                    c.post("/auth/verify", json={"challenge_id": ref, "code": code}).status_code
                ),
                clients,
            )
        )
    assert sorted(statuses) == [200, 400]


def test_new_device_requires_approval_and_binding(env: Any) -> None:
    trusted, new, foreign = env["browser"](), env["browser"](), env["browser"]()
    account(env, trusted)
    account(env, foreign, "bob@example.test")
    r = new.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert r.status_code == 202 and not new.cookies.get(SESSION)
    ref = r.json()["challenge_id"]
    assert new.get("/notes").status_code == 401
    assert new.post("/auth/device/complete", json={"challenge_id": ref}).status_code == 400
    assert (
        foreign.post(f"/devices/requests/{ref}/approve", json={"password": PASSWORD}).status_code
        == 404
    )
    assert len(trusted.get("/devices/requests").json()) == 1
    assert (
        trusted.post(f"/devices/requests/{ref}/approve", json={"password": PASSWORD}).status_code
        == 200
    )
    assert foreign.post("/auth/device/complete", json={"challenge_id": ref}).status_code == 400
    assert new.post("/auth/device/complete", json={"challenge_id": ref}).status_code == 200
    assert new.post("/auth/device/complete", json={"challenge_id": ref}).status_code == 400
    assert (
        new.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    assert new.get("/session").json()["account_id"] == trusted.get("/session").json()["account_id"]


def test_device_revocation_and_expiry(env: Any) -> None:
    c = env["browser"]()
    account(env, c)
    device = c.get("/devices").json()[0]["id"]
    assert c.post(f"/devices/{device}/revoke", json={"password": PASSWORD}).status_code == 200
    assert c.get("/session").status_code == 401
    assert (
        c.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 202
    )
    with psycopg.connect(env["admin"]) as db:
        db.execute(
            "UPDATE devices SET authorized=true, expires_at=%s",
            (env["now"][0] - timedelta(seconds=1),),
        )
    assert c.get("/session").status_code == 401


def test_two_proof_recovery_revokes_sessions_devices_and_old_code(env: Any) -> None:
    old, recovering = env["browser"](), env["browser"]()
    account(env, old)
    session_response = old.get("/session")
    assert session_response.status_code == 200, session_response.json().get("detail")
    aid = session_response.json()["account_id"]
    personal = env["offline"].take(aid)
    ref = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    code = env["mail"].take(ref)
    assert not any(m["secret"] == personal for m in env["mail"].messages)
    payload = dict(
        challenge_id=ref,
        code=code,
        recovery_code=secrets.token_urlsafe(32),
        new_password=NEW_PASSWORD,
    )
    assert recovering.post("/auth/recover/complete", json=payload).status_code == 400
    assert old.get("/session").status_code == 200
    payload["recovery_code"] = personal
    assert recovering.post("/auth/recover/complete", json=payload).status_code == 200
    assert old.get("/session").status_code == 401
    assert recovering.post("/auth/recover/complete", json=payload).status_code == 400
    assert (
        recovering.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 401
    )
    assert (
        recovering.post(
            "/auth/login", json={"login": "alice@example.test", "password": NEW_PASSWORD}
        ).status_code
        == 200
    )
    assert env["offline"].take(aid) != personal
    assert any(m["purpose"] == "security-notification" for m in env["mail"].messages)


@pytest.mark.parametrize("operation", ["login", "recover"])
def test_enumeration(env: Any, operation: str) -> None:
    owner = env["browser"]()
    account(env, owner)
    c = env["browser"]()
    results = []
    for email in ["alice@example.test", "unknown@example.test"]:
        body = (
            dict(login=email, password=NEW_PASSWORD) if operation == "login" else dict(email=email)
        )
        r = c.post("/auth/" + operation, json=body)
        results.append(
            (r.status_code, set(r.json()), r.json().get("status"), r.json().get("detail"))
        )
    assert results[0] == results[1]


def test_secure_cookies_csrf_https_and_session_fixation(env: Any) -> None:
    c = env["browser"]()
    verify(env, c, registration(env, c))
    fake = secrets.token_urlsafe(32)
    c.cookies.set(SESSION, fake, domain="testserver.local", path="/")
    r = c.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert r.status_code == 200 and c.cookies.get(SESSION) != fake
    assert any(
        "HttpOnly" in h and "Secure" in h and "SameSite=strict" in h
        for h in r.headers.get_list("set-cookie")
    )
    assert "access_token" not in r.json()
    assert c.post("/auth/logout", headers={"X-CSRF-Token": "invalid"}).status_code == 403
    assert c.post("/auth/logout", headers={"Origin": "https://attacker.invalid"}).status_code == 403
    assert c.get("/auth/csrf", headers={"Sec-Fetch-Site": "cross-site"}).status_code == 403
    assert c.get("/session").status_code == 200
    assert c.post("/auth/logout").status_code == 204
    assert c.get("/session").status_code == 401
    with TestClient(env["app"], base_url="http://testserver") as plain:
        assert plain.get("/health").status_code == 403


def test_multiple_sessions_ownership_and_revocation(env: Any) -> None:
    c, other = env["browser"](), env["browser"]()
    account(env, c)
    before = c.cookies.get(SESSION)
    assert (
        c.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    assert c.cookies.get(SESSION) != before
    sessions = c.get("/sessions").json()
    assert len(sessions) == 2 and all(set(s) == {"id", "expires_at", "revoked"} for s in sessions)
    account(env, other, "bob@example.test")
    target = sessions[0]["id"]
    assert other.post(f"/sessions/{target}/revoke").status_code == 404
    assert c.post(f"/sessions/{target}/revoke").status_code == 200


def test_mfa_required_suspension_and_admin_remain_blocked(env: Any) -> None:
    c = env["browser"]()
    account(env, c)
    with psycopg.connect(env["admin"]) as db:
        db.execute("UPDATE accounts SET mfa_required=true")
    assert c.get("/session").status_code == 401
    assert (
        c.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 401
    )
    with psycopg.connect(env["admin"]) as db:
        db.execute("UPDATE accounts SET mfa_required=false, status='suspended'")
    assert c.get("/session").status_code == 401
    assert (
        c.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 401
    )
    assert c.get("/administration").status_code == 401


def test_db_and_audit_have_no_raw_secrets(env: Any) -> None:
    c = env["browser"]()
    ref = registration(env, c)
    code = env["mail"].take(ref)
    verify(env, c, ref)
    assert (
        c.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    personal = env["offline"].take(c.get("/session").json()["account_id"])
    with psycopg.connect(env["admin"]) as db:
        content = str(
            [
                db.execute(f"SELECT * FROM {table}").fetchall()  # noqa: S608 -- feste Liste
                for table in [
                    "accounts",
                    "identity_challenges",
                    "sessions",
                    "devices",
                    "recovery_codes",
                    "security_events",
                ]
            ]
        )
        events = str(db.execute("SELECT * FROM security_events").fetchall())
    for secret in [code, PASSWORD, c.cookies.get(SESSION), c.cookies.get(DEVICE), personal]:
        assert secret and secret not in content
    assert "alice@example.test" not in events


def test_validation_and_db_no_admin_creation(env: Any) -> None:
    c = env["browser"]()
    for email in [
        "outside@domain.invalid",
        "a@example.test\nInjected: value",
        "ümlaut@example.test",
    ]:
        r = c.post("/auth/register", json={"email": email, "password": PASSWORD})
        assert r.status_code == 422 and PASSWORD not in r.text
    with psycopg.connect(env["runtime"]) as db:
        with pytest.raises(psycopg.errors.InsufficientPrivilege):
            db.execute(
                "INSERT INTO accounts (id,login,password_hash,kind,verification,status) "
                "VALUES (gen_random_uuid(),'root@example.test','x',"
                "'administrator','verified','active')"
            )


def test_real_verified_accounts_isolation_flags_and_recovery_expiry(env: Any) -> None:
    from uuid import uuid4

    a, b = env["browser"](), env["browser"]()
    account(env, a)
    account(env, b, "bob@example.test")
    aid, bid = a.get("/session").json()["account_id"], b.get("/session").json()["account_id"]
    na, nb = uuid4(), uuid4()
    with psycopg.connect(env["admin"]) as db:
        for identifier, owner in [(na, aid), (nb, bid)]:
            db.execute(
                "INSERT INTO notes VALUES (%s,%s,'Test','Nur synthetisch',NULL)",
                (identifier, owner),
            )
    assert a.get(f"/notes/{na}").status_code == 200
    assert a.get(f"/notes/{nb}").status_code == 404
    assert a.patch(f"/notes/{nb}", json={"title": "Angriff", "body": "x"}).status_code == 404
    with psycopg.connect(env["admin"]) as db:
        db.execute("UPDATE capabilities SET mode='hidden' WHERE name='notes'")
    assert a.get(f"/notes/{na}").status_code == 403
    assert a.get("/administration").status_code == 403
    recovering = env["browser"]()
    ref = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    with psycopg.connect(env["admin"]) as db:
        db.execute(
            "UPDATE recovery_codes SET expires_at=%s WHERE account_id=%s", (env["now"][0], aid)
        )
    assert (
        recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref,
                "code": env["mail"].take(ref),
                "recovery_code": env["offline"].take(aid),
                "new_password": NEW_PASSWORD,
            },
        ).status_code
        == 400
    )


def test_private_file_channel_cleanup_and_permissions(tmp_path: Any) -> None:
    import os

    from syllentra_backend.delivery import LocalFileChannel

    now = [0.0]
    path = tmp_path / ".local/mail/otp.jsonl"
    channel = LocalFileChannel(path, clock=lambda: now[0])
    channel.deliver("a@example.test", "email", "reference", "synthetic-private-code")
    assert path.stat().st_mode & 0o777 == 0o600
    now[0] = 601
    channel.prune()
    assert path.read_text() == ""
    os.chmod(path, 0o644)
    with pytest.raises(ValueError, match="0600"):
        channel.deliver("a@example.test", "email", "reference", "synthetic-private-code")


def test_pending_registration_can_restart_only_with_original_password(env: Any) -> None:
    first, second = env["browser"](), env["browser"]()
    old_ref = registration(env, first)
    old_code = env["mail"].take(old_ref)
    new_ref = registration(env, second)
    assert old_ref != new_ref
    assert (
        first.post("/auth/verify", json={"challenge_id": old_ref, "code": old_code}).status_code
        == 400
    )
    verify(env, second, new_ref)
    with psycopg.connect(env["admin"]) as db:
        assert db.execute("SELECT count(*) FROM accounts").fetchone()[0] == 1


def test_parallel_session_reads_then_revocation(env: Any) -> None:
    owner = env["browser"]()
    account(env, owner)
    token = owner.cookies.get(SESSION)
    clients = [env["browser"]() for _ in range(4)]
    for c in clients:
        c.headers.update({"Authorization": "Bearer " + str(token)})
    with ThreadPoolExecutor(max_workers=4) as pool:
        assert list(pool.map(lambda c: c.get("/session").status_code, clients)) == [200] * 4
    assert owner.post("/auth/logout").status_code == 204
    for c in clients:
        assert c.get("/session").status_code == 401
