# Wiederholbare Verfahren, Hooks und Berechtigungen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Verfahren im vorhandenen Dokumentationsstand

Befehle sind einzeln auszuführen, Ausgabe prüfen, keine Shellpipelines mit maskierten Fehlern. Keine erfundenen `npm test`-/Buildbefehle ohne Manifest. Vorhandene Drittwerkzeuge nur verwenden, wenn vertrauenswürdig und verfügbar; fehlende Werkzeuge offen melden, nicht still installieren. [PACE](../ai/WORKFLOW.md) und konkrete Autorisierung gehen vor.

| Aufgabe | Verfahren / Eingabe | Ergebnis und Grenze |
|---|---|---|
| Gitstand | `git status --short --branch`, `git rev-parse HEAD`, `git ls-remote origin refs/heads/main refs/heads/docs/spec/p1-p2-mobile-workspaces refs/pull/1/head` | SHA/Branch/Worktree vergleichen, PR-Status separat lesen; kein Pull/Reset aus bloßem Statuscheck |
| Spezifikation prüfen | Spec-review-Skill, relevante Primärquellen vollständig lesen, stabile Kennungen/Status/Abnahmen vergleichen | Befunde, Erhaltungsbelege, keine eigenmächtige Fachkorrektur |
| Feature vorbereiten | FE/UC/DEC, Daten-/Schutzgrenze, Pfade, Nichtziele, negative Abnahmen, Abhängigkeiten nach TASK_BRIEF_TEMPLATE | Erst nach Eigentümerentscheidung Implementierungsauftrag; kein Gerüst aus dieser Prozedur |
| Diff prüfen | `git diff --stat`, `git diff --name-status`, `git diff`, später bei Staging `git diff --cached` | Nur freigegebener Umfang; neue untracked Dateien zusätzlich prüfen, nicht im Diff vergessen |
| Verfügbare Checks | Markdownparser, lokale Link-/Anker-/Tabellen-/IDprüfung und `git diff --check`; später echte Manifest-/CIbefehle | Befehle/Versionen/Status festhalten, Produkt- und Dokumentprüfungen trennen |
| Zugänglichkeit | Frontendplan mit Tastatur/Screenreader/Zoom und später axe/Playwright | Heute nur Plan, kein bestandener Produkttest |
| Sicherheitsreview | N2/46 REL plus Konto A/B, direkte API, Entzug, Jobs, Import und Außenweitergabe nach betroffenem Umfang | Offene Belege/Fehler statt pauschaler Sicherheitszusage |
| Abhängigkeiten prüfen | Herkunft/Revision/LICENSE, Transitive/Installskripte/Advisories, Lockfile/SBOM später | Netzwerk/Installation separat autorisieren; Registryauskunft nicht als Code ausführen |
| PR vorbereiten | Titel mit Problem/Verhalten, Scope, echte Checks und Restrisiko; vorhandene PR prüfen | Nur autorisierte Git-/PRaktion, kein automatischer Merge; fremde Diffs erhalten |
| Release prüfen | Release-readiness-Skill, S3 und 46 Profile, aktuelle Belegakte | Fehlende Produktbelege blockieren Freigabe; niemals selbst deployen |
| Abschluss | HANDOFF_TEMPLATE: tatsächliche Dateien, Gründe, Checks, Restpunkte, SHA/Remote/PR | Keine Geheimnisse/Temppfade/Sitzungsgeschichte; nicht durchgeführte Tests ausdrücklich nennen |

Codex: explizite Skillanforderung bzw. normaler Auftrag. Claude: für neue wiederholbare Aufgaben Skills gegenüber Legacy-`.claude/commands` bevorzugen; der offizielle Changelog belegt beide, aber genaue Invocation ist klientabhängig und hier nicht geprüft. Kein neuer Slashcommand, Alias, Deploy- oder Mergeknopf angelegt.

## 2. Hookabwägung ohne Aktivierung

Offizielle Claude-Pluginquellen belegen PreToolUse, PostToolUse, Stop und weitere Ereignisse. Projekt-Settings und Plugin-`hooks/hooks.json` sind verschiedene Einbettungen, nicht blind kopieren. Aktueller Codex-Quelltext enthält ebenfalls Hooks; keine Übernahme des Claude-Schemas. Version/Schema/Ereignis-/Exitstatusvertrag vor Einführung gesondert verifizieren. Sprachmodellbasierte Hooks sind keine deterministische Schutzgrenze.

| Bedarf | Möglicher lokaler Hook | Verlässlichere bzw. ergänzende Grenze |
|---|---|---|
| Formatierung / Syntax | PostToolUse nur für vorab geprüften lokal gepinnten Formatter | Identische deterministische Prüfung in späterer CI; keine versteckte Inhaltsänderung im Review |
| Sensible Pfade / Dateiumfang | PreToolUse meldet unerlaubtes Ziel und blockiert soweit technisch unterstützt | Sandbox-/Filesystemrechte, vollständiger Gitdiff; Shellumgehung nicht durch Textregex sicher abgedeckt |
| Tests | PostToolUse/Stop weist auf betroffene Tests hin | Expliziter reproduzierbarer Runner und CI-Gate, Status nicht überschreiben |
| Secretprävention | Git-pre-commit/Gitleaks auf Diff | Zusätzlich CI-/gesamte relevante Historienprüfung, Secretrotation bei Fund; umgehbare lokale Hooks genügen nicht |
| Settings/MCP/Config | Diffprüfung und menschliches Review jedes Konfigurationsziels | Minimale Tool-/Netzrechte, keine unbekannten Autostartserver; Änderungen nicht automatisch ausführen |
| Scopeverletzung | Stop-Bericht prüft tatsächlich geänderte Pfade | Verantwortlicher prüft Diff; Warnung allein verhindert keinen Zugriff |

Git hooks sind lokal umgehbar/nicht automatisch gemeinsam installiert; `pre-commit` erleichtert Versionsbindung, führt aber selbst Hookcode aus. Erst Herkunft/Revision/Skripte prüfen. Linters prüfen Inhalt unabhängig vom Agenten. GitHub Actions später mit minimalen Permissions, gepinnten Actions, sicherem Umgang mit untrusted PRs und ohne Secrets für fremden Code; Konfiguration der GitHub-Sicherheit in dieser Mission ausdrücklich unberührt. Keine neue Hook-/CI-/MCPdatei oder ausführbarer Scriptinhalt angelegt.
