# Validierung — lokale Identitätsprobe Mission 10

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung

## Ausgang, Auftrag und Reviewgrenze

Vollständiger Nutzerauftrag Mission 10, Abschnitte 1–18; bestehender Branch `docs/spec/p1-p2-mobile-workspaces`, lokaler/Remote-/PR-Ref `cd971cd57ff7c968d6439375aaf1c1798cf16a81`, main `beb66e1cd399f4a0fab55d3fd476a77d7804c5a7`, Arbeitsbaum sauber und PR #1 öffentlich OPEN geprüft. Bereits 130 Dateien / +29.649 / −217 gegen main. [ADR-0009](../ARCHITECTURE_DECISIONS.md#adr-0009--lokale-identitätsprobe-aus-mission-10) begründet separaten Reviewcommit auf erlaubter Branch; keine neue Branch/PR, keine Umschreibung, kein Merge oder Deployment. Eine spätere gestapelte Aufteilung braucht Zustimmung und eine Reviewbasis gegen die Spezifikationsbranch, um vorhandene Änderungen nicht zu duplizieren.

[Architektur](IDENTITY_ARCHITECTURE.md) und [Startanleitung](../../prototypes/backend/README.md) beschreiben tatsächlichen Umfang: synthetische Registrierung, gebundener E-Mail-OTP über privaten lokalen Adapter, bekannte/neue Geräte, Hashsitzungen, Widerruf, Zweikanal-Recovery und eigene Reactansicht. Standardbackend bleibt geschlossen, alte Testharness-Anmeldeverzweigung entfernt. Keine tatsächliche E-Mailzustellung, öffentliche Identität oder operative Administration; keine reale Offlinecodeausgabe und keine endgültige TECH-O-05/06-Entscheidung.

## Tatsächliche Prüfungen und Grenzen

Python 3.12.14, FastAPI 0.161.0, PostgreSQL 17.11 im vorhandenen digestfixierten lokalen Dockercontainer, strikt getrennte Datenbanken `syllentra_test`/`syllentra_prototype`, keine SQLite-Ersatztests. Node 24.19.0, vorhandener Chromium 154.0.8037.57 und OpenSSL 3.5.7. Keine neue Abhängigkeit installiert; Python-/npm-Lockfiles und alle Paketfassungen unverändert.

| Prüfung / Befehl | Tatsächlicher Befund |
|---|---|
| .venv/bin/pytest -q | 66 Tests bestanden, keine übersprungenen Tests. Bisherige 44 Testfälle erhalten und an den echten lokalen Weg angepasst, 22 weitere Identitäts-/Privatkanal-/Parallelfälle. |
| Registrierung / Wiederholung | Pending sperrt Daten, ASCII-/Adressnormalisierung, eindeutiges Konto, Argon2id, keine Adminfelder, Duplikat überschreibt Passwort nicht; korrekte Pending-Anmeldung kann neuen gebundenen Lauf starten. |
| OTP / Zustellung | Richtiger/falscher/abgelaufener/wiederverwendeter Code, fremder Preauth-Cookie, fünf verbrauchte Fehlversuche, Neuversandgrenzen und unveränderter Ablauf; parallele korrekte Einlösung genau einmal erfolgreich. Codes nur aus internem Kanal, nicht aus APIantwort. |
| Geräte | Neue Anfrage ohne Session; fremde Freigabe verweigert; bereits autorisiertes Gerät plus Passwort und passende Referenz nötig; Antragstellerbinding, Replay, Revocation und Ablauf geprüft. |
| Recovery | E-Mail-OTP allein unzureichend; persönlicher Offlinecode zusätzlich, dessen Ablauf/Rotation und Challengereplay geprüft. Alte Sessions/Geräte entzogen, neues Passwort funktioniert, altes nicht. Keine Dokumentenschlüsseloperation implementiert. |
| Sessions / Isolation | Bisherige A/B-, Eigentums-, Rollen-/Flag-, Ablauf-/Widerrufs-/Administrationsnegative erhalten; zusätzlich tatsächlich registrierte/verifizierte A/B-Konten und parallele Lesezugriffe mit anschließender Revocation. |
| Browsergrenzen / Audit | HTTPSpflicht, falscher Origin/CSRF/Fetch-Site gesperrt; Cookies Secure/HttpOnly/SameSite Strict, Sessionfixation verworfen, kein Rohgeheimnis in DB/Audit/Antwort-JSON; Runtime kann keine Adminrolle anlegen. |
| Migrations-/Privatkanalprüfung | Wiederholbarkeit, historische Prüfsumme, FK/Constraints und frühere Eigentumsgrenzen erhalten; neue Zustände additiv. Lokale Kanaldateien 0600, Verzeichnis 0700, überbreite Dateirechte verweigert und explizites Expiry-Prune geprüft. |
| mypy src scripts | Strict erfolgreich, 13 Quelldateien. |
| Ruff check / format --check | Erfolgreich; 16 Pythondateien einschließlich Tests/Fixturehilfe. |
| pip-audit mit explizitem lokalem Cache | 58 Distributionen, null bekannte Schwachstellen am Prüftag; keine native/Image-/unbekannte Schwachstellenfreiheit bewiesen. |
| npm run build, lint, format:check, test | Strict-TypeScriptbuild, ESLint/Prettier und bisherige sieben Vitestfälle bestanden. Keine Prüfung deaktiviert. |
| npm run test:e2e | Bisherige neun Demobrowserfälle bestanden, darin 17 axeanalysen ohne gemeldeten Verstoß; acht Bereiche und Sprache/Theme/Navigation erhalten. |
| npm run test:identity | Vier weitere tatsächliche TLS-/Proxy-/PostgreSQL-Browserfälle bestanden: Registrierung/OTP/Login/Sessionwiderruf/Logout, neues Browsergerät, Zweikanal-Recovery und sechs Sprach-/Theme-Kombinationen mobil. Neun axeanalysen ohne gemeldeten Verstoß. |
| Identitätsartefakte | Zwei leere mobile Formularbilder Hell/Dunkel erzeugt und visuell geprüft; weder Passwörter/OTP noch Tokens sichtbar. Lokal/ignoriert, keine neuen öffentlichen Bilder. Auth-Traces/Videos/automatische Fehlerscreenshots deaktiviert. |
| npm audit --json | Null bekannte Schwachstellen aller Schweregrade am Prüftag. |
| OpenAPI | Snapshot mit tatsächlich registrierter Anwendung identisch; Cookie-/Bearernachweise enthalten, keine Verifikations-/Recoverysecrets als Antwortfelder. Keine Swagger-/Redoc-HTTPansicht. |

## Korrigierte Befunde und offene Beobachtung

Geräte-/Sessionsicht und Beschriftung als eigener lokaler Kontotest von der Demo abgegrenzt. Eigener Sessionwiderruf schließt die Kontosicht statt einen falschen generischen Aktionsfehler zu zeigen. Ein Theme-Test setzte seine Startpräferenzen bei derselben Hashnavigation nicht erneut; echte Neuladung im Test korrigiert, kein Themefall abgeschaltet. Serverzähler und ursprüngliche Fristen bleiben trotz Fehler/Neuversand erhalten; frühere OTPwerte werden nicht wieder ausgegeben.

Ein fehlgeschlagener Test zeigte, dass die Standardrepräsentation des Fixturekontexts lokale DBcredentials in die lokale Testdiagnose übernehmen konnte. Fixture-Repräsentation redigiert, lokale synthetische Credentials rotiert, keine solchen Diagnosen versioniert. API-/Auditausgaben enthalten keine Rohsecrets. Das ist eine tatsächlich behobene Testartefaktgrenze, keine Behauptung einer vollständigen Secretprüfung aller Historien.

**Offene Beobachtung:** Ein einzelner Sitzungsleseaufruf unmittelbar nach erfolgreicher Anmeldung schlug in einer Zwischenprüfung fehl. Ursache nicht abschließend nachgewiesen. Die abschließende vollständige 66er-Passprüfung, ein zusätzlicher Parallel-/Revocationtest und drei separate Wiederholungen genau des betroffenen Recoveryfalls bestanden ohne Wiederauftreten. Nicht als bewiesene Fehlerbehebung ausgeben; vor Produktfreigabe reproduzierbar untersuchen und unabhängig reviewen. Sichere Fehlerantworten bleiben geschlossen, keine Konto-/Privilegienumgehung beobachtet. HTTPX-Testclient-Deprecation bleibt ebenfalls sichtbar und als Wartungsbedarf offen.

## Vollständiger Abgleich der 46 Kontrollen

Referenz ist die unveränderte [kanonische Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md). Jede Zeile aktualisiert die begrenzte Prototypevidenz gegenüber dem [historischen Mission-9-Abgleich](BACKEND_PROTOTYPE_REVIEW.md). **Keine Gesamtproduktkontrolle als bestanden freigeben.** MFA, öffentliche Zustellung, Offlinecodeausgabe, Restore, Last, Datenschutz und menschliche Produktfreigabe stehen aus.

| Kontrolle | Tatsächliches Delta / verbleibender Nachweis |
|---|---|
| REL-S01 | Teilbeleg erweitert: getrenntes HMAC-Servergeheimnis und TLS-/Kanaldateien mit lokalen Rechten; kein produktives Secretmanagement. |
| REL-S02 | Teilbeleg: private Dateien/Caches ignoriert, Fixture-Diagnose redigiert und lokale Testcredentials rotiert; kein gesamter Historienbeweis. |
| REL-S03 | Lokale persistente Adress-/Netz-/Recoverybudgets, OTPversuche und Neuversandgrenzen getestet; verteilte/echte Missbrauchslast offen. |
| REL-S04 | A/B-Testdaten und echte lokale Registrierungs-/Verifikationswege geprüft; keine RLS-/Gesamtproduktisolation behauptet. |
| REL-S05 | Argon2id und lokaler Zweinachweis-Reset geprüft; reale sichere Ausgabe/Schlüsselrecovery offen. |
| REL-S06 | Aktuelle Rollen/Flags/Konto-/Geräte-/Sicherheitsrevision geprüft; kein Adminhandler oder echte MFA/Delegation. |
| REL-S07 | Keine Authsecrets in JSstorage/Bundle; Browser erhält nur notwendige geschützte Cookies, keine öffentlich ausführbare Konfiguration. |
| REL-S08 | Lokales TLS Browser -> Proxy -> Backend tatsächlich ausgeführt, Backend-CA im Proxy geprüft; Browser-Testzertifikat selbst signiert, Produktions-PKI offen. |
| REL-S09 | Ablauf/Widerruf, mehrere Sessions, Gerätesperre, eigene Revocation, Recoveryentzug und Fixationsnegative geprüft; lange V1-/Offlineziele offen. |
| REL-S10 | Strikte lokale Adress-/Passwort-/OTP-/UUID-/Extra-Feldvalidierung, endliche Bodies und SQLparameter; spätere Importformate unverändert offen. |
| REL-S11 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine Datei-/Medienuploads; spätere Prüfung bleibt nötig. |
| REL-S12 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine Archive/Parser; spätere Prüfung bleibt nötig. |
| REL-S13 | Lokale Host-Cookies, exakter Origin, CSRFvergleich und Fetch-Site-Negativfälle geprüft; keine externe CORSfreigabe oder Produktionsintegration. |
| REL-S14 | Generische APIfehler, keine Eingabewerte/SQL/Stacktraces; interne Diagnose nur Ausnahme-Klassenname, produktive Korrelation offen. |
| REL-S15 | Geheimnisfreies DBaudit geprüft, private synthetische Zustellkanäle getrennt; tatsächliche autonome Bereinigung/Monitoring noch offen. |
| REL-S16 | Status-/Antwortform bei falschem Login und Recovery/Registrierungsduplikat gegen Enumeration geprüft; Timing-/Lastbeweis fehlt. |
| REL-S17 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine Webhooks/externe Verbindungen; öffentliche API noch nicht freigegeben. |
| REL-S18 | Unveränderte Paketfassungen/Lockfiles, aktuelle Python-/npm-Audits null bekannte Befunde; OpenSSL-Kernlizenz geprüft, vollständige native/Imagefreigabe fehlt. |
| REL-S19 | Lokaler gebundener Einmalcode vor Datenzugriff implementiert und getestet; Adapter simuliert Zustellung, keine tatsächliche E-Mailkontrolle belegt. |
| REL-S20 | Unverändert gegenüber Mission 9: Offen: keine verschlüsselte unabhängige Sicherung oder Restore; tmpfs ist kein Backup. |
| REL-Q01 | Persistente lokale Budgets erweitert; realer Mehrinstanz-/Client-IP-/Quota-Missbrauchsschutz weiter offen. |
| REL-Q02 | Unverändert gegenüber Mission 9: Teilbeleg: begrenzte Requestgröße und Liste, Containerressourcen; keine V1-Quota-/Lastmessung. |
| REL-Q03 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine KI-/kostenpflichtigen Aufrufe; spätere Kostenbegrenzung offen. |
| REL-Q04 | DE/FR/EN-Identitätsfehler und Verfügbarkeit in UI ergänzt; kein vollständiger Screenreader-/Produktnachweis. |
| REL-Q05 | Lokale Requests mit Busy-Zustand und Timeout; keine Worker-/Langjobfortschrittsimplementierung. |
| REL-Q06 | Eigener Kontotest/Standard-Demo und fehlender Modus getrennt; OTP-/Geräte-/Recovery-/Sitzungszustände getestet, öffentliche Releasewege fehlen. |
| REL-Q07 | Unverändert gegenüber Mission 9: Offen: keine Worker/Jobwiederaufnahme; APItransaktion vor Antwort abgeschlossen. |
| REL-Q08 | Lokaler Browser-/DBconnect-Timeout; keine allgemeine verteilte Kompensation/Idempotenzschicht. |
| REL-Q09 | Duplikatregistrierung und paralleler OTPverbrauch geprüft; keine allgemeine Doppelabgabe-/Import-/Jobschicht. |
| REL-Q10 | Unverändert gegenüber Mission 9: Nicht anwendbar auf V1-Tranche: Zahlung bleibt spätere Option, nicht aktiviert. |
| REL-Q11 | Nur synthetische Adressen und minimale eigene Identitäts-/Session-/Gerätemetadaten; keine Schlüssel oder Rohgeheimnisse in APIs/Audit. |
| REL-Q12 | Unverändert gegenüber Mission 9: Teilbeleg: Eigentumsindex und begrenzte eigene Liste; keine Suche-/Last-/Queryplanmessung. |
| REL-Q13 | Unverändert gegenüber Mission 9: Offen: Liste auf 50 begrenzt, keine Folgeseiten/Pagination implementiert. |
| REL-Q14 | Unverändert gegenüber Mission 9: Nicht durchgeführt: keine Übertragungs-/Kompressions-/Seitenkanalmessung. |
| REL-Q15 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine Uploads/Parser; Ressourcenstress nicht getestet. |
| REL-Q16 | Keine Authsecrets im JSstorage, no-store und Kontosicht bei 401 verworfen; PWA-/Offline-/Restorekontrollstand fehlt. |
| REL-Q17 | Unverändert gegenüber Mission 9: Offen: kein Monitoring/Alarm-/Verfügbarkeitsnachweis; health keine DBbereitschaftsgarantie. |
| REL-Q18 | Begrenztes lokales Sicherheitsereignisschema und geheimnisfreie Fehlerklasse; kein produktives Audit-/Alarm-/Retentionssystem. |
| REL-Q19 | Lokale A/B-Registrierung und parallele OTP-/Sessionfälle getestet; einmalige nicht reproduzierte Sitzungsbeobachtung offen, keine Last-/Racegesamtabnahme. |
| REL-Q20 | Unverändert gegenüber Mission 9: Offen: keine unabhängige verschlüsselte Wiederherstellung oder Nichtwiederbelebungsprüfung. |
| REL-A01 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine KI/Agenten; Prompt-Injection-Test ausstehend. |
| REL-A05 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine KI-Quellenantworten; pädagogische Abnahme ausstehend. |
| REL-A07 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine Parser-/URLabrufe; SSRF-/Archivkorpus ausstehend. |
| REL-A13 | Unverändert gegenüber Mission 9: Offen: keine Releasepipeline/Artefaktfreigabe; Lockfile ist nur Teilbeleg. |
| REL-A16 | Neun Identitäts- plus 17 Demoseiten-axeanalysen ohne gemeldeten Verstoß; Sprache/Theme/Reflow und maskierte Eingaben, keine WCAG-Konformitätsabnahme. |
| REL-A18 | Unverändert gegenüber Mission 9: Nicht in dieser Tranche: keine Bewertungen/Quiz/Adaptivität; alle 28 AT-L bleiben Sollfälle. |

## Nicht implementiert, Entscheidungen und nächste Abhängigkeit

Echte Registrierung/Zustellung außerhalb example.test, reale vertrauenswürdige Offlinecodeübergabe, TOTP/WebAuthn/Passkeys, lokale PIN-/OSbiometriesperre, Admin-MFA/Bootstrap/Delegation, Dokumentenschlüsselrecovery, langlebige Datenspeicherung, unabhängiger verschlüsselter Restore, vollständige physische Löschung, produktive Last-/Timing-/Pentest-/Datenschutz-/Betriebsfreigabe nicht durchgeführt. Codes im privaten Zustellkanal sind keine echten E-Mail-/Unabhängigkeitsnachweise; Expirybereinigung beim Schreiben/Prune, kein autonomer Scheduler. Kein öffentlicher Nutzerzugang. Alle 14 TECH-O und FE-56 bleiben offen.

Empfohlen: Eigentümerreview und unabhängige Sicherheits-/Sitzungsprüfung dieses lokalen Deltas; offene Beobachtung klären. Danach gezielte technische Entscheidung/Probe für echte Faktorbindung, Offlinecodeübergabe, MFA/Recovery und einmaligen Super-Admin-Bootstrap. Erst anschließend eine eigene kontogebundene Lernfunktion im Browser anschließen; keine Demoressourcen importieren. Kein Folgeauftrag, kein Cloud- oder Ausgabenrecht durch Empfehlung.


## Dateiumfang

38 Dateien: 23 bestehende angepasst, 15 neu; 15 Backend-, 13 Frontend- und zehn Dokumentations-/Kontextdateien. Private Zustell-/TLS-/DBdateien und Testartefakte sind ignoriert und nicht enthalten.

| Datei | Änderung |
|---|---|
| [AGENTS.md](../../AGENTS.md) | Geändert |
| [README.md](../../README.md) | Geändert |
| [docs/ARCHITECTURE_DECISIONS.md](../ARCHITECTURE_DECISIONS.md) | Geändert |
| [docs/ai/CONTEXT_CHANGELOG.md](../ai/CONTEXT_CHANGELOG.md) | Geändert |
| [docs/ai/PROJECT_CONTEXT.md](../ai/PROJECT_CONTEXT.md) | Geändert |
| [docs/development/IDENTITY_ARCHITECTURE.md](IDENTITY_ARCHITECTURE.md) | Neu |
| [docs/development/IDENTITY_PROTOTYPE_REVIEW.md](IDENTITY_PROTOTYPE_REVIEW.md) | Neu |
| [docs/development/INTEGRATION_ROADMAP.md](INTEGRATION_ROADMAP.md) | Geändert |
| [docs/spec/E3-pruefnachweis.md](../spec/E3-pruefnachweis.md) | Geändert |
| [docs/spec/README.md](../spec/README.md) | Geändert |
| [prototypes/backend/LICENSES.md](../../prototypes/backend/LICENSES.md) | Geändert |
| [prototypes/backend/README.md](../../prototypes/backend/README.md) | Geändert |
| [prototypes/backend/migrations/002_local_identity.sql](../../prototypes/backend/migrations/002_local_identity.sql) | Neu |
| [prototypes/backend/migrations/003_proof_lifetimes.sql](../../prototypes/backend/migrations/003_proof_lifetimes.sql) | Neu |
| [prototypes/backend/openapi.json](../../prototypes/backend/openapi.json) | Geändert |
| [prototypes/backend/scripts/identity_server.py](../../prototypes/backend/scripts/identity_server.py) | Neu |
| [prototypes/backend/scripts/migrate.py](../../prototypes/backend/scripts/migrate.py) | Geändert |
| [prototypes/backend/scripts/prepare_identity.py](../../prototypes/backend/scripts/prepare_identity.py) | Neu |
| [prototypes/backend/src/syllentra_backend/api.py](../../prototypes/backend/src/syllentra_backend/api.py) | Geändert |
| [prototypes/backend/src/syllentra_backend/delivery.py](../../prototypes/backend/src/syllentra_backend/delivery.py) | Neu |
| [prototypes/backend/src/syllentra_backend/identity.py](../../prototypes/backend/src/syllentra_backend/identity.py) | Neu |
| [prototypes/backend/src/syllentra_backend/identity_routes.py](../../prototypes/backend/src/syllentra_backend/identity_routes.py) | Neu |
| [prototypes/backend/tests/private_fixtures.py](../../prototypes/backend/tests/private_fixtures.py) | Neu |
| [prototypes/backend/tests/test_identity.py](../../prototypes/backend/tests/test_identity.py) | Neu |
| [prototypes/backend/tests/test_security.py](../../prototypes/backend/tests/test_security.py) | Geändert |
| [prototypes/frontend/README.md](../../prototypes/frontend/README.md) | Geändert |
| [prototypes/frontend/package.json](../../prototypes/frontend/package.json) | Geändert |
| [prototypes/frontend/playwright.identity.config.ts](../../prototypes/frontend/playwright.identity.config.ts) | Neu |
| [prototypes/frontend/src/App.tsx](../../prototypes/frontend/src/App.tsx) | Geändert |
| [prototypes/frontend/src/layouts/Shell.tsx](../../prototypes/frontend/src/layouts/Shell.tsx) | Geändert |
| [prototypes/frontend/src/locales/de.json](../../prototypes/frontend/src/locales/de.json) | Geändert |
| [prototypes/frontend/src/locales/en.json](../../prototypes/frontend/src/locales/en.json) | Geändert |
| [prototypes/frontend/src/locales/fr.json](../../prototypes/frontend/src/locales/fr.json) | Geändert |
| [prototypes/frontend/src/pages/Identity.tsx](../../prototypes/frontend/src/pages/Identity.tsx) | Neu |
| [prototypes/frontend/src/pages/Settings.tsx](../../prototypes/frontend/src/pages/Settings.tsx) | Geändert |
| [prototypes/frontend/src/styles/app.css](../../prototypes/frontend/src/styles/app.css) | Geändert |
| [prototypes/frontend/tests/identity/identity.spec.ts](../../prototypes/frontend/tests/identity/identity.spec.ts) | Neu |
| [prototypes/frontend/vite.identity.config.ts](../../prototypes/frontend/vite.identity.config.ts) | Neu |


## Dokumentintegrität und öffentliche Inhalte

76 Markdown-Dateien, 1.043 lokale Links und 674 Tabellen geprüft, keine Struktur-/Linkfehler; 1.397 historische Anker erhalten und 14 Mermaid-Quellblöcke unverändert. 89 FE, 66 UC, 25 DEC-V1, DEC-48/49, 46 REL, 28 AT-L, 20 AT-S3 und 14 TECH-O inhaltlich erhalten; FE-56 offen. Bestehende Fachprimärquellen unverändert, E3 additiv/versioniert und Index fortgeschrieben. Migration 001, beide Lockfiles/Paketfassungen sowie die ursprünglichen UItestdateien bytegleich. Alle 18 bisherigen Backendtestfunktionen/44 Fälle erhalten, kein Skip/Xfail ergänzt. 38 autorisierte Dateien, keine privaten Kanal-/TLS-/DBdateien oder Diagnoseartefakte versioniert. Bekannte aktuelle lokale DB-/HMAC-/Zustellgeheimnisse und Secretmuster gegen öffentliche Änderungen verglichen, keine Treffer; keine Garantie für unbekannte Geheimnisse oder vollständige Historie. git diff --check erfolgreich; abschließende vollständige PostgreSQLsuite erneut 66/66 mit ignoriertem lokalem JUnitbeleg.
