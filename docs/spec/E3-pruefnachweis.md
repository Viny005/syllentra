# E3 — Änderungs- und Prüfnachweis

**Projekt:** Syllentra AI\
**Version:** 0.6\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

> **Historischer Nachweis:** E3.1 bis E3.6 dokumentieren die abgeschlossene S1-Lieferung bis `723af7fa1692f8dbaf888b694fa63806d7d5fc5f`. Die dortige damalige Dateiliste und „S2 geplant“ sind keine Aussagen zum aktuellen Bestand. E3.7 bis E3.10 dokumentieren den anschließend abgeschlossenen S2-Auftrag bis `53ef171be4783748b5c7e3a84bb0cc363d5b4194`. E3.11 bis E3.16 dokumentieren die vier Fachentscheidungen bis `0676f791c858765a005a32e2af8c8442eff9712e`. Die redaktionelle Bereinigung und ihre aktuellen Prüfungen stehen in E3.17. Historische Versionsmatrizen und Prüfzahlen beziehen sich jeweils auf die bezeichnete Lieferung, nicht auf den heutigen Gesamtbestand.

## E3.1 Auftrag und Grenzen

Grundlage ist der vollständig gelesene Arbeitsauftrag vom 16.10.2026 einschließlich FE-01 bis FE-89. Ausgangsstand `ace1d80e80245379beed02296c3c4dd184c8dd70`, bestehender Branch `docs/spec/p1-p2-mobile-workspaces`, bestehende PR #1. Änderungen beschränken sich auf Spezifikationsdokumente. Keine neuen Produktentscheidungen, Anwendungscodeänderungen oder aktivierten Anbieterzugänge. FE-56 bleibt offen, alle Dokumente bleiben Zur Prüfung.

## E3.2 Aufgelöste Widersprüche und tatsächliche Änderungen

| Ausgangsbefund | Korrektur und betroffene Bausteine |
|---|---|
| Persönliche Einzelnutzer-V1, späteres Mehrbenutzersystem und NG-01 | P1 1.1/1.3, G-40, CON-01/02/05, SC-51/53, Risiken; P2-Akteure/Diagramm; F1/F2, DM-01/INV-01 und B3 auf getrennte V1-Konten geändert. NG-01 als durch FE-59 aufgehobenes Nichtziel begründet erhalten. |
| PWA/Cloud noch vollständig offen oder native Fähigkeiten pauschal zugesagt | P1/P2/F1/F2 auf entschiedene PWA und interne zentrale EU-Cloud präzisiert; Hardware-/PWA-Fähigkeiten mit Rückfallwegen, Framework/Anbieter offen. |
| NB-10 könnte eigene Cloud oder bidirektionalen Fremdspeicher bedeuten | P2 Tabelle, Text und Diagramm sowie S1 NB-10 ausschließlich optionaler externer Datei-/Ordner-Leseimport; interne Cloud/Sicherungen davon getrennt. |
| Postfachlesen als üblicher V1-Batch, jede OTP-Mail scheinbar einzeln genehmigen | P2 NB-05 und BAT-02 korrigiert: manuelle Nachrichtendateien, zweckgebundener ausgehender OTP-/Sicherheitsversand und optionale Reminder; keine V1-Inboxfreigabe, FE-56 offen. |
| GitHub nur ausgewählte Repos und noch unentschiedener Produktvorschlag | P2 NB-07, UC-42-Ergänzung, DT-57, DLG-43, BAT-18, B3: freiwillige offizielle Verbindung, einzelne oder alle eigenen öffentlichen Repositories, nur lesend. Technische Verfügbarkeit weiterhin bedingt. |
| „Möglichst kostenlos“ und API-/Verbraucherabo missverständlich | P1 CON-23/24, P2, F3, S1/N1: kostenfreie kommerziell passende Software-/Modell-/Unterabhängigkeitslizenzen, keine Pflicht zu bezahlter API; Infrastrukturkosten gesondert. |
| Konto = Administration, fehlende Sitzungs-/OTP-/Support-/Releaseobjekte | F1–F3 und B1 ergänzt; D1/D2 modellieren getrennte Konten, Adressen, Verifikation, Sitzungen, Rollen, Support, Quoten, Features und Releasefassungen. Genau ein Super Admin, kein pauschales Inhaltsrecht. |
| Unbestimmte automatische Fremdabrufe, keine Source-/Derived-Revisionen | Pro Verbindung manuell als Standard, opt-in Automatik; Integrationslauf/-historie, Revision, Inhaltsannahme und sichere begrenzte Retries in S1/F2/F3/D1/D2/B1/B2. |
| Fehlender Schlüssel-/Klartext-/Lösch-/Restorezusammenhang | Schutzkennzeichnung und Vererbung, getrennte persönliche Schlüsselrecovery, konkrete temporäre Cloudklartextfreigabe, Papierkorb und inhaltsfreie Löschmarkierung, EU-Sicherung/Differenzrestore. N1/N2 halten technische Restfragen offen. |
| Freie Studienleistung ohne ausdrücklichen Institutionsbezug | Optionaler direkter DM-12→DM-04-Bezug, originale institutionelle Skala, geschützte Notendetails; ungeklärte Zuordnung bleibt ungeklärt. |
| Fehlende S1-Verträge und veralteter Index | S1 mit zwölf Verträgen, deutscher 89-FE-Matrix und 30 Abnahmeszenarien; N1/N2 begrenzte Folgeentwürfe, E2 Glossar und aktueller README-Index. |

## E3.3 Bestand und neue Kennungen

Alle bisherigen Kennungsidentitäten bleiben erhalten; keine Umnummerierung. Fachlich ersetzte Aussagen sind durch spätere FE begründet, insbesondere NG-01/FE-59, mobile Methode/FE-55 und GitHub/FE-43.

| Baustein | Vorher → aktuell | Neue Kennungen |
|---|---|---|
| P1 | 0.5 → 0.6 | G-40..G-45, CON-36..CON-42, SC-51..SC-61, R-34..R-40 |
| P2 | 0.6 → 0.7 | Keine neuen NB/CFG/DK-Kennungen |
| F1 | 0.2 → 0.3 | Keine neuen GP-Kennungen |
| F2 | 0.1 → 0.2 | UC-51..UC-63 |
| F3 | 0.1 → 0.2 | AF-28..AF-35 |
| D1 | 0.1 → 0.2 | DM-53..DM-71, INV-26..INV-31 |
| D2 | 0.1 → 0.2 | DT-65..DT-85 |
| B1 | 0.1 → 0.2 | DLG-51..DLG-64 |
| B2 | 0.1 → 0.2 | BAT-20..BAT-23 |
| B3 | 0.1 → 0.2 | Keine neuen OUT-Kennungen |
| S1 | Neu 0.1 | AT-S1-01..AT-S1-30, O-S1-01..O-S1-14; bestehende NB-01..NB-12 |
| N1 / N2 | Neu jeweils 0.1 | NFR-01..NFR-12 / SEC-01..SEC-16; begrenzte Folgeentwürfe |
| E2 / E3 | Neu jeweils 0.1 | Glossar / tatsächlicher Änderungs- und Prüfnachweis |

## E3.4 Nachverfolgbarkeit der neuen fachlichen Bereiche

Die vollständige 89-zeilige Einzelmatrix mit deutschem Inhalt, Nachbarn, Bausteinen, Änderung, Abnahme und Entscheidungsstatus steht in S1.18.1. Diese Übersicht ergänzt die operativen Querverweise, ohne FE neu zu definieren.

| FE-Bereich | Fachliche Verarbeitung und Daten | Bedienung / Betrieb |
|---|---|---|
| FE-27..FE-29, FE-48..FE-52 | UC-59, AF-33, DM-20/21/71, DT-83 | DLG-60, BAT-17, NB-01/03/04 |
| FE-30..FE-32, FE-53..FE-55 | CON-23/24, AF-17..AF-20, NFR-02/05 | NB-08/11, PWA/Hardwaregrenzen |
| FE-33..FE-42 | UC-52/60, DM-03/54/55/68/69/70, DT-67/68/81/82 | DLG-52/61, BAT-14/22/23, SEC-01..SEC-03/15 |
| FE-43..FE-47, FE-50, FE-84..FE-85/89 | UC-56, AF-35, DM-44/62/63, DT-57/74/75 | DLG-43/57, BAT-18/19, NB-05/06/07/09/10/12 |
| FE-56 | Keine aktive Inboxfunktion; manuelle V1-Mitteilungseingabe | P2 NB-05, BAT-02, O-S1-01 |
| FE-57..FE-72 | UC-51..UC-55, AF-28..AF-30, DM-53..DM-61, DT-65..DT-73 | DLG-51..DLG-56, BAT-21/22, SEC-01..SEC-07 |
| FE-73..FE-74 | DM-02/09/25/48, DT-84 | Nutzer-/Kontextsprache, Übersetzungen FR/DE/EN, NFR-08 |
| FE-75..FE-79 | UC-58, AF-32, DM-64..DM-66, DT-77..DT-79 | DLG-59, SEC-08..SEC-11, OUT-01..OUT-08 |
| FE-80..FE-83 | UC-61..UC-63, AF-34, DM-67/68/70, DT-65/80/82 | DLG-62..DLG-64, BAT-16/22/23, SEC-15/16 |
| FE-86..FE-88 | UC-57, AF-31/35, DM-21/22/38/62, DT-74/76 | DLG-58, BAT-20, S1.15, SEC-13 |

## E3.5 Durchgeführte Dokumentationsprüfungen

**Prüfdatum: 16.10.2026.** Folgende Prüfungen wurden auf den tatsächlich gespeicherten Dokumenten ausgeführt. Die Prüfwerkzeuge änderten keine Projektabhängigkeiten oder Anwendungstests.

| Ausgeführte Prüfung | Beobachteter Befund |
|---|---|
| Vollständige Anhangs- und Bestandsaufnahme | Anhang vollständig gelesen; Ausgangsbranch und PR-Git-Ref bei Ausgangs-HEAD. Herold-S1 im dokumentierten Git-Stand gelesen. |
| Kennungsbestand und Definitionstitel gegen Ausgangsdateien | GP 15→15, UC 50→63, AF 27→35, DM 52→71, DT 64→85, DLG 50→64, BAT 19→23, OUT 8→8. Keine alte Definition oder Titelidentität verloren, keine doppelte Definition; neue Kennungen ohne Lücken. |
| P1/P2-Register und Struktur | Alle bisherigen G/CON/SC/AS/R/NG sowie NB/CFG/DK erhalten; neue P1-Register vollständig. Oberstruktur P1.1–P1.10 und P2.1–P2.9 unverändert. NG-01 ausdrücklich historisch aufgehoben. |
| FE-Einzelmatrix | Exakt 89 eindeutige Zeilen, FE-01 bis FE-89 ohne Lücke; 88 fachlich bestätigt, FE-56 ausdrücklich offen. Jede Zeile enthält deutschen Inhalt, Relevanz, NB, Bausteine, Änderung, Abnahmekriterium und Status. |
| NB-Verträge und gemeinsame Grenzen | Zwölf Verträge, je elf Vertragsaspekte und positives/negatives Beispiel. NB-Namen stimmen exakt mit P2 überein. 16 wesentliche negative Grenzfälle als Soll-Verträge nachgewiesen. |
| Integritätsregeln und Referenzen | Alle 25 alten INV-Texte in D1/D2 stimmen nach aktueller Harmonisierung überein; INV-26..31 ergänzen sie. Bekannte Kennungsreferenzen gegen die jeweiligen Definitionsregister geprüft, keine unbekannte Kennung. |
| Markdown-Parser und lokale Verweise | Alle 16 Markdown-Dokumente geparst; 234 relative Links einschließlich vorhandener Abschnittsanker aufgelöst, kein fehlendes Ziel. Geplante S2-/S3-Dateien bleiben unverlinkt. |
| Tabellenprüfung | 412 Markdown-Tabellen erkannt und Spaltenbreiten geprüft; keine inkonsistente Zeile. |
| Mermaid | Alle elf vorhandenen Diagramme mit Mermaid 11.15.0 geparst und im lokalen Chromium als SVG gerendert. Das geänderte P2-Kontextdiagramm zusätzlich visuell geprüft: getrennte Adminrolle, ausgehende Systemmail und nur lesender Fremdspeicher sichtbar. |
| Widerspruchs-/Sprachsuche | Sämtliche Spezifikationsdateien auf überholte Einzelnutzer-V1, GitHub-Kandidat, unbedingte externe Automatik, Inboxrecht, Kalender-Schreibrechte und Kosten-/Schlüsselgrenzen geprüft; gefundene aktuellen Widersprüche korrigiert, verbleibende historische Aussagen ausdrücklich eingeordnet. Durchgängig deutsche KI-Terminologie. |
| Metadaten und Scope | 15 Dokumentversionen/-daten und Prüfstatus abgeglichen; ausschließlich 16 Dateien in docs/spec geändert/neu angelegt. Keine Quellcode-, Manifest-, Lockfile- oder Architekturänderung. |
| Git-Whitespaceprüfung | `git diff --check` erfolgreich. Vor Commit/Push entfernte Branch- und PR-Refs erneut auf unveränderten Ausgangsstand geprüft; main unverändert. |

**Ausführungsgrenze:** Die S1-Abnahmeszenarien und die negativen N1-/N2-Beispiele wurden auf Vollständigkeit und Konsistenz ihrer Spezifikation geprüft. Sie sind keine ausgeführten Produkt-, Sicherheits-, Last-, Geräte- oder Konnektortests. Im Repository existiert kein hierfür konfigurierter Dokumentations-Test-/Lint-Runner; Parser-, Link-, Tabellen-, Kennungs- und Diagrammprüfungen erfolgten mit temporären Werkzeugen. Keine produktiven Daten, Konten oder Dienstzugänge wurden benutzt.

## E3.6 Verbleibende fachliche und technische Grenzen

FE-56 bleibt offen. O-S1-02..O-S1-14 führen EU-Anbieter/Budget, offizielle Providerrechte, Mail-/Pushanbieter, Modelllizenzen und Hardware, PWA-Kompatibilität, Quoten/Fristen, Retryparameter, Schlüsselverteilung/-Recovery, temporäre Cloudklartextbereinigung, endliche sichere Löschmarkierungen/Backupretention, Migration und den sicheren ersten Super-Admin-Bootstrap auf. N1/N2 sind bewusst begrenzte Folgeentwürfe; S2/S3 bleiben geplant. Konkrete technische APIs, Lastmessungen, Securitytests und Produktabnahme stehen aus.

## E3.7 S2-Auftrag, Entscheidungsquellen und Ausgangsstand

Grundlage sind der bestätigte S2-Arbeitsauftrag und die folgenden drei Quellen. Ausgangsstand der Lieferung: `723af7fa1692f8dbaf888b694fa63806d7d5fc5f`; Ergebnis: `53ef171be4783748b5c7e3a84bb0cc363d5b4194`, Spezifikationsbranch und [PR #1](https://github.com/Viny005/syllentra/pull/1).

| Vollständig gelesene Anlage | SHA-256 / Verwendung |
|---|---|
| `PROMPT_CODEX_SYLLENTRA_S2_MIGRATION_COMPLETE_2026-10-16.md` | `60fa38e3efd44d38bad203e3c883120f08a00772e87867b06df9ab1ed1fde6d5` |
| `Syllentra_S2_Datenmigration_v0.1_Entwurf_2026-10-16.md` | `c4b497ea2273ccbe05be128ed383c4afa133d1b4c5aef6a4b9af38166dc6a7a5` |
| `Syllentra_AI_Decisions_V1_Apres_S1_2026-10-16.md` | `1e26677b1396296d9f155c87a5b88b0045c0fd025361b654c4cf68244d39107b` |

Der S2-Entwurf liefert alle 36 MIG-Regeln, 40 AT-S2-Fälle und zwölf O-S2-Punkte. Das ergänzende Entscheidungsregister liefert 25 temporäre DEC-V1-Auditbezüge. Seine frühere offene Exportfrage in Abschnitt G wird durch den ausführbaren S2-Auftrag mit MIG-01/MIG-05 konkretisiert. Die vollständige separate Post-S1-Harmonisierung ist am Ausgangs-HEAD nicht erfolgt; S2 berücksichtigt alle 25 Punkte auf Daten-/Schutzebene, führt aber keine große UI-/Lernalgorithmus-Neuspezifikation durch. Es werden keine neuen FE-Kennungen vergeben.

**Methodischer Nachweis:** Im geprüften Herold-Stand `fce50b47ae646a70bf4d796026dcd1a99d3ae3c2` wurden `docs/spec/SIEDERSLEBEN.md`, Abschnitt „Schnittstellen zu Alt- und Nachbarsystemen“, und `docs/spec/README.md`, Abschnitt S2, gelesen: keine eigene S2-Datei, weil Herold als Greenfield keine Altdaten migriert. Diese projektspezifische Nichtanwendbarkeit wird nicht auf Syllentra übertragen; eine nicht vorhandene Herold-S2-Vorlage wird nicht behauptet.

## E3.8 S2-Datei- und Änderungsmatrix

[S2](S2-datenmigration.md) v0.1 ist neu und erhält alle 17 Ausgangsabschnitte sowie ergänzende Vertrags-/Nachweistiefe. Vorhandene Bausteine werden ausschließlich für nachgewiesene S2-Lücken, klare Zuständigkeiten und korrekte Verweise geändert. Alle Status bleiben „Zur Prüfung durch den Projektinhaber“.

| Datei / Version vorher → aktuell | Tatsächliche Änderung / Begründung |
|---|---|
| S2-datenmigration.md — → 0.1 | Vollständiger Quellentwurf mit 36 MIG, 40 AT-S2, zwölf offenen Punkten; sieben Operationsverträge, 36-zeilige Regel-/Vertrags-/Testzuordnung und 25-zeiliger DEC-Kontextabgleich. |
| P1-ziele-rahmenbedingungen.md 0.6 → 0.7 | S2-Zuständigkeit von nur einmaliger Migration auf eigene Pakete/Restore/Versionswechsel präzisiert; bestehendes G-45/Schutz-/Löschziel vertieft, keine neuen P1-Kennungen. |
| P2-architekturueberblick.md 0.7 → 0.8 | S2-Vertrag und interne Datenwege verlinkt; persönliche Pakete ohne Secrets/aktive Privilegien, Nachbarn bleiben nur lesend. Keine Komponentenarchitektur gewählt. |
| F1-geschaeftsprozesse.md 0.3 → 0.4 | GP-15 auf kontrollierte Wiederverwendung/Portabilität vertieft; Betriebsmigration ist keine automatisch erlaubte Konfiguration. Kein neuer GP. |
| F2-anwendungsfaelle.md 0.2 → 0.3 | UC-49 Export und UC-60 Sicherungsrestore präzisiert; UC-64 eigener Paket-Reimport ergänzt, weil Archivmaterialaufnahme und Backuprestore diesen nicht vollständig abdecken. |
| F3-anwendungsfunktionen.md 0.2 → 0.3 | AF-36 prüft unterstütztes Manifest, Formatabbildung und versioniertes Delta; AF-26 Umfang und AF-34 Löschfilter bleiben zuständig. |
| D1-datenmodell.md 0.2 → 0.3 | DM-72 Portabilitätspaket, DM-73 Migrationslauf, DM-74 MigrationsTeilwirkung ergänzt. DM-50 präzisiert: explizite Auswahl kann null vorhandene Objekte ergeben, konsistent mit bereits erlaubtem leerem OUT-08-Export. Kein pauschales neues Lernoriginal oder dauerhafter Paketinhalt. |
| D2-datentypen.md 0.2 → 0.3 | DT-86 ExportmanifestDT, DT-87 MigrationszustandDT, DT-88 MigrationsdeltaDT, DT-89 MigrationswirkungDT, DT-90 MigrationswegDT ergänzt; konkrete Parser/Kryptographie offen. |
| B1-dialogspezifikation.md 0.2 → 0.3 | DLG-49-Exportzugang ergänzt; DLG-65 für Paket, Importvorschau, Konflikt, Fortschritt und privaten Verlauf mit DE/FR/EN-/Barrierefreiheitsanforderungen. |
| B2-batch.md 0.2 → 0.3 | BAT-24 persönliche Portabilitätsaufträge und BAT-25 geprüfte Versions-/Betriebsüberführung ergänzt; BAT-23 bleibt Sicherung/Restore. Überholte „B3/S1/N1/N2 geplant“-Referenz durch vorhandene Prüfentwürfe ersetzt. |
| B3-druckausgaben.md 0.2 → 0.3 | OUT-08 um Manifest und echten Abdeckungs-/Migrationsbericht vertieft, exportierbare eigene neue Daten berücksichtigt; keine neue OUT-Kennung oder private Adminausgabe. |
| S1-nachbarsysteme.md 0.1 → 0.2 | Ausschließlich S2-Übergabe/Existenz korrigiert; zwölf Nachbarn und gesamte 89-FE-Matrix unverändert. |
| N1-nichtfunktional.md 0.1 → 0.2 | S2-bezogene offene Kapazitäts-, PWA-, Accessibility-, Recovery-/Retentionnachweise auf bestehende NFR bezogen; keine Zahlen erfunden. |
| N2-querschnittskonzepte.md 0.1 → 0.2 | Aktuellen Lösch-/Widerrufskontrollstand, Sicherheitszustandsausschluss, persönliche Schlüssel und Lernheft-/Kalenderschutz auf bestehende SEC bezogen. |
| E2-glossar.md 0.1 → 0.2 | Portabilitätspaket, Manifest, Reimport, Delta, Teilwirkung, Kontrollstand, Cutover, Vorwärtskorrektur, RPO/RTO und Auditkennungen erläutert. |
| E3-pruefnachweis.md 0.1 → 0.2 | S1-Nachweis als Historie erhalten; aktuelle S2-Quellen, tatsächliche Änderungen, Prüfungen, Grenzen und Commitbezüge ergänzt. |
| README.md ohne eigene Version | Alle aktuellen Dokumentversionen/Kennungsumfänge aktualisiert, historische Quellenfassungen ausdrücklich eingeordnet, S2 erst nach tatsächlicher Erstellung als Zur Prüfung verlinkt. S3 bleibt geplant; DEC-V1-Vollharmonisierung gesondert offen. |

**Neue offizielle Kennungen:** UC-64, AF-36, DM-72 bis DM-74, DT-86 bis DT-90, DLG-65, BAT-24 und BAT-25. Keine alten Kennungen oder Definitionstitel neu vergeben. MIG-01 bis MIG-36, AT-S2-01 bis AT-S2-40 und O-S2-01 bis O-S2-12 sind ausschließlich S2-intern; DEC-V1 bleibt temporärer Auditbezug.

**Quellenabgleich/Konflikte:** MIG-11 nennt jetzt ausdrücklich ZIP und 7z, um FE-28 nicht abzuschwächen. MIG-34 verdeutlicht, dass eine Zielwahl keinen V1-Schreibzugriff auf GitHub/Fremdspeicher schafft. MIG-13 erhält lediglich eine grammatische Kasuskorrektur. Alle anderen MIG-Definitionstexte, alle 40 AT-S2-Zeilen und alle zwölf offenen Quellpunkte bleiben inhaltlich erhalten. Die ursprüngliche DM-33/34-Bezeichnung „Lernprofil“ wird in S2.15 zur tatsächlichen pädagogischen Erinnerung korrigiert; Profilpräferenzen gehören zu DM-02. S2.12 verleiht keine neue Automatikberechtigung für manuelle Sitzungen oder den internen Kalender. S2.18.2 enthält die Fundstellen und Auflösung.

## E3.9 Tatsächliche S2-Dokumentationsprüfung

Prüfdatum 16.10.2026. Die folgenden Prüfungen wurden auf den gespeicherten Markdown-Dateien ausgeführt; keine Produktdatenübertragung oder Änderung von Projektabhängigkeiten.

| Ausgeführte Prüfung | Tatsächlicher Befund |
|---|---|
| Anlage/Regel-/Testvergleich | 36 eindeutige MIG, 40 eindeutige AT-S2 und zwölf O-S2 ohne Lücke. Alle 40 AT-S2-Zeilen und alle zwölf offenen Punkte stimmen mit der Anlage überein; MIG-11/34 sind begründet präzisiert, MIG-13 nur grammatisch korrigiert. |
| Regel-/Operations-/Testabdeckung | Alle sieben Wege EXP/IMP/ACA/DEV/BAK/UPG/MOV mit Ein-/Ausgabe, Auslöser/Rechten, Erfolg, Fehlerreaktion, Idempotenz und Rückverweisen. Jede MIG-Regel besitzt eine Zuordnungszeile; alle 40 AT-S2-Fälle werden dort erreicht. Eine zunächst fehlende Zuordnung des Medienquellenfalls wurde ergänzt. |
| Post-S1-Entscheidungskontext | Exakt 25 eindeutige DEC-V1-Zeilen vollständig auf Deutsch abgeglichen; nur S2-Daten-/Schutzfolgen, keine behauptete umfassende Repo-Harmonisierung. |
| Alte/neue Definitionskennungen | GP 15→15, UC 63→64, AF 35→36, DM 71→74, DT 85→90, DLG 64→65, BAT 23→25, OUT 8→8; alle bisherigen Definitionstitel unverändert, neue Kennungen eindeutig und lückenlos an den bisherigen Bereich angeschlossen. |
| Bestehende Regeln und Entscheidungen | Alle G/CON/SC/AS/R/NG-, NB/CFG/DK-/INV-Kennungen erhalten; bestehende INV-Texte in D1/D2 und NFR-/SEC-Definitionen exakt unverändert. Gesamte 89-FE-Matrix in S1 unverändert, FE-56 weiter offen. P1.1–P1.10/P2.1–P2.9 erhalten. |
| Kennungs-/Versions-/Statusbezüge | Verwendete bekannte Kennungsreferenzen gegen Definitionsregister geprüft; alle 16 Dokumentversionen mit README und Prüfstatus abgeglichen. Keine unbekannte Kennung oder übernommene DEC-zu-FE-Umnummerierung. |
| Markdown / Links / Anker | Alle 17 Markdown-Dateien geparst; 297 lokale Links einschließlich Abschnittsanker existieren. Keine Links auf fehlende S3-Datei. |
| Tabellen / Zeichen | 438 Markdown-Tabellen mit konsistenten Spalten geprüft. Unicode ohne Ersatzzeichen, durchgehend KI-Terminologie; Quellcodeblöcke im Parser geprüft. |
| Mermaid | Alle elf Bestandsdiagramme mit den vorhandenen Mermaid-11.15.0-/Chromium-Werkzeugen erfolgreich geparst und gerendert. S2 enthält keine neue Mermaid-Grafik und behauptet keine ungeprüfte Darstellung. |
| Sicherheits-/Semantikreview der Solltexte | Keine Konto-/Rechteübernahme durch Paketbesitz, keine Secrets/aktive Privilegien im persönlichen Export, aktuelle Löschkontrolle vor Restore, keine manuelle Terminverschiebung ohne konkrete Freigabe, keine Wiederbelebung, keine Fremdschreibintegration und keine ungefragte Analysefreigabe. Sollgrenzen anhand der Vertrags- und Abnahmetexte geprüft; kein Produktsicherheitstest. |
| Git / Änderungsscope | Ausschließlich 17 Markdown-Dateien in docs/spec; keine App-, Konfigurations-, Architektur-, Manifest-/Lockfile-, Workflow- oder Dienständerung. `git diff --check` sowie vor Commit die Prüfung des gestagten Diffs erfolgreich. |

**Nicht ausgeführt:** Keine echten Import-/Export-/Restore-, Cloud-, Kryptographie-, Schlüsselverlust-, Kontoisolation-, Browser-/PWA-, Last-, Accessibility- oder Konnektortests; es gibt dafür noch keine implementierte Funktion oder konfigurierte Produkt-Testpipeline in diesem Repository. Die 40 AT-S2-Fälle sind vollständig spezifizierte künftige Abnahmeszenarien, keine 40 erfolgreich ausgeführten Anwendungstests.

## E3.10 S2-Git-Sicherung und offene Grenzen

Historische Lieferbezüge: S1 abgeschlossen mit `723af7fa1692f8dbaf888b694fa63806d7d5fc5f`; S2-Inhalt in `f2e91ca0e273a521b4ad624eaef081420d293e06`, zugehöriger Prüfnachweis in `53ef171be4783748b5c7e3a84bb0cc363d5b4194`. Vorangehende Einzeländerungen bleiben über die Git-Historie nachvollziehbar.

**Weiterhin offen:** O-S2-01 bis O-S2-12 — exakte Export-/Manifest-/Formatprofile, Kryptoverfahren und persönliche Recovery, endliche Marker-/Backup-/Export-/Logfristen, Quoten und reale PWA-Grenzen, sichere Drittadapter, Disaster Restore, Konsistenz/Cutover, starker Altaccountnachweis, rechtliche Exportfähigkeit und EU-Betriebskosten/RPO/RTO. FE-56 bleibt offen und keine V1-Inboxfunktion. Alle 25 DEC-V1-Entscheidungen sind berücksichtigt, ihre vollständige separate Repo-Harmonisierung ist nicht Teil dieser Lieferung. Keine Produkt-, Cloud-, Restore-, Kryptographie-, Security-, Last- oder Browserabnahmetests durchgeführt; keine aktive Produktmigration.

**Freigabestatus:** Zur Prüfung durch den Projektinhaber.

## E3.11 Vier bestätigte Fachentscheidungen — Quelle und Ausgangsstand

Auftrag vom 19.10.2026: L-08 adaptive Lernwiederholung/-planung, L-04 Erinnerungen, L-09 Studienvorgaben und L-02 ablenkungsarmer Lernmodus. Vollständig gelesene Quelle: „Codex-Auftrag — Syllentra AI: Vier bestätigte Fachentscheidungen in die Spezifikation integrieren“, übermittelter Text `Eingefügter Text.txt`, SHA-256 `c68268b759bd0a74d3bda8d09833cd3cd12866d87659899fcd9398b5f5d324a0`.

Ausgangsstand dieser Lieferung: `53ef171be4783748b5c7e3a84bb0cc363d5b4194`; Ergebnis: `0676f791c858765a005a32e2af8c8442eff9712e`. Vier bestätigte Entscheidungen bedeuten weder Gesamtabnahme noch neue FE oder eine Freigabe für Implementierung beziehungsweise Framework-, Datenbank-, Hosting- oder Modellwahl.

## E3.12 Tatsächliche Änderungen und begrenzte Datenmodellergänzung

| Entscheidung | Fachliche Änderung / Zuständigkeit |
|---|---|
| L-08 | Zeitliche Wiederholungsregeln plus Evidenzanpassung; alternative Erklärungen/Übungen bei belegten Schwierigkeiten. UC-23 bis UC-30/UC-32/UC-35/UC-37 präzisiert, AF-09/AF-12/AF-13 und BAT-09/BAT-11 verbunden. Eigene DM-75-Reihenfolge/DM-76-Änderung und BAT-26 für ausdrücklich aktivierte pädagogische Wirkung, keine Kalenderzustimmung. Konflikt-/Aktivierungs-/Undo-Prüfung, Erhalt jüngerer Fortschritte, Formel offen. |
| L-04 | Neuer vollständiger UC-65 mit zentralen persönlichen Regeln DM-77, eindeutiger Vererbung, J−5/J−1, Stundenregel nur bei Uhrzeit, konfigurierbarer Ruhezeit 22:00–08:00, In-App/Verlauf, Kanal-/Geräte-/Digest-/Mailkontrolle. DM-78 trennt externe Nachweise vom bestehenden Hinweis DM-52; BAT-06/07/08/19 erhalten, kein zweiter Zustellbatch. M5/M8 getrennt. |
| L-09 | Neuer vollständiger UC-66 und AF-37; Quellenautorität und persönliche Geltung getrennt nach Hochschule/Studiengang/Ordnung/Kohorte/Inkrafttreten/Übergang. Extraktion bestätigen, Soll/Ist und fehlende Nachweise quellenbezogen anzeigen. DM-04/DM-24 und bestehende Studien-/Quellen-/Leistungsobjekte erweitert; keine unnötige neue Studienvorgabenentität, keine amtliche Anerkennung. Manueller Weg ohne Konnektor. |
| L-02 | Bestehende UC-23/UC-29, DLG-27/31 und AF-12 präzisiert; freiwillige jederzeit beendbare Minimalansicht, optionale Zeitbegrenzung, zurückgestellte nicht dringende Hinweise, Erhalt von Entwürfen/Antworten/Fortschritt, Tastatur/Screenreader und reduzierte Bewegung. Vier Fortschrittsaussagen getrennt; Motivation abschaltbar, kein Ranglisten-/Serien-/Zeitdruckzwang. Kein neuer UC. |

**Abgrenzung neuer Daten:** DM-75/DM-76 sind erforderlich, weil DM-35 ein bestätigter Kalendertermin und DM-39 bis DM-42 ein konkreter Vorschlagsentscheidungs-/Wirkungspfad sind. Keiner dieser Typen darf still zu einer frei automatisch umgeordneten persönlichen Reihenfolge werden. DM-77 ergänzt bislang nicht eigenständig modellierte persönliche Regelvererbung; DM-78 ergänzt fehlende getrennte externe Zustellnachweise. DM-52 bleibt der logische Hinweis mit jetzt expliziter interner Ereignisursache statt einer erfundenen Hochschulquelle; Verlauf und Zustellversuche sind keine doppelten Inhaltskopien. L-09 passt dagegen sauber in bestehende Inhaltsableitung/Studienzugehörigkeit, daher keine neue Entität dafür.

**Aktuelles UC-Verzeichnis:** F2.2 enthielt bislang nur die ursprünglichen 50 Zeilen, obwohl bereits UC-51 bis UC-64 definiert waren. Es wurde ohne Umnummerierung auf sämtliche UC-01 bis UC-66 ergänzt; jede Definition steht weiterhin einmal. Neue Definitionstitel sind exakt „UC-65 — Erinnerungen und Benachrichtigungen verwalten“ und „UC-66 — Studienstruktur mit geltenden Studienvorgaben abgleichen“.

**Neue Kennungen:** UC-65/UC-66, AF-37, DM-75 bis DM-78, DT-91 bis DT-95, DLG-66/DLG-67 und BAT-26. Alle alten Titel/Kennungen und 89-FE-Matrix erhalten, FE-56 offen. Folgende AT-L-Kennungen sind nur lokale künftige Abnahmeanforderungen dieses E3-Nachweises, keine neuen FE oder bereits ausgeführten Produktprüfungen.

## E3.13 Positive und negative Abnahmeanforderungen

| Fall | Gegeben / Aktion | Erwartete Grenze / Ergebnis |
|---|---|---|
| AT-L08-01 | Ausdrücklich aktive Automatik, wiederholt belegte Schwierigkeiten, aktuelle Plan-/Evidenzbasis | Begründete Reihenfolgeanpassung mit Alternativerklärung/geeigneter Übung und Änderungsverlauf, keine Kalenderwirkung. |
| AT-L08-02 | Automatik nie aktiviert; neue Übungsantwort liegt vor | Keine autonome Umordnung; zulässige Empfehlung bleibt möglich, keine fingierte Einwilligung. |
| AT-L08-03 | Manuell fixierter und bereits bestätigter Kalendereintrag kollidiert mit neuer Lernpriorität | Keine Verschiebung/Löschung ohne erforderliche Zustimmung; UC-35/BAT-09-Vorschlagsweg bleibt offen. |
| AT-L08-04 | Nach automatischer Planänderung neue richtige Antwort, anschließend Undo | Nur die gewählte pädagogische Reihenfolgeänderung rücknehmen; jüngere gültige Antwort/Evidenz/Fortschritt erhalten. |
| AT-L08-05 | Plan nach Automatik manuell geändert; altes Undo angefordert | Konflikt sichtbar, keine pauschale Rücksetzung; neue aktuelle Korrektur nötig. |
| AT-L08-06 | Persönliche Automatik zwischen Berechnung und Anwendung deaktiviert | Keine weitere autonome Wirkung, auch nicht durch Wiederanlauf. |
| AT-L08-07 | Verpasste Wiederholung oder keine ausreichende Lernstandsevidenz | Kein erfundener Fehler, kein gesichertes Können/Nullwissen; Unsicherheit, tatsächliche Zeit-/Beleggrundlage sichtbar. |
| AT-L08-08 | Sichere begrenzte Undo-Grundlage kann vor automatischer Änderung nicht bereitgestellt werden | Keine automatische Anwendung ohne die zugesagte Rücknehmbarkeit; nachvollziehbare Einschränkung statt Datenverlust. |
| AT-L04-01 | Ereignisregel überschreibt Kategorie/global, anderes Ereignis unverändert | Effektive Vererbung sichtbar; eigene Punkteliste ersetzt geerbte Liste, explizites Aus reaktiviert keinen Standard. |
| AT-L04-02 | Ruhezeit 22:00–08:00 in gewählter Zone, über Mitternacht fälliger externer Hinweis | Ruhe-/Relevanzprüfung; Dringlichkeit umgeht Datenschutz/Quietregel nicht automatisch; interner Verlauf bleibt verfügbar. |
| AT-L04-03 | Nur Ereignisdatum bekannt, Nutzer wählt Stundenpunkt | Stundenregel bis Uhrzeit-/Zonenklärung nicht wirksam; J−5/J−1 können datumbezogen bleiben, keine erfundene Sendeuhrzeit. |
| AT-L04-04 | OS-Push verweigert und keine Erinnerungsmail aktiviert | Zulässiger In-App-Hinweis verfügbar; kein Push-/Mailrecht erfunden. |
| AT-L04-05 | Zwei Jobs beziehungsweise Retry nach unbekanntem Providerergebnis | Eine logische fachliche Absicht pro Ziel/Kanal, tatsächliche Wirkung zuerst prüfen; Annahme ist weder Auslieferung noch Lesen. |
| AT-L04-06 | Prüfungstermin nur als neuer unbestätigter Vorschlag vorhanden | Gültige bestehende Frist-/Regelbasis unverändert, keine neue Erinnerung zur ungeprüften Zeit. |
| AT-L04-07 | Eigenen Hinweisverlauf löschen, alter Zustelljob läuft später | Keine Wiederanlage/-zustellung gelöschter Meldung und keine Quell-/Termin-/Lernstandslöschung; keine privaten Schatteninhalte. |
| AT-L04-08 | M5-Grundumfang versus M8-Ausbau prüfen | M5 intern/Regeln/In-App/Verlauf; M8 Push/Hauptgerät/Digest/optionale Mail/Nachweise. Nicht entwickelte Funktion nicht als aktiv ausgeben; keine vertrauliche Note in ungeschützter Vorschau. |
| AT-L09-01 | Nutzer stellt rechtmäßig Modulhandbuch/Ordnung manuell bereit, kein Hochschulkonnektor | Unterstützte Extraktion/Geltungsprüfung und bestätigter Soll-Ist-Abgleich nutzbar; kein Pflichtlogin. |
| AT-L09-02 | Ältere Übergangsfassung passt zur Einschreibungskohorte, neuere Fassung betrifft andere Kohorte | Belegte persönliche Geltung entscheidet; neueres Datum verdrängt die alte geltende Fassung nicht. |
| AT-L09-03 | Hochgeladene Datei widerspricht belegter offizieller Quelle | Upload kein Autoritätsvorrang; Widerspruch/Quellenstellen sichtbar und zur Prüfung, keine stille Überschreibung. |
| AT-L09-04 | Kohorte/Übergang oder Extraktionssemantik fehlt | Geltung/Teilabdeckung ungeklärt, kein scheinbar gesicherter Gesamtvergleich oder institutionelle Anerkennung. |
| AT-L09-05 | Prüfungsversuchsnachweis fehlt oder Wahlpflicht-/ECTS-Anrechnung nicht eindeutig | Nicht belegt/nicht prüfbar, keine erfundene Fehlprüfung oder doppelte Anrechnung; Quellen-/Regelbezug erhalten. |
| AT-L09-06 | Regel-/Kontextfassung ändert sich nach Prüfung; vorhandene persönliche Leistungen | Neue Quellen-/Geltungsprüfung erforderlich; Abgleich ändert weder Leistungen noch Kalender ohne genau autorisierten Vorgang. |
| AT-L02-01 | Freiwillig Modus einschalten und jederzeit verlassen, Entwurf/Antwort bereits begonnen | Minimalansicht verlassen ohne Daten-/Fortschrittsverlust und ohne neue Konto-/Anbieterrechte. |
| AT-L02-02 | Normaler Hinweis während Fokus, zugleich notwendiger Sicherheits-/Prioritätshinweis | Nicht dringende Unterbrechung zurückgestellt, erforderlicher Hinweis geschützt erreichbar; keine private Vorschau. |
| AT-L02-03 | Alle Seiten gelesen, keine passende Verständnisprüfung oder Kompetenzbelege | Bearbeitet getrennt von überprüftem Verständnis, geschätztem Wissen und nachgewiesener Kompetenz; kein automatisches Beherrschen. |
| AT-L02-04 | Nur Tastatur/Screenreader beziehungsweise reduzierte Bewegung gewünscht | Bedienpfade, Modusende und Fehlerrückmeldung erreichbar; keine animations-/farbenabhängige Pflichtinformation. |
| AT-L02-05 | Motivation deaktiviert, keine tägliche Serienaktivität | Motivierende Elemente abschaltbar, keine Pflicht-Rangliste, Serie oder künstlicher Zeitdruck. |
| AT-L02-06 | Optionale Zeitbegrenzung läuft ab, Antwort noch nicht abgeschlossen | Entwurf/Antwort/Fortschritt erhalten, kein erzwungener Lernerfolg oder Antwortzwang. |

**Status dieser 28 Fälle:** fachlich nachprüfbare Soll-Abnahmen. Diese Dokumentationslieferung führt keine Anwendungs-, Zustell-, OCR-, LLM-, Pädagogik-, Accessibility- oder Kalenderfunktion aus.

## E3.14 Datei- und Versionsmatrix

| Datei | Version vorher → aktuell | Geänderter Inhalt |
|---|---|---|
| P1-ziele-rahmenbedingungen.md | 0.7 → 0.8 | G-15, CON-15, SC-31 und begrenzte Ziel-/Schutzpräzisierung der vier Entscheidungen. |
| P2-architekturueberblick.md | 0.8 → 0.9 | Persönliche pädagogische Reihenfolge, Kalendergrenze, Hinweis-/Zustellgrenze und geltungsgeprüfter Quellenkontext. |
| F1-geschaeftsprozesse.md | 0.4 → 0.5 | GP-02/GP-04/GP-06 um neue Varianten ergänzt, keine neue Prozesskennung. |
| F2-anwendungsfaelle.md | 0.3 → 0.4 | Vollständiges 66er-Verzeichnis, UC-65/UC-66 und gezielte Präzisierungen bestehender Lern-/Kalender-/Studienfälle. |
| F3-anwendungsfunktionen.md | 0.3 → 0.4 | AF-02/AF-09/AF-12/AF-13 präzisiert; AF-37 Geltungs-/Abdeckungsprüfung. |
| D1-datenmodell.md | 0.3 → 0.4 | DM-04/DM-24/DM-32/DM-35/DM-52 ergänzt, DM-75 bis DM-78 neu. |
| D2-datentypen.md | 0.3 → 0.4 | DT-44 ergänzt, DT-91 bis DT-95 neu; offene Wiederholungsformel, keine technische Schema-/Modellwahl. |
| B1-dialogspezifikation.md | 0.3 → 0.4 | DLG-27/31/32 ergänzt; DLG-66 Erinnerungszentrale und DLG-67 Studienvorgabenabgleich. |
| B2-batch.md | 0.3 → 0.4 | BAT-06/07/08/09/11/19 präzisiert, BAT-26 und eigener nichtkalendarischer Wirkungspfad im Bestandsdiagramm. |
| B3-druckausgaben.md | 0.3 → 0.4 | Bestehende Ausgaben trennen Plan-/Fortschritts-/Quellen-/Hinweisarten und schützen Noten; kein neuer OUT. |
| S1-nachbarsysteme.md | 0.2 → 0.3 | Begrenzte NB-05/NB-09-/UC-65-/UC-66-Vertragsanschlüsse; zwölf Nachbarn und FE-Matrix unverändert. |
| S2-datenmigration.md | 0.1 → 0.2 | Zwei bisher auf separate Lernheft-Harmonisierung verweisende Aussagen an L-08 angepasst; Migration führt keine Automatik aus. MIG-/AT-S2-/O-S2-Register unverändert. |
| N1-nichtfunktional.md | 0.2 → 0.3 | Beleg-/Undo-/Kohorten-/Ruhezeit-/PWA-/Accessibility-Nachweise der vier Entscheidungen. |
| N2-querschnittskonzepte.md | 0.2 → 0.3 | Keine erweiterten Konto-/Kanal-/Kalenderrechte; begrenztes Undo, endliche private Historie und Nichtwiederzustellung. |
| E2-glossar.md | 0.2 → 0.3 | Lernreihenfolge, Hybridwiederholung, Plan-Undo, Hinweise/Zustellung, Studiengeltung und Lernmodus. |
| E3-pruefnachweis.md | 0.2 → 0.3 | Frühere S1/S2-Nachweise als Historie erhalten; Quelle, Änderungen, 28 Sollfälle und tatsächliche Checks fortgeschrieben. |
| README.md | ohne eigene Version | Aktuelle Versionen/Umfänge, UC-65/UC-66 und begrenzten Entwicklungsplan verlinkt. |
| ENTWICKLUNGSPLAN.md | neu 0.1 | Bestätigter Teilstand M2b/M5/M8, frühe Audio-/spätere KI-Notizvorbereitung und getrennte LLM-/Modell-/KI-freie Abhängigkeiten. Kein erfundener freigegebener Gesamtplan. |

**Planungsgrenze:** Vollständiger Meilensteinplan ist im Repository nicht belegt. Nur bestätigte Änderungen UC-09 → M5, grundlegender UC-39 → M2b, interne UC-65-Funktionen → M5 und externe Erweiterungen → M8 sind aufgenommen. Adaptive Funktionen setzen Daten-/Planungs-/Evidenzgrundlagen voraus; weitere Nummern/Termine werden nicht erfunden.

## E3.15 Tatsächliche Dokumentationsprüfungen vom 19.10.2026

Die folgenden Prüfungen wurden auf den gespeicherten Dateien ausgeführt. Es wurden keine Projekt-/Anwendungslaufzeitabhängigkeiten, Dienste oder API-Schlüssel hinzugefügt.

| Ausgeführte Prüfung | Tatsächlicher Befund |
|---|---|
| Offizielles FE-Register | Exakt 89 eindeutige Zeilen in S1.18.1, bytegleiche FE-Zeilen gegenüber Ausgang; FE-56 unverändert offen. Keine neuen FE-Kennungen. |
| Aktuelles UC-Verzeichnis / Definitionen | Exakt 66 eindeutige Verzeichniszeilen UC-01 bis UC-66, dazu 66 eindeutige Definitionstitel; UC-65/UC-66 mit exakten Auftragstiteln. UC-01 bis UC-64 vollständig erhalten, kein Fokus-UC ergänzt. |
| Kennungs-/Titelbestand | GP 15→15, UC 64→66, AF 36→37, DM 74→78, DT 90→95, DLG 65→67, BAT 25→26, OUT 8→8. Alte Definitionstitel unverändert, neue Kennungen ohne Lücke/Doppeldefinition; verwendete bekannte Kennungsreferenzen gegen Register geprüft. |
| Schutz- und Bestandsregister | G/CON/SC/AS/R/NG, NB/CFG/DK/INV erhalten. Bestehende INV-Texte in D1/D2 und SEC-01 bis SEC-16 unverändert. Alle zwölf NB-Namen in P2/S1 identisch. S2-MIG-/AT-S2-/O-S2-Zeilen exakt unverändert. |
| Fachliche Anschlussprüfung | UC-65/UC-66 in F1/F2/F3/D1/D2/B1/B2/B3/S1/N1/N2/E2/E3 und Index verbunden. BAT-09/UC-35 behalten den Kalenderbestätigungspfad; BAT-26 hat eigenen aktivierungs-/revisions-/Undo-geprüften Reihenfolgepfad. Die Kalenderzustimmungsgrenze ist ausdrücklich benannt. |
| Positive/negative Soll-Abnahmen | Acht AT-L08, acht AT-L04, sechs AT-L09 und sechs AT-L02 eindeutig und vollständig dokumentiert; tatsächlich nur Spezifikationsinhalt/Referenzen geprüft, keine 28 ausgeführten Anwendungsfälle behauptet. |
| Meilenstein-/KI-Abhängigkeiten | Neuer Teilplan verwendet nur bestätigte M2b/M5/M8; UC-09/M5, UC-39/M2b und UC-65/M5/M8 konsistent. Audio-/KI-Kern-/Datenabhängigkeiten ohne erfundene weitere Nummern, LLM von Sprach-/OCR-Modellen und KI-freien Funktionen getrennt. |
| Versionen / Status / Struktur | 17 Dokumentköpfe samt Entwicklungsunterlage auf aktuellen Prüfstatus und Version abgeglichen, Index aktualisiert. P1.1–P1.10 und P2.1–P2.9 unverändert. Frühere E3-Nachweise als Historie eingeordnet; keine Gesamtspezifikation freigegeben. |
| Markdown / lokale Links | Alle 18 Markdown-Dateien geparst; 327 lokale Links einschließlich tatsächlich vorhandener Abschnittsanker ohne fehlendes Ziel. Keine fehlende S3-Datei verlinkt. |
| Tabellen / Zeichen | 450 Markdown-Tabellen auf konsistente Spaltenzahl geprüft; Unicode ohne Ersatzzeichen, deutsche KI-Terminologie. Keine ungeprüften neuen Codeblöcke. |
| Mermaid / Sichtprüfung | Alle elf Diagramme mit Mermaid 11.15.0 geparst und lokal als SVG gerendert. Geändertes B2-Diagramm zusätzlich visuell geprüft: Aktivierungszweig, keine automatische Wirkung bei inaktiver Automatik und getrennte Kalenderbestätigung erkennbar. |
| Git / Änderungsscope | `git diff --check` erfolgreich; vor Commit auch gestagter Diff geprüft. Ausschließlich 18 Markdown-Dateien in docs/spec einschließlich neuem Teilplan betroffen; keine App-/Architektur-/Manifest-/Lockfile-/Workflowänderung. |

**Nicht ausgeführt:** Keine realen Anwendungs-, Kalender-, Zustell-, LLM-/OCR-, Wirksamkeits-, Last-, Security- oder Accessibilitytests. Es gibt keine in diesem Dokumentationsauftrag implementierten Funktionen, produktiven Konten oder echten Nutzerdaten als Testgrundlage. Die neuen Abnahmeszenarien und UI-Vorgaben sind künftige Produktnachweise.

## E3.16 Verbleibende offene Punkte und Git-Sicherung

Offen bleiben konkrete Wiederholungsformel, Intervall-/Prioritätsgewichtungen und pädagogische Wirksamkeitsevaluation, unterstützte Extraktionsprofile/Geltungsregeln komplexer Hochschulunterlagen, konkrete Zustell-/Retentions-/Deduplizierungsverfahren sowie tatsächliche Browser-/OS-/Accessibilitynachweise. Zusätzliche Ruhezeitausnahmen werden nicht neu beschlossen. Vollständiger Meilensteinplan und übrige Post-S1-Entscheidungen bleiben getrennt abzugleichen. FE-56 bleibt offen. Keine Anwendungscodeänderung, neue API-Schlüssel, externe Produktintegration, verpflichtende bezahlte API oder technische Stackwahl.

Der Status der Gesamtspezifikation bleibt **Zur Prüfung durch den Projektinhaber**. Git-Veröffentlichung ist keine fachliche Freigabe oder Produktabnahme.

## E3.17 Redaktionelle Bereinigung und Erhaltungsprüfung

**Stand: 19.10.2026.** Grundlage ist der Auftrag „Arbeitsprotokolle vor dem Merge bereinigen“. Überprüfter Ausgangsstand: `39261a5816a99f7c10c79344e5a1adc03b685d49`; dieser enthält die PACE-Einführung über [PR #2](https://github.com/Viny005/syllentra/pull/2). PACE-Regeln und Vorlagen bleiben unverändert.

Erhalten sind die fachlichen Änderungs-/Versionsmatrizen, Quellen einschließlich Prüfsummen und methodischer Referenz, Kennungszuordnungen, historischen Dokumentationsprüfungen, alle 28 Soll-Abnahmen in E3.13 sowie offenen Risiken. Gekürzt sind wiederholte Git-Zwischenstände und Veröffentlichungshinweise; entfernt sind entbehrliche Cache-/Installationsgeschichten und temporäre Arbeitsumgebungsdetails. Die Git-Historie bleibt vollständig erhalten.

Historische GitHub-API-Einschränkungen betrafen den Metadatenzugriff, nicht die fachlichen Prüfergebnisse. Der aktuelle Branch-/PR-Inhaltsstand ist über Git-Refs prüfbar; daraus allein folgt kein API-bestätigter PR-Status. Die inzwischen erfolgte PACE-Integration ist durch den Merge-Commit oben belegt.

**Tatsächlich ausgeführte Prüfungen:**

- Markdown-Parsing aller 29 Markdown-Dateien mit `markdown-it`; 372 lokale Links einschließlich Abschnittsanker und 453 Tabellen ohne Fehler geprüft.
- Vergleich gegen den Ausgangscommit: ausschließlich E3, Spezifikationsindex und die beiden PACE-Kontextdateien geändert; alle übrigen 26 versionierten Dateien bytegleich. Damit bleiben fachliche Anforderungen, Sicherheitsvorgaben, PACE-Anweisungen und Vorlagen unverändert.
- Alle 28 AT-L-Abnahmezeilen wortgleich; 160 historische Tabellenzeilen unverändert, eine fachliche Anschlussprüfungszeile redaktionell gekürzt, ohne fachliche Grenze zu entfernen. Änderungs-/Kennungsmatrizen und Abnahmetabelle vollständig verglichen. Quellenprüfsummen und offene Risiken aus E3.6/E3.10/E3.16 erhalten.
- 89 eindeutige FE und 66 eindeutige UC geprüft, FE-56 weiterhin offen. Referenzierte Kennungen gegen die vorhandenen Nummernkreise geprüft; erhaltene Repository-Commitreferenzen als Git-Commits aufgelöst. Dokumentstatus bleibt zur Prüfung, E3-Version 0.4 im Index konsistent.
- Neue öffentliche Inhalte und Diff auf Geheimnis-/Tokenmuster, private Daten und unzulässige Änderungen geprüft; keine Befunde. `git diff --check` erfolgreich.

Diese Prüfungen belegen Dokumentationskonsistenz und Bestandserhalt. Keine Produkt-, Sicherheits-, Geräte- oder Integrationstests ausgeführt; unveränderte Mermaid-Diagramme wurden in dieser Bereinigung nicht erneut gerendert. Die erforderlichen Produktnachweise aus E3.6, E3.10 und E3.16 bleiben offen.


## E3.18 Aufnahme zweier Release-Checklisten vom 22.10.2026

**Quelle / Umfang:** Der Projektinhaber übernahm zwei Listen mit **20 Sicherheitsprüfungen** und **20 Betriebs-/Performanz-/UX-Prüfungen** und bat um fachlich korrekte Zuordnung zu heutiger Dokumentation und künftigen Umsetzungsschritten. Die 40 Originalpunkte werden einzeln und in Reihenfolge unter `REL-S01..REL-S20` und `REL-Q01..REL-Q20` in [docs/quality/RELEASE_READINESS_40.md](../quality/RELEASE_READINESS_40.md) geführt. N1/N2 wurden um die jeweilige fachliche Einordnung ergänzt, der Index und PACE-Workflow verlinken auf den Nachweiskatalog.

**Abgrenzung:** Es wurden keine FE-, UC-, DM-, DT- oder bestehenden SEC-/NFR-IDs umnummeriert, keine Infrastruktur, kostenpflichtige API, Zahlfunktion oder Stackentscheidung aktiviert und kein Anwendungscode geändert. FE-56 bleibt offen; Zahlungen (REL-Q10) sind kein V1-Ziel. Die bestehenden Fachbausteine bleiben **Zur Prüfung durch den Projektinhaber**.

**Dokumentationskontrollen:** Die Anlage hat genau 20 `REL-Sxx`-Zeilen und 20 `REL-Qxx`-Zeilen, alle eindeutig, und die verlinkten Primärdokumente bestehen im Repository. Weitere vollständige Markdown-/Diff-/Linkprüfungen sind im Abschlussbericht nur anzuführen, wenn sie tatsächlich durchgeführt wurden. **Keine** Authentifizierungs-, Last-, Browser-, Sicherheits-, Backup- oder Wiederherstellungstests wurden im Zuge dieser Dokumentergänzung ausgeführt. Alle produktiven Freigabenachweise bleiben offen.

## E3.19 Mission 2 — Dokumentarische Konsolidierung vom 22.10.2026

**Quelle und Basis:** Nutzerauftrag „Syllentra AI — Mission 2: Consolidation documentaire et harmonisation des décisions“, Abschnitte 1–9, vollständig gelesen; Ausgangscommit `f12a46881f54dccc8568d9982bba0c41564b052e`. Branch und PR-Ref stimmten überein, der Arbeitsbaum war sauber. PR #1 wurde auf der öffentlichen GitHub-Seite als offen, PR #2 als bereits integriert geprüft. Der Auftrag erlaubt Dokumentänderung und normalen Commit/Push auf die bestehende Spezifikationsbranche, keinen Merge oder Infrastrukturtest.

**Korrekturen und Begründungen:**

- DEC-48 und DEC-49 waren am Ausgangsstand nicht vergeben. [ADR-0004/0005](../ARCHITECTURE_DECISIONS.md) dokumentieren bestätigte Hostingbewertungspriorität und unabhängige verschlüsselte EU-Sicherung; technische Auswahl, Kosten-/Kapazitätsnachweise, Schlüssel-/Restoreverfahren und Fristen bleiben offen. Die Anforderungen sind in P1/P2, UC-60, DM-69/DT-81, BAT-23, S1/S2 und begrenzten N1/N2-Anschlüssen verfolgt. Oracle ist kein gewählter Anbieter; 10 EUR brutto/Monat ist kein Ausgabenrecht.
- Die [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md) ordnet alle 25 DEC-V1 bestehenden FE/UC/AF/DM/DT/DLG/BAT/NFR/SEC und lokalen Soll-Abnahmen zu. Wissenskarte, Quellenpassage, freiwillige Rückmeldung, diskrete Hilfe/Pause, Sitzungsbilanz und Wochenziel sind als Varianten vorhandener Fach-/Dialogwege konkretisiert; keine neue Funktion ohne bestätigte Entscheidung und keine zusätzliche UC/AF/DM/DT/DLG/BAT/OUT-Kennung. Algorithmische Parameter, Darstellungsdetails, Messbasis und Produktnachweise bleiben getrennt offen.
- FE-21 ist als Ausgabe-/Hörmodusvariante von FE-20-Eingabe/Sprachdialog getrennt: UC-20, F3.14, DM-02/25/26/48/49, DT-07/61 mit temporärem Wiedergabestand, DLG-26/50 und S1.22. Kein Mikrofonrecht zum Hören, automatische Ausgabe standardmäßig aus, Pause/Fortsetzung/Replay und nur unterstütztes Tempo; Rechte-/Kosten-/Textfallback bleiben erhalten.
- F3-, D1-, D2-, B1- und B2-Kataloge auf die tatsächlich vorhandenen 37 AF, 78 DM, 95 DT, 67 DLG und 26 BAT ergänzt. Alte Kennungen/Titel und Katalogzeilen erhalten; ursprüngliche 50-UC-/52-DM-Matrizen ausdrücklich als historische Ausgangsmatrizen eingeordnet. B3.11/D1.11 und überholte Folgearbeitsbehauptungen aktualisiert, bestehende Dokumente nicht mehr als fehlend ausgegeben.
- Doppelte P2.9.1–P2.9.3-Nachträge nach P2.9.4–P2.9.6 verschoben, frühere Abschnittsanker als kompatible HTML-Anker erhalten; P2.9.7 ergänzt den Bewertungs-/Sicherungskontext. Defekte literale Zeilenumbrüche im PACE-Projektkontext behoben; aktuelle Versionen/Daten/Index und Kontextprotokoll fortgeschrieben. Historische Quellen, Prüfergebnisse und ursprüngliche Freigaben bleiben historisch gekennzeichnet.

**Tatsächliche Dokumentationsprüfungen:**

- Vollständige Markdown-/Link-/Anker- und Tabellenprüfung: 31 Markdown-Dateien, 534 lokale Links einschließlich Abschnittsanker und 463 Tabellen ohne Fehler nach Korrektur des PACE-Tabellenfehlers. Frühere Abschnittsanker zusätzlich gegen die Ausgangsbasis geprüft und erhalten.
- Alle elf vorhandenen Mermaid-Diagramme mit Mermaid 11.15.0 im lokalen Chromium erfolgreich geparst und als SVG gerendert. Anders als beim reinen Node-Parser des Audits ist mit dem vorhandenen Browserwerkzeug eine tatsächliche Prüfung möglich; keine Projektabhängigkeit oder externe Infrastruktur angelegt. Kein Diagrammcode geändert.
- Definitionstitel und vollständige Kataloge abgeglichen: GP 15, UC 66, AF 37, DM 78, DT 95, DLG 67, BAT 26, OUT 8; jeweils eindeutig und lückenlos. Beide Zuordnungstabellen enthalten je genau 25 DEC-V1-Zeilen; 25 lokale AT-DEC-V1 und sechs lokale FE-21-Sollfälle ergänzen die Nachverfolgung, sind keine Produkttests. Alte P2-Anker und eindeutige neue Unterabschnittsnummern geprüft.
- Alle 89 FE-Zeilen, 25 ursprünglichen DEC-V1-Registerzeilen, 36 MIG, 40 AT-S2, zwölf O-S2 und 28 pädagogischen AT-L-Zeilen wortgleich zur Ausgangsbasis. Das gesamte 40-Punkte-Release-Dokument unverändert. G/CON/SC/AS/R/NG-, NB/CFG/DK-, INV-, NFR-/SEC-Bestandsregeln erhalten; aktuelle Kennungsreferenzen gegen Nummernkreise geprüft, kein unbekannter Nummernbereich.
- Metadaten und Dateiumfang geprüft: ausschließlich 23 Markdown-Dateien, einschließlich neuer Matrix, geändert/angelegt; alle übrigen versionierten Dateien unverändert. S3 nicht angelegt, N1/N2 ausschließlich begrenzte Entscheidungs-/Referenzanschlüsse; keine allgemeine Finalisierung oder neue Sicherheitskennungen. Öffentliche Inhalte und Diff auf private Daten, Geheimnis-/Tokenmuster und unerlaubte Änderungen geprüft, keine Befunde. `git diff --check` einschließlich gestagter Änderungen vor Commit erfolgreich.

**Ausführungs- und Abnahmegrenze:** Keine Anwendungs-, TTS-/Mikrofon-, Pädagogik-, Browserprodukt-, Sicherheits-, Last-, Restore- oder Cloudtests durchgeführt. Kein Account, Anbieterzugang, Infrastruktur, kostenpflichtiger Dienst oder Produktcode angelegt. Die Matrix konkretisiert bestätigte Fachziele, ist keine Abnahme oder Implementierung. Die Gesamtspezifikation bleibt **Zur Prüfung durch den Projektinhaber**, FE-56 offen, REL-Q10 außerhalb V1. S3 und die allgemeine N1/N2-Finalisierung bleiben Folgeaufgaben. Technische sowie weitere fachliche Präzisierungen stehen in Matrix Abschnitt 6 und den bestehenden O-S1/O-S2-Registern; die Teilzuordnungen M2b/M5/M8 bleiben erhalten, ein vollständiger Meilensteinplan ist weiterhin nicht belegt. Finalen Commit und Remote-/PR-Git-Stand erst nach normalem Push im Abschlussbericht nennen.
