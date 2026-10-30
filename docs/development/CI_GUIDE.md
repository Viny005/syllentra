# Syllentra CI Guide

Dieses Dokument beschreibt die kontinuierliche Integration (CI) über GitHub Actions für Syllentra AI.

## 1. Zweck und Grenzen der CI

Die automatisierte CI-Pipeline stellt sicher, dass jede Änderung an Spezifikationen, Prototypen und Quellcode bei Pull Requests gegen `main` automatisch auf statische Korrektheit, Typensicherheit, Frontend-Integrität und Backend-Isolationsregeln geprüft wird.

> **Wichtiger Grundsatz:**
> **CI erfolgreich ≠ Produkt produktionsreif.**
> Ein erfolgreicher CI-Lauf belegt die Einhaltung statischer Regeln und das fehlerfreie Verhalten der experimentellen Prototypen unter synthetischen Testdaten. Er ersetzt weder die fachliche Abnahme der Siedersleben-Bausteine durch den Projektinhaber noch formale Sicherheitsaudits, Penetrationstests oder produktive V1-Freigaben.
>
> Die CI prüft insbesondere **keine vollständige Siedersleben-Markdown-Konformität** und der Frontend-Build beweist **weder eine vollständige native PWA-Installation noch Browser-E2E-Funktionalität**.

---

## 2. Struktur der CI-Pipeline (`.github/workflows/ci.yml`)

Die Pipeline besteht aus drei parallelen Jobs auf Standard-Runnern (`ubuntu-24.04`):

### Job A: `static-checks` (Statische Codeanalyse & Typisierung)
* **Frontend:**
  * `npm run typecheck` (`tsc --noEmit`)
  * `npm run lint` (`eslint .`)
  * `npm run format:check` (`prettier --check .`)
* **Backend:**
  * `uv run --locked ruff check src scripts tests`
  * `uv run --locked mypy --config-file pyproject.toml src scripts`

### Job B: `frontend-tests` (Unit-Tests & Build)
* `npm test` (`vitest run` — 13 Unit-Tests, i18n, Kalender, Präferenzen, CSRF-Retry)
* `npm run build` (`tsc --noEmit && vite build` — PWA-Artefaktkompilierung)

### Job C: `backend-postgres-tests` (Isolierte PostgreSQL-Tests)
* Generiert vorab ein flüchtiges Invocation-Token (`SYLLENTRA_CI_INVOCATION_TOKEN`) für den aktuellen Workflow-Lauf.
* Startet einen ephemeren Docker-Container mit fixiertem PostgreSQL-17.11-Image (`python3 scripts/ci_test_db.py start`).
* Unabhängig vom Paketmanager: Start und Teardown nutzen direkt die Standard-Python-Laufzeit (`python3`), um auch bei Fehlschlägen von Paketinstallationen handlungsfähig zu bleiben.
* Erzwingt strikte Lockfile-Bindung über `uv sync --locked` und `uv run --locked pytest -q -x -p no:cacheprovider`.
* Führt alle Backend-Pytest-Tests aus (einschließlich der 24 Datenbank-Isolations- und Concurrency-Tests sowie der 22 Regressionstests für Fehlerpfade in `test_ci_test_db.py`).
* Führt kontrollierten Teardown im Teardown-Schritt aus (`if: always()`), wobei der Schutz fremder Ressourcen kryptografisch durch das Invocation-Token und die Metadatenprüfung sichergestellt wird.

---

## 3. PostgreSQL-Lifecycle & Fail-Closed-Härtung (`ci_test_db.py`)

Die Verwaltung des CI-PostgreSQL-Containers folgt strengen Sicherheits- und Isolationsprinzipien:

### Eigentumsbindung und Invocation-Autorisierung pro CI-Run
* Jede Programminvokation benötigt ein unabhängig bereitgestelltes Invocation-Token (`SYLLENTRA_CI_INVOCATION_TOKEN`, mindestens 16 Zeichen). Eine gespeicherte Containeridentität allein berechtigt niemals eine neue Invokation zur Löschung.
* Jeder Start erzeugt einen eindeutigen Containernamen (`syllentra-ci-pg-<uuid>`).
* Der Container wird beim Start mit eindeutigen Docker-Labels versehen:
  * `syllentra.ci=true`
  * `syllentra.synthetic=true`
  * `syllentra.owner_token=<token>`
* Vor dem Containerstart wird eine atomare Metadaten-Datei `.local/.ci_pg_meta.json` mit Dateirechten `0600` im geschützten Ordner `.local` (`0700`) via `.tmp` und Dateisystem-Rename abgelegt. Nach erfolgreichem `docker run` wird zusätzlich die konkrete Container-ID atomar hinterlegt.

### Fail-Closed-Teardown & Strikte Autorisierung
* **Strikte Invocation-Autorisierung:** Teardown prüft vor jeder Aktion, ob das aktuelle Invocation-Token (`SYLLENTRA_CI_INVOCATION_TOKEN`) exakt mit dem in `.ci_pg_meta.json` hinterlegten `owner_token` übereinstimmt. Bei jeder Abweichung verweigert das Skript sofort jede destruktive Aktion mit einem Fehler (`CIPostgresError`), ohne Docker anzusprechen.
* **Schutz fremder Instanzen:** Existieren Zustandsdateien ohne zugehörige CI-Metadaten oder ist die Metadatendatei beschädigt, leer oder unvollständig, verweigert das Skript den Teardown mit `CIPostgresError`. Fremde Ressourcen bleiben geschützt.
* **Verweigerter Start:** War der Start verweigert (z. B. weil eine fremde `.local/database.json` vorlag), verhindert die Invocation-Token-Prüfung im nachfolgenden Teardown-Schritt (`if: always()`) zuverlässig das Berühren oder Löschen fremder Ressourcen.
* **Eindeutiger Abwesenheitsnachweis:** Ein Container gilt erst dann als abwesend, wenn `docker inspect` explizit `No such container: <name>` meldet oder `docker ps -a --filter name=^/{name}$` nachweislich leer ist. Dämon-Ausfälle ("cannot connect to docker daemon", "permission denied") oder unspezifische Fehler führen zum sofortigen Fail-Closed.
* **Erhalt von Recovery-Informationen:** Kann der Container nicht gestoppt oder entfernt werden (z. B. Docker-Fehler, Daemon blockiert), werden die Metadaten- und Konfigurationsdateien **nicht gelöscht**, und es wird ein Fehlercode zurückgegeben. Dies ermöglicht eine gezielte manuelle Fehleranalyse ohne verwaiste unidentifizierbare Ressourcen.
* **Fail-Closed Dateibereinigung:** Erst nach nachgewiesener Abwesenheit des Containers werden `database.json` und `.ci_pg_meta.json` gelöscht. Scheitert das Löschen einer Datei, wird ein `CIPostgresError` ausgelöst.
* **Keine Geheimnisse in Fehlerausgaben:** Passwörter und Invocation-Tokens werden vor jeder Konsolenausgabe oder Fehlermeldung automatisch durch `[REDACTED]` maskiert.
* **Keine destruktiven globalen Sweeps:** Weder `docker system prune` noch pauschale Datenbanklöschungen werden ausgeführt.

### Timeouts
* Alle Docker-Befehle werden mit Timeouts abgesichert (`_run_docker` mit max. 15s bzw. 20s).
* Der Healthcheck (`pg_isready`) verwendet eine monotone Frist (`time.monotonic()`) von maximal 30 Sekunden.

---

## 4. Lokale Ausführung der Prüfungen

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
uv run --locked ruff check src scripts tests
uv run --locked mypy --config-file pyproject.toml src scripts

# Invocation-Token für Testlauf bereitstellen:
export SYLLENTRA_CI_INVOCATION_TOKEN=$(python3 -c "import secrets; print(secrets.token_hex(16))")

# Unit- & Regressionstests ohne Docker ausführen:
uv run --locked pytest -q -x -p no:cacheprovider tests/test_ci_test_db.py

# Vollständige Suite gegen CI-Container ausführen:
python3 scripts/ci_test_db.py start
uv run --locked pytest -q -x -p no:cacheprovider
python3 scripts/ci_test_db.py stop
```

---

## 5. Sicherheitsregeln der CI

* **Minimale Berechtigungen:** `permissions: contents: read`. Keine Schreibberechtigungen für Tokens.
* **Keine produktiven Secrets:** Sämtliche Testpasswörter werden zur Laufzeit flüchtig generiert.
* **Keine automatischen Merges:** Pull Requests erfordern weiterhin menschliche Prüfung und Autorisierung.
* **Isolierte Container:** Der CI-Container trägt spezifische Labels (`syllentra.ci=true`, `syllentra.owner_token=...`) und bindet ausschließlich an `127.0.0.1:55439`. Vorhandene lokale Container werden weder berührt noch gelöscht.
