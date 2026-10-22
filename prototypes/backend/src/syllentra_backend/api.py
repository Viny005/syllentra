"""Lokale API-Probe mit explizitem synthetischem Identitätsmodus; keine Produktfreigabe."""

import hmac
import logging
import secrets
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Annotated, Any
from uuid import UUID

import psycopg
from fastapi import Depends, FastAPI, Header, HTTPException, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyCookie, HTTPAuthorizationCredentials, HTTPBearer
from psycopg.rows import dict_row
from pydantic import BaseModel, ConfigDict, Field
from starlette.concurrency import run_in_threadpool
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .identity import CSRF, SESSION, IdentityService, LocalIdentity, cookie
from .identity_routes import install as install_identity
from .limits import BodyLimit
from .security import digest


@dataclass(frozen=True)
class Principal:
    account_id: UUID
    kind: str
    token_hash: str


class NoteChange(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(max_length=4000)


def create_app(
    database_url: str,
    *,
    identity: LocalIdentity | None = None,
    clock: Callable[[], datetime] = lambda: datetime.now(UTC),
) -> FastAPI:
    if identity:
        identity.validate(database_url)
    service = IdentityService(identity, clock) if identity else None
    app = FastAPI(
        title="Syllentra lokale Backendprobe", docs_url=None, redoc_url=None, openapi_url=None
    )
    app.add_middleware(
        TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost", "testserver"]
    )
    app.add_middleware(BodyLimit)

    @app.middleware("http")
    async def boundaries(request: Request, call_next: Any) -> Any:
        origin = request.headers.get("origin")
        denied = None
        if identity:
            if request.url.scheme != "https" or (
                request.client and request.client.host not in {"127.0.0.1", "::1", "testclient"}
            ):
                denied = "local_https_required"
            elif request.headers.get("sec-fetch-site") == "cross-site":
                denied = "origin_denied"
            elif origin and origin != identity.origin:
                denied = "origin_denied"
            elif request.method not in {"GET", "HEAD", "OPTIONS"}:
                proof = request.headers.get("x-csrf-token", "")
                stored = request.cookies.get(CSRF, "")
                if (
                    origin != identity.origin
                    or len(stored) != 43
                    or not hmac.compare_digest(proof, stored)
                    or request.headers.get("sec-fetch-site") not in {None, "same-origin"}
                ):
                    denied = "csrf_denied"
        elif origin:
            denied = "browser_integration_unavailable"
        if denied:
            response = JSONResponse({"detail": denied}, status_code=403)
        else:
            try:
                if service and request.method == "POST" and request.url.path.startswith("/auth/"):

                    def network_budget() -> bool:
                        with psycopg.connect(
                            database_url, row_factory=dict_row, connect_timeout=3
                        ) as db:
                            return service.budget(
                                db,
                                "network",
                                request.client.host if request.client else "local",
                                100,
                            )

                    if not await run_in_threadpool(network_budget):
                        return JSONResponse(
                            {"detail": "try_later"},
                            status_code=429,
                            headers={"Cache-Control": "no-store"},
                        )
                response = await call_next(request)
            except Exception as error:
                logging.getLogger("syllentra.local").warning(
                    "backend_failure:%s", type(error).__name__
                )
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
    session_cookie = APIKeyCookie(name=SESSION, scheme_name="LocalSessionCookie", auto_error=False)

    def principal(
        request: Request,
        db: Db,
        credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)],
        session_value: Annotated[str | None, Depends(session_cookie)],
    ) -> Principal:
        token = credentials.credentials if credentials else session_value
        if (
            not token
            or (request.headers.get("authorization") and not credentials)
            or (
                credentials
                and request.cookies.get(SESSION)
                and not hmac.compare_digest(token, request.cookies[SESSION])
            )
        ):
            raise HTTPException(401, "unauthorized", headers={"WWW-Authenticate": "Bearer"})
        if len(token) != 43:
            raise HTTPException(401, "unauthorized")
        row = db.execute(
            "SELECT a.id, a.kind FROM sessions s JOIN accounts a ON a.id = s.account_id "
            "JOIN devices d ON d.id = s.device_id AND d.account_id = a.id "
            "WHERE s.token_hash = %s AND s.expires_at > %s AND NOT s.revoked "
            "AND a.status = 'active' AND a.verification = 'verified' AND d.authorized "
            "AND d.expires_at > %s AND NOT a.mfa_required "
            "AND s.security_epoch = a.security_epoch AND d.security_epoch = a.security_epoch "
            "FOR UPDATE OF a",
            (digest(token), clock(), clock()),
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
        return {
            "status": "local-experimental",
            "authentication": "local-synthetic" if identity else "unavailable",
        }

    @app.get("/auth/csrf")
    def csrf() -> JSONResponse:
        if not identity:
            raise HTTPException(503, "identity_flow_unavailable")
        value = secrets.token_urlsafe(32)
        response = JSONResponse({"csrf_token": value})
        cookie(response, CSRF, value, 3600)
        return response

    def identity_actor(actor: Actor) -> Principal:
        if actor.kind != "user":
            raise HTTPException(403, "administration_unavailable")
        return actor

    install_identity(app, service, connection, identity_actor)

    @app.get("/session")
    def session(actor: Actor) -> dict[str, str]:
        return {
            "account_id": str(actor.account_id),
            "kind": actor.kind,
            "assurance": "local-synthetic-otp",
        }

    @app.post("/auth/logout", status_code=204)
    def logout(db: Db, actor: Actor, response: Response) -> None:
        db.execute(
            "UPDATE sessions SET revoked = true WHERE token_hash = %s AND account_id = %s",
            (actor.token_hash, actor.account_id),
        )
        if service:
            service.audit(db, "session_revoked", actor.account_id)
        response.delete_cookie(SESSION, secure=True, httponly=True, samesite="strict")

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
