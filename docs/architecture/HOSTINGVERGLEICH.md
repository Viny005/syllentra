# Hostingvergleich — Oracle und Alternativen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

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
