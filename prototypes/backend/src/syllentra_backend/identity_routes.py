"""Identitätsrouten: keine Rohgeheimnisse in HTTP-Antworten oder Logs."""

import re
from typing import Annotated, Any
from uuid import UUID

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field, SecretStr, field_validator

from .identity import DEVICE, PREAUTH, SESSION, Db, IdentityService, normalize_email, result


class Input(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Email(Input):
    email: str = Field(min_length=3, max_length=100)

    @field_validator("email")
    @classmethod
    def normalize(cls, value: str) -> str:
        return normalize_email(value)


class Registration(Email):
    password: SecretStr = Field(min_length=12, max_length=256)


class LoginInput(Input):
    login: str = Field(min_length=1, max_length=100)
    password: SecretStr = Field(min_length=12, max_length=256)
    device_proof: SecretStr | None = Field(default=None, min_length=32, max_length=128)


class Challenge(Input):
    challenge_id: UUID


class Otp(Challenge):
    code: SecretStr = Field(min_length=8, max_length=8)

    @field_validator("code")
    @classmethod
    def digits(cls, value: SecretStr) -> SecretStr:
        if not re.fullmatch(r"[0-9]{8}", value.get_secret_value()):
            raise ValueError("Ungültiger Code")
        return value


class Recover(Otp):
    recovery_code: SecretStr = Field(min_length=32, max_length=128)
    new_password: SecretStr = Field(min_length=12, max_length=256)


class Password(Input):
    password: SecretStr = Field(min_length=12, max_length=256)


def install(app: FastAPI, service: IdentityService | None, connection: Any, principal: Any) -> None:
    Database = Annotated[Db, Depends(connection, scope="function")]
    Actor = Annotated[Any, Depends(principal)]

    def unavailable() -> JSONResponse:
        return JSONResponse({"detail": "identity_flow_unavailable"}, status_code=503)

    @app.post("/auth/register")
    def register(body: Registration, db: Database) -> JSONResponse:
        return (
            service.register(db, body.email, body.password.get_secret_value())
            if service
            else unavailable()
        )

    @app.post("/auth/verify")
    def verify(body: Otp, request: Request, db: Database) -> JSONResponse:
        return (
            service.verify_email(
                db, body.challenge_id, request.cookies.get(PREAUTH), body.code.get_secret_value()
            )
            if service
            else unavailable()
        )

    @app.post("/auth/resend")
    def resend(body: Challenge, request: Request, db: Database) -> JSONResponse:
        return (
            service.resend(db, body.challenge_id, request.cookies.get(PREAUTH))
            if service
            else unavailable()
        )

    @app.post("/auth/login")
    def login(body: LoginInput, request: Request, db: Database) -> JSONResponse:
        if not service:
            return unavailable()
        try:
            email = normalize_email(body.login)
        except ValueError:
            return JSONResponse({"detail": "unauthorized"}, status_code=401)
        return service.login(
            db,
            email,
            body.password.get_secret_value(),
            body.device_proof.get_secret_value()
            if body.device_proof
            else request.cookies.get(DEVICE),
        )

    @app.post("/auth/recover")
    def recover_request(body: Email, db: Database) -> JSONResponse:
        return service.request_recovery(db, body.email) if service else unavailable()

    @app.post("/auth/recover/complete")
    def recover(body: Recover, request: Request, db: Database) -> JSONResponse:
        return (
            service.recover(
                db,
                body.challenge_id,
                request.cookies.get(PREAUTH),
                body.code.get_secret_value(),
                body.recovery_code.get_secret_value(),
                body.new_password.get_secret_value(),
            )
            if service
            else unavailable()
        )

    @app.post("/auth/device/complete")
    def complete(body: Challenge, request: Request, db: Database) -> JSONResponse:
        return (
            service.finish_device(db, body.challenge_id, request.cookies.get(PREAUTH))
            if service
            else unavailable()
        )

    @app.get("/devices/requests")
    def requests(db: Database, actor: Actor) -> list[dict[str, Any]]:
        return db.execute(
            "SELECT id, created_at, expires_at, approved FROM identity_challenges "
            "WHERE account_id = %s AND purpose = 'device' AND NOT consumed "
            "AND expires_at > %s ORDER BY created_at DESC LIMIT 20",
            (actor.account_id, service.clock() if service else None),
        ).fetchall()

    @app.post("/devices/requests/{reference}/approve")
    def approve(reference: UUID, body: Password, db: Database, actor: Actor) -> JSONResponse:
        return (
            service.approve_device(
                db, actor.account_id, actor.token_hash, reference, body.password.get_secret_value()
            )
            if service
            else unavailable()
        )

    @app.get("/devices")
    def devices(db: Database, actor: Actor) -> list[dict[str, Any]]:
        return db.execute(
            "SELECT id, authorized, expires_at FROM devices WHERE account_id = %s "
            "ORDER BY id LIMIT 50",
            (actor.account_id,),
        ).fetchall()

    @app.post("/devices/{device_id}/revoke")
    def revoke(device_id: UUID, body: Password, db: Database, actor: Actor) -> JSONResponse:
        return (
            service.revoke_device(db, actor.account_id, device_id, body.password.get_secret_value())
            if service
            else unavailable()
        )

    @app.get("/sessions")
    def sessions(db: Database, actor: Actor) -> list[dict[str, Any]]:
        return db.execute(
            "SELECT id, expires_at, revoked FROM sessions WHERE account_id = %s "
            "ORDER BY id LIMIT 50",
            (actor.account_id,),
        ).fetchall()

    @app.post("/sessions/{session_id}/revoke")
    def revoke_session(session_id: UUID, db: Database, actor: Actor) -> JSONResponse:
        row = db.execute(
            "UPDATE sessions SET revoked = true WHERE id = %s AND account_id = %s "
            "RETURNING token_hash",
            (session_id, actor.account_id),
        ).fetchone()
        if not row:
            return result(404, "not_found")
        if service:
            service.audit(db, "session_revoked", actor.account_id)
        response = result(200, "revoked")
        if row["token_hash"] == actor.token_hash:
            response.delete_cookie(SESSION, secure=True, httponly=True, samesite="strict")
        return response
