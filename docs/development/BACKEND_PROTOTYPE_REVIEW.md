# Prüfbericht — lokale Backendgrundlage Mission 9

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung

## Umfang und Ausgang

Vollständiger Nutzerauftrag Mission 9, Abschnitte 1–12. Sauberer bestehender Branch `docs/spec/p1-p2-mobile-workspaces`, HEAD/Remote/PR-Ref `8ad51e8ef1ed010b20907602fe742268d799621e`, main `beb66e1cd399f4a0fab55d3fd476a77d7804c5a7`; PR #1 auf öffentlicher GitHub-Seite OPEN. Bereits 112 Dateien / +26.168 / −217 gegen main. [ADR-0008](../ARCHITECTURE_DECISIONS.md#adr-0008--lokale-backendprobe-aus-mission-9) begründet getrennten Verzeichnis-/Commitreview auf autorisierter Branch, ohne neue Branch/PR und ohne Änderung an main.

[Backendanleitung](../../prototypes/backend/README.md) dokumentiert Architektur, Datenmodell, Verträge, Sitzungen und Grenzen. [OpenAPI](../../prototypes/backend/openapi.json) wird im Test mit den tatsächlich registrierten Routen verglichen. Keine Produktentscheidung geändert: FE-57 getrennte Administration nur abgegrenzt, nicht implementiert; FE-58 Serverflags teilweise experimentell belegt; FE-59/60/61 nicht als vollständiger Registrierungs-/Verifikationsweg umgesetzt. Fehlende OTP-/Geräte-/MFA-/Recoveryverfahren bleiben blockiert. Keine Ausnahme von N2 für reale Benutzer.

## Tatsächlich ausgeführte Prüfungen

Python 3.12.14; PostgreSQL 17.11 im digestfixierten offiziellen Docker-Image, lokale tmpfs-Datenbank; separater eingeschränkter Runtimezugang und privilegierter Migrationszugang. Keine SQLite-Ersatztests. Tests nur in `syllentra_test`, Entwicklungsdatenbank ohne Konten. Node 24.19.0, bestehender Chromium 154.0.8037.57; Frontendumfang und Abhängigkeiten unverändert.

| Prüfung / reproduzierbarer Befehl | Tatsächliches Ergebnis / Grenze |
|---|---|
| uv sync --locked --cache-dir /tmp/syllentra-uv | 58 Distributionen installiert; exakte Versionen/Artefakthashes in uv.lock, Lizenzinventur gelesen; keine System-/Cloudinstallation |
| .venv/bin/pytest -q | 44 Tests bestanden: Unitanteil Passwort/Budget und tatsächliche API-/PostgreSQL-Integration; keine übersprungenen Tests |
| Authnegative | Fehlende/ungültige/abgelaufene/widerrufene Sitzung, pending/suspended, unbekanntes/nicht autorisiertes Gerät, falsches Passwort, Adminlogin, Client-Testschalter verweigert |
| Isolation / Persistenz | A/B-Listen und Einzelobjekte, fremdes Lesen/Ändern/Löschen, Eigentumsparameter und Header, Rechte-/Geräte-/Rollenwechsel nach Sitzungserteilung; neue Verbindung sieht erlaubte Änderung |
| SQL-/Migrationsgrenzen | Wiederholte Migration idempotent; veränderte historische Migration verweigert; FK gegen kontoabweichendes Gerät; ungültige Flagwerte; Runtime kann weder Kontorolle noch Eigentümer ändern |
| Flags / Administration | hidden/unavailable sperren direkte GET/PATCH/DELETE; nur aktuelle erlaubte Benutzerrolle; künstliche Adminsession erhält weder Administration noch private Notizen; keine echte Adminanlage |
| Eingaben / Fehler / Löschung | Ungültige UUID, Zusatzfelder, leerer Titel, große Eingabe, fehlende Zielbestätigung; kein Passwort-/Eingabe-/DBdetail-Echo; Softdelete aus Folgeansichten entfernt |
| .venv/bin/mypy src scripts | Strict-Typecheck erfolgreich, acht Quelldateien |
| .venv/bin/ruff check src tests scripts; ruff format --check | Lint und Format erfolgreich; neun Pythondateien |
| pip-audit --cache-dir /tmp/syllentra-pip-audit --format json | 58 Distributionen, keine bekannten Advisories; keine Container-/nativen Sicherheitsnachweise |
| Echter lokaler HTTP-Smoke über Uvicorn | /health 200; /session, /notes, /administration anonym 401; /auth/login normal 503; keine offen aktivierte Auth |
| Frontend: npm run build, lint, format:check, test, test:e2e | Build/strict TypeScript/Lint/Format erfolgreich; sieben Unit- und neun Chromium-Szenarien bestanden, 17 axeanalysen ohne gemeldeten Verstoß; keine vollständige WCAG-Abnahme |
| Frontend: npm audit --json | Null bekannte Schwachstellen aller Schweregrade am Prüftag |

Ein anfänglicher Passworttest zeigte `InvalidHashError` bei beschädigtem Hash; gezielt behandelt und unverändert als Negativtest erhalten. FastAPI/Starlette meldet eine Deprecation für HTTPX im Testclient; nicht unterdrückt. Ablösung des Testtransports vor künftigem inkompatiblem Update prüfen, kein derzeit fehlgeschlagener Test. Cacheorte liegen explizit im beschreibbaren lokalen Arbeitsbereich; keine dafür benötigte Systemänderung.

## Vollständige Einordnung der 46 Releasekontrollen

Jede Zeile beschreibt den begrenzten Experimentbeleg oder fehlenden Umfang, **keine insgesamt bestandene Produktkontrolle**. Maßgeblich bleiben [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md), [N2](../spec/N2-querschnittskonzepte.md) und [S3](../spec/S3-inbetriebnahme.md). UIbelege ergänzen den historischen [Frontendbericht](../design/PROTOTYPE_REVIEW.md). Keine Statusänderung der fachlichen Prüfentwürfe.

| Kontrolle | Stand / Beleg oder verbleibende Grenze |
|---|---|
| REL-S01 | Teilbeleg: ignorierte lokale zufällige DBcredentials, keine Werte im Git; produktives Secretmanagement offen. |
| REL-S02 | Teilbeleg: Diff-/Mustervalidierung; kein vollständiger Historien-/Secretscannerbeweis. |
| REL-S03 | Teilbeleg: globales endliches Testloginbudget und 429 getestet; konto-/IP-/OTP-/Recoverylimits fehlen, echte Anmeldung blockiert. |
| REL-S04 | Teilbeleg: PostgreSQL-A/B-API-Negativtests und unveränderlicher Eigentümer; weitere Datenwege fehlen. |
| REL-S05 | Teilbeleg: Argon2id und generische Fehler; vollständige Identitäts-/Resetverfahren offen. |
| REL-S06 | Teilbeleg: Serverflags und getrennte Kontoart; Adminoperationen/MFA/Delegation gesperrt. |
| REL-S07 | Teilbeleg: keine Runtimegeheimnisse im Frontend, unveränderte Demo; produktive Konfiguration offen. |
| REL-S08 | Offen: ausschließlich Loopback-HTTP, kein HTTPS-/Transportfreigabebeleg. |
| REL-S09 | Teilbeleg: Hashsitzung, Ablauf/Widerruf/aktueller Gerätestatus; echte Geräte-/Sessionschnittstelle offen. |
| REL-S10 | Teilbeleg: begrenzte validierte JSON-/UUIDwerte und parametrisierte SQLabfragen; keine Import-/Webhookwege. |
| REL-S11 | Nicht in dieser Tranche: keine Datei-/Medienuploads; spätere Prüfung bleibt nötig. |
| REL-S12 | Nicht in dieser Tranche: keine Archive/Parser; spätere Prüfung bleibt nötig. |
| REL-S13 | Browserintegration bewusst gesperrt; kein CORS/Cookie-/CSRF-Produktnachweis. |
| REL-S14 | Teilbeleg: generische Eingabe-/Dienstfehler; produktive Diagnose/Incidentwege offen. |
| REL-S15 | Teilbeleg: kein Passwort-/Token-/DBdetail-Echo; Audit/Retention und vollständige Loggingprüfung offen. |
| REL-S16 | Teilbeleg: unbekanntes/unverifiziertes/administratives Konto und falsches Passwort liefern gleichen 401-Code; echte Recovery/OTP-Anti-Enumeration offen. |
| REL-S17 | Nicht in dieser Tranche: keine Webhooks/externe Verbindungen; öffentliche API noch nicht freigegeben. |
| REL-S18 | Teilbeleg: Lockfile, Lizenzinventur und Python-/npm-Advisories; native/Imagekomponenten nicht vollständig geprüft. |
| REL-S19 | Blockiert: E-Mail-OTP nicht implementiert; pending verweigert, aber künstliche verified-Fixtures sind kein Nachweis realer E-Mail-Verifikation. |
| REL-S20 | Offen: keine verschlüsselte unabhängige Sicherung oder Restore; tmpfs ist kein Backup. |
| REL-Q01 | Teilbeleg: endliches globales Testloginbudget; kein verteilter Missbrauchs-/Kostenstoppbeleg. |
| REL-Q02 | Teilbeleg: begrenzte Requestgröße und Liste, Containerressourcen; keine V1-Quota-/Lastmessung. |
| REL-Q03 | Nicht in dieser Tranche: keine KI-/kostenpflichtigen Aufrufe; spätere Kostenbegrenzung offen. |
| REL-Q04 | UIfehlermeldungen als Regression geprüft; APIfehler sind datensparsame Codes, deren übersetzter Browseranschluss noch fehlt. |
| REL-Q05 | UI-Simulationslade-/Stopzustände als Regression geprüft; echte asynchrone Backendjobs und zugänglicher Fortschritt nicht implementiert. |
| REL-Q06 | Teilbeleg: Serverflags und erhaltene UI-Demo; keine Release-/Testergruppenadministration. |
| REL-Q07 | Offen: keine Worker/Jobwiederaufnahme; APItransaktion vor Antwort abgeschlossen. |
| REL-Q08 | Teilbeleg: DBconnect-Timeout und Dienstfehler; keine verteilten Retry-/Abbruchnachweise. |
| REL-Q09 | Teilbeleg: Migration wiederholbar, Logout/Softdelete folgen aktuellem Zustand; keine allgemeine Idempotenzschicht. |
| REL-Q10 | Nicht anwendbar auf V1-Tranche: Zahlung bleibt spätere Option, nicht aktiviert. |
| REL-Q11 | Teilbeleg: nur synthetische Daten, minimale Sessionantwort; keine Medien-/temporären Transkripte. |
| REL-Q12 | Teilbeleg: Eigentumsindex und begrenzte eigene Liste; keine Suche-/Last-/Queryplanmessung. |
| REL-Q13 | Offen: Liste auf 50 begrenzt, keine Folgeseiten/Pagination implementiert. |
| REL-Q14 | Nicht durchgeführt: keine Übertragungs-/Kompressions-/Seitenkanalmessung. |
| REL-Q15 | Nicht in dieser Tranche: keine Uploads/Parser; Ressourcenstress nicht getestet. |
| REL-Q16 | Teilbeleg: no-store und keinerlei Browserkontodaten; PWA-/Offline-/Index-/Restorelöschung offen. |
| REL-Q17 | Offen: kein Monitoring/Alarm-/Verfügbarkeitsnachweis; health keine DBbereitschaftsgarantie. |
| REL-Q18 | Offen: sichere Fehler Teilbeleg; Audit, Korrelation, Retention und Incidentübung fehlen. |
| REL-Q19 | Teilbeleg: A/B-Integration und aktuelle Rechte; keine parallele V1-Last-/Raceabnahme. |
| REL-Q20 | Offen: keine unabhängige verschlüsselte Wiederherstellung oder Nichtwiederbelebungsprüfung. |
| REL-A01 | Nicht in dieser Tranche: keine KI/Agenten; Prompt-Injection-Test ausstehend. |
| REL-A05 | Nicht in dieser Tranche: keine KI-Quellenantworten; pädagogische Abnahme ausstehend. |
| REL-A07 | Nicht in dieser Tranche: keine Parser-/URLabrufe; SSRF-/Archivkorpus ausstehend. |
| REL-A13 | Offen: keine Releasepipeline/Artefaktfreigabe; Lockfile ist nur Teilbeleg. |
| REL-A16 | UIregression mit bestehenden Tastatur-/axeprüfungen; keine Auth-UI und keine WCAG-Konformitätsfreigabe. |
| REL-A18 | Nicht in dieser Tranche: keine Bewertungen/Quiz/Adaptivität; alle 28 AT-L bleiben Sollfälle. |

## Verbleibende Blocker und nächste Tranche

Kein produktiver Authdienst; echte Verifikation, neue Geräte, Recovery, Admin-MFA/Bootstrap und sichere Browsertransportsitzung sind Voraussetzungen vor Freigabe realer Nutzer. Globale Prozessrate ist nur lokaler Schutz, kein skalierbares Loginlimit. Native/Betriebssystemlieferkette, Audit, Ruhendverschlüsselung und unabhängiger Restore nicht geprüft. SQLfilter sind kein RLS; unbekannte/gleichzeitige Rechtewechsel und laufende Transaktionen benötigen erweiterte Tests. Softdelete bewahrt Inhalt; endgültige Löschung/Retention/Nichtwiederbelebung fehlen. Keine Speicherung über Containerneustart behauptet.

Empfohlen: zunächst Eigentümerreview dieser Tranche und TECH-O-05/06, dann isolierter Identitäts-Proof-of-Concept mit tatsächlichem E-Mail-OTP, Geräteverifikation, Recovery, verpflichtender Admin-MFA und deren Negativtests. Keine echte Zustellung oder externe Identität ohne gesonderten geeigneten Auftrag. Danach Browserintegration einer einzigen eigenen Notizfunktion mit ausdrücklichem Demo-/Kontowechsel und Ende-zu-Ende-A/B-/Logouttests. Keine vollständige V1 unter 20 EUR bewiesen; alle 14 TECH-O und FE-56 offen.


## Dokumentintegrität und öffentliche Inhalte

74 Markdown-Dateien, 966 lokale Links, 669 Tabellen geprüft; keine Struktur-/Linkfehler. 1.376 historische Anker erhalten; 14 Mermaid-Quellblöcke unverändert, kein neuer Renderlauf behauptet. Primärkataloge byte-/zeilenweise erhalten: 89 FE (FE-56 offen), 66 UC, 25 DEC-V1, DEC-48/49, 46 REL, 28 AT-L, 20 AT-S3, 14 TECH-O. Frontendcode, Tests, Abhängigkeiten und Lockfile bytegleich zum Ausgang. E3 nur additiv samt Versionsfortschreibung; keine alten Nachweise entfernt. Acht bestehende Dateien angepasst, 18 neue Dateien im Backend-/Berichtsumfang. Öffentliche Änderungen auf Secretmuster und tatsächlich erzeugte lokale DBpasswörter geprüft, keine Treffer; ignorierte Credentials/Caches nicht versioniert. Keine vollständige Historien-/Secretscanner-Garantie. git diff --check erfolgreich. Technische Empfehlungen weiter zur Entscheidung, fachliche Spezifikation Zur Prüfung.
