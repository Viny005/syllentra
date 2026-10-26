"""Prioritäre Sicherheits-, Grenz-, Parallelitäts- und Regressionsprüfungen (Mission 12–14).

R1 (persönlicher Offline-Recoverycode ohne automatischen 7-Tage-Ablauf), R2, R3, R4 ( kontrollierter
Reset unverifizierter pending-Konten ab 24 Stunden), R5 und R12 sind als Regressionsprüfungen
gegen die vom Projektinhaber freigegebenen Sicherheitsregeln abgesichert.
"""

import secrets
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta
from typing import Any
from uuid import UUID

import psycopg
import pytest
from fastapi.testclient import TestClient
from helpers import NEW_PASSWORD, PASSWORD, account, registration, verify

from syllentra_backend.api import create_app
from syllentra_backend.delivery import MemoryChannel
from syllentra_backend.identity import DEVICE, PREAUTH, SESSION, LocalIdentity
from syllentra_backend.security import digest


def test_more_than_50_sessions_listing_truncation_and_revocation(env: Any) -> None:
    """Regressionsprüfung R3: aktive Sitzungen zuerst, Widerrufsstatus und Paginierung."""
    c = env["browser"]()
    account(env, c)
    aid = UUID(c.get("/session").json()["account_id"])
    device_id = UUID(c.get("/devices").json()[0]["id"])
    current_session_id = UUID(c.get("/sessions").json()[0]["id"])
    now = env["now"][0]
    low_ids = [UUID(f"00000000-0000-4000-8000-{i:012x}") for i in range(1, 51)]
    high_active_id = UUID("ffffffff-ffff-4fff-8fff-ffffffffffff")
    expired_unrevoked_id = UUID("eeeeeeee-eeee-4eee-8eee-eeeeeeeeeeee")
    high_token = secrets.token_urlsafe(32)
    with psycopg.connect(env["admin"]) as db:
        for sid in low_ids:
            db.execute(
                "INSERT INTO sessions (id, token_hash, account_id, device_id, expires_at, "
                "revoked, security_epoch) VALUES (%s,%s,%s,%s,%s,true,0)",
                (sid, digest(secrets.token_urlsafe(32)), aid, device_id, now - timedelta(hours=1)),
            )
        db.execute(
            "INSERT INTO sessions (id, token_hash, account_id, device_id, expires_at, "
            "revoked, security_epoch) VALUES (%s,%s,%s,%s,%s,false,0)",
            (high_active_id, digest(high_token), aid, device_id, now + timedelta(minutes=15)),
        )
        db.execute(
            "INSERT INTO sessions (id, token_hash, account_id, device_id, expires_at, "
            "revoked, security_epoch) VALUES (%s,%s,%s,%s,%s,false,0)",
            (
                expired_unrevoked_id,
                digest(secrets.token_urlsafe(32)),
                aid,
                device_id,
                now - timedelta(minutes=1),
            ),
        )
    listed = c.get("/sessions").json()
    assert len(listed) == 50
    # R3 behoben: aktuelle Sitzung und weitere aktive Sitzung stehen ganz oben (trotz großer UUID):
    assert UUID(listed[0]["id"]) == current_session_id
    assert listed[0]["revoked"] is False
    assert UUID(listed[1]["id"]) == high_active_id
    assert listed[1]["revoked"] is False
    # Abgelaufene Sitzung mit revoked=false in DB wird effektiv als revoked=True ausgewiesen:
    by_id = {UUID(row["id"]): row for row in listed}
    assert by_id[expired_unrevoked_id]["revoked"] is True
    # Paginierung über offset/limit liefert die restlichen Einträge deterministisch:
    page2 = c.get("/sessions?offset=50&limit=50").json()
    assert len(page2) == 3
    assert {UUID(r["id"]) for r in listed} | {UUID(r["id"]) for r in page2} == (
        {current_session_id, high_active_id, expired_unrevoked_id} | set(low_ids)
    )
    other = env["browser"]()
    other.headers.update({"Authorization": f"Bearer {high_token}"})
    assert other.get("/session").status_code == 200
    assert c.post(f"/sessions/{high_active_id}/revoke").status_code == 200
    assert other.get("/session").status_code == 401


def test_session_visibility_current_cookie_deletion_and_foreign_isolation(env: Any) -> None:
    """Sichtbarkeit und gezielter Widerruf eigener vs. fremder Sitzungen."""
    first, second, bob = env["browser"](), env["browser"](), env["browser"]()
    account(env, first)
    device_cookie = first.cookies.get(DEVICE)
    assert device_cookie
    second.cookies.set(DEVICE, device_cookie, domain="testserver.local", path="/")
    assert (
        second.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    account(env, bob, "bob@example.test")
    first_token = first.cookies.get(SESSION)
    second_token = second.cookies.get(SESSION)
    assert first_token and second_token and first_token != second_token
    with psycopg.connect(env["admin"]) as db:
        row_first = db.execute(
            "SELECT id FROM sessions WHERE token_hash = %s", (digest(first_token),)
        ).fetchone()
        row_second = db.execute(
            "SELECT id FROM sessions WHERE token_hash = %s", (digest(second_token),)
        ).fetchone()
        assert row_first and row_second
        first_id, second_id = str(row_first[0]), str(row_second[0])
    sessions = first.get("/sessions").json()
    assert {s["id"] for s in sessions} == {first_id, second_id}
    assert all(set(s) == {"id", "expires_at", "revoked"} for s in sessions)
    # Fremdes Konto sieht und widerruft keine Sitzung von Alice:
    assert bob.post(f"/sessions/{second_id}/revoke").status_code == 404
    assert second.get("/session").status_code == 200
    # Widerruf der Zweitsitzung lässt die aktuelle Erstsitzung samt Cookie intakt:
    r_other = first.post(f"/sessions/{second_id}/revoke")
    assert r_other.status_code == 200
    assert first.get("/session").status_code == 200
    assert second.get("/session").status_code == 401
    # Widerruf der eigenen aktuellen Sitzung löscht das Sitzungscookie und sperrt sofort:
    r_self = first.post(f"/sessions/{first_id}/revoke")
    assert r_self.status_code == 200
    assert any(SESSION in h for h in r_self.headers.get_list("set-cookie"))
    assert first.get("/session").status_code == 401


def test_device_expiration_exact_boundary(env: Any) -> None:
    """Exakte Ablauffrist eines Geräts: expires_at > clock() (strikt)."""
    c = env["browser"]()
    account(env, c)
    boundary = env["now"][0] + timedelta(days=7)
    with psycopg.connect(env["admin"]) as db:
        db.execute(
            "UPDATE sessions SET expires_at = %s",
            (boundary + timedelta(minutes=15),),
        )
    # 1 Mikrosekunde vor Ablauf: Sitzung und erneutes Login über dieses Gerät sind gültig.
    env["now"][0] = boundary - timedelta(microseconds=1)
    assert c.get("/session").status_code == 200
    assert (
        c.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    # Exakt auf der Grenze (expires_at == clock()): Gerät gilt als abgelaufen.
    env["now"][0] = boundary
    assert c.get("/session").status_code == 401
    relogin = c.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert relogin.status_code == 202
    assert relogin.json()["status"] == "device_verification_required"


def test_inactivity_over_7_days_characterizes_r1_recovery_and_device_lockout(env: Any) -> None:
    """Regressionsprüfung R1: Geräteablauf nach 7d unabhängig; Recovery nach 8, 30 und 90 Tagen."""
    c, recovering = env["browser"](), env["browser"]()
    account(env, c)
    aid = c.get("/session").json()["account_id"]
    personal = env["offline"].take(aid)
    with psycopg.connect(env["admin"]) as db:
        rc_row = db.execute(
            "SELECT used, revoked, expires_at FROM recovery_codes WHERE account_id = %s", (aid,)
        ).fetchone()
        assert rc_row == (False, False, None)
    # Nach 7 Tagen + 1s ist die Gerätebindung (7d) abgelaufen, der persönliche Recoverycode bleibt:
    env["now"][0] += timedelta(days=7, seconds=1)
    assert c.get("/session").status_code == 401
    login_res = c.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert login_res.status_code == 202
    assert login_res.json()["status"] == "device_verification_required"
    # Kontowiederherstellung nach 8 Tagen, 30 Tagen und 90 Tagen Inaktivität:
    passwords = [NEW_PASSWORD, PASSWORD + "-30d", PASSWORD + "-90d"]
    for idx, days in enumerate([8, 30, 90]):
        env["now"][0] += timedelta(days=days - (7 if idx == 0 else 0))
        ref = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
            "challenge_id"
        ]
        otp = env["mail"].take(ref)
        rec_res = recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref,
                "code": otp,
                "recovery_code": personal,
                "new_password": passwords[idx],
            },
        )
        assert rec_res.status_code == 200
        assert rec_res.json()["status"] == "recovered"
        # Bereits verbrauchter persönlicher Recoverycode wird bei Wiederverwendung strikt abgelehnt:
        ref_reuse = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
            "challenge_id"
        ]
        otp_reuse = env["mail"].take(ref_reuse)
        reuse_res = recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref_reuse,
                "code": otp_reuse,
                "recovery_code": personal,
                "new_password": PASSWORD + "-reuse",
            },
        )
        assert reuse_res.status_code == 400
        new_personal = env["offline"].take(aid)
        assert new_personal and new_personal != personal
        personal = new_personal
    # Nach erfolgreichem Recovery-Lauf bei 90 Tagen funktioniert das neue Passwort auf dem Gerät:
    assert (
        recovering.post(
            "/auth/login", json={"login": "alice@example.test", "password": passwords[-1]}
        ).status_code
        == 200
    )


def test_old_pending_account_blocks_different_password_and_allows_same_password_restart(
    env: Any,
) -> None:
    """Regressionsprüfung R4: Vor 24h gleiches Passwort; ab 24h und >24h sicherer Reset."""
    first, stranger, owner_retry, final_client = (
        env["browser"](),
        env["browser"](),
        env["browser"](),
        env["browser"](),
    )
    start = env["now"][0]
    old_ref = registration(env, first, "pending@example.test")
    old_otp = env["mail"].take(old_ref)
    # 1. OTP-Resend (+61s) und gleiches Passwort vor 24h verlängern pending_since NICHT:
    env["now"][0] = start + timedelta(seconds=61)
    assert first.post("/auth/resend", json={"challenge_id": old_ref}).status_code == 202
    _ = env["mail"].take(old_ref)
    env["now"][0] = start + timedelta(hours=12)
    r_same_early = owner_retry.post(
        "/auth/register", json={"email": "pending@example.test", "password": PASSWORD}
    )
    assert r_same_early.status_code == 202
    mid_ref = r_same_early.json()["challenge_id"]
    mid_otp = env["mail"].take(mid_ref)
    with psycopg.connect(env["admin"]) as db:
        ps_row = db.execute(
            "SELECT pending_since FROM accounts WHERE login = 'pending@example.test'"
        ).fetchone()
        assert ps_row and ps_row[0] == start
    # 2. 1 Sekunde vor 24h (24h - 1s): anderes Passwort erhält nur Fake-Challenge (kein OTP):
    env["now"][0] = start + timedelta(hours=24) - timedelta(seconds=1)
    before_messages = len(env["mail"].messages)
    r_before_24h = stranger.post(
        "/auth/register", json={"email": "pending@example.test", "password": NEW_PASSWORD}
    )
    assert r_before_24h.status_code == 202
    assert len(env["mail"].messages) == before_messages
    # 3. Exakt bei 24h: Reset mit neuem Passwort ist zulässig und entwertet frühere Challenges:
    env["now"][0] = start + timedelta(hours=24)
    r_at_24h = stranger.post(
        "/auth/register", json={"email": "pending@example.test", "password": NEW_PASSWORD}
    )
    assert r_at_24h.status_code == 202
    assert len(env["mail"].messages) == before_messages + 1
    reset_ref_24h = r_at_24h.json()["challenge_id"]
    reset_otp_24h = env["mail"].take(reset_ref_24h)
    # Alte Challenges und alte OTPs sind nach dem Reset ungültig (consumed + security_epoch):
    assert (
        first.post("/auth/verify", json={"challenge_id": old_ref, "code": old_otp}).status_code
        == 400
    )
    assert (
        owner_retry.post(
            "/auth/verify", json={"challenge_id": mid_ref, "code": mid_otp}
        ).status_code
        == 400
    )
    # 4. Nach >24h (z. B. +30 Tage nach dem ersten Reset) funktioniert ein weiterer Reset:
    env["now"][0] += timedelta(days=30)
    third_password = PASSWORD + "-final-owner"
    r_after_30d = final_client.post(
        "/auth/register", json={"email": "pending@example.test", "password": third_password}
    )
    assert r_after_30d.status_code == 202
    final_ref = r_after_30d.json()["challenge_id"]
    assert (
        stranger.post(
            "/auth/verify", json={"challenge_id": reset_ref_24h, "code": reset_otp_24h}
        ).status_code
        == 400
    )
    verify(env, final_client, final_ref)
    assert (
        final_client.post(
            "/auth/login", json={"login": "pending@example.test", "password": PASSWORD}
        ).status_code
        == 401
    )
    assert (
        final_client.post(
            "/auth/login", json={"login": "pending@example.test", "password": NEW_PASSWORD}
        ).status_code
        == 401
    )
    assert (
        final_client.post(
            "/auth/login", json={"login": "pending@example.test", "password": third_password}
        ).status_code
        == 200
    )
    # 5. Ein bereits verifiziertes Konto wird auch nach >24h NIEMALS durch /auth/register verändert:
    env["now"][0] += timedelta(days=30)
    msg_count = len(env["mail"].messages)
    r_verified = stranger.post(
        "/auth/register", json={"email": "pending@example.test", "password": NEW_PASSWORD}
    )
    assert r_verified.status_code == 202
    assert len(env["mail"].messages) == msg_count
    with psycopg.connect(env["admin"]) as db:
        v_row = db.execute(
            "SELECT verification, status FROM accounts WHERE login = 'pending@example.test'"
        ).fetchone()
        assert v_row == ("verified", "active")


def test_network_budget_shared_client_host_ignores_forwarded_headers(env: Any) -> None:
    """Regressionsprüfung R2: 100/min Budget ist pro Client-Kontext/Pfad isoliert."""
    legit = env["browser"]()
    account(env, legit, "legit@example.test")
    assert legit.post("/auth/logout").status_code == 204
    noisy = env["browser"]()
    # noisy schöpft sein eigenes 100/min Budget auf /auth/recover vollständig aus (101 Aufrufe):
    statuses = []
    for i in range(101):
        res = noisy.post(
            "/auth/recover",
            json={"email": f"noise{i}@example.test"},
            headers={"X-Forwarded-For": f"198.51.100.{i % 250 + 1}"},
        )
        statuses.append(res.status_code)
    assert statuses[:100] == [202] * 100
    assert statuses[100] == 429
    # R2 behoben: legit auf demselben Loopback-Host wird durch noisy NICHT kollektiv gesperrt:
    ok_login = legit.post(
        "/auth/login",
        json={"login": "legit@example.test", "password": PASSWORD},
        headers={"X-Forwarded-For": "203.0.113.99"},
    )
    assert ok_login.status_code == 200
    # /auth/logout ist zusätzlich vom Eingangs-Netzwerkbudget ausgenommen:
    assert legit.post("/auth/logout").status_code == 204
    # Nach Ablauf des 1-Minuten-Fensters ist auch noisy wieder entsperrt:
    env["now"][0] += timedelta(seconds=61)
    assert noisy.post("/auth/recover", json={"email": "noise0@example.test"}).status_code == 202


def test_per_address_budgets_and_enumeration_resistance(env: Any) -> None:
    """Regressionsprüfung R5 & Anti-Enumeration: Aufrufer-isolierte Budgets und Antwortformen."""
    alice, bob, probe = env["browser"](), env["browser"](), env["browser"]()
    account(env, alice, "alice@example.test")
    account(env, bob, "bob@example.test")
    registration(env, probe, "pending@example.test")
    # 1. Identische Antwortstruktur bei Registrierung für verifiziert, pending und unbekannt:
    reg_shapes = []
    for addr in ["alice@example.test", "pending@example.test", "fresh@example.test"]:
        r = probe.post("/auth/register", json={"email": addr, "password": NEW_PASSWORD})
        reg_shapes.append((r.status_code, set(r.json()), r.json()["status"]))
    expected_shape = (202, {"status", "challenge_id"}, "accepted")
    assert reg_shapes[0] == reg_shapes[1] == reg_shapes[2] == expected_shape
    # 2. Recovery-Budget (3/min pro E-Mail + Aufrufer): probe läuft für alice@example.test in 429,
    # aber alice selbst bleibt handlungsfähig (R5 behoben) und bob@example.test ist unberührt:
    for i in range(4):
        r = probe.post("/auth/recover", json={"email": "alice@example.test"})
        assert r.status_code == (202 if i < 3 else 429)
    assert alice.post("/auth/recover", json={"email": "alice@example.test"}).status_code == 202
    assert probe.post("/auth/recover", json={"email": "bob@example.test"}).status_code == 202
    # 3. Konto-Budget für Gerätewiderruf (10/min pro account_id):
    device_id = alice.get("/devices").json()[0]["id"]
    for i in range(11):
        r = alice.post(f"/devices/{device_id}/revoke", json={"password": NEW_PASSWORD})
        assert r.status_code == (400 if i < 10 else 429)
    # Selbst mit korrektem Passwort greift das 429-Budget bis zum Ablauf der Minute:
    revoke_path = f"/devices/{device_id}/revoke"
    assert alice.post(revoke_path, json={"password": PASSWORD}).status_code == 429
    env["now"][0] += timedelta(seconds=61)
    assert alice.post(revoke_path, json={"password": PASSWORD}).status_code == 200


def test_concurrent_account_recoveries_single_winner(env: Any) -> None:
    """Gleichzeitige Kontowiederherstellungen: exakt ein Gewinner durch FOR-UPDATE-Sperrkette."""
    owner, init_client = env["browser"](), env["browser"]()
    account(env, owner)
    aid = owner.get("/session").json()["account_id"]
    personal = env["offline"].take(aid)
    ref = init_client.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    otp = env["mail"].take(ref)
    preauth = init_client.cookies.get(PREAUTH)
    assert preauth
    contenders = [env["browser"](), env["browser"]()]
    for c in contenders:
        c.cookies.set(PREAUTH, preauth, domain="testserver.local", path="/")
    payload = {
        "challenge_id": ref,
        "code": otp,
        "recovery_code": personal,
        "new_password": NEW_PASSWORD,
    }
    with ThreadPoolExecutor(max_workers=2) as pool:
        statuses = list(
            pool.map(
                lambda c: c.post("/auth/recover/complete", json=payload).status_code,
                contenders,
            )
        )
    assert sorted(statuses) == [200, 400]
    with psycopg.connect(env["admin"]) as db:
        epoch = db.execute("SELECT security_epoch FROM accounts WHERE id = %s", (aid,)).fetchone()
        assert epoch and epoch[0] == 1


def test_recovery_correct_otp_with_wrong_personal_code_increments_attempts(env: Any) -> None:
    """Korrektes E-Mail-OTP + falscher persönlicher Code zählt Fehlversuche und protokolliert."""
    owner, rec = env["browser"](), env["browser"]()
    account(env, owner)
    aid = owner.get("/session").json()["account_id"]
    personal = env["offline"].take(aid)
    ref = rec.post("/auth/recover", json={"email": "alice@example.test"}).json()["challenge_id"]
    otp = env["mail"].take(ref)
    wrong_personal = secrets.token_urlsafe(32)
    for expected_attempts in range(1, 5):
        r = rec.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref,
                "code": otp,
                "recovery_code": wrong_personal,
                "new_password": NEW_PASSWORD,
            },
        )
        assert r.status_code == 400 and r.json()["status"] == "recovery_failed"
        with psycopg.connect(env["admin"]) as db:
            attempts = db.execute(
                "SELECT attempts, consumed FROM identity_challenges WHERE id = %s", (ref,)
            ).fetchone()
            assert attempts == (expected_attempts, False)
    # Alte Sitzung ist weiterhin aktiv; 5. Versuch mit korrektem persönlichem Code gelingt:
    assert owner.get("/session").status_code == 200
    ok = rec.post(
        "/auth/recover/complete",
        json={
            "challenge_id": ref,
            "code": otp,
            "recovery_code": personal,
            "new_password": NEW_PASSWORD,
        },
    )
    assert ok.status_code == 200
    assert owner.get("/session").status_code == 401
    with psycopg.connect(env["admin"]) as db:
        denied = db.execute(
            "SELECT count(*) FROM security_events "
            "WHERE account_id = %s AND event = 'recovery_denied'",
            (aid,),
        ).fetchone()
        assert denied and denied[0] == 4


def test_simultaneous_login_and_device_revocation(env: Any) -> None:
    """Gleichzeitiges Login und Gerätewiderruf hinterlassen niemals eine gültige Sitzung."""
    for _ in range(5):
        email = f"race{secrets.token_hex(3)}@example.test"
        active, logging_in = env["browser"](), env["browser"]()
        account(env, active, email)
        proof = active.cookies.get(DEVICE)
        assert proof
        logging_in.cookies.set(DEVICE, proof, domain="testserver.local", path="/")
        device_id = active.get("/devices").json()[0]["id"]

        def do_login(c: TestClient = logging_in, addr: str = email) -> int:
            res = c.post("/auth/login", json={"login": addr, "password": PASSWORD})
            return int(res.status_code)

        def do_revoke(c: TestClient = active, dev: str = device_id) -> int:
            res = c.post(f"/devices/{dev}/revoke", json={"password": PASSWORD})
            return int(res.status_code)

        with ThreadPoolExecutor(max_workers=2) as pool:
            f_login = pool.submit(do_login)
            f_revoke = pool.submit(do_revoke)
            login_status, revoke_status = f_login.result(), f_revoke.result()
        assert revoke_status == 200
        assert login_status in {200, 202}
        # Unabhängig von der Reihenfolge der Sperre (accounts FOR UPDATE) ist das Gerät widerrufen
        # und jede auf diesem Gerät ausgestellte Sitzung bei /session ungültig (401):
        assert active.get("/session").status_code == 401
        assert logging_in.get("/session").status_code == 401


def test_simultaneous_device_approval_and_authority_revocation(env: Any) -> None:
    """Gleichzeitige Gerätefreigabe und Widerruf des freigebenden Geräts verhindern Abschluss."""
    trusted, revoker, candidate = env["browser"](), env["browser"](), env["browser"]()
    account(env, trusted)
    proof = trusted.cookies.get(DEVICE)
    assert proof
    revoker.cookies.set(DEVICE, proof, domain="testserver.local", path="/")
    assert (
        revoker.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    authority_id = trusted.get("/devices").json()[0]["id"]
    req = candidate.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert req.status_code == 202
    ref = req.json()["challenge_id"]
    with ThreadPoolExecutor(max_workers=2) as pool:
        f_approve = pool.submit(
            lambda: (
                trusted.post(
                    f"/devices/requests/{ref}/approve", json={"password": PASSWORD}
                ).status_code
            )
        )
        f_revoke = pool.submit(
            lambda: (
                revoker.post(
                    f"/devices/{authority_id}/revoke", json={"password": PASSWORD}
                ).status_code
            )
        )
        approve_status, revoke_status = f_approve.result(), f_revoke.result()
    assert revoke_status == 200
    assert approve_status in {200, 400, 401}
    # finish_device prüft, ob approved_by_device noch autorisiert ist -> zwingend 400:
    assert candidate.post("/auth/device/complete", json={"challenge_id": ref}).status_code == 400
    assert not candidate.cookies.get(DEVICE)


def test_repeated_login_then_session_read_transaction_and_cookie_coherence(env: Any) -> None:
    """Mission-10-Szenario isoliert: 25 Zyklen Login -> /session + parallele Sitzungswechsel."""
    c = env["browser"]()
    account(env, c)
    seen_tokens: set[str] = set()
    for _ in range(25):
        env["now"][0] += timedelta(seconds=7)  # unterhalb 10/min Login-Budget bleiben
        r = c.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
        assert r.status_code == 200
        token = c.cookies.get(SESSION)
        assert token and len(token) == 43 and token not in seen_tokens
        seen_tokens.add(token)
        # Unmittelbar nach Antwort ist die Transaktion committet und die Sitzung lesbar:
        me = c.get("/session")
        assert me.status_code == 200 and me.json()["assurance"] == "local-synthetic-otp"
    with psycopg.connect(env["admin"]) as db:
        count = db.execute("SELECT count(*) FROM sessions").fetchone()
        assert count and count[0] == 26  # 1 aus account() + 25 aus Schleife


@pytest.mark.parametrize(
    ("base_url", "client_addr", "headers", "expected"),
    [
        ("http://testserver", ("127.0.0.1", 50000), {}, (403, "local_https_required")),
        ("https://testserver", ("192.0.2.25", 50000), {}, (403, "local_https_required")),
        (
            "https://testserver",
            ("127.0.0.1", 50000),
            {"Sec-Fetch-Site": "cross-site"},
            (403, "origin_denied"),
        ),
        (
            "https://testserver",
            ("127.0.0.1", 50000),
            {"Origin": "https://evil.example.test"},
            (403, "origin_denied"),
        ),
        ("https://evil.invalid", ("127.0.0.1", 50000), {}, (400, None)),
    ],
)
def test_environment_boundaries_between_test_and_normal_runtime(
    env: Any,
    base_url: str,
    client_addr: tuple[str, int],
    headers: dict[str, str],
    expected: tuple[int, str | None],
) -> None:
    """Scharfe Trennung zwischen lokalem Test-/Synthetikmodus und Normalbetrieb."""
    with TestClient(env["app"], base_url=base_url, client=client_addr) as c:
        res = c.get("/health", headers=headers)
        assert res.status_code == expected[0]
        if expected[1] is not None:
            assert res.json() == {"detail": expected[1]}
    # Im Normalbetrieb (identity=None) sind Browser-Origin und /auth/* strikt gesperrt:
    normal_app = create_app(env["runtime"])
    with TestClient(normal_app, base_url="https://testserver") as normal:
        assert normal.get("/health").json() == {
            "status": "local-experimental",
            "authentication": "unavailable",
        }
        origin_headers = {"Origin": "https://127.0.0.1:5174"}
        assert normal.get("/health", headers=origin_headers).status_code == 403
        assert normal.get("/auth/csrf").status_code == 503
        assert (
            normal.post(
                "/auth/register", json={"email": "alice@example.test", "password": PASSWORD}
            ).status_code
            == 503
        )
    # LocalIdentity verweigert geteilte Kanäle und zu kurzen Pepper:
    shared_channel = MemoryChannel()
    with pytest.raises(ValueError, match="Identitätsprobe"):
        LocalIdentity(secrets.token_bytes(32), shared_channel, shared_channel).validate(
            env["runtime"]
        )
    with pytest.raises(ValueError, match="Identitätsprobe"):
        LocalIdentity(b"short-pepper", MemoryChannel(), MemoryChannel()).validate(env["runtime"])


def test_devices_sorting_effective_authorization_and_pagination(env: Any) -> None:
    """Regressionsprüfung R3 für GET /devices: Sortierung, Autorisierung und Paginierung."""
    c = env["browser"]()
    account(env, c)
    aid = UUID(c.get("/session").json()["account_id"])
    current_device_id = UUID(c.get("/devices").json()[0]["id"])
    now = env["now"][0]
    low_ids = [UUID(f"00000000-0000-4000-8000-{i:012x}") for i in range(1, 51)]
    high_active_id = UUID("ffffffff-ffff-4fff-8fff-ffffffffffff")
    expired_flag_true_id = UUID("dddddddd-dddd-4ddd-8ddd-dddddddddddd")
    with psycopg.connect(env["admin"]) as db:
        for did in low_ids:
            db.execute(
                "INSERT INTO devices (id, account_id, proof_hash, authorized, expires_at, "
                "security_epoch) VALUES (%s,%s,%s,false,%s,0)",
                (did, aid, digest(secrets.token_urlsafe(32)), now - timedelta(days=1)),
            )
        db.execute(
            "INSERT INTO devices (id, account_id, proof_hash, authorized, expires_at, "
            "security_epoch) VALUES (%s,%s,%s,true,%s,0)",
            (high_active_id, aid, digest(secrets.token_urlsafe(32)), now + timedelta(days=7)),
        )
        db.execute(
            "INSERT INTO devices (id, account_id, proof_hash, authorized, expires_at, "
            "security_epoch) VALUES (%s,%s,%s,true,%s,0)",
            (
                expired_flag_true_id,
                aid,
                digest(secrets.token_urlsafe(32)),
                now - timedelta(seconds=1),
            ),
        )
    page1 = c.get("/devices").json()
    assert len(page1) == 50
    assert UUID(page1[0]["id"]) == current_device_id and page1[0]["authorized"] is True
    assert UUID(page1[1]["id"]) == high_active_id and page1[1]["authorized"] is True
    by_id = {UUID(r["id"]): r for r in page1}
    assert by_id[expired_flag_true_id]["authorized"] is False
    page2 = c.get("/devices?offset=50&limit=50").json()
    assert len(page2) == 3
    assert {UUID(r["id"]) for r in page1} | {UUID(r["id"]) for r in page2} == (
        {current_device_id, high_active_id, expired_flag_true_id} | set(low_ids)
    )


def test_targeted_login_and_register_caller_isolation_and_recovery_challenge_preservation(
    env: Any,
) -> None:
    """Regressionsprüfung R5: fremde Fehlversuche sperren Besitzer nicht; Recovery bleibt gültig."""
    alice, probe, pending_owner = env["browser"](), env["browser"](), env["browser"]()
    account(env, alice, "alice@example.test")
    aid = alice.get("/session").json()["account_id"]
    personal = env["offline"].take(aid)
    assert alice.post("/auth/logout").status_code == 204
    # 1. Fremder Aufrufer schöpft sein Login-Budget (10/min) für alice@example.test aus:
    for i in range(11):
        r = probe.post(
            "/auth/login", json={"login": "alice@example.test", "password": NEW_PASSWORD}
        )
        assert r.status_code == (401 if i < 10 else 429)
    # Alice kann sich auf ihrem autorisierten Gerät trotzdem anmelden:
    assert (
        alice.post(
            "/auth/login", json={"login": "alice@example.test", "password": PASSWORD}
        ).status_code
        == 200
    )
    # 2. Fremder Aufrufer schöpft sein Register-Budget (10/min) für pending@example.test aus:
    first_ref = registration(env, pending_owner, "pending@example.test")
    _ = env["mail"].take(first_ref)
    for i in range(11):
        r = probe.post(
            "/auth/register", json={"email": "pending@example.test", "password": NEW_PASSWORD}
        )
        assert r.status_code == (202 if i < 10 else 429)
    # Besitzer kann mit korrektem Passwort weiterhin seine Verifikation erneuern:
    retry = pending_owner.post(
        "/auth/register", json={"email": "pending@example.test", "password": PASSWORD}
    )
    assert retry.status_code == 202
    verify(env, pending_owner, retry.json()["challenge_id"])
    # 3. Laufende Kontowiederherstellung wird durch fremdes POST /auth/recover nicht entwertet:
    rec_browser = env["browser"]()
    ref = rec_browser.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    otp = env["mail"].take(ref)
    # Unauthentifizierter Dritter stößt parallel /auth/recover für dieselbe Adresse an:
    interfere = probe.post("/auth/recover", json={"email": "alice@example.test"})
    assert interfere.status_code == 202
    _ = env["mail"].take(interfere.json()["challenge_id"])
    # Ursprüngliche Challenge von rec_browser bleibt einlösbar:
    complete = rec_browser.post(
        "/auth/recover/complete",
        json={
            "challenge_id": ref,
            "code": otp,
            "recovery_code": personal,
            "new_password": NEW_PASSWORD,
        },
    )
    assert complete.status_code == 200


def test_approve_device_verifies_session_and_device_state_and_rejects_duplicate_approval(
    env: Any,
) -> None:
    """Regressionsprüfung R12: approve_device prüft Sitzung/Gerät und sperrt Doppelfreigabe."""
    from psycopg.rows import dict_row

    from syllentra_backend.identity import IdentityService

    trusted, candidate = env["browser"](), env["browser"]()
    account(env, trusted)
    aid = UUID(trusted.get("/session").json()["account_id"])
    device_id = UUID(trusted.get("/devices").json()[0]["id"])
    session_token = trusted.cookies.get(SESSION)
    assert session_token
    session_hash = digest(session_token)
    req = candidate.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert req.status_code == 202
    ref = UUID(req.json()["challenge_id"])
    service = IdentityService(
        LocalIdentity(secrets.token_bytes(32), env["mail"], env["offline"]),
        lambda: env["now"][0],
    )
    # 1. Direktaufruf mit widerrufener Sitzung darf Challenge NICHT freigeben:
    with psycopg.connect(env["admin"], row_factory=dict_row) as db:
        db.execute("UPDATE sessions SET revoked = true WHERE token_hash = %s", (session_hash,))
        res_revoked = service.approve_device(db, aid, session_hash, ref, PASSWORD, device_id)
        assert res_revoked.status_code == 400
        chk = db.execute(
            "SELECT approved FROM identity_challenges WHERE id = %s", (ref,)
        ).fetchone()
        assert chk and chk["approved"] is False
        # Sitzung wiederherstellen, aber freigebendes Gerät widerrufen -> ebenfalls 400:
        db.execute("UPDATE sessions SET revoked = false WHERE token_hash = %s", (session_hash,))
        db.execute("UPDATE devices SET authorized = false WHERE id = %s", (device_id,))
        res_dev_revoked = service.approve_device(db, aid, session_hash, ref, PASSWORD, device_id)
        assert res_dev_revoked.status_code == 400
        chk2 = db.execute(
            "SELECT approved FROM identity_challenges WHERE id = %s", (ref,)
        ).fetchone()
        assert chk2 and chk2["approved"] is False
        db.execute("UPDATE devices SET authorized = true WHERE id = %s", (device_id,))
    # 2. Reguläre Freigabe über HTTP gelingt einmalig (200), Zweitversuch liefert 404:
    first_approve = trusted.post(f"/devices/requests/{ref}/approve", json={"password": PASSWORD})
    assert first_approve.status_code == 200
    second_approve = trusted.post(f"/devices/requests/{ref}/approve", json={"password": PASSWORD})
    assert second_approve.status_code == 404
    assert (
        candidate.post("/auth/device/complete", json={"challenge_id": str(ref)}).status_code == 200
    )


def test_r1_and_r4_boundary_and_decision_readiness(env: Any) -> None:
    """Regressionsprüfung R1: Rotation, expliziter Widerruf, abgelaufener OTP und A/B-Isolation."""
    from psycopg.rows import dict_row

    from syllentra_backend.identity import IdentityService

    alice, bob, recovering = env["browser"](), env["browser"](), env["browser"]()
    account(env, alice, "alice@example.test")
    account(env, bob, "bob@example.test")
    aid = UUID(alice.get("/session").json()["account_id"])
    bid = UUID(bob.get("/session").json()["account_id"])
    alice_personal_1 = env["offline"].take(str(aid))
    bob_personal = env["offline"].take(str(bid))
    service = IdentityService(
        env["config"],
        lambda: env["now"][0],
    )
    # 1. Kontrollierte Regeneration/Rotation ersetzt den alten persönlichen Code sofort:
    with psycopg.connect(env["admin"], row_factory=dict_row) as db:
        acc_row = db.execute("SELECT * FROM accounts WHERE id = %s", (aid,)).fetchone()
        assert acc_row
        service.issue_offline_code(db, acc_row)
    alice_personal_2 = env["offline"].take(str(aid))
    assert alice_personal_2 != alice_personal_1
    ref1 = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    otp1 = env["mail"].take(ref1)
    # Ersetzter alter Code wird abgelehnt:
    assert (
        recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref1,
                "code": otp1,
                "recovery_code": alice_personal_1,
                "new_password": NEW_PASSWORD,
            },
        ).status_code
        == 400
    )
    # 2. Isolationsprüfung zwischen Konto A und Konto B (fremder persönlicher Code wird abgelehnt):
    assert (
        recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref1,
                "code": otp1,
                "recovery_code": bob_personal,
                "new_password": NEW_PASSWORD,
            },
        ).status_code
        == 400
    )
    # 3. Abgelaufener Recovery-OTP (>5 Minuten) wird trotz gültigem persönlichem Code abgelehnt:
    env["now"][0] += timedelta(minutes=6)
    assert (
        recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref1,
                "code": otp1,
                "recovery_code": alice_personal_2,
                "new_password": NEW_PASSWORD,
            },
        ).status_code
        == 400
    )
    # 4. Expliziter Widerruf des persönlichen Recoverycodes (revoke_offline_code) sperrt Einlösung:
    with psycopg.connect(env["admin"], row_factory=dict_row) as db:
        assert service.revoke_offline_code(db, aid) is True
        assert service.revoke_offline_code(db, aid) is False
    ref2 = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    otp2 = env["mail"].take(ref2)
    assert (
        recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref2,
                "code": otp2,
                "recovery_code": alice_personal_2,
                "new_password": NEW_PASSWORD,
            },
        ).status_code
        == 400
    )
    # Nach autorisierter Neuausgabe gelingt die Wiederherstellung und widerruft alte Sitzung/Gerät:
    with psycopg.connect(env["admin"], row_factory=dict_row) as db:
        acc_row = db.execute("SELECT * FROM accounts WHERE id = %s", (aid,)).fetchone()
        assert acc_row
        service.issue_offline_code(db, acc_row)
    alice_personal_3 = env["offline"].take(str(aid))
    ref3 = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    otp3 = env["mail"].take(ref3)
    assert (
        recovering.post(
            "/auth/recover/complete",
            json={
                "challenge_id": ref3,
                "code": otp3,
                "recovery_code": alice_personal_3,
                "new_password": NEW_PASSWORD,
            },
        ).status_code
        == 200
    )
    assert alice.get("/session").status_code == 401
    assert bob.get("/session").status_code == 200


def test_r4_unexpected_associated_data_blocks_pending_reset(env: Any) -> None:
    """Sicherheitswächter R4: Unerwartete Daten an einem pending-Konto verhindern Reset."""
    from uuid import uuid4

    first, stranger = env["browser"](), env["browser"]()
    ref = registration(env, first, "anomaly@example.test")
    _ = env["mail"].take(ref)
    with psycopg.connect(env["admin"]) as db:
        row = db.execute("SELECT id FROM accounts WHERE login = 'anomaly@example.test'").fetchone()
        assert row
        aid = row[0]
        # Künstliche Anomalie: Notiz hängt an einem noch unverifizierten pending-Konto
        db.execute(
            "INSERT INTO notes (id, account_id, title, body, deleted_at) "
            "VALUES (%s, %s, 'Anomalie', 'Darf nicht überschrieben werden', NULL)",
            (uuid4(), aid),
        )
    env["now"][0] += timedelta(hours=25)
    before = len(env["mail"].messages)
    res = stranger.post(
        "/auth/register", json={"email": "anomaly@example.test", "password": NEW_PASSWORD}
    )
    assert res.status_code == 202
    assert len(env["mail"].messages) == before
    with psycopg.connect(env["admin"]) as db:
        events = db.execute(
            "SELECT count(*) FROM security_events "
            "WHERE account_id = %s AND event = 'pending_reset_blocked'",
            (aid,),
        ).fetchone()
        assert events and events[0] == 1


def test_r4_concurrent_registrations_and_verify_vs_reset_at_24h(env: Any) -> None:
    """Parallelitätsprüfung R4: 2 gleichzeitige Resets nach 24h sowie Verify vs. Reset bei 24h."""
    # 1. Zwei gleichzeitige Registrierungen nach >24h auf dasselbe pending-Konto:
    init_client = env["browser"]()
    ref0 = registration(env, init_client, "race-reg@example.test")
    _ = env["mail"].take(ref0)
    env["now"][0] += timedelta(hours=25)
    c1, c2 = env["browser"](), env["browser"]()
    p1, p2 = NEW_PASSWORD + "-c1", NEW_PASSWORD + "-c2"
    with ThreadPoolExecutor(max_workers=2) as pool:
        f1 = pool.submit(
            lambda: c1.post(
                "/auth/register", json={"email": "race-reg@example.test", "password": p1}
            )
        )
        f2 = pool.submit(
            lambda: c2.post(
                "/auth/register", json={"email": "race-reg@example.test", "password": p2}
            )
        )
        r1, r2 = f1.result(), f2.result()
    assert r1.status_code == 202 and r2.status_code == 202
    with psycopg.connect(env["admin"]) as db:
        active_ch = db.execute(
            "SELECT id, security_epoch FROM identity_challenges "
            "WHERE account_id = (SELECT id FROM accounts WHERE login = 'race-reg@example.test') "
            "AND NOT consumed"
        ).fetchall()
        assert len(active_ch) == 1
        acc_epoch = db.execute(
            "SELECT security_epoch FROM accounts WHERE login = 'race-reg@example.test'"
        ).fetchone()
        assert acc_epoch and acc_epoch[0] == 1 and active_ch[0][1] == 1
    # 2. Gleichzeitige Verifikation (mit frischer Challenge kurz vor 24h) und Reset exakt bei 24h:
    owner, resetter = env["browser"](), env["browser"]()
    start = env["now"][0]
    ref_init = registration(env, owner, "race-verify@example.test")
    _ = env["mail"].take(ref_init)
    env["now"][0] = start + timedelta(hours=23, minutes=59)
    retry = owner.post(
        "/auth/register", json={"email": "race-verify@example.test", "password": PASSWORD}
    )
    assert retry.status_code == 202
    valid_ref = retry.json()["challenge_id"]
    valid_otp = env["mail"].take(valid_ref)
    env["now"][0] = start + timedelta(hours=24)
    with ThreadPoolExecutor(max_workers=2) as pool:
        fv = pool.submit(
            lambda: owner.post("/auth/verify", json={"challenge_id": valid_ref, "code": valid_otp})
        )
        fr = pool.submit(
            lambda: resetter.post(
                "/auth/register",
                json={"email": "race-verify@example.test", "password": NEW_PASSWORD},
            )
        )
        rv, rr = fv.result(), fr.result()
    assert rr.status_code == 202
    assert rv.status_code in {200, 400}
    if rv.status_code == 200:
        # Verifikation hat die Kontosperre zuerst gewonnen -> Konto ist verifiziert und wurde
        # durch den parallelen Reset-Aufruf NICHT überschrieben:
        assert (
            owner.post(
                "/auth/login", json={"login": "race-verify@example.test", "password": PASSWORD}
            ).status_code
            == 200
        )
        assert (
            owner.post(
                "/auth/login", json={"login": "race-verify@example.test", "password": NEW_PASSWORD}
            ).status_code
            == 401
        )
    else:
        # Reset hat die Kontosperre zuerst gewonnen -> alte Challenge wurde abgelehnt (400),
        # neue Challenge lässt sich mit NEW_PASSWORD verifizieren:
        new_ref = rr.json()["challenge_id"]
        verify(env, resetter, new_ref)
        assert (
            resetter.post(
                "/auth/login", json={"login": "race-verify@example.test", "password": NEW_PASSWORD}
            ).status_code
            == 200
        )
        assert (
            resetter.post(
                "/auth/login", json={"login": "race-verify@example.test", "password": PASSWORD}
            ).status_code
            == 401
        )


def test_r1_migration_004_revokes_expired_legacy_codes_and_preserves_active_codes(
    env: Any,
) -> None:
    """Migrationsprüfung 004: Bereits abgelaufene Altcodes werden widerrufen, nicht reaktiviert."""
    from pathlib import Path
    from uuid import uuid4

    migration_004 = (
        Path(__file__).resolve().parents[1] / "migrations/004_r1_r4_lifetimes.sql"
    ).read_text(encoding="utf-8")
    # Nur die beiden UPDATE-Anweisungen der Vorwärtsmigration 004 gegen einen Altzustand prüfen:
    update_lines = [line for line in migration_004.splitlines() if line.startswith("UPDATE ")]
    assert len(update_lines) == 2
    expired_aid, active_aid = uuid4(), uuid4()
    with psycopg.connect(env["admin"]) as db:
        for aid, email in [(expired_aid, "exp@example.test"), (active_aid, "act@example.test")]:
            db.execute(
                "INSERT INTO accounts (id,login,password_hash,kind,verification,status) "
                "VALUES (%s,%s,'x','user','verified','active')",
                (aid, email),
            )
        db.execute(
            "INSERT INTO recovery_codes (account_id, verifier, used, revoked, expires_at) "
            "VALUES (%s, 'v1', false, false, CURRENT_TIMESTAMP - interval '1 second'), "
            "(%s, 'v2', false, false, CURRENT_TIMESTAMP + interval '1 day')",
            (expired_aid, active_aid),
        )
        for stmt in update_lines:
            db.execute(stmt)
        exp_row = db.execute(
            "SELECT revoked, expires_at IS NOT NULL FROM recovery_codes WHERE account_id = %s",
            (expired_aid,),
        ).fetchone()
        act_row = db.execute(
            "SELECT revoked, expires_at FROM recovery_codes WHERE account_id = %s",
            (active_aid,),
        ).fetchone()
        assert exp_row == (True, True)
        assert act_row == (False, None)


def test_migration_003_to_004_full_schema_and_legacy_data() -> None:
    """Baut ein echtes Schema 003 mit Altdaten auf und wendet 004_r1_r4_lifetimes.sql an."""
    import hashlib
    from uuid import uuid4

    from scripts.migrate import ROOT, migrate
    from scripts.test_db import create_run_database, drop_run_database

    legacy_run = create_run_database()
    try:
        with psycopg.connect(legacy_run.admin_url) as db:
            db.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
            db.execute(
                "CREATE TABLE schema_migrations (version text PRIMARY KEY, sha256 text NOT NULL)"
            )
            migrations_dir = ROOT / "migrations"
            for version in [
                "001_foundation.sql",
                "002_local_identity.sql",
                "003_proof_lifetimes.sql",
            ]:
                sql_content = (migrations_dir / version).read_text(encoding="utf-8")
                digest = hashlib.sha256(sql_content.encode()).hexdigest()
                db.execute(sql_content)
                db.execute("INSERT INTO schema_migrations VALUES (%s, %s)", (version, digest))

            # 1. Altzustand 003 vor der Migration prüfen: pending_since existiert noch nicht
            col_check = db.execute(
                "SELECT count(*) FROM information_schema.columns "
                "WHERE table_name = 'accounts' AND column_name = 'pending_since'"
            ).fetchone()
            assert col_check == (0,)

            # 2. Synthetische Altdaten im Schema 003 anlegen:
            # 2a. pending-Konto frisch mit aktiver E-Mail-Challenge
            pending_recent_id = uuid4()
            db.execute(
                "INSERT INTO accounts (id, login, password_hash, kind, verification, status) "
                "VALUES (%s, 'pending_fresh@example.test', 'hash_fresh', 'user', 'pending', "
                "'active')",
                (pending_recent_id,),
            )
            challenge_id = uuid4()
            db.execute(
                "INSERT INTO identity_challenges (id, account_id, purpose, verifier, "
                "binding_hash, expires_at, created_at, last_sent_at, attempts, sends, "
                "consumed, approved, security_epoch, prior_verifiers) "
                "VALUES (%s, %s, 'email', 'synth_verifier_1', %s, "
                "CURRENT_TIMESTAMP + interval '10 minutes', CURRENT_TIMESTAMP, "
                "CURRENT_TIMESTAMP, 0, 1, false, false, 0, '{}')",
                (challenge_id, pending_recent_id, "0" * 64),
            )

            # 2b. verified-Konten mit aktiven, abgelaufenen und benutzten Recoverycodes
            act_user_id = uuid4()
            exp_user_id = uuid4()
            used_user_id = uuid4()
            for uid, email in [
                (act_user_id, "active@example.test"),
                (exp_user_id, "expired@example.test"),
                (used_user_id, "used@example.test"),
            ]:
                db.execute(
                    "INSERT INTO accounts (id, login, password_hash, kind, verification, status) "
                    "VALUES (%s, %s, 'hash_verified', 'user', 'verified', 'active')",
                    (uid, email),
                )
            # Aktiver 003-Code (expires_at in der Zukunft, used=false)
            db.execute(
                "INSERT INTO recovery_codes (account_id, verifier, used, expires_at) "
                "VALUES (%s, 'verifier_act', false, CURRENT_TIMESTAMP + interval '5 days')",
                (act_user_id,),
            )
            # Abgelaufener 003-Code (expires_at in der Vergangenheit, used=false)
            db.execute(
                "INSERT INTO recovery_codes (account_id, verifier, used, expires_at) "
                "VALUES (%s, 'verifier_exp', false, CURRENT_TIMESTAMP - interval '1 hour')",
                (exp_user_id,),
            )
            # Bereits benutzter 003-Code (used=true)
            db.execute(
                "INSERT INTO recovery_codes (account_id, verifier, used, expires_at) "
                "VALUES (%s, 'verifier_used', true, CURRENT_TIMESTAMP + interval '1 day')",
                (used_user_id,),
            )

            # 2c. Altsitzungen und Altgeräte
            dev_id = uuid4()
            db.execute(
                "INSERT INTO devices (id, account_id, proof_hash, authorized, expires_at, "
                "security_epoch) VALUES (%s, %s, %s, false, "
                "CURRENT_TIMESTAMP - interval '1 hour', 0)",
                (dev_id, act_user_id, "1" * 64),
            )
            db.execute(
                "INSERT INTO sessions (token_hash, account_id, device_id, expires_at, revoked, "
                "security_epoch) VALUES (%s, %s, %s, CURRENT_TIMESTAMP - interval '1 hour', "
                "true, 0)",
                ("2" * 64, act_user_id, dev_id),
            )

        # 3. Vorwärtsmigration 004 anwenden (via migrate())
        migrate(legacy_run.admin_url)

        # 4. Invarianten nach Migration 003 -> 004 prüfen:
        with psycopg.connect(legacy_run.admin_url) as db:
            # 4a. Schema-Prüfung: pending_since und R1-Spalten existieren nun
            col_after = db.execute(
                "SELECT count(*) FROM information_schema.columns "
                "WHERE table_name = 'accounts' AND column_name = 'pending_since'"
            ).fetchone()
            assert col_after == (1,)

            # 4b. pending-Konto hat pending_since erhalten
            row_pending = db.execute(
                "SELECT verification, pending_since IS NOT NULL, security_epoch "
                "FROM accounts WHERE id = %s",
                (pending_recent_id,),
            ).fetchone()
            assert row_pending == ("pending", True, 0)

            # 4c. E-Mail-Challenge bleibt unverändert aktiv erhalten (keine 24h-Wartepflicht)
            row_chal = db.execute(
                "SELECT consumed, verifier, security_epoch FROM identity_challenges WHERE id = %s",
                (challenge_id,),
            ).fetchone()
            assert row_chal == (False, "synth_verifier_1", 0)

            # 4d. R4-Schwellenwertprüfung: Nach 24h ist Reset möglich
            db.execute(
                "UPDATE accounts SET pending_since = CURRENT_TIMESTAMP - interval '25 hours' "
                "WHERE id = %s",
                (pending_recent_id,),
            )
            row_aged = db.execute(
                "SELECT pending_since <= CURRENT_TIMESTAMP - interval '24 hours' "
                "FROM accounts WHERE id = %s",
                (pending_recent_id,),
            ).fetchone()
            assert row_aged == (True,)

            # 4e. R1: Aktiver Recoverycode hat nun expires_at = NULL, revoked = false, issued_at
            row_act = db.execute(
                "SELECT used, revoked, expires_at, issued_at IS NOT NULL "
                "FROM recovery_codes WHERE account_id = %s",
                (act_user_id,),
            ).fetchone()
            assert row_act == (False, False, None, True)

            # 4f. R1: Abgelaufener Altcode wurde widerrufen (revoked = true) und nicht reaktiviert
            row_exp = db.execute(
                "SELECT used, revoked, expires_at IS NOT NULL "
                "FROM recovery_codes WHERE account_id = %s",
                (exp_user_id,),
            ).fetchone()
            assert row_exp == (False, True, True)

            # 4g. R1: Bereits benutzter Code bleibt used = true
            row_used = db.execute(
                "SELECT used, revoked FROM recovery_codes WHERE account_id = %s",
                (used_user_id,),
            ).fetchone()
            assert row_used == (True, False)

            # 4h. Keine Wiederbelebung alter Nachweise (Sessions / Devices)
            row_dev = db.execute(
                "SELECT authorized FROM devices WHERE id = %s", (dev_id,)
            ).fetchone()
            assert row_dev == (False,)
            row_sess = db.execute(
                "SELECT revoked FROM sessions WHERE token_hash = %s", ("2" * 64,)
            ).fetchone()
            assert row_sess == (True,)
    finally:
        drop_run_database(legacy_run)
