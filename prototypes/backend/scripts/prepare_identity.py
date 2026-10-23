"""Explizite lokale TLS-/Testkanalvorbereitung; keine Accounts oder Zustellungen."""

import json
import os
import secrets
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    local = ROOT / ".local"
    local.mkdir(mode=0o700, exist_ok=True)
    targets = [local / name for name in ["identity.json", "identity.key", "identity.pem"]]
    if any(p.exists() for p in targets):
        raise SystemExit("Identitätszustand vorhanden; nichts überschrieben.")
    subprocess.run(
        [
            "openssl",
            "req",
            "-x509",
            "-newkey",
            "rsa:3072",
            "-sha256",
            "-days",
            "2",
            "-nodes",
            "-keyout",
            str(targets[1]),
            "-out",
            str(targets[2]),
            "-subj",
            "/CN=Syllentra synthetic local test",
            "-addext",
            "subjectAltName=IP:127.0.0.1,DNS:localhost",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    os.chmod(targets[1], 0o600)
    os.chmod(targets[2], 0o600)
    fd = os.open(targets[0], os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(fd, "w") as f:
        json.dump({"mode": "synthetic-local-only", "pepper": secrets.token_hex(32)}, f)
    print("Lokales kurzlebiges TLS und private Testkanäle vorbereitet; keine Identität angelegt.")


if __name__ == "__main__":
    main()
