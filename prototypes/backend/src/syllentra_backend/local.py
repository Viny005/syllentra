"""Lokaler Einstieg ohne Anmeldung, Kontoseed oder Adminbootstrap."""

from scripts.migrate import urls

from .api import create_app

app = create_app(urls()[1])
