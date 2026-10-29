"""Passwortprüfung und opake Sitzungsnachweise ohne eingebettete Rollen."""

import hashlib
import secrets
import threading
import time

from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

PASSWORDS = PasswordHasher()
DUMMY_HASH = PASSWORDS.hash(secrets.token_urlsafe(32))


def digest(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()


def verify_password(encoded: str, supplied: str) -> bool:
    try:
        return PASSWORDS.verify(encoded, supplied)
    except (VerificationError, InvalidHashError):
        return False


class LoginBudget:
    """Endliches lokales Fehlversuchsbudget; kein verteilter Produktionsschutz."""

    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._window = time.monotonic()
        self._attempts = 0

    def allow(self) -> bool:
        with self._lock:
            now = time.monotonic()
            if now - self._window >= 60:
                self._window, self._attempts = now, 0
            self._attempts += 1
            return self._attempts <= 10
