# E3 — Änderungs- und Prüfnachweis

**Projekt:** Syllentra AI\
**Version:** 0.1\
**Stand:** 16.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

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

**Prüfdatum: 16.10.2026.** Folgende Prüfungen wurden auf den tatsächlich gespeicherten Dokumenten ausgeführt. Prüfskripte, Renderbilder und temporäre Pakete liegen außerhalb des Repositories unter `/tmp`; keine Projektabhängigkeiten oder Anwendungstests wurden geändert.

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

**Werkzeugbefunde:** Die erste temporäre npm-Installation scheiterte am nicht beschreibbaren Standardcache; ein eigener Cache unter `/tmp` behob den Fehler, ohne Projektdateien zu ändern. GitHub-PR-Metadaten über `gh pr view` waren auch nach Wiederholung mit erweitertem Ausführungszugang durch HTTP 403 blockiert. Git-Lesezugriff und Branch-/PR-Git-Refs funktionierten; ein offener PR-Status oder neue API-Rechte werden daraus nicht behauptet. Die PR-Inhalte werden durch normalen Push des bereits zugeordneten Branches aktualisiert; kein neuer PR, Merge oder Force-Push.

## E3.6 Verbleibende fachliche und technische Grenzen

FE-56 bleibt offen. O-S1-02..O-S1-14 führen EU-Anbieter/Budget, offizielle Providerrechte, Mail-/Pushanbieter, Modelllizenzen und Hardware, PWA-Kompatibilität, Quoten/Fristen, Retryparameter, Schlüsselverteilung/-Recovery, temporäre Cloudklartextbereinigung, endliche sichere Löschmarkierungen/Backupretention, Migration und den sicheren ersten Super-Admin-Bootstrap auf. N1/N2 sind bewusst begrenzte Folgeentwürfe; S2/S3 bleiben geplant. Konkrete technische APIs, Lastmessungen, Securitytests und Produktabnahme stehen aus.
