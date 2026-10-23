# UI-Bibliotheken — schlanke Auswahl

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Auswahlregel

Voraussetzung ist eine spätere React-/Stackfreigabe (TECH-O-03); im Mission-7-Vergleich keine Installation oder Abhängigkeit eingeführt; der konkrete Mission-8-Auftrag erlaubt die unten verlinkte begrenzte Probe. [Lizenzregister](../development/DEPENDENCY_SELECTION.md) enthält offizielle Repositories, untersuchte Revisionen, Bedingungen und offene Prüfungen. Bevorzugter Kern: Tailwind + ausgewählte shadcn-Komponenten + **eine** Primitivenfamilie + Lucide. Alternative normales CSS reduziert Buildabhängigkeiten. shadcn kopiert Quelltext: Herkunft/Lizenz und spätere Sicherheitsupdates bleiben eigene Verantwortung.

| Kandidat | Konkreter Bedarf / Nutzen | Alternative / Komplexität / Urteil |
|---|---|---|
| Tailwind CSS | Semantische Token in konsistente Utilities überführen | Normales CSS möglich; kein Zwang zu fremder Farbpalette; Kernkandidat |
| shadcn/ui | Anpassbare Buttons, Dialoge, Formulare, Navigation | Keine gesamte Registry ausführen; einzelne Quellen prüfen; Kernkandidat |
| Base UI / Radix UI / React Aria | Fokus, Dialoge, Popover und Tastaturmuster | Base UI zuerst zusammen mit aktueller assistant-ui-Basis vergleichen; Radix gute Alternative, React Aria bei komplexen zugänglichen Widgets. Nicht alle drei übernehmen; API-/Peerkompatibilität im Prototyp offen |
| Lucide React | Einheitliche Icons | Kleine Auswahl statt mehrerer Iconsets; ISC plus MIT-Featheranteile beachten |
| assistant-ui | Streaming, Message/Thread/Composer, Anhänge, History und Fehlerzustände | Eigener kleiner Chat ist Alternative. MIT-Core mit eigenem Runtimeadapter prüfen; kein Assistant Cloud für Historie/Telemetrie voraussetzen. Toolkarte autorisiert nichts; Diktat ist kein vollständiges ASR-/TTS-/Videoangebot |
| Tiptap Core | Strukturierte Notizen, Listen, Formeln und Quellenknoten | Text-/Markdowneditor einfacher. MIT-Core zuerst; Collaboration/Cloud/Content AI/Proerweiterungen nicht als gratis voraussetzen. Historie/Revision/Provenienz/Export im eigenen Fachmodell, nicht nur Editor-Undo |
| PDF.js | Seiten, Textsuche, Quellnavigation und mobile Zoom-/Textansicht | Browserviewer allein bietet nicht alle Quellen-/Rechtefunktionen. Apache-2.0, Worker/CSP/aktive Inhalte prüfen; PDFtagging und OCR bleiben eigene Grenzen |
| React Flow | Konzeptknoten, Beziehungen, Zoom und Navigation | Zunächst zugängliche Begriffs-/Beziehungsliste; Graph später bei belegtem Nutzen. MIT-Core, Proangebot getrennt; Graph allein nicht zugänglich |
| FullCalendar Standard | Tag/Woche/Monat für interne Kurse, Prüfungen, Revisionen und Hinweise | Kleine Terminliste zuerst. Standard MIT, Premiumressourcen/-Scheduler nicht enthalten. Externe Kalender strikt lesend; Drag/Resize darf nie extern schreiben |
| TanStack Query | Asynchrone Serverzustände, Invalidierung und Retrykontrolle | Einfacher Fetch für kleine Probe. Konto-/Schutz-/Konfigurationsrevision im Cachekey, Cache bei Logout/Entzug bereinigen; keine sensiblen Offlinekopien aus Bequemlichkeit |
| TanStack Table / Virtual | Große Modullisten und kontrollierte Tabellenvirtualisierung | Native Tabelle/Pagination zuerst; nur bei gemessener Last hinzufügen; virtuelle Elemente brauchen Screenreader-/Fokustests |
| React Hook Form / Zod | Verständliche Formulare und Schemaprüfung | Kleine native Formulare möglich. Clientvalidierung ersetzt Serverprüfung nicht; APIvertrag nicht getrennt duplizieren |
| react-i18next | DE/FR/EN, Pluralformen und Sprachwechsel | Sprachschlüssel und fachliche Terminologie, Intl für lokale Datums-/Zahlformate. Keine privaten Lerntexte automatisch zur Übersetzung senden |
| KaTeX / Mermaid | Formeln bzw. erklärende Diagramme | Textalternative immer; Makros, Größe/Tiefe und sichere Optionen begrenzen, HTML/Linkziele filtern. Keine Ausführung fremder Diagrammanweisungen |
| Recharts / Visx | Später zugängliche Progressionsdarstellung | Zunächst Werte/Tabelle; Recharts einfacher, Visx flexibler und aufwendiger. Kein zweites Chartpaket parallel |
| Motion / dnd-kit | Gezielte Bewegung bzw. Umordnung mit Tastaturalternative | CSS/normale Up-/Downbuttons zuerst; kein Pflichtdragging oder Pflichtanimation |
| Sonner | Nicht blockierende ergänzende Rückmeldung | Bestehende Live-Region reicht zunächst; Fehler/Entscheidungen dauerhaft an Aufgabe anzeigen |
| Native Audio-/Videoelemente | Zugängliche Mediensteuerung ohne neue Bibliothek | Tastatur, Beschriftung, Rate, Lautstärke und Quellzeit prüfen; keine automatische Wiedergabe. Fremde Voice-/Analyticsdienste standardmäßig aus |

## 2. Tutorvertrag vor Komfort

Server liefert kanonische Conversation-/Message-IDs, Quellrevisionen und begrenzte Ereignisse für Start, Textdelta, Zitat, Fehler, Abbruch und Ende; Protokoll erst mit Backend auswählen. Partielle Antwort als unvollständig markieren. Text-/Audiomodus referenzieren dieselbe Unterhaltung, aber rohe temporäre Transkripte sind kein dauerhaftes Chatarchiv. Anhänge vor Verarbeitung prüfen; Quelle vor Anzeige erneut autorisieren. Umbenennen, Suche, Ordnen, Projekt-/Modulzuordnung, Archiv und bestätigte Löschung nach F2/B1, kein Browser-only-Verlauf.

Toolaktionen sind Vorschläge mit Ziel, Datenumfang und Kostenstatus. Bestätigung gilt für konkrete Operation/Fassung, nicht für unbegrenzte spätere Ausführung. Server prüft Rechte/Flags/Einwilligung unmittelbar vor Wirkung. Retry erzeugt keine doppelte Kalenderänderung oder Ausgabe. Stopp beendet auch weitere Toolwirkungen soweit noch kontrollierbar; unbekannten externen Ausgang zuerst abgleichen.

## 3. Rückbau und Versionspflege

Jede Fremdbibliothek hinter kleiner eigener Komponentenschnittstelle; fachliche Daten nicht in proprietärem Editor-/Cloudformat als einzige Kopie speichern. Nur benötigte Module lazy laden. Bei Auswahl exakte Pakete/Peerabhängigkeiten/Transitive/Advisories/Support und Lizenzbeilagen erneut prüfen und locken. Aktuelle Quellrevision ist kein garantierter stabiler Paketstand. Kein CLIgenerator oder Registrycode wurde ausgeführt.


## Fortschreibung aus Mission 8

Der neue konkrete Eigentümerauftrag autorisiert eine lokale experimentelle UIprobe. Die früheren Nichtimplementierungs-/Nichtinstallationsaussagen dieses Mission-7-Studienstands sind historische Grenzen, keine Sperre des neueren Auftrags. [Code/Anleitung](../../prototypes/frontend/README.md) und [tatsächlicher UI-Prüfbericht](../design/PROTOTYPE_REVIEW.md) dokumentieren den begrenzten Fortschritt. Keine allgemeine Stack-/Bibliotheks-/Produktfreigabe; TECH-O-03 offen. Eigene CSS-Token und native Controls genügen für die Probe, daher keine Tailwind-/shadcn-/Richtext-/PDF-/Graph-/Kalenderinstallation. Fach- und Releaseziele bleiben vollständig bestehen, Backend-/Geräte-/Assistenztechnik-/Sicherheitsabnahmen offen.
