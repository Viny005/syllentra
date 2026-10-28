# Syllentra AI — Spezifikation

Dieses Verzeichnis enthält die Spezifikationsdokumente nach der Methode von Johannes Siedersleben. Die Spezifikation wird schrittweise in deutscher Sprache erarbeitet und mit dem Projektverantwortlichen validiert.

## Kurze Einführung zur Methode Siedersleben

Die Siedersleben‑Methode gliedert eine System‑Spezifikation in klar abgegrenzte Blöcke (P, F, D, B, S, N, E), die jeweils unterschiedliche Aspekte eines Systems dokumentieren: Ziele & Rahmenbedingungen, funktionale Beschreibungen, Daten und Schnittstellen, Betriebs‑ und Sicherheitsaspekte, nichtfunktionale Anforderungen sowie ergänzende Hilfsmittel wie Glossar und Leseanleitung. Ziel ist eine gut strukturierte, überprüfbare und iterativ zu füllende Spezifikation.

## Leseanleitung (E1)

1. Beginnen Sie mit P1 (Ziele und Rahmenbedingungen), um Kontext und Zweck des Systems zu verstehen.
2. Lesen Sie P2 (Architekturüberblick) für eine konzeptionelle Einordnung; beachten Sie, dass Architekturentscheidungen separat dokumentiert bleiben (siehe docs/ARCHITECTURE_DECISIONS.md).
3. Für funktionale Details folgen F1..F3: Geschäftsprozesse → Anwendungsfälle → Anwendungsfunktionen.
4. Datenbezogene Informationen finden sich in D1..D2 (Datenmodell, Datentypenverzeichnis).
5. Betriebs‑ und Interaktionsaspekte sind in B1..B3 dokumentiert; Systemintegrations‑ und Migrationsaspekte in S1..S3.
6. Nichtfunktionale Anforderungen und Querschnittskonzepte sind in N1..N2 gesammelt.
7. Das Glossar (E2) erklärt Begriffe und Abkürzungen.
8. Jedes Dokument enthält Hinweise auf Quell‑/Referenz‑Dokumente im Repo (z. B. docs/PROJECT_VISION.md).

Hinweis: Diese Leseanleitung ist im README.md des Spezifikationsverzeichnisses integriert (E1).

## Index der Spezifikationsblöcke

**Stand: 26.10.2026. Alle ausgearbeiteten Dokumente: Zur Prüfung durch den Projektinhaber.** S1.18.1 enthält sämtliche 89 FE-Einträge; FE-56 ist für V1 als Ausschluss von Postfachlektüre, -synchronisation und -überwachung bestätigt; eine spätere Integration bleibt unverbindlich. Keine Dokumenterstellung oder Git-Aktion bedeutet fachliche Abnahme oder implementierte Funktion.

| Baustein | Version | Inhalt / Stand |
|---|---|---|
| [P1](P1-ziele-rahmenbedingungen.md) | 0.14 | Ziele, Rahmen, Mehrbenutzer-V1, bestätigte Architekturprinzipien (ADR-0012/ADR-0013) und überprüfbare Erfolgskriterien. Zur Prüfung. |
| [P2](P2-architekturueberblick.md) | 0.13 | Kontext, interne/externe Grenzen, zwölf Nachbarn, Informationsklassen und Verankerung der Architekturprinzipien. Zur Prüfung. |
| [F1](F1-geschaeftsprozesse.md) | 0.8 | GP-01 bis GP-15 mit ergänzten Konten-, Import-, Integrations- und Datenkontrollabläufen. Zur Prüfung. |
| [F2](F2-anwendungsfaelle.md) | 0.8 | UC-01 bis UC-66 mit Vorbedingungen, Szenarien, Schutz und Abnahme. Zur Prüfung. |
| [F3](F3-anwendungsfunktionen.md) | 0.8 | AF-01 bis AF-37 als fachliche Prüf- und Auswahlfunktionen. Zur Prüfung. |
| [D1](D1-datenmodell.md) | 0.8 | DM-01 bis DM-78 und INV-01 bis INV-31; Eigentum, Beziehungen und Lebenszyklen. Zur Prüfung. |
| [D2](D2-datentypen.md) | 0.8 | DT-01 bis DT-95, Werte, Strukturfelder und Validierung. Zur Prüfung. |
| [B1](B1-dialogspezifikation.md) | 0.9 | DLG-01 bis DLG-67; persönliche und getrennte administrative Bedienung sowie AT-AUDIO-01..10. Zur Prüfung. |
| [B2](B2-batch.md) | 0.7 | BAT-01 bis BAT-26; autorisierte Hintergrundverarbeitung, Wiederanlauf und Löschfolgen. Zur Prüfung. |
| [B3](B3-druckausgaben.md) | 0.7 | OUT-01 bis OUT-08; kontoisolierte Berichte und geschützte Exporte. Zur Prüfung. |
| [S1](S1-nachbarsysteme.md) | 0.9 | NB-01 bis NB-12, vollständige FE-01..FE-89-Matrix und Schnittstellen-Abnahmeszenarien. Zur Prüfung. |
| [S2](S2-datenmigration.md) | 0.6 | MIG-01 bis MIG-36, AT-S2-01 bis AT-S2-40; eigene Pakete, sichere Migration und Wiederherstellung. Zur Prüfung. |
| [S3](S3-inbetriebnahme.md) | 0.4 | Vollständiger fachlicher Betriebsentwurf: Umgebungen, Bootstrap, unabhängiger Restore, 18 Veröffentlichungsschritte, Rollout, Rückweg, Betrieb und 46 Kontrollverweise. Zur Prüfung. |
| [N1](N1-nichtfunktional.md) | 0.12 | Vollständiger fachlicher V1-Qualitätsentwurf: 25 Prüfprofile, Messverfahren und offene Zielwerte. Zur Prüfung. |
| [N2](N2-querschnittskonzepte.md) | 0.12 | Fachlicher V1-Sicherheitsentwurf: 27 Prüfprofile, Vertrauensgrenzen, bestätigte R1/R4-Eckpunkte, Audioschutzgrenzen (N2.16) und offene technische Verfahren. Zur Prüfung. |
| [E2](E2-glossar.md) | 0.5 | Glossar mit fachlichen Begriffsgrenzen. Zur Prüfung. |
| [E3](E3-pruefnachweis.md) | 0.22 | Änderungs-/Kennungsnachweis sowie tatsächliche Dokument- und lokale Prototypprüfungen. Zur Prüfung. |

E1 ist als Leseanleitung direkt in diesem README integriert; zusammen mit den **17 eigenständigen Bausteindateien (`P1` bis `E3`)** in der obigen Indextabelle umfasst die Spezifikation damit alle **18 Siedersleben-Elemente** und bleibt mit dem Index zur Prüfung. [S2 — Datenmigration](S2-datenmigration.md) ist zur Prüfung ausgearbeitet. [S3 — Inbetriebnahme](S3-inbetriebnahme.md) ist als fachlicher Prüfentwurf ausgearbeitet; zukünftiger Betriebsstart und Bootstrap des einzigen Super Admin sind beschrieben, nicht ausgeführt. Die [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md) ordnet jetzt alle 25 DEC-V1 den bestehenden Fach-/Dialog-/Datenbausteinen und überprüfbaren Soll-Abnahmen zu. Offene Präzisierungen und technische Nachweise bleiben ausdrücklich ausgewiesen; die Matrix ist keine Gesamtabnahme. Die technische Architektur wird separat erarbeitet.

## Zusätzliche verbindliche Prüfgrundlage für spätere Releases

Die [Release-Readiness-Checkliste mit 40 Einzelprüfungen](../quality/RELEASE_READINESS_40.md) vom 22.10.2026 enthält die vollständig erhaltenen zwei Nutzerlisten (REL-S01..REL-S20 und REL-Q01..REL-Q20). Sie ist **kein neuer Siedersleben-Baustein**, sondern ein bereichsübergreifendes Freigaberegister: [N1](N1-nichtfunktional.md) verantwortet Qualität/Leistung, [N2](N2-querschnittskonzepte.md) Sicherheit/Datenschutz, [S2](S2-datenmigration.md) Backup/Restore und [S3](S3-inbetriebnahme.md) den zukünftigen Produktivstart. Produktprüfungen sind noch nicht durchgeführt; kein Eintrag ist deshalb technisch bestanden. REL-Q10 (Doppelzahlungen) ist ausschließlich spätere Option und kein V1-Zahlungsumfang.

## Statuskonventionen

In dieser Spezifikation verwenden wir folgende Statuskennzeichnungen:

- Geplant — Inhalt vorgesehen, noch nicht ausgearbeitet.
- In Bearbeitung — Der Inhalt wird aktuell erarbeitet (z. B. P1).
- Zur Prüfung — Fertig formuliert, steht zur Review durch den Projektverantwortlichen.
- Freigegeben — Validierte und freigegebene Spezifikation.
- Nicht anwendbar — Dieser Block ist für das Projekt nicht relevant; Begründung ist erforderlich.

## Trennung: Spezifikation vs. Architektur vs. Implementierung

- Spezifikation (dieses Verzeichnis): Beschreibt Anforderungen, Ziele, Prozesse, Datenmodelle und Schnittstellen auf einer konzeptionellen und prüfbaren Ebene. Keine technischen Implementierungsdetails, keine Technologieentscheidungen.
- Architektur‑Dokumente (docs/ARCHITECTURE_DECISIONS.md): Dokumentieren getroffene Architekturentscheidungen und Entscheidungsgründe. Architekturentscheidungen werden verlinkt, aber nicht in die Spezifikation hineinkopiert.
- Implementierung (Code‑Repo): Implementierungsdetails, Frameworks, Bibliotheken und Code gehören in den Quellcode und zugehörige Readmes; Verweise von der Spezifikation auf Implementierungsartefakte sind erlaubt, aber die Spezifikation bleibt die autoritative Beschreibung der Anforderungen.

## Verweise auf bestehende Dokumente

Die folgenden historischen/Quell‑Dokumente sind im Repository vorhanden und dienen als Referenzquellen:

- docs/PROJECT_VISION.md
- docs/REQUIREMENTS.md
- docs/ARCHITECTURE_DECISIONS.md
- docs/ROADMAP.md

In jedem neuen Spezifikationsdokument ist eine Sektion "Verweise" aufzunehmen, die relevante Abschnitte dieser Dateien nennt.

## Regeln für die Erstellung und Validierung von Anforderungen

- Anforderungen werden schrittweise in Zusammenarbeit mit dem Projektverantwortlichen ausgearbeitet.
- Keine Anforderung wird als verbindlich dokumentiert, bevor sie nicht explizit vom Projektverantwortlichen freigegeben wurde.
- Historische Dokumente bleiben erhalten. Spezifikationsdokumente sind die autoritativen, freigegebenen Versionen nach Validierung.

---

Datum der Erstellung dieses Dokuments: 2026-10-12
Verantwortlich: (wird bei Veröffentlichung eingetragen)


## Bestätigte Entwicklungszuordnungen und aktueller Entscheidungsumfang

[Entwicklungszuordnungen — Teilstand](ENTWICKLUNGSPLAN.md), Version 0.2, Zur Prüfung: UC-09 → M5, grundlegender UC-39 → M2b, UC-65 intern → M5 und externe Erweiterungen → M8. Kein zuvor im Repository fehlender Gesamtplan wird als bereits freigegeben ausgegeben. L-08/L-04/L-09/L-02 sind nun integriert; die 25 DEC-V1 sind jetzt in der [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md) konsolidiert; deren offene Präzisierungen und der vollständige Meilensteinplan bleiben separat. UC-65 und UC-66 sind die einzigen neuen UC, FE-01 bis FE-89 und FE-56 als bestätigter V1-Ausschluss mit unverbindlicher Zukunftsoption bleiben erhalten. Der [Prüfnachweis](E3-pruefnachweis.md) dokumentiert Quelle, Versionen und tatsächlich ausgeführte Dokumentprüfungen.

## Konsolidierte Entscheidungen und Bewertungsrahmen

[Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md), Version 0.5, **Zur Prüfung**: 25 DEC-V1 mit FE/UC/AF/DM/DT/DLG/BAT/NFR/SEC und Soll-Abnahmen, vollständiger FE-21-Ausgabeanschluss sowie getrennte DEC-48/49. Kein neuer Siedersleben-Baustein und keine neue FE/UC. [ADR-0004/0005](../ARCHITECTURE_DECISIONS.md) halten Oracle als ersten Bewertungskandidaten und die unabhängige verschlüsselte EU-Sicherung fest; endgültige Anbieter/Verfahren, Kapazität/Kosten, RPO/RTO und Fristen offen. Kein Account, externer Infrastrukturtest oder Ausgabe autorisiert. S3 liegt als fachlicher Prüfentwurf vor; N1/N2 sind fachlich vervollständigte Prüfentwürfe mit offenen technischen Nachweisen. Die ursprünglichen 40 Kontrollen im [Originalregister](../quality/RELEASE_READINESS_40.md) bleiben vollständig erhalten.

## Qualitäts- und Freigabeergänzung aus Mission 3

| Dokument | Version / Stand | Zuständigkeit |
|---|---|---|
| [Konsolidierte Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md) | 0.3 · Zur Prüfung | Alle 20 Kandidaten bewertet; sechs neue eigenständige Kontrollen, 46 insgesamt; Prüfprofile und tatsächlicher Status je Kontrolle. |
| [Referenzrahmen](../quality/REFERENZRAHMEN.md) | 0.1 · Zur Prüfung | Belegte ASVS-/OWASP-Ausgaben, eingeschränkte Normabrufe, projektbezogene Zuordnung ohne Konformitätsbehauptung. |
| [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md) | 0.3 · Zur Prüfung | Grundlage von S3: Erstfreigabe, Funktionsgates, Regression, Periodik, Blocker und menschliche Entscheidungen. Kein S3-Verfahren. |

NFR-01..12 und SEC-01..16 bleiben erhalten, ergänzt um NFR-13..25 und SEC-17..27. Messziele und technische Verfahren sind nicht frei erfunden. Alle Kontrollen sind noch ohne Implementierung und Produktnachweis; die vollständige fachliche Formulierung ist keine Abnahme. FE-56: V1-Postfachzugriff ausgeschlossen, Zukunft unverbindlich, keine neue Zahlungs-, Anbieter-, Architektur- oder Betriebsfreigabe.

## S3-Ergänzung aus Mission 4

[S3](S3-inbetriebnahme.md), Version 0.2, **Zur Prüfung durch den Projektinhaber**: 16 Hauptabschnitte, alle 46 bestehenden Releasekontrollen über stabile Profilanker, 14 offene technische/organisatorische Arbeiten O-S3-01..14 und 20 zukünftige Ablaufabnahmen AT-S3-01..20. Keine neue FE, UC, REL-Kontrolle, Anbieterwahl oder Betriebsfreigabe. Konkrete Architektur, Bootstrap-/Recoveryverfahren, Schwellen, tatsächliche Produkt-/Betriebstests und menschliche Genehmigungen bleiben erforderlich. Historische Liefernachweise in E3 ändern ihren damaligen Umfang nicht.

## Technische Vergleichsstudie aus Mission 5

Die [Architekturstudie](../architecture/README.md) mit acht verlinkten Teilstudien vergleicht Architekturform, Hosting, Stack/Identität, Daten/Suche, KI, unabhängige Sicherung und Kosten. Status **Empfohlen / Zur Entscheidung**; kein zusätzlicher Siedersleben-Baustein und keine technische Auswahl. [Quellen/Abrufgrenzen](../architecture/QUELLEN.md) unterscheiden gelesene offizielle Quellen, eigene Rechnungen und nicht verifizierte Angebote/Leistungsannahmen. [Offene technische Entscheidungen](../architecture/OFFENE_ENTSCHEIDUNGEN.md) benötigen Eigentümerfreigabe. Alle Fachanforderungen, 46 Kontrollen und der S3-Prüfentwurf bleiben erhalten; keine Implementierung, Cloudressource, Ausgabe oder Veröffentlichung.

## Machbarkeitsprüfung und Testplanung aus Mission 6

Die [Machbarkeitsprüfung](../architecture/MACHBARKEITSPRUEFUNG.md), [Ressourcenrechnung](../architecture/RESSOURCENBEDARF.md), [geplanten Protokolle T01–T09](../architecture/BENCHMARKPLAN.md) und [TECH-O-Entscheidungsvorlage](../architecture/ENTSCHEIDUNGSVORLAGE.md) ergänzen die Architekturstudie. Keine neuen Fachanforderungen, 46 REL unverändert, alle technischen Tests nicht durchgeführt. Status Empfohlen / Zur Entscheidung; Spezifikationen weiter Zur Prüfung, FE-56: V1-Postfachzugriff ausgeschlossen, Zukunft unverbindlich, kein Provider-/Stack-/Kosten-/Implementierungsbeschluss.


## Design- und Entwicklungsvorbereitung aus Mission 7

[Design System](../design/DESIGN_SYSTEM.md), [UI-/UXplan](../design/UX_AND_FRONTEND_PLAN.md), [Entwicklungs-/Integrationsfolge](../development/INTEGRATION_ROADMAP.md), [Codex-/Claude-Arbeitsrahmen](../ai-tooling/CODEX_CLAUDE_WORKFLOW.md) und [API-/Lizenzquellen](../development/SOURCES.md) ergänzen die Studie im Status Empfohlen / Zur Entscheidung. [ADR-0006](../ARCHITECTURE_DECISIONS.md#adr-0006--persönlicher-qualitätsfokus-und-vergleichsrahmen-aus-mission-7) hält den bestätigten persönlichen Qualitätsfokus und neuen künftigen Vergleichsrahmen bis 20 EUR brutto/Monat fest, keine Ausgabe. Keine neue FE/UC, Zahlungs-/Provider-/Stackentscheidung, Implementierung oder Produktprüfung. Fachentwürfe weiterhin Zur Prüfung; 14 TECH-O offen.


## Lokale Frontendprobe aus Mission 8

[Experimenteller Prototyp](../../prototypes/frontend/README.md), [UI-Prüfbericht](../design/PROTOTYPE_REVIEW.md) und [ADR-0007](../ARCHITECTURE_DECISIONS.md#adr-0007--lokale-frontendprobe-aus-mission-8) beschreiben erste tatsächlich ausführbare Oberflächen mit synthetischen Daten. Keine fachliche V1-/Backend-/KI-/Auth-/Isolationsabnahme, keine endgültige Stackwahl. Spezifikationen Zur Prüfung, FE-56 ist für V1 als Postfachausschluss bestätigt; alle 14 TECH-O bleiben offen. E3 hält eng begrenzte reale UIprüfungen getrennt von historischen Dokumentchecks und noch offenen Produkttests fest.


## Lokale Backendprobe aus Mission 9

[Experimentelle Backendanleitung](../../prototypes/backend/README.md), [Prüfbericht](../development/BACKEND_PROTOTYPE_REVIEW.md) und [ADR-0008](../ARCHITECTURE_DECISIONS.md#adr-0008--lokale-backendprobe-aus-mission-9) ergänzen reale synthetische PostgreSQL-/APItests zu Sitzungen, Isolation und Serverflags. Normale Anmeldung, reale OTP-/Geräte-/Recovery-/MFAwege und Administration bleiben gesperrt; Frontend weiterhin Demo. Keine fachliche Abnahme, Stackendentscheidung oder Betriebsfreigabe. E3 Version 0.13 trennt neue begrenzte Implementierungsbelege von historischen Dokumentprüfungen und weiterhin ausstehenden Produktkontrollen.


## Lokale Identitätsprobe aus Mission 10, Testisolation aus Mission 12 sowie Korrekturen aus Mission 13 und 14

[Architektur](../development/IDENTITY_ARCHITECTURE.md), [Validierung](../development/IDENTITY_PROTOTYPE_REVIEW.md), [Offene Entscheidungen](../development/OPEN_DECISIONS.md) und [ADR-0009](../ARCHITECTURE_DECISIONS.md#adr-0009--lokale-identitätsprobe-aus-mission-10): lokale synthetische Registrierung/OTP/Geräte/Sessions/Zweikanal-Recovery mit eigenem Reactbereich; in Mission 12 ergänzt um Pro-Lauf-PostgreSQL-Testdatenbanken (`syllentra_t_<12 Hex>`); in Mission 13 ergänzt um gezielte Korrekturen für R2 (Netzwerkbudget-Isolierung), R3 (Sortierung, effektiver Status und `offset`/`limit`-Paginierung für Sessions/Geräte), R5 (Aufrufer-isolierte Adressbudgets und Schutz laufender Recovery-Challenges) und R12 (verschärfte Sitzungs-/Geräteprüfung bei `approve_device`); in Mission 14 ergänzt um die vom Projektinhaber freigegebenen Entscheidungen R1 (persönlicher Einmal-Recoverycode ohne automatischen 7-Tage-Ablauf) und R4 (kontrollierter Reset unverifizierter `pending`-Konten ab 24 Stunden) sowie 99 bestandene Backendtests. Keine reale Zustellung, Admin-MFA/Bootstrap oder Produktfreigabe. Standardbackend geschlossen; bestehende acht Lernräume Demo. E3 Version 0.19 bewahrt die damaligen begrenzten Belege. FE-56 ist für V1 als Postfachausschluss bestätigt; alle 14 TECH-O bleiben offen, alle fachlichen Bestände erhalten und Spezifikation Zur Prüfung.


## Audioentscheidungen aus Mission 15 und Konsolidierung aus Mission 17

[P1.10.6](P1-ziele-rahmenbedingungen.md#p1106-bestätigte-audioentscheidungen-aus-mission-15) dokumentiert die bestätigten Arbeitsreferenzen AUDIO-01 bis AUDIO-03: Benachrichtigungstöne, Stimmen je Audiosprache und freiwilliger Hörmodus. Die vorhandenen UC-20/48/65, AF-/Daten-/Dialog-/Nachbar- und Qualitäts-/Schutzbausteine sind gezielt ergänzt; keine neuen FE/UC/DEC-V1 oder Implementierung. [B1.13](B1-dialogspezifikation.md#b113-abnahmeszenarien-für-töne-und-stimmen) enthält zehn zukünftige AT-AUDIO-Sollfälle, [S1.23](S1-nachbarsysteme.md#s123-audioverträge-fähigkeitsgrenzen-und-offene-alternativen) Alternativen, fixierte Quellen und offene Belege. In Mission 17 additiv mit den Identitätsentscheidungen aus Mission 14 (R1/R4 in [N2](N2-querschnittskonzepte.md) Version 0.9 und [E3](E3-pruefnachweis.md) Version 0.18) zusammengeführt. Weiterhin **Zur Prüfung**; FE-56: V1-Postfachzugriff ausgeschlossen, Zukunft unverbindlich, keine Motor-/Stimmen-/Anbieterwahl oder Ausgabe freigegeben.

## Harmonisierung aus Mission 19

R1 ist in DM-54/DT-67/DT-85 und UC-51/52 sowie DLG-51/52 durchgängig von befristeten OTP/Recoveryvorgängen getrennt. R4 gilt ab exakt `>= 24 h`; kein Reset verifizierter Konten oder Aufweichen von Schutzbedingungen. FE-56 ist vom Projektinhaber als Ausschluss jeder Postfachlektüre, -synchronisation und -überwachung in V1 bestätigt; ausgehender autorisierter Versand und manueller Import ausgewählter Inhalte bleiben möglich. Eine spätere Integration ist unverbindlich, keine Implementierungszusage.

F1-/F3-Zusammenfassungen, P2-Versionverweis und bereits behandelte B2-/B3-Fragen sind aktualisiert. Browser-E2E der Mission 14 ist mangels konkretem Beleg als nicht ausgeführt/nicht nachgewiesen gekennzeichnet; frühere Testergebnisse bleiben historische Belege. [E3.32](E3-pruefnachweis.md#e332-mission-19--harmonisierung-nach-audit-und-bestätigter-v1-postfachausschluss) trennt tatsächliche Dokumentprüfung von nicht ausgeführten Produkttests. Keine neue FE/UC/DEC, Architekturentscheidung oder Anwendungsänderung. Alle Fassungen bleiben **Zur Prüfung durch den Projektinhaber**, alle 14 TECH-O offen (historischer Stand Mission 19; anschließende Architekturprinzipien siehe Mission 21).


## Architekturentscheidungen aus Mission 21 (TECH-O-01 bis TECH-O-14)

In Mission 21 sind die vom Projektinhaber bestätigten **14 Architekturprinzipien (`TECH-O-01` bis `TECH-O-14`) sowie die übergreifende Multi-Provider-Architekturregel** in [ADR-0010 bis ADR-0024](../ARCHITECTURE_DECISIONS.md#adr-0010--evolutionärer-modularer-monolith-und-isolierte-worker-tech-o-01), dem aktualisierten Register [Offene technische Entscheidungen](../architecture/OFFENE_ENTSCHEIDUNGEN.md) (Version 0.4), der [Entscheidungsvorlage](../architecture/ENTSCHEIDUNGSVORLAGE.md) (Version 0.3), den sechs Fachkapiteln der [Architekturstudie](../architecture/README.md) (Version 0.5) und [OPEN_DECISIONS.md](../development/OPEN_DECISIONS.md) (Version 0.5) konsolidiert. Jede Entscheidung trennt strikt zwischen **A. bestätigtem Architekturprinzip**, **B. offenen technischen Unterentscheidungen** (konkrete Anbieter, Modelle, Stimmen, Schlüssel-/Restore-/DNS-/Warteschlangen-Konfigurationen) und **C. ausstehenden Nachweisen / zukünftigen Prüfungen** (`T01`–`T09`, Lizenz-/Vertrags-/DSGVO-Prüfungen, RPO/RTO/SLO vor Produktion). [E3.33](E3-pruefnachweis.md#e333-mission-21--konsolidierung-der-14-bestätigten-tech-o-architekturprinzipien-und-der-multi-provider-querschnittsregel) dokumentiert den Prüfnachweis. Alle **89 FE** (`FE-56` als bestätigter V1-Postfachausschluss), **66 UC**, **25 DEC-V1**, `DEC-48`/`DEC-49`, **46 REL**, `R1`/`R4`, `AUDIO-01..03` und `AT-AUDIO-01..10` bleiben unverändert erhalten; alle Siedersleben-Spezifikationsbausteine bleiben **Zur Prüfung durch den Projektinhaber**.

## Bestätigter Darstellungsrahmen aus Mission 23

[P2.5.6](P2-architekturueberblick.md#p256-verbindlicher-darstellungs--und-konfigurationsrahmen-aus-mission-23) präzisiert vorhandene CFG-01..17, FE-57/58 und persönliche Darstellungsfreiheit innerhalb zentraler Richtlinien. [B1.14](B1-dialogspezifikation.md#b114-darstellung-konfiguration-und-quellennavigation-mission-23) enthält 16 nicht ausgeführte AT-VIS-Sollfälle für Themes, Saisonen, Texte, Rechte und Originalquellen. [E3.34](E3-pruefnachweis.md#e334-mission-23--konfigurierbare-darstellung-und-anklickbare-quellen) dokumentiert Wiederverwendung, Lücken und tatsächliche Dokumentprüfungen. Keine neue FE/UC/REL, keine technische Implementierung; konkrete Marke und Saisonregel bleiben Zur Entscheidung.

**Präzisierung Mission 23B:** [B1.14.3](B1-dialogspezifikation.md#b1143-teststatus-voraussetzungen-und-offene-entscheidungen-mission-23b) trennt Nichtausführung, Voraussetzungen und offene Entscheidungen für dieselben 16 AT-VIS. N1.12/N2.17 und die REL-Matrix enthalten Rückzuordnungen; [E3.34.4](E3-pruefnachweis.md#e3344-mission-23b-quellenstatus-und-sechs-gezielte-korrekturen) erläutert Belegstatus, Markdown-Zählbasis und aktuelle Dokumentkontrollen. [TECH-O-Register](../architecture/OFFENE_ENTSCHEIDUNGEN.md) jetzt Version 0.5: zusätzliche offene B/C-Arbeiten in TECH-O-03/06 und ADR-0012/0015, keine neue Architekturwahl.
