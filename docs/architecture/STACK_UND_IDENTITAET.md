# Frontend, Backend und Identität

**Version:** 0.3 · **Stand:** 23.10.2026 · **Status:** Architekturprinzipien (A) in Mission 21 bestätigt; technische Unterentscheidungen (B) und Nachweise (C) offen

## 1. Vergleich der Laufzeit-/Oberflächenvarianten

| Variante | Stärken für Syllentra | Mehraufwand / Grenze | Bewertung |
|---|---|---|---|
| Next.js / React, Node/TypeScript als Hauptbackend | Gemeinsame Sprache für UI/API, breites Ökosystem, serverseitiges Rendering verfügbar | Auth-/Cachinggrenzen zwischen Server/Client, Schutz privater Seiten/Antworten, PWA zusätzlich; Python-KI führt oft zweite Backendlaufzeit ein. SSR/SEO ist für private Lernräume kein bewiesener Bedarf. | Solider Kandidat bei TS-Kompetenz, nicht notwendiger Standard |
| React + Vite als statische PWA, FastAPI/Python als modularer Kern | Statischer Client, ein fachliches Backend in derselben Sprache wie viele KI-/Extraktionswerkzeuge; kein Node-Produktionsprozess nötig | Zwei Entwicklungssprachen bleiben; PWA-Serviceworker, Sync und Authflüsse bewusst entwickeln/testen; Python-CPUarbeit nicht im Request-Eventloop | **Empfohlene Untersuchungsbasis**, keine Stackfreigabe |
| Vite + Node/TypeScript, Python als begrenzter Worker | Klare TS-Fachlogik mit Python-Werkzeugen | Drei Artefakt-/Prozessrollen und sprachübergreifende Schemata, mehr Fehlersuche; doppelte Rechteprüfung nicht auseinanderlaufen lassen | Erst bei Team-/Bibliotheksvorteil |
| Django + React/Vite oder serverbasierte UI | Reifer Auth-/ORM-/Admin-/Migrationsbaukasten | Django-Admin ist nicht automatisch die geforderte getrennte, begrenzte Produktadministration; asynchrone KI/Jobs/PWA benötigen weiterhin eigene Verträge | Sinnvolle Python-Alternative, Lizenz/aktuelle Fassung hier noch nicht separat verifiziert |

React/Vite und Next.js sind keine automatisch installierbare/offlinefähige App. Manifest, Serviceworker-/Updateverhalten, Berechtigungen, Konflikte, sensible lokale Daten und veraltete Clients nach NFR-02/03 prüfen. FR/DE/EN und Text-/Audioausgabe getrennt halten. WCAG 2.2 AA bleibt zu bestätigendes Ziel. Next-/Vite-/FastAPI-Lizenzquellen wurden gelesen; [Quellen](QUELLEN.md) nennen aktuelle beobachtete Releaseweiterleitungen statt ungetesteter Versionspins.

## 2. Modulare Fachlogik und Hintergrundarbeit

API/Anwendungsfälle nach Konto/Profil, Lernorganisation, Gesprächen, Dokumenten, Pädagogik, Kalender, Integration, Administration und Datenkontrolle kapseln. Klare interne Schnittstellen statt sofortiger Microservices. Workerprozess für Parser/Audio/Inferenz getrennt begrenzen; derselbe Release und dieselben fachlichen Regeln können verwendet werden. Ein isolierter Worker ist eine Ausführungs-/Vertrauensgrenze, nicht automatisch eine verteilte Geschäftsdatenarchitektur.

Uploadprüfung, Archive/OCR/FFmpeg und Modellserver nicht öffentlich erreichbar. Begrenzte Jobs mit Konto/Zweck/Quellrevision/Schutz, aktuelle Rechteprüfung, faire Queue, Abbruch, Idempotenz und endliche temporäre Dateien. REST/Events sind mögliche Schnittstellen, kein hier festgelegtes APIprotokoll. Server validiert alle Client-/Toolparameter und nicht vertrauenswürdige Modellantworten.

## 3. Open-Source-Authentifizierung

| Kandidat | Lizenz-/Betriebsbefund | Funktionale Passung und offene Lücke |
|---|---|---|
| Keycloak selbst gehostet | Apache-2.0 gelesen, eigener Java-Prozess/Updates/DBanbindung; zusätzliches RAM-/Betriebsbudget nötig | Reifer IdP-Kandidat für MFA/WebAuthn/Sessions/Recovery. **Verify-email-Link ist kein Nachweis des explizit geforderten E-Mail-OTP-Verfahrens.** Konkreten Flow, neue Geräte und Recovery negativ testen; keine ungeprüfte OTP-Erweiterung installieren. |
| authentik Core | Offizielle Lizenz enthält MIT-Kern, gesonderte Enterprise- und Drittkomponentenbedingungen | Flexibel, aber zusätzliche Betriebs-/Komponentenanforderungen und editionsabhängige Funktionen prüfen; nicht pauschal alles MIT nennen. OTP-/Recoverypassung noch unbewiesen. |
| Auth.js / Bibliotheksansatz | **ISC-Lizenz** im aktuellen offiziellen Quelltext gelesen; keine zusätzliche IdPplattform nötig | Session-/Providerbibliothek ersetzt keine vollständige Registrierung, E-Mail-OTP, Geräteverwaltung, Rollen-MFA, Recovery und Audit. Eigenentwicklungs-/Sicherheitslast beträchtlich; im Pythonbackend zusätzlich passendes Verfahren nötig. |

**Empfehlung zur Entscheidung:** Zuerst Keycloak als begrenzten selbst gehosteten Kandidaten gegen FE-60/SEC-01..07 und tatsächliches RAM prüfen, parallel bibliotheksgestützten schlanken Ansatz vergleichen. Keinen fertigen Fit behaupten. Bestehende Consumer-Abos sind weder OIDC-Integration noch API-/Datenrecht.

## 4. Autorisierung und Adminoberfläche

Authentisierung liefert Identität, nicht Produktberechtigung. Server prüft Konto/Sitzung/Gerät, Rolle, Objekt, Flag, Scope, Zweck und ggf. Support-/Analysefreigabe pro Operation. Keine Rechte aus prompt, Tokeninhalt ohne Aktualitätsprüfung, Clientmenü oder IdP-Gruppenname ungeprüft übernehmen. Änderungen/Entzüge vor Jobwirkung erneut prüfen.

Adminoberfläche als eigener geschützter Bedienbereich mit getrenntem Adminaccount/-kontext; eigener Origin ist eine mögliche technische Grenze, kein hier beschlossener Domainkauf. Genau ein Super Admin; IdP-/Cloudadmin ist nicht automatisch App-Super-Admin oder privater Inhaltsleser. Delegierte dürfen keine Selbstbeförderung oder andere Adminverwaltung. Auth-/IdP-/Backendbetrieb kann technisch Klartextverarbeitung sehen; sensible geräteseitige Schlüssel und explizite temporäre Serveranalyse bleiben ehrlich getrennt.

Sicherer Bootstrap, administrative MFA-Recovery und Schlüsselrecovery bleiben [S3.5](../spec/S3-inbetriebnahme.md#s35-sicherer-erstbootstrap-und-administrative-kontinuität) und O-S3-04/05/11. Keine sichere Lösung aus dem Produktnamen ableiten. Vor Architekturfreigabe Rollen-/Session-/OTP-/Isolationsmatrix inklusive A/B und Verlustfall vorlegen; vor Produktstart tatsächliche Tests.

## 5. Präzisierung aus neuer offizieller Quelle — Mission 6

Neu gelesene Keycloak-Anleitung bestätigt Linkverifikation; Generator-OTP ist kein E-Mail-Codeflow. Die authentik Email-Stage kann bei Recovery standardmäßig einen inaktiven Benutzer aktivieren. Appkontostatus, Konfiguration und Anti-Enumeration deshalb gezielt gegen Pause/Adminsperre/Löschung prüfen. Quellen und konkrete Beleggrenzen in [Machbarkeit Abschnitt 5](MACHBARKEITSPRUEFUNG.md#5-identität-fähigkeiten-und-konkrete-integrationslücken) und [Quellen M6](QUELLEN.md#6-nachrecherche-mission-6); T06/T09 im [Testplan](BENCHMARKPLAN.md) sind nur geplant. Keine endgültige Authauswahl.


## 6. Vom Projektinhaber bestätigte Architekturprinzipien aus Mission 21 (TECH-O-01, TECH-O-03, TECH-O-05, TECH-O-06)

Am 23.10.2026 hat der Projektinhaber die folgenden Architekturprinzipien bestätigt ([ADR-0010](../ARCHITECTURE_DECISIONS.md#adr-0010--evolutionärer-modularer-monolith-und-isolierte-worker-tech-o-01), [ADR-0012](../ARCHITECTURE_DECISIONS.md#adr-0012--anwendungsstack-react--vite--typescript-und-fastapi--python-tech-o-03), [ADR-0014](../ARCHITECTURE_DECISIONS.md#adr-0014--austauschbare-identitätsarchitektur-und-autoritative-fastapi-autorisierung-tech-o-05), [ADR-0015](../ARCHITECTURE_DECISIONS.md#adr-0015--schutzgrenzen-starke-mfa-und-trennung-des-super-admin-tech-o-06)); die obigen Abschnitte 1–5 bleiben als historischer Vergleich aus Mission 5/6 erhalten:

| Bezug | A. Bestätigtes Architekturprinzip | B. Offene technische Unterentscheidungen | C. Ausstehende Nachweise |
|---|---|---|---|
| **TECH-O-01 — Architekturform** | Evolutionärer modularer Monolith mit klarer Aufgabentrennung und isolierten Workern für schwere Verarbeitung; keine flächendeckenden Microservices ab V1. | Prozess-/Supervisor-Zuschnitt und Ressourcenlimits (CPU/RAM/Timeouts) je Workerklasse. | Koexistenz- und Isolationsmessungen (`T01`, `T09`), Nachweis der Fehler-/Abbruchkapselung (`NFR-25`). |
| **TECH-O-03 — Technischer Stack** | Frontend: **React + Vite + TypeScript**; Backend: **FastAPI + Python**; Erhalt des PWA-Ziels (`FE-55`) und der bestehenden Barrierefreiheitsanforderungen (`NFR-08/19/20`, `REL-A16`), wobei **WCAG 2.2 AA** gemäß `NFR-19`, `O-S3-09` und `REL-A16` ein zu bestätigendes und nachzuweisendes Ziel bleibt. | Konkrete Service-Worker-/Offline-Synchronisationsstrategie, gezielte UI-/Hilfspakete und Produktions-ASGI-/Proxy-Konfiguration. | Echte Geräte-/PWA-/Offline-Konfliktprüfungen (`NFR-02/03`), Zielbestätigung (`O-S3-09`) und vollständige Barrierefreiheits-/Screenreader-Prüfung (`REL-A16`, `T01`). |
| **TECH-O-05 — Identität** | Austauschbare Identitätsarchitektur; fachliche Autorisierung autoritativ in FastAPI; Erhalt von `FE-60` (sofortiges E-Mail-OTP bei Registrierung), Geräteverifikation (`SEC-02`), Sessions sowie `R1` (ohne 7d-Autoablauf) und `R4` (kontrollierter Reset unverifizierter `pending`-Konten ab `>= 24 h`, ohne 24h-Wartezeit vor Erstverifikation); Vergleich von **Google Identity Platform / Firebase Authentication**, **Keycloak**, **authentik** und geeigneten **FastAPI-Komponenten**; noch kein Anbieter gewählt (`Argon2id` aus `ADR-0008`/`ADR-0009` ist lokaler Prototyp, produktive Wahl offen unter `REL-S05`/`N2.2`). | Konkrete Auswahl zwischen Google Identity Platform / Firebase Authentication, Keycloak, authentik oder FastAPI-Komponenten, produktives Passwort-Hashing (`REL-S05`) sowie produktives Verfahren zur sicheren Übergabe des persönlichen Recoverycodes (`O-S3-11`). | Nachweis der Einhaltung von E-Mail-OTP (`FE-60`), Gerätebindung, `R1`/`R4`-Regeln, Anti-Enumeration, Portabilität ohne Lock-in, EU-/Datenschutzbedingungen (`O-S3-10`), RAM und Kosten (`T06`, `T09`, `REL-S01..S09`). |
| **TECH-O-06 — Sicherheit des Super Admin** | Verpflichtende starke MFA; getrenntes Adminkonto und getrennte Adminumgebung; genau ein Super Admin (`CON-02/37/40`, `FE-70..72`, `INV-28`, `SEC-05`); kein administratives Inhaltsrecht (`INV-26`); administrative Recovery getrennt von persönlicher Recovery (`SEC-03`); **kein Generalschlüssel (kein Master-Key)** für den Super Admin zur Entschlüsselung privater Dokumente (`FE-77`, `INV-29`, `SEC-09`); Auditierung privilegierter Vorgänge (`DM-57`, `SEC-14`). | Konkrete MFA-Faktoren (z. B. WebAuthn/FIDO2 vs. TOTP), konkrete Sitzungsfristen und technischer Manipulationsschutz der Auditprotokolle (`DM-57`, `SEC-14`), technisches Erstbootstrap-Verfahren (`O-S3-04`, `O-S1-13`), administrative Notfall-Recovery (`O-S3-05`) und persönliche Dokumentenschlüssel-Kryptografie/-Recovery (`O-S3-11`, `O-S1-07`, `O-S2-02`). | Negativ- und Verlustfalltests für Bootstrap, MFA-Zwang, Admin-Isolation und Schlüsselverlust (`AT-S3-02..05`, `T06`, `T09`, `REL-S04/S06/S09/S19`). |
