# KI-APIs — Bedingungen, Gratisgrenzen und offene Belege

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Befund, Quellenstand und Grenzen

Abrufdatum **22.10.2026**. Nur öffentliche Dokumente/SDKquellen gelesen, keine Konten, Keys oder Inferenzaufrufe. „Nicht verifiziert“ ist kein Nein/Null und keine Zusage alter bekannter Quoten. Webseiten von Groq, Gemini, Mistral und Cerebras sowie mehrere Vertragsseiten waren auch beim erlaubten Wiederholungsabruf 403; öffentliche offizielle SDKs bestätigen Integrationsmöglichkeiten, keine aktuellen Preise, Modellverfügbarkeit oder Datenschutzverträge. [Quellenregister](../development/SOURCES.md) bewahrt URLs, Revisionen und Befundgrenzen.

Belastbar aus offiziellen Dokumentationsquellen: Cloudflare Workers AI veröffentlicht 10.000 Neurons/Tag und kostenpflichtige Überschreitung nur im passenden Bezahlmodell; OpenRouter veröffentlicht kontingentierte Freevarianten; Hugging Face veröffentlicht **keine** Inference-Providers-Credits für Free-Nutzer mehr. Alle Angebote können sich ändern, sind keine kostenlose Produktionsgarantie und erfüllen nicht automatisch EU-/Verarbeitungsregeln.

## 2. Kriterienmatrix — Groq, Gemini, Workers AI und OpenRouter

Die Nummern entsprechen den 17 verlangten Prüfkriterien. Für jeden nicht belegten Vertrags-/Tarifpunkt vor Nutzung erneut Herstellerbeleg einholen. DE/FR/EN-Fachgüte muss modell- und aufgabenbezogen gemessen werden; ein mehrsprachiger Produktname ist kein Testnachweis.

| Nr. / Kriterium | GroqCloud | Google Gemini API | Cloudflare Workers AI | OpenRouter |
|---|---|---|---|---|
| 1 API / Modelle | Offizielles `groq-python` belegt API; aktueller Livekatalog nicht verifiziert | Offizielles `python-genai` belegt Gemini-/Vertex-SDKwege; aktueller Katalog nicht verifiziert | Dokumentation listet u. a. Qwen3-30B-A3B, Llama, Whisper und Embeddings; einige Modelle paid-only | APIübersicht belegt kompatible Chat-/Streamingwege und wechselnde Provider; konkreter Livekatalog nicht abgerufen |
| 2 Free tier | Nicht aktuell verifiziert | Nicht aktuell verifiziert; AI Studio, API und Vertex nicht gleichsetzen | 10.000 Neurons/Tag auf Workers Free/Paid laut Quelle, nicht alle Modelle eingeschlossen | Modellvarianten `:free`, veränderliche Verfügbarkeit, kein Produktions-SLA belegt |
| 3 Tages-/Monatsquote | Nicht verifiziert | Nicht verifiziert | Tagesreset 00:00 UTC; kein daraus zugesagtes Monatsguthaben | Unter Creditschwelle 50/Tag; ab mindestens 10 gekauften Credits laut Tabelle 1.000/Tag; Implementierungsdetail gewährt höhere Grenze bereits einen Credit darunter. Keine Beschaffung ableiten; Monatsquote nicht belegt |
| 4 Minute | Nicht verifiziert | Nicht verifiziert | Textgenerierung Standard 300 Requests/min; paid-only Modelle 20/min bzw. 50/min mit passenden vorausbezahlten Gatewaycredits; spezifische Modelllimits beachten | 20/min für beschränkte Freevarianten laut offizieller generierter Konstantendatei; Ausnahmen/BYOK separat |
| 5 Anmeldung | SDK benötigt APIcredential, Konto erforderlich; Registrierung nicht getestet | APIprojekt/-credential nötig; kein Konto angelegt | Cloudflarekonto/zulässiges Credential für REST oder Workerbinding | Account/APIkey notwendig; keines erzeugt |
| 6 Bankkarte | Nicht verifiziert | Nicht verifiziert | Free-Registrierungs-/Kartenvoraussetzungen nicht verifiziert; einige Modelle verlangen bezahlte Billingmethode | Zahlungs-/Kartenvoraussetzung für reinen Freizugang nicht verifiziert; Creditkauf getrennte kostenpflichtige Handlung |
| 7 Geografie | Nicht verifiziert | Nicht verifiziert | Konkrete erlaubte Länder und Inferenzregion nicht hier verifiziert | Regionale Vertrags-/Nutzungsbedingungen offen; Business/Enterprise-EU-Routing ist gesonderte Funktion |
| 8 Kommerzielle Nutzung | Vertrag und einzelne Modelle offen | Vertrag/Tier/Modelle offen | Modellbedingungen gesondert; reine Preisquelle ist kein Nutzungsrecht | Je Modell/Upstreamanbieter und Dienstvertrag; keine pauschale OSSlizenz |
| 9 Vertraulichkeit | Nicht verifiziert | Nicht verifiziert, Free/Paid nicht gleichsetzen | Hersteller: Standardinferenz nach Verarbeitung keine Inhaltsaufbewahrung, begrenzte Rechts-/Sicherheitsausnahmen; stateful Features/Logs anders | Hersteller: Prompt-/Responsepersistenz grundsätzlich opt-in, Metadaten gespeichert; Upstreambedingungen zusätzlich |
| 10 Training | Nicht verifiziert | Nicht verifiziert | Hersteller: kein Training mit Customer Content; keine Übertragung auf Gateway-Upstreams | OpenRouter-I/O-Nutzung opt-in; Upstreamtrainingseinstellungen für Free/Paid getrennt und Anbieterfilter nötig |
| 11 Residenz | Nicht verifiziert | Nicht verifiziert; Vertexregion kein Beweis für Gemini-Free-API | Keine EU-Inferenzgarantie aus R2-EU-Speicher ableiten; Gesamtverarbeitung/Verträge offen | EU-/US-In-region laut Quelle Business/Enterprise, nicht als kostenlose EUgarantie behandeln; konkrete Vertragskette offen |
| 12 Überschreitung | Aktueller Preis/Stop offen | Aktueller Preis/Stop offen | Freegrenze blockiert; Workers Paid darüber 0,011 USD/1.000 Neurons laut Quelle, weitere Worker-/Gateway-/Steuerkosten prüfen | Paidvarianten/Upstream-/Aufladepreise nicht aktuell verifiziert; kein automatischer Wechsel oder Aufladen |
| 13 Limitsteuerung | SDKfehler/Timeout, eigene harte serverseitige Quoten; Dienstlimit offen | Eigene Quote/Budgetguard; Dienstlimit offen | Tagesverbrauch und Modelllimit berücksichtigen, Freefehler nicht durch Upgrade umgehen | 402/429 und streaminterne Fehler dokumentiert; automatische Upstreamfallbacks explizit beschränken, Rechte vor Retry erneut prüfen |
| 14 Tools / Streaming | SDKstütze, konkrete Modellfähigkeiten separat prüfen | SDK belegt Streaming/Toolfunktionen, je Modell prüfen | OpenAI-Kompatibilitätsquelle und aufgabenspezifische Modelle; Featureparität/Tools je Modell prüfen | API-/Streamingdoku; toolfähiges Modell/Provider erforderlich, APIkompatibilität keine vollständige Gleichheit |
| 15 DE / FR / EN | Keine Fachmessung | Keine Fachmessung | Mehrsprachige Modellkandidaten, keine Fachmessung | Abhängig vom gewählten Modell; keine Fachmessung |
| 16 Sensible Inhalte aus | In Syllentra standardmäßig gesperrt, nicht als getestete Anbieterfunktion ausgeben | Ebenso; nur freigegebene Kategorien/Aufgabe | Ebenso; „no training“ ersetzt keine Datenfreigabe | Ebenso; providerinterne Routingweitergabe ausdrücklich begrenzen |
| 17 Vertragsänderung | Aktuelle Terms/Retention/DPA offen, vor Nutzung neu prüfen | Aktuelle Terms/Tier/Training/Region offen | Quelltext ist Herstellerdoku, kein abgeschlossenes DPA; Änderungen/Modelrechte beobachten | OpenRouter plus Upstreamterms, Opt-ins/Modelle/Quoten veränderlich; kein Aborecht aus Consumerchat ableiten |

## 3. Kriterienmatrix — Hugging Face, Mistral und Cerebras

Cerebras als glaubwürdige zusätzliche kompatible APIoption untersucht; kein weiterer Anbieter ohne Zweck in die Auswahl aufgenommen.

| Nr. / Kriterium | Hugging Face Inference Providers | Mistral API | Cerebras Inference |
|---|---|---|---|
| 1 API / Modelle | Offizielle Preisquelle: 200+ Modelle über wechselnde Anbieter, Router/SDK/BYOK; keine Fixauswahl | Offizielles `mistralai/client-python` belegt SDK; aktueller Dienstkatalog offen | Offizielles Cloud-SDK belegt API; aktuelle Modelle offen |
| 2 Free tier | Laut Quelle Free-Nutzer ohne Credits; Kauf oder Upgrade erforderlich. Kein dauerhaft freies Inferenzbudget annehmen | Aktuell nicht verifiziert | Aktuell nicht verifiziert |
| 3 Tag / Monat | PRO 2 USD/Monat, Team/Enterprise 2 USD je Seat als allgemeine Computecredits laut Quelle; Abokosten zusätzlich, Free keine; keine Tagesgarantie | Nicht verifiziert | Nicht verifiziert |
| 4 Minute | Provider-/Modellabhängig, keine allgemeine bestätigte Zahl | Nicht verifiziert | Nicht verifiziert |
| 5 Anmeldung | HFkonto/Token; BYOK braucht Providerkonto | Konto/Key erforderlich, nicht erzeugt | Konto/Key erforderlich, nicht erzeugt |
| 6 Bankkarte | Genaue Kauf-/Kartenvoraussetzung nicht verifiziert | Nicht verifiziert | Nicht verifiziert |
| 7 Geografie | Routingdienst plus Zielproviderbedingungen, Länder/Regionen offen | Nicht verifiziert | Nicht verifiziert |
| 8 Kommerziell | Modell und Upstreamvertrag getrennt prüfen, HF-Hublizenz reicht nicht | Modell-/APIvertrag offen; offene Modellgewichte sind kein freier APIvertrag | Modell-/APIvertrag offen |
| 9 Vertraulichkeit | Hersteller: keine Request-/Responsebodies beim Routing gespeichert; Debuglogs bis 30 Tage ohne Nutzerdaten/Tokens, Upstreampolicy bleibt maßgeblich | Nicht verifiziert | Nicht verifiziert |
| 10 Training | HF erklärt keine Nutzerdatenspeicherung für Training; Zielanbieter gesondert | Nicht verifiziert | Nicht verifiziert |
| 11 Residenz | Keine allgemeine EUgarantie aus HF-/Modellhostort; Zielprovider zusätzlich | Nicht verifiziert | Nicht verifiziert |
| 12 Überschreitung | Prepaidcredits/Upgrade, providerbezogene Pay-as-you-go-Kosten; aktueller Gesamtpreis offen | Nicht verifiziert | Nicht verifiziert |
| 13 Limits | Eigenes serverseitiges Request-/Budgetlimit; HF-Org-Limits editionsabhängig; BYOK andere Rechnung | Bounded Retry/Stop im Adapter, Herstellergrenzen offen | Bounded Retry/Stop im Adapter, Herstellergrenzen offen |
| 14 Tools / Streaming | Provider-/Modellabhängig, kompatibler Router dokumentiert; kein Paritätsbeweis | SDKmethoden, konkrete Fähigkeiten testen | SDKmethoden/Streaming, konkrete Fähigkeiten testen |
| 15 DE / FR / EN | Modellabhängig, keine pädagogische Messung | Keine Fachmessung; Markenherkunft kein Sprachbeleg | Keine Fachmessung |
| 16 Sensible Inhalte aus | Syllentra-Ausgangssperre; BYOK ist keine zusätzliche Datenfreigabe | Gleiche serverseitige Ausgangssperre | Gleiche serverseitige Ausgangssperre |
| 17 Terms / Änderung | HF + Provider + Modellrechte, kostenlose Guthabenannahmen veraltet; DPA/Region/Retention vor Verwendung prüfen | Aktuelle Bedingungen nicht verifiziert | Aktuelle Bedingungen nicht verifiziert |

## 4. Schlussfolgerung für Syllentra

**Keine externe API als verpflichtende Grundlage empfehlen.** Lokale austauschbare Inferenz bleibt erste vertraulichkeitsorientierte Prüfbasis gemäß früherer Studie, kein Leistungsversprechen. Cloudflare und OpenRouter sind nach dokumentierten Gratisgrenzen zuerst weiter prüfbare optionale APIkandidaten für synthetische/unvertrauliche Aufgaben, aber keine sofortige Freigabe; EU-/Vertrags-/Modell-/Datenweitergabegates bleiben offen. Groq/Gemini/Mistral/Cerebras nicht wegen unlesbarer Bedingungen als ungeeignet abwerten, sondern vor Entscheidung Nachweise nachfordern. HF ist nach neuer Quelle kein allgemeiner kostenloser Default.

Preisvergleich erst mit gleicher Last, tatsächlichen Token-/Neuron-/Modellgrößen, FX/Steuer und Abokosten. Beispiel **reine Rechnung**: 5.000 Neurons Mehrverbrauch auf berechtigtem Workers-Paidkonto → 0,055 USD Inferenzanteil, kein EURbruttogesamtpreis und kein genehmigtes Angebot. Kostenbudget für spätere Vergleiche bis **20 EUR brutto/Monat**, keine Ausgabe. Tagesfreimenge weder in garantierte Monatskapazität noch pädagogische Qualität umrechnen.

Vor jedem späteren APIversuch: exakte Modell-ID/Revision, Dienst-/Datenvertrag, geographische Nutzbarkeit, Retention/Training/Subprozessoren, Kostenlimit und konkreter künstlicher Testumfang autorisieren. Kein ChatGPT-/Claude-Abonnement als APIberechtigung betrachten. Keine privaten Universitätsdokumente standardmäßig nach außen. [Adaptergrenzen](AI_PROVIDER_ADAPTERS.md) und [bestehende T01–T09](../architecture/BENCHMARKPLAN.md) bleiben verbindlich; kein APItest ausgeführt.
