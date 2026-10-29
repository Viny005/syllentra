# Syllentra AI — Design System

**Version:** 0.3 · **Stand:** 26.10.2026 · **Status:** Empfohlen / Zur Entscheidung

> **Geltung seit Mission 23:** Der bestätigte Rahmen aus [P2.5.6](../spec/P2-architekturueberblick.md#p256-verbindlicher-darstellungs--und-konfigurationsrahmen-aus-mission-23) und Abschnitt 7 hat Vorrang. Die nachfolgenden konkreten Farb-, Schrift- und Animationsvorschläge bleiben unfreigegebene historische Entwürfe, keine Markenentscheidung.

## 1. Gestaltungsziel und Entscheidungsgrenze

Ruhiger akademischer Arbeitsplatz: Inhalte und nachprüfbare Lernentwicklung vor dekorativen KI-Effekten. Eigenständiger Vorschlag mit tiefem Petrol, warmen neutralen Flächen und sparsamem Türkis; keine Übernahme einer fremden Produktidentität. Persönliche Nutzung erhält zuerst hohe Qualität; Kontoisolation, getrennte Administration und spätere Registrierung bleiben V1-Ziele. Ausgang der Mission 7: kein fertiges UI. Die begrenzte UIprobe aus Mission 8 steht im Nachtrag; keine freigegebene Marke oder nachgewiesene WCAG-Konformität.

Herkunft: Mission 7, P1/P2, B1, NFR-08/18/19/20 und FE-57/58 in [S1](../spec/S1-nachbarsysteme.md). Grundlagen und Lizenzbefunde: [Quellen](../development/SOURCES.md). Namen der Tokens sind konzeptionell, keine bereits existierenden CSS-Variablen.

## 2. Semantische Farbtoken

| Token | Hell | Dunkel | Zweck |
|---|---|---|---|
| `surface.canvas` | `#F7F8FA` | `#111827` | Seitenhintergrund |
| `surface.panel` | `#FFFFFF` | `#1F2937` | Dokumente, Dialoge, Karten |
| `surface.subtle` | `#EEF2F6` | `#273449` | Abgesetzte sekundäre Flächen |
| `text.primary` | `#172033` | `#F3F4F6` | Hauptinhalt |
| `text.secondary` | `#475569` | `#CBD5E1` | Beschreibungen, Metadaten |
| `action.primary` | `#115E59` | `#5EEAD4` | Hauptaktion und aktive Auswahl |
| `action.onPrimary` | `#FFFFFF` | `#111827` | Text auf Hauptaktion |
| `action.hover` | `#134E4A` | `#99F6E4` | Zeiger-/Tastaturzustand ohne Fokusverlust |
| `border.control` | `#64748B` | `#94A3B8` | Erkennbare interaktive Begrenzung |
| `focus.ring` | `#1D4ED8` | `#93C5FD` | Separater Fokus mit neutralem Abstand |
| `status.info` | `#1D4ED8` | `#93C5FD` | Information mit Symbol und Text |
| `status.success` | `#166534` | `#86EFAC` | Bestätigter Erfolg |
| `status.warning` | `#92400E` | `#FCD34D` | Prüfung nötig, kein bloßer Farbindikator |
| `status.danger` | `#B91C1C` | `#FCA5A5` | Fehler, kritische Handlung |

Statusfarben zunächst als Text/Symbol auf `surface.panel` verwenden, nicht beliebig als Hintergrund kombinieren. Sekundärflächen brauchen eigene Kontrastprüfung. Disabled-Zustände bleiben beschriftet; reduzierte Deckkraft ersetzt keine verständliche Begründung.

Synthetische sRGB-Kontrastberechnung erfolgt für diese Tokenpaare im Dokumentationscheck: primärer/sekundärer Text, Primäraktion, Fokusring und Statusfarben gegen die jeweils vorgesehene Fläche. Zielvorschlag: mindestens 4,5:1 für normalen Text, 3:1 für erforderliche Nichttextkonturen; tatsächliche gerenderte Zustände später messen. Markenänderung darf keinen unlesbaren Fokus oder Text veröffentlichen. Keine pauschale Konformitätsaussage aus Hexwerten.

## 3. Typografie und räumliche Ordnung

| Bereich | Vorschlag | Begründung |
|---|---|---|
| Schrift | Lokaler Systemfontstack: `system-ui`, `Segoe UI`, `sans-serif`; Code `ui-monospace`, `monospace` | Keine externe Fontabfrage; keine neuen Fontdateien oder pauschal frei weitergebbaren Systemschriftarten |
| Grundschrift | 16 px / Zeilenhöhe 1,6; längere Notizen 17–18 px / 1,65 | Lesbarkeit über lange Sitzungen; Zoom/Benutzereinstellung respektieren |
| Hierarchie | 12 Metadaten, 14 Nebenbedienung, 16 Basis, 20 Abschnitt, 26 Seitentitel, 34 Einstieg; relative Einheiten in Umsetzung | Keine übergroßen Überschriften im Arbeitsbereich |
| Lesebreite | 65–75 Zeichen; Inhalte nicht über gesamte Desktopbreite strecken | Lerntexte und Quellen leichter vergleichen |
| Abstände | Token `space.1..8`: 4, 8, 12, 16, 24, 32, 48, 64 px | Kleines konsistentes Raster, keine zufälligen Einzelwerte |
| Radien | 4 px Eingaben, 8 px Karten, 12 px große Dialoge; rund nur für Avatar/Status | Ruhiger wiedererkennbarer Charakter |
| Schatten | Hell: zurückhaltend `0 2px 8px` mit schwarzer 8-%-Deckkraft; dunkel: Kontur statt starkem Schatten | Hierarchie nicht nur durch Schatten vermitteln |
| Raster | 12 Spalten Desktop, 8 Tablet, 4 Smartphone, variable Gutter 16–32 px | Flexibles Aufgabenlayout statt starrem Geräteetikett |
| Dichte | Standard großzügig; kompakt für Tabellen als Nutzereinstellung | Kompakt darf Touchziele/Lesbarkeit nicht aufheben |

Logo zunächst eigene Wortmarke „Syllentra AI“ mit austauschbarem Platzhalter für ein später freizugebendes Symbol; kein fremdes Logo importiert. Icons aus einer geprüften Lucide-Auswahl, konsistente 20/24 px und Textlabel bei unklarer Bedeutung. Dekorative Icons vor Assistenztechnik verbergen; Iconbuttons brauchen zugänglichen Namen.

## 4. Komponenten und Interaktionszustände

Ein Primärbutton je Aufgabengruppe; Secondary-/Ghost-/Danger-Varianten. Einheitlich: Standard, Hover, Focus-visible, aktiv, disabled mit Grund, busy mit verständlichem Status, Erfolg und Fehler. Wiederholbares Absenden unterbinden, ohne Serveridempotenz zu ersetzen. Laden zeigt benannte Region und Abbruch soweit möglich; Skeletons ohne hektische Animation. Leere Listen erklären den nächsten erlaubten Schritt, Fehler bieten sichere Wiederholung und erhalten Eingaben.

Fokusvorschlag: 2-px-Ring mit 2-px-Abstand, in Scrollcontainern sichtbar; keine ausschließlich hoverbasierte Bedienung. Dialog fokussiert Titel/erste sinnvolle Eingabe, hält Fokus angemessen, Escape/Zurück schließen soweit sicher, Rückkehr zum Auslöser. Irreversible Löschung zeigt Ziel und Folgen; normale manuelle Speicherung kein zusätzlicher Bestätigungsdialog. Toast nur Ergänzung, niemals alleiniger Nachweis eines dauerhaften Fehlers.

Animationen 120–180 ms für Orientierung; `prefers-reduced-motion` respektieren, keine Pflichtanimation, blinkende Lernbelohnung oder Autoscroll gegen bewusstes Lesen. Streaming mit Pausieren/Stoppen, neue Inhalte nicht pro Token laut vorlesen. Quellen- und Berechtigungszustände bleiben auch bei Streaming stabil.

## 5. Personalisierung und Administration

FE-57/58 und CFG in P2 bleiben maßgeblich. Unterstützte Token, Texte, Logo, Navigation, Bereichsreihenfolge und Widgets sind validierte serverseitige Konfigurationsdaten mit Version, Entwurf, Vorschau und Rückweg unter aktuellen Rechten. Keine freie HTML-/JavaScript-/CSS-Ausführung aus Textfeldern, keine beliebige URL als Konnektor, kein selbst definierter Button als neue Backendfunktion. Logoformate/Größen, Farbpaarungen, Linkziele und erlaubte Komponenten prüfen. Keine Secrets oder privaten Kontodaten in öffentlichem Branding.

Nutzerpräferenzen für Sprache/Theme/Dichte sind vom globalen Markenentwurf getrennt. Konfiguration kann keine Pflichtwarnung, Tastaturbedienung, Datenschutzanzeige oder Serverberechtigung abschalten. Flags bestimmen verfügbare Funktionen, Menüeinträge allein keine Rechte. Adminvorschau nutzt eigene synthetische Daten, keine standardmäßige Einsicht in Lerninhalte. Rollback revalidiert heutige Schutzregeln und reaktiviert keine entzogenen Rechte.

## 6. Designabnahme vor Umsetzung

Eigentümer bestätigt Richtung, Lesedichte und vorgeschlagene Zielwerte. Danach Komponentenproben auf echten Smartphone-/Tablet-/Desktopkonfigurationen in beiden Themes und DE/FR/EN; Tastatur, Screenreader, Zoom und lange Texte. Tokenkontraste, Zustandsvollständigkeit, erlaubte Konfigurationsänderung und UI-/Servergrenzen nach [Frontendplan](UX_AND_FRONTEND_PLAN.md) prüfen. Am Mission-7-Ausgang war keine UI implementiert/getestet; der nachfolgende Mission-8-Nachtrag dokumentiert den begrenzten neuen Stand.


## Fortschreibung aus Mission 8

Der neue konkrete Eigentümerauftrag autorisiert eine lokale experimentelle UIprobe. Die früheren Nichtimplementierungs-/Nichtinstallationsaussagen dieses Mission-7-Studienstands sind historische Grenzen, keine Sperre des neueren Auftrags. [Code/Anleitung](../../prototypes/frontend/README.md) und [tatsächlicher UI-Prüfbericht](../design/PROTOTYPE_REVIEW.md) dokumentieren den begrenzten Fortschritt. Keine allgemeine Stack-/Bibliotheks-/Produktfreigabe; TECH-O-03 offen. Eigene CSS-Token und native Controls genügen für die Probe, daher keine Tailwind-/shadcn-/Richtext-/PDF-/Graph-/Kalenderinstallation. Fach- und Releaseziele bleiben vollständig bestehen, Backend-/Geräte-/Assistenztechnik-/Sicherheitsabnahmen offen.

## 7. Bestätigter fachlicher Rahmen aus Mission 23

**Quelle:** Eigentümerauftrag Mission 23 vom 26.10.2026; maßgeblich sind [P2.5.6](../spec/P2-architekturueberblick.md#p256-verbindlicher-darstellungs--und-konfigurationsrahmen-aus-mission-23) und [B1.14](../spec/B1-dialogspezifikation.md#b114-darstellung-konfiguration-und-quellennavigation-mission-23). Die Petrol-/Türkisfarben, Typografie- und Animationswerte oben bleiben historische Entwurfs-/Prototypvorschläge, keine endgültige Markenentscheidung. Bestätigt ist jetzt eine eigenständige hochwertige farbenfrohe Lernumgebung mit vielseitigen ausgewogenen Farbwelten, unterscheidbaren Lernbereichsakzenten, klarer Hierarchie und zugänglicher responsiver Bedienung. Eine generische Chat-/Kartenoberfläche genügt nicht; Semester, Module, Materialien, Aufgaben, Übungen und Fortschritt tragen die Orientierung.

Unterstützte Design-Tokens, helle/dunkle/Systemvarianten, persönliche erlaubte Paletten/Akzente und ausdrückliche Saisonwahl sind zentral kontrollierbar. Sicherheits-/Datenschutz-/Accessibility-Regeln gehen administrativer Richtlinie, freigegebenen Standards und persönlicher Auswahl vor. Getrennte Administration verwaltet erlaubte Themes, Standard/Zwangsdarstellung, Saisonzuordnung, Texte/Übersetzungen, Navigation, Widgets und Featurezustände mit Vorschau, Validierung, Veröffentlichung und revalidierter Rücknahme. Neue Funktionen entstehen nicht aus Token oder Textfeldern.

Logo, endgültige Palette, Schriften, Illustrationsstil, konkretes Token-/Komponentenschema und Saisonlogik bleiben **Zur Entscheidung**. Die alten Kontrast-/Animationswerte werden nicht als neue Freigabe ausgegeben. Keine neue Bibliothek, keine Assets oder UI implementiert; bestehende Prototypevidenz gilt ausschließlich für ihren damaligen Umfang. Die 16 AT-VIS-Sollfälle und manuelle Geräte-/Accessibility-/Viewerprüfungen sind erst künftig auszuführen. Die Architekturprinzipien aus Mission 21 bleiben unverändert; ältere TECH-O-Offen-Angaben dieses Dokuments sind historische Prüfstände.
