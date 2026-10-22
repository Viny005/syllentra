# Machbarkeitsprüfung — nachgewiesen, bedingt und offen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Auftrag und Evidenz

Mission 6, Ausgangscommit `9eb07f3fdc7c3b7c73b762af7fbfe761e9341807`; der zuerst übermittelte Auftrag endete in Abschnitt 12, die nachgereichten Abschnitte 12–16 sind Teil des Auftrags. Ausschließlich Dokumentation und öffentliche Recherche. Keine Installation, Cloudressource, Registrierung, Modellausführung, Benchmark oder Ausgabe. Die neun Studien aus Mission 5 bleiben Grundlage, keine Wiederholung ihrer hypothetischen Rangfolge als Messergebnis.

[Neue Quellen](QUELLEN.md#6-nachrecherche-mission-6) wurden am 22.10.2026 abgefragt: offizielle Websites, dokumentierte öffentliche Modellmetadaten-APIs und offizielle Repositories. Auch nach erneuter autorisierter Anfrage Netzwerk-403 bei Host-/Modellhost-/Vertragsseiten. Zwei veraltete Keycloak-Quellpfade ergaben 404; öffentliche Verzeichnisansicht lieferte die korrekten Dokumente. Keine geschützte API aufgerufen, Authentisierung umgangen oder Zugangsdaten angefordert. Öffentliches SDKschema liefert keine aktuellen Preise.

**Belegklassen:** dokumentierte Herstellerfunktion; Vertrag/Angebot; veröffentlichter Herstellerbenchmark; unabhängige Evaluation; eigene theoretische Rechnung; eigener tatsächlich ausgeführter Test. In dieser Lieferung keine eigenen technischen Tests und keine neu verifizierte unabhängige Modellevaluation. Fehlende Fakten bleiben **nicht verifiziert**. Dokumentierte Funktion ist nicht gleich integrierte, getestete oder genehmigte Syllentra-Funktion.

## 2. Oracle nach DEC-48: fünf getrennte Kategorien

| Prüfbereich | A: öffentlich angekündigt | B: tatsächlich garantiert | C: kapazitätsabhängig | D: Konto/Zahlmittel/Bezahlrahmen | E: unbekannte Leistung |
|---|---|---|---|---|---|
| Ampere A1 | Historische 4-OCPU-/24-GB-Größenordnung nur Untersuchungsannahme; heutige Quote nicht verifiziert | Keine garantierte kostenlose EU-Zuteilung nachgewiesen | Shape/Region und Zeitpunkt müssen tatsächlich verfügbar sein | Aktuelle Registrierungs-/Zahlmittel-/Upgradebedingungen unlesbar | CPU-/RAM-/Bandbreitenleistung für den konkreten Stack nicht gemessen |
| Block-/Bootspeicher | Heutige freie Gesamt- und Bootmenge nicht verifiziert | Keine konkrete nutzbare GB-/IOPS-Zusage belegt | Verfügbare Volumes/Region/Quoten prüfen | Überziehung, Snapshots und Upgradekosten offen | DB-/Modelllade-/Backup-IO unbekannt |
| Objekt-/Backupspeicher | Freimenge/Requests/Transfer nicht aktuell bestätigt | OCI-internes Backup erfüllt allein DEC-49 nicht | Angebot/Region prüfen | Speicher-/Restore-/Egresspreis offen | Durchsatz und Restorezeit unbekannt |
| Netzwerk/IPv4/Bandbreite | Aktuelle Freimengen/Adresskosten unlesbar | Keine garantierte kostenlose öffentliche IPv4 oder Bandbreite aus alter Werbung ableiten | Netz-/Region-/Adressangebot prüfen | Kosten/Sperren/Abrechnungslimits offen | Konkurrenz zwischen Medien, Modellen und Restore messen |
| EU und Kontobestand | EU-Standort muss ausgewählt und vertraglich passend sein, kein Ausweichen in ungeprüfte Nicht-EU-Region | Aktuelle Vertrags-/Subprozessor-/SLAzusagen nicht verifiziert | Heimatregion und verfügbare Kapazität auseinanderhalten | Aufrechterhaltung Free Tier, Sperrung/Kündigung und Zahlungsanforderung offen | Produktionsverfügbarkeit nicht aus kostenloser Quote beweisbar |
| Inaktivität / Rückgewinnung | Mögliche Rückgewinnung/Suspendierung als Risiko prüfen; aktuelle Regeln nicht lesbar | Keine Bestands-/SLAgarantie behaupten | Eine früher vorhandene Instanz kann nicht als dauerhafte Zusage gelten | Aktuelle Schwellen, Beobachtungsdauer und Upgradefolgen nicht verifiziert | Kein künstliches Lastprogramm zur Umgehung von Idlebedingungen vorschlagen |

**Oracle-Ergebnis:** Persönlicher begrenzter Prototyp auf *tatsächlich zugeteilter* geeigneter EU-CPUinstanz theoretisch prüfbar. Vollständige Multiuser-V1 einschließlich KI, sicherer Identität und unabhängiger Recovery weder kapazitiv noch finanziell nachgewiesen. ARM64-Unterstützung von Motoren ist dokumentiert, aber Wheels/Parser/Modelldateien, konkrete ISA und gemeinsamer Betrieb müssen T01/T02/T04/T05 bestehen. Keine CPU-Quote wird als Instanzverfügbarkeit ausgegeben. Vor Anbieterentscheidung aktuelles offizielles Angebot/Regeln und später gesondert genehmigte Zuteilungsprobe nötig.

## 3. Hetzner / Scaleway und deutscher Bruttorahmen

| Prüfgegenstand | Hetzner | Scaleway | Zu schließender Nachweis |
|---|---|---|---|
| Geeigneter Compute | Nicht billigste VM vergleichen: Szenarien A/B aus Ressourcenstudie, ausreichend RAM für gemeinsame Prozesse | Gleiche Lastbasis, ggf. zusätzliche Managed-Mindestressourcen | SKU, CPUarchitektur, garantierte/geteilte CPU, RAM, Region, aktuelle Lieferbarkeit |
| Aktueller Preis | Website und Billing-FAQ erneut 403; SDK enthält Preisstrukturen, kein gültiges Angebot | Preis-/öffentliche APIbeschreibung erneut 403 | Netto-/Bruttopreis pro Zeitraum, Mindestabrechnung, Rabatte und Kündigung |
| Speicher / Traffic / IPv4 | Aktuelle GB/IO/IPv4/Trafficlimits und Überschreitungen nicht verifiziert | Gleiches gilt für Compute-/Objekt-/Managed-DB-Dienste | Nicht nur Grundpreis, sondern Boot-/Daten-/Snapshot-/Egresskosten vergleichen |
| Backups / Snapshots | Umfang, Region, Aufschlag, Restore und Löschrechte nicht aktuell bestätigt | Aktuelle Bedingungen nicht verifiziert | Provider-Snapshot ersetzt kein unabhängiges DEC-49-Backup |
| Datenschutz / Vertrag / Wachstum | EU-Region, Vertrag, Unterauftragnehmer, Zugriff und Resizeablauf offen | Je Managed-Dienst prüfen, nicht nur Anbieteradresse | Zulässige Verarbeitung, Ausfall-/Export-/Kündigungsweg, Preis-/Kapazitätsstaffel |

Deutsches Privatszenario **Rechenannahme 19 % USt**: `brutto = netto × 1,19`; z. B. hypothetische 8,00 EUR netto → 9,52 EUR brutto, **kein Anbieterpreis**. §12-UStG-Abruf blockiert, Anwendbarkeit/Steuersatz nicht als hier rechtlich live bestätigt ausgeben. Netto-/Bruttoangabe des tatsächlichen Angebots prüfen, vorhandene Bruttowerte nicht nochmals besteuern; Unternehmer-/Reverse-Charge-Konstellation gesondert. USD-Backupkosten benötigen datierten Umrechnungskurs und geklärte Steuerbehandlung. Ohne aktuelle Angebote kein belastbarer EUR-Gesamtbetrag oder Nachweis ≤10 EUR brutto/Monat.

## 4. Modelle, Lizenzen und veröffentlichte Evaluation

Alle exakten Gewichtsrevisionen/Dateihashes sind noch zu fixieren. Hersteller-README-SHA ist **kein Gewichts-Hash**. Tabellen-RAMwerte aus [Ressourcenbedarf](RESSOURCENBEDARF.md) sind Rechnungen, keine Benchmarks; Motorlizenz ersetzt Gewichtslizenz nicht.

| Identifizierter Kandidat | Gewichts-/Kommerzstatus | Größe / Quantisierung / Kontext | CPU / Sprachen / Gütenachweis |
|---|---|---|---|
| Qwen/Qwen3-1.7B | Hersteller erklärt Qwen3-Gewichte Apache-2.0; individuelle LICENSE und Metadaten-API erneut 403, Revision nicht verifiziert | 1,7B laut Hersteller; Q4-Gewichtstheorie ca. 0,85 GB; konkrete Datei/Quantisierung und native Kontextgrenze noch unbestätigt | llama.cpp-ARM grundsätzlich dokumentiert; konkreter Build/Modellkern und DE/FR/EN-Qualität T02/T03 |
| Qwen/Qwen3-4B-Instruct-2507 | Expliziter 2507-Kandidat im Herstellertext, Apache-2.0-Aussage; konkrete LICENSE/API noch blockiert | 4B, Q4-Theorie 2 GB; 2507-Text nennt große Kontexte, konkrete Modellkonfiguration nicht separat gelesen | Kein Gratis-Echtzeitnachweis; GPU nicht grundsätzlich Voraussetzung, mehrere CPUinferenzjobs ungeprüft |
| Qwen/Qwen3-8B | Herstellerkandidat; direkte config/API nicht lesbar, Gewichtslizenzbeilage offen | 8B, Q4-Theorie 4 GB; Hersteller zeigt u. a. Q8_0-GGUF sowie Laufbeispiele mit 40.960/131.072 Kontext. Das sind **keine pauschal bestätigte native Grenze oder RAMzusage**. | Größere CPU-/KVlast; DE/FR/EN und fakultäre Inhalte getrennt bewerten |
| OpenAI Whisper multilingual tiny/base/small | Hersteller erklärt Code **und Gewichte MIT**; neuer offizieller Pythonkatalog nennt Checkpointdateien mit SHA256-Bezug in Download-URL, keine Gewichte geladen | 39/74/244 Mio. Parameter; veröffentlichte whisper.cpp-RAMwerte ca. 273/388/852 MB, Decode-/Dateireserven zusätzlich; Quantisierung artefaktspezifisch. Audiosegment-/Textkontext aus konkreter Runtime fixieren. | CPU/ARM64 dokumentiert, keine A100-Geschwindigkeit auf OCI übertragen; keine `.en`-Variante für DE/FR. WER/Timestamps T05 |
| Qwen/Qwen3-Embedding-0.6B | Neuer offizieller Familienkatalog gelesen; konkrete Gewichts-LICENSE/Revision noch offen | Hersteller: 0,6B, 32K Sequenz, 1024 Dimensionen. Größe folgt Präzision; maximale Sequenz nicht als knappe CPUkonfiguration übernehmen. | Hersteller nennt DE/FR/EN und über 100 Sprachen. MTEB 70,58 für **8B**, Stand 05.06.2025, ist Herstellerbericht und kein 0,6B-/Syllentra-Nachweis. |
| intfloat/multilingual-e5-small / BAAI/bge-m3 | Mission-5-Kandidaten; konkrete Karten/Lizenzen/Revisionen weiter nicht verifiziert | Konkrete Artefakte, Tokenizer, Kontext, Dimension und Quantisierung vor T02/Retrievalprobe fixieren | Vergleich gegen Volltext, kein automatisch besseres pädagogisches Gedächtnis |
| Piper: de_DE-thorsten-medium, fr_FR-siwis-medium, en_US-lessac-medium als **zu verifizierende Kandidaten-IDs** | Aktueller Motor GPL-3.0; neue offizielle Stimmendokumentation verweist auf gesonderte Modellkarten. Die Stimmendokumentation bezeichnet persönliche Nutzung/Forschung als Ziel und verweist auf teils restriktive Modellkarten; daraus weder pauschales Kommerzrecht noch pauschales Lizenzverbot ableiten. Je Stimme Gewicht-/Datensatz-/Kommerzrecht offen. | Größe/Quantisierung/RAM/Kontext je konkreter Stimme nicht verifiziert; keine ausgewählten Artefakte | DE/FR/EN getrennt abnehmen. Vorläufige 0,5–2 GiB Testreserve, CPU möglich, kein gemessener Realtime-Faktor |
| hexgrad/Kokoro-82M | Hersteller nennt Apache-Gewichte, konkrete Stimmenbedingungen offen | 82M, Artefakt/Hash/RAM noch festzulegen | FR/EN-Beispiele, DE für geprüften Stand nicht nachgewiesen; nicht alleiniger Drei-Sprachen-TTS-Nachweis |

Allgemeine Modellfähigkeit, Selbstbewertungen und veröffentlichte Herstellerbenchmarks belegen keine zuverlässige Hochschuldidaktik. Unabhängige Evaluation auf vergleichbarer CPU/Quantisierung/Sprach-/Fachlast ist hier **nicht verifiziert**. T03 benötigt eigene synthetische Fachfälle, Quellenprüfung und menschliche Rubrik. Lokale Inferenz ist kein Zugriff auf Consumer-Abos und kein pauschales Recht zur Cloudanalyse sensibler Inhalte.

## 5. Identität: Fähigkeiten und konkrete Integrationslücken

| Forderung | Keycloak | authentik | Bibliotheksansatz / gemeinsame Pflicht |
|---|---|---|---|
| Offene Registrierung | Konfigurierbarer IdP-Kandidat; konkreten Flow noch prüfen | Enrollment-Flow als Kandidat | Registrierung vollständig implementieren/prüfen, keine private Appdatenfreigabe vor Verifikation |
| E-Mail-OTP | Neu gelesene Verify-Email-Anleitung beschreibt **Link**. OTP-Policy beschreibt TOTP/HOTP-Generator, nicht E-Mail-Code. Kein nativer passender Flow bewiesen. | Neue Email-Stage beschreibt tokenisierten Link/Message und Rückkehr mit Token; kein passender eingegebener E-Mail-OTP-Code nachgewiesen. | Codebindung, Endlichkeit, Einmaligkeit, Limits und Fehlerfreiheit gesondert nachweisen; kein ungeprüftes Plugin |
| Geräte / Sessions / Widerruf | Produktfunktion als Kandidat, konkrete Appbindung/Entzug noch T06 | Ebenso | Aktuelle App-/Gerätezustände bleiben autoritativ; lokale Sperre kein Sessionrecht |
| Rollen-MFA / Recovery | Generator-MFA dokumentiert; Adminverlustverfahren bleibt offen | Flowausgestaltung, Faktoren und Wiederherstellung prüfen | Keine alleinige SMS-Recovery, kein Dokumentenschlüsselerwerb durch Kontoerfolg |
| Inaktiver/gesperrter Account | Nicht durch Recovery alte Apprechte aktivieren | **Email-Stage kann standardmäßig inaktive Nutzer per Recovery reaktivieren**; Aktivierungsoption und Appkontostatus zwingend prüfen. Eine Sperrpolicy darf nicht nebenbei Kontenexistenz verraten. | Regression mit Pause, Adminsperre, Löschung und Anti-Enumeration; T06/T09 |
| Getrennte UI, ein Super Admin, begrenzte Delegation | Kein automatischer Fit durch Realm-/Cloudadmin | Ebenso | Appinvariante, sichere Erstbesetzung, MFA und aktuelle Serverrechte; IdP-Gruppen allein reichen nicht |
| Kontoisolation / Serverkontrolle | IdP authentisiert, autorisiert nicht alle Fachobjekte | Ebenso | Backend/DB/Jobs/RAG/Cache müssen Objekt-/Scope-/Feature-/Supportrechte prüfen |
| RAM | Eigener Java-/DB-/Betriebsbedarf, gemeinsames Speicherprofil noch ungemessen | Server-/Worker-/DBprofil und jeweilige Versionsabhängigkeiten messen | Weniger IdPprozesse spart evtl. RAM, erhöht Eigenimplementierungs-/Reviewlast. Keine sichere Variante allein aus RAM wählen. |

Keine der drei Varianten ist als vollständige, sichere Syllentra-Integration bestätigt. Auth.js-Lizenz bleibt ISC, authentik-Bereiche/Enterprisebedingungen und Keycloak Apache-2.0 unverändert. T06 ist vor einer endgültigen Lösung nötig, Bootstrap/Recovery bleibt Eigentümer-/Architekturentscheidung.

## 6. Backup: neue technische Aussage, Vertrag weiter offen

Neuer offizieller R2-Text dokumentiert **Bucket locks** gegen Überschreiben/Löschen, auch gegenüber Lifecyclelöschung; bei EU-Jurisdiktion entsprechende Zuständigkeitsbindung. Konfigurationsberechtigte können Regeln ändern/entfernen. Das ist **kein Nachweis eines unentfernbaren Schutzes gegen kompromittierten Accountadmin**. Rollen/Keys trennen, Konfigurationsrechte nicht auf dem Primärhost, endliche mit DSGVO-Löschpflichten kompatible Retention; keine unbefristete Sperre als Standard.

Neue restic-Dokumentation unterscheidet Entfernen von Snapshots (`forget`) und physische Bereinigung (`prune`), benötigt Scratchspace und beschreibt Risiken in append-only-Umgebungen. Manipulierte Snapshotzeiten und ein privilegierter Prunelauf können legitime Sicherungen gefährden; getrennte Wartungsrechte und geprüfte Retentionsauswahl nötig. Bucketlock und restic-Prune müssen zeitlich/rechtlich zusammenpassen, sonst Fehler oder dauerhaft wachsende Kopien.

R2-EU-Objektjurisdiktion und Standardpreise bleiben die in Mission 5 belegten Aussagen; die gesamte Vertrags-/Metadaten-/DPAprüfung ist erneut blockiert. Hetzner Storage Box/B2/Scaleway: aktuelle Standort-/Vertrags-/Preis-/Recoverygarantien nicht neu verifiziert. Gleicher Anbieter wie Primärhost ist kein unabhängiges DEC-49-Backup. Konfiguration konsistent und verschlüsselt sichern, Schlüssel getrennt verfügbar, keine temporären Transkripte/Secretschattenkopien; tatsächlicher unabhängiger Restore erst T07 nach gesonderter Autorisierung.

## 7. Machbarkeit und möglicher Entwicklungsblocker

Ein kleiner Prototyp ist als **Prüfvorhaben**, nicht fertige V1, konkret abgrenzbar. Blockierend vor technischer Adoption: ungeprüfte Gewichts-/Stimmenrechte, ungeklärtes OTP-/Adminrecoveryverfahren, fehlender zulässiger EU-/Backupvertrag, fehlende Kapazität bzw. nicht erfüllte bestätigte Qualität/Latenz, kein autorisierter Kosten-/Testauftrag. Dokumentation und weitere öffentliche Recherche bleiben möglich. Keine bestätigte Ziel-V1-Funktion löschen; progressive Aktivierung nach [Ressourcenprofilen](RESSOURCENBEDARF.md), [Testplan](BENCHMARKPLAN.md) und [Entscheidungsvorlage](ENTSCHEIDUNGSVORLAGE.md). FE-56 offen, kein Pflicht-Pay-API, keine automatische Beschaffung.
