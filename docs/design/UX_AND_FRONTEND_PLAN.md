# Lernräume, Responsive und Frontendprüfung

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Arbeitsräume und Aufgabenpfade

| Raum | Hauptaufgabe / Informationshierarchie | Kritischer Zustand / Grenze |
|---|---|---|
| Dashboard | Nächster erlaubter Lernschritt, anstehende Termine, letzter Arbeitsraum, Fortschritt mit Beleg | Leerer Erststart erklärt Modul/Projektanlage; keine erfundene Kompetenz aus Nutzungszeit |
| Module und Kurse | Semester → Modul → Thema; Ressourcen, Lernziele, Fristen und Gespräche | Frühere Semester bleiben erreichbar; Projekt darf unabhängig oder mehrfach zugeordnet sein |
| Dokumente | Quelle auswählen, Seite/Abschnitt prüfen, an Tutor/Notiz binden | Importvorschau, Fehler, Schutzklasse und temporärer Verarbeitungsstatus sichtbar |
| Tutor | Unterhaltung + Composer, optional Quellenpanel; Historie und Kontext erreichbar | Streaming, Abbruch, Offline, unzulässige externe Weitergabe, fehlende Belege klar unterscheiden |
| Notizen | Strukturierter Text, Formel, Quelle, Revision und manuell/KI/Bestätigung | Vorschlag vor Übernahme, Konfliktvergleich und Export; keine Quelländerung durch Editor-Undo |
| Übungen | Lernziel, Aufgabe, eigener Versuch, Feedback und nachvollziehbarer Kompetenzbeleg | Antwort nicht vorzeitig verraten, mehrdeutige Korrektur als unsicher markieren |
| Progression | Ziel → Belege → Kompetenzstand → nächster sinnvoller Schritt | Noten/ECTS von KI-Schätzung trennen; Korrektur und Herkunft auffindbar |
| Kalender | Interner Studienkalender + getrennte minimale externe Verfügbarkeit | Manuellspeichern direkt; Import-/KI-Übernahme bestätigen; externe Ereignisse nie verändern |
| Wissenskarte | Begriffe und Beziehungen mit Quellbezug, Graph und Listenalternative | Knotenrechte auch nach Filter/Entzug, kein ausschließlich visuelles Lernen voraussetzen |
| Einstellungen / Mein Profil | Akademische Daten, Avatar, Sprachen, Lernpräferenzen, Datenexport/Löschung und Integrationen | Bestätigt/manuell/geschätzt kennzeichnen, Secrets nie anzeigen; keine Pflicht zur Preisgabe irrelevanter Daten |
| Administration | Getrennter Accountbereich für freigegebene Konfiguration, Flags, Quoten, Preview/Rollback | Kein implizites Inhaltsleserecht; keine Selbstbeförderung, eigener klar erkennbarer Kontext |

Navigation: Desktop linke Bereichsleiste + eigener Kontextbereich; Hauptaufgabe mittig, Quellen/Details rechts optional. Tablet reduzierte Leiste/Drawer; Smartphone ein Hauptpanel, Quellen als eigener Rückweg. Vorschlag für maximal vier häufige mobile Ziele plus „Mehr“; konkrete Ziele vom Eigentümer prüfen und über erlaubte Konfiguration verwalten. Keine mobile Adminoberfläche als ungeschützte Abkürzung.

Beispielpfad: Modul → Dokument → Seite → belegte Tutorantwort → überprüfte strukturierte Notiz → Übung → Lernbeleg. Quellenrevision und Berechtigung bleiben an jeder Übergabe erhalten. Nach Ressourcenfehlern Eingabe/Entwurf schützen und erlaubten nächsten Schritt zeigen, niemals still einen externen Anbieter zuschalten.

## 2. Responsive und Zugänglichkeit

Breakpoints als Vorschlag nach Inhalt: unter 640 px einspaltig, 640–1023 px umschaltbare Nebenansicht, ab 1024 px optionale zwei/drei Panels. Nicht allein an Gerätenamen festmachen. Reflow bei 320 CSS-px und 400-%-Zoom prüfen; breite Tabellen/Diagramme bekommen gezielte Navigation statt horizontalem Seitenscroll. Touchzielvorschlag 44×44 CSS-px, Mindestanforderungen später gegen bestätigten WCAGrahmen prüfen. Fokus darf nicht unter Composer/Stickyheader verschwinden.

Logische Überschriften/Landmarks/Skiplink, Tastaturfolge, programmatische Labels, inline Feldfehler mit Zusammenfassung; Statusmeldungen dosiert über Live-Region. Keine nur farblichen Quellen-/Fortschrittszustände. Formeln mit verständlicher sprachlicher Alternative; PDFtextansicht/OCRqualität offen, ungetaggtes PDF wird nicht durch den Viewer barrierefrei. Audio/Video mit zugänglichen Steuerelementen und temporären Transkriptansichten unter Schutz-/Löschregeln; keine unbegrenzte Transkriptspeicherung für Accessibility behaupten. Löschfrist und erforderliche zugängliche Ersatzdarstellung fachlich abstimmen.

DE/FR/EN mit langen Übersetzungen, Plural, Datums-/Zahl-/Zeitzonenformat und Sprache der Seite testen. Theme folgt expliziter Nutzerwahl oder Systempräferenz, keine unlesbare kurze Zwischenfarbe. Daten aus anderen Konten dürfen auch beim Theme-/Sprachwechsel nie aus Cache auftauchen. Reduzierte Bewegung, Kontrast und Bedienhilfen haben Vorrang vor Branding.

## 3. Künftiger Prüfplan, nicht ausgeführt

| Prüfbereich | Werkzeug / Verfahren | Konkrete Sollfälle / Nachweis |
|---|---|---|
| Token und Komponenten | Vitest, Testing Library; optional Storybook | Alle Button-/Dialog-/Feldzustände, Fokus und erlaubte Themeänderung; Storybook ohne produktive Daten/Secrets |
| Kernnavigation und Rechte | Playwright in bestätigter Geräte-/Browsermatrix | Konto A/B, Direktlink auf verborgenes Feature, abgelaufene Sitzung, getrennte Adminoberfläche; Serverantwort zusätzlich negativ prüfen |
| Responsive / Themes | Playwright-Screenshots, menschlicher Vergleich | 320/390/768/1280 CSS-px als Testvorschlag, Hell/Dunkel, 200/400-%-Zoom, Textüberlauf und keine verdeckten Controls |
| Formulare und Fehler | Vitest + Playwright | Leere/ungültige Daten, langsames Netz, 401/403/409/429/5xx, Retry/Abbruch, Eingabenerhalt und sichere Fehlermeldung |
| Tutor und Quelle | Deterministische Fakeereignisse + später echter erlaubter Backendtest | Deltas, unvollständiges Streamende, veraltete/entzogene Quelle, Zitatseite, Moduswechsel Text/Audio, Tool ohne Autorisierung abweisen |
| Barrierefreiheit | axe-core plus manuell Tastatur/Screenreader | Dialog/Fokus/Fehler/Live-Region, Listenalternative Graph, Medien, echte iOS-/Androidbedienung; axe allein kein AA-Nachweis |
| Sprachen | Lokalisierte Testfixtures | DE/FR/EN, Plural/Datumszeitzone, lange Menüs, keine technischen Schlüsselnamen im UI |
| Performance | Lighthouse lokal + Browserprofil und echte Nutzermessung nach Freigabe | Kalte/warme Navigation, Bundle/Editor/PDF-Lazyload, Streaminteraktion, langsames Gerät; Zielwerte nach N1.10 vor Messung vereinbaren |
| Visuelle Regression | Gepinnter Browser/Fonts/Viewport, synthetische Daten | Stabiler Referenzstand, Änderungen menschlich prüfen; kein automatisches Akzeptieren neuer Screenshots |

Vitest für kleine deterministische Logik, Testing Library für beobachtbare Bedienung, Playwright für wenige kritische End-to-End-Flows. Storybook erst bei wiederkehrender Komponentenpflege, visuelle SaaSdienste nicht nötig. CIausbau separat autorisieren; keine Tests oder UI-Konformität in dieser Mission behaupten. Anknüpfung an T01/T03/T05/T06/T09 im [bestehenden Testplan](../architecture/BENCHMARKPLAN.md), NFR-01/02/08/13/18/19/20 und REL-A16. Keine konkurrierenden Produktabnahmekataloge erzeugen.
