# Ressourcenbedarf und Startkonfigurationen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Rechenbasis und gemeinsame Komponenten

Alle folgenden Reserven sind **Planungshypothesen zur Messung**, keine beobachteten Werte, zugesagten OCI-Ressourcen oder neuen V1-Produktgrenzen. Referenz: Linux ARM64/x86-CPU, kurze begrenzte Kontexte, kleine synthetische Bestände, kein GPUzwang. GiB und GB nicht vermischen; Plattenbedarf Dezimal-GB, RAM GiB. Modellgewichtstheorie aus Mission 5 bleibt `Parameter × Bit / 8` ohne Cache/Runtime.

| Komponente | RAM-Testreserve GiB | CPU-/Plattenannahme und Trennung |
|---|---|---|
| Statische PWA / HTTPS | 0,1–0,25 | 0,1–0,5 GB Artefakte; kein Node-Produktionsprozess bei statischer Vitevariante |
| Backend | 0,25–0,75 | Begrenzte Prozesse, keine CPUparser im Requestloop; Build-/Debugstände nicht mit Produktion gleichsetzen |
| PostgreSQL einschließlich Jobs/Metadaten | 0,75–1,5 | Gemeinsame transaktionale Queue als Hypothese, 1–3 GB kleiner synthetischer Bestand/WALreserve; mehr Material wächst |
| Identität | 1–2 | IdP-Testreserve; Bibliotheksvariante nicht als automatisch sichere RAMersparnis buchen |
| OS / Monitoring / Logs | 0,75–1,25 | Begrenzte Logs, ca. 2–5 GB OS plus Updates; Alarmierung/Retention nötig |
| Workersteuerung | 0,1–0,25 | Fachlicher Job-/Deduplizierungszustand in DB, kein verpflichtender Redisdienst |
| Dokumentensuche | 0,25–0,5 | Volltext/Indexcache zusätzlich berücksichtigt, Überschneidung mit DBmessung später bereinigen |
| PDF/OCR pro aktivem Job | 0,5–2 | 1–2 CPUthreads als Testbudget, temporäre Bilder/Archive begrenzen; eigene Prozess-/Dateirechte |
| Kleine Embeddings pro Modellprozess | 0,5–2 | 1–2 Threads, Token-/Batchlimit; konkrete Gewichte/Tokenizer erst nach Lizenzprüfung |
| Qwen3 1,7B / 4B / 8B, kurze Q4-Hypothese | 2–4 / 4–8 / 8–14 | 1–4 Threads pro geplantem Job; ca. 0,85 / 2 / 4 GB reine Q4-Gewichtstheorie, echte Dateien größer möglich |
| ASR / TTS | 0,5–1,5 / 0,5–2 | ASR 1–4, TTS 1–2 Threads als Testbudget; keine garantierte Realtimeleistung |
| Backupprozess | 0,25–0,75 | Scratch-/Prunereserve und Netz/IO; zusätzlich unabhängiges Ziel, keine unabhängige Sicherung auf derselben VM |

Grundbetrieb ohne aktive KI-/Medien-/Backupprozesse: **3,2–6,5 GiB** als Summe der ersten sieben Zeilen. Eigene konservative Reserven, kein Mindest-RAM einer Software behauptet. Ein separater Broker würde die Rechnung erhöhen; Jobsteuerung und Queue sind nicht zwei ungezählte Dienste.

## 2. Vier Nutzungsfälle

| Szenario | Annahme | Gleichzeitig zu reservierender RAM | CPU-/Plattenrisiko |
|---|---|---|---|
| A: ein aktiver Nutzer | Grundbetrieb + ein 1,7B-Modell, andere Medienjobs pausiert | **5,2–10,5 GiB**; mit OCR und Backup zusätzlich bis 13,25 GiB | 2–4 verfügbare CPUthreads als Testprofil; 30–50 GB lokales Startvolumen als Kapazitätshypothese inklusive OS, Modelle, 5 GB Material, Index/Temp/Updates; tatsächliche freie Bootmenge offen |
| B: wenige Konten, eine aktive KIarbeit | Grundbetrieb + ein 4B-Modell, Medien nur nacheinander | **7,2–14,5 GiB**; Backup +0,25–0,75 | 4 CPUthreads als Testprofil, Antworten der anderen Konten warten fair; 50 GB Material braucht deutlich mehr Gesamt-/Backupplatz als Szenario A |
| C: mehrere Konten mit Queue | Grundbetrieb + 4B + ein gleichzeitig erlaubter ASRjob + Backup | **7,95–16,75 GiB**; Embeddings/OCR zusätzlich nur mit Reserve oder seriell | CPUkonkurrenz kann trotz RAMpassung unbrauchbare Wartezeit erzeugen; Warteschlange begrenzen, keine reine RAM-Freigabe |
| D: parallele Inferenz | Grundbetrieb + zwei eigenständige 4B-Prozesse + Embedding + ASR + Backup | **12,45–26,75 GiB** ohne zusätzliche hohe Kontext-/Batchspitzen | Zwei Prozesse können Gewichte duplizieren. Ein geteilter Modellserver spart Gewichte, benötigt je aktivem Request KV/Workspaces; kein Nachweis, dass hypothetische 24 GiB reichen. |

Grundrechnungen schließen bestimmte zusätzliche Medienprozesse bewusst aus; solche Prozesse dürfen nicht ungeplant gleichzeitig starten. Für 8B statt 4B weitere 4–6 GiB je Prozess als Hypothesendifferenz; keine universelle Formel. Kontext-KV wächst abhängig von Architektur/Layern/KVheads/Datentyp/Tokenanzahl und parallelen Sequenzen; konkrete config noch unlesbar. Nicht aus „256K Kontext unterstützt“ auf kleine RAMlast schließen.

CPUthreads sind keine reservierten physischen Kerne oder Oracle-OCPUgarantie. Compute-, Netz- und Speicherdurchsatz müssen gemessen werden. Material-/Modell-/DB-/Index-/WAL-/Temp-/Update-/Backupscratch summieren; Monitoring soll knappen Speicher vor neuer Aufnahme melden. Bestehende zulässige Daten bleiben les-/exportier-/löschbar. Global- und Kontoquoten, CPU-/RAM-/Zeit-/Joblimits, Abbruch und sichere Wiederaufnahme schützen andere Konten.

## 3. Gemeinsame Maschine oder Trennung

Kleiner Grundbetrieb darf konzeptionell auf einer Maschine liegen, aber mit getrennten minimalen Prozess-/DB-/Dateirechten, nicht öffentlich erreichbaren Modell-/Admininternas und begrenzten untrusted Workern. Parser/Medien benötigen immer eine überprüfbare Isolationsgrenze, nicht zwangsläufig eigene bezahlte VM. Ressourcenerschöpfung, unvereinbare Kernel-/Beschleuniger-/Bibliotheksabhängigkeiten, starke Last oder strengere Schutzgrenze können eine eigene Maschine erforderlich machen. Entscheidung nach T01/T02/T04/T09. Backupziel nach DEC-49 **immer anbieterunabhängig**; Recoverykeys/aktuelle Kontrolllage auch bei Primärverlust verfügbar.

Eine tatsächlich verfügbare hypothetische 24-GiB-Instanz könnte Szenario A/B tragen, dies ist **rechnerische Möglichkeit**, keine Zuteilungs-/Latenz-/Sicherheitszusage. Ein persönlicher begrenzter Prototyp bleibt denkbar, auch wenn D oder die vollständige Multiuser-V1 nicht tragfähig sind. Kein notwendiger privater Dauer-PC und kein Ersatz fehlender Cloudkapazität durch verpflichtende Pay-API.

## 4. Progressive Aktivierung ohne Zielkürzung

| Startstufe als Vorschlag | Abhängigkeiten / Aktivierungsbeleg | Weiter vorhandenes V1-Soll |
|---|---|---|
| KI-freier Grundumfang | Verifizierte Konten, Isolation, Profil/Module/Projekte, manuelle Lernorganisation, interner Kalender, sichere Dateien, Datenkontrolle, Backup; T01/T06/T07/T09 | Generative Ziele weiterhin spezifiziert, ausgeschaltete Funktionen serverseitig unzugänglich |
| Einfache KI | Geprüfter kleiner LLM, Lizenz, Quellen-/Pädagogikrubrik, einzelner fairer Job; T02/T03, Pflichtkontrollen | Kein pauschaler Qualitätsnachweis für alle Fächer/Sprachen |
| Begrenzte Transkription | Gültige Audioquelle, ASR-Lizenz, begrenzte Dauer/Queue, T05 und nachgewiesene temporäre Bereinigung | Umfang-/Wartegrenzen offen benennen; Video/weitere Medien nicht als automatisch fertig ausgeben |
| Asynchroner Ausbau | Idempotente persistente Jobs, aktuelle Rechte/Quoten, Abbruch, ehrlicher Teilstatus | Kein unbeschränktes Hintergrundrechnen und keine Schattenarchive |
| Aufwendige Funktionen | Größere Kontexte, komplexe Videobilder, mehrere Inferenzjobs/hochwertige Stimmen nur mit ausreichenden Belegen/Kapazität | Eigentümer entscheidet nach Ergebnissen, keine bestätigte Funktion aus Ziel-V1 löschen |

Alle Stufen benötigen menschliche Umfangsfreigabe und anwendbare 46 REL-/S3-Gates; Flags allein ersetzen keine Autorisierung. 10 EUR brutto sind nur Untersuchungsgrenze, keine Ausgabe und keine nachgewiesene vollständige V1-Kostenobergrenze. [Machbarkeit](MACHBARKEITSPRUEFUNG.md), [Testplan](BENCHMARKPLAN.md), [Entscheidungsvorlage](ENTSCHEIDUNGSVORLAGE.md).
