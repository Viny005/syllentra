# Offene Entscheidungen des Entwicklungsökosystems

**Version:** 0.2 · **Stand:** 23.10.2026 · **Status:** Empfohlen / Zur Entscheidung

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

## 4. Vorbereitete Identitätsentscheidungen aus Mission 13 (R1 und R4)

Die folgenden zwei Punkte betreffen fachliche Frist- und Aufbewahrungsregeln des lokalen Identitätsprototyps ([identity.py](../../prototypes/backend/src/syllentra_backend/identity.py)). Gemäß Auftrag Mission 13 wurden sie **nicht** eigenmächtig im Anwendungscode geändert, sondern durch Grenz- und Charakterisierungstests ([test_mission12_audit.py](../../prototypes/backend/tests/test_mission12_audit.py)) abgesichert und zur Entscheidung durch den Projektinhaber aufbereitet:

| Risiko / Gegenstand | Heutiger Prototypzustand (beibehalten) | Untersuchte Optionen | Empfehlung (Zur Entscheidung) | Betroffene Quellen / Tests |
|---|---|---|---|---|
| **R1 — Kopplung von Geräteablauf (7d) und Offline-Recoverycode-Ablauf (7d)** | Sowohl `devices.expires_at` als auch `recovery_codes.expires_at` betragen `clock() + 7 Tage`. Nach >7 Tagen ohne Anmeldung oder Recovery-Rotation sind Gerät **und** persönlicher Offlinecode gleichzeitig abgelaufen; selbst mit gültigem Passwort, E-Mail-OTP und Offlinecode ist keine Anmeldung oder Wiederherstellung mehr möglich. | **Option R1-A (Empfohlen):** Persönlichen Offline-Recoverycode als langlebigen Einmalnachweis (z. B. 90–365 Tage oder bis Verbrauch/Rotation) von der 7-Tage-Gerätefrist entkoppeln.<br>**Option R1-B:** Bei erfolgreichem Login eines verifizierten Kontos nach Ablauf aller Geräte einen zweistufigen Re-Autorisierungspfad (Passwort + E-Mail-OTP + unverbrauchter Recoverycode) erlauben.<br>**Option R1-C:** Status quo (7d/7d) nur für kurzlebige synthetische Lokalproben beibehalten. | **Option R1-A** für die nächste Identitätstranche freigeben, sobald die sichere reale Offlinecode-Ausgabe (TECH-O-05/06, SEC-05) festgelegt ist. | [identity.py](../../prototypes/backend/src/syllentra_backend/identity.py), [IDENTITY_ARCHITECTURE.md](IDENTITY_ARCHITECTURE.md), `test_inactivity_over_7_days_characterizes_r1_recovery_and_device_lockout`, `test_r1_and_r4_boundary_and_decision_readiness` |
| **R4 — Unbegrenzte Aufbewahrung unverifizierter `pending`-Konten** | `clean()` löscht abgelaufene `identity_challenges` nach >1 Stunde, lässt aber Konten mit `verification = 'pending'` dauerhaft in `accounts`. Eine spätere Registrierung derselben Adresse mit anderem Passwort erhält dauerhaft nur eine Fake-Challenge (kein OTP). | **Option R4-A (Empfohlen):** Unverifizierte `pending`-Konten ohne aktive/kürzlich abgelaufene Challenge nach einer festen Frist (z. B. 24 Stunden, analog zu `clean()`) vor neuer Registrierung kontrolliert bereinigen oder überschreiben.<br>**Option R4-B:** Nach Ablauf der ursprünglichen Challenge (z. B. >24h) eine Neuinitialisierung von `pending`-Konten mit neuem Passwort + neuem E-Mail-OTP zulassen.<br>**Option R4-C:** Status quo für geschlossene synthetische Lokalproben beibehalten. | **Option R4-A** (24-Stunden-Ablauf für unverifizierte `pending`-Konten ohne Sitzung/Daten) durch den Projektinhaber bestätigen. | [identity.py](../../prototypes/backend/src/syllentra_backend/identity.py), [IDENTITY_PROTOTYPE_REVIEW.md](IDENTITY_PROTOTYPE_REVIEW.md), `test_old_pending_account_blocks_different_password_and_allows_same_password_restart`, `test_r1_and_r4_boundary_and_decision_readiness` |
