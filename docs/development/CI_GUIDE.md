# Syllentra CI Guide

Dieses Dokument beschreibt die kontinuierliche Integration (CI) über GitHub Actions für Syllentra AI.

## 1. Zweck und Grenzen der CI

Die automatisierte CI-Pipeline stellt sicher, dass jede Änderung an Spezifikationen, Prototypen und Quellcode bei Pull Requests gegen `main` automatisch auf statische Korrektheit, Typensicherheit, Frontend-Integrität und Backend-Isolationsregeln geprüft wird.

> **Wichtiger Grundsatz:**
> **CI erfolgreich ≠ Produkt produktionsreif.**
> Ein erfolgreicher CI-Lauf belegt die Einhaltung statischer Regeln und das fehlerfreie Verhalten der experimentellen Prototypen unter synthetischen Testdaten. Er ersetzt weder die fachliche Abnahme der Siedersleben-Bausteine durch den Projektinhaber noch formale Sicherheitsaudits, Penetrationstests oder produktive V1-Freigaben.

---

## 2. Struktur der CI-Pipeline (`.github/workflows/ci.yml`)

Die Pipeline besteht aus drei parallelen Jobs auf Standard-Runnern (`ubuntu-24.04`):

### Job A: `static-checks` (Statische Codeanalyse & Typisierung)
* **Frontend:**
  * `npm run typecheck` (`tsc --noEmit`)
  * `npm run lint` (`eslint .`)
  * `npm run format:check` (`prettier --check .`)
* **Backend:**
  * `uv run ruff check src scripts tests`
  * `uv run mypy --config-file pyproject.toml src scripts`

### Job B: `frontend-tests` (Unit-Tests & Build)
* `npm test` (`vitest run` — 13 Unit-Tests, i18n, Kalender, Präferenzen, CSRF-Retry)
* `npm run build` (`tsc --noEmit && vite build` — PWA-Artefaktkompilierung)

### Job C: `backend-postgres-tests` (Isolierte PostgreSQL-Tests)
* Startet einen ephemeren Docker-Container mit fixiertem PostgreSQL-17.11-Image (`scripts/ci_test_db.py start`)
* Konfiguriert flüchtiges `tmpfs`, interne Loopback-Bindung (`127.0.0.1:55439`) und zufällige Passwörter
* Schützt `.local/database.json` mit Dateirechten `0600`
* Führt alle 116 Backend-Pytest-Tests aus (`pytest -q -x -p no:cacheprovider`), einschließlich 24 Datenbank-Isolations- und Concurrency-Tests
* Stoppt und entfernt den CI-Container zuverlässig im Teardown (`if: always()`)

---

## 3. Lokale Ausführung der Prüfungen

Alle in der CI ausgeführten Prüfungen können lokal reproduziert werden:

### Frontend (`prototypes/frontend`)
```bash
npm ci
npm run typecheck
npm run lint
npm run format:check
npm test
npm run build
```

### Backend (`prototypes/backend`)
```bash
uv sync --locked
uv run ruff check src scripts tests
uv run mypy --config-file pyproject.toml src scripts

# Für Pytest-Ausführung gegen lokalen oder CI-Container:
python scripts/ci_test_db.py start
uv run pytest -q -x -p no:cacheprovider
python scripts/ci_test_db.py stop
```

---

## 4. Sicherheitsregeln der CI

* **Minimale Berechtigungen:** `permissions: contents: read`. Keine Schreibberechtigungen für Tokens.
* **Keine produktiven Secrets:** Sämtliche Testpasswörter werden zur Laufzeit flüchtig generiert.
* **Keine automatischen Merges:** Pull Requests erfordern weiterhin menschliche Prüfung und Autorisierung.
* **Isolierte Container:** Der CI-Container trägt spezifische Labels (`syllentra.ci=true`) und bindet ausschließlich an `127.0.0.1:55439`. Vorhandene lokale Container werden weder berührt noch gelöscht.
