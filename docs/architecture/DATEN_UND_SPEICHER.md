# Datenbank, Suche und Dateispeicher

**Version:** 0.2 · **Stand:** 23.10.2026 · **Status:** Architekturprinzipien (A) in Mission 21 bestätigt; technische Unterentscheidungen (B) und Nachweise (C) offen

## 1. Ausgangspunkt und Alternativen

[D1](../spec/D1-datenmodell.md) enthält 78 fachliche Entitäten und 31 Invarianten; keine mechanische Tabelle-pro-Entität-Entscheidung. Beziehungen zwischen Konto, Semester, Modul, Projekt, Sitzung, Beleg, Gespräch und Quelle sprechen für Transaktionen und referenzielle Integrität. Herkunft, Revision und Schutzklasse müssen überall nachvollziehbar bleiben.

| Kandidat | Nutzen | Risiken / Urteil zur Entscheidung |
|---|---|---|
| PostgreSQL | Relationen/Fremdschlüssel, atomare Transaktionen, JSONB für variable Metadaten, Volltext/Indizes, optional RLS und pgvector in einer Datenhaltung | Eigene Konfiguration, Updates, Backup/PITR und Restore nötig; PostgreSQL-Lizenz aus offizieller Quelle gelesen. **Empfohlene Basis**, unterstützte Major-/Patchfassung vor Auswahl bestätigen. |
| SQLite | Wenig Betrieb für isolierten Prototyp, transaktional und portabel | Begrenzter paralleler Schreibbetrieb, prozess-/dateibasierte Zugriffssicherung, Multiuser-/Job-/Restoreanforderungen schwieriger; keine Cloud-V1-Standardempfehlung. Aktuelle Lizenz-/Supportquelle nicht verifiziert. |
| MariaDB | Etablierter relationaler Kandidat | RLS-/Vektor-/JSON-/Volltextanforderungen konkret vergleichen; zusätzliches Know-how ohne belegten Vorteil hier nicht gerechtfertigt. Lizenz/Version noch nicht verifiziert. |
| Dokumentdatenbank / MongoDB | Flexible Dokumentstrukturen | Relationen/Invarianten/Mehrdatensatzmigration komplexer; editionsabhängige Lizenzbedingungen nicht pauschal „Open Source“. Kein Bedarf für zusätzliche Primärdatenbank belegt. |
| Managed PostgreSQL | Betreiber entlastet von Teilen des DBbetriebs, gleicher relationaler Kern | Mindestkosten, Extension-/RLS-/Backup-/Superusergrenzen, EU-Region und unabhängiger Restore prüfen; eigenes Providerbackup erfüllt DEC-49 allein nicht. |

Quellen und Grenzen: [QUELLEN](QUELLEN.md). PostgreSQL-Hauptwebsite war blockiert; ein gelesenes `master/configure.ac` ist kein freigegebener stabiler Produktionszweig und kein Beleg für den Supportzeitraum.

## 2. Mandantentrennung und Konsistenz

Eigentümer/Konto auf Daten, Beziehungen, Quellen, Ableitungen, Jobs und Indexeinträgen durchsetzen. Kontobezogene Eindeutigkeit und Referenzen verhindern nicht nur fremde Zeilen, sondern fremde Verknüpfungen. Serverseitige Autorisierung bleibt Pflicht. RLS als zusätzliche Grenze prüfen; Superuser, Tabellenbesitzer, BYPASSRLS und Connection-Pooling-/Sessionvariablen können Schutz aushebeln. Keine App mit unbeschränkter DBrolle betreiben; FORCE-RLS-/Rollenmodell und A/B-Negativtests passend prüfen. RLS wird nicht als bereits implementiert behauptet.

Geschäftsänderung und benötigter Job-/Outboxeintrag möglichst konsistent abschließen; Worker mit begrenzter Lease, Versuchszahl und Deduplizierung ausführen. Vor Wirkung Rechte/Flag/Entzug/Quelle erneut prüfen, unbekannte externe Wirkung zuerst abgleichen. Eine PostgreSQL-gestützte Queue ist eine zu testende Vereinfachung, kein selbst gebautes universelles Brokersystem. Redis/Valkey erst bei belegtem Bedarf; Lizenz pro Version prüfen. Valkey-Quelllizenz gelesen, Redis-Lizenzdatei gelesen, keine Gleichsetzung aller Redis-Versionen mit BSD.

## 3. pgvector gegenüber separater Vektordatenbank

| Aspekt | PostgreSQL + optionale pgvector-Extension | Separate Vektordatenbank, z. B. Qdrant |
|---|---|---|
| Betriebs-/Providerzahl | Keine zweite Datenbank, gemeinsamer Rechte-/Lösch-/Backupkontext | Zusätzlicher Prozess/Speicher/Update-/Restorepfad, ggf. weiterer Anbieter |
| Suche | Für überprüfbare V1-Bestände exakte Suche bzw. später HNSW/IVFFlat prüfen; Hybrid mit Volltext | Spezialisierte Such-/Verteilfunktionen bei nachgewiesen großem Bedarf |
| Isolation | Kontofilter, RLS und Quellschutz auch auf Embeddings; kein globaler ungefilterter Trefferabruf | ACL-/Tenantfilter an jeder Operation und konsistente Rückvalidierung im Backend |
| Recall / Last | ANN-Filter können Trefferzahl/Recall reduzieren; offizielles README beschreibt iterative Scans ab 0.8.0. Kein Verzicht auf Filter für mehr Treffer. | Payloadfilter/Recall separat messen, Source-of-Truth-Abgleich erforderlich |
| Datenlebenszyklus | Transaktionen/Versionen besser bündelbar; Vektorindex trotzdem eigener Schutz-/Löschgegenstand | DB-/Indexverzug und Wiederbelebung aus unabhängigem Restore eigens verhindern |
| Lizenz | pgvector PostgreSQL-Lizenz gelesen; README verwendet Installationstag 0.8.7, kein daraus bewiesener aktueller Supportstatus | Qdrant Apache-2.0-Quelllizenz gelesen; konkrete Release-/Cloudbedingungen offen |

**Empfehlung:** Zunächst PostgreSQL-Volltext + strukturierte Filter. Embeddings nur bei gemessenem Retrievalgewinn; dann pgvector mit eigenem Qualitäts-/Rechte-/Ressourcennachweis. Eine separate Vektordatenbank braucht einen ADR mit belegtem Vorteil. Konversationshistorie und pädagogisches Langzeitgedächtnis bleiben fachlich getrennt; „alle Chats als Vektorarchiv“ ist keine Memorystrategie.

## 4. Dokumente, Sicherungen und Migration

Binäre PDFs/Medien/Archive bevorzugt als versionierte geschützte Dateien oder Objektblobs, Metadaten/Beziehungen in PostgreSQL. Für einen kleinen zentralen Betrieb ist ein autorisiert angebundenes Dateiverzeichnis auf verschlüsseltem Volume ein Kandidat; S3-kompatibler Objektspeicher verbessert spätere Skalierung, benötigt aber weitere ACL-/Region-/Kosten-/Restoreprüfung. Pfade/Objektkennungen sind keine Autorisierung; Zugriff nur nach Serverprüfung, temporäre Downloadberechtigungen eng und endlich.

Kein großes Primärbackup als persönliches Exportpaket anbieten. DB-Transaktionsstand, Objektversionen, Konfigurationsfassung und aktueller Lösch-/Entzugskontrollstand müssen zusammen rekonstruierbar sein. restic auf laufende DBdateien allein liefert keinen konsistenten PostgreSQL-Restore: geeigneter Dump oder physische Sicherung mit korrektem WAL-/Konsistenzverfahren erforderlich. RPO bestimmt später Dump-/WAL-Bedarf; Snapshot, Replikat und unabhängiges Backup sind verschieden.

Schema-/Dateiformat-/Embeddingversionen mit Migration, Trockenlauf, altem PWA-Client, Abbruch und Rückweg nach [S2](../spec/S2-datenmigration.md) und [S3](../spec/S3-inbetriebnahme.md) prüfen. Embeddings neu berechnen darf keine gelöschten Quellen reaktivieren. Dokumentenschlüssel bleiben persönlich; Backend besitzt keine privaten Klartextschlüssel.


## 5. Vom Projektinhaber bestätigte Architekturprinzipien aus Mission 21 (TECH-O-04, TECH-O-08, TECH-O-10 und Multi-Provider-Grenze)

Am 23.10.2026 hat der Projektinhaber die folgenden Daten-, Retrieval- und Sicherungsprinzipien bestätigt ([ADR-0013](../ARCHITECTURE_DECISIONS.md#adr-0013--datenhaltung-geschützter-dateispeicher-volltextsuche-und-postgresql-queue-tech-o-04), [ADR-0017](../ARCHITECTURE_DECISIONS.md#adr-0017--quellenbasiertes-rag-volltext-referenz-und-strukturiertes-pädagogisches-gedächtnis-tech-o-08), [ADR-0019](../ARCHITECTURE_DECISIONS.md#adr-0019--anbieterunabhängige-verschlüsselte-sicherung-und-konsistenter-restore-tech-o-10), [ADR-0021](../ARCHITECTURE_DECISIONS.md#adr-0021--querschnittsentscheidung-kontrollierte-multi-provider-austauschbarkeit-und-fallback-grenzen)):

| Bezug | A. Bestätigtes Architekturprinzip | B. Offene technische Unterentscheidungen | C. Ausstehende Nachweise |
|---|---|---|---|
| **TECH-O-04 — Daten, Suche und Queue** | **PostgreSQL** ist die primäre Datenbank; große Dateien nutzen einen getrennten geschützten Speicher; die **PostgreSQL-Volltextsuche** bildet die initiale Referenz; der Einsatz von `pgvector` hängt von Testergebnissen ab; eine **PostgreSQL-Aufgabenwarteschlange (Task-Queue)** wird vor der Auswahl einer zusätzlichen Queue-Technologie evaluiert. | Konkrete PostgreSQL-Major-/Patchversion, Dateispeichervariante (verschlüsseltes Volume vs. S3-kompatibler EU-Objektspeicher), `pgvector`-Aktivierung, PG-Queue-Schema und RLS-/Rollenhärtung. | Qualitäts-/Latenzvergleich Volltext vs. `pgvector` (`T03`, `T04`), Durchsatz-/Sperrverhalten der PG-Queue (`T01`, `T09`) und konsistenter DB-plus-Dateispeicher-Restore (`T07`). |
| **TECH-O-08 — RAG und Gedächtnis** | RAG stützt sich auf überprüfbare Quellen; PostgreSQL-Volltext als initiale Referenz; `pgvector` und Embeddings nur bei nachgewiesenem Mehrwert; strukturiertes pädagogisches Gedächtnis getrennt von der Konversationshistorie; strikte Datenisolation jedes einzelnen Kontos. | Chunking-/Zitierstrategie, eventuelles mehrsprachiges Embeddingmodell (`E5`, `BGE-M3`, `Qwen3-Embedding`) und Reindexierungsregeln. | Messbarer Retrievalgewinn gegenüber Volltext (`T03`, `T04`), A/B-Isolations- und Lösch-/Nichtwiederbelebungstests auf Suchindizes (`T09`, `REL-S04/Q16`). |
| **TECH-O-10 — Sicherungen (DEC-49)** | Verschlüsselte Sicherungen unabhängig vom primären Hostinganbieter (`DEC-49`); getrennte Verwaltung der Wiederherstellungsschlüssel; Konsistenz zwischen PostgreSQL und Dateien; Restores verbindlich zu testen; noch kein Backupwerkzeug oder -anbieter ausgewählt. | Konkretes Sicherungswerkzeug (`restic`, `Borg`), unabhängiger EU-Speicheranbieter (R2-EU, Storage Box, Scaleway Object Storage, B2 EU je Primärhost) und Append-only-/Schlüsselrotationsverfahren. | Vertrags-/EU-Prüfung des Backupziels, Nachweis getrennter Schreib-/Löschrechte und praktische Restore-Proben einschließlich Nichtwiederbelebung gelöschter Inhalte (`T07`, `AT-S3-06..09`, `REL-S20/Q20`). |
| **Querschnitt — Keine naive Rotation** | Keine naive Anbieterrotation auf PostgreSQL, private Schlüssel oder das gesamte Primärhosting anwenden; Austauschbarkeit betrifft klar abgegrenzte Adapter, nicht die relationale Wahrheitsquelle. | — | Konsistenz- und Integritätsnachweise bei Migration/Restore nach [S2](../spec/S2-datenmigration.md) und [S3](../spec/S3-inbetriebnahme.md). |
