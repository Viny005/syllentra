# Dokumente, Retrieval und pädagogische Evaluation

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Kleine überprüfbare Verarbeitungskette

Geschütztes Original → isolierte Extraktion → normalisierte Passagen mit Quelle/Revision/Seite oder Audiozeit → konto-/zweckgefilterte Suche → minimale belegte Kontextauswahl → KIantwort → validierte Zitate und überprüfte Lernnotiz. Keine ausführbaren Anweisungen aus Dokumenten, keine externe Recherche oder Inferenz als Nebenwirkung. Historie der Unterhaltung ist nicht das pädagogische Langzeitgedächtnis.

| Baustein | Abwägung / Lizenzbefund | Zeitpunkt / einfachere Alternative |
|---|---|---|
| PDF.js | Apache-2.0; Viewer/Textauswahl/Seitenquellen im Client, kein universeller serverseitiger RAGparser | Bei Dokumentansicht; zugängliche Textalternative/aktive Inhalte/Worker prüfen |
| pypdf | BSD-3-Clause gelesen, Pythontext-/Metadatenextraktion, keine garantierte Tabellen-/OCRgüte | Erster permissiver Text-PDFvergleich nach Stackfreigabe; mit problematischen Seiten prüfen |
| PyMuPDF | Frühere offizielle Quelle: AGPL-3.0 bzw. kommerzielle Lizenz, keine pauschal permissive Webappintegration | Nur nach konkreter Copyleft-/Distributions-/Betriebsprüfung; pypdf/PDF.js einfacher lizenzierbare Kandidaten, kein pauschales Rechtsgutachten |
| Tesseract / OCRalternative | Früher verifizierter Apache-2.0-Motor; Sprachdaten/Modellartefakte extra prüfen | Erst bei Scanbedarf, CPU-/Sandbox-/Formelqualität messen; keine unnötige OCR für Text-PDF |
| sentence-transformers | Apache-2.0-Code gelesen; Python/ML-/Torchabhängigkeiten beträchtlich, Gewichtslizenz getrennt | Erst nach gemessenem Mehrwert über Volltext; keine Modellgewichte geladen |
| Qwen3-Embedding-0.6B | Offizieller Modellkatalog/Herstelleraussagen aus Mission 6; individuelle Artefaktlizenz/Hash weiter offen | Kleiner multilingualer Vergleichskandidat, kein garantierter Retrievalsieg; 8B-MTEBscore nicht auf 0,6B/Pädagogik übertragen |
| PostgreSQL Full Text Search | Bestehende relationale Datenhaltung, Sprachkonfiguration und strukturierte Filter | Zuerst prüfbare Baseline mit DE/FR/EN-Konfiguration; OCR-/Synonym-/Crosslanguagegrenzen dokumentieren |
| pgvector | PostgreSQL-Lizenz, gleiche Daten-/Lösch-/Backupgrenze; ANNfilter können Recall ändern | Nur nach Retrievalgewinn, exakte Suche zunächst; keine zweite Vektordatenbank nötig |
| Reranker | Kann Hybridtreffer verbessern, zusätzliche Gewichte/RAM/Latenz/Sprach-/Lizenzprüfung | Erst nach belegtem Rankingproblem, keine konkrete unprüfbare Modellwahl; Volltext + Filter + einfaches Fusionranking zuerst |
| Zusätzliche Dokumentframeworks / Vektordienste | Mehr Loader, Netz-/Parser-/Abhängigkeitsflächen und Lifecycle | Ohne konkreten Formatzwang/Skalierungsbeleg zurückstellen; Parserports erlauben späteren Wechsel |

Textsplit nach Absatz/Überschrift/Seite statt blindem Tokenfenster; kleines begrenztes Overlap als später zu messender Parameter. Tabellen/Formeln/Abschnittsgrenzen erhalten, OCRunsicherheit kennzeichnen. Zeichen-/Tokenzählung mit tatsächlich verwendeter Modellfassung; Chunk-ID enthält Konto/Quelle/Revision/Extraktor-/Chunkerfassung. Audiosegmente mit Beginn/Ende und Quellrevision, Videoframes mit Zeitbezug. Temporäre Transkripte nach bestätigtem Lifecycle löschen; daraus übernommene geschützte Lernnotizen separat und provenancefähig erhalten.

## 2. Suche, Revisionen und Löschung

Account/Objekt/Quellschutz **vor** Suche und Promptaufbau begrenzen, abgerufene Quellen unmittelbar vor Ausgabe nochmals gegen aktuelle Rechte prüfen. Kein globales Top-k erst nachträglich filtern und dann für Recall Schutz abschalten. Hybridsuche nur mit identischem zulässigem Korpus vergleichen. Zitat verweist auf erreichbare Seite/Passage/Audiozeit und Quellrevision, nicht bloß Dateiname; fehlende Quelle offen anzeigen.

Revisionswechsel markiert Ableitungen als überprüfungsbedürftig, überschreibt keine bestätigte Notiz still. Korrektur/Export/Löschung umfasst Passagen, Vektoren, Caches, Vorschauen, Modellkontext und temporäre Dateien; endliche Logs ohne Schattenkopien. Unabhängiger Restore muss aktuellen Lösch-/Widerrufskontrollstand berücksichtigen. Index gilt als abgeleitet/reproduzierbar, darf keine gelöschten Originale wiederbeleben. [D1/D2](../spec/D1-datenmodell.md), [S2](../spec/S2-datenmigration.md), [N2](../spec/N2-querschnittskonzepte.md) bleiben Primärquellen.

## 3. Evaluation ohne Pflicht-Pay-API

| Ansatz | Nutzen / Lizenz | Grenzen / Entscheidung |
|---|---|---|
| Deterministische Referenzfälle | Eigene synthetische Quellen, Goldpassagen/Seiten/Zeiten, Schemaprüfung, A/B-/Lösch-/Injectionnegativfälle | Zuerst ohne weitere Infrastruktur; T03/T09 und neun DE/FR/EN-Starterfälle aus BENCHMARKPLAN weiterverwenden |
| Menschliches Fachreview | Faktische Richtigkeit, Lernzielpassung, verständliche Erklärung, Übungs-/Korrekturqualität | Zweite fachkundige Sicht bei kritischen Themen, Bewertungsrubrik und Dissens dokumentieren; kein behaupteter Standardscore |
| Ragas | Aktueller gelesener Quelltext **Apache-2.0**, RAGmetriken und flexible Modellanbindung | Modelljudge/Embeddings können Kosten/Datentransfer verursachen; lokale geprüfte Backends bzw. deterministische Teile, Telemetrie/Defaults vor Einsatz prüfen |
| DeepEval | Gelesene `LICENSE.md` **Apache-2.0**; Test-/LLMevalframework | Hosted Confident-AI-Angebote/Keys/Daten separat; kein Pflichtcloudjudge, mehr Abhängigkeiten. Nicht parallel zu Ragas ohne spezifischen Nutzen |
| Multilinguale Benchmarks | Identische fachliche Ziele, DE/FR/EN getrennte Auswertung | Öffentliche Benchmarklizenz und Domänenübertragbarkeit prüfen; Publisherleaderboard kein universitärer Abnahmebeleg |

Je Testfall: Frage/Lernziel, synthetische Quelle mit Goldbeleg, erwartete Antwortgrenzen/Unbeantwortbarkeit, erlaubtes Konto/Provider, Modell-/Prompt-/Parserfassung und menschliche Rubrik. Messen: Retrieval-Recall/Ranking, Zitatgenauigkeit/Quelltreue, behauptete unbelegte Fakten, Verständnis, Aufgaben-/Korrekturrichtigkeit, Sprachkonsistenz, Daten-/Rechteverletzung, Injectionabwehr, Zeit/RAM/Verbrauch. Datenschutzverletzung nicht durch guten Durchschnittsscore kompensieren.

Rubrikvorschlag 0 fehlerhaft, 1 teilweise, 2 korrekt/belegt für Fakt, Erklärung und Übung, mit begründetem menschlichem Urteil; Schwellen/Umfang vor Versuch Eigentümer bestätigen. LLMrichter kann Vorsortierung unterstützen, ist selbst fehler-/prompt-/sprachabhängig und **kein alleiniger pädagogischer Beweis**. Keine Evaluation/Modellausführung vorgenommen. T02/T03/T04/T09 bleiben geplant, fachliche Sicherheitsgates unverändert.
