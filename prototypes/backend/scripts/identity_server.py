"""Eigener ausdrücklich lokaler Einstieg; kein produktiver Servermodus."""

import json
import os
import sys
from pathlib import Path

import uvicorn

from scripts.migrate import urls
from syllentra_backend.api import create_app
from syllentra_backend.delivery import LocalFileChannel
from syllentra_backend.identity import LocalIdentity

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    if sys.argv[1:] not in [[], ["--test"]]:
        raise SystemExit("Nur lokaler Modus, optional --test für isolierte Browserprüfungen.")
    local = ROOT / ".local"
    state = local / "identity.json"
    if state.stat().st_mode & 0o077 or state.stat().st_uid != os.getuid():
        raise SystemExit(
            "Identitätsdatei muss ausschließlich dem aktuellen lokalen Benutzer gehören."
        )
    data = json.loads(state.read_text())
    if data.get("mode") != "synthetic-local-only":
        raise SystemExit("Kein zulässiger lokaler Identitätsmodus.")
    config = LocalIdentity(
        bytes.fromhex(data["pepper"]),
        LocalFileChannel(local / "mail/otp.jsonl"),
        LocalFileChannel(local / "offline/recovery.jsonl"),
    )
    app = create_app(urls(test=sys.argv[1:] == ["--test"])[1], identity=config)
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8443,
        ssl_keyfile=str(local / "identity.key"),
        ssl_certfile=str(local / "identity.pem"),
        access_log=False,
        log_level="warning",
    )


if __name__ == "__main__":
    main()
