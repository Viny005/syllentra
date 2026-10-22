# Lokale experimentelle Backendgrundlage

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung

Mission 9 prüft Python/FastAPI und PostgreSQL reversibel mit synthetischen Daten. Kein produktiver Identitätsdienst, keine vollständige V1 und keine endgültige Stackentscheidung. [ADR-0008](../../docs/ARCHITECTURE_DECISIONS.md#adr-0008--lokale-backendprobe-aus-mission-9), [Prüfbericht](../../docs/development/BACKEND_PROTOTYPE_REVIEW.md), [Lizenzen](LICENSES.md).

## Aufbau und Grenzen

Ein modular gegliederter Prozess: `api.py` für validierte Anwendungsoperationen und aktuelle Rechte, `security.py` für Passwort-/Sitzungsnachweise, `limits.py` für begrenzte Eingaben. Direkte parametrisierte psycopg-Abfragen statt zusätzlichem ORM. Keine Worker, Queue, KI, Vektordatenbank oder externen Dienste. Spätere Worker müssen dieselben aktuellen Konto-/Objekt-/Funktionsgrenzen prüfen; heute nicht implementiert.

Der normale lokale Einstieg `syllentra_backend.local:app` legt **keine Konten an** und verweigert jede Anmeldung mit 503. Registrierung, OTP, neue Geräte, Recovery und MFA sind nicht implementiert; entsprechende Endpunkte existieren nicht. Es gibt keinen öffentlichen Verifikations-, Seed- oder Bootstrapweg. Das interne Python-Testharness ermöglicht ausschließlich gegen `syllentra_test` die Anmeldung künstlicher bereits verifizierter Konten mit künstlichem autorisiertem Gerätenachweis. Diese Fixtures sind kein ausgeführter OTP-/Geräteverifikationsprozess. Kein Schalter in HTTP-Headern, Queryparametern oder im Frontend aktiviert das Testharness.

## Reproduzierbarer lokaler Einstieg

Voraussetzungen: bestehendes Docker mit lokalem Daemon, Python 3.12 und `uv`. Keine Installation über fremde Shellskripte. Der Container ist ausschließlich für synthetische Daten bestimmt, loopbackgebunden, ressourcenbegrenzt und verwendet flüchtigen tmpfs-Speicher. Kein Cloudhosting. Vor Ausführung prüfen, dass Port 55439 und Containername frei sind. Niemals Produktionsdatenbanken einsetzen.

Vom Repositoryverzeichnis:

```bash
cd prototypes/backend
uv sync --locked --cache-dir /tmp/syllentra-uv
python scripts/local_db.py start
.venv/bin/python scripts/migrate.py
PYTHONPATH=src .venv/bin/uvicorn syllentra_backend.local:app --host 127.0.0.1 --port 8000 --no-access-log
```

Das Startscript verwendet das offizielle Image `postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27` (beobachtet: PostgreSQL 17.11, Debian Bookworm). Bei fehlendem Image zuerst diesen Digest bewusst mit `docker pull` beziehen. Kein veränderlicher Tag im Startscript. PostgreSQL-Lizenz und Debian-Paketbeilage gelesen; das gesamte Betriebssystemimage ist damit nicht sicherheits-/lizenzfreigegeben.

Zufällige lokale Datenbankpasswörter werden ausschließlich in ignoriertem `.local/database.json` (0600, Verzeichnis 0700) abgelegt und nicht ausgegeben. `syllentra_prototype` bleibt ohne Konten, `syllentra_test` enthält nur kurzlebige Fixtures. Der Migrationszugang besitzt DDL-Rechte, der getrennte APIzugang `syllentra_runtime` nicht. Lokale Dateirechte ersetzen kein produktives Secretmanagement. Keinen Debugger, Requestbody-/Authorizationlog oder öffentliche Bindung aktivieren.

Das Script überschreibt vorhandenen Zustand nicht. Stoppen/Entfernen des eigenen Containers verwirft den tmpfs-Datenbestand; die lokale Zustandsdatei wird dadurch ungültig. Nach bewusster eigener Bereinigung erneut starten und migrieren. **Kein Nachweis dauerhafter Speicherung über Containerneustart, kein Backup oder Restore.** PostgreSQL-Persistenz ist hier nur über getrennte Verbindungen im laufenden lokalen Container geprüft. Auf Hardware ohne zuverlässiges isoliertes Docker/PostgreSQL Tests als blockiert melden, nicht auf SQLite umstellen und PostgreSQL-Erfolg behaupten.

Prüfungen aus `prototypes/backend`:

```bash
.venv/bin/pytest -q
.venv/bin/mypy src scripts
.venv/bin/ruff check src tests scripts
.venv/bin/ruff format --check src tests scripts
.venv/bin/pip-audit --cache-dir /tmp/syllentra-pip-audit --format json
```

Die Tests migrieren ausschließlich `syllentra_test` und löschen/ersetzen deren künstliche Fixtures. Nicht parallel gegen dieselbe Testdatenbank ausführen. Entwicklungsdaten bleiben getrennt. Die Syntaxgrenze 16 KiB, zehn synthetische Loginversuche pro Prozess/Minute und 15 Minuten Testsession sind bewusst begrenzte **Experimentparameter**, keine genehmigten V1-Fristen, Quoten oder SLO.

## Minimales Datenmodell und Migration

| Tabelle | Zweck / Integrität |
|---|---|
| accounts | UUID, eindeutiger Login, Argon2id-Hash, Benutzer-/Administrationskonto, pending/verified, active/suspended/deleted; keine Super-Admin-Identität |
| devices | Kontobindung, SHA-256 des zufälligen künstlichen Gerätenachweises, aktuelle Autorisierung; kein Ersatz für echte Geräteverifikation |
| sessions | SHA-256 des zufälligen Sitzungstokens als Schlüssel, Konto/Gerät, Ablauf, Widerruf; zusammengesetzter Fremdschlüssel verhindert kontoabweichendes Gerät |
| notes | Eigene künstliche Notiz, begrenzter Titel/Text, Eigentumsindex und Löschzeitpunkt; Inhalt bleibt beim Softdelete gespeichert |
| capabilities | Kontrollierter Funktionsname, hidden/unavailable/available, erlaubte Kontoart; validierte persistente Serverkonfiguration |
| schema_migrations | Angewandter Dateiname und SHA-256; historische Migrationen nach Anwendung unveränderlich |

[001_foundation.sql](migrations/001_foundation.sql) erzeugt Schema/Constraints und ausschließlich Funktionskonfiguration, keine Konten. `scripts/migrate.py` verwendet Transaktion, Advisory-Lock und Prüfsummenvergleich; Wiederholung erhält Daten, veränderte Historie stoppt sicher. Runtime darf Konten/Geräte/Flags nur lesen, Sitzungen einfügen und widerrufen, Notizen lesen und ausschließlich Titel/Text/Löschzeitpunkt ändern. Kein DDL, kein Ändern des Eigentümers oder der Kontorolle. Neue Schemastände benötigen neue Migration; kein automatisches destruktives Downgrade.

Notizlöschung verlangt das Ziel als `X-Confirm-Delete`, setzt `deleted_at` und sperrt weitere Zugriffe. Das ist ein getesteter Softdelete, **keine endgültige physische Löschung**, kein vollständiger Papierkorb und kein fertiger Kontolöschprozess nach SEC-15/16. Purge, Retention, Export, Derivate, Offline-/Restoremarker bleiben offen. Die API besitzt kein Kontoanlage-/Kontolöschrecht.

## APIvertrag

[openapi.json](openapi.json) ist ein erzeugter, im Test mit der Anwendung verglichener Vertragsstand; Swagger/ReDoc/OpenAPI-HTTPendpunkte sind ausgeschaltet. JSON-Eingaben verbieten zusätzliche Modellfelder. Öffentliche Fehler spiegeln weder Eingabewerte noch DBdetails. Private Antworten tragen `Cache-Control: no-store`.

| Methode / Pfad | Zugriff / tatsächliches Verhalten |
|---|---|
| GET /health | Öffentlich; ausdrücklich local-experimental und authentication unavailable; keine Datenbankbereitschaftsgarantie |
| POST /auth/login | Normal immer 503; im internen Testharness nur verifiziertes aktives künstliches Benutzerkonto mit Passwort und autorisiertem künstlichem Gerät; keine Adminanmeldung |
| GET /session | Gültige Sitzung; eigene Konto-ID/Kontoart und synthetic-test-only, keine Hashes, Gerätegeheimnisse oder Tokens |
| POST /auth/logout | Aktuelle Sitzung atomar widerrufen, 204; Folgezutritt 401; kein fremder Token als Parameter |
| GET /capabilities | Authentifiziert; aktuelle freigegebene/uneingeschränkt verfügbare oder sichtbare unverfügbare Modi, hidden ausgelassen; Rollenrechte wirken zusätzlich |
| GET /notes | Eigene nicht gelöschte künstliche Notizen, maximal 50, stabile UUID-Sortierung; keine Pagination implementiert |
| GET /notes/{note_id} | Eigener nicht gelöschter Datensatz; fremd, gelöscht und unbekannt einheitlich 404 |
| PATCH /notes/{note_id} | Nur eigener Datensatz unter aktuellem Notizrecht; Titel/Text validiert; Besitzer nicht änderbar |
| DELETE /notes/{note_id} | Eigenes aktuelles Recht und explizite Zielbestätigung; Softdelete, 204 |
| GET /administration | Identität wird geprüft, danach immer 403; kein funktionsfähiger Administrationshandler |

401 bedeutet fehlende/ungültige/abgelaufene/widerrufene oder nicht mehr berechtigte Sitzung; 403 gesperrte Funktion/Browserintegration, 409 fehlende Löschbestätigung, 413 zu große Eingabe, 422 ungültige Eingabe, 429 Testloginbudget, 503 fehlender Identitätsweg/Datenbankfehler. Keine Tokens in URLs. Bearer nur im Authorization-Header; keine Cookies, CORS oder Querytoken-Alternative.

## Sitzung, Rechte und Bedrohungen

Argon2id mit gesalzenen Bibliotheksparametern, begrenzte Passwortlänge, Dummyhashprüfung für unbekannte Logins. Nachweislücken werden nicht durch neue Rollen oder Dauerfristen übergangen. Zufälliges 256-Bit-Bearertoken; nur sein SHA-256 liegt in PostgreSQL. Bei jedem Zugriff aktuelle Verifikation, Kontostatus, Gerät, Ablauf und Widerruf nachschlagen; Rollen nicht im Token einfrieren. Die Ablaufuhr ist für deterministische Tests injizierbar, zur Laufzeit UTC. Transaktion inklusive Commit endet vor der Antwort; Fehler liefern keine irreführende Erfolgsmeldung.

Alle Notizabfragen enthalten `account_id = authentifizierte Identität`; Clientheader, Querywerte und Objektkennungen ersetzen diese nie. Auch direkte PATCH/DELETE-Aufrufe prüfen den aktuellen Serverflag. Administratoren erhalten kein Notizrecht. Die lokale Serverkonfiguration darf keine neue Funktion aus Text oder URL ausführen. Konfigurationseditor, Historie, Vorschau, Rollback und Adminrechte fehlen und bleiben gesperrt.

Adminbootstrap ist ausschließlich vorbereitet als Grenze/Protokollbedarf: null privilegierte Standardkonten; vor jeder zukünftigen Erstbesetzung Eigentümerauftrag, geprüfte Identitäts-/MFA-/Recoverybindung, atomare Einmaligkeit, Audit und Nachweis gegen Konkurrenz/Replay. Erst danach genau ein Super Admin gemäß S3.5. Hier weder Bootstrapkommando noch Standardpasswort oder realer Super Admin; die allgemeine Kontoart administrator ist keine Implementierung der Super-Admin-/Delegationsrollen.

Anwendungsschutz ist **kein PostgreSQL-RLS-Beweis**: Der begrenzte Servicedatenbankzugang kann alle für seinen Zweck freigegebenen Zeilen lesen. Prozess-/DBkompromittierung, produktive Konkurrenzfälle zwischen Rechteänderung und laufender Operation, verteiltes Ratelimiting, Audit/Alarmierung und Secretrotation benötigen weitere Arbeit. Keine komplette Pentest-/ASVS-Konformität behaupten.

## Frontendanschluss und nächste Sperren

Der bestehende [Frontend-Prototyp](../frontend/README.md) bleibt Demo mit acht Bereichen, DE/FR/EN, Themes, Navigation und unveränderten UItests. Keine Testsession im Browser, kein Token in localStorage, keine Übernahme von Demoressourcen als authentifizierte Inhalte. Auch ein erfolgreicher Healthcheck ist keine authentifizierte Session. Browser-Origin-Requests werden absichtlich 403 gesperrt, kein CORS-Wildcard oder automatische Backendverbindung.

Reihenfolge der späteren Integration: Identitätsentscheidung und OTP-/Geräte-/Recovery-/MFA-Negativtests; geprüfte Browsertransportsitzung einschließlich CSRF/CORS/HTTPS; schmale getrennte APIadapter mit Laufzeitvalidierung auf Basis des Vertrags; ausdrücklicher Demo-/Kontowechsel mit Bereinigung; zunächst eigene Notizen und Fähigkeiten; End-to-End-A/B-, Logout-, Ablauf-/Widerrufs- und Nichtverfügbarkeitsfälle. Keine versteckte Zusammenführung beider Datenquellen. Erst nach separater Berechtigung aktivieren. [Integrationsfolge](../../docs/development/INTEGRATION_ROADMAP.md).

Offen bleiben echte Registrierung/OTP, Geräteverwaltung, MFA/Recovery, sichere einmalige Super-Admin-Erstbesetzung, Endnutzerkonto-Lifecycle, HTTPS/Ruhendverschlüsselung, Sicherung/Restore, Audit/Retention, Last-/Parallelitätsnachweise und Datenschutzfreigabe. Alle 14 TECH-O und FE-56 bleiben offen; 46 REL sind nicht insgesamt bestanden. Keine Cloud, Ausgaben, externen Benutzerkonten, KI oder Veröffentlichung durchgeführt.
