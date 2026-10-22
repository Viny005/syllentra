"""Lokale Identitätsübergänge; Fristen sind ausschließlich Experimentparameter."""

import hashlib
import hmac
import re
import secrets
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Any
from urllib.parse import urlsplit
from uuid import UUID, uuid4

import psycopg
from fastapi.responses import JSONResponse

from .delivery import PrivateChannel
from .security import DUMMY_HASH, PASSWORDS, digest, verify_password

Db = psycopg.Connection[dict[str, Any]]
SESSION = "__Host-syllentra-session"
DEVICE = "__Host-syllentra-device"
PREAUTH = "__Host-syllentra-preauth"
CSRF = "__Host-syllentra-csrf"


def normalize_email(value: str) -> str:
    email = value.strip().lower()
    if not re.fullmatch(r"[a-z0-9][a-z0-9._+-]{0,63}@example\.test", email):
        raise ValueError("Nur synthetische ASCII-Adressen unter example.test zulässig.")
    return email


def cookie(response: JSONResponse, name: str, value: str, age: int = 900) -> None:
    response.set_cookie(
        name, value, max_age=age, secure=True, httponly=True, samesite="strict", path="/"
    )


def result(status: int, detail: str, **data: Any) -> JSONResponse:
    return JSONResponse({"status": detail, **data}, status_code=status)


@dataclass(frozen=True)
class LocalIdentity:
    pepper: bytes = field(repr=False)
    mail: PrivateChannel
    offline: PrivateChannel
    origin: str = "https://127.0.0.1:5174"

    def validate(self, database_url: str) -> None:
        url = urlsplit(database_url)
        if (
            url.scheme not in {"postgresql", "postgres"}
            or bool(url.query or url.fragment)
            or url.port != 55439
            or url.hostname not in {"127.0.0.1", "localhost"}
            or url.path not in {"/syllentra_test", "/syllentra_prototype"}
            or len(self.pepper) < 32
            or self.mail is self.offline
            or self.origin != "https://127.0.0.1:5174"
        ):
            raise ValueError("Lokale Identitätsprobe erfordert isolierte DB und getrennte Kanäle.")


class IdentityService:
    def __init__(self, config: LocalIdentity, clock: Callable[[], datetime]) -> None:
        self.config, self.clock = config, clock

    def verifier(self, purpose: str, reference: str, secret: str) -> str:
        return hmac.new(
            self.config.pepper, f"{purpose}:{reference}:{secret}".encode(), hashlib.sha256
        ).hexdigest()

    def audit(self, db: Db, event: str, account: UUID | None = None) -> None:
        # Nur endliche Metadaten, keine Mailadresse, Eingabewerte oder Geheimnisse.
        db.execute(
            "DELETE FROM security_events WHERE occurred_at < %s",
            (self.clock() - timedelta(days=7),),
        )
        db.execute(
            "INSERT INTO security_events VALUES (%s, %s, %s, %s)",
            (uuid4(), account, event, self.clock()),
        )

    def budget(self, db: Db, operation: str, key: str, maximum: int = 10) -> bool:
        now = self.clock()
        db.execute("DELETE FROM identity_budgets WHERE expires_at <= %s", (now,))
        row = db.execute(
            "INSERT INTO identity_budgets VALUES (%s, %s, 1) ON CONFLICT (scope_hash) "
            "DO UPDATE SET attempts = identity_budgets.attempts + 1 RETURNING attempts",
            (self.verifier("budget", operation, key), now + timedelta(minutes=1)),
        ).fetchone()
        return bool(row and row["attempts"] <= maximum)

    def clean(self, db: Db) -> None:
        db.execute(
            "DELETE FROM identity_challenges WHERE expires_at < %s",
            (self.clock() - timedelta(hours=1),),
        )

    def challenge(self, db: Db, account: dict[str, Any], purpose: str) -> JSONResponse:
        self.clean(db)
        now, reference, binding = self.clock(), uuid4(), secrets.token_urlsafe(32)
        code = f"{secrets.randbelow(100000000):08d}" if purpose != "device" else ""
        db.execute(
            "UPDATE identity_challenges SET consumed = true WHERE account_id = %s "
            "AND purpose = %s AND NOT consumed",
            (account["id"], purpose),
        )
        db.execute(
            "INSERT INTO identity_challenges "
            "(id, account_id, purpose, verifier, binding_hash, expires_at, created_at, "
            "last_sent_at, security_epoch) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                reference,
                account["id"],
                purpose,
                self.verifier(purpose, str(reference), code) if code else None,
                digest(binding),
                now + timedelta(minutes=5),
                now,
                now,
                account["security_epoch"],
            ),
        )
        if code:
            self.config.mail.deliver(account["login"], purpose, str(reference), code)
        response = result(
            202,
            "device_verification_required" if purpose == "device" else "accepted",
            challenge_id=str(reference),
        )
        cookie(response, PREAUTH, binding, 300)
        return response

    def fake_challenge(self) -> JSONResponse:
        response = result(202, "accepted", challenge_id=str(uuid4()))
        cookie(response, PREAUTH, secrets.token_urlsafe(32), 300)
        return response

    def register(self, db: Db, email: str, password: str) -> JSONResponse:
        if not self.budget(db, "register", email):
            return result(429, "try_later")
        encoded = PASSWORDS.hash(password)  # Auch im Duplikatpfad keine billige Existenzantwort.
        row = db.execute(
            "INSERT INTO accounts (id,login,password_hash,verification,status) "
            "VALUES (%s,%s,%s,'pending','active') ON CONFLICT (login) DO NOTHING "
            "RETURNING *",
            (uuid4(), email, encoded),
        ).fetchone()
        if not row:
            pending = db.execute(
                "SELECT * FROM accounts WHERE login = %s FOR UPDATE", (email,)
            ).fetchone()
            if (
                pending
                and pending["verification"] == "pending"
                and pending["status"] == "active"
                and pending["kind"] == "user"
                and not pending["mfa_required"]
                and verify_password(pending["password_hash"], password)
            ):
                return self.challenge(db, pending, "email")
            return self.fake_challenge()
        self.audit(db, "register", row["id"])
        return self.challenge(db, row, "email")

    def locked_challenge(
        self, db: Db, reference: UUID, binding: str | None, purpose: str
    ) -> tuple[dict[str, Any], dict[str, Any]] | None:
        # Einheitliche Sperrreihenfolge Konto -> Challenge verhindert doppelte Einlösung.
        hint = db.execute(
            "SELECT account_id FROM identity_challenges WHERE id = %s", (reference,)
        ).fetchone()
        if not hint:
            return None
        account = db.execute(
            "SELECT * FROM accounts WHERE id = %s FOR UPDATE", (hint["account_id"],)
        ).fetchone()
        row = db.execute(
            "SELECT * FROM identity_challenges WHERE id = %s FOR UPDATE", (reference,)
        ).fetchone()
        if (
            not row
            or not account
            or not binding
            or row["purpose"] != purpose
            or row["consumed"]
            or row["expires_at"] <= self.clock()
            or row["attempts"] >= 5
            or account["status"] != "active"
            or account["kind"] != "user"
            or account["mfa_required"]
            or row["security_epoch"] != account["security_epoch"]
            or not hmac.compare_digest(row["binding_hash"], digest(binding))
        ):
            return None
        return row, account

    def check_code(self, db: Db, row: dict[str, Any], account: dict[str, Any], code: str) -> bool:
        # Fehlerantworten dürfen diese Zählung nicht per Exception zurückrollen.
        db.execute(
            "UPDATE identity_challenges SET attempts = attempts + 1 WHERE id = %s", (row["id"],)
        )
        ok = hmac.compare_digest(
            row["verifier"] or "", self.verifier(row["purpose"], str(row["id"]), code)
        )
        if not ok:
            self.audit(db, "otp_denied", account["id"])
        return ok

    def issue_offline_code(self, db: Db, account: dict[str, Any]) -> None:
        code = secrets.token_urlsafe(32)
        db.execute(
            "INSERT INTO recovery_codes (account_id,verifier,used,expires_at) "
            "VALUES (%s, %s, false, %s) ON CONFLICT (account_id) "
            "DO UPDATE SET verifier = EXCLUDED.verifier, used = false, "
            "expires_at = EXCLUDED.expires_at",
            (
                account["id"],
                self.verifier("offline", str(account["id"]), code),
                self.clock() + timedelta(days=7),
            ),
        )
        self.config.offline.deliver(account["login"], "offline-recovery", str(account["id"]), code)

    def authorize_device(self, db: Db, account: dict[str, Any], response: JSONResponse) -> None:
        proof = secrets.token_urlsafe(32)
        db.execute(
            "INSERT INTO devices (id, account_id, proof_hash, authorized, expires_at, "
            "security_epoch) VALUES (%s,%s,%s,true,%s,%s)",
            (
                uuid4(),
                account["id"],
                digest(proof),
                self.clock() + timedelta(days=7),
                account["security_epoch"],
            ),
        )
        cookie(response, DEVICE, proof, 604800)
        response.delete_cookie(PREAUTH, secure=True, httponly=True, samesite="strict")

    def verify_email(self, db: Db, reference: UUID, binding: str | None, code: str) -> JSONResponse:
        pair = self.locked_challenge(db, reference, binding, "email")
        if not pair or pair[1]["verification"] != "pending":
            return result(400, "verification_failed")
        row, account = pair
        if not self.check_code(db, row, account, code):
            return result(400, "verification_failed")
        db.execute("UPDATE identity_challenges SET consumed = true WHERE id = %s", (reference,))
        db.execute("UPDATE accounts SET verification = 'verified' WHERE id = %s", (account["id"],))
        self.issue_offline_code(db, account)
        response = result(200, "verified")
        self.authorize_device(db, account, response)
        self.audit(db, "email_verified", account["id"])
        return response

    def resend(self, db: Db, reference: UUID, binding: str | None) -> JSONResponse:
        hint = db.execute("SELECT purpose FROM identity_challenges WHERE id = %s", (reference,))
        kind = hint.fetchone()
        pair = self.locked_challenge(db, reference, binding, kind["purpose"] if kind else "email")
        if not pair or pair[0]["purpose"] == "device":
            return result(202, "accepted")
        row, account = pair
        if (
            row["sends"] >= 3
            or row["attempts"] >= 5
            or self.clock() < row["last_sent_at"] + timedelta(seconds=60)
        ):
            return result(202, "accepted")
        code = f"{secrets.randbelow(100000000):08d}"
        previous = [row["verifier"], *row["prior_verifiers"]]
        while self.verifier(row["purpose"], str(reference), code) in previous:
            code = f"{secrets.randbelow(100000000):08d}"
        # Versuchszähler und ursprüngliche Ablaufzeit bleiben erhalten.
        db.execute(
            "UPDATE identity_challenges SET verifier = %s, sends = sends + 1, "
            "last_sent_at = %s, prior_verifiers = array_append(prior_verifiers, verifier) "
            "WHERE id = %s",
            (self.verifier(row["purpose"], str(reference), code), self.clock(), reference),
        )
        self.config.mail.deliver(account["login"], row["purpose"], str(reference), code)
        self.audit(db, "otp_resent", account["id"])
        return result(202, "accepted")

    def login(self, db: Db, email: str, password: str, proof: str | None) -> JSONResponse:
        if not self.budget(db, "login", email):
            return result(429, "try_later")
        account = db.execute(
            "SELECT * FROM accounts WHERE login = %s FOR UPDATE", (email,)
        ).fetchone()
        valid = verify_password(account["password_hash"] if account else DUMMY_HASH, password)
        if (
            not valid
            or not account
            or account["verification"] != "verified"
            or account["status"] != "active"
            or account["kind"] != "user"
            or account["mfa_required"]
        ):
            self.audit(db, "login_denied", account["id"] if account else None)
            return JSONResponse({"detail": "unauthorized"}, status_code=401)
        device = db.execute(
            "SELECT id FROM devices WHERE account_id = %s AND proof_hash = %s "
            "AND authorized AND expires_at > %s AND security_epoch = %s",
            (account["id"], digest(proof or ""), self.clock(), account["security_epoch"]),
        ).fetchone()
        if not device:
            self.audit(db, "device_requested", account["id"])
            return self.challenge(db, account, "device")
        # Hashparameter nach erfolgreicher Prüfung sicher aktualisieren.
        if PASSWORDS.check_needs_rehash(account["password_hash"]):
            db.execute(
                "UPDATE accounts SET password_hash = %s WHERE id = %s",
                (PASSWORDS.hash(password), account["id"]),
            )
        response = result(200, "authenticated")
        self.session(db, account, device["id"], response)
        self.audit(db, "login_ok", account["id"])
        return response

    def session(
        self, db: Db, account: dict[str, Any], device: UUID, response: JSONResponse
    ) -> None:
        token = secrets.token_urlsafe(
            32
        )  # Nie eine vom Client vorgegebene Sitzungskennung übernehmen.
        db.execute(
            "INSERT INTO sessions (token_hash, account_id, device_id, expires_at, "
            "security_epoch) VALUES (%s,%s,%s,%s,%s)",
            (
                digest(token),
                account["id"],
                device,
                self.clock() + timedelta(minutes=15),
                account["security_epoch"],
            ),
        )
        cookie(response, SESSION, token)

    def request_recovery(self, db: Db, email: str) -> JSONResponse:
        if not self.budget(db, "recovery", email, 3):
            return result(429, "try_later")
        account = db.execute(
            "SELECT * FROM accounts WHERE login = %s FOR UPDATE", (email,)
        ).fetchone()
        if (
            not account
            or account["verification"] != "verified"
            or account["kind"] != "user"
            or account["status"] != "active"
            or account["mfa_required"]
        ):
            return self.fake_challenge()
        self.audit(db, "recovery_requested", account["id"])
        return self.challenge(db, account, "recovery")

    def recover(
        self,
        db: Db,
        reference: UUID,
        binding: str | None,
        code: str,
        offline_code: str,
        password: str,
    ) -> JSONResponse:
        pair = self.locked_challenge(db, reference, binding, "recovery")
        if not pair or pair[1]["verification"] != "verified":
            return result(400, "recovery_failed")
        row, account = pair
        otp_ok = self.check_code(db, row, account, code)
        personal = db.execute(
            "SELECT * FROM recovery_codes WHERE account_id = %s FOR UPDATE", (account["id"],)
        ).fetchone()
        personal_ok = bool(
            personal
            and personal["expires_at"] > self.clock()
            and not personal["used"]
            and hmac.compare_digest(
                personal["verifier"], self.verifier("offline", str(account["id"]), offline_code)
            )
        )
        if not otp_ok or not personal_ok:
            self.audit(db, "recovery_denied", account["id"])
            return result(400, "recovery_failed")
        db.execute("UPDATE recovery_codes SET used = true WHERE account_id = %s", (account["id"],))
        db.execute(
            "UPDATE accounts SET password_hash = %s, security_epoch = security_epoch + 1 "
            "WHERE id = %s",
            (PASSWORDS.hash(password), account["id"]),
        )
        db.execute("UPDATE sessions SET revoked = true WHERE account_id = %s", (account["id"],))
        db.execute("UPDATE devices SET authorized = false WHERE account_id = %s", (account["id"],))
        db.execute(
            "UPDATE identity_challenges SET consumed = true WHERE account_id = %s", (account["id"],)
        )
        account["security_epoch"] += 1
        response = result(200, "recovered")
        response.delete_cookie(SESSION, secure=True, httponly=True, samesite="strict")
        self.authorize_device(db, account, response)
        self.issue_offline_code(db, account)
        self.config.mail.deliver(account["login"], "security-notification", str(uuid4()), "")
        self.audit(db, "recovered", account["id"])
        return response

    def approve_device(
        self, db: Db, account_id: UUID, session_hash: str, reference: UUID, password: str
    ) -> JSONResponse:
        if not self.budget(db, "approve", str(account_id)):
            return result(429, "try_later")
        account = db.execute(
            "SELECT * FROM accounts WHERE id = %s FOR UPDATE", (account_id,)
        ).fetchone()
        if not account or not verify_password(account["password_hash"], password):
            return result(400, "verification_failed")
        session = db.execute(
            "SELECT device_id FROM sessions WHERE token_hash = %s", (session_hash,)
        ).fetchone()
        row = db.execute(
            "UPDATE identity_challenges SET approved = true, approved_by_device = %s "
            "WHERE id = %s AND account_id = %s AND purpose = 'device' "
            "AND NOT consumed AND expires_at > %s AND security_epoch = %s RETURNING id",
            (
                session["device_id"] if session else None,
                reference,
                account_id,
                self.clock(),
                account["security_epoch"],
            ),
        ).fetchone()
        if not row or not session:
            return result(404, "not_found")
        self.audit(db, "device_approved", account_id)
        return result(200, "approved")

    def finish_device(self, db: Db, reference: UUID, binding: str | None) -> JSONResponse:
        pair = self.locked_challenge(db, reference, binding, "device")
        if not pair or not pair[0]["approved"] or pair[1]["verification"] != "verified":
            return result(400, "verification_failed")
        row, account = pair
        authority = db.execute(
            "SELECT id FROM devices WHERE id = %s AND account_id = %s "
            "AND authorized AND expires_at > %s AND security_epoch = %s",
            (row["approved_by_device"], account["id"], self.clock(), account["security_epoch"]),
        ).fetchone()
        if not authority:
            return result(400, "verification_failed")
        db.execute("UPDATE identity_challenges SET consumed = true WHERE id = %s", (reference,))
        response = result(200, "device_verified")
        self.authorize_device(db, account, response)
        return response

    def revoke_device(
        self, db: Db, account_id: UUID, device_id: UUID, password: str
    ) -> JSONResponse:
        if not self.budget(db, "revoke", str(account_id)):
            return result(429, "try_later")
        account = db.execute(
            "SELECT * FROM accounts WHERE id = %s FOR UPDATE", (account_id,)
        ).fetchone()
        if not account or not verify_password(account["password_hash"], password):
            return result(400, "verification_failed")
        row = db.execute(
            "UPDATE devices SET authorized = false WHERE id = %s AND account_id = %s RETURNING id",
            (device_id, account_id),
        ).fetchone()
        if not row:
            return result(404, "not_found")
        db.execute(
            "UPDATE sessions SET revoked = true WHERE account_id = %s AND device_id = %s",
            (account_id, device_id),
        )
        self.audit(db, "device_revoked", account_id)
        return result(200, "revoked")
