# D2 — Datentypen und Wertebereiche

**Projekt:** Syllentra AI\
**Dokument:** D2 — Datentypen\
**Version:** 0.7\
**Stand:** 23.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber\
**Bezugsstand:** Vier bestätigte Entscheidungen vom 19.10.2026; Ausgangs-HEAD `53ef171be4783748b5c7e3a84bb0cc363d5b4194`, Branch `docs/spec/p1-p2-mobile-workspaces`, PR #1; aktuelle Fassungen im [Index](README.md).\
**Methode:** Spezifikationsbaustein nach Johannes Siedersleben, fachlich vergleichbar mit der [Herold-D2-Referenz](https://github.com/carstenlucke/herold/blob/main/docs/spec/D2-datentypen.md).

> **Freigabegrenze:** FE-01 bis FE-17 sind bestätigte Entscheidungen. Die Ergänzung über eine abgeschirmte, nach Hochschule aufklappbare Notenansicht ist vom Nutzer ausdrücklich vorgegeben. FE-43 bestätigt den öffentlichen V1-Umfang (Auswahl oder alle eigenen öffentlichen Repositories) und freiwillige offizielle Kontoverbindung; dies ist keine Behauptung einer fertig implementierten oder technisch verfügbaren Integration. D1 und F2 werden durch D2 nicht stillschweigend umnummeriert oder umgeschrieben.

## D2.1 Auftrag und Abgrenzung

D2 definiert fachliche Wertemengen, Abwesenheit, Vergleichbarkeit, Wertebereiche, Datensicherheit und Validierungsregeln für die fachlichen Entitätstypen `DM-01` bis `DM-78` aus [D1](D1-datenmodell.md). Es entscheidet weder über Datenbank, SQL-Spaltentyp, ORM, API-Schema, Verschlüsselungsprodukt noch technisches Authentifizierungsverfahren. Fachliche Bezeichnungen wie `DT-01` sind **neue D2-Typkennungen**, keine bestehenden D1-Entitäten oder DB-Tabellen. Bestehende Kennungen `UC-01..UC-50`, `GP-01..GP-15`, `AF-01..AF-27`, `INV-01..INV-25`, `FE-01..FE-17`, `DK-01..DK-12` und `CFG-01..CFG-17` behalten ihre Bedeutung.

### D2.1.1 Allgemeine Typ- und Validierungsregeln

1. `Pflicht`, `optional`, `unbekannt`, `nicht verfügbar`, `nicht zutreffend` und **absichtlich nicht gespeichert** sind unterscheidbar. Unbekannte Zahlen sind weder Null noch fehlerhaftes NaN; ein fehlender Beleg ist kein Gegenbeweis.
2. Gleichheit von Kennungen vergleicht die stabile fachliche Identität. Namen und URLs dürfen nicht als alleiniger Identitätsbeweis gelten.
3. Zeitliche Vergleiche erfolgen auf eindeutig bestimmten Zeitpunkten; lokale Planung berücksichtigt Zeitzonen, Sommerzeit und getrennte Datumspräzision.
4. Eingabe- und Ausgabewerte werden fachlich validiert. Externe Dokumente und Repository-Inhalte sind **unvertrauenswürdige Daten**, keine Befehle zur Rechteerweiterung.
5. Ein Datentyp kann mehreren DM-Entitäten dienen; nicht jeder dort genannte Typ ist automatisch ein zwingendes Feld der Entität. Pflichtfelder und Kardinalitäten richten sich zusätzlich nach D1 und dem jeweiligen Fachstatus.
6. Sichtbarkeit im UI wird in B1 ausgestaltet. D2 macht für personenbezogene und insbesondere Notendaten die erforderliche Sichtbarkeits- und Quelleninformation typisierbar.
7. Jede Ausführung benötigt die konkret wirksame Freigabe. Freigabestatus, Entscheidung und **tatsächlicher Ausführungsstand** sind getrennte Werte.
8. Zugangskanäle und Anbieterlimits sind zeitabhängig. „Kostenlos“ ist nur eine nachweisbare aktuelle Eigenschaft eines erlaubten Weges, keine pauschale Eigenschaft der Marke ChatGPT/Claude.
9. Gleichheit prüft Werte desselben Typs und Geltungsbereichs; unbekannte Werte beweisen weder Gleichheit noch Ungleichheit der unbekannten Sachverhalte. Enumerationen sind ungeordnet; ihre Reihenfolge im Katalog ist weder Rang noch erlaubte Zustandsfolge. Strukturen werden anhand ihrer benannten fachlichen Bestandteile verglichen. Mengen sind duplikatfrei und ungeordnet, Folgen ausdrücklich geordnet. Konkrete technische Kodierung und Serialisierung werden nicht festgelegt.
10. Ein fehlender optionaler Wert ist zulässig, ein unbekannter benötigter Wert wird ausdrücklich gekennzeichnet. Pflichtangaben gelten statusbezogen nach D1. Unbekannte Berechtigung, ungeklärte Verarbeitungseignung, unklarer Kostenrahmen oder fehlender für diesen Zugang erforderlicher Kontingentnachweis erlauben keine davon abhängige Ausführung. Ein nachweislich nicht zutreffendes Limit ist von einem unbekannten erforderlichen Limit zu unterscheiden. Ein bestehender anderer zulässiger manueller Weg bleibt möglich, ohne Rechte oder Zusatzkosten zu erfinden.
11. Die Typen, Enumerationswerte und nachfolgend präzisierten Vergleichs-/Validierungsregeln sind D2-Vorschläge zur Prüfung, soweit sie über bestehende Anforderungen und die ausdrücklich bestätigten FE-15 bis FE-17 hinausgehen. Eine Typdefinition erzeugt keine neue Entität, Beziehung oder Softwarefunktion.
12. Die vollständigen Gesprächsinhalte unterliegen DK-08 und werden nicht in KI-Verbrauchsstatistiken (zulässige Konfigurations-/Übermittlungsmetadaten zu DK-05/DK-06) verdoppelt.

## D2.2 Typenkatalog

| Kennung | Typ | Kategorie | D1-Bezug |
|---|---|---|---|
| DT-01 | `KennungDT` | Skalar | DM-01..DM-78 |
| DT-02 | `ZeitpunktDT` | Skalar | DM-01, DM-03, DM-21, DM-26, DM-35, DM-40, DM-41, DM-47 |
| DT-03 | `KalenderdatumDT` | Skalar | DM-05, DM-11, DM-12, DM-35 |
| DT-04 | `ZeitzoneDT` | Skalar | DM-05, DM-11, DM-35, DM-47 |
| DT-05 | `ZeitraumDT` | Struktur | DM-04, DM-05, DM-35, DM-46, DM-47 |
| DT-06 | `MehrsprachigerTextDT` | Struktur | DM-02, DM-06, DM-09, DM-13, DM-48 |
| DT-07 | `SpracheDT` | Skalar | DM-02, DM-25, DM-26, DM-48 |
| DT-08 | `MedienartDT` | Enumeration | DM-20, DM-21, DM-26, DM-29 |
| DT-09 | `DateireferenzDT` | Struktur | DM-20, DM-21, DM-24, DM-26 |
| DT-10 | `QuellenartDT` | Enumeration | DM-19, DM-23, DM-38, DM-51 |
| DT-11 | `QuellenLocatorDT` | Struktur | DM-19, DM-21, DM-23 |
| DT-12 | `DatenherkunftDT` | Enumeration | DM-04, DM-12, DM-14, DM-20, DM-21, DM-33, DM-37 |
| DT-13 | `NachweisgradDT` | Enumeration | DM-12, DM-14, DM-32, DM-33 |
| DT-14 | `UnsicherheitsangabeDT` | Struktur | DM-15, DM-24, DM-30, DM-32, DM-38, DM-52 |
| DT-15 | `DatenfreigabeDT` | Struktur | DM-03, DM-36, DM-44, DM-46 |
| DT-16 | `BerechtigungsstatusDT` | Enumeration | DM-03, DM-36, DM-44 |
| DT-17 | `KanalartDT` | Enumeration | DM-43, DM-44, DM-45, DM-47 |
| DT-18 | `IntegrationsstatusDT` | Enumeration | DM-43, DM-44, DM-45 |
| DT-19 | `ModellEigenschaftenDT` | Struktur | DM-45, DM-46 |
| DT-20 | `GeldbetragDT` | Struktur | DM-46, DM-47 |
| DT-21 | `MetrikeinheitDT` | Enumeration | DM-46, DM-47 |
| DT-22 | `MessstandDT` | Enumeration | DM-46, DM-47 |
| DT-23 | `KontingentDT` | Struktur | DM-46, DM-47 |
| DT-24 | `AbrechnungsperiodeDT` | Struktur | DM-47 |
| DT-25 | `KIStatistikDT` | Struktur | DM-47 |
| DT-26 | `NotenOriginalDT` | Struktur | DM-04, DM-12 |
| DT-27 | `NotenskalaDT` | Struktur | DM-04, DM-12 |
| DT-28 | `NotenAequivalenzDT` | Struktur | DM-12 |
| DT-29 | `NotenAnsichtDT` | Struktur | DM-02, DM-04, DM-12 |
| DT-30 | `ECTSWertDT` | Skalar | DM-06, DM-12 |
| DT-31 | `StudienstatusDT` | Enumeration | DM-04, DM-05, DM-06, DM-07, DM-08 |
| DT-32 | `PruefungsstatusDT` | Enumeration | DM-11, DM-12 |
| DT-33 | `ProjektstatusDT` | Enumeration | DM-16, DM-18 |
| DT-34 | `KontexttypDT` | Enumeration | DM-09, DM-10, DM-22, DM-27, DM-39 |
| DT-35 | `KontextBezugDT` | Struktur | DM-17, DM-22, DM-27, DM-39 |
| DT-36 | `DokumentFassungDT` | Struktur | DM-20, DM-21 |
| DT-37 | `AbleitungsstatusDT` | Enumeration | DM-21, DM-24 |
| DT-38 | `GespraechsstatusDT` | Enumeration | DM-25, DM-26 |
| DT-39 | `NachrichtenrolleDT` | Enumeration | DM-26 |
| DT-40 | `LernmodusDT` | Enumeration | DM-28, DM-29, DM-30 |
| DT-41 | `AufgabenschwierigkeitDT` | Struktur | DM-29, DM-30, DM-32 |
| DT-42 | `AntwortBewertungDT` | Struktur | DM-30, DM-31, DM-32 |
| DT-43 | `HilfestufeDT` | Enumeration | DM-31 |
| DT-44 | `LernfortschrittDT` | Struktur | DM-28, DM-32 |
| DT-45 | `ErinnerungsstatusDT` | Enumeration | DM-33, DM-34 |
| DT-46 | `ErinnerungsRevisionDT` | Struktur | DM-33, DM-34 |
| DT-47 | `VorschlagsartDT` | Enumeration | DM-39, DM-40 |
| DT-48 | `VorschlagsstatusDT` | Enumeration | DM-39, DM-40, DM-41 |
| DT-49 | `VorschlagsaktionDT` | Enumeration | DM-41 |
| DT-50 | `AusfuehrungsstatusDT` | Enumeration | DM-42 |
| DT-51 | `ImportstatusDT` | Enumeration | DM-37, DM-40 |
| DT-52 | `TerminstatusDT` | Enumeration | DM-11, DM-35 |
| DT-53 | `VerfuegbarkeitsfensterDT` | Struktur | DM-35, DM-36 |
| DT-54 | `SynchronisationsKonfliktDT` | Struktur | DM-03, DM-25, DM-39, DM-41, DM-48 |
| DT-55 | `VersionsstandDT` | Struktur | DM-20, DM-21, DM-39, DM-40, DM-48, DM-49 |
| DT-56 | `KompetenzBelegDT` | Struktur | DM-13, DM-14, DM-19, DM-23 |
| DT-57 | `GitHubProfilReferenzDT` | Struktur | DM-14, DM-19, DM-23 |
| DT-58 | `DatenschutzSichtbarkeitDT` | Enumeration | DM-02, DM-12, DM-14, DM-33, DM-47 |
| DT-59 | `DatenkontrollStatusDT` | Enumeration | DM-50, DM-51 |
| DT-60 | `LoeumfangDT` | Struktur | DM-20, DM-21, DM-22, DM-25, DM-33, DM-34, DM-50 |
| DT-61 | `KonfigurationswertDT` | Struktur | DM-48, DM-49 |
| DT-62 | `ArchivstatusDT` | Enumeration | DM-05, DM-16, DM-20, DM-25 |
| DT-63 | `DatenkategorieDT` | Enumeration | DM-01..DM-78 |
| DT-64 | `PruefergebnisDT` | Struktur | DM-12, DM-14, DM-30, DM-32, DM-37, DM-40 |
| DT-65 | KontostatusDT | Fachlicher Zustands-/Wertebereich | DM-01 |
| DT-66 | EMailAdressrolleDT | Fachlicher Zustands-/Wertebereich | DM-53 |
| DT-67 | VerifikationszweckDT | Fachlicher Zustands-/Wertebereich | DM-54 |
| DT-68 | SitzungsstatusDT | Fachlicher Zustands-/Wertebereich | DM-55 |
| DT-69 | AdministrationsrechtDT | Fachlicher Zustands-/Wertebereich | DM-56 |
| DT-70 | SupportumfangDT | Struktur | DM-58 |
| DT-71 | QuotarahmenDT | Struktur | DM-59 |
| DT-72 | FeatureSichtbarkeitDT | Fachlicher Zustands-/Wertebereich | DM-60 |
| DT-73 | ReleaseStatusDT | Fachlicher Zustands-/Wertebereich | DM-61 |
| DT-74 | IntegrationslaufstatusDT | Fachlicher Zustands-/Wertebereich | DM-62 |
| DT-75 | SyncModusDT | Fachlicher Zustands-/Wertebereich | DM-63 |
| DT-76 | QuellrevisionDT | Struktur | DM-21, DM-23, DM-38 |
| DT-77 | SchutzstufeDT | Fachlicher Zustands-/Wertebereich | DM-64 |
| DT-78 | SchlüsselverfügbarkeitDT | Fachlicher Zustands-/Wertebereich | DM-65 |
| DT-79 | VerarbeitungsumfangDT | Struktur | DM-66 |
| DT-80 | PapierkorbstatusDT | Fachlicher Zustands-/Wertebereich | DM-67, DM-68 |
| DT-81 | SicherungsstatusDT | Fachlicher Zustands-/Wertebereich | DM-69 |
| DT-82 | WiederherstellungsstatusDT | Fachlicher Zustands-/Wertebereich | DM-70 |
| DT-83 | ArchivExtraktionsstatusDT | Fachlicher Zustands-/Wertebereich | DM-71 |
| DT-84 | SprachpräferenzenDT | Struktur | DM-02, DM-09, DM-25, DM-48 |
| DT-85 | GeheimnisNachweisDT | Struktur | DM-54, DM-65 |
| DT-86 | ExportmanifestDT | Struktur | DM-72 |
| DT-87 | MigrationszustandDT | Struktur | DM-73 |
| DT-88 | MigrationsdeltaDT | Struktur | DM-73, DM-74 |
| DT-89 | MigrationswirkungDT | Struktur | DM-74 |
| DT-90 | MigrationswegDT | Struktur | DM-73 |
| DT-91 | LernreihenfolgeDT | Struktur | DM-75 |
| DT-92 | PädagogischePlanänderungDT | Struktur | DM-76 |
| DT-93 | ErinnerungsregelDT | Struktur | DM-77 |
| DT-94 | BenachrichtigungszustellungDT | Struktur | DM-78, DM-52 |
| DT-95 | StudienvorgabenAbgleichDT | Struktur | DM-24, DM-04, DM-06, DM-11, DM-12 |

## D2.3 Fachliche Typdefinitionen

Die nachfolgenden Typen sind als fachliche Kontrakte zu lesen: `Werte/Felder` ist die erlaubte Grundform; `Regeln` beschreibt semantische Invarianten. Ein Zustand muss zusätzlich die für seinen D1-Entitätstyp geltenden Pflicht- und Bezugskriterien erfüllen.

### DT-01 — KennungDT

**Art:** Skalar\
**Betroffene D1-Entitäten:** DM-01..DM-52

**Zweck:** Stabile, nicht interpretierbare Identität eines fachlichen Objekts.

**Werte beziehungsweise Felder:** Nichtleerer opaker Wert; eindeutiger Geltungsbereich je Objektart/Eigentümer.

**Fachliche Regeln:** Nicht aus Namen, E-Mail-Adressen oder GitHub-URLs abgeleitet; nach Löschung nicht für ein anderes Objekt wiederverwenden. Gleichheit erlaubt, keine Sortierreihenfolge aus der Kennung ableiten.

**Abwesenheit, Kardinalität und Vergleich:** Fehlen vor Anlage ist kein zugewiesener Schlüssel. Gleichheit nur innerhalb Objektart und Eigentumsgrenze; keine Ordnung, kein Recht durch bloße Kenntnis der Kennung.

**Prüfbeispiel:** Zwei Projekte mit gleichem Namen besitzen verschiedene Kennungen.

### DT-02 — ZeitpunktDT

**Art:** Skalar\
**Betroffene D1-Entitäten:** DM-01, DM-03, DM-21, DM-26, DM-35, DM-40, DM-41, DM-47

**Zweck:** Eindeutiger Zeitpunkt einschließlich Zeitzoneninformation für Ereignisse und Revisionsstände.

**Werte beziehungsweise Felder:** Valider Zeitpunkt mit Offset beziehungsweise eindeutigem UTC-Bezug.

**Fachliche Regeln:** Speichern und Vergleichen als Zeitpunkte; Anzeige in gewählter Zeitzone. Bloße Datumsangaben nicht als exakten Zeitpunkt erfinden.

**Abwesenheit, Kardinalität und Vergleich:** Bekannte Zeitpunkte sind nach ihrem tatsächlichen Moment vergleichbar, unabhängig von Anzeigeoffset. Ungenaue oder unbekannte Angaben nicht für eine exakte Reihenfolge verwenden.

**Prüfbeispiel:** Prüfung 10:00 Europe/Berlin und zugehöriger UTC-Zeitpunkt repräsentieren dasselbe Ereignis.

### DT-03 — KalenderdatumDT

**Art:** Skalar\
**Betroffene D1-Entitäten:** DM-05, DM-11, DM-12, DM-35

**Zweck:** Datum ohne Uhrzeit für Fristen und Kalendertage.

**Werte beziehungsweise Felder:** Gültiges Kalenderdatum; Präzision Tag.

**Fachliche Regeln:** Unbekannte Uhrzeit bleibt unbekannt; Datumsgrenzen nicht in lokale 00:00-Uhr-Termine umdeuten.

**Abwesenheit, Kardinalität und Vergleich:** Gleichheit und Ordnung nach bekanntem Kalenderdatum; kein Vergleich als genauer Zeitpunkt ohne zusätzliche Zeit-/Zonenangabe.

**Prüfbeispiel:** Nur „16.10.2026“ wird als Datum ohne vermeintliche Vorlesungsstunde erfasst.

### DT-04 — ZeitzoneDT

**Art:** Skalar\
**Betroffene D1-Entitäten:** DM-05, DM-11, DM-35, DM-47

**Zweck:** IANA-Zeitzonenkennzeichen zur lokalen Planung und Periodeninterpretation.

**Werte beziehungsweise Felder:** Unterstützte gültige Zeitzonenkennung; z. B. Europe/Berlin.

**Fachliche Regeln:** Sommerzeitumstellungen beachten. Nicht existente oder doppelte Ortszeiten müssen geklärt und dürfen nicht still normalisiert werden.

**Abwesenheit, Kardinalität und Vergleich:** Vergleich nach fachlich aufgelöster Zeitzonenidentität, keine Rangfolge. Ein fester Offset ersetzt keine Zone mit Sommerzeitregeln; unbekannte Zone blockiert die davon abhängige genaue Planung.

**Prüfbeispiel:** Europe/Berlin.

### DT-05 — ZeitraumDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-04, DM-05, DM-35, DM-46, DM-47

**Zweck:** Zeitliches Intervall mit expliziter Präzision und ggf. Zeitzone.

**Werte beziehungsweise Felder:** `von`, `bis`, `granularitaet`, `zeitzone?`; Höchstens eine offene Grenze, nur wo fachlich erlaubt; eine unbekannte Grenze ist keine absichtlich offene Grenze.

**Fachliche Regeln:** `bis` muss nach `von` liegen; Genaue Zeiträume sind im vorliegenden Typvorschlag halboffen [von, bis); unbekannte Grenzen erlauben keine präzise Überlappungsentscheidung. Datumsintervalle und genaue Zeitpunkte nicht vermischen, Tagesgrenzen mit Zeitzone kenntlich machen.

**Abwesenheit, Kardinalität und Vergleich:** Bekannte Grenzen nach DT-02 beziehungsweise DT-03 vergleichen; Überlappung und Enthaltensein nur bei passender Präzision und geklärten Grenzen. Keine universelle Sortierung unvollständiger Intervalle.

**Prüfbeispiel:** Abrechnungsmonat als [01.10. 00:00, 01.11. 00:00) lokal.

### DT-06 — MehrsprachigerTextDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-02, DM-06, DM-09, DM-13, DM-48

**Zweck:** Text mit Sprachkennzeichen und nachprüfbarem Quellbezug.

**Werte beziehungsweise Felder:** `text`, `sprache?`, `ursprung?`, `istUebersetzung`.

**Fachliche Regeln:** Fehlende Sprache bleibt unbekannt; Übersetzung ersetzt nicht rechtlich maßgeblichen Originalwortlaut. Keine freien HTML-/Skriptausführungen.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein Text je Sprachfassung; 0..n zusätzliche Fassungen. Vergleich mit Sprache und Herkunft, keine Gleichsetzung verschiedener Übersetzungen durch ähnliche Formulierung.

**Prüfbeispiel:** Deutscher Modultitel und französische nutzerseitige Anzeige.

### DT-07 — SpracheDT

**Art:** Skalar\
**Betroffene D1-Entitäten:** DM-02, DM-25, DM-26, DM-48

**Zweck:** Sprachkennung für Oberfläche, Texte, Stimme und Lernpräferenzen.

**Werte beziehungsweise Felder:** Gültige Sprachkennung (z. B. de, fr, en); optionale regionale Varianten.

**Fachliche Regeln:** Sprachauswahl verleiht weder Quellenrechte noch zusätzliche Medienfähigkeiten.

**Abwesenheit, Kardinalität und Vergleich:** Sprachkennungen nach ihrer gültigen kanonischen Bedeutung vergleichen; Groß-/Kleinschreibung darf dieselbe Sprachkennung nicht verdoppeln. Keine Rangfolge und keine Gleichsetzung von Sprache und Sprachkompetenz.

**Prüfbeispiel:** de-DE.

### DT-08 — MedienartDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-20, DM-21, DM-26, DM-29

**Zweck:** Semantische Art einer gespeicherten Ressource.

**Werte beziehungsweise Felder:** dokument; bild; audio; video; text; sonstige

**Fachliche Regeln:** Tatsächliche Dateiformate und Dateigrößen später festlegen; Medienart nicht als vertrauenswürdigen Inhaltsnachweis ansehen.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Ein hochgeladenes PDF ist dokument.

### DT-09 — DateireferenzDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-20, DM-21, DM-24, DM-26

**Zweck:** Geschützter Verweis auf einen Inhalt, nicht eine öffentlich lesbare Dateiadresse.

**Werte beziehungsweise Felder:** `referenz`, `medienart`, `groesse?`, `pruefsumme?`, `berechtigungsstatus`.

**Fachliche Regeln:** Keine dauerhafte ungeschützte URL oder Geheimnisse in Anzeigen; Löschung entfernt bzw. entwertet Referenz entsprechend Umfang.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein geschützter Inhaltsbezug je Wert; optionale Größe/Prüfsumme bleiben bei Nichtverfügbarkeit unbekannt. Gleicher Dateiname oder gleiche Prüfsumme beweisen weder gleiche logische Dokumentidentität noch gleiche Rechte.

**Prüfbeispiel:** Zugriff auf PDF v2 nur durch autorisiertes Gerät.

### DT-10 — QuellenartDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-19, DM-23, DM-38, DM-51

**Zweck:** Klassifikation einer Informationsquelle.

**Werte beziehungsweise Felder:** hochschule; lernplattform; dokument; github_profil; github_repository; website; benutzerangabe; anbieter; sonstige

**Fachliche Regeln:** Quelle garantiert weder Wahrheit noch Nutzungsrecht; GitHub-Profil ist grundsätzlich keine eigene Fähigkeit oder Kompetenz.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** github_repository.

### DT-11 — QuellenLocatorDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-19, DM-21, DM-23

**Zweck:** Identifizierbare öffentliche Adresse oder freigegebene interne Quellenreferenz.

**Werte beziehungsweise Felder:** `art`, `locator`, `zugriff` (öffentlich / eigens freigegeben / unbekannt), `pruefstand`.

**Fachliche Regeln:** Nur erlaubte HTTPS-URLs und explizite interne Referenzen; weder private Token noch Zugangsdaten im Locator; keine erzwungene Öffnung unbekannter Deep Links.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein Locator je Wert; mehrere Quellen als 0..n getrennte Bezüge. Normalisierung darf Ressource oder Zugriffsgrenze nicht ändern; gleiche URL beweist keine persönliche Identität.

**Prüfbeispiel:** https://github.com/benutzer/repository (nur beispielhaft).

### DT-12 — DatenherkunftDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-04, DM-12, DM-14, DM-20, DM-21, DM-33, DM-37

**Zweck:** Unabhängige Kennzeichnung des Ursprungs einer Aussage.

**Werte beziehungsweise Felder:** amtlich_belegt; durch_nutzer_eingegeben; aus_dokument_importiert; extern_beobachtet; durch_ki_abgeleitet; sonstige

**Fachliche Regeln:** Herkunft darf nach Nutzerbestätigung nicht still auf amtlich wechseln; amtlich_belegt benötigt konkreten geeigneten Beleg.

**Abwesenheit, Kardinalität und Vergleich:** Bei fehlender Herkunft ausdrücklich unbekannt; amtlich_belegt nur mit qualifizierter Quelle. Importweg, manuelle Erfassung, KI-Ableitung und amtlicher Nachweis können sich überlagern; der gewählte Herkunftswert ersetzt nicht die gesonderten Herkunfts-/Bestätigungsmerkmale aus D1.

**Prüfbeispiel:** KI-Vermutung zu Java bleibt durch_ki_abgeleitet.

### DT-13 — NachweisgradDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-12, DM-14, DM-32, DM-33

**Zweck:** Belastbarkeit einer fachlichen Aussage bzw. Bewertung.

**Werte beziehungsweise Felder:** unbekannt; vorlaeufig; durch_nutzer_bestaetigt; extern_belegt; amtlich_bestaetigt

**Fachliche Regeln:** Die Werte bezeichnen Quellen-/Bestätigungsgrade, keine numerische Skala und keine automatische Hierarchie für fachliches Können.

**Abwesenheit, Kardinalität und Vergleich:** Fehlender Nachweis ist unbekannt, kein negativer Leistungsbefund. Der Wert ist keine vollständige Ersetzung gleichzeitiger Quellen-, Nutzerbestätigungs- und Aktualitätsmerkmale; vorhandene Nachweise bleiben separat.

**Prüfbeispiel:** Ein GitHub-Repository kann einen vorläufigen Technologiehinweis liefern.

### DT-14 — UnsicherheitsangabeDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-15, DM-24, DM-30, DM-32, DM-38, DM-52

**Zweck:** Erklärbare fachliche Unsicherheit ohne erfundene Prozentgenauigkeit.

**Werte beziehungsweise Felder:** `status` (unbekannt/gering/mittel/hoch; Ausmaß der Unsicherheit), `begruendung?`, `fehlende_basis?`.

**Fachliche Regeln:** Keine pauschale Wahrscheinlichkeit ohne kalibrierte Grundlage; fehlende Daten sind nicht gleich negative Bewertung.

**Abwesenheit, Kardinalität und Vergleich:** Unbekannte Unsicherheit bedeutet keine geringe Unsicherheit. Kategorien sind nur im beschriebenen Bewertungsrahmen vergleichbar, keine allgemeine Rangfolge persönlicher Fähigkeiten.

**Prüfbeispiel:** Bewertung der Übungsantwort: mittel wegen unvollständiger Aufgabenstellung.

### DT-15 — DatenfreigabeDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-03, DM-36, DM-44, DM-46

**Zweck:** Zweck-, daten- und zeitbezogene Zugriffs- oder Kostenfreigabe.

**Werte beziehungsweise Felder:** `eigentümer`, `zweck`, `datenumfang`, `ziel`, `gueltigkeit`, `status`, `widerrufsstand?`.

**Fachliche Regeln:** Mindestrechte; Widerruf sperrt neue Nutzung. Browseranmeldung beim Anbieter allein begründet keinen Drittzugriff.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein konkreter Eigentümer, Zweck und erlaubter Umfang je Freigabe; kein leeres Wildcard-Ziel. Freigaben nur in passendem Geltungsbereich vergleichen, nicht zu pauschalen Rechten vereinigen.

**Prüfbeispiel:** GitHub-Repositorium X nur lesend ausgewählt.

### DT-16 — BerechtigungsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-03, DM-36, DM-44

**Zweck:** Fachlicher Zustand einer Geräte- oder Integrationsberechtigung.

**Werte beziehungsweise Felder:** angefragt; aktiv; deaktiviert; abgelehnt; abgelaufen; widerrufen; fehlerhaft; unbekannt

**Fachliche Regeln:** Nur aktiv mit passendem Zweck, Datenumfang und gültigem Zugang erlaubt Zugriff; deaktiviert, unbekannt oder fehlerhaft erlauben keine Nutzung. Reaktivierung nach Deaktivierung prüft die noch vorhandene Freigabe; nach Widerruf ist eine neue Autorisierung erforderlich.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** GitHub-Freigabe widerrufen.

### DT-17 — KanalartDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-43, DM-44, DM-45, DM-47

**Zweck:** Unterscheidung der tatsächlich nutzbaren KI-Zugangswege.

**Werte beziehungsweise Felder:** oeffentliches_webangebot; verbraucherabo; offiziell_verbundene_app; api_freikontingent; api_kostenpflichtig; lokales_modell; manueller_externer_weg; unbekannt

**Fachliche Regeln:** Verbraucherabo ≠ API-Recht. Frei bedeutet nicht unbegrenzt. Öffentliches Webangebot und manuelle externe Nutzung bedeuten keine automatisierte Schnittstelle oder Zugriff auf externe Gesprächshistorien; der manuelle Weg überträgt selbst keine Daten durch Syllentra. Kein Scraping privater Sitzungen, keine inoffiziellen Cookie-Brücken.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Claude-Pro-Abonnement hat ohne separate Berechtigung keine API-Freigabe.

### DT-18 — IntegrationsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-43, DM-44, DM-45

**Zweck:** Prüfbarer Stand einer Anbieteranbindung.

**Werte beziehungsweise Felder:** nicht_unterstuetzt; katalogisiert; pruefung_noetig; verfuegbar; gesperrt; gestoert

**Fachliche Regeln:** Nur eine aktuell überprüfte, autorisierte verfügbare Kombination darf verwendet werden. Deep Link ist noch keine Datenintegration.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Nicht unterstützte LinkedIn-Schnittstelle bleibt nicht_unterstuetzt.

### DT-19 — ModellEigenschaftenDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-45, DM-46

**Zweck:** Aufgabenbezogen nutzbare Modellaussagen mit Aktualität.

**Werte beziehungsweise Felder:** `faehigkeiten`, `modalitaeten`, `qualitaetsbasis?`, `datenschutzeignung`, `zulassungsstand`, `preislage?`, `aktualisiert`.

**Fachliche Regeln:** Unbekannte Fähigkeit ist kein zugesicherter Support; kostenlose Eignung nur bei tatsächlich nachgewiesenem Kontingent.

**Abwesenheit, Kardinalität und Vergleich:** 0..n belegte Fähigkeiten und Modalitäten; fehlende Eignung ist unbekannt. Nur gleiche Aufgabe, Kriterien und Zeitstände erlauben sachlichen Vergleich, keine universelle Modellrangliste.

**Prüfbeispiel:** Modell kann Text; Audio nicht nachgewiesen.

### DT-20 — GeldbetragDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-46, DM-47

**Zweck:** Währungsgebundener Geldbetrag mit Kenntnisstand.

**Werte beziehungsweise Felder:** `betrag?`, `waehrung?`, `messstatus` (DT-22), `stand`; Betrag und Währung bei bekanntem Geldwert gemeinsam erforderlich.

**Fachliche Regeln:** Nie dimensionslose Beträge addieren oder unterschiedliche Währungen ohne begründete Umrechnung zusammenzählen; 0 nicht mit unbekannt verwechseln.

**Abwesenheit, Kardinalität und Vergleich:** Bekannter Betrag endlich und währungsgebunden; Kosten-/Budgetwert nicht negativ, echte Erstattungen bei Bedarf gesondert präzisieren. Gleichheit/Ordnung nur bei gleicher Währung und vergleichbarer Messbasis; Schätzung bleibt Schätzung.

**Prüfbeispiel:** 0 EUR nach nachweisbarem Gratis-Aufruf, nicht für unbekannten Preis.

### DT-21 — MetrikeinheitDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-46, DM-47

**Zweck:** Vergleichbare Einheit einer Nutzungsmetrik.

**Werte beziehungsweise Felder:** aufrufe; eingabe_token; ausgabe_token; zeichen; audio_sekunden; daten_bytes; geldbetrag; sonstige

**Fachliche Regeln:** Geldwerte verwenden DT-20 einschließlich Währung, nicht eine pauschale Euro-Einheit. Bei sonstige ist die konkrete Einheit zu benennen. Einheiten verschiedener Anbieter sind nicht automatisch äquivalent; nicht verfügbare Metrik bleibt unbekannt.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** 500 eingabe_token.

### DT-22 — MessstandDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-46, DM-47

**Zweck:** Verlässlichkeit einer Kosten-/Quota-/Verbrauchsangabe.

**Werte beziehungsweise Felder:** gemessen; anbieter_gemeldet; berechnet; geschaetzt; unbekannt

**Fachliche Regeln:** Aus geschätzten Kosten dürfen keine bestätigten Rechnungsbeträge gemacht werden; unbekannt wird nicht als 0 angezeigt.

**Abwesenheit, Kardinalität und Vergleich:** Messstand gilt je Kennzahl. Berechnet nennt die verwendete Grundlage; aus Schätzungen berechnete Summen werden dadurch nicht zu gemessenen Rechnungswerten.

**Prüfbeispiel:** Quota des Anbieters nicht abrufbar: unbekannt.

### DT-23 — KontingentDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-46, DM-47

**Zweck:** Verbrauchs- oder Kostenrahmen im Anbieter- und Gültigkeitskontext.

**Werte beziehungsweise Felder:** `anbieter`, `modellbezug?`, `berechtigungsbezug`, `kanal`, `obergrenze?`, `verbrauch?`, `offene_nutzung?`, `einheit`, `periode`, `messstand_je_wert`, `letzter_stand`; Geldwerte mit Währung.

**Fachliche Regeln:** Bei erschöpften oder unklaren Limits stoppt die davon abhängige Nutzung bis zur Klärung; keine unautorisierte kostenpflichtige Wiederholung oder Ausweichnutzung. Rest nur bei hinreichend verlässlichen, zeitbezogenen Grundlagen bekannt; offene oder unklare Nutzung nicht als sicher unverbraucht abziehen. Statistik ist keine aktuelle Quotenabfrage.

**Abwesenheit, Kardinalität und Vergleich:** Bekannte Mengen und Limits endlich, nicht negativ und einheitengebunden; bei Geld Währung erforderlich. Fehlende Obergrenze bedeutet unbekannt, keinesfalls unbegrenzt. Vergleich nur für denselben Zugang, Zeitraum und Berechtigungsrahmen.

**Prüfbeispiel:** API-Freikontingent mit verbleibendem Rest als datierte Anbieterangabe, nicht als garantierte aktuelle Restmenge.

### DT-24 — AbrechnungsperiodeDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-47

**Zweck:** Zeitbereich für Anbieter-/Modell-Statistik (FE-14, FE-17).

**Werte beziehungsweise Felder:** `auswahl` = tag / woche / monat / benutzerdefiniert; `intervall` (DT-05), `zeitzone` (DT-04), `wochenbeginn?`, `vollstaendigkeit`, `abgedeckte_teilintervalle`; Grenzen bei Auswertungen endlich und bekannt.

**Fachliche Regeln:** Perioden dürfen sich als alternative Ansichten überlappen, aber nicht bei Summenbildung derselben Nutzung doppelt zählen. Tages-, Wochen- und Monatsgrenzen werden in der ausgewählten Zeitzone bestimmt; der Wochenbeginn ist explizit, kein stiller universeller Standard. Ausschließlich vorhandene hinreichend aufgelöste Metriken aggregieren: Aus einer Monatssumme entstehen keine erfundenen Tageswerte oder benutzerdefinierten Teilsummen. Fehlende Zeitabdeckung bleibt erkennbar; keine zusätzlichen privaten Eingaben für feinere Statistik speichern. Aggregation ist kein Beweis für verbleibende Anbieterquota.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein explizites Auswertungsintervall je Wert. Tag/Woche/Monat und benutzerdefiniert sind ungeordnete Auswahlarten; Gleichheit umfasst Intervall, Zone und gegebenenfalls Wochenbeginn.

**Prüfbeispiel:** Auswertung 01.–15. Oktober Europe/Berlin.

### DT-25 — KIStatistikDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-47

**Zweck:** Datensparsame, periodische Nutzungssumme ohne Gesprächsduplikat.

**Werte beziehungsweise Felder:** `eigentuemerkontext`, `anbieter`, `modell`, `kanal`, `periode` (DT-24), `anzahl?`, `verbrauchswerte[0..n]`, `kosten?` (DT-20), `datenstand`; jede Kennzahl mit Einheit (DT-21), Messstand (DT-22), Herkunft, Zeitabdeckung und gegebenenfalls Tarifstand.

**Fachliche Regeln:** Keine automatisch gespeicherten Prompts, Privatnachrichten oder Antworttexte. Nur Aggregate, keine automatische Einzelaufrufhistorie und keine rekonstruierenden Gesprächsverweise. Fehlende Metrik und unvollständige Abdeckung explizit; gemessene, geschätzte und anbieterberichtete Werte nicht als einheitlich gemessen ausgeben. Einheiten, Zugangskanäle, Währungen und Berechtigungsgrenzen nicht unbemerkt vermischen.

**Abwesenheit, Kardinalität und Vergleich:** 0..n tatsächlich verfügbare Verbrauchsmetriken; unbekannt ist keine Nullsumme. Aggregate nur bei gleichem Eigentums-, Anbieter-, Modell-, Kanal-, Perioden- und Einheitenkontext vergleichen; überlappende Summen nicht addieren.

**Prüfbeispiel:** Wochenübersicht je Modell mit 23 bekannten Aufrufen, kein Prompt-Text.

### DT-26 — NotenOriginalDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-04, DM-12

**Zweck:** Unveränderter Wert der Studienleistung im ursprünglichen Hochschulsystem (FE-15).

**Werte beziehungsweise Felder:** `originalwert`, `notenformat`, `hochschul-/systembezug`, `studienzugehoerigkeitsbezug?`, `zuordnungsstand`, `skalenreferenz?`, `nachweisstatus`, `datenherkunft`, `quelle`, `stand`; fehlender Originalwert bedeutet keine erfundene Note.

**Fachliche Regeln:** Keine global deutsche 1,0–5,0-Skala erzwingen. Originalwortlaut und bekannte ursprüngliche Skala bleiben unabhängig von optionaler Umrechnung erhalten; fehlende Skala/Quelle ausdrücklich unbekannt, ohne fiktiven amtlichen Nachweis. Nachträgliche belegte Korrekturen sind sichtbar als Korrektur zu kennzeichnen; keine unsichtbare Überschreibung durch eine Äquivalenz.

**Abwesenheit, Kardinalität und Vergleich:** Ein bekannter Originalwert je Leistung; fehlende Note lässt die sonstige Studienleistung bestehen. Gleichheit mit System, Skala und Stand; keine globale numerische Ordnung von B+, bestanden und 1,7.

**Prüfbeispiel:** „B+“ bleibt B+ nach nordamerikanischer Skala.

### DT-27 — NotenskalaDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-04, DM-12

**Zweck:** Beschreibung eines belegbaren Bewertungssystems.

**Werte beziehungsweise Felder:** `skalenname`, `institution?`, `regelungs-/kursbezug?`, `grenzen/werte?`, `richtung?`, `bestehensregel?`, `quelle`, `gueltigkeit`, `kenntnisstand`.

**Fachliche Regeln:** Nur belegt verfügbare Skalenregeln verwenden; unterschiedliche Hochschul- oder Kursordnungen können unterschiedliche Skalen haben.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein belegtes oder als unvollständig markiertes Bewertungssystem je Wert; zulässige Werte und Richtung nur aus zugehöriger Regel. Skalenidentität umfasst Institution/Regelungsbereich und Gültigkeit.

**Prüfbeispiel:** Hochschule A: zulässige Originalnoten und Prädikate.

### DT-28 — NotenAequivalenzDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-12

**Zweck:** Optionale unverbindliche und begründete Vergleichsansicht (FE-15).

**Werte beziehungsweise Felder:** `originalnotenbezug`, `ausgangswert`, `ausgangsskala`, `zielskala`, `ergebnis?`, `methode`, `quelle`, `regelstand`, `unsicherheit`, `ist_indikativ=true`.

**Fachliche Regeln:** Keine automatische offizielle Anerkennung; nicht berechenbare oder unzureichend belegte Umrechnung unterdrücken. Original bleibt sichtbar im geöffneten Notenbereich.

**Abwesenheit, Kardinalität und Vergleich:** 0..1 angebotene Äquivalenz je expliziter Zielskala und Regelstand; keine belastbare Regel bedeutet keine berechnete Zahl. Vergleich nur innerhalb derselben begründeten Zielskala; Originalwert nie überschreiben.

**Prüfbeispiel:** B+ → nur falls belastbare Umrechnungsregel existiert, als indikativ.

### DT-29 — NotenAnsichtDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-02, DM-04, DM-12

**Zweck:** Fachliche Gruppierung von Leistungen nach Institution/Studienzugehörigkeit.

**Werte beziehungsweise Felder:** `institution/Studienzugehoerigkeit`, `zuordnungsstand`, `leistungsreferenzen[0..n]`, `sichtbarkeitsregeln` (DT-58), `sortierung?`, `zugriffsberechtigung`; eine ausgewählte, eindeutig bestimmte Gruppierung je Detailansicht.

**Fachliche Regeln:** Standard: Profil zeigt geschlossene Rubrik „Noten“ ohne einzelne Werte. Erst Rubrik öffnen, dann Institution/Studienzugehörigkeit auswählen; kein ungewolltes Anzeigen auf Dashboard, Push oder Vorschau. Fehlende Institution/Studienzugehörigkeit nicht erraten: Manuelle Leistungen bleiben erfassbar; bei ungeklärter Zuordnung keine Institution erfinden und die Leistung nicht automatisch in einer Institutionsansicht anzeigen. Die Klärung und geschützte Bearbeitung solcher Eingaben sind in B1 zu präzisieren; eine zusätzliche institutionslose Notenübersicht ist hier nicht freigegeben. Gruppenauswahl ersetzt keine Zugriffsberechtigung. Exakte Dialogfolge durch B1.

**Abwesenheit, Kardinalität und Vergleich:** Je gewählter geschützter Gruppe 0..n Leistungsreferenzen desselben Eigentümers; eine Leistung nur bei bestätigter Zuordnung einer Institution zurechnen. Kein automatisches Zusammenführen gleichnamiger Hochschulen oder Berechnen eines institutionsübergreifenden Schnitts.

**Prüfbeispiel:** Mein Profil → Noten → THM → Leistungen; weitere Hochschule separat.

### DT-30 — ECTSWertDT

**Art:** Skalar\
**Betroffene D1-Entitäten:** DM-06, DM-12

**Zweck:** Nichtnegativer Punktewert in einer ausdrücklich gekennzeichneten Leistungskategorie.

**Werte beziehungsweise Felder:** Endlicher Dezimalwert >= 0; unbekannt ist kein Zahlenwert. Soll-ECTS und erworbene ECTS semantisch getrennte Felder.

**Fachliche Regeln:** ECTS erfordern entsprechende Studienkontexte; keine positive Kompetenzbehauptung aus ECTS allein.

**Abwesenheit, Kardinalität und Vergleich:** Bekannte Werte nach Dezimalwert innerhalb derselben ECTS-Kategorie vergleichbar; unbekannt ist nicht 0. Derselbe Leistungsnachweis darf in einer Summe nicht über mehrere Bezüge doppelt zählen.

**Prüfbeispiel:** Modul-Soll 6 ECTS, erworben noch unbekannt.

### DT-31 — StudienstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-04, DM-05, DM-06, DM-07, DM-08

**Zweck:** Status akademischer Zugehörigkeiten und Arbeitsbereiche.

**Werte beziehungsweise Felder:** geplant; aktiv; ruhend; abgeschlossen; archiviert; unbekannt

**Fachliche Regeln:** Archiviert ist nur der jeweilige Archivzustand, kein Ersatz für den gesonderten Abschluss-/Leistungsstand; DT-62 bleibt getrennt. Semesterzeit allein rechtfertigt keinen Statuswechsel oder Verlust offener Aufgaben.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Semester abgeschlossen, aber offenes Projekt bleibt aktiv.

### DT-32 — PruefungsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-11, DM-12

**Zweck:** Stand eines Prüfungsvorgangs.

**Werte beziehungsweise Felder:** angekuendigt; terminiert; verschoben; absolviert; bewertet; abgebrochen; unbekannt

**Fachliche Regeln:** Verschoben erfordert Quellenprüfung; amtliche Note nur mit entsprechender Herkunft. Wiederholungen sind eigene Versuche.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Prüfung verschoben, Lernplan unverändert bis Bestätigung.

### DT-33 — ProjektstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-16, DM-18

**Zweck:** Fachlicher Stand einer Projektarbeit/-aufgabe.

**Werte beziehungsweise Felder:** geplant; aktiv; pausiert; abgeschlossen; archiviert; abgebrochen

**Fachliche Regeln:** Archivierung nach bestätigter Eignung; Kursabschluss beendet Projekt nicht automatisch.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Projekt läuft über zwei Semester.

### DT-34 — KontexttypDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-09, DM-10, DM-22, DM-27, DM-39

**Zweck:** Zulässige Zielart einer fachlichen Verknüpfung.

**Werte beziehungsweise Felder:** semester; modul; kurs; thema; projekt; pruefung; lernziel; allgemein

**Fachliche Regeln:** Für einen konkreten Bezug muss das Ziel tatsächlich zugänglich sein und zur Eigentumsgrenze gehören. DM-22 erlaubt nur Modul/Kurs/Thema/Projekt, DM-27 nur Modul/Kurs/Projekt, DM-17 genau Projekt und Modul. allgemein bedeutet kein künstliches Zielobjekt und keinen erzwungenen Kontextbezug. Nicht jede Beziehung erlaubt jeden Zieltyp.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Gesprächskontext projekt.

### DT-35 — KontextBezugDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-17, DM-22, DM-27, DM-39

**Zweck:** Identifizierbare Beziehung zu einem bestehenden fachlichen Kontext.

**Werte beziehungsweise Felder:** `typ` (DT-34), `zielkennung` (DT-01), `herkunft` (DT-12), `gueltigkeitsstand`, `bestaetigungsstand`; je konkretem Bezug genau ein erlaubtes Ziel, mehrere Bezüge als eigene Relationen.

**Fachliche Regeln:** Linkentfernung ändert nicht das verlinkte Original. KI-Klassifizierung verlangt Bestätigung, Startkontext eines Gesprächs nicht.

**Abwesenheit, Kardinalität und Vergleich:** Genau eine erlaubte Zielart mit passender Kennung je Relation; mehrere Kontexte durch mehrere Relationen. Gleichheit von Ziel und Beziehung getrennt betrachten; allgemein bleibt kontextfrei, ohne erfundenes Ziel.

**Prüfbeispiel:** Dasselbe PDF zu Kurs A und Projekt B verlinkt.

**Präzisierung DEC-V1-02/09:** Auch qualifizierte sekundäre Themen-/Lernzielbezüge von DM-09 tragen erlaubte Zielkennung, Relationsgrund, Quellrevision, Herkunft und Unsicherheit; weder Elternhierarchie noch Kompetenzübertragung ableiten. Keine neue Zielart oder fremder Kontenzugriff durch die Kartenansicht.

[Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### DT-36 — DokumentFassungDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-20, DM-21

**Zweck:** Identität einer versionierten Inhaltsfassung einschließlich Rückverfolgbarkeit.

**Werte beziehungsweise Felder:** `dokumentkennung`, `versionskennung`, `revisionsfolge`, `quelle`, `fassungzeit?`, `pruefsumme?`.

**Fachliche Regeln:** Version gehört genau einem Dokument; aktiver Bezug zeigt auf eine eigene vorhandene Version. Auch ein archiviertes Dokument hat 1..n vorhandene Versionen und genau eine aktive. Neue Fassung ersetzt oder aktiviert nichts automatisch; historische Zitate und Ableitungen bleiben an die tatsächlich verwendete Version gebunden. Löschen der letzten Version bei fortbestehendem Original unzulässig; Wechsel vor Löschung der aktiven Version nur mit ausdrücklich gewählter eigener verbleibender Fassung nach D1.5.3.

**Abwesenheit, Kardinalität und Vergleich:** Dokument- und Versionskennung erforderlich, Herkunft darf ausdrücklich unbekannt sein. Revisionsfolgen nur innerhalb desselben Originals ordnen; Identität einer Fassung nicht mit deren aktuellem Inhaltszugriff verwechseln.

**Prüfbeispiel:** PDF v1, PDF v2; v1 weiterhin referenzierbar.

### DT-37 — AbleitungsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-21, DM-24

**Zweck:** Status bearbeiteter bzw. extrahierter Informationen.

**Werte beziehungsweise Felder:** vorlaeufig; geprueft; unvollstaendig; veraltet; quelle_entfernt; geloescht

**Fachliche Regeln:** Quellenlöschung entwertet behauptete Nachprüfbarkeit; Eine unabhängig behaltene Ableitung ist kein nachweislich verfügbares Original. Ihr Löschumfang und die historischen Quellbezüge werden nach D1 getrennt ausgewiesen; keine verdeckte Vollkopie eines zur Löschung bestimmten Inhalts.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Transkript mit fehlendem Abschnitt: unvollstaendig.

### DT-38 — GespraechsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-25, DM-26

**Zweck:** Auffindbarkeit, Archivierung und Verfügbarkeit eines Gesprächs.

**Werte beziehungsweise Felder:** aktiv; archiviert; loeschung_angefordert; geloescht

**Fachliche Regeln:** Archiviert bleibt auffindbar und ist keine Löschung; Nachrichtenhistorie getrennt von Erinnerungen. DM-26 übernimmt hier nur Verfügbarkeit/Löschbezug seiner Unterhaltung, keinen eigenständigen Gesprächsarchivstatus; Verarbeitungsfehler einer Nachricht sind davon getrennt.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Unterhaltung archiviert, Erinnerung weiterhin separat.

### DT-39 — NachrichtenrolleDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-26

**Zweck:** Kennzeichnung des Erzeugers einer Nachricht.

**Werte beziehungsweise Felder:** nutzer; assistent; werkzeug; system

**Fachliche Regeln:** Rolle ist keine Autorisierung. Externe Werkzeugtexte werden als nicht vertrauenswürdiger Inhalt behandelt.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Werkzeugausgabe = werkzeug, keine Nutzerfreigabe.

### DT-40 — LernmodusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-28, DM-29, DM-30

**Zweck:** Unterstützte fachliche Lernart.

**Werte beziehungsweise Felder:** erklaerung; uebung; wiederholung; pruefungssimulation; reflektieren; frei

**Fachliche Regeln:** Lernen darf ohne vollständiges Profil beginnen; nicht jeder Schritt erfordert Frage.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Prüfungssimulation getrennt von amtlicher Prüfung.

### DT-41 — AufgabenschwierigkeitDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-29, DM-30, DM-32

**Zweck:** Aufgabenrelative Schwierigkeit mit erklärbarem Bezug zum Lernziel.

**Werte beziehungsweise Felder:** `niveau?`, `bezugsziel`, `grundlage`, `unsicherheit`.

**Fachliche Regeln:** Keine universelle numerische Fähigkeitsskala ohne pädagogische Kalibrierung; adaptives Angebot orientiert sich an Evidenz.

**Abwesenheit, Kardinalität und Vergleich:** Unbekanntes Niveau ist keine niedrige Schwierigkeit. Vergleich nur bei gleicher Aufgabe-/Lernzielgrundlage und passendem Bewertungsmaßstab.

**Prüfbeispiel:** Schwierigkeit „mittel“ relativ zu SQL-JOIN-Lernziel.

### DT-42 — AntwortBewertungDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-30, DM-31, DM-32

**Zweck:** Differenzierte Antwortprüfung unter Berücksichtigung verwendeter Hilfen.

**Werte beziehungsweise Felder:** `korrektheit`=richtig/teilweise/falsch/nicht_bewertbar; `begruendung`, `sicherheit`, `hilfen[]`, `selbststaendig?`.

**Fachliche Regeln:** Vollständige Lösungshilfe ≠ selbstständige richtige Antwort; unklare Frage nicht als sicher falsch werten. Leere Hilfenliste oder unbekannte Selbstständigkeit beweisen keine Eigenleistung. Bekannte zuvor gezeigte Lösungen sind auch bei späteren Versuchen zu berücksichtigen.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein Korrektheitsbefund je bewerteter Antwort; Hilfen 0..n und Selbstständigkeit gegebenenfalls unbekannt. Gleichheit von Befunden beweist keine gleiche Fähigkeit; Kategorien bilden keine offizielle Notenskala.

**Prüfbeispiel:** Falsches Vorzeichen nach einem ersten Hinweis korrigiert: teilweise unterstützt.

### DT-43 — HilfestufeDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-31

**Zweck:** Pädagogische Unterstützungsart gemäß FE-07.

**Werte beziehungsweise Felder:** orientierung; gezielter_hinweis; teilschritt; vollstaendige_loesung

**Fachliche Regeln:** Keine starre Pflichtreihenfolge und keine feste Anzahl; vollständige Lösung auf ausdrücklichen Wunsch sofort möglich.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Erst Hinweis auf Umformung, später Lösungsweg.

### DT-44 — LernfortschrittDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-28, DM-32

**Zweck:** Bearbeitung eines Lernziels ohne automatischen Kompetenznachweis.

**Werte beziehungsweise Felder:** `bearbeitungsstand`, `wissen?`, `nachweise[]`, `aktualitaet`, `hilfebezug`.

**Fachliche Regeln:** Gelesenes Kapitel != Wissensstand != belegte Kompetenz != Note/ECTS.

**Abwesenheit, Kardinalität und Vergleich:** Fortschritt, Wissen und Beleggrad bleiben getrennt. Prozentwerte nur bei bekanntem Nenner und konsistentem Bereich von 0 bis 100; unbekannter Wissensstand bleibt unbekannt. Vergleich nur für denselben Zielumfang und Zeitstand.

**Prüfbeispiel:** Kapitel 100 % gelesen, Wissensstand unbekannt.

**Präzisierung L-02/L-08:** `verstaendnis_geprueft` wird mit tatsächlichen Aufgaben-/Versuchs-/Hilfebelegen und Zeit geführt; `bearbeitet`, `wissensstand_geschaetzt` und `kompetenz_nachgewiesen` bleiben unabhängige Aussagen mit eigener Belegqualität. Kein automatischer Übergang durch Lesen, Timerablauf oder abgearbeitete Wiederholung. Plan-Undo ändert diese Evidenzfelder nicht.

**Präzisierung DEC-V1-08/17/21:** Optionaler Bezug auf manuelles Sitzungsfeedback und tatsächliche Dauer/Messgrundlage samt Unterbrechungs-/Lückenangabe; fehlend bleibt unbekannt oder bewusst nicht gespeichert. Geschätzte Dauer ist kein Messwert. Eine Bilanz referenziert reale Antworten/Hilfen und Zeitraum, keine erfundene Bestehensprognose.

[Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### DT-45 — ErinnerungsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-33, DM-34

**Zweck:** Vertrauens-/Aktualitätsstand langfristiger pädagogischer Erinnerung.

**Werte beziehungsweise Felder:** vorlaeufig; bestaetigt; zur_neubewertung; ueberholt; geloescht

**Fachliche Regeln:** FE-16: veraltete/widersprüchliche Schätzung auf „zur Neubewertung“; nicht allein wegen des Alters oder Widerspruchs löschen, nicht als aktuelle sichere Aussage weiterverwenden. Dies gilt auch für zuvor bestätigte Einschätzungen; neuer Beleg, Anlass und Zeitpunkt bleiben erkennbar. Nutzerbestätigung und Aktualität sind getrennte Merkmale. FE-16 sperrt weder ausdrücklich gewählte Löschung nach FE-13 noch tatsächlich geltende Aufbewahrungs-/Löschregeln.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** „Kann SQL JOIN“ nach widersprechendem Test: zur_neubewertung.

### DT-46 — ErinnerungsRevisionDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-33, DM-34

**Zweck:** Versionierte, explizit löschbare fachliche Aussage mit Korrekturgrund.

**Werte beziehungsweise Felder:** `eintragkennung`, `revisionskennung`, `revisionsfolge`, `aussage`, `status` (DT-45), `nachweis-/bestaetigungsstand`, `unsicherheit?`, `quellen[0..n]`, `aenderungsgrund?`, `zeitpunkt`; fehlende Begründung als unbekannt kennzeichnen.

**Fachliche Regeln:** Ein fortbestehender DM-33 hat genau eine aktuelle eigene DM-34 und 0..n frühere Revisionen. Die aktuelle Aussage ist eine Sicht darauf, keine unabhängige widersprechende Kopie. Historie kann gezielt entfernt werden; umfasst die Löschung auch die aktuelle Aussage, nur mit ausdrücklich bestimmtem zulässigem Ersatzstand fortbestehen, sonst Eintrag löschen. Niemals still ältere Aussagen wiederbeleben. geloescht bezeichnet höchstens verbleibende zulässige Statusmetadaten, keine inhaltlich noch verfügbare aktuelle Revision. Nach Löschen keine stille Wiederherstellung aus Revisionen, Caches oder Nebenprotokollen.

**Abwesenheit, Kardinalität und Vergleich:** Revision gehört genau einem Erinnerungseintrag; Quellen 0..n. Reihenfolge nur innerhalb dieses Eintrags und ohne Anspruch auf lückenlos erhaltene Historie nach berechtigter Löschung.

**Prüfbeispiel:** Revision 2 korrigiert Annahme über Java-Erfahrung.

### DT-47 — VorschlagsartDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-39, DM-40

**Zweck:** Fachlicher Anlass eines bestätigungspflichtigen Vorschlags.

**Werte beziehungsweise Felder:** dokumentklassifizierung; studienimport; kalenderplanung; pruefungsverschiebung; semesterarchivierung; kostenfreigabe; sonstige

**Fachliche Regeln:** Nicht jeder Hinweis ist ein Vorschlag; manuelle Speicherung und automatisch sichtbarer Gesprächskontext erzeugen keinen künstlichen Vorschlag.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Prüfungsverschiebung erzeugt ggf. kalenderplanung.

### DT-48 — VorschlagsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-39, DM-40, DM-41

**Zweck:** Entscheidungsstand einer konkreten Vorschlagsfassung aus F2.11.1.

**Werte beziehungsweise Felder:** offen; angenommen; abgelehnt; gegenstand_entfallen

**Fachliche Regeln:** „Später“ bleibt offen. Neue inhaltliche Fassung ist zunächst offen; ältere Entscheidung autorisiert neue Inhalte nicht. Final widersprüchliche Entscheidungen auf mehreren Geräten unzulässig.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein Entscheidungsstand je betrachteter Fassung. Final angenommen oder abgelehnt wird nicht durch späteres Bearbeiten umgeschrieben; die neue Fassung wird getrennt offen geprüft.

**Prüfbeispiel:** Gerät A lehnt v1 ab, Gerät B darf v1 nicht annehmen.

### DT-49 — VorschlagsaktionDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-41

**Zweck:** Einzelne Nutzerentscheidung an einer Fassung.

**Werte beziehungsweise Felder:** annehmen; ablehnen; spaeter; bearbeiten

**Fachliche Regeln:** Bearbeiten erzeugt bei Inhaltsänderung neue offene Fassung; spaeter ist keine finale Ablehnung. Entscheidung zu konkretem Stand gebunden.

**Abwesenheit, Kardinalität und Vergleich:** Aktion ist kein langlebiger Entscheidungsstatus. Wiederholtes Öffnen oder spaeter erzeugt keine zweite finale Entscheidung; die konkrete Fassung bleibt erforderlich.

**Prüfbeispiel:** „Später“ = Status offen.

### DT-50 — AusfuehrungsstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-42

**Zweck:** Stand der tatsächlichen Wirkung nach einer zulässigen Annahme.

**Werte beziehungsweise Felder:** nicht_uebernommen; uebernahme_laeuft; uebernommen; teilweise_uebernommen; fehlgeschlagen; ergebnis_unklar

**Fachliche Regeln:** Jeder DM-42-Beleg gehört genau zu einer wirksam annehmenden DM-41-Entscheidung derselben Fassung; Rechte, Kostenrahmen und bestätigte Grundlage bleiben erforderlich. Annahme ist kein Erfolg. ergebnis_unklar vor Wiederholung abgleichen; je Fassung, Ziel und Teilwirkung höchstens eine logische Wirkung. Änderungen der Grundlage erfordern aktuelle Prüfung statt Übertragung einer alten Annahme.

**Abwesenheit, Kardinalität und Vergleich:** Wirkstatus bezieht sich auf den tatsächlich betrachteten Ziel-/Teilwirkungsumfang. Verlorene Verbindung beweist keinen Fehler ohne Wirkung; bei unbekannter Wirkung ergebnis_unklar statt vorschnell fehlgeschlagen.

**Prüfbeispiel:** Akzeptierte Zeitplanung, Netzfehler: ergebnis_unklar.

### DT-51 — ImportstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-37, DM-40

**Zweck:** Stand eines angekündigten Datenimports.

**Werte beziehungsweise Felder:** eingegangen; pruefung_noetig; freigabe_ausstehend; uebernommen; abgelehnt; fehlgeschlagen

**Fachliche Regeln:** Vorschlag nur bestätigt übernehmen, Duplikate und externe Quellenstände prüfen; wiederholter Import darf nicht verdoppeln.

**Abwesenheit, Kardinalität und Vergleich:** Importstand ersetzt weder Vorschlagsentscheidung noch Wirkung. Teilübernahme und unklare Wirkung bleiben über DT-50 getrennt erkennbar; ein fehlgeschlagener Import erklärt bereits gespeicherte Teilwirkungen nicht für ungeschehen.

**Prüfbeispiel:** Stundenplan importiert, Freigabe ausstehend.

### DT-52 — TerminstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-11, DM-35

**Zweck:** Stand des internen Studientermins.

**Werte beziehungsweise Felder:** geplant; bestaetigt; verschoben; erledigt; abgesagt

**Fachliche Regeln:** Bewusst manuell gespeicherter Eintrag direkt; importierte oder KI-geplante Termine erst nach Übernahme. Externe Kalender nie als Schreibziel.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** KI-Lerntermin geplant erst nach Annahme.

### DT-53 — VerfuegbarkeitsfensterDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-35, DM-36

**Zweck:** Minimierte persönliche Kalenderverfügbarkeit.

**Werte beziehungsweise Felder:** `zeitraum`, `belegt` (ja/nein/unbekannt), `herkunft`, `abrufstand`.

**Fachliche Regeln:** Keine vollständige dauerhafte Kopie privater Titel, Einladungen, Personen oder Notizen; ausnahmslos lesend.

**Abwesenheit, Kardinalität und Vergleich:** 0..n minimierte Fenster je erlaubtem Zeitraum. Vergleich nach bekanntem Intervall und Abrufstand; fehlender oder veralteter Abruf erzeugt keine angenommene Freizeit.

**Prüfbeispiel:** Freier Zeitraum Montag 14–16, ohne privaten Eventtitel.

### DT-54 — SynchronisationsKonfliktDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-03, DM-25, DM-39, DM-41, DM-48

**Zweck:** Konflikt zweier Änderungen desselben Objektstandes.

**Werte beziehungsweise Felder:** `objekt`, `basisrevision`, `kandidat_a`, `kandidat_b`, `konfliktart`, `entscheidung?`.

**Fachliche Regeln:** Nicht still überschreiben; bei finalen Entscheidungen aktuelles Ergebnis respektieren; widerrufenes Gerät kann keinen Zugriff behalten.

**Abwesenheit, Kardinalität und Vergleich:** Mindestens zwei konkurrierende Kandidaten und ein bekanntes Bezugsobjekt; Basis kann ausdrücklich unbekannt sein. Kandidaten sind geschützte, löschumfangspflichtige Daten und keine unbegrenzte Schattenhistorie.

**Prüfbeispiel:** Zwei Geräte entscheiden Vorschlag gleichzeitig.

### DT-55 — VersionsstandDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-20, DM-21, DM-39, DM-40, DM-48, DM-49

**Zweck:** Vergleichbarer Revisionsstand einer fachlichen Entität.

**Werte beziehungsweise Felder:** `objektkennung`, `revision`, `aktualisiert`, `ursprung`, `basis?`.

**Fachliche Regeln:** Nur Versionsgleichheit oder fachlich zulässiger Nachfolger; keine stillen last-write-wins-Verluste.

**Abwesenheit, Kardinalität und Vergleich:** Objektbezug und Revisionsidentität erforderlich. Nachfolgerordnung nur innerhalb desselben Objekts und mit bekannter Grundlage; Zeitstempel allein beweist keine Nachfolge oder Freigabe.

**Prüfbeispiel:** Dokumentstand v2 ersetzt nicht v1-Quellenverweis.

### DT-56 — KompetenzBelegDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-13, DM-14, DM-19, DM-23

**Zweck:** Nachvollziehbarer Kompetenzhinweis mit Beitrag und Belegqualität.

**Werte beziehungsweise Felder:** `kompetenz`, `belegquelle`, `belegtyp`, `selbststaendigkeit`, `nachweisgrad`, `aktualitaet`, `unsicherheit`.

**Fachliche Regeln:** Öffentliche GitHub-Sprache allein beweist keine Beherrschung oder persönliche Autorschaft; Projektteams und KI-Anteile wenn erkennbar differenzieren.

**Abwesenheit, Kardinalität und Vergleich:** Genau eine Kompetenzzuordnung mit nachvollziehbarem Evidenzbezug oder ausdrücklich vorläufiger Grundlage. Vergleich nach Kontext und Belegqualität, keine sichere Autorschaft aus Profilbesitz oder Repository-Sprache.

**Prüfbeispiel:** Repository nutzt Java: Indiz, nicht amtliches Zertifikat.

### DT-57 — GitHubProfilReferenzDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-14, DM-19, DM-23, DM-44

**Zweck:** Freiwillige offizielle GitHub-Kontoverbindung und öffentliche Leseanalyse gemäß FE-43.

**Werte beziehungsweise Felder:** `profil_url?`, `verbundenes_konto`, `scope` = `ausgewaehlte_oeffentliche_repositories` oder `alle_eigenen_oeffentlichen_repositories`, `repository_urls[0..n]`, `zugriff=oeffentlich_lesend`, `pruefstand`, `freigabe`, `quellrevision`, `urheberschaftsnachweis?`.

**Fachliche Regeln:** Scope bewusst wählen. Einzelauswahl erweitert sich nicht still; Gesamtauswahl kann neue eigene öffentliche Repositories nur unter gültiger Synchronisationsregel berücksichtigen. Private Repositories und Schreibzugriff sind in V1 ausgeschlossen. Offizieller Zugang und Limits sind vor Nutzung nachzuweisen; URL allein ist kein Kontonachweis. Dauerhafter optionaler Profilbezug ist in D1 DM-19/DM-23/DM-44 präzisiert.

**Abwesenheit, Kardinalität und Vergleich:** Profil-URL 0..1; Repositoryauswahl 0..n, bei Einzelanalyse mindestens ein erlaubtes öffentliches Ziel. Leere Gesamtauswahl ist möglich und wird nicht mit Fehler oder Zugriffsrecht auf andere Konten verwechselt. Identität, Scope und aktuelle Freigabe sind gemeinsam zu prüfen; Repositorysprache beweist keine individuelle Urheberschaft.

**Prüfbeispiel:** „Alle meine öffentlichen Repositories“ liest ein neues eigenes öffentliches Repository nur im aktiven erlaubten Sync, niemals ein privates und niemals schreibend.

### DT-58 — DatenschutzSichtbarkeitDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-02, DM-12, DM-14, DM-33, DM-47

**Zweck:** Schutzklasse fachlicher Ansichten und Benachrichtigungen.

**Werte beziehungsweise Felder:** nur_nach_oeffnen; im_geschuetzten_detail; in_allgemeiner_uebersicht; nie_in_benachrichtigung

**Fachliche Regeln:** Die Werte sind kontextbezogene Regeln und dürfen kombiniert werden, etwa geschütztes Detail plus nie_in_benachrichtigung; sie sind keine Rangfolge. Widersprüche werden zugunsten der jeweils strengeren Schutzregel aufgelöst, nicht zur Freigabe ausgelegt. Für Noten gilt verbindlich: kein Einzelwert auf Mein Profil, Dashboard, Vorschau oder Benachrichtigung; nur im ausdrücklich geöffneten, institutionsbezogen ausgewählten und berechtigten Detail. Eine allgemeine Übersichtskonfiguration darf dies nicht aufheben; externes Teilen ist nie impliziert. Systemnotiz darf keine Note auf Sperrbildschirm enthüllen.

**Abwesenheit, Kardinalität und Vergleich:** Je Anzeigekontext eine oder mehrere gleichzeitig geltende Schutzregeln. Fehlende Regel ist keine Freigabe; keine allgemeine Ordnung, welche die strengere Regel unbeabsichtigt ersetzt.

**Prüfbeispiel:** Dashboard zeigt keine Einzelnoten.

### DT-59 — DatenkontrollStatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-50, DM-51

**Zweck:** Status einer Korrektur-, Export- oder Löschanfrage.

**Werte beziehungsweise Felder:** beantragt; bestaetigung_noetig; in_arbeit; teilweise_abgeschlossen; abgeschlossen; fehlgeschlagen; externe_reste_ungeklaert

**Fachliche Regeln:** Nicht als abgeschlossen melden, wenn Backups/Anbieter unbekannt oder Vorgang partiell. Tatsächliche Entfernung der Historie und Ableitungen prüfen.

**Abwesenheit, Kardinalität und Vergleich:** Abschluss nur im ausgewiesenen tatsächlich erfüllten Umfang. Eine abgeschlossene lokale Teilwirkung und offene externe Restpunkte sind getrennt erkennbar; keine vollständige Löschung aus bloßem Antrag ableiten.

**Prüfbeispiel:** Gespräch gelöscht, externe Aufbewahrung ungeklärt.

### DT-60 — LoeumfangDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-20, DM-21, DM-22, DM-25, DM-33, DM-34, DM-50

**Zweck:** Kontrollierter Umfang einer Datenentfernung.

**Werte beziehungsweise Felder:** `ziele[1..n]` jeweils mit Zielart, Zielkennung und gegebenenfalls konkreter Revision/Fassung; `revisionsumfang`, `ableitungsumfang`, `ausnahmen`, `bestaetigter_umfang`; keine unverbundenen Listen mit uneindeutiger Paarung.

**Fachliche Regeln:** Verknüpfung entfernen != Original löschen; Erinnerungshistorie separat wählbar; unerreichbare externe Löschung kenntlich.

**Abwesenheit, Kardinalität und Vergleich:** 1..n eindeutig gepaarte Ziele; Umfang auf konkrete Beziehungen, Versionen, Erinnerungsstände und Ableitungen beziehen. Gleiche Zielkennung bei unterschiedlichem Umfang ist keine gleiche Löschfreigabe.

**Prüfbeispiel:** Lösche Erinnerung inklusive Revisionen, behalte unabhängige Prüfung.

### DT-61 — KonfigurationswertDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-48, DM-49

**Zweck:** Typisierte, versionsgebundene erlaubte Konfiguration.

**Werte beziehungsweise Felder:** `bereich` (CFG-01 bis CFG-17), `schluessel`, `werttyp`, `wert` oder geschützter Geheimnisverweis, `validierung`, `revisionsstand`, `sensitivitaet`.

**Fachliche Regeln:** CFG-01..CFG-17 vorgegeben; kein beliebiger Code, keine externen Kalenderschreibrechte und keine Klartext-Zugangsdaten in sichtbaren Einstellungen. Vorschau wirkt nicht auf aktive Werte; Wiederherstellung validiert heutige Grenzen und hebt weder Notenschutz noch echte Löschung, Widerruf oder Kostenregeln auf.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein unterstützter Schlüssel mit zulässigem Werttyp je Wert; unbekannter Schlüssel oder ungültiger Wert wird nicht wirksam. Geheimnisinhalt ist keine normale Textausgabe; Gleichheit von Fassungen ersetzt keine erneute Validierung.

**Prüfbeispiel:** Menütitel geändert; Zugriffsrechte unverändert.

**FE-21-Parameter im vorhandenen Typ:** Unterstützte Schlüssel für Ausgabesprache (DT-07), Stimme (nur tatsächlich verfügbare Auswahl), Geschwindigkeit (nur belegter unterstützter Bereich) und ausdrückliche Hörmoduswahl (ein/aus, Standard aus). Kein beliebiger Servicecode und kein implizites Mikrofon-/Anbieterrecht. DM-02 referenziert persönliche Werte; DM-48/DM-49 führen gültige Fassungen. Unbekannte Fähigkeit ist nicht aktivierbar, fehlender Tempobereich wird nicht durch erfundene Zahlen ersetzt.

**AUDIO-01/02/03 — unterstützte Parameter im selben Typ:**

| Parametergruppe | Fachlicher Wertebereich / Validierung |
|---|---|
| Geltung und Herkunft | Genau eigenes Konto; global, je Audiosprache (DT-07) und vorhandene Kurs-/Gesprächsgeltung mit berechtigtem Bezug und Revision. Explizites Aus, geerbt, unbekannt und nicht verfügbar bleiben verschieden. FE-74 bleibt maßgeblich; Konflikte zeigen, keine neue Prioritätsregel erfinden. |
| Optionale Benachrichtigungstöne | Aktivierung/Lautlos und Referenz auf einen tatsächlich freigegebenen In-App-Tonkatalogeintrag samt Fassung; OS-/Push-Tonwahl getrennt und nur bei nachgewiesener Plattformfähigkeit. Keine freie URL oder ausführbare Konfiguration. |
| Stimme je Audiosprache | Zuordnung Sprache → Motor-/Stimmenreferenz und Katalogfassung; FR/DE/EN initialer Zielumfang. Nur tatsächlich verfügbare erlaubte Stimmen auswählbar; entfernte/unklare Referenz wird unverfügbar, keine andere Sprache still einsetzen. |
| Tempo und Lautstärke | Nur belegter Wertebereich und Einheit des erlaubten Motors/Geräts; unbekannt ist kein erfundener Zahlenwert. Lautstärke nur soweit kontrollierbar, keine OS-Lautstärkegarantie. |
| Hörmodus | Ausdrückliche persönliche Wahl ein/aus, Standard aus; aktiver Laufzustand separat und an Sitzung/Gerät/Gespräch gebunden. Persistenz/Sync eines Werts erteilt keine automatische Wiedergabefreigabe nach Wiederanmeldung/Gerätewechsel. |
| Verwaltungswerte | Zulässige Kataloge, Audioverfügbarkeit, Rollen-/Serverflags, Quoten-/Kostenobergrenzen und Verfügbarkeitstexte nur unter passendem Verwaltungsrecht; keine persönlichen Inhalte oder neue Anbieterberechtigung. |

Fachliche Zuordnung innerhalb vorhandener CFG-09/10/11/14/15; keine CFG-18. Vorschau ist eine bewusste Aktion mit neutralem Text, kein persistierter Privattext. Reset setzt nur gewählte unterstützte Präferenzen auf angezeigte zulässige Standards, startet keine Ausgabe und hebt keine Datenschutz-/Anbieterentscheidung auf. [B1.13](B1-dialogspezifikation.md#b113-abnahmeszenarien-für-töne-und-stimmen) prüft unter anderem entfernte Stimme, Lautlos und Rechteentzug.

**Präzisierung DEC-V1-06/18/19/25:** Ausschließlich unterstützte persönliche Präferenzen für Lernprofil-/Hilfe-/Pausen-/Zielangebote mit Aktivierung/Deaktivierung; manuelle Rückmeldung, Korrektur und Ablehnung/Aufschub getrennt von KI-Schätzung. Keine neue Gesundheitskategorie, Pflichtprofilierung oder automatische Kosten-/Kalenderfreigabe.

[Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### DT-62 — ArchivstatusDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-05, DM-16, DM-20, DM-25

**Zweck:** Unterscheidet aufbewahrte und archivierte Daten von gelöschten.

**Werte beziehungsweise Felder:** aktiv; archivierung_vorgeschlagen; archiviert

**Fachliche Regeln:** Archivierung nur nach Prüfung abgeschlossener Arbeit, falls FE-06 betroffen; archivierte Gespräche/Dokumente bleiben auffindbar.

**Abwesenheit, Kardinalität und Vergleich:** Abwesenheit und Gleichheit nach D2.1.1; Werte ungeordnet und ohne implizite Freigabe. Nicht aufgeführte Werte benötigen eine versionierte Spezifikationsänderung.

**Prüfbeispiel:** Offene Wiederholungsprüfung nicht archiviert.

### DT-63 — DatenkategorieDT

**Art:** Enumeration\
**Betroffene D1-Entitäten:** DM-01..DM-52

**Zweck:** Referenz auf fachliche Datenklassen gemäß P2.6.2.

**Werte beziehungsweise Felder:** DK-01; DK-02; DK-03; DK-04; DK-05; DK-06; DK-07; DK-08; DK-09; DK-10; DK-11; DK-12

**Fachliche Regeln:** DK-Klassen überlappen semantisch; technische physische Partition wird nicht vorgeschrieben; Weitergabe DK-06 ergänzt Ursprungsklasse.

**Abwesenheit, Kardinalität und Vergleich:** Ein Objekt kann mehreren DK-Klassen angehören; Klassen als duplikatfreie Menge anwenden, nicht als exklusive physische Partition.

**Prüfbeispiel:** Gespräch DK-08; pädagogische Erkenntnis DK-03.

### DT-64 — PruefergebnisDT

**Art:** Struktur\
**Betroffene D1-Entitäten:** DM-12, DM-14, DM-30, DM-32, DM-37, DM-40

**Zweck:** Explizit prüfbares Resultat mit Kontext und Grenzen.

**Werte beziehungsweise Felder:** `ergebnis`=gueltig/ungueltig/nicht_pruefbar; `grund`, `fehlerhinweise[]`, `belege[]`, `geprueft_am`.

**Fachliche Regeln:** Unbekanntheit nicht als positiv interpretieren; validierte Nutzerzuordnung ≠ offiziell bescheinigte Leistung.

**Abwesenheit, Kardinalität und Vergleich:** Genau ein kontextbezogener Prüfbefund mit Zeitpunkt; Hinweise und Belege 0..n. nicht_pruefbar ist kein positiver Befund; gueltig allein belegt keine amtliche Leistung oder Ausführungsfreigabe.

**Prüfbeispiel:** Ohne Skalenquelle keine Notenkonversion: nicht_pruefbar.


## D2.4 Zustandsübergänge und fachliche Zuständigkeiten

| Datentyp | Zulässige Transition bzw. Prüfbedingung | Nicht zulässig |
|---|---|---|
| DT-16 BerechtigungsstatusDT | angefragt → aktiv oder abgelehnt nach Prüfung; aktiv → deaktiviert/abgelaufen/widerrufen/fehlerhaft; deaktiviert → aktiv nur bei weiterhin gültiger Freigabe; unbekannt erlaubt keinen Zugriff | Automatische Reaktivierung widerrufener Berechtigung |
| DT-31 StudienstatusDT | geplant → aktiv → abgeschlossen; abgeschlossene, geprüfte Teile → archiviert nach bestätigtem Vorschlag | Automatische Archivierung offener Prüfungen/Projekte wegen Semesterdatum |
| DT-45 ErinnerungsstatusDT | vorlaeufig oder bestaetigt → zur_neubewertung bei veralteter/widersprüchlicher Grundlage; Neubewertung führt nur nach entsprechender Prüfung zu neuem Stand; Korrektur nach DT-46, autorisierte Löschung nach FE-13 bleibt möglich | Alten Inhalt nach Löschung durch Schattenkopie wiederherstellen |
| DT-48 VorschlagsstatusDT | offen → angenommen oder abgelehnt; offene Fassung mit ungültiger Grundlage → gegenstand_entfallen; historische finale Entscheidung unverändert; inhaltliche Bearbeitung → neue Fassung offen | Annahme einer alten Fassung für andere Zielstände |
| DT-49 VorschlagsaktionDT | `spaeter` belässt offen, `bearbeiten` erzeugt bei Änderung eine neue offene Fassung | `spaeter` als finale Ablehnung behandeln |
| DT-50 AusfuehrungsstatusDT | nach wirksamer Annahme: nicht_uebernommen → uebernahme_laeuft → uebernommen / teilweise_uebernommen / fehlgeschlagen / ergebnis_unklar; Wiederholung nur nach Wirkungsabgleich mit weiterhin gültiger Freigabe | Zweite Wirkung aus unklarem Ergebnis ohne Abgleich |
| DT-38 GespraechsstatusDT | aktiv ↔ archiviert; Löschanfrage und kontrollierte Löschung gesondert | Archivierung als tatsächliche Löschung ausgeben |
| DT-36 DokumentFassungDT | Neue Version zusätzlich zur bisherigen; aktiver Zeiger wechselt nur begründet und bewusst | Neue Version ohne Prüfung als stille Überschreibung |
| DT-54 SynchronisationsKonfliktDT | Bei konkurrierenden Ständen Grundlage und Rechte neu prüfen | Stilles Last-Write-Wins bei Entscheidungen, Freigaben oder Erinnerungen |

**Wichtig:** Diese Transitionsnotation ist fachlich; konkrete Zustandsautomaten und Ereignistypen für jede einzelne Entität werden in D1/D2 bei der Abnahme konsistent gehalten, technische Durchsetzung in N2/Architektur/Tests.

### D2.4.1 Zuordnung zu den kanonischen Zuständen aus F2.11.1

Die ASCII-Werte sind fachliche Normalisierungen der deutschen F2-Bezeichnungen, keine abweichenden Entscheidungen oder technischen Enums. D1 übernimmt dieselben Begriffe. Entscheidungsstand DT-48 und tatsächliche Wirkung DT-50 werden unabhängig beschrieben; ein neuer Fassungsinhalt ändert keine historische Entscheidung.

| Typ und D2-Wert | Maßgebliche F2-Bezeichnung / Bedeutung |
|---|---|
| DT-48 `offen` | Offen; auch nach „Später“ |
| DT-48 `angenommen` | Angenommen; genau die geprüfte konkrete Fassung |
| DT-48 `abgelehnt` | Abgelehnt; keine Wirkung dieser Fassung |
| DT-48 `gegenstand_entfallen` | Gegenstand entfallen; Ziel oder Grundlage nicht mehr gültig; historische Annahme/Ablehnung nicht rückwirkend ersetzen |
| DT-50 `nicht_uebernommen` | Nicht übernommen; keine bestätigte Wirkung ausgeführt |
| DT-50 `uebernahme_laeuft` | Übernahme läuft; keine zweite Übernahme aus anderer Ansicht |
| DT-50 `uebernommen` | Übernommen; Wirkung tatsächlich nachvollziehbar ausgeführt |
| DT-50 `teilweise_uebernommen` | Teilweise übernommen oder fehlgeschlagen — tatsächlich übernommene und noch offene Teilwirkungen unterscheidbar |
| DT-50 `fehlgeschlagen` | Teilweise übernommen oder fehlgeschlagen — Fehler mit nachweislich ausgebliebener Wirkung im jeweils betrachteten Umfang |
| DT-50 `ergebnis_unklar` | Ergebnis unklar; tatsächliche Wirkung vor Wiederholung klären |

Die feinere Unterscheidung der zwei Fehler-/Teilwirkungswerte präzisiert die gemeinsame F2-Anzeige; sie erlaubt weder Annahme ohne Zustimmung noch Erfolg ohne Wirknachweis. `nicht_uebernommen` kann auf der Vorschlagsansicht auch ohne DM-42 gelten; D1 verlangt keine Ausführungsentität für eine offene oder abgelehnte Fassung. Ein vorhandener DM-42-Beleg benötigt dagegen immer die wirksame Annahme.

## D2.5 Drei bestätigte neue Entscheidungen FE-15 bis FE-17

| Entscheidung | Fachlich bestätigte Bedeutung | Verbindliche D2-Auswirkung |
|---|---|---|
| **FE-15** | Originalnote und Originalnotenskala aufbewahren; eine Umrechnung ist nur gegebenenfalls, indikativ, getrennt und belegt zulässig | DT-26 `NotenOriginalDT`, DT-27 `NotenskalaDT`, DT-28 `NotenAequivalenzDT`, DT-29 `NotenAnsichtDT` und Herkunfts-/Beleggradtypen |
| **FE-16** | Ältere oder widersprochene pädagogische Einschätzungen zur Neubewertung markieren statt willkürlich zu löschen | DT-45 `ErinnerungsstatusDT`, DT-46 `ErinnerungsRevisionDT`, Unsicherheits-/Zeitstandtypen; keine automatische Erhöhung des Beherrschungsgrades |
| **FE-17** | KI-Statistiken je Tag, Woche, Monat und individuellem Zeitraum, soweit tatsächlich vorhandene Messwerte dies erlauben | DT-24 `AbrechnungsperiodeDT`, DT-25 `KIStatistikDT`, DT-22 `MessstandDT`, DT-21 `MetrikeinheitDT`; keine automatische Prompt-Speicherung |

### D2.5.1 Ergänzende ausdrücklich genannte Anforderung: Noten geschützt gruppieren

**Fachlicher Wunsch:** „Mein Profil“ soll die Einzelnoten nicht ungefragt zeigen. Der Nutzer öffnet erst den Bereich **Noten** und danach die gewählte **Hochschule bzw. Studienzugehörigkeit** (z. B. THM, andere Bildungseinrichtung), bevor einzelne Noten sichtbar werden. `DT-29 NotenAnsichtDT` stellt diese Gruppierung als Datenansicht mit Zugriff und Sichtbarkeit bereit. Mehrere Hochschulen und fremde Bewertungssysteme bleiben unterscheidbar; ihre Originalnoten werden nicht in einen pauschalen gemeinsamen Schnitt umgerechnet. Welche Klick- und Navigationsschritte die Geräteoberfläche zeigt, spezifiziert **B1**. Die Datenschutzeinstellungen, Gerätesperrhinweise und Vorschauen konkretisieren **N2** und B1.

**Akzeptanz:** Profilübersicht zeigt keine einzelne Note. Bereich „Noten“ geöffnet, aber keine Hochschule gewählt: keine automatisch offengelegten fremden Systeme. Erst Auswahl der berechtigten Studienzugehörigkeit zeigt zugehörige Originalnoten, Quellen und gegebenenfalls *getrennt markierte* indikative Äquivalenzen.

### D2.5.2 Bestätigter V1-Umfang: Öffentliche GitHub-Nachweise

FE-43 bestätigt die freiwillige offizielle GitHub-Kontoverbindung mit der bewussten Wahl einzelner oder aller eigenen öffentlichen Repositories im ausschließlichen Lesemodus. DM-19, DM-23 und DM-44 beschreiben den optionalen dauerhaften Bezug, DT-57 den Scope und DT-56 die vorsichtige nachweisbezogene Kompetenzsicht. Die technische Verfügbarkeit und aktuelle offizielle Rechte sind separat nachzuweisen.

Ein öffentliches GitHub-Profil muss nicht die Kontohoheit des Nutzers beweisen: Der Nutzer benennt es als sein Profil, Syllentra kennzeichnet den Bestätigungsstand. Programmiersprache, Repository-Beschreibung oder Beitragsstatistik allein sind **kein sicherer Nachweis persönlicher Beherrschung**. Tatsächliche eigene Beiträge, Teamarbeit und KI-generierte Inhalte werden nur soweit belegbar unterschieden; Kompetenzvorschläge bleiben ggf. vorläufig nach FE-11. Kein automatisches Schreiben in Repositories.

Die offiziell zulässigen Abrufverfahren und aktuellen Limits für öffentliche Repository-, Sprach- und Beitragsmetadaten sind bei Umsetzung anhand folgender Quellen zu überprüfen: [GitHub REST API – rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api), [GitHub REST – repositories, languages, contributors](https://docs.github.com/en/rest/repos/repos). Zugriffsfehler und Limits werden angezeigt, nicht umgangen. **Private Repositories, LinkedIn und weitere Plattformen sind durch diesen V1-Umfang nicht zugesagt**; eine spätere Erweiterung erfordert eine gesonderte fachliche Entscheidung und offiziell erlaubte Verfahren mit minimalen Berechtigungen. Der Verweis auf eine künftige Version ist keine Zusage.

**Quellenprüfstand:** Der Abruf der offiziellen GitHub-Dokumentation wurde am 15.10.2026 auch mit erweiterter Ausführungsberechtigung durch HTTP 403 blockiert. Deshalb bestätigt dieser Entwurf weder aktuelle API-Limits noch konkrete Zugangsrechte oder vollständige Beitragsdaten. Öffentliche Sichtbarkeit beweist weder Kontohoheit noch beliebige Weiterverwendungsrechte.

**Dokumentgrenze:** D1 enthält bisher keine ausdrückliche dauerhaft gespeicherte `ProfilLink`-Relation zwischen `DM-02` und `DM-23`. Bei der späteren Abnahme ist zu entscheiden, ob ein optionaler solcher Bezug in **D1** präzisiert wird; D2 erfindet weder eine 53. DM-Entität noch behauptet es diese Relation bereits als umgesetzt. Die Bedienung „GitHub-Profil hinzufügen / ausgewählte Repositories analysieren“ wird als konkrete F2-/B1-Ergänzung geprüft, ohne UC-42 umzunummerieren.

## D2.6 Domänenübergreifende Struktur- und Schutzregeln

### D2.6.1 Nachweise, Kontext, Herkunft

- `DT-12 DatenherkunftDT` und `DT-13 NachweisgradDT` sind **orthogonale Dimensionen**. Eine Nutzerbestätigung verändert allenfalls den Bestätigungsstand, niemals ohne Quelle den amtlichen Ursprung.
- Für geteilte Dokumente bleibt `DM-20` ein logisches Original. `DM-21` beschreibt jede Fassung, `DM-22` die Kontexte. Gleiche Dateinamen begründen weder identische Originale noch automatische Verschmelzung.
- Quellenverweise auf gelöschte oder nicht mehr zugängliche Originale tragen einen nicht-nachprüfbaren Status. Eine gespeicherte Zusammenfassung kann kein verschwundenes Original als Vollzitat ersetzen.
- Kontextbezüge aus Kurs/Projekt bei Gesprächsstart (FE-04) werden automatisch gesetzt, ohne eine KI-Klassifikation von Uploads (FE-02) vorab zu bestätigen.

### D2.6.2 Löschung, Datensparsamkeit, Geräte

- Daten können **archiviert** oder **gelöscht** sein; diese Werte sind nicht gleich. Bestätigte Erinnerungslöschung umfasst gewählte Revisionen und rekonstruierbare Kopien im fachlich beherrschten Umfang; unerreichbare externe Kopien bleiben kenntlich.
- KI-Statistiken enthalten nur zulässige Metadaten bzw. aggregierte Metriken; kein Prompt-Text, keine Nachrichtenkopie, keine versteckte Konversation anhand direkter Reidentifikatoren.
- Widerruf einer Gerätefreigabe sperrt zukünftige Nutzung, behauptet jedoch nicht ohne Beleg die Entfernung bereits lokal gespeicherter Daten.
- Wenn ein importierter Kalenderwert, ein Vorschlag oder ein Kostenlimit zwischen Prüfung und Verwendung geändert wird, ist die geprüfte Fassung erneut zu validieren. Keine automatische externe Kalenderänderung, auch nicht nach Zustimmung.

### D2.6.3 Gültigkeit, Validierung und Unbekannt

| Sachverhalt | Repräsentation | Verbotene Abkürzung |
|---|---|---|
| Nicht bekannte Note | `NotenOriginalDT` fehlt oder Wert ausdrücklich unbekannt | Automatisch `0`, `1,0` oder „nicht bestanden“ setzen |
| Keine Hochschulnotenskala verfügbar | `NotenskalaDT` unvollständig und dokumentiert | Deutsche Skala voraussetzen |
| Keine seriöse Äquivalenz | `NotenAequivalenzDT` nicht angeboten | Unbegründete numerische Umrechnung |
| KI-Modellzugang nur als Verbraucherabo | `KanalartDT=verbraucherabo`; Integrationsstatus gesondert | Direkten API-Zugang behaupten |
| Kostenangabe nicht verfügbar | `MessstandDT=unbekannt` | Kostenlosheit / Nullkosten behaupten |
| Alte Lernannahme | `ErinnerungsstatusDT=zur_neubewertung` | Als aktuelle sichere Beherrschung verwenden |
| Nutzer wählt „Später“ | `VorschlagsaktionDT=spaeter`, Stand offen | Annahme oder Ablehnung erfinden |
| Ausführung zeitlich unklar | `AusfuehrungsstatusDT=ergebnis_unklar` | Doppelte Ausführung ohne Prüfung |
| Privater Kalender nicht erreichbar | Verfügbarkeitsfenster unbekannt | Leere Zeiten als frei annehmen |
| GitHub-Profil verweist auf Teamrepo | `KompetenzBelegDT` mit Nachweisgrad/Urheberschaft offen | Alle Beiträge dem Nutzer zurechnen |

<a id="d27-rückverfolgbarkeit-der-52-entitäten"></a>

## D2.7 Ausgangsmatrix der ursprünglichen 52 Entitäten

Diese Tabelle bewahrt den ursprünglichen Bezugsumfang. Ergänzte Kennungen stehen im vollständigen Katalog und den jeweiligen Nachträgen; die [aktuelle Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md) ergänzt die 25 DEC-V1. Kein alter Eintrag entfällt.

Die Zuordnung zeigt für jede D1-Entität die in D2 ausdrücklich relevanten Typen, einschließlich mittelbarer Ansichten, Quellen- und Prüfbezüge. Sie behauptet keine neuen direkten Pflichtattribute oder Beziehungen: etwa gehören Notenwerte weiter zu DM-12, die Studienzugehörigkeit DM-04 liefert ihren Kontext. DT-57 bleibt bei allen Bezügen ein bestätigter GitHub-V1-Umfang (FE-43), dessen technische Verfügbarkeit separat nachzuweisen ist. DT-01 und DT-63 gelten zusätzlich als allgemeine Identitäts- und Datenklassentypen, wenn fachlich erforderlich.

| D1 | Fachliches Objekt | Relevante D2-Typen |
|---|---|---|
| DM-01 | Nutzerkonto | DT-01, DT-02, DT-63 |
| DM-02 | PersönlichesProfil | DT-01, DT-06, DT-07, DT-29, DT-58, DT-63 |
| DM-03 | Gerätefreigabe | DT-01, DT-02, DT-15, DT-16, DT-54, DT-63 |
| DM-04 | Studienzugehörigkeit | DT-01, DT-05, DT-12, DT-26, DT-27, DT-29, DT-31, DT-63 |
| DM-05 | Semester | DT-01, DT-03, DT-04, DT-05, DT-31, DT-62, DT-63 |
| DM-06 | Modul | DT-01, DT-06, DT-30, DT-31, DT-63 |
| DM-07 | Kurs | DT-01, DT-31, DT-63 |
| DM-08 | SemesterModulBezug | DT-01, DT-31, DT-63 |
| DM-09 | Themenknoten | DT-01, DT-06, DT-34, DT-63 |
| DM-10 | Lernziel | DT-01, DT-34, DT-63 |
| DM-11 | Prüfung | DT-01, DT-03, DT-04, DT-32, DT-52, DT-63 |
| DM-12 | Studienleistung | DT-01, DT-03, DT-12, DT-13, DT-26, DT-27, DT-28, DT-29, DT-30, DT-32, DT-58, DT-63, DT-64 |
| DM-13 | Kompetenz | DT-01, DT-06, DT-56, DT-63 |
| DM-14 | Kompetenzbeleg | DT-01, DT-12, DT-13, DT-56, DT-57, DT-58, DT-63, DT-64 |
| DM-15 | Studienentscheidung | DT-01, DT-14, DT-63 |
| DM-16 | Projekt | DT-01, DT-33, DT-62, DT-63 |
| DM-17 | ProjektModulBezug | DT-01, DT-35, DT-63 |
| DM-18 | Projektaufgabe | DT-01, DT-33, DT-63 |
| DM-19 | RepositoryBezug | DT-01, DT-10, DT-11, DT-56, DT-57, DT-63 |
| DM-20 | Dokument | DT-01, DT-08, DT-09, DT-12, DT-36, DT-55, DT-60, DT-62, DT-63 |
| DM-21 | Dokumentversion | DT-01, DT-02, DT-08, DT-09, DT-11, DT-12, DT-36, DT-37, DT-55, DT-60, DT-63 |
| DM-22 | DokumentArbeitsbereichBezug | DT-01, DT-34, DT-35, DT-60, DT-63 |
| DM-23 | Informationsquelle | DT-01, DT-10, DT-11, DT-56, DT-57, DT-63 |
| DM-24 | Inhaltsableitung | DT-01, DT-09, DT-14, DT-37, DT-63 |
| DM-25 | Unterhaltung | DT-01, DT-07, DT-38, DT-54, DT-60, DT-62, DT-63 |
| DM-26 | Nachricht | DT-01, DT-02, DT-07, DT-08, DT-09, DT-38, DT-39, DT-63 |
| DM-27 | GesprächskontextBezug | DT-01, DT-34, DT-35, DT-63 |
| DM-28 | Lerneinheit | DT-01, DT-40, DT-44, DT-63 |
| DM-29 | Übungsaufgabe | DT-01, DT-08, DT-40, DT-41, DT-63 |
| DM-30 | Lösungsversuch | DT-01, DT-14, DT-40, DT-41, DT-42, DT-63, DT-64 |
| DM-31 | Hilfenachweis | DT-01, DT-42, DT-43, DT-63 |
| DM-32 | Lernstand | DT-01, DT-13, DT-14, DT-41, DT-42, DT-44, DT-63, DT-64 |
| DM-33 | PädagogischerErinnerungseintrag | DT-01, DT-12, DT-13, DT-45, DT-46, DT-58, DT-60, DT-63 |
| DM-34 | Erinnerungsrevision | DT-01, DT-45, DT-46, DT-60, DT-63 |
| DM-35 | InternerStudientermin | DT-01, DT-02, DT-03, DT-04, DT-05, DT-52, DT-53, DT-63 |
| DM-36 | ExterneKalenderLesefreigabe | DT-01, DT-15, DT-16, DT-53, DT-63 |
| DM-37 | Importvorgang | DT-01, DT-12, DT-51, DT-63, DT-64 |
| DM-38 | Quellenbeobachtung | DT-01, DT-10, DT-14, DT-63 |
| DM-39 | Entscheidungsvorschlag | DT-01, DT-34, DT-35, DT-47, DT-48, DT-54, DT-55, DT-63 |
| DM-40 | Vorschlagsfassung | DT-01, DT-02, DT-47, DT-48, DT-51, DT-55, DT-63, DT-64 |
| DM-41 | Vorschlagsentscheidung | DT-01, DT-02, DT-48, DT-49, DT-54, DT-63 |
| DM-42 | Vorschlagsausführung | DT-01, DT-50, DT-63 |
| DM-43 | Integrationsangebot | DT-01, DT-17, DT-18, DT-63 |
| DM-44 | Integrationsberechtigung | DT-01, DT-15, DT-16, DT-17, DT-18, DT-63 |
| DM-45 | Modellangebot | DT-01, DT-17, DT-18, DT-19, DT-63 |
| DM-46 | Kosten- und Nutzungsfreigabe | DT-01, DT-05, DT-15, DT-19, DT-20, DT-21, DT-22, DT-23, DT-63 |
| DM-47 | KI-Nutzungsaggregat | DT-01, DT-02, DT-04, DT-05, DT-17, DT-20, DT-21, DT-22, DT-23, DT-24, DT-25, DT-58, DT-63 |
| DM-48 | Konfiguration | DT-01, DT-06, DT-07, DT-54, DT-55, DT-61, DT-63 |
| DM-49 | Konfigurationsfassung | DT-01, DT-55, DT-61, DT-63 |
| DM-50 | Datenkontrollvorgang | DT-01, DT-59, DT-60, DT-63 |
| DM-51 | ExterneDatenübermittlung | DT-01, DT-10, DT-59, DT-63 |
| DM-52 | Änderungshinweis | DT-01, DT-14, DT-63 |

<a id="d28-nachvollziehbarkeit-der-50-anwendungsfälle"></a>

## D2.8 Ausgangsmatrix der ursprünglichen 50 Anwendungsfälle

Diese Tabelle bewahrt den ursprünglichen Bezugsumfang. Ergänzte Kennungen stehen im vollständigen Katalog und den jeweiligen Nachträgen; die [aktuelle Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md) ergänzt die 25 DEC-V1. Kein alter Eintrag entfällt.

Die originalen UC-Titel aus F2 bleiben unverändert. Die D2-Zuordnung ist eine Wert-/Validierungssicht, keine Umnummerierung der Use Cases.

| Anwendungsfall | Schwerpunkt der D2-Verarbeitung |
|---|---|
| UC-01 — Geführten Einstieg nutzen oder überspringen | DT-06, DT-15, DT-58 |
| UC-02 — Mein Profil bearbeiten | DT-06, DT-07, DT-29, DT-58 |
| UC-03 — Studieninformationen und Nachweise aktualisieren | DT-12, DT-13, DT-26, DT-27, DT-30 |
| UC-04 — Persönlichen Arbeitsstand auf einem berechtigten Gerät fortsetzen | DT-02, DT-16, DT-54 |
| UC-05 — Gerätezugriff beenden oder entziehen | DT-16, DT-59 |
| UC-06 — Semester anlegen, wechseln und verwalten | DT-04, DT-31, DT-62 |
| UC-07 — Modul oder Kurs anlegen und zuordnen | DT-31, DT-34, DT-35 |
| UC-08 — Themen, Kapitel und Lernziele organisieren | DT-06, DT-34, DT-40 |
| UC-09 — Noten, ECTS und Prüfungsleistungen erfassen | DT-26, DT-27, DT-28, DT-30 |
| UC-10 — Semesterabschluss und Archivierung bestätigen | DT-31, DT-62, DT-48 |
| UC-11 — Lernmaterial als dauerhaftes Original aufnehmen | DT-08, DT-09, DT-36 |
| UC-12 — KI-Vorschlag zur Dokumentzuordnung entscheiden | DT-35, DT-48, DT-49 |
| UC-13 — Ein Dokument mit mehreren Arbeitsbereichen verknüpfen | DT-35, DT-36 |
| UC-14 — Dokumentenverknüpfung entfernen ohne Original zu löschen | DT-35, DT-60 |
| UC-15 — Material analysieren und Quellenlage nachvollziehen | DT-10, DT-11, DT-37 |
| UC-16 — Zulässige Audio- oder Videoinhalte aufbereiten | DT-08, DT-09, DT-37 |
| UC-17 — Allgemeine Unterhaltung beginnen | DT-38, DT-39 |
| UC-18 — Unterhaltung aus Kurs oder Projekt mit Kontext starten | DT-34, DT-35, DT-38 |
| UC-19 — Unterhaltung suchen und fortsetzen | DT-38, DT-39 |
| UC-20 — Zwischen Text und Sprache im Gespräch wechseln | DT-07, DT-08, DT-39 |
| UC-21 — Gespräch organisieren, zuordnen und archivieren | DT-35, DT-38, DT-62 |
| UC-22 — Unterhaltung mit abgestimmten Löschfolgen entfernen | DT-59, DT-60 |
| UC-23 — Interaktive Lerneinheit mit frei gewähltem Einstieg beginnen | DT-40, DT-41 |
| UC-24 — Adaptives Verständnis überprüfen | DT-41, DT-42, DT-43 |
| UC-25 — Fehler mit schrittweisen Hinweisen bearbeiten | DT-42, DT-43 |
| UC-26 — Vollständige Lösung und Lösungsweg anfordern | DT-42, DT-43 |
| UC-27 — Lernstrategie an Rückmeldung und Fortschritt anpassen | DT-40, DT-41, DT-44 |
| UC-28 — Prüfungsnahe Übung oder Simulation durchführen | DT-41, DT-42, DT-43 |
| UC-29 — Lernfortschritt und Wissensstand unterscheiden | DT-13, DT-44, DT-45 |
| UC-30 — Prüfungsvorbereitung für mehrere Prüfungen planen | DT-05, DT-40, DT-44 |
| UC-31 — Lernergebnis in Kompetenzportfolio überführen | DT-13, DT-56 |
| UC-32 — Internen Studienkalendereintrag manuell pflegen | DT-02, DT-04, DT-52 |
| UC-33 — Stundenplan importieren und bestätigen | DT-51, DT-48, DT-50 |
| UC-34 — Persönliche Kalender ausschließlich lesend berücksichtigen | DT-16, DT-53 |
| UC-35 — KI-Lernplanung in internen Kalender übernehmen | DT-05, DT-48, DT-50 |
| UC-36 — Änderung an autorisierter Studienquelle erkennen und anzeigen | DT-10, DT-14 |
| UC-37 — Prüfungsverschiebung prüfen und neu planen | DT-32, DT-48, DT-50 |
| UC-38 — Zentralen Eingang „Zu prüfen“ und kontextuelle Vorschläge verwalten | DT-47, DT-48, DT-49, DT-50, DT-54 |
| UC-39 — Projekt unabhängig oder modulbezogen anlegen | DT-31, DT-33, DT-34 |
| UC-40 — Projekt mit mehreren Modulen verknüpfen | DT-35 |
| UC-41 — Projektaufgaben und Ergebnisse verfolgen | DT-02, DT-33, DT-44 |
| UC-42 — Ausgewähltes Repository lesend analysieren | DT-10, DT-11, DT-56, DT-57 |
| UC-43 — Kompetenzen, Zertifikate und Nachweise pflegen | DT-13, DT-56, DT-55 |
| UC-44 — Studienentscheidung mit Quellen vorbereiten | DT-12, DT-13, DT-14 |
| UC-45 — Unterstützte Integration aus Katalog verbinden | DT-16, DT-17, DT-18 |
| UC-46 — KI-Dienst aufgabenbezogen auswählen und Kosten freigeben | DT-17, DT-18, DT-20, DT-22, DT-23 |
| UC-47 — Integrationsberechtigung deaktivieren oder widerrufen | DT-16, DT-59 |
| UC-48 — Administrationskonfiguration ändern und zurücksetzen | DT-16, DT-61, DT-55 |
| UC-49 — Persönliche Daten kontrolliert einsehen und exportieren | DT-59, DT-60 |
| UC-50 — Originale, persönliche Daten und Beziehungen kontrolliert löschen | DT-59, DT-60, DT-64 |

## D2.9 Rückverweise auf Geschäftsprozesse, Funktionen, Invarianten und Datenklassen

**F1-Geschäftsprozesse:** GP-01 Profil, GP-02 Semester, GP-03 Material, GP-04 Lernen, GP-05 Prüfungen, GP-06 Planung, GP-07 Änderungen, GP-08 Beratung, GP-09 Projekte, GP-10 Gespräche, GP-11 Kompetenzen, GP-12 Semesterabschluss, GP-13 Integrationen, GP-14 Verwaltung, GP-15 Datenkontrolle. Die D2-Geltungsregeln in D2.1–D2.8 gelten jeweils in den über F2 referenzierten Vorgängen.

| F3-Funktionen | Hier besonders relevante Datentypen |
|---|---|
| AF-01..AF-04 | DT-10..DT-16, DT-34..DT-37, DT-48 |
| AF-05..AF-08 | DT-35..DT-36, DT-48..DT-50, DT-55 |
| AF-09..AF-12 | DT-40..DT-46, DT-56 |
| AF-13..AF-16 | DT-02..DT-05, DT-34..DT-35, DT-52..DT-54 |
| AF-17..AF-20 | DT-15..DT-25, DT-57 |
| AF-21..AF-24 | DT-12..DT-14, DT-42..DT-46, DT-56 |
| AF-25..AF-27 | DT-15..DT-16, DT-54..DT-55, DT-59..DT-64 |

| D1-Invarianten | Validierungsaspekte in D2 |
|---|---|
| INV-01..INV-04 | Eigentum, freiwilliger Einstieg, getrennte Leistung, Archivzustände: DT-01, DT-12..DT-16, DT-26..DT-33, DT-62 |
| INV-05..INV-08 | Originale, Versionen, Mehrfachverknüpfung, bestätigte Klassifikation, Herkunft: DT-09..DT-14, DT-35..DT-37, DT-48 |
| INV-09..INV-12 | Unterhaltungen, Hilfen, Wissen und löschbare Erinnerung: DT-34, DT-38..DT-46, DT-60 |
| INV-13..INV-16 | Kalender, externe Lesegrenze, Quellstand, Vorschlagsfassungen: DT-02..DT-05, DT-48..DT-53 |
| INV-17..INV-20 | Entscheidungen, Ausführungen, Berechtigungen, Verbrauch: DT-15..DT-25, DT-48..DT-50 |
| INV-21..INV-25 | Konfiguration, Revisionen, Geräteabgleich, Löschung: DT-54..DT-64 |

`DK-01..DK-12` sind in `DT-63 DatenkategorieDT` vollständig aufgeführt. `CFG-01..CFG-17` bleiben die in P2 definierten Konfigurationsbereiche, deren tatsächlich unterstützte Schlüssel in B1/N2 bzw. einer versionierten Konfigurationsliste spezifiziert werden; D2 erfindet keine freie Programmiersprache als Konfigurationswert.

### D2.9.1 Einzelbezüge der bestätigten Entscheidungen FE-01 bis FE-17

| Entscheidung | Inhalt (bereits bestätigt) | Relevante Datentypen |
|---|---|---|
| FE-01 | Freiwillige Ersteinrichtung; fehlende optionale Profilfelder sperren keinen Einstieg | DT-06, DT-15, DT-58 |
| FE-02 | KI-Klassifizierung eines Dokuments erst nach Prüfung verbindlich | DT-35, DT-47, DT-48, DT-49 |
| FE-03 | Adaptiver Zeitpunkt, Häufigkeit und Schwierigkeit der Verständnisaufgaben | DT-40, DT-41, DT-42 |
| FE-04 | Kurs-/Projekt-Gespräch erhält automatisch einen sichtbaren korrigierbaren Bezug | DT-34, DT-35, DT-38 |
| FE-05 | Prüfungsterminänderung: Hinweis und neue Planung nur mit Bestätigung | DT-14, DT-32, DT-48, DT-50 |
| FE-06 | Semesterarchivierung nur für tatsächlich abgeschlossene Teile nach Freigabe | DT-31, DT-48, DT-62 |
| FE-07 | Gestufte Hinweise vor Komplettlösung; Lösung auf ausdrücklichen Wunsch | DT-42, DT-43 |
| FE-08 | Ein Vorschlag in zentraler Liste und im Kontext, gemeinsame Entscheidung | DT-47, DT-48, DT-49, DT-50 |
| FE-09 | Ein gemeinsames Dokumentoriginal, mehrere Beziehungen ohne Kopie | DT-35, DT-36 |
| FE-10 | Automatische Modellauswahl aus autorisierten Optionen, manuelle Wahl möglich | DT-17, DT-18, DT-19, DT-20 |
| FE-11 | Pädagogische Beobachtung automatisch als vorläufige Erinnerung | DT-13, DT-45, DT-46 |
| FE-12 | Ein logisches Dokument, Versionshistorie und aktiver Versionsbezug | DT-36, DT-55 |
| FE-13 | Erinnerungsänderungshistorie einsehbar, korrigierbar und löschbar | DT-45, DT-46, DT-60 |
| FE-14 | KI-Verbrauch aggregiert ohne automatisch gespeicherte Prompts oder Antworten | DT-21..DT-25 |
| FE-15 | Originalnote mit Quellskala; Äquivalenz nur getrennt und indikativ | DT-26, DT-27, DT-28, DT-29 |
| FE-16 | Veraltete/widersprüchliche Lernannahme zur Neubewertung ohne Pauschallöschung | DT-45, DT-46 |
| FE-17 | Nutzungsstatistiken täglich, wöchentlich, monatlich und benutzerdefiniert | DT-24, DT-25 |

### D2.9.2 Nachvollziehbarkeit aller bestehenden Integritätsregeln

Die nachfolgenden Prüfkerne sind Verweise auf D1 und keine Änderung der dort maßgeblichen Invarianten.

| D1-Regel | Referenzierter Prüfkern |
|---|---|
| INV-01 | Alle personenbezogenen Objekte gehören einem autorisierten Nutzerkontext; V1 unterstützt getrennte verifizierte Nutzerkonten; jedes persönliche Objekt besitzt genau einen Eigentümer; Datenzugriff wird trotz Gerätefreigabe und Administratorrolle geprüft. |
| INV-02 | Fehlende optionale Profilfelder sperren keine allgemeinen Lern- und Gesprächsfunktionen; fehlende für eine Spezialfunktion notwendige Eingaben betreffen nur diese Funktion. |
| INV-03 | Semester, Modul, Kurs, Prüfung und Studienleistung besitzen eigene Identität; erneute Prüfungsversuche überschreiben alte Ergebnisse nicht. |
| INV-04 | Nur tatsächlich als abgeschlossen geprüfte Elemente dürfen nach Nutzerbestätigung archiviert werden. Offene Prüfungen, Kurse und Projekte bleiben aktiv. |
| INV-05 | Ein bewusst gespeichertes logisches Dokument hat mindestens eine Version; die aktive Fassung muss zu diesem Dokument gehören. Eine neue Revision ersetzt die referenzierbare alte Version nicht stillschweigend. |
| INV-06 | Ein Original kann mehreren Arbeitsbereichen angehören. Das Entfernen genau eines Bezugs entfernt keine Version, kein Original und keinen anderen Bezug. |
| INV-07 | Eine KI-abgeleitete Dokumentklassifizierung bleibt Vorschlag. Sie wird nur für die geprüfte Fassung als endgültige Zuordnung übernommen. Bewusste direkte manuelle Zuordnung ist eine Nutzerhandlung. |
| INV-08 | Offizielle, manuell erfasste, importierte und KI-geschätzte Informationen behalten unterscheidbare Herkunft und Verlässlichkeitsgrad; Nutzerbestätigung ersetzt kein offizielles Zeugnis. |
| INV-09 | Aus Kurs/Projekt gestartete Gespräche erhalten sichtbar und korrigierbar Kontext, ohne redundanten Dialog. Allgemeine Gespräche dürfen ohne Kontext existieren. Nachrichtenverlauf ist nicht pädagogische Erinnerung. |
| INV-10 | Fragen und Schwierigkeitsgrad hängen von Ziel, Antworten und Schwierigkeiten ab. Hilfen und vollständige Lösungen bleiben als Einflussfaktoren getrennt von selbstständigem Erfolg. |
| INV-11 | Pädagogisch relevante Erkenntnisse können ohne vorherigen Einzeldialog mit Quellen-/Begründungsbezug als vorläufig gespeichert werden. Bestätigung und amtlicher Nachweis sind gesondert. |
| INV-12 | Erinnerungsänderungen sind nachvollziehbar und einsehbar, jedoch nach dem gewählten autorisierten Umfang löschbar; die alte Aussage darf nicht in einer unveränderlichen Schattenhistorie fortbestehen. |
| INV-13 | Aus externen Kalendern dürfen nur genehmigte verfügbarkeitsbezogene Informationen ausgewertet werden. Keine Syllentra-Operation erzeugt, ändert oder löscht externe private Ereignisse. |
| INV-14 | Bewusste manuelle Kalenderpflege kann direkt gespeichert werden. Imports und KI-Vorschläge verändern DM-35 erst nach ausdrücklicher Prüfung der anzuwendenden Vorschlagsfassung. |
| INV-15 | Zentrale Liste und fachlicher Kontext zeigen denselben logischen Vorschlag mit gemeinsamer Versions- und Entscheidungsidentität; die Anzeige selbst erzeugt keine Kopie. |
| INV-16 | Eine Annahme ist nicht der Nachweis erfolgreicher Ausführung. Übernahme wird idempotent bzw. mit nachprüfbarer Wirkung behandelt; Fehlversuche werden sichtbar, Ablehnung wird nicht ausgeführt. |
| INV-17 | Ein fehlgeschlagener Abruf ist keine Bestätigung des früheren Standes. Ändert sich die Quelle oder das Ziel, wird eine alte Vorschlagsfassung nicht unbesehen wirksam. |
| INV-18 | Anbietermodelle werden nur über offiziell zulässige Zugangskanäle und bestehende Freigaben ausgewählt. Kostenlose geeignete Modelle bevorzugen, aber keine Abonnements als API-Rechte, keine Umgehung von Limits. |
| INV-19 | Aggregierte Statistik speichert Anbieter, Modell, Periode und zulässige Kennzahlen. Prompts, Nachrichten, vollständige Antworten und unzulässige Identifikatoren werden nicht automatisch für Statistik gespeichert. |
| INV-20 | Unbekannte Gebühren und fehlende Rechte werden nicht als Freigabe behandelt. Verbrauchsschätzung und Anbieteranzeige sind keine Garantie exakter Kontingentstände. |
| INV-21 | Eine gespeicherte Konfigurationsfassung darf weder externe Schreibrechte noch neue ungenehmigte Kosten oder beliebige Codeausführung freischalten; Wiederherstellen validiert erneut. |
| INV-22 | Link entfernen, Original löschen, Version löschen, Gespräch löschen, Erinnerung löschen, Revisionshistorie löschen und Konto kontrollieren haben verschiedene deklarierte Wirkungen; geteilte Bezüge zuerst ausweisen. |
| INV-23 | Externe Daten und lokale Gerätekopien werden nur mit tatsächlichem Nachweis als gelöscht gemeldet; Sicherungen und Anbieterfristen werden offen ausgewiesen. |
| INV-24 | Parallel geänderte Arbeitsstände und final entschiedene Vorschlagsfassungen dürfen nicht unbemerkt überschrieben oder mehrfach angewandt werden. |
| INV-25 | Zugangsgeheimnisse sind keine normalen öffentlich konfigurierbaren Profilattribute. Dokumente, private Kalendereinträge, Modelleingaben und sensible Notizen sind nur zweckmäßig zugänglich. |

### D2.9.3 Verzeichnis der unveränderten Funktionen AF-01 bis AF-27

Die fachlichen Funktionen und ihre Beschreibung bleiben F3 vorbehalten.

| Funktion | Vorhandene Bezeichnung in F3 |
|---|---|
| AF-01 | Zulässigen Daten- und Berechtigungskontext bestimmen |
| AF-02 | Herkunft und Verlässlichkeit bewerten |
| AF-03 | Aufbereitetes Lernmaterial qualifizieren |
| AF-04 | Dokumentzuordnung vorschlagen |
| AF-05 | Gemeinsame Ressourcenbeziehungen bewerten |
| AF-06 | Vorschlagsfassung und Entscheidung abgleichen |
| AF-07 | Vorschläge kontextübergreifend konsolidieren |
| AF-08 | Studienstrukturen auf Konflikte prüfen |
| AF-09 | Adaptive Lernaufgabe auswählen |
| AF-10 | Lernantwort begründet einschätzen |
| AF-11 | Gestufte Hilfe bestimmen |
| AF-12 | Lernfortschritt und Wissen differenzieren |
| AF-13 | Studienplanung und Konflikte ableiten |
| AF-14 | Quellenänderung fachlich vergleichen |
| AF-15 | Abschluss- und Archivierungseignung prüfen |
| AF-16 | Gesprächskontext zweckgebunden bilden |
| AF-17 | KI-Zugangswege auf tatsächliche Berechtigung prüfen |
| AF-18 | Geeigneten KI-Dienst und geeignetes Modell auswählen |
| AF-19 | Kontingent und Ausgaben begrenzen |
| AF-20 | Anbieterfehler und Ersatzoption beurteilen |
| AF-21 | Vorläufige pädagogische Erinnerungen ableiten |
| AF-22 | Erinnerungsänderung und -korrektur auswerten |
| AF-23 | Kompetenznachweise gewichten |
| AF-24 | Studienoptionen nachvollziehbar vergleichen |
| AF-25 | Konfiguration regelkonform prüfen |
| AF-26 | Export- und Löschfolgen ermitteln |
| AF-27 | Geräteübergreifende Änderungen abgleichen |

### D2.9.4 Unterstützte Konfigurationsbereiche

Die bestehenden Kennungen `CFG-01`; `CFG-02`; `CFG-03`; `CFG-04`; `CFG-05`; `CFG-06`; `CFG-07`; `CFG-08`; `CFG-09`; `CFG-10`; `CFG-11`; `CFG-12`; `CFG-13`; `CFG-14`; `CFG-15`; `CFG-16`; `CFG-17` bleiben aus P2 unverändert. D2 legt keine zusätzlichen Konfigurationsrechte fest.


## D2.10 Fachliche Prüffälle für die Abnahme

| Nr. | Geprüftes Verhalten | Erwartetes Ergebnis |
|---|---|---|
| T-01 | Profil ohne Hochschule oder Noten geöffnet | Einstieg erlaubt; keine Note auf der Profilübersicht |
| T-02 | Nutzer öffnet „Noten“, danach „THM“ | Nur zugehörige DM-04-/DM-12-Leistungen werden sichtbar, weitere Institutionen bleiben getrennt |
| T-03 | Nutzer erfasst B+ aus anderem Notensystem | Original B+ bleibt erhalten, keine erzwungene deutsche Zahl |
| T-04 | Äquivalenzregeln fehlen | Keine scheinpräzise Umrechnung; indikative Bewertung fehlt ausdrücklich |
| T-05 | Modul hat 6 Soll-ECTS, Prüfung noch nicht bestanden | 6 ECTS Soll werden nicht als erworben angezeigt |
| T-06 | Alter Java-Lernhinweis widerspricht neuem Test | Auch zuvor bestätigte Erinnerung zur_neubewertung, kein Löschen nur wegen des Widerspruchs und keine sichere Weiterverwendung; ausdrückliche autorisierte Löschung bleibt möglich |
| T-07 | Nutzer korrigiert eine Erinnerung und entfernt die Historie | Aktueller Stand bleibt nach gewähltem Umfang; entfernte Altwerte nicht rekonstruierbar |
| T-08 | Nutzer löscht Erinnerung samt Revisionen | Keine Schattenkopie wird als aktuelle Lernpräferenz reimportiert |
| T-09 | Falsche Übung mit teilweiser Hilfe | Antwort bewertet samt Hilfennachweis, kein unabhängig beherrschtes Wissen |
| T-10 | Nutzer fordert vollständige Lösung sofort | Verfügbar ohne Zwang zu vorherigen Hinweisen; Nutzung wird vermerkt |
| T-11 | Tag-, Wochen-, Monats- oder benutzerdefinierte KI-Auswertung | Perioden mit Zeitzone, Einheiten, Messstand je Kennzahl und Datenvollständigkeit unterschieden; aus bloßer Monatssumme keine Tages- oder Teilperiodensumme erfinden; überlappende Ansichten nicht doppelt summieren |
| T-12 | Anbieter meldet kein Restquota | „Unbekannt“, nicht kostenlos und nicht 0 |
| T-13 | Verbrauchsaggregat gespeichert | Enthält keine Prompt- oder Antwort-Volltexte |
| T-14 | Nutzer wählt bestimmtes Modell | Modell muss trotzdem autorisiert, datenschutzgeeignet und innerhalb des Kostenrahmens sein |
| T-15 | ChatGPT-Plus-Account vorhanden, keine API-Berechtigung | Kein automatischer OpenAI-API-Zugang |
| T-16 | Öffentliches GitHub-Profil und ein Repo explizit ausgewählt | Nur lesende, limitierte Prüfung; Kompetenzen als nachvollziehbare Hinweise |
| T-17 | Repo einer Gruppe zeigt Python | Keine Behauptung, der Nutzer habe allen Python-Code selbst geschrieben |
| T-18 | GitHub gibt 403/429 wegen Rate Limit | Respektierte Pause/Fehlermeldung; kein Login-Scraping oder Limitumgehen |
| T-19 | Dokument v2 wird erstellt | v1 bleibt bis zur gezielten Löschung verfügbar; aktive eigene Fassung auch im Archiv erforderlich, kein ungefragter Wechsel. Löschen der letzten Version bei fortbestehendem Original wird zurückgewiesen |
| T-20 | Eine von drei Dokumentzuordnungen gelöscht | Original und zwei andere Zuordnungen bleiben erhalten |
| T-21 | Derselbe Vorschlag wird auf Gerät A angenommen und B abgelehnt | Höchstens eine finale Entscheidung zu dieser Fassung wirksam |
| T-22 | Gerät wiederholt unsichere Übernahme | Keine zweite Wirkung bis tatsächlicher Stand geklärt |
| T-23 | Import einer Prüfung schlägt neuen Kalendertermin vor | Interner Eintrag erst nach Bestätigung; privater Kalender nur lesend |
| T-24 | Semesterende mit Wiederholungsprüfung | Prüfung bleibt aktiv, keine automatische Archivierung |
| T-25 | Unbekannte Datum-Uhrzeit-Kombination | Nicht als eindeutiger Moment ausgegeben; Nachfrage oder Kennzeichnung |
| T-26 | Widerrufenes Gerät meldet sich erneut | Keine neue berechtigte Synchronisation; Entfernung älterer lokaler Kopien nicht behauptet |
| T-27 | Externe Löschung nicht bestätigt | Löschstatus teilweise / externe_reste_ungeklaert, keine irreführende Vollständigkeit |
| T-28 | Noten in Push-Benachrichtigungen oder Dashboardvorschau | Keine Einzelnoten. Konfiguration oder allgemeine Benachrichtigungsfreigabe ersetzen nicht die vorgeschriebene geschützte Detailansicht |

## D2.11 Grenzen und offene Detaillierung

1. **Notensysteme:** Keine pauschale numerische Umrechnungsformel. Hochschulregel und Quelle je System nachweisen, selbst wenn das UI mehrsprachig ist.
2. **Noten-UI:** Verschachtelte, geschützte Darstellung nach Nutzerwunsch ist eine fachliche Anforderung; B1 spezifiziert Navigation, Tastatur- und mobile Bedienung; N2 die Exposition sensibler Angaben.
3. **Externe Profile:** FE-43 bestätigt den öffentlichen GitHub-V1-Umfang mit bestehenden D1-Bezügen; dies behauptet keine implementierte Integration. Der optionale dauerhafte Profilbezug ist in D1 präzisiert; technische Kontonachweise bleiben zu prüfen. Private Repos, Organisationen und weitere Plattformen werden gesondert geplant; keine Rechte durch URL allein.
4. **Wertebereiche:** Konkrete Dauergrenzen, Speicherquoten, zulässige Dateiformate/-größen, tatsächliche Token-/Kostenmetriken und Ablaufregeln benötigen aktuelle Quellen und später N1/N2/S1.
5. **Bildungsbewertungen:** Schwierigkeitsskalen, Nachweisqualität und adaptive Bewertungsmaßstäbe sind fachlich zu evaluieren; bloßes Anwenden einer heuristischen Kategorie ist kein amtlicher Leistungsbeleg.
6. **Datenhaltung:** Verschlüsselung, physisches Schema, Sync-Protokoll, Sicherungen und revisionssichere Löschverfahren sind N2/Architektur; D2 schreibt keine technische Lösung vor.
7. **Abnahme:** FE-01..FE-17 sind bestätigt, aber sämtliche neu eingeführten D2-Typen, konkreten Enum-Ausprägungen und ergänzenden Abbildungsannahmen sind noch `Zur Prüfung` und dürfen von Codex nicht ohne Bericht als implementiert oder fachlich freigegeben bezeichnet werden.

### D2.11.1 Verweise und dokumentübergreifender Prüfstand

**Historischer Quellenstand des ursprünglichen D2-Entwurfs:** Die folgenden Versionszahlen und Bestandsumfänge dokumentieren die damalige Grundlage; aktuelle Fassungen und S2-Ergänzungen stehen im Index und im abschließenden Nachtrag.

- [P1 — Ziele und Rahmenbedingungen](P1-ziele-rahmenbedingungen.md), v0.5: freiwilliger Einstieg, Schutz persönlicher Daten, Kosten und Kalendergrenzen.
- [P2 — Architekturüberblick](P2-architekturueberblick.md), v0.6, insbesondere P2.5 und P2.6.2: CFG-01 bis CFG-17 und DK-01 bis DK-12.
- [F1 — Geschäftsprozesse](F1-geschaeftsprozesse.md), v0.2: GP-01 bis GP-15 und ursprüngliche FE-01 bis FE-06.
- [F2 — Anwendungsfälle](F2-anwendungsfaelle.md), v0.1, insbesondere F2.11.1: die 50 UC und Trennung von Entscheidung und Wirkung.
- [F3 — Anwendungsfunktionen](F3-anwendungsfunktionen.md), v0.1: AF-01 bis AF-27 und FE-10/FE-11.
- [D1 — Datenmodell](D1-datenmodell.md), v0.1, insbesondere D1.5 bis D1.7: 52 Entitätstypen, 25 Invarianten und FE-12 bis FE-14.
- [Spezifikationsindex](README.md): Zuständigkeiten und Statuskonventionen.
- Historische Quellen: [Projektvision](../PROJECT_VISION.md), Abschnitte „Project vision“ und „Design principles“; [Anforderungen](../REQUIREMENTS.md), Abschnitte 1 und 3; [Architekturentscheidungen](../ARCHITECTURE_DECISIONS.md), Abschnitt „Current position“; [Roadmap](../ROADMAP.md), Phasen 2 und 3. Sie begründen keine neue technische Festlegung in D2.

**Historischer Prüfstand 15.10.2026:** Der damalige D2-Auftrag änderte ältere Bausteine nicht. **Aktueller Abgleich 16.10.2026:** DM-12 besitzt jetzt den optionalen direkten DM-04-Studienzugehörigkeitsbezug; DM-19/DM-23/DM-44 präzisieren dauerhafte optionale GitHub-Bezüge. FE-43 ersetzt den damaligen Produktvorschlag. Neue technische Detailtypen bleiben zur Prüfung; kein Implementierungsnachweis.

### D2.11.2 Korrekturen gegenüber dem gelieferten Vollentwurf

| Befund | Präzisierung ohne Umnummerierung |
|---|---|
| Vergleich, Abwesenheit und Kardinalität teilweise nur allgemein | Jeder der 64 Typen hat eigene Hinweise; bekannte Werte, Unbekanntheit und Nichtverfügbarkeit bleiben getrennt. |
| AF-18 im Verzeichnis verkürzt; Typverwendungen nicht überall gleich nachgewiesen | Originaltitel aus F3 wiederhergestellt; Katalog, Definitionen und DM-Matrix auf dieselben unmittelbaren oder kontextuellen Verwendungen abgestimmt. |
| Zustandsnotation ohne ausdrückliche F2-Zuordnung | ASCII-Werte vollständig zugeordnet; Teilwirkung, Fehler und unklare Wirkung differenziert; keine zusätzliche finale Entscheidung durch „Später“. |
| Noten mit möglicher Anzeigeausnahme in einem Prüffall | Keine ungefragt sichtbaren Einzelnoten in Profil, Dashboard, Vorschau oder Benachrichtigungen; geschützte Institutionsauswahl verbindlich, Umrechnung getrennt und indikativ. |
| FE-16-Transition nur aus vorläufigem Stand beschrieben | Auch bestätigte überholte/widersprüchliche Einschätzungen zur Neubewertung; keine pauschale Löschung, keine Blockade autorisierter Löschung. |
| Ein globaler Messstand und Euro-Einheit zu eng | Messstand je Kennzahl, Geldwerte mit Währung und zeitbezogener Grundlage; keine erfundenen feinen Perioden aus gröberen Summen. |
| GitHub-Ausschnitt könnte als festgelegte Produktgrenze gelesen werden | Historischer V1-Vorschlag durch FE-43 ersetzt; bestätigter öffentlicher Scope bei weiterhin ausstehender technischer Rechteprüfung; keine zugesagten privaten Repositories, weitere Plattformen oder aktuellen API-Rechte. Quellenabruf blockiert, spätere offizielle Prüfung erforderlich. |

**Freigabestatus:** Zur Prüfung durch den Projektinhaber — D2 v0.7. Git-Commit und Push ersetzen keine gemeinsame fachliche Abnahme.


## D2.12 Ergänzende Datentypen für Konten und sichere Lebenszyklen

Die Entscheidungen FE-27 bis FE-89 ergänzen den Bestand. FE-56 war beim historischen Abgleich noch offen; seit der Eigentümerentscheidung aus Mission 19 vom 23.10.2026 sind Postfachlektüre, -synchronisation und -überwachung in V1 ausgeschlossen. Ausgehende OTP-/Sicherheitsmails, autorisierte Benachrichtigungen und manueller Import ausgewählter Inhalte bleiben möglich; eine spätere Integration ist unverbindlich. Die übrigen bestätigten Vorgaben bleiben erhalten. Die vollständige deutsche Entscheidungsmatrix und die zwölf Nachbarverträge stehen in [S1](S1-nachbarsysteme.md). Eine fachliche Entscheidung ist keine Aussage über implementierte Funktionen oder aktuell erteilte Anbieterrechte. Alle Bausteine bleiben **Zur Prüfung**. Historische Prüfstände, frühere FE-Teilmengen und alte Versionsbezüge bezeichnen ausschließlich ihre damalige Grundlage; maßgeblich ist der aktuelle Index mit [Änderungs- und Prüfnachweis](E3-pruefnachweis.md).

Die folgenden Wertbereiche sind fachliche Typen, keine ausgewählten Kryptoverfahren oder API-Payloads. Strukturfelder mit `_optional` dürfen fehlen; notwendige Rechte werden bei Abwesenheit nicht angenommen. Kennungen gehören zum jeweiligen Eigentumskontext.

### DT-65 — KontostatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-01.

**Werte beziehungsweise Felder:** `registriert_unbestaetigt; aktiv_verifiziert; freiwillig_pausiert; administrativ_gesperrt; loeschung_bestaetigt; bereinigung_laufend; geloescht`.

**Validität und Vergleich:** Keine Adminannahme zwischen Verifikation und allgemeiner Freigabe; Sperre und Pause bewahren Daten. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-66 — EMailAdressrolleDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-53.

**Werte beziehungsweise Felder:** `privat_primaer; privat_zusaetzlich; hochschule`.

**Validität und Vergleich:** Genau eine private verifizierte Primäradresse; Rolle gewährt kein Postfachrecht. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-67 — VerifikationszweckDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-54.

**Werte beziehungsweise Felder:** `registrierung; neue_adresse; neues_geraet; kontorecovery; administrative_mfa; sensible_aktion`.

**Validität und Vergleich:** Der Zweck allein bestimmt keine gemeinsame Frist aller Nachweisarten. OTP und temporäre Verifikations-/Recoveryanfragen bleiben befristet; der zusätzliche persönliche Einmal-Recoverycode nach R1 besitzt kein automatisches Sieben-Tage-Verfallsdatum und endet durch Verbrauch, Widerruf, kontrollierten Ersatz/Rotation oder Sicherheitsinvalidierung. Beide Nachweise sind getrennt zu prüfen; einmaliger Verbrauch bleibt verbindlich. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-68 — SitzungsstatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-55.

**Werte beziehungsweise Felder:** `aktiv; lokal_gesperrt; server_abgelaufen; abgemeldet; widerrufen`.

**Validität und Vergleich:** Lokaler Zustand kann mit Serverablauf zusammenfallen; diese Achsen werden getrennt gespeichert, nicht als technisch exklusive Gesamtzustände missverstanden. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-69 — AdministrationsrechtDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-56.

**Werte beziehungsweise Felder:** `branding; konfiguration; quota; feature_test; feature_release; kontosperre; super_admin_exklusiv`.

**Validität und Vergleich:** Versionierter unterstützter Rechtekatalog plus individuelle Zuweisung; sekundäre Rollen haben nie Administratorverwaltung oder Selbstbeförderung. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-70 — SupportumfangDT

**Art / Verwendung:** Struktur; DM-58.

**Werte beziehungsweise Felder:** `objektkennungen, zweck, beguenstigter, lesen, gesondertes_aenderungsrecht, beginn, ende, widerruf`.

**Validität und Vergleich:** Nicht leere eindeutige Ziele, genau ein Zweck, endliche Gültigkeit; Standard nur lesend. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-71 — QuotarahmenDT

**Art / Verwendung:** Struktur; DM-59.

**Werte beziehungsweise Felder:** `dimension, einheit, grundwert, kontoausnahme, verbrauch, warnschwelle`.

**Validität und Vergleich:** Nichtnegative konsistente Werte; Einheiten vergleichbar; konkrete Zahlen erst nach Entscheidung, fehlende Pflichtwerte nicht als unendlich deuten. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-72 — FeatureSichtbarkeitDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-60.

**Werte beziehungsweise Felder:** `verborgen; bald; ausgewaehlte_tester; oeffentlich; deaktiviert`.

**Validität und Vergleich:** Sichtbarkeit allein ist keine serverseitige Aktionsberechtigung; deaktiviert bewahrt Daten. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-73 — ReleaseStatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-61.

**Werte beziehungsweise Felder:** `entwurf; vorschau; intern_getestet; testerphase; geplant; verfuegbar; abgesagt; zurueckgenommen`.

**Validität und Vergleich:** Vorschau verändert aktive Fassung nicht; nur aktuelle zulässige Verfügbarkeit gestattet Ankündigung. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-74 — IntegrationslaufstatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-62.

**Werte beziehungsweise Felder:** `angefordert; laeuft; teilweise; erfolgreich; unterbrochen; fehler; wirkung_unbekannt; widerrufen`.

**Validität und Vergleich:** Unbekannter Ausgang ist kein belegter Fehler und keine Erlaubnis zum doppelten Aufruf. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-75 — SyncModusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-63.

**Werte beziehungsweise Felder:** `manuell; automatisch_opt_in`.

**Validität und Vergleich:** Automatik verlangt gültiges Opt-in, Intervall und aktuellen Scope; interner Geräteabgleich ist gesondert. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-76 — QuellrevisionDT

**Art / Verwendung:** Struktur; DM-21, DM-23, DM-38.

**Werte beziehungsweise Felder:** `quellkennung, externe_revision_optional, hash_optional, aenderungszeit_optional, abrufzeit, gewissheit`.

**Validität und Vergleich:** Fehlende Revision/Hash ist unbekannt und kein Gleichheitsbeweis; Dateiname reicht nicht. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-77 — SchutzstufeDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-64.

**Werte beziehungsweise Felder:** `persoenlich_standard; sensibel_geraeteseitig`.

**Validität und Vergleich:** Bei mehreren Quellen gilt mindestens deren höchster Schutz; explizite Herabstufung nachvollziehbar und rechtlich zulässig. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-78 — SchlüsselverfügbarkeitDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-65.

**Werte beziehungsweise Felder:** `geraet_berechtigt; schluessel_verfuegbar; wiederherstellung_noetig; entzogen; unbekannt`.

**Validität und Vergleich:** Als getrennte Merkmale von Berechtigung und Verfügbarkeit auswerten; Kontoverifikation erzeugt keinen Schlüssel. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-79 — VerarbeitungsumfangDT

**Art / Verwendung:** Struktur; DM-66.

**Werte beziehungsweise Felder:** `operation, ziel, zweck, dokumentrevisionen, notwendige_ausschnitte, gueltigkeit, widerruf`.

**Validität und Vergleich:** Eigene Cloud sieht temporär freigegebenen Klartext; kein Schlüsseltransfer, kein dauerhaftes Klartextduplikat und kein fingiertes Ende-zu-Ende-Versprechen für diese Operation. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-80 — PapierkorbstatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-67, DM-68.

**Werte beziehungsweise Felder:** `im_papierkorb; wiederhergestellt; endgueltige_bereinigung_laufend; endgueltig_bereinigt`.

**Validität und Vergleich:** Keine abgeschlossene Löschung vor tatsächlichem Erfolg; Sicherungsreste und Fristen gesondert. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-81 — SicherungsstatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-69.

**Werte beziehungsweise Felder:** `vorgesehen; laeuft; verfuegbar; unvollstaendig; abgelaufen; bereinigt`.

**Validität und Vergleich:** Nur vollständig belegte, zugängliche eigene Sicherung als verfügbar anbieten; EU und Verschlüsselung verpflichtend. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

**DEC-49-Nachweis im DM-69-Kontext (keine Erweiterung der obigen Zustandswerte):** Primär-/Sicherungsanbieterbezug, EU-Standort und geprüfte Unabhängigkeit mit Prüfzeit, Integrität und tatsächlichem Restorebeleg führen; unbekannt ist kein positiver Nachweis. Verschlüsselungs-/Schlüsselbezug ist geschützt, kein Schlüsselinhalt. Anbieterunabhängigkeit und erfolgreicher letzter Test sind getrennte Merkmale, keine pauschale Garantie zukünftiger Wiederherstellbarkeit.

### DT-82 — WiederherstellungsstatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-70.

**Werte beziehungsweise Felder:** `ausgewaehlt; differenzen_geprueft; bestaetigt; laeuft; teilweise; abgeschlossen; abgebrochen`.

**Validität und Vergleich:** Bestätigung gilt nur für geprüfte Fassung und Auswahl; Löschmarkierungen werden erneut vor Wirkung geprüft. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-83 — ArchivExtraktionsstatusDT

**Art / Verwendung:** Fachlicher Zustands-/Wertebereich; DM-71.

**Werte beziehungsweise Felder:** `ungeprueft; sicher_pruefbar; teilweise_zulaessig; abgewiesen; extrahiert`.

**Validität und Vergleich:** Nicht unterstützt, beschädigt, ausführbar, Pfadflucht und Limitüberschreitung getrennt begründen; keine Ausführung. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-84 — SprachpräferenzenDT

**Art / Verwendung:** Struktur; DM-02, DM-09, DM-25, DM-48.

**Werte beziehungsweise Felder:** `ui_sprache, ki_sprache, uebungssprache, audiosprache, kontext_override`.

**Validität und Vergleich:** UI V1 FR/DE/EN; vier Bereiche unabhängig, bewusster Kontextwert vor allgemeiner Präferenz; Originalterminologie bleibt. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### DT-85 — GeheimnisNachweisDT

**Art / Verwendung:** Struktur; DM-54, DM-65.

**Werte beziehungsweise Felder:** `geschuetzter_verweis, zweck, nachweisart, ausgabezeit, ablauf_optional, verbrauchsstatus, widerrufsstatus, ersetzungsstatus, sicherheitsinvalidierungsstatus`.

**Validität und Vergleich:** Opaker geschützter Nachweis, kein sichtbares Geheimnisfeld. `ablauf_optional` fehlt nur bei einer nach bestätigter Regel nicht automatisch ablaufenden Nachweisart wie dem persönlichen Einmal-Recoverycode nach R1. Für OTP und temporäre Recoveryanfragen ist eine eigene Ablaufgrenze obligatorisch; fehlender Pflichtablauf ist ungültig. Die persönliche Codegültigkeit endet durch Verbrauch, Widerruf, Ersatz/Rotation oder Sicherheitsinvalidierung; unbekannter Nachweisstatus erlaubt keine Nutzung. N2.2/SEC-03 und DM-54 sind maßgeblich. Keine Passwörter, OTP, Recoverycodes, Tokens oder privaten Schlüssel in Ausgabe/Repository/Logs; konkretes Schutzverfahren N2. Unbekannte Pflichtangaben führen zu „nicht prüfbar“ oder Sperre, nicht zu erfundenem Erfolg. Gleichheit benötigt passenden Eigentümer, Zweck und aktuelle Revision; Statusnamen allein erteilen keine Erlaubnis.

**Prüfbeispiel:** Ein Wert außerhalb des beschriebenen Bereichs wird sichtbar zurückgewiesen, ohne vorhandene gültige Daten zu überschreiben.

### Übernahme der ergänzten Integritätsregeln

INV-26 bis INV-31 aus [D1](D1-datenmodell.md) gelten unverändert auch für die neuen Datentypen. DT-57 wird im folgenden Änderungsvermerk auf FE-43 präzisiert: Scope `ausgewaehlte_oeffentliche_repositories` oder `alle_eigenen_oeffentlichen_repositories`, freiwilliger offizieller Kontobezug, V1 ausschließlich lesend; private Quellen und automatische Scoperweiterung sind ausgeschlossen.

## D2.13 Fachliche Typen für portable Pakete und Migrationszustände

[S2](S2-datenmigration.md) definiert Semantik; die folgenden fünf Typen füllen die Manifest-/Delta-/Lauflücke, ohne binäre Formate, Kryptoverfahren oder Parserbibliotheken zu wählen. Kontobeziehungen, Schutz DT-77, Schlüsselverfügbarkeit DT-78, Freigabe DT-79, Identität DT-01 und Quellrevision DT-76 gelten zusätzlich. Aktive Secrets und Sicherheitsprivilegien sind keine Pakettypen.

### DT-86 — ExportmanifestDT

**Art / Verwendung:** Fachliche Struktur für DM-72 und AF-36.

**Felder:** Paketkennung, Export-/Fachschemafassung, unterstütztes Formatprofil, Eigentumshinweis ohne Liveberechtigung, Erstellzeit, Stichtags-/Konsistenzbasis, gewählte Bereiche, 0..n Inhaltspositionen mit relativem Pfad/Typ/Größe/Integritätsmerkmal/Quellrevision/Schutz/Abhängigkeit, Ausschlüsse/Fehlstellen und Prüfergebnis.

**Validität/Vergleich:** Nur unterstützte Schemafassungen; Pfade innerhalb der erlaubten Paketgrenze. Keine ausführbaren Inhalte oder Geheimnisse als Schemafelder. Fehlender obligatorischer Integritäts-/Versionsnachweis sperrt den betroffenen Inhalt; Integrität beweist nicht Berechtigung. Leere Bestandsliste kann gültig sein, „vollständig“ nur relativ zum erklärten zulässigen Umfang und ohne unbenannte Fehlstellen.

**Prüfbeispiel:** Ein Paket mit `../`-Pfad oder Sessiontokenposition wird nicht als gültiger persönlicher Import freigegeben.

### DT-87 — MigrationszustandDT

**Art / Verwendung:** Fachlicher Zustandsbereich DM-73.

**Werte:** `entwurf`, `pruefung`, `vorschau_bereit`, `bestaetigung_ausstehend`, `ausfuehrung`, `erfolgreich`, `teilweise_erfolgreich`, `abgebrochen`, `pausiert`, `fehlgeschlagen`, `nicht_pruefbar`, `wirkung_unbekannt`.

**Regeln:** Erlaubter Übergang benötigt aktuelle Rechte und geprüfte Vergleichsgrundlage. Erfolgreich nur nach belegtem Abschluss der bestätigten zulässigen Auswahl; Teilwirkung nicht als vollständigen Erfolg darstellen. Bei unbekannter Wirkung vor Wiederholung abgleichen. Ein Abbruch nach Teilwirkung ist kein vollständiges Zurückrollen. Ablauf/Widerruf sperrt neue Wirkungen unabhängig vom angezeigten Status.

**Prüfbeispiel:** Nach Zeitüberschreitung bleibt `wirkung_unbekannt`, bis der tatsächliche Zielstand geklärt ist; kein blinder Neustart.

### DT-88 — MigrationsdeltaDT

**Art / Verwendung:** Versionierte Struktur für DM-73/DM-74 und DLG-65.

**Felder/Werte:** Auswahl-/Vorschaufassung, Quell-/Zielgrundlage, Prüfzeit, 0..n Objektunterschiede mit Klasse `neu`, `identisch`, `aenderbar`, `konflikt`, `ausgeschlossen`, `unsicher`, `fehlende_abhaengigkeit`; pro Unterschied erlaubte Strategie `behalten`, `quellinhalt_annehmen`, `ueberspringen`, `getrennte_kopie`, `manuell_zusammenfuehren`, notwendige Bestätigung, Grund und Schutz.

**Regeln:** Kopie nur für rechtmäßig kopierbaren Inhalt und niemals zur Umgehung endgültiger Löschung oder Rechte. Quellen-/Zielrevision und manuelle Sitzungs-/Evidenzbindung erhalten. Geänderte Vergleichsgrundlage macht die alte Entscheidung nicht zur Freigabe neuer Inhalte. Teilunterschiede unterliegen ihren jeweiligen Daten-/Notenschutzrechten.

**Prüfbeispiel:** Altes Lernprofil trifft jüngere belegte Leistung: jüngere Evidenz bleibt; Konflikt und Herkunft werden ausgewiesen.

### DT-89 — MigrationswirkungDT

**Art / Verwendung:** Fachliche Struktur für DM-74.

**Felder:** Wirkungseinheit, tatsächlicher Eigentümer, Quellidentität/-revision, Ziel-/Basisrevision, konkrete bestätigte Auswahl, Duplikatvergleich, Status `offen`/`angewandt`/`ausgelassen`/`gesperrt`/`fehlgeschlagen`/`wirkung_unbekannt`, Nachweiszeit, Fehler-/Reststatus.

**Regeln:** Gleiche fachliche Wirkung nach Wiederaufnahme nicht verdoppeln; Auftragskennung allein beweist keine Identität beliebiger anderer Inhalte. Unklarer Ausgang zuerst prüfen. Neuer Korrekturauftrag erhält eigenen Bezug und löscht keine zwischenzeitliche Evidenz. Fehlende Nachweise nicht als Erfolg interpretieren.

**Prüfbeispiel:** Erneuter Klick nach bereits angewandtem Teilimport gibt denselben tatsächlichen Ergebnisnachweis zurück statt einer zweiten Anlage.

### DT-90 — MigrationswegDT

**Art / Verwendung:** Enumeration für DM-73, BAT-24/BAT-25 und S2-Vertragswahl.

**Werte:** `EXP` persönlicher Export; `IMP` eigener Syllentra-Reimport; `ACA` unterstützter akademischer Import; `DEV` eigener Geräteabgleich; `BAK` interne Sicherung/Restore; `UPG` interner Versions-/Schemawechsel; `MOV` EU-Betriebs-/Speicherwechsel.

**Regeln:** Weg bestimmt nicht allein Recht oder aktuelle Freigabe. BAK unterscheidet persönlichen Restore und gesondert genehmigten Betriebsfall. UPG/MOV sind keine normalen Nutzerimporte. Unbekannter Weg gesperrt statt als allgemeiner Konnektor ausgeführt.

**Prüfbeispiel:** Ein Nutzerpaket mit behauptetem Weg MOV erhält dadurch keinen Zugriff auf eine betriebliche Mehrkontensicherung.

## D2.14 Typen für Lernreihenfolge, Hinweise und geltende Studienvorgaben

### DT-91 — LernreihenfolgeDT

**Art / Bezug:** Struktur für DM-75, AF-09/AF-13 und BAT-26.

**Felder:** Persönlicher Kontext und Revision, 0..n geordnete eigene Lernziel-/Themenbezüge, Wiederholungsgrundlage und beobachtete Wiederholungen `geplant`/`abgeschlossen`/`verpasst`/`unbekannt`, letzte geeignete Belegzeit, Evidenzqualität, Schwierigkeits-/Zeit-/Prüfungsnähegrundlage, ausdrücklicher Automatikzustand samt Revision.

**Regeln:** Vollständiges Lernziel-/Konzept-/Themen-/Kapitelmodell berücksichtigen; abgeschlossene Wiederholung benötigt tatsächlichen Nachweis, verpasst beweist keine Wissenslücke. Reihenfolge enthält keine implizite Terminbuchung. Fehlende Evidenz/Zeiten bleiben unbekannt; konkrete Wiederholungsformel und Intervallgewichte nicht festgelegt. Manuelle Fixierungen und bestätigte Termine nur Randbedingung, nicht durch Reihenfolgenwert veränderbar.

**Prüfbeispiel:** Unbekannter Wissensstand führt zu vorläufig begründeter Auswahl, nicht „0 % Wissen“ oder erzwungener Kalenderübernahme.

**Präzisierung DEC-V1-14/15/16:** Manuell, ausdrücklich aktivierte Automatik und hybrid sind fachliche Modi des bestehenden Reihenfolgeplans; Fixierungen, aktuelle Evidenz und Zeitgrundlage bleiben getrennt. Ein importierter Modus ist keine heutige Aktivierung, kein neuer Termin und keine festgelegte Intervallformel.

[Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### DT-92 — PädagogischePlanänderungDT

**Art / Bezug:** Struktur für DM-76.

**Felder:** Änderung, Planbasis-/Zielrevision, `manuell`/`automatisch`/`ruecknahme`, Automatik-/Belegrevision, verständlicher Grund, Zeit, tatsächlich angewandter oder gesperrter/unklarer Umfang, optionaler Bezug auf die zurückgenommene Änderung.

**Regeln:** Automatische Wirkung setzt aktuelles ausdrückliches Opt-in und passende Basis voraus. Rücknahme ist eine neue konfliktgeprüfte Planänderung; keine Rücksetzung jüngerer Lernnachweise, manueller Termine, Rechte oder Löschungen. Alte Änderung bleibt historisch ihrem tatsächlichen Ergebnis zugeordnet, bis kontrollierte Historienlöschung greift. Keine privaten Inhaltsvollkopien allein für Undo halten.

**Prüfbeispiel:** Parallel manuell geänderter Plan verhindert blindes Undo; aktuelle Auswahl/Korrektur nötig, neue Antworten bleiben erhalten.

### DT-93 — ErinnerungsregelDT

**Art / Bezug:** Struktur für DM-77, UC-65, BAT-06/07/08/19.

**Felder:** Geltungsbereich, ausdrücklich gesetzte/geerbte Merkmale, Aktivierung, relative Erinnerungspunkte mit Einheit `kalendertage_vorher` oder `stunden_vorher`, Kanalwahl, Benachrichtigungszone, Ruhezeitbeginn/-ende, Dringlichkeits-/Digestwahl, Zielgerätebezüge und Revision.

**Regeln:** Explizite Ereigniswerte vor Kategorie vor persönlichem Globalwert vor Standard; geerbte Punkte werden bei ausdrücklicher eigener Punkteliste ersetzt, nicht ungefragt vereinigt. Aus ist keine Abwesenheit. Relative Werte nichtnegative fachlich valide Werte; J−5/J−1 als Tagesstandards, Stundenpunkte brauchen bekannte Ereignisuhrzeit und Zone. Lokale Ruhezeit initial 22:00–08:00 über Mitternacht, konfigurierbar; DST/mehrdeutige Zeit klären statt willkürlich senden. Kein neuer globaler Versandzeitstandard. Dringlichkeit umgeht Ruhe-/Schutzgrenzen nicht automatisch. Nicht unterstützte Kanaloption bleibt inaktiv statt als Recht zu gelten.

**Prüfbeispiel:** Nur Ereignisdatum vorhanden: J−1 ist datumbezogen nutzbar, „2 Stunden vorher“ wird bis zur Uhrzeitklärung nicht wirksam. Unbestätigte neue Terminzeit ändert keinen gültigen Erinnerungspunkt.

### DT-94 — BenachrichtigungszustellungDT

**Art / Bezug:** Struktur für DM-78 und BAT-19, M8.

**Felder:** Logische Hinweis-/Erinnerungsabsicht, wirksame Ereignis-/Regelgrundlage, Ziel-/Kanalbezug, 0..n Versuche, Annahme-/Auslieferungs-/Lesenachweis je gesondertem Zeitpunkt oder `unbekannt`, Fehler-/Widerrufsstand.

**Regeln:** Wiederholungsversuch und reine Inhaltsrevision erzeugen keine neue fachliche Absicht. Unterschiedliche berechtigte Zielgeräte unterscheiden Zustellungen, nicht den zugrunde liegenden Hinweis. Providerannahme beweist weder Auslieferung noch Lesen; fehlender Nachweis bleibt unbekannt. Keine privaten Inhalte, OTP oder Tokens im Nachweis. In-App-Gelesenstatus ist getrennt von externer Zustellung und gehört zu DM-52.

**Prüfbeispiel:** Ein Retry nach unbekanntem Providerergebnis gleicht zunächst den tatsächlichen Stand ab; nach Widerruf oder Historienlöschung kein blindes Neuversenden.

### DT-95 — StudienvorgabenAbgleichDT

**Art / Bezug:** Struktur für DM-24 mit DM-04/DM-06/DM-11/DM-12 und AF-37/UC-66.

**Felder:** Quellen-/Dokumentrevision und konkrete Belegstelle, belegte Quellautorität, Geltungskontext Hochschule/Studiengang/Ordnung/Einschreibung/Kohorte/Inkrafttreten/Übergang, Extraktions-/Bestätigungsfassung, 0..n unterstützte Regelpositionen (Pflicht-/Wahlpflicht, ECTS, Voraussetzung, Prüfungsform/-versuchsbezug), passende Istnachweise und quellengebundener Vergleich.

**Werte/Validität:** Geltung `belegt_anwendbar`, `belegt_nicht_anwendbar` oder `ungeklaert`; Ergebnis pro Regel `belegt_erfuellt`, `abweichung_belegt`, `nachweis_fehlt` oder `nicht_pruefbar`. Unbekannt ist kein Gegenbeweis; fehlende Nachweise sind keine erfundene Fehlprüfung. Bestätigte Extraktion und persönlicher Geltungsnachweis sind getrennt, Nutzerbestätigung keine amtliche Anerkennung. Unvollständiger Regelumfang bleibt Teilvergleich. Kein Dateiname, Upload oder neueres Datum ersetzt Geltungs-/Autoritätsprüfung.

**Prüfbeispiel:** Neue Ordnung ohne bekannte Kohortenzuordnung bleibt ungeklärt; ältere belegbar gültige Übergangsfassung wird nicht still verdrängt. Einheiten/ECTS/Versuche nur nach dokumentierter Semantik abgleichen, keine doppelte Anrechnung erfinden.

## D2.15 FE-21 — Wiedergabestand getrennt von Präferenzen

DM-25/DM-26 referenzieren den zulässigen Antwort-/Fassungsbezug; DT-07 beschreibt die Ausgabesprache, DT-61 die unterstützten persistenten persönlichen Parameter. Der vorübergehende Wiedergabestand unterscheidet fachlich bereit, laufend, pausiert, beendet und nicht verfügbar/Fehler samt tatsächlicher Position oder unbekannt. Das sind weder DT-38-Gesprächsstatus noch neue DM-/DT-Kennungen oder technische API-Enums. Pause/Fortsetzung/Replay und Medienfehler dürfen Text und Gesprächskontext nicht verwerfen. Wiederanlauf muss heutige Inhalts-/Geräte-/Anbieterrechte erneut prüfen; kein garantierter Browser-Hintergrund- oder Offlinebetrieb. Audio-/Positionkopien erben Quellschutz und zulässige Lösch-/Temporärregeln; keine Speicherung von Mikrofoninhalt beim bloßen Hören.

**Abnahme:** Standard aus verhindert automatische neue Ausgabe, ausdrückliches Einschalten erlaubt nur aktuell zulässige Antworten; unbekannte Stimme bleibt unverfügbar. Mikrofonverweigerung sperrt eine tatsächlich verfügbare erlaubte TTS-Ausgabe nicht. Prüfbezüge: UC-20, DLG-26/DLG-50 und [FE-21-Abnahme](ENTSCHEIDUNGSMATRIX.md#4-fe-21--getrennte-ausgabevariante-und-abnahme).
