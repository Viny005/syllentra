# Entwicklungsrollen und menschliche Verantwortung

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Gemeinsamer Rollenvertrag

Die folgende Matrix ist eine Organisationsvorlage, keine aktivierten Unteragenten. Rollen verleihen weder Dateirechte noch Git-/Tool-/Cloudrechte. Standard READ_ONLY; EDIT/COMMIT_PUSH ausschließlich im konkreten Auftrag und nach [PACE](../ai/WORKFLOW.md). Verbot für alle: private Echtdaten/Secrets, globale Toolkonfiguration, nicht beauftragte Dateien, eigenmächtige FE-/DEC-Änderung, `main`, Merge/Deployment/Kosten. Neue Produktentscheidungen ausschließlich Eigentümer; technische Empfehlung kein Beschluss. Fehlender Anwendungscode ist kein Auftrag, ihn anzulegen.

Je Rolle gemeinsame Berichtsstruktur: Ausgangs-/End-SHA, Quellen/IDs, tatsächlicher Umfang, Befund mit Schwere und Datei, tatsächlich gelaufene Checks samt Status, offene Entscheidung und empfohlener nächster Schritt. Keine bloßen „alles sicher“-Aussagen. Verantwortlicher Bearbeiter integriert; Eigentümer prüft fachliche/technische Entscheidungen und Freigaben. Unabhängiger Reviewer bleibt standardmäßig lesend und verantwortet Befundqualität, nicht Produktabnahme.

## 2. Rollenmatrix

Pfade für künftigen Anwendungscode sind bewusst **nicht erfunden**. „Später zugeteilte Pfade“ heißt heute keine Schreibrechte; konkrete Grenzen müssen nach Stack-/Strukturentscheidung im Auftrag stehen. Werkzeuge werden nur eingesetzt, wenn vorhanden und erlaubt.

| Rolle | Ziel, Kompetenz und Verantwortung | Erlaubter Arbeitsbereich / explizit verboten | Benötigte Werkzeuge / Erfolg / Autonomie |
|---|---|---|---|
| Architektur / Spezifikation | Fachgrenzen, Siedersleben, Traceability; Widerspruch und Alternativen belegen | Lesend Spezifikation/ADRs; Schreiben nur zugeteilte `docs/spec`-/Architekturdateien; keine Implementierung oder Entscheidungsschließung | Git/Markdown-/IDcheck; unveränderte FE/UC/DEC außer bestätigter Änderung, begründete Befunde; keine Stackwahl |
| Backend / API | Autoritative Anwendungsfälle, Fehler-/Transaktionsverträge, Serverrechte | Heute nur zugeteilte Vertragsdokumente; später zugeteilte Backend-/Testpfade; keine UI-/Cloud-/Authpolitikänderung nebenbei | Später Typer/pytest/APInegativtests; Konto A/B, Flag-/Replayfälle bestanden; keine eigenmächtige Schema-/Provideränderung |
| Frontend / UI/UX | Zugängliche Lernaufgaben, Design System, PWAzustände | `docs/design` im Auftrag; später zugeteilte UI-/Tests; keine Rechte allein im Client implementieren oder fremde Designs kopieren | Komponenten-/Browser-/Assistenztests später; Aufgabenpfad und Fehlerzustände belegbar; Zielwerte bleiben zu bestätigen |
| Sicherheit / Datenschutz | Threatmodel, Isolation, Secrets, Sessions, Admin-/Flaggrenzen; Befunde priorisieren | Lesend gesamte freigegebene Oberfläche, zugeteilte Schutzdokumente; keine privaten Kontoinhalte, keine Liveangriffe/Providerkonfiguration | Gitdiff/Secretscan später SAST; Negativfälle und Restrisiko nachvollziehbar; kein Ausnahme-/Releaseentscheid |
| Datenbank / Migration | D1/D2-Invarianten, Accountbeziehungen, Revision/Restore/Löschung | Heute Fach-/Migrationsstudie; später zugeteilte Schema-/Tests; keine produktiven DBzugänge oder Echtmigration | Später isolierte PGtests/Restoreprobe; Rollback ohne Wiederbelebung belegt; kein Schemaforce oder Produktionsdump |
| KI / RAG | Adapter, Retrieval, Quellen/Datenschutz, Kosten und Ressourcen | Zugewiesene KI-/Integrationsunterlagen; später Adaptertests; keine fremden Gewichte/Modelle/Netzcalls ohne Auftrag | Deterministische Korpora, später T02/T03; Belegtreue und Rechte geprüft; kein Außenfallback/automatischer Download |
| Pädagogische Qualität | Fachrubriken, Lernziele, Übungs-/Korrektheitsqualität und Sprachvergleich | Synthetische Korpora/Rubriken nach Auftrag; keine Notenänderung, privaten Lernprofile oder amtliche Anerkennung | Menschliches Fachreview + deterministische Fälle; nachvollziehbare Fehler/Unsicherheit; LLMscore keine alleinige Freigabe |
| Tests / Validierung | Anwendbare Sollkriterien prüfen, Regression und negative Fälle gestalten | Zugewiesene Prüfpläne, später Testpfade; keine Tests löschen/abschalten für grüne Ergebnisse | Vorhandene Runner, später Vitest/Playwright/pytest; echte Testzahlen/Befehle/Umgebung; kein ungetestetes Verhalten als bestanden |
| Dokumentation | Quellen, Status, Links und PACE aktuell halten | Nur beauftragte Markdown-/dekl. Skilldateien; kein Code, keine fachliche Änderung aus redaktionellem Anlass | Markdown/Link/IDdiff; Quellen/Versionen konsistent und Historie erhalten; keine Sitzungsarchive |
| Release / Betrieb | 46 REL, S3, unabhängiger Restore und Rückweg prüfen | Zunächst lesende Evidenzmatrix/zugeteilte Betriebsdokumente; kein Merge, Cloudaccount, Deployment, Zahlung | Später autorisierte Artefakt-/Restore-/Releasechecks; jeder anwendbare Beleg vorhanden; Eigentümer entscheidet Freigabe |

## 3. Sinnvolle Besetzung

Jetzt: ein Dokumentations-/Spezifikationsbearbeiter; lesendes Sicherheits-/Konsistenzreview bei gesondertem Auftrag. Nach Anwendungsfreigabe situativ Backend und UI mit disjunkten Dateien; Security/Tests als Reviewverantwortung, nicht zehn dauerhafte Prozesse. Eine Person kann mehrere Rollen übernehmen, muss Selbstprüfung und unabhängige Abnahme aber klar unterscheiden. Umfang, Kosten und Nebenwirkungen jedes Unterauftrags bleiben innerhalb des Hauptauftrags.
