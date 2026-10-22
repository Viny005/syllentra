# Lokale experimentelle Backendgrundlage

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung

Mission 10 erweitert die lokale Sicherheitsprobe aus Mission 9 um tatsächlich testbare synthetische Identität. Keine öffentliche Registrierung, produktive Authentifizierung, echte Mailzustellung oder endgültige Stackwahl. [Identitätsarchitektur](../../docs/development/IDENTITY_ARCHITECTURE.md), [aktueller Prüfbericht](../../docs/development/IDENTITY_PROTOTYPE_REVIEW.md), [historische Mission 9](../../docs/development/BACKEND_PROTOTYPE_REVIEW.md), [Lizenzen](LICENSES.md).

## Aufbau und Grenzen

FastAPI/Python mit PostgreSQL, direktem psycopg, Argon2id und getrennten Modulen für API, Identitätsübergänge, Eingabegrenze, Kryptonachweise und private lokale Zustelladapter. Kein externer IdP, keine Worker/Queue/KI. `syllentra_backend.local:app` bleibt ohne aktivierten Identitätsdienst und verweigert Anmeldung mit 503. Die bisherige Anmeldeverzweigung `synthetic_test_harness` ist entfernt. Nur der ausdrücklich gestartete TLS-Einstieg erlaubt lokale Registrierung/Verifikation mit synthetischen `example.test`-Adressen. Keine Seeds und kein Super Admin.

## Reproduzierbarer lokaler Einstieg

Voraussetzungen: vorhandenes Python 3.12, uv, Docker mit lokalem Daemon und OpenSSL. Keine fremden Installationsskripte. Aus dem Repository:

```bash
cd prototypes/backend
uv sync --locked --cache-dir /tmp/syllentra-uv
python scripts/local_db.py start
.venv/bin/python scripts/migrate.py
.venv/bin/python scripts/prepare_identity.py
PYTHONPATH=src .venv/bin/python -m scripts.identity_server
```

`local_db.py start` nur ausführen, wenn der eigene Containername/Port 55439 und `.local/database.json` noch nicht belegt sind. Vorhandenen eigenen laufenden Zustand weiterverwenden, nicht überschreiben. Das offizielle Image ist per Digest `postgres@sha256:858bb5e98eed02eb8cafbcdc007f9a65d1b613972028944a8ec2133ccaf80d27` fixiert, beobachtet PostgreSQL 17.11 / Debian Bookworm. Bei fehlendem Image zuerst diesen Digest bewusst mit `docker pull` beziehen. Kein Cloudhosting. Zufällige Datenbankpasswörter nur in ignorierter `.local/database.json` (0600, Verzeichnis 0700); getrennte Migrations-/APIrolle und Entwicklungs-/Testdatenbanken.

`prepare_identity.py` erzeugt ausschließlich lokale 0600-Dateien für Servergeheimnis und zweitägiges selbst signiertes Loopback-TLS. Bestehende Dateien werden nicht überschrieben; abgelaufene Testzertifikate bewusst prüfen/erneuern. Keine vertrauenswürdige öffentliche Zertifikatskette behauptet. `identity_server` bindet fest an Loopback:8443, erlaubt ausschließlich lokale bekannte Datenbankziele und startet ohne Konten. Option `--test` ausschließlich für Browserprüfungen gegen `syllentra_test`, nie parallel zu pytest.

In einem zweiten Terminal:

```bash
cd prototypes/frontend
npm ci --ignore-scripts --cache /tmp/syllentra-npm
npm run build
npm run preview:identity
```

Nur dieser explizite Startmodus verwendet Loopback:5174 mit HTTPS und festem geprüftem HTTPS-Proxy zum lokalen Backend. Im lokalen Identitätsbereich über Einstellungen synthetische Registrierung versuchen. Selbst signiertes Zertifikat nur für diesen eigenen lokalen Test prüfen; keinen allgemeinen Zertifikatsschutz abschalten. Gewöhnlicher Frontendstart und acht Demo-Lernräume bleiben getrennt, keine Demoobjekte werden zu Kontodaten.

OTP und Offline-Testcode werden nicht im Browser angezeigt und nicht von einer API zurückgegeben. Die berechtigten automatisierten Tests erhalten sie ausschließlich aus getrennten privaten Kanälen (`.local/mail/otp.jsonl` und `.local/offline/recovery.jsonl`), außerhalb des Webroots. Keine wirkliche E-Mail oder sichere reale Offlineübergabe bewiesen. Nach dem Test private Kanäle durch berechtigten lokalen Betreiber bereinigen; `LocalFileChannel.prune()` entfernt abgelaufene Einträge. Kein automatischer Bereinigungsscheduler, kein Logging von Nachrichteninhalten.

Prüfungen aus `prototypes/backend`:

```bash
.venv/bin/pytest -q
.venv/bin/mypy src scripts
.venv/bin/ruff check src tests scripts
.venv/bin/ruff format --check src tests scripts
.venv/bin/pip-audit --cache-dir /tmp/syllentra-pip-audit --format json
```

Zusätzlich aus `prototypes/frontend`: `npm run build`, `npm run lint`, `npm run format:check`, `npm test`, `npm run test:e2e`, **anschließend** `npm run test:identity` und `npm audit --json`. Vorhandenen Chromium nutzen (optional CHROMIUM_PATH); keine Browserdownloads nötig. E2E-Demo startet/stoppt Preview auf 4173, Identitäts-E2E seinen eigenen TLS-Backend-/Frontendprozess auf 8443/5174 gegen die separate Testdatenbank. Diese Ports müssen frei sein. Die Testkonfiguration akzeptiert das selbst signierte Browserzertifikat nur lokal; der Frontendproxy prüft weiterhin die konkrete Backend-CAbeilage. Auth-Traces/Videos/automatische Fehlerscreenshots aus, damit Testartefakte keine Anmeldedaten kopieren.

PostgreSQL liegt in ressourcenbegrenztem **tmpfs**. Stoppen/Entfernen des eigenen Containers verliert den Inhalt und macht die lokale Zustandsdatei ungültig. Keine Persistenz über Containerneustart, verschlüsselte Sicherung oder Restore nachgewiesen. Ohne zuverlässigen isolierten PostgreSQL Tests als blockiert melden; kein stiller SQLite-Ersatz. Nur eigene Prozesse beenden. Kein Deployment, externer Account oder Ausgabe autorisiert.

## Minimales Datenmodell und Migration

001 bewahrt Konto-/Geräte-/Session-/Notiz-/Flagmodell mit Eigentums-FK und Constraints. 002 ergänzt Sicherheitsrevision, MFA-Pflicht, Ablauf und nicht geheime Verwaltungs-UUIDs sowie Identitätschallenges, Recoveryverifikatoren, persistente Budgets und sichere Ereignismetadaten. Altes synthetisches Vertrauen wird widerrufen. 003 ergänzt persönliche Codegültigkeit und vorherige OTPverifikatoren. Historische Migrationen nicht nachträglich ändern; Migrationen transaktional, wiederholbar und gegen Prüfsummenabweichung gesperrt. Kein destruktives Downgrade.

Runtime hat kein DDL, keine Rollen-/Flagänderung und kein Notizeigentümer-/Gerätebesitzerwechselrecht. Benutzeranlage und Identitätszustände sind ausschließlich im festen serverseitigen Benutzerweg zugänglich. Notizlöschung bleibt bestätigter **Softdelete**, keine physische endgültige Löschung oder vollständiger Papierkorb. Datenexport, Retention aller Produktdaten, Nichtwiederbelebung und unabhängiger Restore bleiben offen.

## APIvertrag

[openapi.json](openapi.json) wird gegen die tatsächlich registrierten Routen geprüft, inklusive Cookie-/Bearernachweis. Swagger/ReDoc/OpenAPI-HTTPansichten sind ausgeschaltet. JSONwerte streng begrenzt, Extra-Felder verboten, Eingabe-/DBfehler nicht gespiegelt, Antworten no-store. Kein Roh-OTP/Recoverycode/Sessiontoken im Antwort-JSON; notwendige Cookies Secure/HttpOnly/SameSite Strict.

| Pfad / Methode | Tatsächlicher Zweck / Grenze |
|---|---|
| GET /health | Lokaler Experimentstatus; kein DBbereitschaftsbeweis |
| GET /auth/csrf | CSRFnonce und geschützter Cookie; kein Anmeldenachweis |
| POST /auth/register, /auth/verify, /auth/resend | Synthetische Benutzerregistrierung, gebundener Einmalcode, begrenzter Neuversand |
| POST /auth/login | Erst nach Passwort, aktivem verifiziertem Konto und berechtigtem Gerät; geforderte aber fehlende MFA sperrt |
| POST /auth/device/complete | Vorherige Freigabe vom berechtigten Gerät plus gebundener Antragsteller; danach neu anmelden |
| POST /auth/recover, /auth/recover/complete | Generische Anfrage; E-Mail-OTP **plus** persönlicher Einmalcode, Entzug alten Vertrauens; keine Dokumentenschlüsselrecovery |
| GET /session; POST /auth/logout | Eigene aktuelle Identität; aktuelle Session widerrufen und Cookie löschen |
| GET /devices, /devices/requests; POST /devices/requests/{id}/approve, /devices/{id}/revoke | Nur eigenes Gerät/Anfrage, aktuelle Rechte und Passwortbestätigung bei Geräteaktionen |
| GET /sessions; POST /sessions/{id}/revoke | Nur eigene nicht geheime Verwaltungsreferenzen; niemals Token/Hashausgabe |
| GET /capabilities; GET/PATCH/DELETE /notes/{id}; GET /notes | Bestehende aktuelle Rollen-/Flag-/Eigentumsprüfung und endliche Liste |
| GET /administration | Immer gesperrt; kein funktionsfähiger Adminhandler, keine öffentliche Erstbesetzung |

401 ungültige Identität, 403 Rechte-/Transport-/CSRFsperre, 404 unbekannt/fremd, 409 fehlende Notizlöschbestätigung, 413 Eingabe zu groß, 422 ungültiges Modell, 429 Budget, 503 fehlender Modus/Dienst. Identitätsfehlversuche liefern generische kontrollierte Antworten, damit nötige Zähler erhalten bleiben. Ohne explizite lokale Konfiguration bleiben Identitywege blockiert. Vollständige Sicherheitsgrenzen und Testfristen in der Architektur.

## Sitzung, Rechte und Bedrohungen

Opake zufällige 256-Bit-Sitzung, nur SHA-256 in DB; jede Anfrage kontrolliert aktuellen Konto-/Verifikations-/Geräte-/MFA-/Revisions-/Ablauf-/Widerrufszustand. Neues Passwort über Recovery entzieht alle alten Sessions/Geräte. Keine vom Browser frei wählbare Geräte-ID als Vertrauensnachweis. OTP-HMAC mit geheimem separatem Schlüssel und Zweck-/Challengebindung; falsche, alte, wiederverwendete und fremd gebundene Codes verweigert. Testfristen, Budgets und endliche Metadatenretention sind keine Produkt-SLO oder bestätigten V1-Zahlen.

Account- und sensible Übergangssperren verhindern konkurrierende Mehrfachverwendung. Eigene Notizen bleiben serverseitig gefiltert, Adminrolle kein privates Inhaltsrecht. Keine RLS-/Pentest-/ASVS- oder Gesamt-REL-Konformität behauptet. Bibliotheks-/IdPwahl, Hardware-/Gerätebindung, produktive Parallelität/Last, echte Offlinecodeübergabe, MFA, Schlüsselverwaltung und Wiederherstellung offen. Produktive sensitive Passwörter niemals in dieser Probe verwenden.

## Frontendanschluss und nächste Sperren

Eigener lokaler Identitätsbereich in DE/FR/EN, Hell/Dunkel/System; Registrierung, maskierte OTP-/Recoveryeingabe, Login, Geräteprüfung/-freigabe, eigene Sessions und Logout. Kein Secret in localStorage, kein Kontoexport ins Demo-Dataset. Gerätefreigabereferenzen sind bewusst nicht geheime Vergleichswerte. Standardstart zeigt Identität unverfügbar. Die bestehenden acht Lernbereiche bleiben Demo und erhalten ihre UItests.

MFA, Passkeys, lokale Inaktivitätssperre, echte Zustellung, sichere reale Wiederherstellung/Schlüsselrecovery und jeder Adminweg bleiben unvollständig bzw. gesperrt. Nächster Schritt: Eigentümerreview der lokalen Belege, dann getrennte Entscheidung und Testmission zu echten Faktor-/Recovery-/Bootstrapverfahren. Keine Cloud, Ausgabe oder öffentliche Nutzerfreigabe ableiten. Alle 14 TECH-O und FE-56 bleiben offen, Fachspezifikationen Zur Prüfung.
