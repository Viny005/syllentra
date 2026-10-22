"""Strikt lokale API-Probe; Anmeldung ausschließlich im synthetischen Testharness."""

import secrets
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Annotated, Any
from uuid import UUID

import psycopg
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from psycopg.rows import dict_row
from pydantic import BaseModel, ConfigDict, Field, SecretStr
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .limits import BodyLimit
from .security import DUMMY_HASH, PASSWORDS, LoginBudget, digest, verify_password


@dataclass(frozen=True)
class Principal:
    account_id: UUID
    kind: str
    token_hash: str


class Login(BaseModel):
    model_config = ConfigDict(extra="forbid")
    login: str = Field(min_length=1, max_length=80)
    password: SecretStr = Field(min_length=12, max_length=256)
    device_proof: SecretStr = Field(min_length=32, max_length=128)


class NoteChange(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(max_length=4000)


def create_app(
    database_url: str,
    *,
    synthetic_test_harness: bool = False,
    clock: Callable[[], datetime] = lambda: datetime.now(UTC),
) -> FastAPI:
    # Selbst versehentliche Aktivierung ist auf eine explizite Testdatenbank beschränkt.
    if synthetic_test_harness and not database_url.endswith("/syllentra_test"):
        raise ValueError("Testharness nur mit isolierter synthetischer Testdatenbank erlaubt.")
    app = FastAPI(
        title="Syllentra lokale Backendprobe", docs_url=None, redoc_url=None, openapi_url=None
    )
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost", "testserver"]
    )
    app.add_middleware(BodyLimit)
    budget = LoginBudget()

    @app.middleware("http")
    async def boundaries(request: Request, call_next: Any) -> Any:
        # Keine Cookieauth und kein CORS; Browser-Ursprünge werden vor jedem APIzugriff gesperrt.
        if request.headers.get("origin"):
            response = JSONResponse({"detail": "browser_integration_unavailable"}, status_code=403)
        else:
            try:
                response = await call_next(request)
            except Exception:
                response = JSONResponse({"detail": "service_unavailable"}, status_code=503)
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
        return response

    @app.exception_handler(RequestValidationError)
    async def invalid_input(_request: Request, _exc: RequestValidationError) -> JSONResponse:
        # Pydanticfehler enthalten sonst Eingabewerte; niemals Passwort/Token/Privattext spiegeln.
        return JSONResponse({"detail": "invalid_input"}, status_code=422)

    def connection() -> Iterator[psycopg.Connection[dict[str, Any]]]:
        with psycopg.connect(database_url, row_factory=dict_row, connect_timeout=3) as db:
            yield db

    Db = Annotated[psycopg.Connection[dict[str, Any]], Depends(connection, scope="function")]

    bearer = HTTPBearer(auto_error=False)

    def principal(
        db: Db, credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)]
    ) -> Principal:
        if credentials is None:
            raise HTTPException(401, "unauthorized", headers={"WWW-Authenticate": "Bearer"})
        token = credentials.credentials
        if len(token) != 43:
            raise HTTPException(401, "unauthorized")
        row = db.execute(
            "SELECT a.id, a.kind FROM sessions s JOIN accounts a ON a.id = s.account_id "
            "JOIN devices d ON d.id = s.device_id AND d.account_id = a.id "
            "WHERE s.token_hash = %s AND s.expires_at > %s AND NOT s.revoked "
            "AND a.status = 'active' AND a.verification = 'verified' AND d.authorized",
            (digest(token), clock()),
        ).fetchone()
        if not row:
            raise HTTPException(401, "unauthorized")
        return Principal(row["id"], row["kind"], digest(token))

    Actor = Annotated[Principal, Depends(principal)]

    def notes_rights(db: Db, actor: Actor) -> Principal:
        capability = db.execute("SELECT mode, allowed_kind FROM capabilities WHERE name = 'notes'")
        row = capability.fetchone()
        if (
            actor.kind != "user"
            or not row
            or row["mode"] != "available"
            or row["allowed_kind"] != actor.kind
        ):
            raise HTTPException(403, "capability_unavailable")
        return actor

    NotesActor = Annotated[Principal, Depends(notes_rights)]

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "local-experimental", "authentication": "unavailable"}

    @app.post("/auth/login")
    def login(body: Login, db: Db) -> dict[str, str | int]:
        if not synthetic_test_harness:
            raise HTTPException(503, "identity_flow_unavailable")
        if not budget.allow():
            raise HTTPException(429, "try_later")
        row = db.execute("SELECT * FROM accounts WHERE login = %s", (body.login,)).fetchone()
        ok = verify_password(
            row["password_hash"] if row else DUMMY_HASH, body.password.get_secret_value()
        )
        if not ok or not row or row["verification"] != "verified" or row["status"] != "active":
            raise HTTPException(401, "unauthorized")
        # Admin-MFA ist nicht implementiert; daher keine privilegierte Anmeldung.
        if row["kind"] != "user":
            raise HTTPException(401, "unauthorized")
        device = db.execute(
            "SELECT id FROM devices WHERE account_id = %s AND proof_hash = %s AND authorized",
            (row["id"], digest(body.device_proof.get_secret_value())),
        ).fetchone()
        if not device:
            raise HTTPException(401, "unauthorized")
        if PASSWORDS.check_needs_rehash(row["password_hash"]):
            # Runtime darf Accounts absichtlich nicht ändern; Migration/Identitätsweg bleibt offen.
            raise HTTPException(503, "identity_upgrade_required")
        token = secrets.token_urlsafe(32)
        db.execute(
            "INSERT INTO sessions (token_hash, account_id, device_id, expires_at) "
            "VALUES (%s, %s, %s, %s)",
            (digest(token), row["id"], device["id"], clock() + timedelta(minutes=15)),
        )
        return {"access_token": token, "token_type": "bearer", "expires_in": 900}

    @app.get("/session")
    def session(actor: Actor) -> dict[str, str]:
        return {
            "account_id": str(actor.account_id),
            "kind": actor.kind,
            "assurance": "synthetic-test-only",
        }

    @app.post("/auth/logout", status_code=204)
    def logout(db: Db, actor: Actor) -> None:
        db.execute(
            "UPDATE sessions SET revoked = true WHERE token_hash = %s AND account_id = %s",
            (actor.token_hash, actor.account_id),
        )

    @app.get("/capabilities")
    def capabilities(db: Db, actor: Actor) -> dict[str, str]:
        return {
            row["name"]: row["mode"]
            if row["name"] == "notes" and actor.kind == "user" and row["allowed_kind"] == actor.kind
            else "unavailable"
            for row in db.execute(
                "SELECT name, mode, allowed_kind FROM capabilities WHERE mode != 'hidden'"
            ).fetchall()
        }

    @app.get("/notes")
    def notes(db: Db, actor: NotesActor) -> list[dict[str, Any]]:
        return db.execute(
            "SELECT id, title, body FROM notes WHERE account_id = %s "
            "AND deleted_at IS NULL ORDER BY id LIMIT 50",
            (actor.account_id,),
        ).fetchall()

    @app.get("/notes/{note_id}")
    def note(note_id: UUID, db: Db, actor: NotesActor) -> dict[str, Any]:
        row = db.execute(
            "SELECT id, title, body FROM notes WHERE id = %s AND account_id = %s "
            "AND deleted_at IS NULL",
            (note_id, actor.account_id),
        ).fetchone()
        if not row:
            raise HTTPException(404, "not_found")
        return row

    @app.patch("/notes/{note_id}")
    def change_note(note_id: UUID, body: NoteChange, db: Db, actor: NotesActor) -> dict[str, Any]:
        row = db.execute(
            "UPDATE notes SET title = %s, body = %s WHERE id = %s AND account_id = %s "
            "AND deleted_at IS NULL RETURNING id, title, body",
            (body.title, body.body, note_id, actor.account_id),
        ).fetchone()
        if not row:
            raise HTTPException(404, "not_found")
        return row

    @app.delete("/notes/{note_id}", status_code=204)
    def delete_note(
        note_id: UUID,
        db: Db,
        actor: NotesActor,
        confirm: Annotated[str | None, Header(alias="X-Confirm-Delete")] = None,
    ) -> None:
        if confirm != str(note_id):
            raise HTTPException(409, "confirmation_required")
        row = db.execute(
            "UPDATE notes SET deleted_at = %s WHERE id = %s AND account_id = %s "
            "AND deleted_at IS NULL RETURNING id",
            (clock(), note_id, actor.account_id),
        )
        if not row.fetchone():
            raise HTTPException(404, "not_found")

    @app.get("/administration")
    def administration(_actor: Actor) -> None:
        # Kein Adminhandler, bevor MFA, Erstbesetzung, Audit und Recovery validiert sind.
        raise HTTPException(403, "administration_unavailable")

    return app
