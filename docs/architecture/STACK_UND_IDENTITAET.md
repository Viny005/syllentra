# Frontend, Backend und Identität

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

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
