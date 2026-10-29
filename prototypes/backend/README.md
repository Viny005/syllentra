# Lokale experimentelle Backendgrundlage

**Version:** 0.5 · **Stand:** 23.10.2026 · **Status:** Experimentell / Zur Prüfung

Mission 10 erweitert die lokale Sicherheitsprobe aus Mission 9 um tatsächlich testbare synthetische Identität; Mission 12 isoliert PostgreSQL-Testläufe pro Prozess; Mission 13 behebt R2 (Netzwerkbudget-Isolierung), R3 (Sortierung, effektiver Status und `offset`/`limit`-Paginierung bei `GET /sessions` und `GET /devices`), R5 (Aufrufer-isolierte Adressbudgets und Erhalt laufender Recovery-Challenges) sowie R12 (vollständige Sitzungs-/Geräteprüfung bei `approve_device`); Mission 14 setzt die vom Projektinhaber freigegebenen Entscheidungen R1 (persönlicher Offline-Einmal-Recoverycode ohne automatischen 7-Tage-Ablauf, gültig bis Verbrauch, explizitem Widerruf, kontrollierter Rotation oder Sicherheitsinvalidierung bei unabhängiger 7-Tage-Gerätefrist) und R4 (kontrollierter Reset unverifizierter `pending`-Konten nach mindestens 24 Stunden ab `pending_since` mit neuem Argon2id-Passwort, neuem E-Mail-OTP, `security_epoch`-Erhöhung, Invalidierung alter Challenges und Anomalie-Sperre bei unerwarteten Daten) um. Keine öffentliche Registrierung, produktive Authentifizierung, echte Mailzustellung oder endgültige Stackwahl. [Identitätsarchitektur](../../docs/development/IDENTITY_ARCHITECTURE.md), [aktueller Prüfbericht](../../docs/development/IDENTITY_PROTOTYPE_REVIEW.md), [historische Mission 9](../../docs/development/BACKEND_PROTOTYPE_REVIEW.md), [Lizenzen](LICENSES.md).

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

`prepare_identity.py` erzeugt ausschließlich lokale 0600-Dateien für Servergeheimnis und zweitägiges selbst signiertes Loopback-TLS. Bestehende Dateien werden nicht überschrieben; abgelaufene Testzertifikate bewusst prüfen/erneuern. Keine vertrauenswürdige öffentliche Zertifikatskette behauptet. `identity_server` bindet fest an Loopback:8443, erlaubt ausschließlich lokale bekannte Datenbankziele und startet ohne Konten. Option `--test` ausschließlich für Browserprüfungen gegen `syllentra_test`. Backend-Pytestläufe erzeugen seit Mission 12 über [scripts/test_db.py](scripts/test_db.py) je Prozess eine eigene Datenbank `syllentra_t_<12 Hex>` (`TEMPLATE template0`) mit Eigentumsvermerk (`COMMENT ON DATABASE`) und berühren `syllentra_test` oder `syllentra_prototype` niemals. Zerstörende Bereinigungen (`wipe`/`drop_run_database`) prüfen vor jedem `DELETE`/`DROP` Namen und Eigentumskommentar. Verwaiste Laufdatenbanken lassen sich kontrolliert mit `.venv/bin/python -m scripts.test_db sweep <Stunden>` auflisten und nur mit `--apply` entfernen.

### Betriebsregeln für Testdatenbank-Bereinigung und Betriebsgrenzen

Für die Verwaltung und Bereinigung von Testdatenbanken ([scripts/test_db.py](scripts/test_db.py)) gelten verbindliche Betriebsregeln:

* **Kein automatischer oder unbeaufsichtigter Sweep:** Ein destruktiver Sweep darf niemals automatisch während laufender Testläufe oder über unbeaufsichtigte Hintergrundjobs (Cron, Scheduler) ausgeführt werden.
* **Advisory-Locks und Prozesslebenszyklus:** Ein verlorener PostgreSQL-Advisory-Lock beweist nicht zwingend, dass der ursprüngliche Testprozess beendet wurde (z. B. bei Verbindungsabbruch oder Timeout). Ebenso ist ein reines Mindestalter allein kein hinreichender Nachweis für das Ende des Besitzerprozesses.
* **Manuelle Bestandskontrolle:** Verwaiste Testdatenbanken dürfen ausschließlich nach Überprüfung der aktiven Prozesse und Verbindungen manuell bereinigt werden. Der Befehl `sweep <Stunden>` (ohne `--apply`) dient der sicheren, rein lesenden Bestandsaufnahme.
* **Destruktive Bereinigung:** `sweep <Stunden> --apply` und `reclaim_orphaned_database()` sind destruktive Operationen und ausschließlich für ausdrücklich autorisierte, isolierte Testumgebungen bestimmt. Sie dürfen niemals gegen gemeinsame (`syllentra_test`, `syllentra_prototype`) oder gar produktive Datenbanken gerichtet werden.
* **Schwellenwert 0:** Der Altersschwellenwert `0` (`sweep 0 --apply`) ist ausschließlich für gezielte automatisierte Testfälle in einem dedizierten Wegwerf-Container zugelassen.
* **Kein erzwungener Verbindungsabbruch:** Es wird grundsätzlich kein `DROP DATABASE ... WITH (FORCE)` eingesetzt; laufende Verbindungen blockieren die Löschung, um versehentliche Datenzerstörung bei noch aktiven Prozessen zu verhindern.
* **Grenzen des Prototyps:** Diese Regeln sind als betriebliche Schutzgrenzen für die lokale Testisolation des experimentellen Prototyps zu verstehen, nicht als produktionsreife Sicherheitsgarantie.

Der dokumentierte Validierungsnachweis der PostgreSQL-Testisolation (116/116 Tests bestanden) ist in [docs/development/PR1_PREMERGE_TEST_EVIDENCE.md](../../docs/development/PR1_PREMERGE_TEST_EVIDENCE.md) hinterlegt.

**Hinweis für Windows / WSL / Linux-Container:** `LocalFileChannel` ([delivery.py](src/syllentra_backend/delivery.py)) und `identity_server.py` erzwingen POSIX-Dateirechte (`0600`/`0700`, `os.getuid()`, `os.O_NOFOLLOW`). Auf Windows-Hosts ohne native Linux-WSL-Distribution sind Backend-Tests und Linter deshalb in einem nativen Linux-Dateisystem (z. B. WSL2 oder im gepinnten Container `ghcr.io/astral-sh/uv:python3.12-bookworm-slim` im selben Loopback-Netz wie `syllentra-mission9-local`) auszuführen, da Windows-Bind-Mounts in Docker Desktop standardmäßig Modus `0777` zeigen.

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

001 bewahrt Konto-/Geräte-/Session-/Notiz-/Flagmodell mit Eigentums-FK und Constraints. 002 ergänzt Sicherheitsrevision, MFA-Pflicht, Ablauf und nicht geheime Verwaltungs-UUIDs sowie Identitätschallenges, Recoveryverifikatoren, persistente Budgets und sichere Ereignismetadaten. Altes synthetisches Vertrauen wird widerrufen. 003 ergänzt persönliche Codegültigkeit und vorherige OTPverifikatoren. 004 ([004_r1_r4_lifetimes.sql](migrations/004_r1_r4_lifetimes.sql)) ergänzt `revoked` und `issued_at` auf `recovery_codes`, entkoppelt neue persönliche Recoverycodes vom automatischen 7-Tage-Ablauf (`expires_at = NULL`, R1; bereits abgelaufene Altcodes werden widerrufen statt still reaktiviert) und führt `accounts.pending_since` für die 24-Stunden-Frist unverifizierter `pending`-Konten (R4) ein. Historische Migrationen nicht nachträglich ändern; Migrationen transaktional, wiederholbar und gegen Prüfsummenabweichung gesperrt. Kein destruktives Downgrade.

Runtime hat kein DDL, keine Rollen-/Flagänderung und kein Notizeigentümer-/Gerätebesitzerwechselrecht. Benutzeranlage und Identitätszustände sind ausschließlich im festen serverseitigen Benutzerweg zugänglich. Notizlöschung bleibt bestätigter **Softdelete**, keine physische endgültige Löschung oder vollständiger Papierkorb. Datenexport, Retention aller Produktdaten, Nichtwiederbelebung und unabhängiger Restore bleiben offen.

## APIvertrag

[openapi.json](openapi.json) wird gegen die tatsächlich registrierten Routen geprüft, inklusive Cookie-/Bearernachweis. Swagger/ReDoc/OpenAPI-HTTPansichten sind ausgeschaltet. JSONwerte streng begrenzt, Extra-Felder verboten, Eingabe-/DBfehler nicht gespiegelt, Antworten no-store. Kein Roh-OTP/Recoverycode/Sessiontoken im Antwort-JSON; notwendige Cookies Secure/HttpOnly/SameSite Strict.

| Pfad / Methode | Tatsächlicher Zweck / Grenze |
|---|---|
| GET /health | Lokaler Experimentstatus; kein DBbereitschaftsbeweis |
| GET /auth/csrf | CSRFnonce und geschützter Cookie; kein Anmeldenachweis |
| POST /auth/register, /auth/verify, /auth/resend | Synthetische Benutzerregistrierung, gebundener Einmalcode, begrenzter Neuversand; unverifizierte `pending`-Konten ab 24h (`pending_since`) sicher mit neuem Passwort + neuem OTP rücksetzbar (R4), verifizierte Konten niemals |
| POST /auth/login | Erst nach Passwort, aktivem verifiziertem Konto und berechtigtem Gerät; geforderte aber fehlende MFA sperrt |
| POST /auth/device/complete | Vorherige Freigabe vom berechtigten Gerät plus gebundener Antragsteller; danach neu anmelden |
| POST /auth/recover, /auth/recover/complete | Generische Anfrage; E-Mail-OTP **plus** persönlicher Einmalcode (gültig bis Verbrauch/Widerruf/Rotation, R1), Entzug alten Vertrauens; keine Dokumentenschlüsselrecovery |
| GET /session; POST /auth/logout | Eigene aktuelle Identität; aktuelle Session widerrufen und Cookie löschen |
| GET /devices, /devices/requests; POST /devices/requests/{id}/approve, /devices/{id}/revoke | Nur eigenes Gerät/Anfrage, effektives `authorized` (`authorized AND expires_at > clock()`), aktives Gerät zuerst, Paginierung (`offset`/`limit`), Sitzungs-/Gerätesperre und Passwortbestätigung bei Geräteaktionen |
| GET /sessions; POST /sessions/{id}/revoke | Nur eigene nicht geheime Verwaltungsreferenzen, effektives `revoked` (`revoked OR expires_at <= clock()`), aktive Sitzungen zuerst, Paginierung (`offset`/`limit`); niemals Token/Hashausgabe |
| GET /capabilities; GET/PATCH/DELETE /notes/{id}; GET /notes | Bestehende aktuelle Rollen-/Flag-/Eigentumsprüfung und endliche Liste |
| GET /administration | Immer gesperrt; kein funktionsfähiger Adminhandler, keine öffentliche Erstbesetzung |

401 ungültige Identität, 403 Rechte-/Transport-/CSRFsperre, 404 unbekannt/fremd, 409 fehlende Notizlöschbestätigung, 413 Eingabe zu groß, 422 ungültiges Modell, 429 Budget, 503 fehlender Modus/Dienst. Identitätsfehlversuche liefern generische kontrollierte Antworten, damit nötige Zähler erhalten bleiben. Ohne explizite lokale Konfiguration bleiben Identitywege blockiert. Vollständige Sicherheitsgrenzen und Testfristen in der Architektur.

## Sitzung, Rechte und Bedrohungen

Opake zufällige 256-Bit-Sitzung, nur SHA-256 in DB; jede Anfrage kontrolliert aktuellen Konto-/Verifikations-/Geräte-/MFA-/Revisions-/Ablauf-/Widerrufszustand. Neues Passwort über Recovery entzieht alle alten Sessions/Geräte. Keine vom Browser frei wählbare Geräte-ID als Vertrauensnachweis. OTP-HMAC mit geheimem separatem Schlüssel und Zweck-/Challengebindung; falsche, alte, wiederverwendete und fremd gebundene Codes verweigert. Testfristen, Budgets und endliche Metadatenretention sind keine Produkt-SLO oder bestätigten V1-Zahlen.

Account- und sensible Übergangssperren verhindern konkurrierende Mehrfachverwendung. Eigene Notizen bleiben serverseitig gefiltert, Adminrolle kein privates Inhaltsrecht. Keine RLS-/Pentest-/ASVS- oder Gesamt-REL-Konformität behauptet. Bibliotheks-/IdPwahl, Hardware-/Gerätebindung, produktive Parallelität/Last, echte Offlinecodeübergabe, MFA, Schlüsselverwaltung und Wiederherstellung offen. Produktive sensitive Passwörter niemals in dieser Probe verwenden.

## Frontendanschluss und nächste Sperren

Eigener lokaler Identitätsbereich in DE/FR/EN, Hell/Dunkel/System; Registrierung, maskierte OTP-/Recoveryeingabe, Login, Geräteprüfung/-freigabe, eigene Sessions und Logout. Kein Secret in localStorage, kein Kontoexport ins Demo-Dataset. Gerätefreigabereferenzen sind bewusst nicht geheime Vergleichswerte. Standardstart zeigt Identität unverfügbar. Die bestehenden acht Lernbereiche bleiben Demo und erhalten ihre UItests.

MFA, Passkeys, lokale Inaktivitätssperre, echte Zustellung, sichere reale Wiederherstellung/Schlüsselrecovery und jeder Adminweg bleiben unvollständig bzw. gesperrt. Nächster Schritt: Eigentümerreview der lokalen Belege, dann getrennte Entscheidung und Testmission zu echten Faktor-/Recovery-/Bootstrapverfahren. Keine Cloud, Ausgabe oder öffentliche Nutzerfreigabe ableiten. Die 14 Architekturprinzipien TECH-O-01 bis TECH-O-14 sowie die Multi-Provider-Entscheidung sind auf Prinzipienebene (A) bestätigt; technische Unterentscheidungen (B) und Benchmarks/Nachweise (C) bleiben offen. Die Anforderung FE-56 ist für V1 fachlich entschieden (kein Auslesen, Synchronisieren oder Überwachen von E-Mail-Postfächern in V1); Fachspezifikationen Zur Prüfung.
