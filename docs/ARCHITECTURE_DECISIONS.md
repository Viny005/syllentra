# Architecture Decision Records

This directory is intentionally structured to support future Architecture Decision Records (ADRs). The project is still in its research and design phase, and no final technology stack should be considered settled without evaluation.

## Purpose

Architecture Decision Records help document:

- the reasons for a design choice
- the alternatives considered
- the trade-offs involved
- the context in which a decision was made

## Initial ADR structure

Each ADR should include:

- Title
- Status
- Date
- Context
- Decision
- Consequences
- Alternatives considered

## Initial ADRs to be created as needed

### ADR-0001: Document architecture decisions
This ADR should establish the expectation that major decisions are recorded and reviewed before implementation work proceeds.

### ADR-0002: Define the intended system boundaries
This ADR should document major components, responsibilities, and integration boundaries as the architecture becomes more concrete.

### ADR-0003: Select evaluation criteria for future technology choices
This ADR should define the criteria by which AI providers, frameworks, databases, and infrastructure choices will be assessed.

## Current position

Die 14 übergreifenden **Architekturprinzipien TECH-O-01 bis TECH-O-14** sowie die **Querschnittsentscheidung zur Austauschbarkeit mehrerer Anbieter (Multi-Provider)** wurden vom Projektinhaber in Mission 21 (23.10.2026) auf Architekturebene bestätigt (siehe `ADR-0010` bis `ADR-0024` unten). Dabei gilt durchgängig die dreifache Trennung:
- **A. Bestätigtes Architekturprinzip:** vom Projektinhaber genehmigte architektonische Leitlinie.
- **B. Offene technische Unterentscheidung:** noch nicht ausgewählter konkreter Anbieter, Dienst, Schlüssel-/MFA-Mechanismus, Modell-/Stimmenkatalog, Queue-/Backup-Werkzeug oder Versionsstand.
- **C. Ausstehender Nachweis / zukünftige Prüfung:** noch nicht ausgeführter Benchmark (`T01`–`T09`), Sicherheitstest, Restore-Lauf, Lizenz-/Vertragsnachweis oder Last-/Kostenbeleg.

Ein bestätigtes Architekturprinzip gilt niemals als Nachweis einer bereits funktionierenden oder abgenommenen Produktimplementierung.

## Bestätigte Entscheidungsgrundlagen vom 22.10.2026

Quelle: Nutzerauftrag „Syllentra AI — Mission 2: Consolidation documentaire et harmonisation des décisions“, Abschnitte 2 und 3. **DEC-48** und **DEC-49** waren im überprüften Ausgangsstand `f12a46881f54dccc8568d9982bba0c41564b052e` nicht vergeben. Sie sind eigene bestätigte Entscheidungsbezüge, keine FE-Nachträge und keine Umnummerierung von DEC-V1-01 bis DEC-V1-25. Die folgenden ADRs dokumentieren den bestätigten Bewertungsauftrag und die Schutzanforderung; ihre technische Ausarbeitung bleibt **Zur Prüfung durch den Projektinhaber**. Kein Account, keine Infrastruktur oder Ausgabe ist dadurch autorisiert.

### ADR-0004 — Vorrangige Hostingbewertung von Oracle Cloud (DEC-48)

**Datum:** 22.10.2026\
**Status:** Bewertungspriorität durch Projektinhaber bestätigt; technische Auswahl offen, ADR zur Prüfung.

**Kontext:** Syllentra benötigt zentrale mehrbenutzerfähige Daten-/Verarbeitungskapazität mit EU-Residenz, Geräteabgleich und Betrieb ohne ständig eingeschalteten privaten PC. Kostenlose Angebote sind zu prüfen, keine nachgewiesene dauerhafte Kostenfreiheit vorauszusetzen.

**Entscheidungsrahmen:** Oracle Cloud Infrastructure ist die **erste zu untersuchende und später gesondert zu testende Option**, kein endgültig gewählter Anbieter. Wenn Oracle Anforderungen nicht erfüllt, sind geeignete Alternativen zu vergleichen. Diese Dokumentationsmission erstellt weder Accounts noch externe Testressourcen und führt keinen Infrastrukturtest aus.

**Bewertungskriterien:** Tatsächliche EU-Regionen und Unterauftragnehmer; Sicherheits-/Rechte- und Schlüsselgrenzen; real verfügbare CPU-/Modellkapazität, Speicher, Netz, Kontingente und Parallelbetrieb; Verfügbarkeit und operative Einschränkungen einschließlich Ausfall-/Accountverlust; vollständige Speicher-, Transfer-, Backup- und Betriebskosten, Gratislimits und Abrechnungsrisiken; kommerziell geeignete Software-/Modelllizenzen, Skalierbarkeit und Portabilität. Der Vergleich berücksichtigt DEC-49 und keine verpflichtende kostenpflichtige KI-API. Ein Gratisetikett ersetzt keine aktuellen Bedingungen oder Kapazitätsbelege.

**Kosten-/Ausführungsgrenze:** Seit Mission 7 bis zu **20 EUR brutto/Monat** ausschließlich für künftige Vergleiche; ersetzt die frühere 10-EUR-Hypothese aus PACE/Mission 2–6. **Keine Ausgabe genehmigt**; keine Buchung, Provisionierung oder automatische kostenpflichtige Ausweichlösung. Erfordert ein späterer Test Ressourcen oder Kontozugang, ist der konkrete Test vor Ausführung gesondert zu autorisieren.

**Alternativen und Folgen:** Andere geeignete EU-konforme Hostingmöglichkeiten bleiben prüfbar; konkrete Kandidaten und Messwerte sind noch zu ermitteln. Provider-, Framework-, Datenbank- und Modellentscheidung werden nicht vorweggenommen. Ein negatives Oracle-Ergebnis führt zu dokumentiertem Vergleich statt Abschwächung von Datenschutz oder Sicherheit.

**Verweise:** [P1](spec/P1-ziele-rahmenbedingungen.md), [P2](spec/P2-architekturueberblick.md), [N1](spec/N1-nichtfunktional.md), [Entscheidungsmatrix](spec/ENTSCHEIDUNGSMATRIX.md).

### ADR-0005 — Anbieterunabhängige verschlüsselte Sicherung (DEC-49)

**Datum:** 22.10.2026\
**Status:** Schutzziel durch Projektinhaber bestätigt; technisches Verfahren und Anbieter offen, ADR zur Prüfung.

**Kontext:** Portabilität und eine Kopie innerhalb derselben Hostingumgebung schützen nicht ausreichend gegen deren Ausfall, versehentliche Löschung, Korruption oder Kompromittierung. Bei Oracle als möglichem Primärhost darf die erforderliche unabhängige Sicherung nicht allein bei Oracle liegen.

**Entscheidungsrahmen:** Verschlüsselte Sicherungen in der EU mit sicherer Schlüsselverwaltung und **Speicher bei einem vom primären Hostinganbieter unabhängigen Anbieter**. Eine zusätzliche Region oder ein zweites Konto desselben Anbieters belegt diese Anbieterunabhängigkeit nicht. Geeignete Zugriffs-/Schlüsseltrennung und kontrollierte Wiederherstellung müssen auch beim Verlust des Primärzugangs nachweisbar sein. Kein endgültiger Backupanbieter, Verschlüsselungsprodukt oder kostenpflichtiger Dienst wird ausgewählt.

**Nachweise und Folgen:** Zugriffsrechte auf Erstellung, Abruf, Wiederherstellung und Löschung begrenzen und prüfen; Integrität, Wiederherstellbarkeit und Portabilität unter Ausfall, versehentlicher Löschung, Korruption und Kompromittierung untersuchen. Periodische echte Restore-Proben dokumentieren; aktueller Lösch-/Widerrufskontrollstand bleibt auch bei unabhängigem Restore maßgeblich. Endliche Retention und Benutzerlöschung technisch abstimmen, keine gelöschten Inhalte wiederbeleben. Schlüsselverwaltung bleibt mit FE-77/78 vereinbar: Backupzugriff ist kein privates Inhaltslese- oder Dokumentenschlüsselrecht für Admins.

**Offene technische Entscheidungen:** Anbieter, Verfahren, Verantwortlichkeiten und Nachweis der Unabhängigkeit, Schutz gegen Manipulation/ungewollte Löschung, Schlüsselrecovery, RPO/RTO, Sicherungsfrequenz, Testintervall und Retention. Keine Zahlen oder pauschale Unveränderlichkeits-/Sofortlöschgarantie erfinden. Kosten- und Lizenzprüfung einschließlich Transfer; kein nicht autorisierter kostenpflichtiger Dienst. S3 wird später Betriebsfreigabe und Abläufe aufnehmen, wird hier nicht begonnen.

**Alternativen:** Geeignete unabhängige EU-Sicherungsverfahren sind zu vergleichen. Eine Sicherung nur beim Primäranbieter oder bloßer Nutzerselfservice-Export ersetzt DEC-49 nicht; ergänzende interne Kopien bleiben möglich.

**Verweise:** [S2](spec/S2-datenmigration.md), [N2](spec/N2-querschnittskonzepte.md), [Release-Register](quality/RELEASE_READINESS_40.md), [Entscheidungsmatrix](spec/ENTSCHEIDUNGSMATRIX.md).

## Technische Vergleichsstudie vom 22.10.2026 — keine zusätzliche Architekturfreigabe

Mission 5 dokumentiert [Architekturvergleich](architecture/README.md), [offene technische Entscheidungen](architecture/OFFENE_ENTSCHEIDUNGEN.md) und [Quellen/Abrufgrenzen](architecture/QUELLEN.md) im Status **Empfohlen / Zur Entscheidung**. Modularer Monolith, PostgreSQL, Vite/FastAPI, begrenzte CPU-Worker, konkrete KI-/Authkandidaten und drei Hostingkonzepte sind Untersuchungsempfehlungen, keine beschlossenen ADRs. Bestehende ADR-0004/0005 und DEC-48/49 unverändert: Oracle zuerst bewerten, unabhängiges verschlüsseltes EU-Backup erforderlich. Keine neue ADR-Kennung, kein Anbieter/Stack ausgewählt, kein Ausgaben-/Implementierungs-/Deploymentauftrag.

Vor einer technischen Entscheidung aktuelle Angebote, individuelle Gewichts-/Stimmenlizenzen, Support-/ARM64-Nachweise und geeignete Leistungs-/Sicherheitsmessungen nach eigenem Auftrag schließen. Erst die ausdrückliche Eigentümerentscheidung darf einen entsprechenden ADRstatus ändern. Ein hypothesenbasierter Punktwert oder zugängliches README ist keine Sicherheits-/Verfügbarkeits-/Budgetgarantie.


### ADR-0006 — Persönlicher Qualitätsfokus und Vergleichsrahmen aus Mission 7

**Status:** Bestätigter Untersuchungsrahmen des Eigentümers; technische Empfehlungen weiter **Empfohlen / Zur Entscheidung**, Fachentwürfe Zur Prüfung.

**Quelle / Datum:** Vollständiger Nutzerauftrag „SYLLENTRA AI — MISSION 7“, Abschnitt 1, 22.10.2026; Ausgangscommit `f3e3aa647cd96171e300056379063d5761f16e70`.

**Bestätigt:** Zuerst hochwertige persönliche Lernassistenz mit guter UX, nützlicher Pädagogik und zufriedenstellender Leistung. Künftige Vergleiche dürfen bis zu **20 EUR brutto/Monat** untersuchen; frühere 10-EUR-Hypothese ersetzt, historische Rechnungen bleiben datierte Nachweise. **Keine Ausgabe genehmigt.** V1-Registrierung/Multiuser mit strikter Isolation, getrennten Adminaccounts, Serverrechten und progressiver Aktivierung bleibt unverändert. Mögliche spätere Nutzerbeiträge nur untersuchen; kein V1-Zahlungssystem genehmigt.

**Folgen / Grenzen:** Neue [Design-/Entwicklungsstudie](development/INTEGRATION_ROADMAP.md) ergänzt die bisherigen Alternativen, wählt keinen Anbieter/Stack/Modell und genehmigt keine Installation, API, Cloud oder Inbetriebnahme. DEC-48/49 und alle TECH-O bleiben bestehen. Persönlicher Prototyp ersetzt keine vollständige Multiuser-V1-Abnahme; Sicherheit wird nicht später nachgerüstet. Budgetplausibilität und Leistung benötigen aktuelle Angebote und gesondert erlaubte Tests.


### ADR-0007 — Lokale Frontendprobe aus Mission 8

**Status:** Vom Eigentümer autorisierter experimenteller Umfang, **keine endgültige Stackentscheidung**. Quelle: vollständige Mission 8, Abschnitte 1–13, 22.10.2026; Ausgangscommit `2f526e4c3120353be9b9648af3956b89372acb90`.

React + Vite + TypeScript für einen lokalen, reversiblen, synthetischen UI-Prototyp gewählt: stärkster bisher dokumentierter Frontendkandidat, keine fachliche Gegenanforderung festgestellt. Node 24.x, npm mit exakten Versionen/Lockfile, Installskripte aus. Eigenes tokenbasiertes CSS und native Controls statt zusätzlicher UI-/Router-/Editor-/Kalenderframeworks halten den Umfang klein. TypeScript 6.0.3 wegen tatsächlichem Peerbereich des Linters, keine blinde Latestinstallation. Lizenzen und echte [Prüfungen](design/PROTOTYPE_REVIEW.md) dokumentiert.

TECH-O-03 und sämtliche übrigen TECH-O bleiben offen; keine Bestätigung von FastAPI, Datenbank, Hosting, Authentisierung oder KIanbieter. Keine fachliche FE-/UC-/DECänderung, keine Produktfreigabe, Kosten, Cloud oder Merge/Deployment. [Prototyp](../prototypes/frontend/README.md) kann nach UXreview ersetzt/entfernt werden; kein eigener Backendvertrag oder persistentes Produktdatenformat angelegt.


### ADR-0008 — Lokale Backendprobe aus Mission 9

**Datum:** 22.10.2026\
**Status:** Lokales Experiment durch Nutzerauftrag autorisiert; Umsetzung Zur Prüfung. Keine endgültige Technologieentscheidung.

**Kontext:** Mission 8 liefert ausschließlich eine UI-Demo. Mission 9 autorisiert eine reversible lokale Sicherheitsgrundlage mit synthetischen Daten auf dem bestehenden Spezifikationsbranch. FE-57/58/59, SEC-01..07 und S3.5 bleiben unverändert; fehlende OTP-/Geräte-/MFA-/Recoverywege dürfen keinen realen Benutzerzugang eröffnen.

**Experiment:** FastAPI/Python mit PostgreSQL und direktem psycopg, ein modular gegliederter Prozess ohne Queue/Worker/ORM. Argon2id, opake gehashte Serversitzungen, aktuelle Eigentums-/Rollen-/Flagprüfung und eingeschränkter SQL-Servicezugang. PostgreSQL im lokalen flüchtigen offiziellen Docker-Image, getrennte Entwicklungs-/Testdatenbanken, versionierte Vorwärtsmigration. Laufzeit ohne Seed und mit gesperrter Anmeldung; künstliche Verifikation/Geräte nur im internen isolierten Testharness. Keine funktionale Administration und keine Super-Admin-Erstbesetzung.

**Alternativen / Konsequenzen:** Keycloak/authentik bzw. geprüfter Bibliotheksansatz aus TECH-O-05 bleiben zu vergleichen; das Testharness ist kein alternativer produktiver Identitätsanbieter. Django, TS-Backend und ORM bleiben möglich. Direkte kleine SQLschicht vermeidet zusätzliche Abhängigkeit, verlangt dafür disziplinierte serverseitige Filter und Negativtests. Keine technische Hypothese wird durch begrenzte Tests automatisch endgültig gewählt. TECH-O-01/03/04/05/06/13 bleiben insbesondere offen.

**Review / Git:** PR #1 ist offen und umfasste vor Mission 9 112 Dateien mit 26.168 hinzugefügten und 217 entfernten Zeilen. Bestehenden autorisierten Branch beibehalten, Backendcode separat unter `prototypes/backend` und in eigenem Commit reviewen; Ausgang `8ad51e8ef1ed010b20907602fe742268d799621e` begrenzt das Reviewdelta. Eine neue Branch/PR wurde nicht genehmigt oder angelegt. Spätere Aufteilung nur mit ausdrücklicher Zustimmung: gestapelte Backendbranch auf PR-#1-HEAD, zunächst gegen die Spezifikationsbranch reviewen, nach deren Merge Ziel/Basis sorgfältig aktualisieren. Eine vorzeitige zweite PR gegen main würde die bestehenden 112 Dateien duplizieren. Kein Rebase, Force-Push oder Merge hier.

**Belege / Grenzen:** [Lokale Anleitung](../prototypes/backend/README.md), [APIvertrag](../prototypes/backend/openapi.json), [Prüfbericht](development/BACKEND_PROTOTYPE_REVIEW.md). Keine produktive Auth, KI, Cloud, Ausgaben, vollständige REL-Abnahme oder Deployment. Browserintegration bleibt gesperrt, Frontend unveränderte Demo; endgültige Anbieter-/Stack-/Frist-/Bootstrapentscheidungen beim Projektinhaber.


### ADR-0009 — Lokale Identitätsprobe aus Mission 10

**Datum:** 22.10.2026\
**Status:** Begrenzte lokale Umsetzung durch Nutzerauftrag autorisiert; Experiment Zur Prüfung, keine endgültige IdP-/MFA-/Stackwahl.

**Kontext / Rechte:** Mission 10, Abschnitte 1–18, autorisiert synthetische Registrierung, OTP, Geräte, Sessions, Recovery und lokale UI auf bestehender Branch. Ausgang `cd971cd57ff7c968d6439375aaf1c1798cf16a81`; PR #1 OPEN, bereits 130 Dateien / +29.649 / −217 gegen main. Gleiche Branch und separater Reviewcommit; keine neue Branch/PR. Spätere gestapelte Aufteilung nur mit Zustimmung und zunächst gegen die Spezifikationsbranch, um das ungemergte Ausgangsdelta nicht nochmals gegen main zu duplizieren; kein Rebase/Force-Push/Merge hier.

**Experimentelle Umsetzung:** Vorhandenen FastAPI-/PostgreSQL-Kern modular erweitern, keine neue Laufzeitabhängigkeit oder externer IdP. Serverseitig gebundene HMAC-Einmalcodes über private lokale Adapter; bekannter Gerätenachweis im geschützten Cookie, neues Gerät nur über vorhandenes berechtigtes Gerät plus Passwortbestätigung oder gesonderte Recovery mit verifizierter E-Mail plus persönlichem Offline-Einmalcode. Keine Dokumentenschlüsselübernahme. Eigener expliziter Loopback-TLS-Einstieg mit restriktiver DB-/Adress-/Originprüfung, Host-Cookies, CSRF und fest geprüftem lokalem HTTPS-Proxy. Vorherigen Verifikationstest-Anmeldebypass entfernen; normaler deaktivierter Einstieg bleibt geschlossen.

**Alternativen / Entscheidung offen:** Keycloak/authentik und Bibliotheksauth bleiben TECH-O-05. TOTP und WebAuthn brauchen sichere Faktorbindung, Secretspeicherung, Wiederherstellung und Plattformnachweise; keine unvollständige Admin-MFA aktivieren. Persönlicher Offline-Testcode demonstriert nur den getrennten lokalen Recoverykanal, keine genehmigte reale Ausgabe. Adminlogin und Bootstrap bleiben gesperrt, kein echter Super Admin. Softwarelizenz-/Modell-/Hostingwahl nicht durch Experiment entschieden.

**Konsequenzen:** Größere eigene Sicherheitsverantwortung trotz kleiner Abhängigkeitszahl; bestehende Produktanforderungen nicht abschwächen. Nur experimentelle Fristen/Budgets, keine V1-SLO. TLS selbst signiert, lokale Mailboxen keine echte Mailzustellung; keine Produktionsreife. [Architektur](development/IDENTITY_ARCHITECTURE.md), [Anleitung](../prototypes/backend/README.md) und [Prüfbericht](development/IDENTITY_PROTOTYPE_REVIEW.md) trennen Implementierung, tatsächliche Tests und ausstehende Verfahren. Historischer Stand bei Abschluss von Mission 10: FE-56 und alle 14 TECH-O offen (FE-56 seit Mission 19 als V1-Postfachausschluss bestätigt; die 14 TECH-O-Architekturprinzipien in Mission 21 in `ADR-0010` bis `ADR-0024` bestätigt, Unterentscheidungen und Nachweise weiter offen), Spezifikation Zur Prüfung; keine Cloud, Ausgabe, externe Accounts, öffentliche Registrierung oder Veröffentlichung.


## Vom Projektinhaber bestätigte Architekturprinzipien aus Mission 21 (23.10.2026 — TECH-O-01 bis TECH-O-14 und Multi-Provider)

Quelle: Ausdrücklicher Eigentümerauftrag „SYLLENTRA AI — MISSION 21: Consolidation des 14 décisions architecturales TECH-O selon Siedersleben/PACE“ vom 23.10.2026 (ausgehend von `docs/spec/p1-p2-mobile-workspaces` bei `a70076fb4f8d5d22b171541b30b61b6e912ba342`, [PR #1](https://github.com/Viny005/syllentra/pull/1)), auf dem dedizierten Prüfzweig `docs/mission21-tech-o-consolidation` veröffentlicht (`34d71aab23dfb603b4eaea1b1273888af1857447`) und nach dem unabhängigen Codex-Audit (Mission 22) in Mission 21B präzisiert; die Nachvollziehbarkeit stützt sich ausschließlich auf die übergebenen Missionsaufträge und die versionierten Repository-Dokumente (ohne Behauptung einer Prüfung externer, nicht im Repository versionierter Gesprächsprotokolle). Für jede Entscheidung sind **A. Bestätigtes Architekturprinzip**, **B. Offene technische Unterentscheidung** und **C. Ausstehender Nachweis** strikt getrennt. Keine neue `FE`-, `UC`- oder `DEC-V1`-Kennung; keine Freigabe von Ausgaben, Cloudkonten, Modell-Downloads, Benchmarks oder Produktivbetrieb.

### ADR-0010 — Evolutionärer modularer Monolith und isolierte Worker (TECH-O-01)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Unterentscheidungen (B) und Nachweise (C) offen.
- **Kontext:** Die 89 FE, 66 UC und strikten Kontentrennungsgrenzen (`FE-58`, `FE-59`, `SEC-04`) erfordern gemeinsame Transaktionen, einheitliche Autorisierung und geringen Betriebsaufwand ohne verfrühte Verteilungskomplexität.
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Evolutionärer modularer Monolith mit klarer Trennung der fachlichen Verantwortlichkeiten im autoritativen Anwendungskern und isolierten Workerprozessen für rechenintensive oder nicht vertrauenswürdige Hintergrundverarbeitung (Medien, OCR, ASR, TTS, KI-Läufe) hinter austauschbaren internen Adaptern. Keine flächendeckenden Microservices ab V1.
- **Offene technische Unterentscheidungen (B):** Konkreter Prozess-/Supervisor-Zuschnitt, Adapter-Schnittstellen, Ressourcenlimits (CPU/RAM/Timeouts) je Workerklasse sowie spätere Auslagerungsschwellen einzelner Worker.
- **Ausstehende Nachweise und Konsequenzen (C):** Koexistenz- und Isolationsmessungen (`T01`, `T09`), Nachweis der Fehler-/Abbruchkapselung zwischen API-Kern und Workern (`NFR-25`, `REL-Q07..Q09`).
- **Betrachtete Alternativen:** Verteilte Microservices ab V1 (abgelehnt wegen höherer Angriffs-, Konsistenz- und Betriebskomplexität); monolithischer Einzelprozess ohne Workerisolation (abgelehnt wegen Blockade- und Parserrisiken).

### ADR-0011 — Hosting-Prüffolge: OCI vorrangig, Hetzner als bevorzugter Rückfall, Google Cloud als Alternative (TECH-O-02)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt (`DEC-48` gewahrt); konkreter Anbieter/Vertrag (B) und Kapazitäts-/Kostennachweis (C) offen.
- **Kontext:** Zentrale EU-Datenhaltung und Cloud-Betrieb unabhängig vom privaten PC (`CON-36`, `FE-42`, `FE-75`, `SEC-08`) sowie Bewertungspriorität `DEC-48` ([ADR-0004](#adr-0004--vorrangige-hostingbewertung-von-oracle-cloud-dec-48)).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Oracle Cloud Infrastructure (OCI) ist der erste zu testende Kandidat. Hetzner ist die bevorzugte europäische Rückfalllösung (Fallback). Google Cloud bleibt als weitere bewertbare Alternative erhalten. Es ist noch kein Anbieter, keine Region, kein Konto und kein Server endgültig ausgewählt.
- **Offene technische Unterentscheidungen (B):** Endgültige Anbieterwahl, konkrete EU-Region, Instanzklasse/Architektur (ARM64 vs. x86_64), Netz-/Volume-Zuschnitt und Auftragsverarbeitungsvertrag.
- **Ausstehende Nachweise und Konsequenzen (C):** Verifikation aktueller offizieller Tarife, Gratis-/Kontingentregeln, EU-Unterauftragnehmer und realer Zuteilung sowie gesondert autorisierte Infrastruktur-/Lastprobe (`T01`, `T08`, `O-S3-01/03`).
- **Betrachtete Alternativen:** Sofortige Festlegung auf einen einzigen Anbieter ohne Kapazitäts-/Vertragsbeleg (abgelehnt); Betrieb auf privatem Dauer-PC (durch `CON-36` / `FE-75` ausgeschlossen).

### ADR-0012 — Anwendungsstack: React + Vite + TypeScript und FastAPI + Python (TECH-O-03)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Paket-/UI-Unterentscheidungen (B) und PWA-/A11y-Produktnachweise (C) offen.
- **Kontext:** Mehrsprachige (`DE`/`FR`/`EN`), installierbare PWA (`FE-55`) und ein autoritatives Backend mit direkter Anbindung an Python-basierte Extraktions-/KI-Werkzeuge; erste lokale Proben in [ADR-0007](#adr-0007--lokale-frontendprobe-aus-mission-8) und [ADR-0008](#adr-0008--lokale-backendprobe-aus-mission-9).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Frontend auf Basis von **React + Vite + TypeScript**; Backend auf Basis von **FastAPI + Python**. Das PWA-Ziel (`FE-55`) und die bestehenden Barrierefreiheitsanforderungen (`NFR-08/19/20`, `REL-A16`) bleiben verbindlich erhalten; das genaue normative Zielniveau (**WCAG 2.2 AA**) bleibt gemäß `NFR-19`, `O-S3-09` und `REL-A16` ein durch den Projektinhaber zu bestätigendes und in der Produktprüfung nachzuweisendes Ziel.
- **Offene technische Unterentscheidungen (B):** Konkrete Service-Worker-/Offline-Synchronisationsstrategie, gezielte UI-/Hilfsbibliotheken, Produktions-ASGI-/Reverse-Proxy-Konfiguration und gepinnte Zielversionen für die V1-Freigabe.
- **Ausstehende Nachweise und Konsequenzen (C):** Echte Geräte-/Browser-/PWA-Installations- und Offline-Konflikttests (`FE-55`, `NFR-02/03`), Bestätigung des Zielniveaus (`O-S3-09`) und vollständige Barrierefreiheits-/Screenreader-Prüfung (`NFR-08/19/20`, `REL-A16`) sowie Ende-zu-Ende-Integrationstests zwischen React-Client und FastAPI-Kern (`FE-55`, `NFR-02/03`, `REL-Q07..Q09`).
- **Betrachtete Alternativen:** Next.js/Node.js-Vollstack oder Django-Monolith (nicht als V1-Hauptstack gewählt, um Laufzeit- und SSR-Caching-Komplexität für private Lernräume gering zu halten).

### ADR-0013 — Datenhaltung, geschützter Dateispeicher, Volltextsuche und PostgreSQL-Queue (TECH-O-04)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Speicher-/Extension-Unterentscheidungen (B) und Last-/Qualitätsnachweise (C) offen.
- **Kontext:** 78 fachliche Entitäten und 31 Invarianten in [D1](spec/D1-datenmodell.md) verlangen transaktionale Integrität, strikte Kontoisolation (`SEC-04/19`) und konsistente Sicherung (`DEC-49`).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** **PostgreSQL** ist die primäre relationale Datenbank. Große Dateien und Medien nutzen einen getrennten geschützten Dateispeicher. Die **PostgreSQL-Volltextsuche** bildet die initiale Referenz für Suche und Retrieval. Der Einsatz von `pgvector` hängt vom nachgewiesenen Mehrwert in Tests ab. Eine **PostgreSQL-basierte Aufgabenwarteschlange (Task-Queue)** wird evaluiert, bevor eine zusätzliche Queue-/Broker-Technologie ausgewählt wird.
- **Offene technische Unterentscheidungen (B):** Konkreter geschützter Dateispeicher (verschlüsseltes Volume vs. S3-kompatibler EU-Objektspeicher), PostgreSQL-Major-/Patchversion, eventuelle `pgvector`-Aktivierung, konkretes Tabellenschema der PostgreSQL-Queue (`FOR UPDATE SKIP LOCKED`) und RLS-/Rollenhärtung.
- **Ausstehende Nachweise und Konsequenzen (C):** Dedizierter Retrieval- und Ressourcenvergleich zwischen PostgreSQL-Volltextsuche und `pgvector`/Embeddings in Verbindung mit `T03` (Quellenbindung und pädagogische Güte in `DE`/`FR`/`EN`), `T01` (CPU-/RAM-Koexistenz) und `T09` (durchgängige Konto- und Indexisolation) — während `T04` das Benchmarkprotokoll für Dokumentextraktion und Provenienz (Text-/Seitenbelege als Zulieferung für den Index) prüft — sowie Durchsatz-/Sperrverhalten der PostgreSQL-Queue unter Last (`T01`, `T09`) und konsistenter DB-plus-Dateispeicher-Restore (`T07`).
- **Betrachtete Alternativen:** Separate Vektordatenbank (z. B. Qdrant) oder externer Message-Broker (z. B. Redis/Valkey/RabbitMQ) ab Start ohne Bedarfsnachweis (abgelehnt).

### ADR-0014 — Austauschbare Identitätsarchitektur und autoritative FastAPI-Autorisierung (TECH-O-05)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; IdP-/Komponentenwahl (B) und produktive Sicherheits-/Integrationsnachweise (C) offen.
- **Kontext:** Verifizierter Zugang mit sofortigem E-Mail-OTP bei der Registrierung (`FE-60`, `SEC-01`), Gerätevertrauen und -freigabe (`SEC-02`), Zweikanal-Recovery und die am 23.10.2026 bestätigten Entscheidungen **R1** (persönlicher Einmal-Recoverycode ohne automatischen 7-Tage-Ablauf) und **R4** (kontrollierte Rücksetzung eines mindestens 24 Stunden unverifiziert gebliebenen `pending`-Kontos in einem neuen Registrierungsablauf, ohne 24-Stunden-Wartezeit vor der Erstverifikation; [ADR-0009](#adr-0009--lokale-identitätsprobe-aus-mission-10), [N2.2](spec/N2-querschnittskonzepte.md#n22-konten-authentifizierung-und-sitzungen)).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Austauschbare Identitätsarchitektur hinter klaren internen Schnittstellen, während sämtliche fachlichen Autorisierungs-, Sitzungs-, Geräte-, Rollen-, Flag- und Kontentrennungskontrollen **autoritativ im FastAPI-Backend** durchgesetzt werden. `FE-60`, Geräteverifikation, Sitzungsverwaltung sowie die Regeln **R1** und **R4** bleiben vollständig erhalten. Verglichen werden **Google Identity Platform / Firebase Authentication**, **Keycloak**, **authentik** und geeignete **FastAPI-Komponenten**. Es ist noch kein Identitätsanbieter ausgewählt (die lokale `Argon2id`-Implementierung aus `ADR-0008`/`ADR-0009` bleibt ein lokaler Prototyp; das produktive Passwort-Hashing und die endgültige Komponentenwahl unterliegen `REL-S05`/`N2.2` und der `TECH-O-05`-Auswahl).
- **Offene technische Unterentscheidungen (B):** Auswahl zwischen verwaltetem Dienst (Google Identity Platform / Firebase Authentication), selbst gehostetem IdP (Keycloak, authentik) oder gehärteten FastAPI-Authentifizierungskomponenten, produktive Passwort-Hashing-/MFA-Konfiguration (`REL-S05`, `REL-S06`) sowie das produktive Verfahren zur sicheren Übergabe des persönlichen Recoverycodes (`O-S3-11`).
- **Ausstehende Nachweise und Konsequenzen (C):** Nachweis der exakten Einhaltung von E-Mail-OTP (`FE-60`), Gerätebindung, Anti-Enumeration, `R1`/`R4`-Regeln, Datenkontrolle/Portabilität ohne harten Lock-in, Datenschutz/EU-Verarbeitung (`O-S3-10`), RAM-/Betriebsbedarf und Kosten für jeden Kandidaten (`T06`, `T09`, `REL-S01..S09`).
- **Betrachtete Alternativen:** Übertragung fachlicher Objekt-/Rollenautorisierung an einen externen IdP oder ungeprüfte Übernahme von Standard-Link-Flows ohne E-Mail-OTP (abgelehnt).

### ADR-0015 — Schutzgrenzen, starke MFA und Trennung des Super Admin (TECH-O-06)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; konkrete MFA-/Bootstrap-/Recovery-Verfahren (B) und Sicherheitsnachweise (C) offen.
- **Kontext:** Genau ein Super Admin (`CON-02`, `CON-37`, `CON-40`, `FE-70..72`, `INV-28`, `SEC-05`), kein administratives Zugriffsrecht auf private Benutzerinhalte (`INV-26`), Schutz privater Dokumentenschlüssel ohne Klartext am Backend oder bei der Administration (`FE-77`, `INV-29`, `SEC-09`), Auditierung privilegierter Vorgänge (`DM-57`, `SEC-14`) und kontrollierter Erstbootstrap ([S3.5](spec/S3-inbetriebnahme.md#s35-sicherer-erstbootstrap-und-administrative-kontinuität)).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Verpflichtende starke MFA für die Administration; strikt getrenntes Administrationskonto und getrennte Administrationsumgebung; administrative Kontowiederherstellung strikt getrennt von der persönlichen Benutzerwiederherstellung (`SEC-03`); **keinerlei universeller Schlüssel (kein Master-Key / keine Backdoor)**, mit dem der Super Admin private Benutzerdokumente entschlüsseln könnte (`FE-77`, `INV-26`, `INV-29`, `SEC-09`).
- **Offene technische Unterentscheidungen (B):** Konkrete starke MFA-Faktoren (z. B. WebAuthn/FIDO2-Hardwaretoken vs. TOTP), konkrete Sitzungsfristen und technischer Manipulationsschutz der Administrations-Auditprotokolle (`DM-57`, `SEC-14`), technisches Erstbootstrap-Protokoll (`O-S3-04`, `O-S1-13`), administratives Notfall-/Recoveryverfahren ohne zweiten Super Admin (`O-S3-05`) und das getrennte Verfahren der persönlichen Dokumentenschlüssel-Kryptografie und -Recovery (`SEC-09`, `O-S3-11`, `O-S1-07`, `O-S2-02`).
- **Ausstehende Nachweise und Konsequenzen (C):** Negativ- und Ablaufprüfungen für Bootstrap, MFA-Zwang, Admin-Isolation und Verlustfälle (`AT-S3-02..05`, `T06`, `T09`, `REL-S04/S06/S09/S19`).
- **Betrachtete Alternativen:** Gemeinsames Benutzer-/Adminkonto, ungeschützter Seed-Admin oder administrativer Schlüssel-Escrow für private Dokumente (strikt abgelehnt).

### ADR-0016 — Austauschbare KI-Motoren mit lokaler/kontrollierter Priorität (TECH-O-07)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Modell-/Motorwahl (B) und Lizenz-/Qualitäts-/Ressourcennachweise (C) offen.
- **Kontext:** Pädagogische Assistenz (`DE`/`FR`/`EN`), Quellentreue (`NFR-21..23`), Schutzkennzeichnung und Verarbeitungsfreigabe vor jeder externen Datenübermittlung (`DM-51`, `DM-64`, `DM-66`, `DLG-59`, `SEC-10/17/20/24`) sowie Verzicht auf verpflichtende kostenpflichtige KI-APIs (`CON-23/24`).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Austauschbare KI-Motoren über klar definierte interne Adapter. Priorität haben Modelle, die lokal oder auf kontrollierter eigener Infrastruktur ausführbar sind. Externe KI-APIs bleiben optional und unterliegen vor jeder Nutzung ausdrücklichen Prüfungen von Datenschutz, Schutzstufe/Einwilligung (`DM-51/64/66`, `DLG-59`, `SEC-10/20`), Lizenz (`O-S1-05`), Qualität und Kosten (`CON-23/24`). Es ist noch kein Modell endgültig ausgewählt.
- **Offene technische Unterentscheidungen (B):** Konkrete Inferenzlaufzeit (z. B. `llama.cpp`, `Ollama`, `vLLM`), konkrete Modellgewichte und Quantisierungsstufen (z. B. `Qwen3-1.7B`/`4B`/`8B`), Aufgabenrouting (leichte vs. komplexe Läufe) sowie ggf. zulässige optionale externe API-Anbieter.
- **Ausstehende Nachweise und Konsequenzen (C):** Prüfung der individuellen Gewichtslizenzen und Prüfsummen vor Download (`O-S1-05`, `REL-A13/A14`), CPU-/RAM-/Latenz- und Verbrauchsmessungen samt Raten-/Kostenlimits (`T01`, `T02`, `NFR-15`, `REL-Q01..Q03`) sowie mehrsprachige pädagogische Qualitäts-, Quellentreue- und Prompt-Injection-Prüfungen (`T03`, `NFR-21..23`, `REL-A01/05/07/18`).
- **Betrachtete Alternativen:** Festverdrahtung eines einzelnen proprietären Cloud-LLM als V1-Pflichtvoraussetzung (abgelehnt).

### ADR-0017 — Quellenbasiertes RAG, Volltext-Referenz und strukturiertes pädagogisches Gedächtnis (TECH-O-08)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Embedding-/Chunking-Unterentscheidungen (B) und Retrievalnachweise (C) offen.
- **Kontext:** Nachvollziehbare Quellenarbeit (`NFR-16/21..23`), Ressourcen- und Modellverbrauchsgrenzen (`NFR-15`), Schutzvererbung (`SEC-11/19`) und Trennung zwischen Gesprächsverlauf und langfristigem Lernstand (`D1`, `NFR-24`).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** RAG stützt sich auf überprüfbare, kontogebundene Quellen. Die PostgreSQL-Volltextsuche dient als initiale Referenz. `pgvector` und Embeddings werden nur eingesetzt, wenn ihr Mehrwert in Tests nachgewiesen ist. Das pädagogische Gedächtnis wird strukturiert und getrennt von der Konversationshistorie geführt (`NFR-24`). Strikte Datenisolation jedes einzelnen Kontos vor und nach jedem Retrievalschritt (`SEC-04/11/19`).
- **Offene technische Unterentscheidungen (B):** Chunking-/Zitierstrategie, Konsolidierungsregeln des pädagogischen Gedächtnisses, eventuelles mehrsprachiges Embeddingmodell (z. B. `multilingual-e5-small`, `BGE-M3`, `Qwen3-Embedding-0.6B`) und Reindexierungsregeln.
- **Ausstehende Nachweise und Konsequenzen (C):** Dedizierter Retrieval- und Ressourcenvergleich zwischen PostgreSQL-Volltextsuche und `pgvector`/Embeddings in Verbindung mit `T03` (Quellenbindung und pädagogische Güte in `DE`/`FR`/`EN`), `T01` (CPU-/RAM-Koexistenz) und `T09` (durchgängige Konto- und Indexisolation) — gestützt auf die durch `T04` (Dokumentextraktion und Provenienz) gelieferten Text- und Seitenbelege — sowie A/B-Isolations- und Lösch-/Nichtwiederbelebungstests auf Suchindizes und Gedächtniseinträgen (`T09`, `REL-S04/Q16`).
- **Betrachtete Alternativen:** Unstrukturiertes Vektorarchiv sämtlicher Chats als Gedächtnisersatz oder globale ungefilterte Vektorsuche (abgelehnt).

### ADR-0018 — Lokale Priorität und austauschbare Medienverarbeitung unter Erhalt von AUDIO-01..03 (TECH-O-09)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Komponenten-/Stimmenauswahl (B) und Medien-/Qualitätsnachweise (C) offen.
- **Kontext:** Verarbeitung von PDFs, Bildern, Audio und Video (`FE-21`, `FE-52`, `FE-74`) sowie die in Mission 15/17 bestätigten Entscheidungen `AUDIO-01`, `AUDIO-02` und `AUDIO-03` ([P1.10.6](spec/P1-ziele-rahmenbedingungen.md#p1106-bestätigte-audioentscheidungen-aus-mission-15), [B1.13](spec/B1-dialogspezifikation.md#b113-abnahmeszenarien-für-töne-und-stimmen), [S1.23](spec/S1-nachbarsysteme.md#s123-audioverträge-fähigkeitsgrenzen-und-offene-alternativen)).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Priorität für lokale/kontrollierte Verarbeitung; austauschbare Komponenten für PDF, OCR, ASR, TTS und Video. Direkte Textextraktion hat Vorrang vor OCR, sobald Text unmittelbar extrahierbar ist. Seitenverweise und Zeitstempel (Timestamps) werden erhalten, sofern verfügbar. Langläufer-Aufgaben unterstützen Statusverfolgung, Fehlerbehandlung, Abbruch und kontrollierte Bereinigung temporärer Dateien. `AUDIO-01`, `AUDIO-02` und `AUDIO-03` bleiben vollständig gewahrt. Optionale Google-Dienste können ergänzt werden, falls ihr Vorteil nachgewiesen und freigegeben ist.
- **Offene technische Unterentscheidungen (B):** Konkrete PDF-/OCR-/ASR-/TTS-/Video-Bibliotheken und -Modelle (z. B. PDF-Parser mit passender Lizenz, Tesseract, `whisper.cpp`, Web Speech API vs. Piper-Stimmen `DE`/`FR`/`EN`, optionale Google-Adapter) sowie der lizenzgeprüfte In-App-Tonkatalog (`AUDIO-01`).
- **Ausstehende Nachweise und Konsequenzen (C):** Prüfung individueller Stimmen-/Parser-/Codec-Lizenzen (`O-S1-05`), Messungen zu Dokumentextraktion und Provenienz (`T04`), Laufzeit-/RAM-/WER-/Zeitstempel- und Temp-Löschungsmessungen für die mehrsprachige Audio-Transkription/ASR (`T05`) sowie gesondert zu definierende und auszuführende Prüfungen für Sprachausgabe (TTS) und Video-Verarbeitungspipeline (`FE-21/52/74`, `N1.11`, `SEC-12/21/27`) und die Produktabnahme der zehn Szenarien `AT-AUDIO-01` bis `AT-AUDIO-10` (`N1.11`, `SEC-12/21/27`).
- **Betrachtete Alternativen:** Zwingender OCR-Durchlauf auf allen Text-PDFs oder obligatorischer externer Cloud-Medien-/TTS-Dienst (abgelehnt).

### ADR-0019 — Anbieterunabhängige verschlüsselte Sicherung und konsistenter Restore (TECH-O-10)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt (`DEC-49` gewahrt); Backupwerkzeug/-anbieter (B) und Restore-Proben (C) offen.
- **Kontext:** Verbindliche Anforderung `DEC-49` ([ADR-0005](#adr-0005--anbieterunabhängige-verschlüsselte-sicherung-dec-49)), Schutz vor Verlust oder Kompromittierung des Primäranbieters ([S2](spec/S2-datenmigration.md), [S3.6](spec/S3-inbetriebnahme.md#s36-unabhängige-sicherung-und-nachgewiesener-restore)).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Verschlüsselte Sicherungen unabhängig vom primären Hostinganbieter; getrennte Verwaltung der Wiederherstellungsschlüssel; gesicherte Konsistenz zwischen PostgreSQL-Datenbank, geschützten Dateien und aktuellem Lösch-/Widerrufskontrollstand; verbindlich zu testende Wiederherstellungen (Restores). Es ist noch kein Backupwerkzeug und kein Backupanbieter endgültig ausgewählt. `DEC-49` bleibt uneingeschränkt erhalten.
- **Offene technische Unterentscheidungen (B):** Konkretes Sicherungswerkzeug (z. B. `restic`, `Borg`), konkreter unabhängiger EU-Speicheranbieter (`O-S3-02`, z. B. Cloudflare R2 EU, Hetzner Storage Box, Scaleway Object Storage, Backblaze B2 EU je nach gewähltem Primärhost), RPO/RTO- und Übungsfrequenz je Datenklasse (`O-S3-06`, `O-S2-06/11`), endliche Aufbewahrung und Nichtwiederbelebung (`O-S3-07`, `O-S2-08`) sowie Append-only-/Lock- und Schlüsselverwaltungsverfahren (`O-S3-11`, `O-S2-02`).
- **Ausstehende Nachweise und Konsequenzen (C):** Vertrags-/EU-Verifikation des Backupziels (`O-S3-02/10`), Nachweis getrennter Schreib-/Löschrechte und praktische Restore-Übung auf isolierter Zielumgebung einschließlich Nichtwiederbelebung gelöschter Daten (`T07`, `AT-S2-26..33`, `AT-S3-06..09`, `REL-S20/Q20`).
- **Betrachtete Alternativen:** Sicherung ausschließlich beim Primärhoster oder unverschlüsselte Objektablage (durch `DEC-49` ausgeschlossen).

### ADR-0020 — Transaktionale Kommunikation, unabhängige Domain/DNS und V1-Postfachausschluss (TECH-O-11)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt (`FE-56` gewahrt); Mail-/Registrar-/Push-Auswahl (B) und Zustellnachweise (C) offen.
- **Kontext:** Zuverlässiger E-Mail-OTP- und Sicherheitsversand (`NB-05`, `SEC-01/03`), Hinweise (`NB-09`, `UC-65`) und der in Mission 19 bestätigte V1-Ausschluss jeglicher Postfachlektüre (`FE-56`).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Zuverlässige transaktionale E-Mails für OTP und Sicherheitsereignisse; unabhängig vom Hostinganbieter kontrollierte Domain; einfache DNS-Verwaltung mit Möglichkeit zur Dienstbündelung nur bei nachgewiesenem realem Vorteil; persistente interne In-App-Benachrichtigungen mit austauschbaren Push-/E-Mail-Transportadaptern; optionale und ausdrücklich autorisierte externe Integrationen. `FE-56` bleibt strikt gewahrt: **keinerlei Lesen, Überwachen oder Synchronisieren von E-Mail-Postfächern in V1**.
- **Offene technische Unterentscheidungen (B):** Auswahl des transaktionalen E-Mail-Dienstes (SMTP/API) und der konkreten Web-Push-/Benachrichtigungstransporte (`O-S1-03`), Auswahl des Domainregistrars/DNS-Betreibers sowie Bounce-/Rate-Limit-Regeln (`O-S3-08/12/13`).
- **Ausstehende Nachweise und Konsequenzen (C):** Verifikation von Zustellbarkeit (`SPF`/`DKIM`/`DMARC`), Annahme-/Zustellnachweisen ohne Postfach-Leserecht (`O-S1-03`, `AT-S1-10`), Timeout-/Wirkungsprüfung und Deduplizierung ohne unkontrollierte Wiederholung (`AT-S1-14`), Datenschutz/EU-Bedingungen (`O-S3-10`) sowie Quoten/Preisen (`T06`, `T08`, `O-S3-08/12/13`).
- **Betrachtete Alternativen:** Kopplung der Domainkontrolle an einen einzelnen Compute-Host oder Einführung eines E-Mail-Postfachimports in V1 (abgelehnt).

### ADR-0021 — Querschnittsentscheidung: Kontrollierte Multi-Provider-Austauschbarkeit und Fallback-Grenzen

- **Datum:** 23.10.2026 · **Status:** Querschnitts-Architekturprinzip (A) durch Projektinhaber bestätigt; adapterspezifische Fallbackregeln (B) und Idempotenz-/Fehlernachweise (C) offen.
- **Kontext:** Externe und lokale Dienste für E-Mail, KI-Inferenz, OCR, Transkription (ASR), Sprachausgabe (TTS) und Benachrichtigungen unterliegen Quoten-, Ausfall-, Lizenz- und Datenschutzgrenzen (`S1`, `S2`, `S3`, `N1`, `N2`, `REL-Q01..Q09`).
- **Entscheidung (A — Bestätigtes Architekturprinzip):**
  1. **Drei strikt getrennte Betriebsarten:** Die Architektur unterscheidet durchgehend zwischen **(1) geplantem Anbieterwechsel** (bewusster Austausch eines Adapters oder Dienstanbieters nach Vertrags-, Datenschutz-, Lizenz- und Kostenprüfung), **(2) kontrollierter Migration von Daten oder Diensten** (geplante Daten-/Dienstmigration und Wiederherstellung gemäß `S2`/`S3`; **keine naive Anbieterrotation** auf die primäre PostgreSQL-Datenbank, private Schlüssel oder das vollständige Primärhosting) und **(3) sicherem automatischem Fallback für eine einzelne Operation** (ausschließlich für austauschbare Adapter wie E-Mail-Versand, KI-Modelle, OCR, ASR, TTS und Benachrichtigungstransporte).
  2. **Strenge Fallback-Bedingungen:** Ein automatischer Fallback für eine einzelne Operation auf einen Zweitanbieter ist **nur** zulässig, wenn er technisch sicher, vertraglich erlaubt und vollständig konform mit den Datenschutz-, Schutzstufen- und Einwilligungsregeln (`SEC-08/10/20`, `DM-51/64/66`, `DLG-59`, `N2.16`) ist.
  3. **Idempotenz und Deduplizierung:** Doppelte Ausführungen und doppelte fachliche Wirkungen sind durch geeignete Operationskennungen, Zustandsverfolgung, Deduplizierung und Idempotenzprüfungen zu verhindern (`AT-S1-14`, `AT-S3-14`).
  4. **Striktes Kosten-, Lizenz- und Quotenschutzgesetz:** Niemals automatische Ausgaben, kostenpflichtige Fallbacks oder Tarif-Upgrades auslösen; niemals Beschränkungen kostenloser Tarife (Free Tiers) durch Mehrfachkonten oder unzulässige Rotation umgehen.
  5. **Ehrliche Degradation bei Quotenende:** Es wird nicht versprochen, dass eine wesentliche kontingentabhängige Funktion nach Erschöpfung ihres Kontingents weiterläuft: Ist ein erlaubtes Kontingent erschöpft oder kein zulässiger Fallback verfügbar, stoppt oder degradiert die unmittelbar betroffene Funktion sauber mit verständlicher Meldung (`AT-S3-18`, `REL-Q04/Q06`), während unabhängige Anwendungsbereiche (Lesen, Bearbeiten, Exportieren und Löschen vorhandener eigener Daten) nutzbar bleiben.
- **Offene technische Unterentscheidungen (B):** Konkrete Idempotenzschlüssel, Circuit-Breaker-/Retry-Parameter und erlaubte Anbieterpaare je Adaptertyp.
- **Ausstehende Nachweise und Konsequenzen (C):** Negativ- und Abbruchtests für Quota-Erschöpfung, Providerausfall, Verbot stillen Drittanbieterwechsels und Verhinderung doppelter Zustellung/Analyse (`AT-S1-14`, `AT-S3-14`, `AT-S3-18`, `AT-AUDIO-07/09`, `REL-Q01..Q09`).
- **Betrachtete Alternativen:** Unkontrolliertes Multi-Cloud-Datenbank-Clustering, Umgehung von Free-Tier-Limits oder stillschweigendes Ausweichen auf kostenpflichtige/unautorisierte Dritt-APIs (abgelehnt).

### ADR-0022 — Leistungsziele, RPO/RTO/SLO, Quoten und 20-EUR-Untersuchungsrahmen (TECH-O-12)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; konkrete Schwellenwerte (B) und Mess-/Lastnachweise (C) offen.
- **Kontext:** Qualitätsprofile `NFR-01..25` in [N1](spec/N1-nichtfunktional.md), Betriebsgates in [S3](spec/S3-inbetriebnahme.md) und persönlicher Qualitätsfokus aus [ADR-0006](#adr-0006--persönlicher-qualitätsfokus-und-vergleichsrahmen-aus-mission-7).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Lasten, Latenzen, Verfügbarkeit, Warteschlangen und Ressourcenverbrauch werden systematisch gemessen. Bezifferte Zielwerte für **RPO, RTO und SLO** werden vor dem Produktivstart verbindlich festgelegt (`O-S3-06`, `O-S3-08`). Aufbewahrungsfristen (Retention) werden differenziert nach Datenkategorien geregelt (`O-S3-07`, `O-S2-08`); faire Quoten und Limits gelten pro Konto (`O-S3-08`, `O-S3-12`). Für die persönliche Phase gilt ein indikativer Orientierungsrahmen von **20 EUR brutto/Monat ohne jede Ausgabenautorisierung**; persönliche Erprobung und spätere öffentliche V1-Öffnung werden strikt unterschieden.
- **Offene technische Unterentscheidungen (B):** Konkrete Zahlenwerte für Antwortzeiten, Verfügbarkeit, Queue-Tiefen, Kontokontingente und Alarme (`O-S3-08`), RPO/RTO je Datenklasse (`O-S3-06`, `O-S2-06/11`), endliche Retentionsdauern (`O-S3-07`, `O-S2-08`) sowie Kosten-/Verbrauchsgrenzen (`O-S3-12`).
- **Ausstehende Nachweise und Konsequenzen (C):** Ausführung der Benchmark- und Lastprotokolle (`T01`–`T09`), Verifikation realer Anbieterpreise und Nachweis der harten Kosten-/Quotensperren (`N1.10`, `S3.6/14`, `O-S3-06..08/12`, `REL-Q01..Q05`).
- **Betrachtete Alternativen:** Freie Erfindung ungemessener SLA-/Latenzgarantien oder Gleichsetzung eines persönlichen Einzeltests mit öffentlicher Multiuser-V1-Kapazität (abgelehnt).

### ADR-0023 — Vollständiges Lizenz-, Artefakt-, Datenschutz- und Kommerzialisierungsinventar (TECH-O-13)

- **Datum:** 23.10.2026 · **Status:** Architekturprinzip (A) durch Projektinhaber bestätigt; Einzelprüfungen konkreter Artefakte/Verträge (B/C) vor Einführung offen.
- **Kontext:** Einsatz von Open-Source-Paketen, Sprach-/KI-Modellen, Stimmen, Tonassets und externen Diensten unter `NFR-05/25`, `SEC-23/24/26`, `O-S1-05`, `O-S3-10/12` und `REL-S18/A13/A14`.
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Vollständiges Inventar für jede Komponente, Abhängigkeit, jedes Modell, Gewicht, jede Stimme und jedes Asset mit Version, Herkunft (Provenienz), Lizenz und Vertragsbedingungen (`O-S1-05`, `REL-S18`, `REL-A14`). Bevorzugung permissiver Lizenzen ohne automatischen Pauschal-Ausschluss anderer kompatibler Open-Source-Lizenzen (z. B. LGPL/GPL-3.0 in isolierten Prozessen nach Einzelfallprüfung). Verbindliche Prüfung der DSGVO-Rollen, Rechtsgrundlagen, Verarbeitungsregionen, Drittlandtransfers und Unterauftragsverarbeiter (`O-S3-10`, `SEC-26`) sowie der späteren kommerziellen Nutzbarkeit und Tarifgrenzen (`O-S3-12`) anhand der tatsächlich eingesetzten Komponenten.
- **Offene technische Unterentscheidungen (B):** Freigabe konkreter Modellgewichte, TTS-Stimmenkarten (`DE`/`FR`/`EN`), PDF-/Medienbibliotheken, Tonassets (`O-S1-05`) und Auftragsverarbeitungsverträge (`O-S3-10`).
- **Ausstehende Nachweise und Konsequenzen (C):** Lückenlose Lizenz-/Hash-/SBOM- und Lieferkettenprüfung vor Aufnahme neuer Artefakte (`O-S1-05`, `REL-S18`, `REL-A13`, `REL-A14`) sowie datenschutzrechtliche und tarifliche Vertragsprüfung vor jeder externen Anbindung (`O-S3-10`, `O-S3-12`, `SEC-23/24/26`).
- **Betrachtete Alternativen:** Ableitung von Modell- oder Stimmenrechten allein aus dem Repository-Code-Lizenzetikett (abgelehnt).

### ADR-0024 — PACE-Berechtigungsmodell und Freigabevorbehalt vor V1-Entwicklung (TECH-O-14)

- **Datum:** 23.10.2026 · **Status:** Architektur- und Governanceprinzip (A) durch Projektinhaber bestätigt; Einzelmandate je Folgemission (B/C) gesondert zu erteilen.
- **Kontext:** Kontrollierte Zusammenarbeit mehrerer KI-Entwicklungsagenten (Codex, Antigravity, Claude) an Spezifikation, Architektur und isolierten Prototypen (`AGENTS.md`, [WORKFLOW.md](ai/WORKFLOW.md), `SEC-18/23/24`).
- **Entscheidung (A — Bestätigtes Architekturprinzip):** Verbindliche Nutzung der fünf kanonischen PACE-Modi aus [WORKFLOW.md](ai/WORKFLOW.md): **`READ_ONLY`**, **`DRAFT`**, **`EDIT`**, **`COMMIT_PUSH`** und **`MERGE_DEPLOY`** (vereinfachte Kurzschreibweisen einzelner Aufgabenbriefe wie `EDIT/DRAFT`, `COMMIT/PUSH/PR` oder `TEST_CLOUD/DEPLOY` begründen keine konkurrierende PACE-Nomenklatur). Dabei werden sechs Befugnisebenen strikt unterschieden: **(1)** Vorbereitung ohne Änderung am Repository (`READ_ONLY` und `DRAFT`, wobei `DRAFT` die Erstellung von Entwürfen außerhalb des Repositories erlaubt), **(2)** autorisierte lokale Änderung im Arbeitsbaum (`EDIT`), **(3)** Veröffentlichung auf einem Arbeits- oder Prüfzweig (`COMMIT_PUSH`), **(4)** gesonderte ausdrückliche Autorisierung zur Ausführung eines Cloud-Tests, **(5)** gesonderte ausdrückliche Autorisierung für ein Deployment und **(6)** gesonderte ausdrückliche Autorisierung für einen Merge nach `main` (`MERGE_DEPLOY` nur mit expliziter menschlicher Freigabe). Ein PACE-Modus impliziert niemals automatisch eine sensible Operation außerhalb des genehmigten Missionsumfangs; Paketinstallationen, große Downloads (insbesondere Modellgewichte), Cloud-Tests, Ausgaben und sicherheitskritische Aktionen bedürfen stets einer gesonderten expliziten Freigabe. **Kein automatischer Merge nach `main`.** Die formale Eigentümervalidierung der Spezifikation und der manuelle Merge gehen dem offiziellen Start der V1-Produktentwicklung voraus.
- **Offene technische Unterentscheidungen (B):** Konkrete Einzelbeauftragung für lokale Benchmarkläufe (`T01`–`T09`), spätere CI-Runner/Actions-Pins (`REL-A13`), Branch-Protection-Regeln und gestapelte Review-Branches bei Bedarf.
- **Ausstehende Nachweise und Konsequenzen (C):** Formale Eigentümerabnahme der Siedersleben-Spezifikation (`Zur Prüfung` → `Freigegeben`), gesondert genehmigte Ausführungen von `T01`–`T09` und manueller Merge nach `main`.
- **Betrachtete Alternativen:** Unbeschränkte autonome Agentenausführung mit impliziten Installations-, Cloud- oder Merge-Rechten (abgelehnt).
