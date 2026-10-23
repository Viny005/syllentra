# Hostingvergleich — Oracle und Alternativen

**Version:** 0.3 · **Stand:** 23.10.2026 · **Status:** Architekturprinzipien (A) in Mission 21 bestätigt; konkrete Anbieterwahl (B) und Nachweise (C) offen

> **Fortschreibung Mission 7:** Für künftige Vergleiche gilt jetzt bis zu **20 EUR brutto/Monat**, keine Ausgabe genehmigt. Die nachfolgenden 10-EUR-Aussagen/Rechnungen dokumentieren den früheren Untersuchungsstand aus Mission 5/6; sie sind keine aktuelle Obergrenze. Auch unter 20 EUR ist vollständige V1-Leistung nicht nachgewiesen. [Bestätigter Rahmen](../ARCHITECTURE_DECISIONS.md#adr-0006--persönlicher-qualitätsfokus-und-vergleichsrahmen-aus-mission-7).

## 1. Evidenz und Bewertungsgrenze

DEC-48 aus [ADR-0004](../ARCHITECTURE_DECISIONS.md#adr-0004--vorrangige-hostingbewertung-von-oracle-cloud-dec-48) priorisiert **Oracle untersuchen**, nicht Oracle auswählen. Kein Anbieter wurde eingerichtet oder getestet. Direkte offizielle Angebots-/Regionsseiten waren am 22.10.2026 trotz erneutem autorisiertem Abruf mit Tunnel-403 unzugänglich. Deshalb sind aktuelle Preise, tatsächlich verfügbare Quoten, Vertragsbedingungen und regionale Kapazität **nicht verifiziert**. Quellen/Abrufstatus: [Quellenregister](QUELLEN.md). Eine GitHub-Softwarequelle belegt keine Cloudverfügbarkeit.

## 2. Oracle Cloud Always Free — Detailprüfung

| Aspekt | Technische Einordnung / zu prüfende Behauptung | Nachweis vor Auswahl |
|---|---|---|
| Ampere A1 / ARM64 | Historisch publizierte Größenordnung bis 4 OCPU / 24 GB RAM pro Always-Free-Tenancy ist **kein aktuell verifiziertes Angebot**. Kein GPU-Angebot oder tatsächlicher freier Platz daraus ableitbar. OCPU nicht pauschal mit x86-vCPU gleichsetzen. | Aktuelle offizielle Gesamtquote, OCPUstunden/RAMstunden, Shapes, EU-Heimatregion und tatsächliche Zuteilung in gesondert erlaubter Probe |
| Kleine x86-Free-Instanzen | Geringer RAM kann Web-/Hilfsaufgaben tragen, nicht automatisch LLM, Datenbank und Medienverarbeitung zusammen. Aktuelle Shapes/Anzahl **nicht verifiziert**. | Speicher-/CPUgrenzen und reproduzierbare Koexistenztests |
| Block-/Objektspeicher | Bootvolume, Dokumente, Datenbank, temporäre Dateien, Modellgewichte, Index und Snapshots konkurrieren um Kontingente. Historische Gratiszahlen nicht als zugesagt budgetieren. | Heutige eingeschlossene GB, IOPS, Requests, Restore-/Transferkosten und Überschreitungsverhalten |
| Netz und Region | EU-Hauptdaten und zulässige Unterauftragnehmer erforderlich; nicht beliebige Heimatregion wählen, nur weil dort Kapazität verfügbar ist. | Regions-/Vertragsprüfung, Bandbreite/Egress/öffentliche IPv4, private Netze, DNS/HTTPS |
| Verfügbarkeit | „Out of capacity“, Registrierungs-/Kontoprüfung, Änderungen von Gratisbedingungen, Suspendierung und Rückgewinnung inaktiver Ressourcen sind zu untersuchende Risiken, keine hier aktuell bestätigten Einzelbedingungen. | Aktuelle offizielle Regeln, Sperr-/Idlekriterien, Benachrichtigung, Export-/Recoveryweg; kein Free-Tier-SLA unterstellen |
| ARM64-Software | PostgreSQL/Python/Node und C/C++ prinzipiell portierbar. llama.cpp und whisper.cpp dokumentieren ARM-Unterstützung; konkrete Linux-ARM64-Builds, Python-Wheels, OCR-/Medien-/Kryptoabhängigkeiten trotzdem separat prüfen. | Versionsgebundene ARM64-Build-/Import-/Modelltests, keine x86-Container oder Apple-Metal-Benchmarks als OCI-Nachweis |
| Multiuser und KI | Appseitige Kontentrennung hängt nicht von gratis/bezahlt ab. Eine CPU-Queue kann mehrere Konten sicher bedienen; Antwortzeit bei mehreren KI-Aufträgen ist **nicht gemessen**. | N1-Lastprofil, RAM-/KV-Cachemessung, faire begrenzte Parallelität, RAG-/ASR-Koexistenz und Qualitätsrubriken |
| Kosten und Wachstum | Kein automatisches Upgrade oder bezahlte Ersatz-API. Gratisinstanz spart nicht Backup, Mailzustellung, Domain und Pflege. | Harte technisch wirksame Limits, Konditions-/Kapazitäts-/Kostenprüfung und getrennte Ausgabenfreigabe |

**Ergebnis:** Oracle bleibt erster experimenteller Kapazitätskandidat. Eine robuste V1 auf stets kostenlos verfügbarer OCI-Inferenz ist **nicht bewiesen**. Ohne reale Zuteilung und Benchmarks darf sie weder zugesagt noch als fertige V1 freigegeben werden. DEC-49 verlangt auch bei Oracle einen unabhängigen Backupanbieter.

## 3. Zwei glaubwürdige Alternativen

| Bereich | Hetzner Cloud, EU-Standort | Scaleway, EU-Standort |
|---|---|---|
| Konzept | Eine bezahlte zentrale VM für Anwendung, PostgreSQL, Dateien und begrenzte Worker; unabhängiges Backup | Zentrale VM, optional verwaltete PostgreSQL-/Objekt-/Maildienste beim selben Primäranbieter; unabhängiges Backup |
| Hauptnutzen | Einfacher portabler Linuxbetrieb, vorhersehbare Ressourcenklasse statt auf freie OCI-Zuteilung angewiesen | Weniger Primäranbieter für Compute/DB/Objekte/Mail möglich; Betriebsaufwand durch Managed Services verschiebbar |
| Preis und Zuteilung | Aktuelle VM-/IPv4-/Transferpreise und Lieferbarkeit **nicht verifiziert**; kein konkreter Serverpreis behauptet | Aktuelle Dienst-/Mindestpreise, Regionen und Lieferbarkeit **nicht verifiziert** |
| Sicherheit / EU | Exakte EU-Region und Vertrags-/Subprozessorprüfung; selbst betriebene DB/Updates/Backup bleiben Betreiberpflicht | Serviceweise Region, Vertrag, private Erreichbarkeit, Backup-/Exportrechte und Managed-Grenzen prüfen |
| ARM/x86 | x86 oder ARM je tatsächlich angebotenem Tarif; quantisierte CPU-Modelle abhängig von Speicherbandbreite/ISA prüfen | Je Shape CPUarchitektur/GPUangebot prüfen; Managed heißt nicht ausreichend kostenlose Inferenz |
| Wartung | Wenige Dienste, aber eigener Patch-/Auth-/DB-/Restorebetrieb | Mehr Dienstkonfiguration, mögliche Mindestkosten, Anbieterbindung und serviceübergreifender Restore |
| Wachstum | Mehr RAM/CPU, ausgelagerte Worker oder später dedizierte Inferenz; Migration kontrolliert | Dienste getrennt skalierbar; Komplexität erst bei belegtem Bedarf rechtfertigen |
| Offene harte Grenze | Vollständiger KI-/Betriebsumfang unter 10 EUR brutto/Monat nicht nachgewiesen | Mehrere Managed Services unter 10 EUR brutto/Monat nicht nachgewiesen |

Anbieterreduktion bedeutet Bündelung des **Primärbetriebs**, niemals Aufgabe der DEC-49-Unabhängigkeit. Ein einzelner Anbieter für alles inklusive einzigem Backup ist kein zulässiger V1-Vorschlag. Die drei vollständigen Konzepte stehen im [Architekturvergleich](README.md).

## 4. Externe Dienste und Hybridvarianten

| Konzept | Infrastruktur-Anbieter | Weitere notwendige/optionale Dienste und Zählung |
|---|---|---|
| A: OCI + unabhängiger R2-EU-Backupkandidat | 2 | Sicherheits-/OTP-Mailzustellung nötig: OCI-Mail falls geeignet und bestätigt, sonst zusätzlicher Mailanbieter. Domainregistrar/DNS nötig, kann vorhandener oder bereits gezählter Anbieter sein. Insgesamt konservativ 2–4 Anbieter; keine verifizierte 2-Anbieter-Zusage. |
| B: Hetzner + unabhängiger R2-EU-Backupkandidat | 2 | Externe zuverlässige OTP-/Sicherheitsmail voraussichtlich zusätzliche Dienstgrenze; Selbsthosting von SMTP nicht als kostenlose sichere Zustellung voraussetzen. Registrar/DNS ggf. zusätzlich: typischer Planungsfall 3–4 Anbieter. |
| C: Scaleway + unabhängiger R2-EU-Backupkandidat | 2 | Mail/Domain/DNS soweit im geprüften Primärangebot bündelbar, sonst weitere Anbieter: 2–4. Mehr Managed Services beim selben Anbieter erhöhen Dienstzahl trotz gleicher Anbieterzahl. |

Dienste ohne extra Betreiber zählen trotzdem: PWA-Push kann von Browser-/OS-Pushsystemen abhängen; optionale Kalender-/GitHub-/Hochschulverbindungen ergänzen je aktive Verbindung eigene Vertrauensgrenzen. Lokale Open-Weight-Inferenz, eigener IdP und PostgreSQL benötigen keinen externen KI-/Authanbieter. Sie haben trotzdem Betriebskosten. Sicherheitsmail ist nicht die offene FE-56-Postfachlesefunktion.

**Hybrid nur bei Nutzenbeleg:** Zentrale App/DB bei A/B/C plus getrennte EU-Inferenz auf eigener gemieteter Hardware oder ausdrücklich zulässiger optionaler API. Vorteil kann erst ein gemessener Engpass mit Qualitäts-/Latenzverbesserung sein. Nachteile: zusätzliche Netzwerk-/Provider-/Kosten-/Datenschutzgrenze und Fehlerfälle. Keine Empfehlung für V1 unter 10 EUR ohne Belege; kein persönlicher Dauer-PC als Pflichtserver, keine automatische bezahlte Ausweich-API. Ein externer GPUanbieter wäre ein weiterer Anbieter; ein Worker beim selben Hostanbieter eine zusätzliche Dienst-/Sicherheitsgrenze.


## 5. Vom Projektinhaber bestätigte Architekturprinzipien aus Mission 21 (TECH-O-02, TECH-O-11 und Multi-Provider-Querschnitt)

Am 23.10.2026 hat der Projektinhaber die Hosting-, Kommunikations- und Multi-Provider-Prinzipien auf Architekturebene bestätigt ([ADR-0011](../ARCHITECTURE_DECISIONS.md#adr-0011--hosting-prüffolge-oci-vorrangig-hetzner-als-bevorzugter-rückfall-google-cloud-als-alternative-tech-o-02), [ADR-0020](../ARCHITECTURE_DECISIONS.md#adr-0020--transaktionale-kommunikation-unabhängige-domaindns-und-v1-postfachausschluss-tech-o-11), [ADR-0021](../ARCHITECTURE_DECISIONS.md#adr-0021--querschnittsentscheidung-kontrollierte-multi-provider-austauschbarkeit-und-fallback-grenzen)):

| Bezug | A. Bestätigtes Architekturprinzip | B. Offene technische Unterentscheidungen | C. Ausstehende Nachweise |
|---|---|---|---|
| **TECH-O-02 — Hosting-Prüffolge (DEC-48)** | Zentrale EU-Datenhaltung unabhängig vom privaten PC (`CON-36`, `FE-42`, `FE-75`, `SEC-08`): **Oracle Cloud Infrastructure (OCI)** ist der erste zu testende Kandidat (`DEC-48`); **Hetzner** ist die bevorzugte europäische Rückfalllösung (Fallback); **Google Cloud** bleibt als weitere Alternative erhalten (neben den in Mission 5 untersuchten EU-Optionen). Es ist noch kein Anbieter, keine Region, kein Konto und kein Server endgültig ausgewählt. | Endgültige Anbieterwahl, konkrete EU-Region, Shape/Architektur (ARM64 vs. x86_64), Netz-/Volume-Konfiguration und Auftragsverarbeitungsvertrag. | Aktuelle offizielle Preis-/Quoten-/Kapazitätsprüfung, EU-Unterauftragnehmerprüfung und gesondert genehmigte Infrastrukturprobe (`T01`, `T08`, `O-S3-01/03`). |
| **TECH-O-11 — Kommunikation, DNS und Integrationen** | Zuverlässige transaktionale E-Mails für OTP und Sicherheit (`NB-05`, `SEC-01/03`); unabhängig vom Hosting kontrollierte Domain; einfaches DNS mit Möglichkeit zur Bündelung nur bei echtem Vorteil; persistente interne Benachrichtigungen mit austauschbaren Push-/E-Mail-Transporten (`NB-09`, `UC-65`); optionale und autorisierte externe Integrationen; strikter Erhalt von `FE-56` (**keine Postfachlektüre, -überwachung oder -synchronisation in V1**). | Konkreter transaktionaler E-Mail-Anbieter und Web-Push-/Benachrichtigungsadapter (`O-S1-03`), Domainregistrar/DNS-Betreiber sowie Bounce-/Rate-Limit-Regeln (`O-S3-08/12/13`). | Zustellbarkeits- (`SPF`/`DKIM`/`DMARC`), Annahme-/Zustellnachweise ohne Inboxrecht (`O-S1-03`, `AT-S1-10`), Timeout-/Deduplizierungsnachweise (`AT-S1-14`), EU/DSGVO- (`O-S3-10`) sowie Quoten-/Preisprüfung (`T06`, `T08`, `O-S3-08/12/13`). |
| **Querschnitt — Multi-Provider & kein naives Hosting-Failover** | Strikte Trennung zwischen **(1) geplantem Anbieterwechsel**, **(2) kontrollierter Migration von Daten oder Diensten** (`S2`/`S3`; **keine naive Anbieterrotation** auf das gesamte Primärhosting, PostgreSQL oder private Schlüssel) und **(3) sicherem automatischem Fallback für eine einzelne Operation** (nur für austauschbare Adapter wie E-Mail, KI, OCR, ASR, TTS und Hinweise und nur wenn technisch sicher, vertraglich erlaubt und konform mit `SEC-08/10/20`, `N2.16`); Idempotenz/Deduplizierung; Verbot automatischer Ausgaben/Upgrades oder Free-Tier-Umgehungen; bei Quotenende stoppt/degradiert die unmittelbar betroffene Funktion sauber mit verständlicher Meldung (`AT-S3-18`, `REL-Q04/Q06`), während unabhängige Bereiche (Lesen, Bearbeiten, Exportieren, Löschen eigener Daten) nutzbar bleiben. | Konkrete Adapter-Fallbacks, Idempotenzschlüssel und Quoten-Circuit-Breaker. | Negativtests für Quota-Erschöpfung, Ausfall und Verhinderung doppelter fachlicher Wirkungen (`AT-S1-14`, `AT-S3-14`, `AT-S3-18`, `REL-Q01..Q09`). |
