# Syllentra AI — Spezifikation

Dieses Verzeichnis enthält die Spezifikationsdokumente nach der Methode von Johannes Siedersleben. Die Spezifikation wird schrittweise in deutscher Sprache erarbeitet und mit dem Projektverantwortlichen validiert.

## Kurze Einführung zur Methode Siedersleben

Die Siedersleben‑Methode gliedert eine System‑Spezifikation in klar abgegrenzte Blöcke (P, F, D, B, S, N, E), die jeweils unterschiedliche Aspekte eines Systems dokumentieren: Ziele & Rahmenbedingungen, funktionale Beschreibungen, Daten und Schnittstellen, Betriebs‑ und Sicherheitsaspekte, nichtfunktionale Anforderungen sowie ergänzende Hilfsmittel wie Glossar und Leseanleitung. Ziel ist eine gut strukturierte, überprüfbare und iterativ zu füllende Spezifikation.

## Leseanleitung (E1)

1. Beginnen Sie mit P1 (Ziele und Rahmenbedingungen), um Kontext und Zweck des Systems zu verstehen.
2. Lesen Sie P2 (Architekturüberblick) für eine konzeptionelle Einordnung; beachten Sie, dass Architekturentscheidungen separat dokumentiert bleiben (siehe docs/ARCHITECTURE_DECISIONS.md).
3. Für funktionale Details folgen F1..F3: Geschäftsprozesse → Anwendungsfälle → Anwendungsfunktionen.
4. Datenbezogene Informationen finden sich in D1..D2 (Datenmodell, Datentypenverzeichnis).
5. Betriebs‑ und Interaktionsaspekte sind in B1..B3 dokumentiert; Systemintegrations‑ und Migrationsaspekte in S1..S3.
6. Nichtfunktionale Anforderungen und Querschnittskonzepte sind in N1..N2 gesammelt.
7. Das Glossar (E2) erklärt Begriffe und Abkürzungen.
8. Jedes Dokument enthält Hinweise auf Quell‑/Referenz‑Dokumente im Repo (z. B. docs/PROJECT_VISION.md).

Hinweis: Diese Leseanleitung ist im README.md des Spezifikationsverzeichnisses integriert (E1).

## Index der Spezifikationsblöcke

Für jeden Block sind Name, Rolle, aktueller Status und Pfad aufgeführt. Nicht ausgefüllte Blöcke werden als „Geplant" markiert.

- P1 — P1-ziele-rahmenbedingungen.md
  - Rolle: Ziele und Rahmenbedingungen des Projekts; Zielgruppe, Abgrenzungen und Annahmen.
  - Status: In Bearbeitung (gemeinsame Erarbeitung mit dem Projektverantwortlichen).
  - Pfad: docs/spec/P1-ziele-rahmenbedingungen.md

- P2 — P2-architekturueberblick.md
  - Rolle: Konzeptioneller Architekturüberblick (keine technischen Entscheidungen hierher kopieren).
  - Status: Geplant
  - Pfad: docs/spec/P2-architekturueberblick.md

- F1 — F1-geschaeftsprozesse.md
  - Rolle: Beschreibung der Studien-, Lern- und Verwaltungsprozesse mit Auslösern, Akteuren, Aktivitäten, Ergebnissen und fachlichen Grenzen.
  - Status: Zur Prüfung
  - Pfad: docs/spec/F1-geschaeftsprozesse.md

- F2 — F2-anwendungsfaelle.md
  - Rolle: Anwendungsfälle (Use Cases) in verständlicher Form.
  - Status: Geplant
  - Pfad: docs/spec/F2-anwendungsfaelle.md

- F3 — F3-anwendungsfunktionen.md
  - Rolle: Detaillierte Anwendungsfunktionen mit Schnittstellenreferenzen.
  - Status: Geplant
  - Pfad: docs/spec/F3-anwendungsfunktionen.md

- D1 — D1-datenmodell.md
  - Rolle: Konzeptionelles Datenmodell.
  - Status: Geplant
  - Pfad: docs/spec/D1-datenmodell.md

- D2 — D2-datentypen.md
  - Rolle: Verzeichnis der Datentypen und Strukturen.
  - Status: Geplant
  - Pfad: docs/spec/D2-datentypen.md

- B1 — B1-dialogspezifikation.md
  - Rolle: Dialog- und Interaktionsspezifikation (für Chat-/Konversationsflows etc.).
  - Status: Geplant
  - Pfad: docs/spec/B1-dialogspezifikation.md

- B2 — B2-batch.md
  - Rolle: Beschreibung geplanter Batch‑Prozesse.
  - Status: Geplant
  - Pfad: docs/spec/B2-batch.md

- B3 — B3-druckausgaben.md
  - Rolle: Vorgaben zu Druckausgaben / Reporting (falls zutreffend).
  - Status: Geplant / ggf. Nicht anwendbar (bei Nicht‑Nutzung angeben)
  - Pfad: docs/spec/B3-druckausgaben.md

- S1 — S1-nachbarsysteme.md
  - Rolle: Beschreibung angrenzender Systeme und Integrationspunkte.
  - Status: Geplant
  - Pfad: docs/spec/S1-nachbarsysteme.md

- S2 — S2-datenmigration.md
  - Rolle: Anforderungen und Verfahren zur Datenmigration.
  - Status: Geplant
  - Pfad: docs/spec/S2-datenmigration.md

- S3 — S3-inbetriebnahme.md
  - Rolle: Inbetriebnahme‑ und Rollout‑Hinweise.
  - Status: Geplant
  - Pfad: docs/spec/S3-inbetriebnahme.md

- N1 — N1-nichtfunktional.md
  - Rolle: Nichtfunktionale Anforderungen (z. B. Performance, Verfügbarkeit, Skalierbarkeit).
  - Status: Geplant
  - Pfad: docs/spec/N1-nichtfunktional.md

- N2 — N2-querschnittskonzepte.md
  - Rolle: Querschnittskonzepte (z. B. Logging, Monitoring, Sicherheitskonzepte allgemein).
  - Status: Geplant
  - Pfad: docs/spec/N2-querschnittskonzepte.md

- E1 — Leseanleitung
  - Rolle: Anleitung zum Lesen und Struktur der Spezifikation; integriert in dieses README.md.
  - Status: Fertig (als README.md im Spezifikationsverzeichnis)
  - Pfad: docs/spec/README.md

- E2 — E2-glossar.md
  - Rolle: Glossar und Abkürzungsverzeichnis.
  - Status: Geplant
  - Pfad: docs/spec/E2-glossar.md

## Statuskonventionen

In dieser Spezifikation verwenden wir folgende Statuskennzeichnungen:

- Geplant — Inhalt vorgesehen, noch nicht ausgearbeitet.
- In Bearbeitung — Der Inhalt wird aktuell erarbeitet (z. B. P1).
- Zur Prüfung — Fertig formuliert, steht zur Review durch den Projektverantwortlichen.
- Freigegeben — Validierte und freigegebene Spezifikation.
- Nicht anwendbar — Dieser Block ist für das Projekt nicht relevant; Begründung ist erforderlich.

## Trennung: Spezifikation vs. Architektur vs. Implementierung

- Spezifikation (dieses Verzeichnis): Beschreibt Anforderungen, Ziele, Prozesse, Datenmodelle und Schnittstellen auf einer konzeptionellen und prüfbaren Ebene. Keine technischen Implementierungsdetails, keine Technologieentscheidungen.
- Architektur‑Dokumente (docs/ARCHITECTURE_DECISIONS.md): Dokumentieren getroffene Architekturentscheidungen und Entscheidungsgründe. Architekturentscheidungen werden verlinkt, aber nicht in die Spezifikation hineinkopiert.
- Implementierung (Code‑Repo): Implementierungsdetails, Frameworks, Bibliotheken und Code gehören in den Quellcode und zugehörige Readmes; Verweise von der Spezifikation auf Implementierungsartefakte sind erlaubt, aber die Spezifikation bleibt die autoritative Beschreibung der Anforderungen.

## Verweise auf bestehende Dokumente

Die folgenden historischen/Quell‑Dokumente sind im Repository vorhanden und dienen als Referenzquellen:

- docs/PROJECT_VISION.md
- docs/REQUIREMENTS.md
- docs/ARCHITECTURE_DECISIONS.md
- docs/ROADMAP.md

In jedem neuen Spezifikationsdokument ist eine Sektion "Verweise" aufzunehmen, die relevante Abschnitte dieser Dateien nennt.

## Regeln für die Erstellung und Validierung von Anforderungen

- Anforderungen werden schrittweise in Zusammenarbeit mit dem Projektverantwortlichen ausgearbeitet.
- Keine Anforderung wird als verbindlich dokumentiert, bevor sie nicht explizit vom Projektverantwortlichen freigegeben wurde.
- Historische Dokumente bleiben erhalten. Spezifikationsdokumente sind die autoritativen, freigegebenen Versionen nach Validierung.

---

Datum der Erstellung dieses Dokuments: 2026-10-12
Verantwortlich: (wird bei Veröffentlichung eingetragen)

