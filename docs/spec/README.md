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

**Stand: 16.10.2026. Alle ausgearbeiteten Dokumente: Zur Prüfung durch den Projektinhaber.** S1.18.1 enthält sämtliche 89 FE-Einträge; FE-56 bleibt offen. Keine Dokumenterstellung oder Git-Aktion bedeutet fachliche Abnahme oder implementierte Funktion.

| Baustein | Version | Inhalt / Stand |
|---|---|---|
| [P1](P1-ziele-rahmenbedingungen.md) | 0.7 | Ziele, Rahmen, Mehrbenutzer-V1 und überprüfbare Erfolgskriterien. Zur Prüfung. |
| [P2](P2-architekturueberblick.md) | 0.8 | Kontext, interne/externe Grenzen, zwölf Nachbarn und Informationsklassen. Zur Prüfung. |
| [F1](F1-geschaeftsprozesse.md) | 0.4 | GP-01 bis GP-15 mit ergänzten Konten-, Import-, Integrations- und Datenkontrollabläufen. Zur Prüfung. |
| [F2](F2-anwendungsfaelle.md) | 0.3 | UC-01 bis UC-64 mit Vorbedingungen, Szenarien, Schutz und Abnahme. Zur Prüfung. |
| [F3](F3-anwendungsfunktionen.md) | 0.3 | AF-01 bis AF-36 als fachliche Prüf- und Auswahlfunktionen. Zur Prüfung. |
| [D1](D1-datenmodell.md) | 0.3 | DM-01 bis DM-74 und INV-01 bis INV-31; Eigentum, Beziehungen und Lebenszyklen. Zur Prüfung. |
| [D2](D2-datentypen.md) | 0.3 | DT-01 bis DT-90, Werte, Strukturfelder und Validierung. Zur Prüfung. |
| [B1](B1-dialogspezifikation.md) | 0.3 | DLG-01 bis DLG-65; persönliche und getrennte administrative Bedienung. Zur Prüfung. |
| [B2](B2-batch.md) | 0.3 | BAT-01 bis BAT-25; autorisierte Hintergrundverarbeitung, Wiederanlauf und Löschfolgen. Zur Prüfung. |
| [B3](B3-druckausgaben.md) | 0.3 | OUT-01 bis OUT-08; kontoisolierte Berichte und geschützte Exporte. Zur Prüfung. |
| [S1](S1-nachbarsysteme.md) | 0.2 | NB-01 bis NB-12, vollständige FE-01..FE-89-Matrix und Schnittstellen-Abnahmeszenarien. Zur Prüfung. |
| [S2](S2-datenmigration.md) | 0.1 | MIG-01 bis MIG-36, AT-S2-01 bis AT-S2-40; eigene Pakete, sichere Migration und Wiederherstellung. Zur Prüfung. |
| [N1](N1-nichtfunktional.md) | 0.2 | Begrenzter Folgeentwurf: Qualitätsanforderungen und offene Mess-/Nachweisaufgaben. Zur Prüfung. |
| [N2](N2-querschnittskonzepte.md) | 0.2 | Begrenzter Konzeptentwurf: Konten, Rechte, Schutz, Schlüssel, Audit, Löschung. Zur Prüfung. |
| [E2](E2-glossar.md) | 0.2 | Glossar mit fachlichen Begriffsgrenzen. Zur Prüfung. |
| [E3](E3-pruefnachweis.md) | 0.2 | Änderungsmatrix, Kennungsbestand und tatsächliche Dokumentationsprüfungen. Zur Prüfung. |

E1 ist als Leseanleitung in diesem README enthalten und bleibt mit dem Index zur Prüfung. [S2 — Datenmigration](S2-datenmigration.md) ist zur Prüfung ausgearbeitet. **S3 — Inbetriebnahme** bleibt geplant, ohne Link auf eine fehlende Datei; S3 übernimmt sicheren Betriebsstart und den Bootstrap des einzigen Super Admin. Die vollständige Harmonisierung von DEC-V1-01 bis DEC-V1-25 bleibt ein gesonderter Vorgang; S2 berücksichtigt ihre Daten-/Schutzgrenzen, ohne neue Lernalgorithmen oder UI-Funktionen vollständig einzuführen. Die technische Architektur wird separat erarbeitet.

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

