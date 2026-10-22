# Frontend-Prototyp — UI-/UX-Prüfbericht Mission 8

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung durch den Projektinhaber

## 1. Auftrag und tatsächlicher Umfang

Vollständiger Mission-8-Auftrag mit 13 Abschnitten, Ausgangscommit `2f526e4c3120353be9b9648af3956b89372acb90`, sauberer bestehender Spezifikationsbranch, lokal/Remote/PR-Ref identisch und PR #1 OPEN. Kein Frontend am Ausgang. [ADR-0007](../ARCHITECTURE_DECISIONS.md#adr-0007--lokale-frontendprobe-aus-mission-8) dokumentiert ausschließlich den erlaubten Versuch; TECH-O-03 und alle übrigen TECH-O bleiben offen.

[Ausführbarer Code und Anleitung](../../prototypes/frontend/README.md): React/Vite/TypeScript, fünf direkte Laufzeitbibliotheken, eigenes CSS mit semantischen Tokens und nativen Dialog-/Formularelementen. Keine zusätzliche UI-/Router-/Editor-/Kalenderplattform nötig. [Installierte Versionen und Lizenzprüfung](../../prototypes/frontend/LICENSES.md); gebündelte Laufzeitnotices, Lockfile, Installskripte deaktiviert. Keine Kosten, Cloud, Konten, Modelle, KI-API, Backend, Deployment oder neue MCPverbindung.

## 2. Erprobbarer Umfang

| Raum | Tatsächlich bedienbar | Grenze |
|---|---|---|
| Übersicht | Navigation, drei Modulkarten, Agenda und Sessiondialog | Nur fiktive Fortschritts-/Kalenderwerte |
| Kurse | Modulliste/-detail, Themen/Lernziel/Materialverweise, früheres Semester als Leerzustand | Keine echte Einschreibung, Noten oder Modulverwaltung |
| Bibliothek | Übersetzte lokale Suche, Kurs-/Formatfilter, leere Ergebnisse, Dialogvorschau | Keine Datei geladen/hochgeladen, kein PDF-/Audioreader |
| Lernbegleiter | Beispiele, Eingabe, feste lokale Antwort, Wartestatus/Stop, Beispielverlauf und Quellenplatzhalter | Keine echte KI oder Quellenanalyse, kein dauerhafter Chatverlauf |
| Notizen | Drei strukturierte Beispiele mit Themen, Erklärung und weiterführender Frage | Lesemodus, kein Editor/Versionsspeicher |
| Kalender | Wochennavigation, Artenkennzeichnung, validierte manuelle Sitzung im RAM | Keine externe Integration, Reminder, Speicherung oder Synchronisierung |
| Fortschritt | Ziele, fiktive Schätzung vs. fiktive manuelle Markierung, Herkunftsdialog | Keine Kompetenzmessung oder offizielle Leistung |
| Einstellungen | DE/FR/EN, Hell/Dunkel/System, lokale Präferenzspeicherung mit sicherem Rückfall | Nur zwei bekannte Präferenzwerte, keine Kontoeinstellungen |
| Administration / Fehlerroute | Eigenständige klare Nichtverfügbarkeitsgrenze, Rückweg bei unbekannter Route | Keine Authentisierung oder Rechteverwaltung simuliert |

## 3. Tatsächlich ausgeführte Prüfungen

Umgebung: Node 24.19.0, npm 11.9.0, vorhandenes Linux-Chromium 154.0.8037.57; Playwright 1.64.1, axe-core über @axe-core/playwright 4.14.0. Keine realen Mobilgeräte oder Safari-/Firefox-Läufe. Befehle aus `prototypes/frontend`, keine verkürzten Nulltestläufe.

| Befehl / Verfahren | Ergebnis | Aussagegrenze |
|---|---|---|
| `npm ci --ignore-scripts --cache /tmp/syllentra-npm` | Wiederholte saubere Installation aus Lockfile erfolgreich, zuletzt 149 Pakete installiert | Lock enthält zusätzlich nicht installierte optionale Plattformpakete; kein fremdes Installskript ausgeführt |
| `npm run typecheck`, im Build erneut | TypeScript strict ohne Fehler | Kein Backendvertrag oder fachlicher Vollständigkeitsbeweis |
| `npm run build` | Produktionsbundle erfolgreich | Optimierter lokaler Build, keine Produktion oder Bereitstellung |
| `npm run lint` | ESLint ohne Fehler | Keine vollständige Sicherheitsanalyse |
| `npm run format:check` | Prettier ohne Abweichungen | Nur Formatierung |
| `npm test` | **7 Tests bestanden** | Datum/Zeitzonengrenzen, ungültige Termine, vollständige Übersetzungs-/Variablenmengen, Präferenzen und Singular/Plural |
| `npm run test:e2e` | **9 Chromium-Szenarien bestanden** | Acht echte UIroutes, Details/History, Filter/Preview, Dialogfokus/Tabzyklus/Escape, Formfehler/RAMspeicherung, Chat/Stop/HTMLtext, Theme/Sprachen, mobile Navigation und gesperrter Storage |
| axe in E2E | **17 Analysen ohne gemeldeten Verstoß** | Acht Hauptseiten × zwei Themes, zusätzlich französische mobile Einstellungen; WCAGtags 2A/AA/2.1AA/2.2AA, kein vollständiger Konformitätsnachweis |
| Reflow-/Sprachprüfung | Alle acht Seiten bei 390 px in DE/FR/EN und bei 320 px zusätzlich ohne horizontalen Seitenüberlauf | Keine vollständige reale Geräte-/Zoommatrix |
| Systemtheme / lokaler Storage | OShell/-dunkel-Wechsel, explizite Wahl und Reload geprüft, nur Sprache/Theme gespeichert | Kein Produktcache oder geräteübergreifendes Sync |
| Laufzeitnetz / Konsole | Desktop-Hauptparcours ohne Seitenfehler und ohne Requests außerhalb des lokalen Ursprungs | Beobachteter Testumfang, keine allgemeine Netzwerksandboxgarantie; Abhängigkeitsinstallation benötigt Registryzugriff |
| Devserver-Smoke | Echter Vite-Devserver gestartet, Übersicht und Bibliothek im Browser gerendert, keine Seitenfehler | Zusätzliche lokale Entwicklungsprüfung, kein Deployment |
| `npm audit --json` | Keine bekannte gemeldete Schwachstelle, alle Schweregrade 0 | Datierter Advisorybefund, keine zukünftige Sicherheitsgarantie |

Reproduzierbare Belege in versionierten Tests; Rohberichte/Traces und Gesamtaufnahmen bleiben lokal ignoriert. Keine früheren T01–T09 dadurch als vollständig bestanden markieren: einzelne UIbeobachtungen ersetzen keine geplanten Auth-/RAG-/Medien-/Restore-/Lastproben.

## 4. Gefundene und korrigierte Probleme

Initial fehlende TypeScript-Deklaration für CSSimporte ergänzt. Die reale Dialogprüfung fand fehlenden Fokus-Rückweg; Auslöser wird jetzt explizit wieder fokussiert. Ergänzte Tastaturprüfung zeigte außerdem eine Lücke beim umlaufenden Tabfokus; der Dialog begrenzt Tab/Shift-Tab jetzt ausdrücklich auf sichtbare Bedienelemente, Escape bleibt verfügbar. Ein Testselektor wurde auf den konkreten Kalenderleerzustand präzisiert, weil Erfolg und Leerzustand gleichzeitig legitime Statusmeldungen sind. Singular-/Pluraltexte ergänzt. Endlauf vollständig bestanden; keine Fehlprüfung abgeschaltet.

## 5. Aufnahmen und visuelle Prüfung

18 lokale PNGs erzeugt: acht Desktopseiten in Hell/Dunkel (1440 × 1000 CSS-px, bei längerem Inhalt volle Seite) und mobile Übersicht in beiden Themes (390 × 844 CSS-px, volle Seite). Die Aufnahmen wurden visuell auf erkennbare Überläufe, abgeschnittene Texte, Farb-/Ausrichtungsfehler geprüft; in den geprüften Ansichten keine solchen Fehler festgestellt. Kleine Metadaten und Informationsdichte bleiben Gegenstand des Eigentümerreviews. Kein menschlicher Screenreader-/universeller Kontrastnachweis daraus ableiten.

Vier repräsentative, bereinigte Aufnahmen versioniert; vollständiger Satz über den E2E-Befehl erneut erzeugbar:

| Desktop | Mobil |
|---|---|
| [Übersicht hell](prototype-screenshots/dashboard-light.png) | [Übersicht hell](prototype-screenshots/mobile-light.png) |
| [Übersicht dunkel](prototype-screenshots/dashboard-dark.png) | [Übersicht dunkel](prototype-screenshots/mobile-dark.png) |

## 6. Einordnung aller 46 Release-Kontrollen

**Keine Produktfreigabe.** Die folgenden Gruppen bilden alle 46 unveränderten IDs ab. „Teilbeleg“ bedeutet nur beobachtetes Prototypelement, nicht Bestehen des vollständigen Profils. Fehlende Server-, Sicherheits- und Betriebsnachweise bleiben vor echter V1 verpflichtend. [Kanonische Profile](../quality/RELEASE_KONTROLLMATRIX.md).

| Kontroll-IDs | Anwendbarkeit jetzt / tatsächlicher Befund | Offen für V1 |
|---|---|---|
| REL-S01, REL-S02, REL-S07, REL-S15, REL-S18 | Teilbelege: keine Keys/.env, Diff-/Secretmustersuche, keine Chatlogs/Remoteaufrufe, Lock-/Lizenz-/Auditprüfung | Vollständiger Secret-/Build-/Betriebs-/Lieferkettennachweis |
| REL-S10, REL-S14, REL-S16 | Teilbelege: Formulargrenzen, Reacttextausgabe, übersetzte harmlose Fehler | Servervalidierung, sichere Backendfehler/Anti-Enumeration |
| REL-S03, REL-S04, REL-S05, REL-S06, REL-S09, REL-S19 | Nicht im lokalen UIumfang: keine Konten/Auth/DB/Serverrechte; kein Bestehen behauptet | Authentisierung, Isolation, Session/Recovery/Verifikation und Negativtests |
| REL-S08, REL-S11, REL-S12, REL-S13, REL-S17, REL-S20 | Keine Veröffentlichung, Uploads, Cross-Origin-API, Webhooks oder Backups; nur lokales HTTP ohne Secrets | HTTPS, Parser-/Upload-/Integrationsgrenzen und verschlüsselter unabhängiger Restore |
| REL-Q03, REL-Q04, REL-Q05, REL-Q06, REL-Q11, REL-Q16 | Teilbelege: keine bezahlten Pfade, Fehler/Leer-/Wartezustände, Präferenzen statt Inhaltsstorage | Tatsächliche Quoten/Fees, Dienstfehler-/Cache-/Rechte-/Löschwirksamkeit |
| REL-Q07, REL-Q08, REL-Q09 | Teilbelege: lokaler Stop, endliche Simulation, einmalige manuelle Sitzung im geprüften Ablauf | Keine API-/Job-/Serveridempotenz, Retry-/Wirkungsabgleich oder echte Timeouts belegt |
| REL-Q01, REL-Q02, REL-Q12, REL-Q13, REL-Q14, REL-Q15, REL-Q17, REL-Q18, REL-Q19, REL-Q20 | Kein API-/DB-/Produktionsbetrieb, große echte Bestände, Mehrnutzer oder Backup im Scope | Last, Parallelität, Indizes/Pagination, Übertragung, Monitoring, sichere Logs, unabhängige Recovery |
| REL-Q10 | Kein V1-Zahlungssystem genehmigt; nicht aktiviert | Nur nach neuer ausdrücklicher Fachentscheidung |
| REL-A01, REL-A05, REL-A07, REL-A18 | Keine Modelle, RAG, Tools, Parser oder pädagogische Bewertung; synthetische Texte keine Belege | Injection-/Tool-/SSRF-/Medien-/Güte-/Datenschutztests nach Funktion |
| REL-A13 | Teilbelege: scoped Commit, Lockintegritäten, keine Installskripte | Vertrauenswürdige produktive CI/CD und tatsächliche Artefakt-/Releasekette |
| REL-A16 | Teilbelege: 17 axeanalysen, Keyboard-/Fokus-/Reflow-/Sprachtests, Reduced-motion-Regel | Reale Assistenztechnik/Browser/Geräte, vollständiger bestätigter WCAGumfang |

## 7. Grenzen, Review und nächste sichere Tranche

Experimenteller Code erfüllt keine FE/UC allein durch ähnlich benannte Oberfläche. Keine Backendauthentisierung/-isolation, privaten Daten, Echt-KI, Uploads, dauerhaften Inhalte, Sync, PWAinstallation oder echte Administration implementiert. Native Datum-/Uhrzeitpicker können abhängig von Browser/OS eigene Lokalisierung verwenden. Desktop-/Mobile-Chromiumemulation ersetzt keine iPhone-/Android-/Safari-/Screenreaderprüfung. Dateigrößen/Buildzeiten sind keine bestätigten Performance-SLOs.

Vor nächster Implementierung Eigentümerreview der UI-/Lesedichte und Aufgabenpfade; Stack-/Auth-/Datenmodell-/Bootstrap-/Schlüsselentscheidungen separat. Erste sichere Backendtranche: verifizierter Zugang/Session/Entzug, Konto A/B, zentrale Rechte/Flags und strikt getrennte Administration mit synthetischen Daten und negativen Direktaufrufen, bevor Lerninhalte angebunden werden. Noch keine Umsetzung autorisiert; FE-56 offen, 14 TECH-O offen, 20 EUR nur Vergleichsrahmen ohne Ausgabe.

PR #1 enthält bereits vor Mission 8 65 geänderte Dateien und über 18.000 hinzugefügte Zeilen gegenüber main. Zusammen mit dem Prototyp ist eine getrennte Review von Dokumentation und Frontend sachlich ratsam. Keine automatische Branch-/PRaufteilung: bestehenden Auftrag befolgt, keine neue Branch/PR oder Zusammenführung. Bereinigtes Reviewpaket mit Anleitung, Tests und vier Bildern statt aller lokalen Traces/Artefakte.


## 8. Wiederverwendbare Cloud-Arbeitsumgebung

Die tatsächlich verwendeten Installations-/Prüfschritte und Startanweisungen wurden über das vorhandene Onboardingwerkzeug als `install_script` und `start_skill` im **Konfigurationsentwurf** gespeichert. Keine Secrets, neue Netzdestinationsliste oder Repositorymitgliedschaft verändert. Speichern führt nichts aus und veröffentlicht nichts; Prüfung/Speichern in den Umgebungseinstellungen und gegebenenfalls Veröffentlichung der Arbeitsumgebung sind eigenständige Nutzerschritte, kein Appdeployment. Frische Wiederherstellung der Umgebung nicht getestet. Im aktuellen Workspace sind Installation, Build, Tests und gerenderter Devserver belegt.
