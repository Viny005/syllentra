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

No final stack has been selected. The repository is intentionally documenting principles and decisions first, allowing the architecture to evolve based on research and experimentation.

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
