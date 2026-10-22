# Syllentra AI — lokaler Frontend-Prototyp

**Version:** 0.1.0 · **Stand:** 22.10.2026 · **Status:** Experimentell / Zur Prüfung durch den Projektinhaber

Interaktive, reversible UI-Probe aus Mission 8. **Keine operative V1:** ausschließlich synthetische Daten, kein Backend, keine Anmeldung, keine Kontoisolation, keine echte KI oder Cloudverbindung. Bitte keine persönlichen Daten eingeben. TECH-O-03 bleibt offen; React/Vite/TypeScript ist nur für diesen Versuch ausgewählt.

## Lokal ausführen

Voraussetzung: Node 24.x und npm. Bestehenden Checkout verwenden, keinen zusätzlichen Worktree anlegen.

```bash
cd prototypes/frontend
npm ci --ignore-scripts
npm run dev
```

Der Entwicklungsserver bindet standardmäßig nur an die lokale Loopbackadresse. Keine externe Veröffentlichung oder automatische Netzfreigabe; Port 5173 ist vorgesehen. In eingeschränkten Umgebungen gegebenenfalls einen beschreibbaren npm-Cache mit `--cache /tmp/syllentra-npm` angeben. Keine APIkeys, Umgebungsgeheimnisse, Accounts oder Zusatzdienste nötig. Browser nach lokalem Start öffnen; diese Anleitung ist kein Deploymentauftrag.

## Prüfungen

```bash
npm run typecheck
npm run build
npm run lint
npm run format:check
npm test
npm run test:e2e
npm audit
```

Playwright startet für E2E-Prüfungen einen lokalen Vite-Previewserver auf Port 4173 und beendet ihn danach. Der Build muss vorher existieren. Chromium muss bereits installiert sein; Standardpfad `/usr/bin/chromium`, anderer Pfad über `CHROMIUM_PATH`. Kein automatischer Browserdownload. Der Testbrowser verwendet im isolierten Container `--no-sandbox`; ausschließlich lokale synthetische Daten, keine persönlichen Profile oder externen Ziele. Das ist keine Produktionsbrowser- oder App-Sicherheitskonfiguration. Testberichte/Traces und automatisch erzeugte Aufnahmen unter `test-results/` bzw. `artifacts/screenshots/` sind ignoriert. Ausgewählte bereinigte Aufnahmen im [Prüfbericht](../../docs/design/PROTOTYPE_REVIEW.md).

## Aufbau

- `src/ui`: wiederverwendbare Dialoge, Status-/Leerzustände und Basiselemente.
- `src/layouts`: Desktopnavigation, mobile Dialognavigation und Rahmen.
- `src/pages`: acht Hauptbereiche sowie getrennte Adminabgrenzung/Fehlerseite.
- `src/features`: Modulkarten und Formular für lokale Beispielsitzungen.
- `src/data`: ausdrücklich fiktive Module, Dokumente und Kalenderdaten.
- `src/locales`: vollständige deutsche, französische und englische Ressourcen, lokale i18next-Konfiguration ohne Netzloader.
- `src/styles`: zentrale semantische Tokens und responsive Darstellung.
- `src/lib`: kleine Datums-, Präferenz- und Hashroutingfunktionen.
- `tests`: deterministische Kernprüfungen und reale Chromium-End-to-End-Prüfungen.

Hashnavigation nutzt normale Links, Browser-Zurück und direkte Unterseiten ohne zusätzlichen Router. Kein künstlicher Backend-/Servicebaukasten. Eigene CSS-Komponenten und native Dialog-/Formularelemente reichen für diese Probe: kein Tailwind-/shadcn-Generator und keine zusätzlichen Primitiven, Richtext-, PDF-, Chat-, Graph- oder Kalenderpakete installiert. [Installierte Pakete/Lizenzen](LICENSES.md).

## Bedienbare Abläufe und Datengrenzen

Dashboard → Kursdetails → Bibliotheksfilter → lokale Dokumentvorschau → simulierter Chat. Beispieldialog/-verlauf, Texteingabe, feste Antwort nach begrenzter Wartezeit und Stop. Keine semantische Antwort auf freie Fragen und keine Quelle tatsächlich analysiert. Strukturierte Notizen sind lesbar, kein Editor/PDFreader vorgetäuscht. Kalender mit Wochennavigation und direkt gespeicherter manueller Sitzung **nur im Arbeitsspeicher**, ohne künstliche zweite Bestätigung. Kalenderdaten sind zivile Beispieldaten/-zeiten ohne externe Zeitzonensynchronisation. Fortschritt und manuelle Markierung sind ausdrücklich fiktiv, kein Kompetenz-/Leistungsnachweis.

Sprache und Theme werden ausschließlich als bekannte Auswahlwerte mit `syllentra-demo:`-Präfix lokal gespeichert; bei blockiertem Storage funktioniert die Sitzung weiter. Keine Nachrichten, Termine, Dokumente oder Lernprofile im Browserspeicher. Seitenwechsel können lokale Seitenentwürfe zurücksetzen; Neuladen verwirft sämtliche Beispieldatenänderungen. Keine Mehrgeräte-/Offline-/PWA-Installationszusage, Serviceworker oder echte Authentisierung. Administration als eigener nicht aktiver Bereich, ohne Rechteformular oder simulierte Sicherheitsfreigabe.

## Offene Entscheidungen

Eigentümerreview von Design, Lesedichte, Geräten/Browsern, Bedienpfaden und experimentellem Stack; danach separat genehmigte Backend-/Auth-/Isolationsprobe. Alle 14 TECH-O sowie FE-56 bleiben offen. [Design System](../../docs/design/DESIGN_SYSTEM.md), [fachliche Spezifikation](../../docs/spec/README.md), [Prüfbericht](../../docs/design/PROTOTYPE_REVIEW.md). Keine Ausgabe, Cloud, KI-API, neue MCPverbindung, Veröffentlichung oder Merge freigegeben.
