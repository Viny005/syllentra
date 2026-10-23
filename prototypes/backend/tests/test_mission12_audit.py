"""Prioritäre Sicherheits-, Grenz-, Parallelitäts- und Regressionsprüfungen (Mission 12 & 13).

R2, R3, R5 und R12 sind ab Mission 13 als Regressionsprüfungen abgesichert; R1 (>7 Tage
Inaktivität) und R4 (nicht ablaufende pending-Konten) bleiben bis zur Freigabe der offenen
Entscheidungen ausdrücklich als Charakterisierung („en attente de décision“) dokumentiert.
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
    """Charakterisierung R1 (en attente de correctif): >7 Tage Inaktivität sperrt Zugang."""
    c, recovering = env["browser"](), env["browser"]()
    account(env, c)
    aid = c.get("/session").json()["account_id"]
    personal = env["offline"].take(aid)
    # Nach 7 Tagen + 1s sind sowohl Gerätebindung (7d) als auch Offline-Code (7d) abgelaufen:
    env["now"][0] += timedelta(days=7, seconds=1)
    assert c.get("/session").status_code == 401
    login_res = c.post("/auth/login", json={"login": "alice@example.test", "password": PASSWORD})
    assert login_res.status_code == 202
    assert login_res.json()["status"] == "device_verification_required"
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
            "new_password": NEW_PASSWORD,
        },
    )
    # Charakterisierung R1: Selbst mit korrektem E-Mail-OTP und korrektem persönlichem Code
    # schlägt die Wiederherstellung nach >7 Tagen fehl, weil recovery_codes.expires_at <= clock().
    assert rec_res.status_code == 400
    assert rec_res.json()["status"] == "recovery_failed"


def test_old_pending_account_blocks_different_password_and_allows_same_password_restart(
    env: Any,
) -> None:
    """Charakterisierung R4 (en attente de correctif): alte pending-Konten laufen nicht ab."""
    first, stranger, owner_retry = env["browser"](), env["browser"](), env["browser"]()
    old_ref = registration(env, first, "pending@example.test")
    _ = env["mail"].take(old_ref)
    # Nach 30 Tagen ist die ursprüngliche Challenge längst abgelaufen, das pending-Konto bleibt:
    env["now"][0] += timedelta(days=30)
    before_messages = len(env["mail"].messages)
    r_diff = stranger.post(
        "/auth/register", json={"email": "pending@example.test", "password": NEW_PASSWORD}
    )
    assert r_diff.status_code == 202
    # Charakterisierung R4: Mit anderem Passwort wird nur eine Fake-Challenge geliefert (kein OTP):
    assert len(env["mail"].messages) == before_messages
    # Nur mit dem ursprünglichen Passwort lässt sich die Verifikation neu starten:
    r_same = owner_retry.post(
        "/auth/register", json={"email": "pending@example.test", "password": PASSWORD}
    )
    assert r_same.status_code == 202
    assert len(env["mail"].messages) == before_messages + 1
    verify(env, owner_retry, r_same.json()["challenge_id"])


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
    assert approve_status in {200, 401}
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
    """Grenz- und Entscheidungsbereitschaftstest für R1 (knapp vor 7d) und R4 (Challenges)."""
    c, recovering, pending_client = env["browser"](), env["browser"](), env["browser"]()
    account(env, c)
    aid = c.get("/session").json()["account_id"]
    personal = env["offline"].take(aid)
    p_ref = registration(env, pending_client, "stale-pending@example.test")
    _ = env["mail"].take(p_ref)
    # 1 Sekunde vor Ablauf der 7-Tage-Frist ist die Kontowiederherstellung noch möglich und rotiert
    # sowohl Gerätebindung als auch Offline-Wiederherstellungscode um weitere 7 Tage:
    env["now"][0] += timedelta(days=7) - timedelta(seconds=1)
    ref = recovering.post("/auth/recover", json={"email": "alice@example.test"}).json()[
        "challenge_id"
    ]
    otp = env["mail"].take(ref)
    rec = recovering.post(
        "/auth/recover/complete",
        json={
            "challenge_id": ref,
            "code": otp,
            "recovery_code": personal,
            "new_password": NEW_PASSWORD,
        },
    )
    assert rec.status_code == 200
    new_personal = env["offline"].take(aid)
    assert new_personal and new_personal != personal
    # Abgelaufene Challenge von stale-pending (>1h überfällig) wurde durch clean() entfernt,
    # während das pending-Konto bis zur Entscheidung über R4 in accounts erhalten bleibt:
    with psycopg.connect(env["admin"]) as db:
        ch_row = db.execute("SELECT id FROM identity_challenges WHERE id = %s", (p_ref,)).fetchone()
        assert ch_row is None
        acc_row = db.execute(
            "SELECT verification, status FROM accounts WHERE login = 'stale-pending@example.test'"
        ).fetchone()
        assert acc_row == ("pending", "active")
