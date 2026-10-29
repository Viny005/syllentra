"""Zwei kontrollierte lokale Testkanäle, niemals HTTP-/E-Mail-Zustellung."""

import json
import os
import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any, Protocol


class PrivateChannel(Protocol):
    def deliver(self, recipient: str, purpose: str, reference: str, secret: str) -> None: ...


class MemoryChannel:
    def __init__(self) -> None:
        self.messages: list[dict[str, str]] = []
        self._lock = threading.Lock()

    def deliver(self, recipient: str, purpose: str, reference: str, secret: str) -> None:
        with self._lock:
            self.messages.append(
                dict(recipient=recipient, purpose=purpose, reference=reference, secret=secret)
            )

    def take(self, reference: str) -> str:
        with self._lock:
            return next(m["secret"] for m in reversed(self.messages) if m["reference"] == reference)


class LocalFileChannel:
    """0600-Datei außerhalb des Webroots; nur synthetischer interner Testempfänger."""

    def __init__(self, path: Path, clock: Callable[[], float] = time.time) -> None:
        if ".local" not in path.parts:
            raise ValueError("Privater lokaler Kanal muss außerhalb des Webroots liegen.")
        self.path, self.clock = path, clock
        self.path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        if self.path.parent.stat().st_mode & 0o077:
            raise ValueError("Privates Zustellverzeichnis benötigt Modus 0700.")
        self._lock = threading.Lock()

    def update(self, item: dict[str, Any] | None = None) -> None:
        with self._lock:
            fd = os.open(self.path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
            with os.fdopen(fd, "r+") as f:
                stat = os.fstat(f.fileno())
                if stat.st_mode & 0o077 or stat.st_uid != os.getuid():
                    raise ValueError("Privater Zustellkanal benötigt eigenen Modus 0600.")
                retained = [r for line in f if (r := json.loads(line))["expires_at"] > self.clock()]
                if item:
                    retained.append(item)
                f.seek(0)
                f.truncate()
                for row in retained:
                    f.write(json.dumps(row) + "\n")

    def prune(self) -> None:
        self.update()

    def deliver(self, recipient: str, purpose: str, reference: str, secret: str) -> None:
        lifetime = 604800 if purpose == "offline-recovery" else 600
        self.update(
            dict(
                recipient=recipient,
                purpose=purpose,
                reference=reference,
                secret=secret,
                expires_at=self.clock() + lifetime,
            )
        )
