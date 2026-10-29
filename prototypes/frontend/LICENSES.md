# Lizenzen und Abhängigkeitsprüfung — Frontend-Prototyp

**Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung

Die Installationsfreigabe stammt aus Mission 8, nicht aus der früheren Vergleichsstudie. Fünf direkte Laufzeitbibliotheken; übrige direkte Pakete dienen Build, Typprüfung, Lint, Formatierung und Tests. Keine Premium-/Cloud-/KIanbieterpakete. Registry-Metadaten, Engines, Peerabhängigkeiten und tatsächlich gelieferte Lizenzdateien geprüft; Bezug ausschließlich `registry.npmjs.org`, exakte direkte Versionen und Integritäten im Lockfile. TypeScript 6.0.3 statt der neuesten 7er-Version, weil typescript-eslint 8.72.0 laut Peerbereich TypeScript <6.1 verlangt. Node 24.19.0 verwendet; Node 24.x als reproduzierbare Laufzeit vorgesehen.

| Paket                  | Version | Lizenzbefund am installierten Paket | Rolle                          |
| ---------------------- | ------- | ----------------------------------- | ------------------------------ |
| `i18next`              | 26.5.5  | MIT                                 | Browserlaufzeit                |
| `lucide-react`         | 1.61.0  | ISC + MIT-Anteile laut LICENSE      | Browserlaufzeit                |
| `react`                | 19.3.1  | MIT                                 | Browserlaufzeit                |
| `react-dom`            | 19.3.1  | MIT                                 | Browserlaufzeit                |
| `react-i18next`        | 17.1.2  | MIT                                 | Browserlaufzeit                |
| `@axe-core/playwright` | 4.14.0  | MPL-2.0                             | Nur Entwicklungs-/Testwerkzeug |
| `@eslint/js`           | 10.0.1  | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `@playwright/test`     | 1.64.1  | Apache-2.0                          | Nur Entwicklungs-/Testwerkzeug |
| `@types/react`         | 19.3.0  | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `@types/react-dom`     | 19.3.0  | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `@vitejs/plugin-react` | 6.1.2   | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `eslint`               | 10.13.0 | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `globals`              | 17.13.0 | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `prettier`             | 3.9.10  | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `typescript`           | 6.0.3   | Apache-2.0                          | Nur Entwicklungs-/Testwerkzeug |
| `typescript-eslint`    | 8.72.0  | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `vite`                 | 8.3.5   | MIT                                 | Nur Entwicklungs-/Testwerkzeug |
| `vitest`               | 5.0.5   | MIT                                 | Nur Entwicklungs-/Testwerkzeug |

## Transitive Abhängigkeiten und Installationsgrenzen

Das Lockfile erfasst zusätzlich transitive und optionale plattformspezifische Pakete. Alle aufgelösten Pakete enthalten Lizenzmetadaten; vorkommend: MIT, ISC, Apache-2.0, BSD-2-Clause, BSD-3-Clause, BlueOak-1.0.0 und MPL-2.0. Eine deklarierte Metadatenlizenz ist keine vollständige juristische Prüfung jeder Quelldatei. MPL-Anteile betreffen insbesondere Test-/Transformationswerkzeuge; bei Weitergabe geänderter gedeckter Dateien deren Pflichten beachten. Keine Modifikation/Übernahme solcher Drittquellen. Engine-/Modell-/Datensatzrechte sind hier nicht betroffen, weil keine Modelle oder Daten geladen werden.

`npm audit --json` im tatsächlichen Lauf ohne bekannte gemeldete Schwachstelle; das ist keine Sicherheitsgarantie oder vollständige Lieferkettenprüfung. Registryadvisories benötigen Netzwerk und sehen Paketmetadaten, keine Lerninhalte. `npm ci --ignore-scripts` ist durch lokale `.npmrc` zusätzlich abgesichert. Das im Lockfile als Installskript markierte optionale macOS-Paket fsevents wurde unter Linux nicht ausgeführt. Kein fremder Generator, Registryinstaller, postinstall oder Remotehook gestartet.

Die Original-Lizenztexte der Browserlaufzeit und ihrer relevanten Laufzeitabhängigkeiten stehen in [THIRD_PARTY_NOTICES.txt](public/THIRD_PARTY_NOTICES.txt) und werden als statisches Buildartefakt mitgeführt. React-/i18next-MIT und Lucide-ISC/Feather-MIT nicht mit eigener Projektlizenz gleichsetzen. Systemfonts werden nicht eingebettet oder extern heruntergeladen. Vor echter Distribution vollständige Artefakt-/Lizenz-/Noticesprüfung wiederholen; keine Rechtsfreigabe für spätere proprietäre Erweiterungen aus diesem Prototyp ableiten.
