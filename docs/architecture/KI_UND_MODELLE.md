# KI, Modelle und nachzuweisende Kapazität

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Ergebnis und Evidenzklassen

**Ein vollständiger mehrbenutzerfähiger KI-Betrieb auf kostenlos zugeteilter CPU-Hardware ist nicht nachgewiesen.** Kleine quantisierte Modelle plus begrenzte asynchrone Warteschlange sind prüfbare Kandidaten, keine V1-Leistungszusage. Kein Modell wurde geladen oder benchmarked. A: offizielle gelesene technische-/Lizenzquelle; B: eigene transparent bezeichnete Kapazitätsrechnung; C: nicht verifizierte Artefakt-/Leistungs-/Vertragsannahme. [Quellen](QUELLEN.md), Abruf 22.10.2026.

## 2. Inferenzmotoren

| Motor | Beleg / Lizenz | ARM64 / Hardware | Abwägung |
|---|---|---|---|
| llama.cpp | MIT gelesen; Quantisierung und CPU/GPU-Mischbetrieb offiziell dokumentiert | ARM/NEON grundsätzlich unterstützt; Apple Metal ist kein Linux-Ampere-Benchmark. Konkretes GGUF, Build und Architektur testen. | **Empfohlener erster CPU-Kandidat**: wenige Bausteine, kontrollierter Modellserver hinter Backend; keine öffentliche Tool-/Inference-API |
| Ollama | MIT gelesen, einfache Modellverwaltung und kompatible Schnittstellen | Linux-/Modell-/Beschleunigerpaket auf konkretem ARM64 prüfen; Modellkarte/Lizenz bleibt getrennt | Bequemer Betriebskandidat; Modellnachladen, Speicherresidenz, öffentliche Erreichbarkeit und unautorisierter Download müssen begrenzt werden |
| vLLM | Apache-2.0 gelesen; offizielles README nennt GPUtypen und x86/ARM/PowerPC-CPUunterstützung | Nicht pauschal GPU-only. Build-/Kernel-/Modellsupport und Speicherbedarf je Backend prüfen. | Für belegten höheren Durchsatz/Batches oder GPUwachstum interessant, kein nachgewiesener Vorteil auf knapper Gratis-CPU |

Kein Server-/Bibliothekslizenztext autorisiert automatisch Modellgewichte, Sprachstimmen oder Trainingsdaten. Quantisierte Drittartefakte brauchen zusätzlich Provenienz, Integrität und passende Gewichtslizenz.

## 3. Modellkandidaten und individuelle Lizenzgrenzen

| Konkreter Kandidat | Lizenzbefund am Abrufdatum | Plausible Nutzung / Grenze |
|---|---|---|
| Qwen3-1.7B | Offizielles Qwen3-README erklärt seine Open-Weight-Modelle Apache-2.0; dieses Modell ist dort benannt. Konkrete Checkpoint-LICENSE/Quantisierung noch nicht direkt verifiziert, Modellhost 403. | Kleine Kurzantwort-/Extraktionsbaseline, keine zugesicherte universitäre Korrektheit; Multilingualität fachlich DE/FR/EN prüfen |
| Qwen3-4B-Instruct-2507 | Veröffentlichung und Gewichtslizenzbehauptung Apache-2.0 im offiziellen README explizit; Artefaktdatei/Hash/Lizenzbeilage noch offen | Vorrangiger fachlicher Vergleichskandidat für strukturierte Notizen/Quiz/RAG, kurze begrenzte Kontexte zuerst |
| Qwen3-8B | Im offiziellen Modellkatalog benannt, gleiche veröffentlichte Apache-2.0-Aussage; individuelle Artefaktbeilage offen | Qualitätsvergleich gegen 4B, höherer RAM-/CPUbedarf; kein kostenloser Mehrnutzer-Echtzeitbetrieb belegt |
| google/gemma-3-4b-it | Offizielle Gemmaimplementierung gefunden, konkrete Modellkarte/Lizenzbedingungen wegen 403 **nicht verifiziert**; Gemma-Gewichte nicht mit Code-Apache/MIT gleichsetzen | Nur nach individueller Bedingungs-/Kommerzialisierungsprüfung; keine Standardempfehlung für verpflichtenden V1-Kern |
| Whisper tiny / base / small, jeweils multilingual | OpenAI erklärt **Code und Modellgewichte MIT**; LICENSE gelesen. „.en“-Varianten sind kein FR-/DE-Ersatz. | ASR-Baseline mit whisper.cpp; veröffentlichte Speicherwerte und je Sprache eigene WER-/Fachbegriffstests |
| intfloat/multilingual-e5-small | Offizieller E5-Katalog identifiziert Modellfamilie; genaue Checkpointlizenz hier **nicht verifiziert**. Repositorylizenz allein unzureichend. | Kleiner Embeddingkandidat, vor Nutzung konkrete Modellkarte/Lizenz und Retrievalqualität prüfen |
| BAAI/bge-m3 | Offizielles FlagEmbedding-README beschreibt multilingualen M3; konkrete Gewichtsartefakt-LICENSE **nicht verifiziert** | Größerer mehrsprachiger Vergleichskandidat; nicht automatisch sparsamer oder besser für V1 |
| hexgrad/Kokoro-82M | Offizielles README nennt Apache-lizenzierte Gewichte; Artefakt-/Stimmenbedingungen noch offen | FR/EN-Beispiele vorhanden; **DE-Unterstützung für den konkreten Stand nicht belegt**. Kein alleiniger nachgewiesener DE/FR/EN-TTS-Kern. |
| Piper, je ausgewählte DE-/FR-/EN-Stimme | Aktuelles OHF-Piper-COPYING GPL-3.0 gelesen; **jede Stimme besitzt gesonderte Gewicht-/Datensatzbedingungen, hier nicht verifiziert** | CPU-TTS-Kandidat nur nach Stimmeninventar und Lizenzprüfung. Historische MIT-Aussage des alten Motors nicht auf heutigen Fork übertragen. |

Der frühere Qwen2.5-Repositoryaufruf führte inhaltlich zum Qwen3-README; daraus wird **keine** Lizenz für alte Qwen2.5-3B-/72B-Gewichte abgeleitet. Die individuellen noch offenen Lizenzbeilagen sind Auswahlblocker, keine stillen Freigaben. Offenheit ist nicht Lizenzfreiheit. Aktuelle genaue Modelle bleiben austauschbare Kandidaten, kein finales Modell beschlossen.

## 4. Gewichtsspeicher und realistische Koexistenz

Eigene Rechnung B: reiner Gewichtsspeicher ungefähr `Parameterzahl × Bitbreite / 8`. Bei 4 bit ergeben sich 1,7B → 0,85 GB, 4B → 2 GB, 8B → 4 GB **dezimal**, jeweils ohne Quantisierungsmetadaten, KV-Cache, Aktivierungen, Runtime und Betriebssystem. Daraus folgt keine Gesamt-RAM- oder Laufzeitzusage.

| Modellklasse / Testannahme | Vorläufiger RAM-Planungsbereich, nicht gemessen | CPU/GPU / Engpass |
|---|---|---|
| 1,7B, Q4, kurzer Kontext | 2–4 GiB insgesamt für einen Modellprozess als Messhypothese | CPU grundsätzlich Kandidat, Speicherbandbreite und Kontext/Predictlimit messen |
| 4B, Q4, kurzer Kontext | 4–8 GiB als Messhypothese | CPU-Kandidat; lange Kontexte und Parallel-KV-Cache können darüber liegen |
| 8B, Q4, kurzer Kontext | 8–14 GiB als Messhypothese | CPU möglich, aber größere Latenz/Queue wahrscheinlich; keine gemessene Tokenrate |
| whisper.cpp multilingual tiny/base/small | Offizielle Mem-Tabelle: ungefähr **273 / 388 / 852 MB**; tatsächliche Prozess-/Medienlast zusätzlich | ARM64-Image dokumentiert; keine aus A100-Whisper-Geschwindigkeiten abgeleitete OCI-Leistung |

Für eine angenommene 24-GiB-Maschine (kein bestätigtes OCI-Angebot) reservieren Modellprozess, Datenbank, API/Jobs, Authdienst, Embeddings/ASR und OS gemeinsam Speicher. Eine illustrative Summenspanne 4–8 + 2–4 + 2–4 + 1–2 + 2–4 + 2 GiB ergibt **13–24 GiB**, noch ohne hohe Parallelitätsreserve. Das sind Planungsannahmen, keine Messwerte und keine Mindestproduktanforderungen. Bei 4 OCPU teilen sich ASR, OCR, DB und LLM dieselbe knappe Rechenleistung; RAM-Passung beweist keine brauchbare Mehrnutzerlatenz. Modelle nicht unkontrolliert gleichzeitig laden; faire Queue/Residenz-/Abbruchregel und Ressourcenreservierung messen.

## 5. Aufgabenspezifische Ausführung und Nachweise

Alle RAM-/CPUwerte ohne Quellenkennzeichnung sind **vorläufige Messhypothesen**, keine bestätigten Kapazitätsgrenzen. „Ohne GPU möglich“ ist keine Geschwindigkeitszusage. Serverhardware muss zentral funktionieren; lokales Gerät bleibt freiwillig und tatsächlich unterstützungsabhängig.

| Aufgabe | Ort / Hardware / RAM und CPU | GPU, Durchsatz und Latenz | Güteprüfung / Sprachen | Lizenz / Kosten / Datenschutz |
|---|---|---|---|---|
| Dialog, strukturierte Notizen, Erklärungen, Übungen/Quiz | Zentraler Server, llama.cpp mit Qwen3-1.7B/4B als erste Kandidaten; 2–8 GiB Modellhypothese, 1–4 CPU-Threads als Testbudget | GPU nicht konzeptionell zwingend, für höhere Parallelität ggf. erforderlich; Token/s und erste/volle Antwort **nicht verifiziert** | Quellen-/JSON-/Aufgaben-/Korrektheitsrubrik, unbeantwortbare Fragen; DE/FR/EN jeweils bewerten; strukturvalide Ausgabe ist kein fachlicher Beweis | Qwen-Lizenzstatus Abschnitt 3; keine Lizenzgebühr als Prämisse nach Prüfung, Hardware kostet; minimaler zulässiger Kontext, kein kontofremder Prompt |
| Embeddings und RAG | Server, kleines multilinguales E5 als offener Kandidat; grobe 0,5–2 GiB Testreserve für kleine Variante, 1–2 CPU-Threads als Testbudget mit Batching; PostgreSQL/optional pgvector | Keine GPU vorausgesetzt; Indexaufbau/Recall und Queryzeit **nicht verifiziert** | Quellenpassagen, Recall/Ranking, Filter und Zitate gegen Referenzkorpus; alle drei Sprachen, missverständliche/gesperrte Quellen | Gewichtslizenz offen; zusätzliche DB-/Speicher-/Reindexkosten; Embeddings erben Quellschutz, keine ungefilterte globale Retrievalsuche |
| PDF/Text/Tabellen/OCR | Isolierter Serverworker, zunächst Textparser; Tesseract für Rasterseiten, grobe 0,5–2 GiB Testreserve und 1–2 CPU-Threads je begrenztem Job | CPU möglich; Seiten/min und Formelerkennung **nicht verifiziert**, große Raster/Archive begrenzen | Passagen-/Seiten-/Tabellenabgleich, OCRfehler und Unsicherheit; DE/FR/EN-Sprachdaten prüfen | Tesseract Apache-2.0 gelesen; PyMuPDF-COPYING gesonderte Copyleft-/Kommerzbedingungen, nicht still permissiv; jede Parser-/Sprachdatenlizenz prüfen; SSRF/aktive Inhalte nie ausführen |
| Audio-ASR | Zentraler begrenzter whisper.cpp-Worker; tiny/base/small-RAMwerte aus Abschnitt 4, Audiodatei/Decoder zusätzlich, 1–4 CPU-Threads als Testbudget; lokal nur optional | GPU optional; Realtime-Faktor, Queue und lange Vorlesung **nicht verifiziert** | WER, Fachwörter, Zeitmarken/Segmentgrenzen und Quellenbezug je DE/FR/EN; kein erfundenes Timestamping | Whisper MIT; Audio-/Transkript-/Speicherarbeit kostet; temporäre Kopien nach Abschluss/Fehler/Abbruch bereinigen, dauerhafte Notiz eigenständig geschützt |
| TTS | Optional Gerät/OS bei tatsächlich geeigneter Stimme oder Server mit geprüfter Piper-/Kokoro-Stimme; grobe 0,5–2 GiB Testreserve, 1–2 CPU-Threads als Testbudget | GPU nicht vorausgesetzt, erstes Audio/Realtime-Faktor **nicht verifiziert** | Verständlichkeit/Fachwörter, Unterbrechung/Replay, DE/FR/EN je Stimme; Kokoro-DE-Lücke beachten | Motor und Stimme getrennt lizenzieren; Textfallback; kein Mikrofonrecht zum Hören, kein stiller externer Sprachdienst |
| Video | Server: begrenztes Demux/Audio-ASR plus selektive Folienbilder/OCR; grobe 1–4 GiB Worker-Testreserve, abhängig von Auflösung, 1–4 CPU-Threads als Testbudget | CPU-Basis möglich, vollständiges multimodales LLM nicht Gratis-V1-Annahme; Dauer/Framebudget **nicht verifiziert** | Audio-/Bild-/Zeitbezüge getrennt, fehlende visuelle Analyse ehrlich anzeigen; Sprachprüfung wie ASR/OCR | FFmpeg-Lizenz konfigurations-/codecabhängig (LGPL/GPL und mögliche weitere Rechte); keine freie Gesamtlizenz aus Motorname; temporäre Frames/Spuren schützen/löschen |
| Pädagogisches Langzeitgedächtnis | Zentrale strukturierte Daten/Belege, nicht zwingend LLM; geteiltes DB-/Index-/CPUbudget statt eigener großer Modellinstanz | Keine GPU nötig für CRUD/Regeln; Abruf-/Aktualisierungszeit messen | Bestätigt/manuell/KI-geschätzt, Korrektur, Herkunft, demonstrierte Kompetenz und Nichtwiederbelebung; DE/FR/EN-Felder | PostgreSQL-/ggf. Modelllizenz; Speicherkosten; Historie getrennt von Memory, exportier-/korrigier-/löschbar, konto-/quellgeschützt |
| Agenten/Tools und Modellrouting | Serverregistrierte erlaubte Werkzeuge, feste Schemas, Operationsbindung und Rechte; 1 CPU-Thread als Orchestrierungshypothese plus vorhandener Modellprozess statt zusätzlichem Agentenmodell | Kein eigenes GPUerfordernis; begrenzte Schritte/Timeout/Tokenbudget; Gesamtlatenz **nicht verifiziert** | Direct/Indirect Injection, manipulierte Toolargumente, echte Bestätigung, Widerruf vor Wirkung und Deduplizierung | Keine neue Agentenframeworkpflicht; Libraries individuell prüfen; kein kostenpflichtiger Fallback, keine Tool-/Kalender-/Löschrechte aus Modelltext |

## 6. Austauschbarkeit und Schutz

Fachliche Anwendung beschreibt Aufgabe, Eingabefassung, Sprache, Quelle/Schutzklasse, aktuelle Einwilligung, strukturiertes Ergebnis, Grenzen und Fehler. Ein Adapter bindet lokal verfügbare Modell-/Motorfassung oder ausdrücklich zulässigen optionalen Anbieter. Modellkatalog enthält Gewichtslizenz, Hash, Sprach-/Hardware-/Kontextfähigkeit und gemessene Güte; „OpenAI-kompatibel“ bezeichnet ein Protokoll, keine Anbieter-/API-Berechtigung.

Retrieval begrenzt Quellen **vor** Promptaufbau auf aktuelles Konto/Objekt/Quellschutz; Ausgabe separat validieren. Fremde Dokumente/Toolausgaben sind Daten, keine Systemanweisungen. Modelle dürfen keine geheimen Credentials erhalten. Der Server prüft jedes Toolziel, Scope und Bestätigung unmittelbar vor Wirkung; Netzwerk-/SSRFgrenze unabhängig vom Modell. ChatGPT-/Claude-Abos sind kein automatischer APIzugang; Vertragsrecht hier nicht verifiziert. Sensible eigene Cloudanalyse sieht nur explizit freigegebene notwendige Ausschnitte; keine falsche E2EE-Behauptung.

## 7. Erst später zu autorisierender Messplan

Keine Gewichte herunterladen/ausführen in dieser Mission. Für spätere autorisierte Probe: vorab geprüfte Lizenzen/Hashes, echte ARM64/x86-Hardware, Basisspeicher/Netz und konkurrierende Konten; Modelle/Quantisierung/Kontext/Grenzen fixieren. Kalt-/Warmlauf, erste/volle Ausgabe, Prefill/Decode, CPU/RAM/KV, Fehler, Queue und Durchsatz erfassen; ASR-Realtime-Faktor, OCRgüte und Retrieval separat. Dann fachliche DE/FR/EN-Referenzfälle und REL-A01/05/07/18 prüfen.

Zeitrechnung nur als Sensitivität: 500 Ausgabetoken benötigen bei **hypothetischen** 1/5/20 Token/s allein 500/100/25 Sekunden Decode, plus Prefill/Queue/Netz. Keine dieser Raten wurde gemessen oder für OCI als plausibler Istwert bestätigt. Lange Antwort und mehrere gleichzeitige Nutzer verschärfen die Last. Bestätigte N1-Ziele vor Abnahmelauf vereinbaren; ohne Messung keine Zusage „Echtzeit auf Always Free“.
