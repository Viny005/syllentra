# Paket- und Lizenznachweise Backendprobe

**Stand:** 22.10.2026 · **Status:** Lokale Inventur / Zur Prüfung

Installiert aus PyPI über `uv.lock` mit exakten Fassungen und Artefakthashes. Python 3.12.14, uv aus vorhandener Umgebung; keine Systeminstallation. Vier direkte Laufzeitabhängigkeiten: FastAPI (MIT), psycopg[binary] (LGPL-3.0-only), argon2-cffi (MIT), uvicorn (BSD-3-Clause). Fünf direkte Entwicklungsabhängigkeiten: pytest, httpx, Ruff, mypy und pip-audit sowie deren transitive Abhängigkeiten. Keine bezahlten Dienste. Herkunft: offizielle Paketmetadaten `https://pypi.org/pypi/<Name>/<Version>/json`, lokale Wheel-METADATA und mitgelieferte Lizenztexte.

Die folgende Inventur erfasst alle 58 tatsächlich installierten Distributionen. Lizenzspalte aus METADATA, nach Möglichkeit SPDX-Ausdruck; lokale Beilagen gelesen und im [Hashinventar](license-inventory.json) mit Dateihashes festgehalten. Metadaten ersetzen keine vollständige juristische Freigabe. packageurl-python enthält im installierten Wheel keine gesonderte Lizenzbeilage; MIT-Metadatum belegt, zusätzliche Quellen-/Distributionsprüfung offen. Keine Lizenzkompatibilität des gesamten Betriebssystemimages behauptet.

| Distribution | Version | Lizenz laut Paket | Lizenz-/Notice-Dateien |
|---|---|---|---|
| annotated-doc | 0.0.5 | MIT | 1 |
| annotated-types | 0.8.0 | MIT | 1 |
| anyio | 4.15.1 | MIT | 1 |
| argon2-cffi | 25.1.0 | MIT | 1 |
| argon2-cffi-bindings | 26.1.0 | MIT | 1 |
| ast_serialize | 0.13.1 | MIT | 2 |
| boolean.py | 5.0 | BSD-2-Clause | 3 |
| CacheControl | 0.14.4 | Apache-2.0 | 1 |
| certifi | 2026.10.19 | MPL-2.0 | 1 |
| cffi | 2.1.1 | MIT-0 | 1 |
| charset-normalizer | 3.5.2 | MIT | 1 |
| click | 8.5.0 | BSD-3-Clause | 1 |
| cyclonedx-python-lib | 11.12.0 | Apache-2.0 | 2 |
| defusedxml | 0.7.1 | PSFL | 1 |
| fastapi | 0.161.0 | MIT | 1 |
| filelock | 4.2.4 | MIT | 1 |
| h11 | 0.16.0 | MIT | 1 |
| httpcore | 1.0.9 | BSD-3-Clause | 1 |
| httpx | 0.28.1 | BSD-3-Clause | 1 |
| idna | 3.20 | BSD-3-Clause | 1 |
| iniconfig | 2.3.1 | MIT | 1 |
| librt | 0.16.0 | MIT | 1 |
| license-expression | 30.4.4 | Apache-2.0 | 12 |
| markdown-it-py | 4.2.0 | MIT License | 2 |
| mdurl | 0.1.2 | MIT License | 1 |
| msgpack | 1.2.3 | Apache-2.0 | 1 |
| mypy | 2.4.0 | MIT | 2 |
| mypy_extensions | 1.1.0 | MIT | 1 |
| opentelemetry-api | 1.45.1 | Apache-2.0 | 1 |
| packageurl-python | 0.17.6 | MIT | 0 |
| packaging | 26.3 | Apache-2.0 OR BSD-2-Clause | 3 |
| pathspec | 1.1.1 | Mozilla Public License 2.0 (MPL 2.0) | 1 |
| pip | 26.2.2 | MIT | 22 |
| pip-requirements-parser | 32.0.1 | MIT | 1 |
| pip_api | 0.0.35 | Apache-2.0 (vollständiger Text in METADATA) | 1 |
| pip_audit | 2.10.1 | Apache Software License | 1 |
| platformdirs | 4.13.5 | MIT | 1 |
| pluggy | 1.7.0 | MIT | 1 |
| psycopg | 3.3.6 | LGPL-3.0-only | 1 |
| psycopg-binary | 3.3.6 | LGPL-3.0-only | 1 |
| py-serializable | 2.1.0 | Apache-2.0 | 1 |
| pycparser | 3.12 | BSD-3-Clause | 1 |
| pydantic | 2.14.1 | MIT | 1 |
| pydantic_core | 2.50.1 | MIT | 1 |
| Pygments | 2.21.0 | BSD-2-Clause | 2 |
| pyparsing | 3.3.3 | MIT | 1 |
| pytest | 9.1.1 | MIT | 1 |
| requests | 2.34.2 | Apache-2.0 | 2 |
| rich | 15.0.0 | MIT | 1 |
| ruff | 0.17.2 | MIT | 1 |
| sortedcontainers | 2.4.0 | Apache 2.0 | 1 |
| starlette | 1.9.0 | BSD-3-Clause | 1 |
| tomli | 2.5.0 | MIT | 1 |
| tomli_w | 1.2.0 | MIT License | 1 |
| typing-inspection | 0.4.4 | MIT | 1 |
| typing_extensions | 4.16.0 | PSF-2.0 | 1 |
| urllib3 | 2.8.0 | MIT | 1 |
| uvicorn | 0.54.0 | BSD-3-Clause | 1 |

psycopg und das getrennte binäre Wheel sind LGPL-3.0-only, keine pauschale MIT-Lizenz. Bei späterer Binärweitergabe Austausch-/Relinking-, Quell-/Lizenz- und Beilagepflichten einschließlich eingebundener nativer Bibliotheken gesondert erfüllen; hier werden keine Wheels, virtuellen Umgebungen oder Containerimages im Repository weitergegeben. Argon2-Bindings enthalten zusätzliche native Bestandteile; deren vollständige Redistributionsprüfung bleibt vor Produktartefakten nötig. certifi und pathspec bringen MPL-Anteile mit; kein pauschaler Freibrief für jede Änderung/Weitergabe.

Offizielles Docker-Library-Image für PostgreSQL per Digest in `scripts/local_db.py`; PostgreSQL 17.11 und dessen Debian-Copyrightdatei tatsächlich im Container gelesen (PostgreSQL-Lizenz plus dort ausgewiesene Drittanteile). Digest fixiert das beobachtete Artefakt, garantiert weder langfristige Aktualität noch Schwachstellenfreiheit. Betriebssystem-/native Komponenten nicht vom Python-Advisoryaudit abgedeckt.

`pip-audit` über alle 58 installierten Distributionen: keine bekannten Schwachstellen am Prüftag. Kein Nachweis unbekannter Schwachstellen oder vollständiger Container-/Lieferkettensicherheit. Lockfileänderungen erfordern erneute Inventur und Prüfung; keine automatische Versionsanhebung.
