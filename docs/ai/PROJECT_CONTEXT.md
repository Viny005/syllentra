# Syllentra AI — überprüfter Projektkontext

**Version:** 0.4 · **Stand:** 22.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

## Git-Snapshot und Geltung

Repository: `Viny005/syllentra` — <https://github.com/Viny005/syllentra>.
Aktueller Arbeitsbranch: `docs/spec/p1-p2-mobile-workspaces`, zugeordnet zu [PR #1](https://github.com/Viny005/syllentra/pull/1).
Am 22.10.2026 lokal, per entferntem Branch und PR-Git-Ref überprüfter Ausgangscommit dieser Konsolidierung: `f12a46881f54dccc8568d9982bba0c41564b052e`. Arbeitsbaum vor Bearbeitung sauber, PR #1 auf der öffentlichen GitHub-Seite als offen geprüft. PACE ist durch PR #2 seit `39261a5816a99f7c10c79344e5a1adc03b685d49` integriert. Der Snapshot ist eine datierte Ausgangsbasis, kein dauerhaft aktueller HEAD; bei jeder Aufgabe erneut prüfen. Endcommit/Push werden im Abschlussbericht nachgewiesen.

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
| [40-Punkte-Release-Checkliste](../quality/RELEASE_READINESS_40.md) | Zwei vom Projektinhaber am 22.10.2026 bestätigte Quellenlisten mit je 20 Prüfpunkten (REL-S01..20, REL-Q01..20); V1-Freigabekriterien, REL-Q10 Zahlung nur spätere Option. Ohne Produktnachweise. |
| [E2](../spec/E2-glossar.md), [E3](../spec/E3-pruefnachweis.md) | Begriffe sowie datierte tatsächliche Dokumentationsprüfungen; kein Produktabnahmetest. |
| [Entscheidungsmatrix](../spec/ENTSCHEIDUNGSMATRIX.md) | Aktuelle DEC-V1-/FE-21-Zuordnung und DEC-48/49, Soll-Abnahmen und verbleibende Präzisierungen; zur Prüfung. |
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

**FE-56 bleibt offen:** keine automatische Hochschulpost-/Inbox-Lesefunktion in V1. Technische Nachweise/Parameter aus S1.19 und S2.17 bleiben offen; insbesondere konkrete Provider, Verfahren für Schlüssel/Recovery, sichere PWA-/Offline-Fähigkeiten, Betriebs-/Lösch-/Backupnachweise sowie messbare Qualitäts- und Lizenznachweise. Die [Entscheidungsmatrix](../spec/ENTSCHEIDUNGSMATRIX.md) dokumentiert jetzt alle 25 DEC-V1 einschließlich ergänzter Varianten und Soll-Abnahmen; weitere fachliche Präzisierungen und der vollständige Meilensteinplan bleiben offen. Keine offenen Fragen durch Agentenannahmen schließen.

**Architektur:** ADR-Konvention vorhanden, keine finale Framework-, Datenbank-, Hostinganbieter- oder KI-Modellwahl. S3 ist geplant und nicht ausgearbeitet. DEC-48 priorisiert Oracle Cloud Infrastructure zur späteren Bewertung; Alternativen bleiben bei fehlender Eignung offen, kein Anbieter endgültig ausgewählt. DEC-49 verlangt verschlüsselte EU-Sicherung unabhängig vom Primäranbieter mit sicheren Schlüsseln/Rechten und periodischen verifizierbaren Restore-Proben. [ADR-0004/0005](../ARCHITECTURE_DECISIONS.md) halten Rahmen und offene Verfahren fest. Keine Accounts, Infrastrukturtests, Ressourcen oder Ausgaben sind autorisiert; RPO/RTO, Frequenz und Retention bleiben offen.

**Entwicklung und Tests:** Am überprüften Ausgangsstand ausschließlich Dokumentation und `.gitignore`, kein Anwendungscode, keine App-Testpipeline, keine implementierten oder getesteten Produktfunktionen. E3 dokumentiert frühere Dokumentprüfungen; sie ersetzen keine neuen Prüfungen. Die aktuelle Konsolidierung prüft Dokumentation und Bestandserhalt, keine Authentisierung, Konnektoren oder Laufzeitfunktionen.

## Sicherheits- und Kostengrenzen

Keine Geheimnisse, privaten Lernmaterialien oder personenbezogenen Echtdaten ins öffentliche Repository. Nachvollziehbare Nutzerentscheidungen, Rechte-/Kontentrennung und geschützte Dokumente sind verbindlicher Rahmen. Externe Datenverarbeitung erfordert passende ausdrückliche Freigabe. Kein verpflichtender kostenpflichtiger KI-API-Zugang; kostenlose kommerziell geeignete Software-/Modelllizenzen bevorzugen, Sicherheit erhalten.

**Untersuchungslimit für Infrastruktur: maximal 10 EUR brutto pro Monat. Keine Ausgabe genehmigt.** Dies ist ausschließlich eine Grenze für Untersuchung/Vergleich aus dem PACE-Auftrag vom 19.10.2026, keine Buchungs-, Kontoeröffnungs- oder Betriebsfreigabe. Keine kostenpflichtigen Dienste oder Infrastruktur aktivieren.

## Auftragsumfang und nächste Schritte

Mission 2 erlaubt dokumentarische Konsolidierung der DEC-V1/FE-21 und DEC-48/49, Katalog-/Referenz-/Metadatenkorrektur, tatsächliche Dokumentprüfungen sowie Commit/normalen Push auf den bestehenden Spezifikationsbranch zur Aktualisierung von PR #1. Kein Merge, `main` unverändert, keine Anwendung, kein Account, keine Infrastruktur-/Externprobe oder Ausgabe. S3 und allgemeine Finalisierung von N1/N2 sind ausdrücklich nicht Teil dieser Mission. Die 89 FE, 66 UC, 28 pädagogischen Sollfälle und 40 Release-Kontrollen bleiben erhalten, FE-56 offen. Dokumente bleiben zur Prüfung; nach Abschluss ist kein weiterer Produkt-/Architekturauftrag durch diesen Kontext erteilt.

Die Übernahme der 40 Release-Kontrollen vom 22.10.2026 bleibt als historische Kontextänderung im [Protokoll](CONTEXT_CHANGELOG.md) und in E3.18 nachvollziehbar; sie ist kein bestandener Produkttest oder Zahlungsumfang.

Arbeitsregeln: [AGENTS.md](../../AGENTS.md), [Workflow](WORKFLOW.md). Übergaben und Kontextänderungen verwenden die dort verlinkten Vorlagen und das [Protokoll](CONTEXT_CHANGELOG.md).
