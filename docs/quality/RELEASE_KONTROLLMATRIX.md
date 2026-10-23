# Syllentra AI — konsolidierte Release-Kontrollmatrix

**Version:** 0.3 · **Stand:** 23.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

## 1. Bestand, Zählung und Abgrenzung

Die [40 ursprünglichen Kontrollen](RELEASE_READINESS_40.md) bleiben vollständig, unverändert und in ihrer Reihenfolge erhalten. Dieses Dokument ergänzt ihre Prüfprofile und bewertet die 20 Vorschläge aus Mission 3. Es entstehen **sechs neue eigenständige Kontrollen**, somit **46 insgesamt**: REL-S01..S20, REL-Q01..Q20 und REL-A01/05/07/13/16/18. Elf Vorschläge vertiefen vorhandene Kontrollen, zwei sind Doppelungen und einer ist betriebsabhängig. Kandidaten sind keine zusätzlich gezählten Kontrollen.

Nicht vergebene Kandidatenkennungen: **REL-A02, REL-A03, REL-A04, REL-A06, REL-A08, REL-A09, REL-A10, REL-A11, REL-A12, REL-A14, REL-A15, REL-A17, REL-A19, REL-A20**. Sie bleiben als Herkunftsverweise in Abschnitt 2, ohne eigene Prüfprofile; keine Umnummerierung oder stillschweigende Streichung eines Schutzziels.

Alle 46 Profile: **nicht implementiert, nicht produktgetestet**; gegenwärtig ausschließlich dokumentarisch ausgearbeitet. Die Kategorie „neu“ ist eine fachliche Konsolidierung zur Prüfung, keine neue FE-Entscheidung oder technische Freigabe. „Blocker“ bezeichnet unmittelbare Schutz-/Integritätsverletzung, „Hoch“ eine wesentliche Qualitäts-/Betriebsanforderung. Beide müssen bei Anwendbarkeit erfüllt sein. Eine bedingte Technik hebt ihr zugrunde liegendes Schutzziel nicht auf. Ungeklärte Anwendbarkeit zählt nicht als bestanden.

## 2. Bewertung aller 20 Kandidaten

| Kandidat | Einordnung | Zugeordneter Kontrollpunkt | Begründung / nötige Vertiefung | Anforderungen / S2 |
|---|---|---|---|---|
| REL-A01 | Neuer eigenständiger Kontrollpunkt | REL-A01 | Prompt Injection benötigt einen eigenen Angriffs- und Wirkungsnachweis über allgemeine Eingabeprüfung hinaus. | SEC-17/18; NFR-01 |
| REL-A02 | Bereits abgedeckt, vertiefen | REL-S06 | Werkzeug-/Operations-/Bestätigungsbindung und Rechtewechsel vor Ausführung ergänzen. | SEC-04/18; NFR-07 |
| REL-A03 | Bereits abgedeckt, vertiefen | REL-S04, REL-Q16/19 | Kontext, Embeddings und Inferencebatch in vorhandene Isolationstests aufnehmen. | SEC-19; NFR-01/03; S2.8 |
| REL-A04 | Bereits abgedeckt, vertiefen | REL-Q11, REL-S06/15 | Minimale Payload, freigegebener Provider und unzulässiger Fallback ausdrücklich prüfen. | SEC-20; NFR-05/11 |
| REL-A05 | Neuer eigenständiger Kontrollpunkt | REL-A05 | Quellenbeleg und fachliche Aussagegüte sind durch Datenminimierung nicht geprüft. | NFR-21; SEC-19/20 |
| REL-A06 | Bereits abgedeckt, vertiefen | REL-Q11/16/20, REL-S15 | Transkript-/Zwischenkopien auf sämtlichen Abschluss-/Fehler-/Restorepfaden verfolgen. | SEC-27; NFR-12; S2.7/8 |
| REL-A07 | Neuer eigenständiger Kontrollpunkt | REL-A07 | Dateigrundschutz existiert; ausgehende URL-/DNS-/Redirect-/SSRF-Grenze ist als eigene Angriffsklasse zusätzlich nachzuweisen. | SEC-12/21; NFR-09 |
| REL-A08 | Doppelung, zuordnen | REL-S06 | Rollenisolation ist bereits Teil des serverseitigen Rechtekontrollpunkts; kein zweites Abhaken. | SEC-05/06 |
| REL-A09 | Doppelung, zuordnen | REL-S06 | Feature-Flags sind im Original bereits ausdrücklich serverseitig enthalten. | SEC-07 |
| REL-A10 | Bereits abgedeckt, vertiefen | REL-S03/05/09/19 | Konto-/Dokumentenschlüsselrecovery und Admin-MFA-Verlust als getrennte Missbrauchsfälle ergänzen. | SEC-03/09/22; S2.8 |
| REL-A11 | Bereits abgedeckt, vertiefen | REL-S20 | DEC-49-Unabhängigkeit, getrennte Zugänge/Schlüssel und EU-Belege ausdrücklich aufnehmen. | NFR-04/11; SEC-08/22; S2.8 |
| REL-A12 | Bereits abgedeckt, vertiefen | REL-Q20 | Ausfall des Primäranbieters als zwingender tatsächlicher Restorefall, nicht nur Dateirücklesen. | NFR-04; SEC-25; S2.8 |
| REL-A13 | Neuer eigenständiger Kontrollpunkt | REL-A13 | Vertrauenswürdige Build-/Veröffentlichungskette ist mehr als Secret-/Abhängigkeitsscan. | SEC-23/24; NFR-25 |
| REL-A14 | Bereits abgedeckt, vertiefen | REL-S18 | Modelle, Gewichte, Korpora und Lizenzen zum vorhandenen Komponenten-/Updateinventar ergänzen. | SEC-24; NFR-05/25 |
| REL-A15 | Bereits abgedeckt, vertiefen | REL-Q06/16/19 | Reale Geräte-/OS-/Browserfähigkeiten und Sync-/Konfliktfälle konkretisieren. | NFR-02/03; S2.4/8 |
| REL-A16 | Neuer eigenständiger Kontrollpunkt | REL-A16 | Ganzheitliche Aufgaben-/Kriterienabdeckung ist mit einzelnen zugänglichen Fehler-/Ladezuständen nicht belegt; AA-Ziel bleibt zu bestätigen. | NFR-08/19/20 |
| REL-A17 | Bereits abgedeckt, vertiefen | REL-Q04/06 | DE/FR/EN und unabhängige Ausgabesprachen in vorhandene Zustands-/Fehlerprüfung aufnehmen. | NFR-20; FE-21 |
| REL-A18 | Neuer eigenständiger Kontrollpunkt | REL-A18 | Fachlich bewertete Übungen, Kompetenznachweise und Adaptionsgüte benötigen eine eigene Rubrik. | NFR-22/23/24 |
| REL-A19 | Bereits abgedeckt, vertiefen | REL-Q11/16/20 | S2-Lebenszyklusfälle auf sämtliche Ableitungen, Indizes, KI-Speicher und Backups anwenden. | SEC-11/15/27; NFR-12; S2.7/8 |
| REL-A20 | Bedingt nach aktivierter Betriebsfunktion | REL-Q17/18/20 | Incident-/Rollbackübung wird vor realem Produktivbetrieb verpflichtend; jetzt keine Infrastruktur, kein zusätzlicher Kontrollpunkt. | SEC-25; NFR-17/25; S2.8 |

## 3. Prüfprofile aller 46 eigenständigen Kontrollen

Die Profile konkretisieren das Original, ohne es zu ersetzen. Ein Beleg umfasst immer Version/Funktion, Anwendbarkeit, Sollwert mit Quelle, konkrete Schritte/Befehl, Umgebung, Datum, Istbefund, Status, verantwortliche Person und geschützten Artefaktverweis. Sämtliche Zeit-/Mengen-/Güteschwellen sind nach [N1.10](../spec/N1-nichtfunktional.md#n110-messprotokoll-und-offene-zielwerte) vor einem Abnahmelauf zu bestätigen. [N2](../spec/N2-querschnittskonzepte.md) definiert die Schutzgrenzen, [S2](../spec/S2-datenmigration.md) Migration und Restore. Gemeinsame Freigabe-/Regressions-/Periodikregeln: [Freigabevoraussetzungen](FREIGABEVORAUSSETZUNGEN.md).

### REL-S01

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Offenlegung von Servercredentials |
| Anforderungen | SEC-08/22 |
| Funktionen | Laufzeitkonfiguration, KI-/Konnektorzugang |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Bundle, Konfiguration, Logs und Artefakte mit künstlichen Secrets prüfen |
| Erwartetes Ergebnis | Secrets nur im geschützten vorgesehenen Serverkontext |
| Erforderlicher Beleg | Secretinventar ohne Werte; Scan- und Rechtebefund |
| Verpflichtend ab / erneut | Vor erster Veröffentlichung und Secret-/Konfigurationsänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S02

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Geheimnis bleibt in Git oder Artefakten |
| Anforderungen | SEC-22/23 |
| Funktionen | Repository, Historie, CI |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Versionierte Dateien, gesamte relevante Historie, ignorierte Secretpfade und Veröffentlichungsartefakte scannen |
| Erwartetes Ergebnis | Keine Realgeheimnisse öffentlich; bei Fund Widerruf und Vorfallbehandlung statt bloßem Dateilöschen |
| Erforderlicher Beleg | Scanumfang und bereinigte Befund-/Widerrufsnachweise |
| Verpflichtend ab / erneut | Vor Veröffentlichung, bei Änderungen und nach Secretvorfall |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S03

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Brute Force, OTP-/Recoverymissbrauch |
| Anforderungen | SEC-01/03; NFR-09 |
| Funktionen | Login, Verifikation, Gerätefreigabe, Recovery |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Konto-/IP-/Kontextlimits, verteilte Versuche, Codeablauf und legitimen Recoveryweg testen |
| Erwartetes Ergebnis | Bestätigte Limits wirken; kein Replay; legitime Recovery bleibt sicher möglich |
| Erforderlicher Beleg | Versuchs-/Sperr-/Entsperrprotokolle ohne Codes |
| Verpflichtend ab / erneut | Vor Zugangsfunktion; nach Authänderung und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S04

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Kontenübergreifender Zugriff |
| Anforderungen | SEC-04/19; NFR-01 |
| Funktionen | Daten, Index, KI-Kontext, Jobs, Cache und Restore |
| Kritikalität | Blocker |
| Anwendbarkeit | V1; RLS nur bei gewählter Technik |
| Prüfmethode | A/B-Kennung, Suchfilter, Batchkontext und Storagepfad manipulieren; RLS oder gleichwertige Isolation negativ testen |
| Erwartetes Ergebnis | Kein fremder Inhalt, Metadatum oder Existenzhinweis |
| Erforderlicher Beleg | Mandantenmatrix mit bereinigten Antworten und Speicher-/Indexfällen |
| Verpflichtend ab / erneut | Vor jeder datenführenden Veröffentlichung; relevante Regression |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S05

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Passwort-/Recoverygeheimnisse aus Datenhaltung auslesbar |
| Anforderungen | SEC-01/03/22 |
| Funktionen | Passwortspeicherung, Authentisierung und Recovery |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Speicherschema und Authbibliothek prüfen; künstliche Passwortdaten gegen Klartext/reversible Speicherung untersuchen |
| Erwartetes Ergebnis | Geeigneter adaptiver Hash und geprüfte Implementierung; keine Klartext-/reversible Passwortspeicherung; Accountrecovery kein Schlüsselrecovery |
| Erforderlicher Beleg | Schema-/Konfigurationsreview, künstliche Passwort- und Recoveryfälle |
| Verpflichtend ab / erneut | Vor Identitätsfunktion und Verfahren-/Bibliothekswechsel |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S06

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Horizontale/vertikale Eskalation und unautorisierte Agentenwirkung |
| Anforderungen | SEC-04/05/06/07/13/18 |
| Funktionen | Objekte, Admins, Support, Flags, Werkzeuge und externe Kalender |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Direktaufruf, Selbstbeförderung, zweiten Super Admin, abgelaufenen Grant, deaktiviertes Flag und Rechtewechsel vor Wirkung testen |
| Erwartetes Ergebnis | Aktuelle Serverrechte je Operation; genau ein Super Admin; keine externe Kalenderänderung oder fehlende sensible Bestätigung |
| Erforderlicher Beleg | Operations-/Rollen-/TOCTOU-Matrix; Audit ohne private Inhalte |
| Verpflichtend ab / erneut | Vor jeweiliger Aktivierung; jede Rechte-/Agenten-/Flagänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S07

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Secret im öffentlichen Client |
| Anforderungen | SEC-08/22 |
| Funktionen | Browserbundle, PWA, öffentliche Konfiguration |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Build, Quellmaps, Storage und Netzantworten gegen Konfigurationsklassifikation prüfen |
| Erwartetes Ergebnis | Nur explizit öffentliche Werte; keine Service-/privaten Schlüssel oder fremden Tokens |
| Erforderlicher Beleg | Build-/Netzwerkreview und Secretnegativbefund |
| Verpflichtend ab / erneut | Vor Veröffentlichung und Build-/Konfigurationsänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S08

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Abhören oder unsichere Sitzungsübertragung |
| Anforderungen | SEC-02/08; NFR-11 |
| Funktionen | Browser, API, Integration und Cookies |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Unsichere Protokolle, Mischinhalte, Zertifikatsfehler und Cookieattribute prüfen |
| Erwartetes Ergebnis | Verschlüsselte zulässige Wege; kein stiller Downgrade; sichere Sessioncookies gemäß gewählter Technik |
| Erforderlicher Beleg | Transport-/Cookie-/Fehlerprüfprotokoll |
| Verpflichtend ab / erneut | Vor Netzfreigabe; nach Netz-/Authänderungen und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S09

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Fortgeltung entwendeter/entzogener Sessions |
| Anforderungen | SEC-02/03; NFR-03 |
| Funktionen | Sessions, Geräte, Sperre und Recovery |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Ablauf, Logout, Rotation, Geräteentzug und lokale Entsperrung bei abgelaufener Serversitzung testen |
| Erwartetes Ergebnis | Alte Rechte nicht nutzbar; lokale Entsperrung erzeugt keine Serverrechte |
| Erforderlicher Beleg | Session-/Gerätezustände und negative Folgeaufrufe |
| Verpflichtend ab / erneut | Vor Anmeldung/Sync; nach Sitzungsänderung und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S10

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Injektion, fehlerhafte Werte und unsichere Ausgabe |
| Anforderungen | SEC-12/18/21 |
| Funktionen | API, Markdown, Konfiguration, Importmetadaten, Toolparameter |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Schema-, Grenz-, Skript-/HTML-/Formel- und Ausgabeinjektionsfälle einschleusen |
| Erwartetes Ergebnis | Server lehnt Ungültiges ab; keine Ausführung aus Inhalt; sichere Darstellung und strukturierte Fehler |
| Erforderlicher Beleg | Versionierter Eingabe-/Ausgabekorpus und beobachtete Antworten |
| Verpflichtend ab / erneut | Vor betroffenen Eingabefunktionen; Parser-/Rendereränderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S11

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unbegrenzte Aufnahme und Archivverarbeitung |
| Anforderungen | NFR-09/15; SEC-12 |
| Funktionen | Uploads, Medien, Archive und Quoten |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Große/rekursive Archive, entpackte Menge, Abbruch und Grenzwerte vor/während Verarbeitung testen |
| Erwartetes Ergebnis | Bestätigte Limits durchgesetzt; bestehende Daten bleiben les-/exportierbar; keine unbeschränkte Verarbeitung |
| Erforderlicher Beleg | Grenzwert- und Verbrauchsprotokoll mit bestätigten Sollwerten |
| Verpflichtend ab / erneut | Vor Import/Medienfunktion; nach Format-/Limitänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S12

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Aktiver oder getarnter Dateiinhalt |
| Anforderungen | SEC-12/21 |
| Funktionen | Datei-/Archivimport und Vorschau |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Falsche MIME/Endung, tatsächliche Signatur, Pfadflucht, Bomben und aktive Inhalte testen |
| Erwartetes Ergebnis | Erlaubte Formate inhaltlich geprüft; keine Pfadflucht oder Programmausführung |
| Erforderlicher Beleg | Dateikorpus, Isolations- und Parserbefunde |
| Verpflichtend ab / erneut | Vor Import/Vorschau; Parser-/Formatwechsel |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S13

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unerlaubter Browserursprung oder CSRF |
| Anforderungen | SEC-04/08/12 |
| Funktionen | Cross-Origin-API und zustandsändernde Browseraufrufe |
| Kritikalität | Blocker |
| Anwendbarkeit | Bedingt V1 nach Architektur; CSRF-Risiko separat prüfen |
| Prüfmethode | Nicht erlaubte Origins/Methoden/Header, Credentialkombination und gefälschte Zustandsänderung testen |
| Erwartetes Ergebnis | Nur erlaubte Aufrufe; kein Wildcard mit Credentials; passender CSRF-Schutz |
| Erforderlicher Beleg | API-/Originmatrix und CSRF-Negativfälle oder begründete Nichtanwendbarkeit |
| Verpflichtend ab / erneut | Vor betroffener API; Origin-/Sessionänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S14

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Interne Details in öffentlichen Fehlern |
| Anforderungen | SEC-14; NFR-18 |
| Funktionen | API, UI, Datei-/Modellfehler |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Parser-, Datenbank-, Auth- und Providerfehler gezielt auslösen |
| Erwartetes Ergebnis | Keine Stacktraces, SQL, internen Pfade oder Geheimnisse öffentlich; sichere Korrelation möglich |
| Erforderlicher Beleg | Bereinigte Fehlerantworten und interne Zugriffskontrolle |
| Verpflichtend ab / erneut | Vor Veröffentlichung; Fehlerpfadänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S15

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Privatdaten/Secrets in Konsole oder Diagnose |
| Anforderungen | SEC-14/20/27; NFR-10 |
| Funktionen | Browser-, Server-, Job-, KI- und CI-Logs |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Künstliche private Texte und Secrets über Erfolg, Fehler, Debug und Crash verfolgen |
| Erwartetes Ergebnis | Keine unnötigen Inhalte/Secrets; notwendige Metadaten datensparsam und endlich |
| Erforderlicher Beleg | Logfeldinventar, Scan und Retentionstest |
| Verpflichtend ab / erneut | Vor Veröffentlichung; Log-/Provider-/Jobänderung und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S16

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Kontenexistenzleak oder unverständliche Fehler |
| Anforderungen | SEC-01/14; NFR-18/20 |
| Funktionen | Login/Recovery sowie allgemeine UI |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Existierendes/nicht existierendes Konto vergleichen; übrige Fehleraufgaben DE/FR/EN prüfen |
| Erwartetes Ergebnis | Keine hilfreichen Kontenexistenzsignale; andere Fehler bleiben verständlich und zustandsspezifisch |
| Erforderlicher Beleg | Anti-Enumeration-Befunde inkl. relevanter Seiteneffekte; Sprachfälle |
| Verpflichtend ab / erneut | Vor Auth-/UI-Freigabe; Text-/Authänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S17

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Gefälschter oder wiederholter Webhook |
| Anforderungen | SEC-04/13; NFR-07 |
| Funktionen | Eingehende Webhooks falls gewählt |
| Kritikalität | Blocker |
| Anwendbarkeit | Bedingt; keine Webhookfunktion vorausgesetzt |
| Prüfmethode | Signatur/Quelle verändern, alte Nachricht replayen, doppelt/ungeordnet liefern |
| Erwartetes Ergebnis | Nur gültige aktuelle berechtigte Wirkung, keine Duplikate |
| Erforderlicher Beleg | Signatur-/Replay-/Idempotenzfälle oder begründete Nichtanwendbarkeit |
| Verpflichtend ab / erneut | Vor Webhookaktivierung; Schlüssel-/Handleränderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S18

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Schwachstellen, manipulierte Komponenten und Lizenzkonflikt |
| Anforderungen | SEC-24; NFR-05/25 |
| Funktionen | Code, Abhängigkeiten, Images, Modelle, Gewichte und Konnektoren |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Version/Herkunft/Hash/Lizenz und transitive Abhängigkeiten inventarisieren; Befunde bewerten und Updates regressiv prüfen |
| Erwartetes Ergebnis | Keine ungeklärte blockierende Schwachstelle/Manipulation oder unzulässige notwendige Lizenz |
| Erforderlicher Beleg | Komponenten-/Modellinventar, Quellen und Update-/Schwachstellenbericht |
| Verpflichtend ab / erneut | Vor Auswahl/Release; bei Updates und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S19

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unverifizierter Erstzugang |
| Anforderungen | SEC-01/03 |
| Funktionen | Registrierung, OTP und erster Appdatenzugang |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Unverifiziert gegen Datenendpunkte; falsche, abgelaufene und wiederverwendete OTP prüfen |
| Erwartetes Ergebnis | Verifikations-/Recoveryweg begrenzt; erst bestätigte E-Mail erlaubt Appdatenzugang |
| Erforderlicher Beleg | Verifikations- und Replay-Negativfälle |
| Verpflichtend ab / erneut | Vor Registrierung; Authregression |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-S20

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unbrauchbare oder abhängige Sicherung |
| Anforderungen | SEC-08/15/22/25; NFR-04/11/12 |
| Funktionen | Automatische verschlüsselte unabhängige EU-Sicherung nach DEC-49 |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 vor Produktion |
| Prüfmethode | Region, getrennte Zugänge/Schlüssel, automatischen Lauf, Retention, Primäranbieterabhängigkeit und Löschstand prüfen |
| Erwartetes Ergebnis | Sicherung unabhängig abruf-/entschlüsselbar; endliche Fristen; kein Wiederaufleben alter Rechte/Daten; Ziele bestätigt |
| Erforderlicher Beleg | Backup-/Abhängigkeits-/Schlüsselmatrix und Laufbelege; S2/DEC-49 |
| Verpflichtend ab / erneut | Vor erster Produktion; nach Backup-/Schlüsseländerung und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q01

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Überlast oder missbräuchlicher Ressourcenverbrauch |
| Anforderungen | NFR-09/14/15; SEC-18 |
| Funktionen | API, KI, Import, Suche und Jobs |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Konten mit verschieden großen Lasten und Missbrauchsmustern gegeneinander prüfen |
| Erwartetes Ergebnis | Bestätigte Limits/Fairness wirken; kein unbeschränktes Inference-/Queuewachstum |
| Erforderlicher Beleg | Lastprofil, Verbrauch und Ablehnungs-/Fairnessbericht |
| Verpflichtend ab / erneut | Vor jeweiliger Aktivierung; Last-/Limit-/Modelländerung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q02

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unbegrenzte externe Aufrufe/Parallelität |
| Anforderungen | NFR-06/09/14/15; SEC-13/18 |
| Funktionen | Konnektoren, Inference, Warteschlangen |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Zeit-/Mengen-/Parallelitätsbudget erschöpfen; widerrufene Verbindung vor Retry |
| Erwartetes Ergebnis | Begrenzte Last und aktuelle Rechte; externe Limits respektiert; kein stiller kostenpflichtiger Fallback |
| Erforderlicher Beleg | Budget-/Queue-/Verbindungsprotokolle |
| Verpflichtend ab / erneut | Vor betreffendem Dienst; Budget-/Retryänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q03

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Nicht genehmigte Ausgabe oder Pflicht-Pay-API |
| Anforderungen | NFR-05/15; SEC-18/20 |
| Funktionen | Infrastruktur-/KI-Verbrauch und optionale externe Wege |
| Kritikalität | Blocker |
| Anwendbarkeit | V1; keine Ausgabe autorisiert |
| Prüfmethode | Kostenpfad ohne/mit abgelaufener Freigabe; Gratislimit erschöpfen; automatische Ausweichwahl versuchen |
| Erwartetes Ergebnis | Keine Ausgabe ohne ausdrückliche passende Autorisierung; kostenpflichtiger Weg stoppt; keine verpflichtende bezahlte API |
| Erforderlicher Beleg | Kosten-/Einwilligungsmatrix, Grenz-/Fallbackfälle |
| Verpflichtend ab / erneut | Vor kostenrelevantem Weg; Preis-/Modell-/Providerwechsel |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q04

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unverständliche/fehlende mehrsprachige Fehlermeldung |
| Anforderungen | NFR-08/18/20 |
| Funktionen | UI DE/FR/EN und unabhängige Ausgabesprachen |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Kernfehler in jeder Sprache und verschiedenen Sprachkombinationen auslösen |
| Erwartetes Ergebnis | Fachlich gleiche handlungsfähige Meldung; keine Secretdetails oder fehlenden Übersetzungsschlüssel |
| Erforderlicher Beleg | Sprach-/Fehlermatrix, fachliches Textreview |
| Verpflichtend ab / erneut | Vor UI-Freigabe; Text-/Lokalisierungsänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q05

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unsichtbare lange Arbeit oder ungewollter Mehrfachstart |
| Anforderungen | NFR-08/13/14/18 |
| Funktionen | Asynchrone Vorgänge, Fortschritt und Abbruch |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Lange/stehende Jobs mit Tastatur/Screenreader bedienen; erneuten Start und Abbruch testen |
| Erwartetes Ergebnis | Zustand zugänglich und wahr; keine unkontrollierte Doppelwirkung; Abbruch nach fachlich definierter Grenze |
| Erforderlicher Beleg | Zeit-/Fortschritts-/Bedienprotokoll |
| Verpflichtend ab / erneut | Vor Jobfunktion; Zustands-/Queueänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q06

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Falsche Zustandsanzeige oder verdeckte Einschränkung |
| Anforderungen | NFR-02/03/17/18/20 |
| Funktionen | PWA, Offline, Leer-/Rechte-/Flag-/Störungszustand |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | OS-/Browsermatrix, fehlende Fähigkeiten, Offline und deaktivierte Funktionen in DE/FR/EN prüfen |
| Erwartetes Ergebnis | Begrenzungen sichtbar; sichere brauchbare Rückwege; keine falsche Verfügbarkeit |
| Erforderlicher Beleg | Geräte-/Fähigkeits-/Sprach-/Zustandsmatrix |
| Verpflichtend ab / erneut | Vor Client-/Funktionsfreigabe; Browser-/PWA-/Flagänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q07

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Retry nach Entzug oder doppelte Wirkung |
| Anforderungen | NFR-06/07; SEC-13/18 |
| Funktionen | Imports, Agenten, Integration und Hintergrundjobs |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Transient/permanent, Scopeentzug, Kostenänderung und Abbruch nach Erfolg unterscheiden |
| Erwartetes Ergebnis | Begrenzter Backoff; je Versuch aktuelle Rechte/Kosten; keine doppelte Wirkung oder Endlosschleife |
| Erforderlicher Beleg | Retry-/Wirkungs-/Entzugsfälle mit Zustandsfolge |
| Verpflichtend ab / erneut | Vor Wiederholungsfunktion; Job-/Rechteänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q08

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Hängende oder ungeklärt wiederholte Operation |
| Anforderungen | NFR-07/13/17; SEC-13 |
| Funktionen | API, Modell, Export und Jobs |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Langsame/nie antwortende Abhängigkeit und Timeout nach externer Wirkung simulieren |
| Erwartetes Ergebnis | Bestätigte Fristen; ehrlicher unbekannter Ausgang; Abgleich vor Wiederholung |
| Erforderlicher Beleg | Zeit-/Status-/Wirkungsspuren mit bestätigtem Timeout |
| Verpflichtend ab / erneut | Vor Abhängigkeit; Timeout-/Provideränderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q09

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Doppelte Daten/Plan-/Lernwirkung |
| Anforderungen | NFR-07/24; SEC-18 |
| Funktionen | Formulare, Import, Sitzung, Bestätigung und Jobstart |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Parallele identische Requests, Klick-/Netzretry und Replay |
| Erwartetes Ergebnis | Serverseitig genau zulässige beabsichtigte Wirkung; keine doppelte Anrechnung; Rechte erneut geprüft |
| Erforderlicher Beleg | Idempotenz-/Zähler-/Raceprotokoll |
| Verpflichtend ab / erneut | Vor schreibender Funktion; Transaktions-/Deduplizierungsänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q10

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Doppelte Zahlung |
| Anforderungen | NFR-07; SEC-18 |
| Funktionen | Nur später eigens genehmigte Zahlungsfunktion |
| Kritikalität | Blocker |
| Anwendbarkeit | Nicht V1; spätere ausdrückliche Entscheidung nötig |
| Prüfmethode | Erst nach Fachfreigabe Transaktion, Callback, Replay und Abstimmung prüfen |
| Erwartetes Ergebnis | Keine Doppelzahlung; gegenwärtig keine Zahlung implementieren/aktivieren |
| Erforderlicher Beleg | Spätere Transaktions-/Webhookbelege; aktuell dokumentierte Nichtanwendbarkeit |
| Verpflichtend ab / erneut | Vor späterer Zahlungsaktivierung; nicht als V1-Produkttest ausgeben |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q11

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unnötige private Datenübertragung oder Schattenkopien |
| Anforderungen | NFR-10/11/12; SEC-10/11/20/26/27 |
| Funktionen | Client, API, Suche, Modell, Logs, Transkripte und Exporte |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | Payloads und temporäre Kopien je Quelle/Zweck/Kategorie verfolgen; verbotenen Provider und Fehler-/Crashpfad prüfen |
| Erwartetes Ergebnis | Nur erforderliche zulässige Daten; temporäre Transkripte bereinigt; keine dauerhafte Rohtextschattenhistorie |
| Erforderlicher Beleg | Datenfluss-/Temporärspeichermatrix, minimale Payload-/Bereinigungsbelege |
| Verpflichtend ab / erneut | Vor Datenverarbeitung; Datenfluss-/Provider-/Retentionänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q12

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unbrauchbare Abfrageleistung oder falsche Indexrechte |
| Anforderungen | NFR-13/16; SEC-19 |
| Funktionen | Suche, Module, Projekte, Gespräche und Verlauf |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Repräsentative Bestände steigern; Queryplan/Index und Rechteänderung messen |
| Erwartetes Ergebnis | Bestätigte Zeit-/Aktualitätsziele; keine fremden oder gesperrten Treffer |
| Erforderlicher Beleg | Query-/Indexmessung, Referenzergebnisse und Rechtefälle |
| Verpflichtend ab / erneut | Vor Suche/Listennutzung; Schema-/Indexänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q13

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unbegrenzte Listen oder Rechteleck auf Folgeseiten |
| Anforderungen | NFR-09/16; SEC-04 |
| Funktionen | Listen, Suche, Audit, Materialien und Verlauf |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Große Bestände, manipulierte Seitenzeiger und parallele Löschung/Rechtewechsel |
| Erwartetes Ergebnis | Begrenzte Ausgabe; aktuelle Rechte jeder Seite; nachvollziehbare Sortierung ohne stille Datenverwechslung |
| Erforderlicher Beleg | Pagination-/Grenz-/Rechteprotokoll |
| Verpflichtend ab / erneut | Vor Listenfreigabe; Pagination-/Sortieränderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q14

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unnötiger Netz-/CPU-Verbrauch oder Kompressionsseitenkanal |
| Anforderungen | NFR-13/15; SEC-08/12 |
| Funktionen | Antworten und Datei-/Medientransfer |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 nach Medien-/Transportauswahl |
| Prüfmethode | Komprimierbare/unpassende Formate vergleichen; reflektierte Secrets und CPUspitzen berücksichtigen |
| Erwartetes Ergebnis | Angemessene sparsame Übertragung ohne Schutzverlust; keine blinde Doppelkompression; Nebenkanalrisiko beherrscht |
| Erforderlicher Beleg | Format-/Größen-/CPUvergleich und Sicherheitsreview |
| Verpflichtend ab / erneut | Vor betroffener Übertragung; Format-/Transportänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q15

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Parser-/Speicherüberlast bei parallelem Upload |
| Anforderungen | NFR-09/14/15; SEC-12 |
| Funktionen | Import und Medien unter Last |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Datei-/Entpackgrößen, Abbruch und konkurrierende Konten unter realen Ressourcengrenzen messen |
| Erwartetes Ergebnis | Bestätigte Limits; keine endlosen temporären Kopien; faire Kernbedienung bleibt innerhalb Ziele |
| Erforderlicher Beleg | CPU-/RAM-/Speicher-/Queue- und Abbruchbericht |
| Verpflichtend ab / erneut | Vor Import; Parser-/Kapazitäts-/Limitänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q16

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Fremde/veraltete oder gelöschte Cache-/Offlineinhalte |
| Anforderungen | NFR-01/03/12/16; SEC-11/15/19/27 |
| Funktionen | PWA, Retrieval, Vorschau, Transkripte und Cache |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 |
| Prüfmethode | A/B-Wechsel, Entzug, Ablauf, Quellschutzänderung, Löschung, Altclient und Indexneubau |
| Erwartetes Ergebnis | Keine Kontenvermischung oder Wiederbelebung; bestehende Offlinekopien ehrlich begrenzt; temporäre Kopien endlich |
| Erforderlicher Beleg | Cache-/Index-/Offlinelifecycles und Lösch-Negativfälle |
| Verpflichtend ab / erneut | Vor Cache/Offline; Speicher-/Sync-/Retentionänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q17

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Ausfall unbemerkt oder ohne Verantwortliche |
| Anforderungen | NFR-17; SEC-25 |
| Funktionen | Erreichbarkeit, kritische Pfade und Alarmierung |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 vor Produktion |
| Prüfmethode | Dienstausfall/Modellstörung synthetisch auslösen; Alarm und Reaktionszuordnung verfolgen |
| Erwartetes Ergebnis | Bestätigte Erkennungs-/Reaktionsziele; keine privaten Inhalte im Monitoring; zuständige Person erreichbar |
| Erforderlicher Beleg | Alarm-/Ausfallzeitlinie und Kontakt-/Rollenbeleg |
| Verpflichtend ab / erneut | Vor erster Produktion; Monitoringänderung und periodische Übung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q18

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Nicht diagnostizierbare oder zu offene Betriebsfehler |
| Anforderungen | NFR-10/17; SEC-14/25 |
| Funktionen | Fehlerlogs, Audit und Incidentdiagnose |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 |
| Prüfmethode | Fehler über Request/Jobkorrelation verfolgen; fremden Zugriff, Secretfeld und Retentionsablauf prüfen |
| Erwartetes Ergebnis | Nötige sichere Metadaten, begrenzter Zugriff/Frist; Vorfall nachvollziehbar ohne Privattext |
| Erforderlicher Beleg | Korrelations-/Zugriffs-/Retentionsbefund und bereinigte Incidentzeitlinie |
| Verpflichtend ab / erneut | Vor Produktion; Loggingänderung und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q19

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Racebedingungen, Lastversagen und Kontenvermischung |
| Anforderungen | NFR-01/03/13/14/15/24; SEC-04/19 |
| Funktionen | Mehrnutzer-Auth, Upload, Suche, KI, Sync, Quoten und Jobs |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 vor Freigabe |
| Prüfmethode | Bestätigtes Lastprofil mit A/B, gleichem Material, Paralleländerung, Doppelabgabe und Gerätewechsel ausführen |
| Erwartetes Ergebnis | Isolations-/Konsistenzregeln ohne Ausnahme; bestätigte Kapazitäts-/Zeitziele erfüllt |
| Erforderlicher Beleg | Lastprofil, Rohmessungen, Race-/Mandantenmatrix |
| Verpflichtend ab / erneut | Vor erster Freigabe; relevante Parallelitäts-/Daten-/Modelländerung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-Q20

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Sicherung nicht wiederherstellbar oder alte Rechte/Daten aktiv |
| Anforderungen | NFR-04/11/12; SEC-09/15/22/25/27 |
| Funktionen | Unabhängiger Restore, Export/Import, Derivate und Konto-/Schlüsselverlust |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 vor Produktion |
| Prüfmethode | Primäranbieter verlieren; unabhängige Sicherung mit/ohne Schlüssel, endgültig gelöschten Daten, A/B und aktuellem Kontrollstand restaurieren |
| Erwartetes Ergebnis | Integrität und bestätigte RPO/RTO; keine Rechte-/Löschwiederbelebung; fehlender persönlicher Schlüssel nicht erschlichen |
| Erforderlicher Beleg | Tatsächlicher Restorevergleich, Messwerte und aktuelle Kontrollstand-Negativfälle; S2 |
| Verpflichtend ab / erneut | Vor Produktion; Backup-/Schlüssel-/Formatänderung und periodisch |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-A01

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Prompttext steuert Rechte, Werkzeuge oder Datenabfluss |
| Anforderungen | SEC-12/17/18; NFR-01 |
| Funktionen | Nutzerprompt, RAG, Dokumente, Audio, Webseite und Repository |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 vor KI-/Agentenaktivierung |
| Prüfmethode | Direkte/indirekte mehrsprachige, kodierte und mehrstufige Injectionfälle; tatsächliche Tool-/Datenwirkung beobachten |
| Erwartetes Ergebnis | Keine Rechteausweitung, fremden Daten, Secretweitergabe oder unbestätigte sensible Wirkung; Restbefunde dokumentiert |
| Erforderlicher Beleg | Versionierter Angriffskorpus, Modell-/Promptfassung und Wirkungsprotokoll |
| Verpflichtend ab / erneut | Vor KI-Aktivierung; Modell-/Prompt-/Tool-/Retrievaländerung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-A05

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Erfundene oder nicht belegende pädagogische Quellen |
| Anforderungen | NFR-21; SEC-19/20 |
| Funktionen | Erklärungen, Zitate, Studienvorgaben und Zusammenfassungen |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 vor beleggestützter KI-Ausgabe |
| Prüfmethode | Referenzkorpus mit fehlenden/widersprüchlichen Quellen; Quellenstelle und Aussagebezug menschlich prüfen |
| Erwartetes Ergebnis | Quelle/Fassung/Stelle erreichbar und berechtigt; Unsicherheit klar; bestätigte Güterubrik erfüllt, keine erfundene Anerkennung |
| Erforderlicher Beleg | Korpus, Herkunft, fachliche Bewertungen und Fehlerrubrik |
| Verpflichtend ab / erneut | Vor Ausgabe; Modell-/Prompt-/Retrieval-/Quelllogikänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-A07

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Dokument-/URLimport kompromittiert Parser oder internes Netz |
| Anforderungen | SEC-12/21; NFR-09 |
| Funktionen | Datei, Archiv, Webseite, Repository und serverseitige URLabrufe |
| Kritikalität | Blocker |
| Anwendbarkeit | V1; SSRF-Teil vor serverseitigem Abruf |
| Prüfmethode | Bomben/Pfadflucht/aktive Inhalte plus interne/Loopback/Link-Local-/Metadatenziele, DNSwechsel und Redirects |
| Erwartetes Ergebnis | Keine fremde Codeausführung; keine unautorisierten internen Abrufe; Format-/Größen-/Netzgrenzen wirksam |
| Erforderlicher Beleg | Angriffskorpus, Parser-/Ressourcen-/Netzwerkbelege |
| Verpflichtend ab / erneut | Vor Import/Abruf; Parser-/URL-/Netzänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-A13

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Manipulierter Build/Release oder Secretzugang durch fremden PR |
| Anforderungen | SEC-22/23/24; NFR-25 |
| Funktionen | CI/CD, Build, Artefakt, Abhängigkeiten und Release |
| Kritikalität | Blocker |
| Anwendbarkeit | V1 sobald Apppipeline/Produktveröffentlichung vorgesehen |
| Prüfmethode | Untrusted-PR, Artefaktvertauschung, fehlende Freigabe und überbreite Pipelineberechtigung simulieren |
| Erwartetes Ergebnis | Keine Produktionssecrets für untrusted Code; nachvollziehbarer Quell-/Build-/Artefaktbezug; nur geprüftes Artefakt freigebbar |
| Erforderlicher Beleg | Berechtigungs-/Provenienz-/Manipulationsbefunde und Releasezuordnung |
| Verpflichtend ab / erneut | Vor Pipeline-/Produktveröffentlichung; Pipeline-/Build-/Berechtigungsänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-A16

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Unzugängliche Kernabläufe und unbelegte WCAG-Behauptung |
| Anforderungen | NFR-08/19/20 |
| Funktionen | UI inklusive Auth, Administration, Lernen und Medien |
| Kritikalität | Hoch |
| Anwendbarkeit | V1: Grundzugänglichkeit verbindlich; WCAG 2.2 AA als Ziel ausdrücklich zu bestätigen |
| Prüfmethode | Automatisierte Hinweise plus manuelle Tastatur-, Screenreader-, Kontrast-, Reflow/Zoom-, Fokus-, Bewegungs- und Fehlerprüfung |
| Erwartetes Ergebnis | NFR-08 erfüllt; nach Zielbestätigung alle anwendbaren A/AA-Kriterien geprüft; keine unbelegte Konformitätsbehauptung |
| Erforderlicher Beleg | Seiten-/Aufgaben-/Kriterienmatrix, Assistenzversionen, Defekte und Nachprüfungen |
| Verpflichtend ab / erneut | Vor UI-Freigabe; Zielentscheidung vorher, UI-/Authänderung und periodische Stichprobe |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

### REL-A18

| Merkmal | Prüfprofil |
|---|---|
| Risiko | Fehlerhafte Korrektur oder fingierter Kompetenzfortschritt |
| Anforderungen | NFR-22/23/24; SEC-11/19 |
| Funktionen | Übungen, Quiz, Rückmeldung, adaptive Planung und Lernnachweise |
| Kritikalität | Hoch |
| Anwendbarkeit | V1 vor pädagogischer Bewertung/Anpassung |
| Prüfmethode | Referenzaufgaben mit Teilfehlern/Mehrdeutigkeit; menschliche Rubrik; Korrektur, Undo und jüngere Belege prüfen |
| Erwartetes Ergebnis | Aufgabe/Lösung/Ziel konsistent; nur tatsächlich belegte Kompetenz; Schätzung gekennzeichnet; bestätigte fachliche Güte erfüllt |
| Erforderlicher Beleg | Versionierte Aufgaben-/Lösungsrubrik, Fachbewertungen, Evidenzspur und 28 AT-L-Zuordnung |
| Verpflichtend ab / erneut | Vor Bewertungs-/Adaptionsfunktion; Modell-/Prompt-/Bewertungslogikänderung |
| Tatsächlicher Stand | Nicht implementiert; nicht produktgetestet; ausschließlich dokumentarisch spezifiziert. |

## 4. Rückverfolgbarkeit und sichere Veröffentlichung

Jeder neue NFR-/SEC-Aspekt ist über sein Prüfprofil an mindestens eine Kontrolle angeschlossen. Mehrfachbezüge bezeichnen unterschiedliche Nachweisanteile, keine mehrfachen Kontrollnummern. Quellenqualität (REL-A05), pädagogische Bewertung (REL-A18) und sichere Modell-/Agentenwirkung (REL-A01/S06) sind getrennte Nachweise: eine korrekte Antwort beweist keine Autorisierung und eine sichere Toolausführung keine fachliche Güte.

REL-A16 führt WCAG 2.2 AA ausdrücklich als **zu bestätigendes Ziel**. Bestehende Zugänglichkeitsanforderungen gelten bereits; es wird keine zusätzliche formal genehmigte Standardbindung behauptet. REL-A20 erhält kein neues Profil, seine Incident-/Rollbackfälle sind vor Produktion unter REL-Q17/18/20 nachzuweisen. REL-Q10 bleibt spätere Option ohne V1-Zahlungsumfang. FE-56 schließt gemäß Mission 19 jede Postfachlektüre, -synchronisation und -überwachung in V1 aus; eine spätere Integration bleibt unverbindlich. Dokumentstatus und erfolgte Dokumentprüfungen sind in [E3](../spec/E3-pruefnachweis.md) getrennt von der ausstehenden Produktabnahme nachgewiesen.

## 5. Betriebszuordnung aus S3

[S3.8](../spec/S3-inbetriebnahme.md#s38-einbindung-aller-46-release-kontrollen) referenziert alle 46 bestehenden Profile mit Pflichtzeitpunkt, Ergebnisprüfung, Sperrwirkung und Neubewertung. Erwartetes Ergebnis, Anwendbarkeit und Beleg bleiben hier maßgeblich, ohne neue REL-Kennungen. S3 beschreibt zukünftige Verfahren; alle Kontrollen bleiben nicht implementiert/nicht produktgetestet. S3.7/13 verlangen zusätzlich die konkrete menschliche Veröffentlichungsgenehmigung; die hier dokumentierten Prüfziele sind keine Genehmigung.
