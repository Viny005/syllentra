# Syllentra AI — überprüfter Projektkontext

**Version:** 0.1 · **Stand:** 19.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

## Git-Snapshot und Geltung

Repository: `Viny005/syllentra` — <https://github.com/Viny005/syllentra>.
Fachlicher Ausgangsbranch: `docs/spec/p1-p2-mobile-workspaces`, PR [#1](https://github.com/Viny005/syllentra/pull/1).
Am 19.10.2026 lokal und per Remote-Ref überprüfter Ausgangscommit: `0676f791c858765a005a32e2af8c8442eff9712e` (`docs(spec): integrate adaptive learning and study management decisions`). Arbeitsbaum vor PACE sauber. PACE-Arbeitsbranch: `chore/pace-workflow`, auf diesem Stand angelegt; PR-Ziel ist ausschließlich der Spezifikationsbranch. Dieser Snapshot bezeichnet die Ausgangsbasis, nicht einen dauerhaft aktuellen HEAD; bei jeder Aufgabe neu prüfen. PR-Metadatenzugriff war zuvor mit HTTP 403 beschränkt; ein Git-Ref belegt keinen offenen PR-Status.

## Ziel und Aufbau

Adaptiver Lernbegleiter für Studierende: Materialien, Audio und Gespräche mit persönlichen Lernzielen, Studienorganisation und nachvollziehbarer Lernentwicklung verbinden. Dokumentation zuerst; Spezifikation, Architektur, Implementierung und Testbelege getrennt halten. PACE beschreibt die Arbeit am Repository, keine neue Produktfunktion.

## Maßgebliche Quellen

| Quelle | Zuständigkeit und Status |
|---|---|
| [Spezifikationsindex / E1](../spec/README.md) | Einstieg, Versions-/Statusübersicht und Siedersleben-Konvention. Alle ausgearbeiteten Dokumente weiterhin Zur Prüfung durch den Projektinhaber. |
| [P1](../spec/P1-ziele-rahmenbedingungen.md), [P2](../spec/P2-architekturueberblick.md) | Ziele/Rahmen, Systemkontext und Nachbarsysteme; keine technische Stackentscheidung. |
| [F1](../spec/F1-geschaeftsprozesse.md), [F2](../spec/F2-anwendungsfaelle.md), [F3](../spec/F3-anwendungsfunktionen.md) | Prozesse, 66 Anwendungsfälle und fachliche Funktionen. |
| [D1](../spec/D1-datenmodell.md), [D2](../spec/D2-datentypen.md) | Fachliche Daten, Beziehungen, Invarianten und Datentypen. |
| [B1](../spec/B1-dialogspezifikation.md), [B2](../spec/B2-batch.md), [B3](../spec/B3-druckausgaben.md) | Dialoge, Hintergrundverarbeitung und Ausgaben. |
| [S1](../spec/S1-nachbarsysteme.md), [S2](../spec/S2-datenmigration.md) | Nachbarverträge, kanonische 89 FE in S1.18.1, Migration/Export/Wiederherstellung. |
| [N1](../spec/N1-nichtfunktional.md), [N2](../spec/N2-querschnittskonzepte.md) | Qualitätsanforderungen und Schutzkonzepte als begrenzte Prüfentwürfe. |
| [E2](../spec/E2-glossar.md), [E3](../spec/E3-pruefnachweis.md) | Begriffe sowie datierte tatsächliche Dokumentationsprüfungen; kein Produktabnahmetest. |
| [Entwicklungszuordnungen](../spec/ENTWICKLUNGSPLAN.md) | Bestätigter Teilstand, kein vollständiger freigegebener Meilensteinplan. |
| [ADR-Konvention](../ARCHITECTURE_DECISIONS.md), [Roadmap](../ROADMAP.md) | Noch keine finale Stackwahl; historische Forschungs-/Entwicklungsphasen. |
| [Vision](../PROJECT_VISION.md), [ursprüngliche Anforderungen](../REQUIREMENTS.md) | Historische Grundlagen; bei Abweichungen aktuelle bestätigte Entscheidungen und deren Quellenstatus prüfen. |
| [PACE-Auftrag im Kontextprotokoll](CONTEXT_CHANGELOG.md) | Quelle der neuen Arbeitskonvention und des Untersuchungslimits; keine Änderung fachlicher FE/UC. |

## Bestätigter fachlicher Rahmen

Die Zusammenfassung ersetzt keine Primärquelle: S1.18.1 enthält **89 FE, davon 88 bestätigt und FE-56 offen**. F2 enthält **66 UC**. Dokumente sind weiterhin Prüfentwürfe; bestätigte Einzelentscheidungen sind keine Gesamtabnahme.

- V1: voneinander isolierte Benutzerkonten, installierbare PWA, eigene zentrale EU-Cloud ohne erforderlichen privaten Dauer-PC. Getrennte Administration, serverseitige Rechteprüfung; Adminrolle allein erlaubt kein Lesen privater Inhalte (S1/N2).
- Kalender außen strikt lesend; interner Kalender getrennt. Importe und KI-Kalenderänderungen vor Speicherung bestätigen; manuelles direktes Speichern verlangt keine künstliche zweite Bestätigung (P1/P2/S1).
- Sensible Dokumente besonders schützen; private Schlüssel nicht im Klartext an Backend/Admins. Gesondert freigegebene minimale temporäre Klartextverarbeitung ist keine durchgängige Ende-zu-Ende-Verschlüsselung (S1/S2/N2).
- Nur geeignete ausdrücklich freigegebene externe Integrationen; URLs berechtigen weder zur Installation noch Ausführung unbekannter Konnektoren. Anbieterabonnement bedeutet kein automatisches API-Recht (S1).
- Vier zuletzt integrierte Entscheidungen L-08/L-04/L-09/L-02 betreffen adaptive Wiederholung mit kontrollierter Reihenfolgeänderung, persönliche Erinnerungsregeln (UC-65), Studienvorgabenabgleich (UC-66) und optionalen ablenkungsarmen Lernmodus. Inhalt, Grenzen und Belege: E3.11–16 und Entwicklungszuordnungen.

## Offene Entscheidungen und Status

**FE-56 bleibt offen:** keine automatische Hochschulpost-/Inbox-Lesefunktion in V1. Technische Nachweise/Parameter aus S1.19 und S2.17 bleiben offen; insbesondere konkrete Provider, Verfahren für Schlüssel/Recovery, sichere PWA-/Offline-Fähigkeiten, Betriebs-/Lösch-/Backupnachweise sowie messbare Qualitäts- und Lizenznachweise. Vollständige Harmonisierung der übrigen DEC-V1-Punkte und vollständiger Meilensteinplan sind nicht abgeschlossen. Keine offenen Fragen durch Agentenannahmen schließen.

**Architektur:** ADR-Konvention vorhanden, keine finale Framework-, Datenbank-, Hostinganbieter- oder KI-Modellwahl. S3 ist geplant und nicht ausgearbeitet. Zentrale EU-Cloud ist fachlicher Rahmen, kein ausgewählter Anbieter.

**Entwicklung und Tests:** Am überprüften Ausgangsstand ausschließlich Dokumentation und `.gitignore`, kein Anwendungscode, keine App-Testpipeline, keine implementierten oder getesteten Produktfunktionen. E3 dokumentiert frühere Dokumentprüfungen; sie ersetzen keine neuen Prüfungen. Die PACE-Mission prüft Dokumentation und unveränderte Spezifikation, keine Authentisierung, Konnektoren oder Laufzeitfunktionen.

## Sicherheits- und Kostengrenzen

Keine Geheimnisse, privaten Lernmaterialien oder personenbezogenen Echtdaten ins öffentliche Repository. Nachvollziehbare Nutzerentscheidungen, Rechte-/Kontentrennung und geschützte Dokumente sind verbindlicher Rahmen. Externe Datenverarbeitung erfordert passende ausdrückliche Freigabe. Kein verpflichtender kostenpflichtiger KI-API-Zugang; kostenlose kommerziell geeignete Software-/Modelllizenzen bevorzugen, Sicherheit erhalten.

**Untersuchungslimit für Infrastruktur: maximal 10 EUR brutto pro Monat. Keine Ausgabe genehmigt.** Dies ist ausschließlich eine Grenze für Untersuchung/Vergleich aus dem PACE-Auftrag vom 19.10.2026, keine Buchungs-, Kontoeröffnungs- oder Betriebsfreigabe. Keine kostenpflichtigen Dienste oder Infrastruktur aktivieren.

## Nächster freigegebener Umfang

Aktuell ausschließlich PACE einführen: Agentenanweisungen, Workflow, Projektkontext, Vorlagen, Kontextprotokoll und optional knapper README-Link; separater Branch, Commit/Push und separate Draft-PR gegen den Spezifikationsbranch soweit Zugang vorhanden. Keine Änderung an 89 FE, 66 UC oder bestehenden Spezifikationen, kein Anwendungscode, keine Sicherheitsimplementierung, Technologieentscheidung, Merge oder Deployment. Nach Abschluss ist kein weiterer Produkt-/Architektur-/Implementierungsauftrag allein durch diesen Kontext freigegeben; nächste konkrete Aufgabe vom Projektinhaber abwarten. PR #1 bleibt ohne Merge.

Arbeitsregeln: [AGENTS.md](../../AGENTS.md), [Workflow](WORKFLOW.md). Übergaben und Kontextänderungen verwenden die dort verlinkten Vorlagen und das [Protokoll](CONTEXT_CHANGELOG.md).
