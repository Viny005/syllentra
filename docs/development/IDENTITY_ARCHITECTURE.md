# Lokale Identitätsarchitektur — Mission 10

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung

## Umfang, Primärquellen und unveränderliche Grenzen

Mission 10 autorisiert ausschließlich lokale synthetische Identität und Tests, keine öffentliche Registrierung, tatsächliche Mailzustellung, Cloud, Ausgaben oder Produktfreigabe. [FE-37..39 und FE-59..63/70](../spec/S1-nachbarsysteme.md), [SEC-01..07/09/14/22](../spec/N2-querschnittskonzepte.md), [S3.5](../spec/S3-inbetriebnahme.md#s35-sicherer-erstbootstrap-und-administrative-kontinuität) und [14 TECH-O](../architecture/OFFENE_ENTSCHEIDUNGEN.md) bleiben maßgeblich. Keine fachliche Entscheidung geändert; FE-56 offen. [ADR-0009](../ARCHITECTURE_DECISIONS.md#adr-0009--lokale-identitätsprobe-aus-mission-10) dokumentiert das begrenzte Experiment.

Der bisherige Einstieg `syllentra_backend.local:app` bleibt gesperrt (503 bei Anmeldung). Nur der bewusst gestartete eigene TLS-Einstieg aktiviert vollständige lokale Benutzerwege. Die alte `synthetic_test_harness`-Anmeldeverzweigung wurde entfernt, nicht als Umschalter veröffentlicht. Neue Registrierung erlaubt ausschließlich synthetische ASCII-Adressen unter `example.test`; keine echten Empfänger oder Adminrollen. Anwendung, DB und Kanäle bleiben lokal. URLprüfung verweigert fremden Host, andere Datenbanknamen/-ports, Queryoptionen und Fragmente; kein unkontrollierter libpq-Hostoverride.

## Verantwortungen und Zustandsübergänge

`identity_routes.py` validiert Eingaben und übersetzt APIaufrufe, `identity.py` kapselt Registrierung, Verifikation, Authentisierung, Gerätefreigabe, Recovery, Budgets und Sicherheitsereignisse. `security.py` liefert Argon2id und Digest, `delivery.py` getrennte private Testkanäle. `api.py` prüft Transport, CSRF, aktuelle Sitzungen, Konto-/Objekt-/Funktionsrechte; Administration bleibt immer gesperrt. Kein neuer IdP, keine Queue oder externe Zustellung.

| Weg | Voraussetzungen | Wirkung / sichere Sperre |
|---|---|---|
| Registrierung | Zulässige synthetische Adresse, Passwort mindestens 12/höchstens 256 Zeichen, Budgets | Neues Benutzerkonto pending; kein Zugriff auf Anwendungsdaten. ASCIIadresse kontrolliert trimmen und kleinschreiben; öffentliche Produktionsnormalisierung bleibt offen. |
| Duplikat | Gleiche normalisierte Adresse | Kein zweites Konto, kein Überschreiben des Passworts. Antwort immer accepted mit Referenz. Pending und korrektes vorhandenes Passwort dürfen einen neuen gebundenen Verifikationslauf beginnen; falsches Passwort verändert den bestehenden Lauf nicht. |
| Adressverifikation | Richtiger zweckgebundener OTP und geheimer Preauth-Cookie derselben Anfrage | verified, erstes servergebundenes Gerät und persönlicher Offline-Testcode; **keine automatische Appsession**. Danach Passwortanmeldung erforderlich. |
| Bekanntes Gerät | Passwort, aktives verifiziertes Benutzerkonto, aktueller nicht widerrufener Gerätenachweis, keine unerfüllte MFA-Pflicht | Neue zufällige zeitbegrenzte Session; niemals eine vorgegebene Sessionkennung übernehmen. |
| Neues/abgelaufenes Gerät | Richtiges Passwort, aber kein aktueller Gerätenachweis | Nur gebundene Geräteanfrage, noch keine Session. Bestehendes berechtigtes Gerät prüft passende nicht geheime Referenz und bestätigt mit Passwort. Antragsteller muss danach seinen gebundenen Cookie vorweisen; erst dann neuer Gerätenachweis und anschließende Anmeldung. |
| Geräteverlust | Kein vorhandenes berechtigtes Gerät | Kein bloßes Vertrauen in Geräte-ID oder E-Mail allein; getrennter Recoveryweg nötig. |
| Recoveryanfrage | Aktives verifiziertes Benutzerkonto ohne unerfüllte MFA-Pflicht | Generische Antwort; lokaler Recovery-OTP bei Zulässigkeit, ansonsten gleichförmige fiktive Referenz. |
| Recoveryabschluss | Gebundener gültiger E-Mail-OTP **plus** gültiger persönlicher Offline-Einmalcode und neues Passwort | Alle alten Sessions/Geräte/Challenges entziehen, Sicherheitsrevision erhöhen, neuen lokalen Gerätenachweis und getrennten Offlinecode ausgeben; danach neu anmelden. Sicherheitsbenachrichtigung nur im lokalen Kanal. |
| MFA/Admin | Faktor-/Bootstrapverfahren fehlen | Keine Anmeldung oder Wiederherstellung, die eine geforderte MFA umgeht; Administration auch mit künstlichem Admin-Token unzugänglich. |

Das initiale Einrichten eines persönlichen Recoverycodes erfolgt hier ausschließlich über einen **getrennten privaten lokalen Offline-Testkanal**, nicht über die Mailbox oder die API. Beide Kanäle liegen für das Experiment auf demselben Rechner; dies beweist keine unabhängige sichere reale Übergabe. Deren Verfahren bleibt vor Produktnutzung zu entscheiden. Kontorecovery gibt keine persönlichen Dokumentenschlüssel zurück, entschlüsselt keine privaten Dokumente und stellt kein Admin-Schlüsselrecht her.

## OTP, Budgets und Beweisspeicher

Achtstelliger OTP aus `secrets.randbelow`, HMAC-SHA-256-Verifikator mit separat lokal geschütztem 256-Bit-Servergeheimnis. Zweck und zufällige Challenge-UUID sind Bestandteil des Verifikators; Konto, Sicherheitsrevision und zufälliger Preauth-Cookie binden den Vorgang. Ein reiner DBabzug erlaubt ohne Servergeheimnis kein einfaches vollständiges Offline-Durchprobieren des kleinen Codebereichs. Das ersetzt kein produktives Secretmanagement oder Schutz gegen vollständige Prozesskompromittierung.

Experimentparameter: OTP/Preauth/Geräteanfrage fünf Minuten, höchstens fünf Prüfversuche, zwei zusätzliche Zustellungen im Mindestabstand von 60 Sekunden. Neue Codes unterscheiden sich von allen bisherigen Codes derselben Challenge; ursprüngliche Ablaufzeit und Versuchszahl bleiben erhalten. Erfolgreiche Verwendung verbraucht den Vorgang unter Konten-/Zeilensperre; parallele OTPverwendung nur einmal erfolgreich. Fehler werden als normale Fehlerantwort zurückgegeben, damit Versuchszähler **committet** und nicht versehentlich durch HTTPexceptions zurückgerollt werden.

Persistente DBbudgets begrenzen Registrierung/Login pro normalisierter Adresse auf zehn/Minute, Recovery auf drei/Minute, zusätzliche Passwortbestätigungen auf zehn/Minute; ein Netzwerkbudget begrenzt Auth-POSTs auf 100/Minute. Schlüssel werden mit dem Servergeheimnis pseudonymisiert; keine rohe IP/Mailadresse in Budget-/Auditdaten. Das lokale Proxy-Netzwerkbudget ist kein verteilter Produktionsschutz und unterscheidet keine realen Proxy-Client-IP-Adressen. Zahlen sind ausschließlich begrenzte Versuchsparameter, keine genehmigten N1-/V1-Grenzwerte. Gleiche Antwortform/Status gegen Enumeration geprüft; vollständige Timing-/Lastresistenz nicht nachgewiesen.

Sicherheitsereignisse enthalten nur zufällige ID, eigene Konto-ID sofern bekannt, kontrollierten Ereignistyp und Zeit. Keine Passwörter, OTP, Recoverycodes, Tokens, Mailadressen oder privaten Inhalte im Audit. Ereignisse älter als sieben Tage werden bei Auditpflege bereinigt; verbrauchte/abgelaufene Challenges bei neuer Challengepflege nach einer Stunde, abgelaufene Budgetfenster bei Zugriff. Kein unabhängiger Produktionsscheduler behauptet. Unbehandelte Backendfehler protokollieren ausschließlich den Ausnahme-Klassennamen, keinen Fehlertext oder Stacktrace.

Private Testmailboxen benötigen 0700-Verzeichnisse und eigene 0600-Dateien, verweigern finale Symlinks und überbreite Dateirechte. OTPzustellungen haben zehn Minuten lokale Kanalretention, Offline-Testcodes sieben Tage; Bereinigung beim Schreiben oder explizitem `prune()`. **Ohne weitere Aktion kein autonomer Löschlauf.** Diese Mailboxen enthalten bewusst zugestellte künstliche Geheimnisse, sind keine Sicherheitslogs und niemals über HTTP abrufbar. Nach abgeschlossenem Versuch durch berechtigten lokalen Betreiber bereinigen; keine garantierte physische Löschung aus tmpfs/RAM/Filesystemkopien behaupten.

## Datenmodell, Rechte und Transaktionen

[Migrationen](../../prototypes/backend/migrations/002_local_identity.sql) erweitern das bestehende Schema additiv; [003](../../prototypes/backend/migrations/003_proof_lifetimes.sql) ergänzt Lebensdauer und frühere OTPverifikatoren. Historische Migration 001 bleibt unverändert. Migration 002 entzieht altes synthetisches Geräte-/Sitzungsvertrauen, statt es als echte Verifikation zu übernehmen.

| Daten | Ergänzung / Integrität |
|---|---|
| accounts | Sicherheitsrevision und MFA-Pflicht; Rollenprüfung serverseitig. Runtime darf keine Adminrolle einfügen oder Kontorolle ändern. |
| devices | Ablauf, Revision und servergenerierter geheimer Nachweis; Konto darf per Runtime nicht umgehängt werden. |
| sessions | Zusätzliche nicht geheime UUID für Eigenverwaltung, Ablauf, Widerruf, Revision; Rohsessiontoken nie in DB. |
| identity_challenges | Konto, Zweck, Bindinghash, OTP-HMAC, vorherige HMACs, Fristen, Versuche/Zustellungen, Verbrauch und Freigabegerät; FK verhindert fremdes Freigabegerät. |
| recovery_codes | Kontobindung, HMAC, Verbrauch und endliche sieben Tage Testgültigkeit; Codewechsel invalidiert früheren Code. |
| identity_budgets | Pseudonymisierter Operationsschlüssel, Fenster und Zähler. |
| security_events | Begrenzte zweckgebundene Metadaten ohne Geheimniswerte. |

Die Kontenzeilensperre wird bei jeder privaten Anfrage unter Zeilensperre gegen Rollen-/Kontozustandsänderungen gehalten; kritische Identitätsübergänge sperren zuerst Konto, dann Challenge. Das serialisiert lokale Operationen desselben Kontos, ohne globale Mehrnutzerlast zu beweisen. Auch der Freigabegerätenachweis wird beim Abschluss erneut geprüft. Serverseitige Notizfilter und Rollen-/Featurechecks bleiben erhalten; kein PostgreSQL-RLS oder allgemeiner Admin-Inhaltszugriff eingeführt. Migrationsrolle ist getrennt; Runtime erhält nur erforderliche zusätzliche Spalten-/Tabellenrechte, kein DDL und keine Flagschreibrechte. Produktionsrollen und atomic veröffentlichte Konfiguration bleiben weiter zu untersuchen.

## Browser, TLS und CSRF

Expliziter lokaler Einstieg unter HTTPS, kurzlebiges selbst signiertes Zertifikat für Loopback. Frontendproxy verbindet ebenfalls per HTTPS und prüft das Backend gegen die konkrete lokale Zertifikatsbeilage (`Agent({ca: cert})`, kein `secure: false`). Playwright vertraut dem selbst signierten Browserziel ausschließlich im Test mit `ignoreHTTPSErrors`; kein Nachweis öffentlicher Zertifikats-/HSTS-/PKIreife. Backend lauscht ausschließlich auf Loopback, kein unverschlüsselter Identitätsmodus.

Session-, Geräte-, Preauth- und CSRF-Cookies: `Secure`, `HttpOnly`, `SameSite=Strict`, `__Host-`-Präfix, Path `/`, kein Domainattribut. Rohsessiontoken nur im geschützten Cookie, nicht im JSON oder localStorage. Vor jeder schreibenden Operation exakten erlaubten Origin, Fetch-Metadaten und passenden CSRF-Header/Cookie prüfen; Cross-Site-Anfragen auch lesend verweigern. Keine CORSwildcard. Der CSRFnonce im JSON ist **kein Anmeldetoken**. Bearer bleibt für kontrollierte interne APItests möglich; widersprüchliche Cookie-/Beareridentitäten werden verweigert. [OpenAPI](../../prototypes/backend/openapi.json) führt beide Nachweisarten.

React erhält einen eigenen Identitätsbereich mit Registrierung, maskierter OTPeingabe, Anmeldung, Gerätefreigabe, Recovery, Abmeldung und eigener Session-/Geräteverwaltung. DE/FR/EN und Themes erhalten. Kennungen zur passenden Gerätefreigabe sind ausdrücklich **nicht geheime Anfragereferenzen**, keine OTPs. Persönliche Geheimnisse werden weder vorgelesen noch als Text/Debugausgabe angezeigt; Auth-Test-Traces, Videos und automatische Fehlerscreenshots sind aus. Die acht Demo-Lernräume bleiben unabhängige Fixtures; keine Demoobjekte als Kontodaten übernehmen. Bei 401 wird die lokale Kontosicht verworfen, Logout löscht den Cookie; Sprache/Theme bleiben die einzigen persistenten JavaScript-Präferenzen. Außerhalb des expliziten lokalen TLS-Modus bleibt der Identitätsbereich unverfügbar.

## MFAabwägung und ausstehende Produktentscheidungen

| Option | Nutzen | Noch notwendiger Nachweis / heutiger Stand |
|---|---|---|
| TOTP | Unabhängiger Besitzfaktor ohne SMSanbieter | Sichere Secretbindung/-ablage, Enrollmentbestätigung, Replay-/Zeitfenster, Recovery und Schlüsselverwaltung; nicht implementiert/aktiviert. |
| Passkeys/WebAuthn | Originbindung und mögliche Hardware-/OSintegration | Geprüfte RP-/Geräte-/Credential-/Recoverystrategie und reale Plattformtests; keine Rohbiometrie. Nicht implementiert. |
| Persönliche Recoverycodes | Zusätzlicher persönlicher Besitznachweis im gesonderten Recoveryweg | Lokaler HMAC-/Einmal-/Ablauf-/Rotationsbeleg vorhanden; sichere reale Offlineausgabe und Verlustverfahren offen. Kein Ersatz für reguläre Admin-MFA. |
| E-Mail-Verifikations-OTP | Nachweis des kontrollierten Adresskanals | Kein unabhängiger zweiter Faktor zur selben E-Mail-Recovery und keine Admin-MFA; keine reale Zustellbarkeit getestet. |

TECH-O-05/06 bleiben offen; die technische Auswahl und echte Adminfaktor-/Recoverybindung fehlen. Sobald `mfa_required` gesetzt ist, verweigert der heutige Dienst Anmeldung, bestehende Sessions und Recovery, statt einen Faktor vorzutäuschen. Kein Super Admin, keine Standardidentität, keine öffentliche Selbstbeförderung. Einmaligkeits-/Konkurrenz-/Identitäts-/MFA-/Auditverträge des künftigen Bootstrap bleiben S3.5; keine ausführbare Erstbesetzung geliefert.

Geräte- und Sitzungstokens bleiben kopierbare Besitznachweise, keine Hardwareattestation; ein gestohlener gültiger Sessiontoken kann bis Entzug/Ablauf missbraucht werden. Token-/Browser-/Gerätekompromittierung ist vor Produktion weiter zu prüfen.

Weitere Grenzen: offene Produktionsnormalisierung, Echtzustellung, Daten-/Secretverschlüsselung im Ruhezustand, sichere reale Offlinecodeübergabe, lokale Inaktivitätssperre/Passkeys/OSbiometrie, Schlüsselrecovery, unabhängiger Restore, vollständige Löschung, verteilte Raten-/Last-/Timing-/Penetrationsnachweise und rechtliche Prüfung. Passwortwechsel ist hier ausschließlich Teil der geprüften Recovery, kein zusätzlicher ungesicherter Resetweg. [Validierungsbericht](IDENTITY_PROTOTYPE_REVIEW.md) trennt tatsächliche Resultate und verbleibende Beobachtungen.
