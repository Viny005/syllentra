# Offene Entscheidungen des Entwicklungsökosystems

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Fortgeltung

Alle 14 [TECH-O](../architecture/OFFENE_ENTSCHEIDUNGEN.md) bleiben offen; A/B/C/D aus der [Entscheidungsvorlage](../architecture/ENTSCHEIDUNGSVORLAGE.md) ist Evidenzklasse, keine Genehmigung. Keine neue FE/UC/DEC oder konkurrierende Entscheidungsnummer. FE-56 offen; 25 DEC-V1, DEC-48/49 und 46 REL erhalten. Technische/visuelle Empfehlungen hier Empfohlen / Zur Entscheidung; Fachspezifikation weiterhin Zur Prüfung.

## 2. Vor konkreter Einführung zu entscheiden

| Gegenstand | Empfehlung / Alternativen | Benötigte Eigentümerentscheidung / Nachweis | Anschluss |
|---|---|---|---|
| Persönliche Qualität und Untersuchungsbudget | Persönlicher Nutzen zuerst, bis 20 EUR brutto/Monat künftig vergleichen | Priorität und Vergleichsrahmen bereits in Mission 7 bestätigt; reale Ausgabe weiter separat, Leistungsziele offen | TECH-O-12/14, P1/N1/ADR-0004 |
| Stack / UIbasis | React/Vite + FastAPI bleibt Prüfbasis, kleines Tailwind/shadcn/Primitivenpaket | Stack und isolierte Komponentenprobe autorisieren, Kompetenz-/Browser-/Peer-/Updateprüfung | TECH-O-03 |
| Visuelle Richtung | Ruhiges Petrol/Türkis, Hell/Dunkel, konzeptionelle Token | Gestaltung/Zielgeräte/Lesedichte, WCAG-2.2-AA-Ziel und Testmatrix bestätigen | NFR-08/19/20, REL-A16 |
| Skills / Clientkompatibilität | Drei deklarative kanonische Skills, Claude liest explizit | Echte Codex-/Claudeversion/Discovery/Invocation separat prüfen; kein automatischer Claudealias belegt | PACE, TECH-O-14 |
| Rollen / Parallelität | Ein Bearbeiter, unabhängiges lesendes Review situativ | Pro Auftrag Agentenzahl, Pfade, Toolrechte und Ressourcen erlauben | SEC-18/23/24 |
| Hook / CI / Updates | Deterministische kleine Checks, später CI; keine aktiven Hooks jetzt | Konkrete Runner, gepinnte Actions/Tools, Updateverantwortung und minimale Rechte | TECH-O-13/14, REL-A13 |
| MCP | Öffentliche Dokumente/Git vor zusätzlichen Servern | Endpoint/Tools/Lizenz/Retention/Rechte einzeln; kein Account/Server derzeit genehmigt | SEC-13/18/20/24 |
| KI-API | Optional, standardmäßig keine privaten Inhalte, kein Pflicht-Payzugang | Aktuelle Vertrags-/Regions-/Limit-/Preisnachweise und konkreter Datenscope vor Probe | TECH-O-07/13, SEC-20 |
| Adapter/RAG/Evaluation | Kleiner Port, Volltextbaseline, pgvector/Embedding nach Gütebeleg, menschliche Rubrik | Gewichts-/Parser-/Stimmenrechte, Qualität und RAM/Latenz per genehmigtem T02–T04/T09 | TECH-O-07/08/09 |
| Hosting / Backup / Auth | Bestehende OCI-/Alternativ-/Recovery-/Backupprüfung fortführen | Regionale Kapazität/Verträge/Gesamtkosten ≤20 EUR nicht nachgewiesen; keine Wahl oder Ausgabe | TECH-O-02/05/06/10/11, DEC-48/49 |
| Zahlung | Nur spätere mögliche Nutzerbeteiligung untersuchen | Neuer Fachauftrag nötig; REL-Q10 keine V1-Aktivierungsfreigabe | FE unverändert, Freigabematrix |

## 3. Wesentliche Restgefahren

Webblockaden verhindern vollständige Tarif-/Vertrags-/Normprüfung; offizielle Repositorydokumente sind Herstellerangaben, kein abgeschlossener Vertrag. Aktuelle Hauptzweigrevision beweist weder stabilen Paketstand noch garantierte Wartung. Lizenz auf oberster Ebene umfasst nicht automatisch Assets/Transitive/Gewichte/Datasets/Enterprisefunktionen. UI-/Agent-/MCPtexte sind keine durchsetzbare Schutzgrenze. 20 EUR ermöglichen einen erweiterten Vergleich, beweisen keine ausreichende CPU-/RAM-/KIleistung oder sichere vollständige V1. Keine neue Abhängigkeit installiert, kein Modell/API getestet, keine Anwendungs- oder Produktabnahme.

Entscheidungen zuerst nach [ADR-Konvention](../ARCHITECTURE_DECISIONS.md) dokumentieren, bestätigte Fachänderungen in Primärquellen, danach PACE. [Integrationsfolge](INTEGRATION_ROADMAP.md) ist Vorschlag für nächste Aufträge, kein automatischer Entwicklungsstart.
