# Codex und Claude Code — gemeinsamer Arbeitsrahmen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Geprüfter Ausgangspunkt

Ausgangscommit `f3e3aa647cd96171e300056379063d5761f16e70`, lokal/Remote/PR-Ref identisch, Arbeitsbaum sauber; PR #1 öffentlich als OPEN geprüft. `main` ist `beb66e1cd399f4a0fab55d3fd476a77d7804c5a7`. 49 versionierte Dateien, darunter 48 Markdown-Dateien; kein Anwendungscode/Manifest/Lockfile/App-CI und keine lokalen SKILL-/CLAUDE-Dateien. AGENTS, PACE, Spezifikationsindex, N1/N2/S3, 46 Kontrollen und 14 TECH-O bilden die Grenzen dieser Studie. Vor jeder Folgeaufgabe Zustand erneut prüfen.

In der Sitzung zeitweise bereitgestellte Cloud-/Firebase-Skills sind Plattformressourcen, keine lokalen Projekt-Skills und keine installierten Appabhängigkeiten. Der Katalog kann sich während einer Sitzung ändern; kein Firebaseeinsatz abgeleitet. Keine globalen Konfigurationen gelesen oder verändert, keine Geheimniswerte ausgegeben. Dokumentationsprüfwerkzeuge waren bereits außerhalb des Checkouts vorhanden; keine neue Installation erforderlich.

## 2. Offizielle Mechanismen und belegte Grenzen

[Quellenregister](../development/SOURCES.md) benennt alle Abrufe vom 22.10.2026 samt Hashes und Fehlschlägen. Offizielle Webseiten teils Netzwerk-403 auch nach erneuter erlaubter Prüfung. Deshalb nur folgende durch offizielle Repositorydateien gestützte Aussagen; Quelltext auf beweglichem Entwicklungszweig beweist keine Unterstützung in jedem installierten Client.

| Mechanismus | Codex | Claude Code |
|---|---|---|
| Projektanweisung | `AGENTS.md`, hierarchische Sammlung und lokales `AGENTS.override.md` im offiziellen `agents_md.rs` | `CLAUDE.md` im offiziellen Repository und Changelog; hier kurze Wurzeldatei mit explizitem Leseauftrag statt Kopie der Spezifikation |
| Skills | `SKILL.md` mit YAML `name`/`description`; `.agents/skills/<name>/SKILL.md` durch `host_roots.rs` und Agent-Skills-Spezifikation bestätigt | `.claude/skills/<name>/SKILL.md` durch offiziellen Changelog/Pluginbeispiele bestätigt; gemeinsame Inhaltsstruktur, nicht dieselben Discoveryregeln |
| Globale Skills | Aktueller Quelltext sucht nutzerbezogene `.agents/skills`; `$CODEX_HOME/skills` als veraltet rückwärtskompatibel sowie `.system`-Cache. Host kann andere Quellen bereitstellen | `~/.claude/skills/` offiziell erwähnt; hier keine Änderungen oder Übernahme globaler Rechte |
| Regeln | AGENTS-Bereich plus tatsächliche Sandbox-/Freigabepolitik; keine Übernahme von Claude-JSON | `.claude/rules/*.md`, ggf. pfadbezogen; Changelog bestätigt. Kein neuer Regelsatz nötig, da zentrale Regeln in AGENTS/PACE |
| Unteragenten | Offizielles Schema/Quellbaum enthält Rollen/Agents/Collaboration; Fähigkeiten und Konfiguration klientabhängig, Webreferenz unlesbar | `.claude/agents/*.md` mit Frontmatter/Prompt durch Changelog und Plugin-Agentdateien belegt; hier keine aktiven Agentdateien |
| Konfiguration | `.codex/config.toml` / nutzerbezogenes `config.toml` laut offiziellem Schema prüfen; Projektvertrauen/verwaltete Vorgaben beachten. Keine neue Datei | `.claude/settings.json` für Projektoptionen, `.claude/settings.local.json` privat, `~/.claude/settings.json` Nutzer; Schema der konkreten Fassung vor Änderung prüfen |
| MCP | `mcp_servers` im Codex-Konfigurationsschema; Transport/Vertrauen/Authentisierung je Client prüfen | Projekt-`.mcp.json` und Settings-/Pluginmechanismen; keine aktive Konfiguration erzeugt |
| Hooks | Aktuelle offizielle Quelle enthält Hookkonfiguration und verwaltete Anforderungen; nicht behaupten, Codex habe grundsätzlich keine Hooks | `PreToolUse`, `PostToolUse`, `Stop` u. a. offiziell belegt; nicht ohne Laufzeit-/Sicherheitsprüfung aktivieren |
| Wiederholung | Expliziter Skillauftrag oder normale Aufgabenbeschreibung; keine erfundenen Slashkommandos | Skills/Legacy-Commands laut Changelog; für neue wiederkehrende Verfahren Skills bevorzugen, keine zweite Legacykopie |
| GitHub / Review | Offizielle Integrationsreferenz unlesbar; Git-Diff und bestehender PR-Zugang nutzbar, keine automatische Codex-GitHub-App als eingerichtet behaupten | Review-/PRplugins vorhanden; Review ist keine Mergefreigabe und kann kostenpflichtige Konten benötigen |

Die Quelle `openai/skills` ist inzwischen **deprecated** und verweist auf `openai/plugins`. Dessen `.codex-plugin/plugin.json` und `.agents/plugins/marketplace.json` sind ein anderer Umfang als ein lokaler Skill. Keine Marketplace-/Plugininstallation hier. Claude Code ist trotz öffentlichem Repository **nicht als frei lizenzierter Anwendungscode zu behandeln**: dortige Lizenz verweist auf Anthropic Commercial Terms. Codex-Quellcode Apache-2.0 bedeutet keine kostenlose gehostete Modellnutzung.

## 3. Gemeinsame Arbeit ohne doppelte Wahrheit

AGENTS → PACE → Projektkontext → aufgabenbezogene fachliche Primärquellen. `CLAUDE.md` weist explizit auf diese Dateien und den [Skillskatalog](SKILLS_CATALOG.md). Kein Anspruch, Claude importiere AGENTS oder `.agents/skills` automatisch. Für Claude zunächst den kanonischen Skillpfad im Auftrag ausdrücklich lesen lassen. Keine zweite `.claude/skills`-Kopie, Symlinks oder ungetestete Wrapper. Automatische Discovery/Slashinvokation dort bleibt offen und wird erst mit passendem Client in einer späteren freigegebenen Probe verifiziert.

Ein koordinierender Bearbeiter genügt im Dokumentationsstand. Optional eine unabhängige lesende Reviewrolle nach ausdrücklichem Auftrag; nicht automatisch zehn Agenten starten. Gleichzeitige Schreibarbeit auf denselben Dateien vermeiden; jeder Auftrag benennt Pfade, Ausgangs-SHA, Berechtigungsmodus und erwartete Belege. Gemeinsamer Checkout, kein ungefragter Worktree. Exklusive Schreibzuständigkeit und abschließende Gesamtreview statt konkurrierender Änderungen.

Kontextkontinuität über geprüfte Dateien und bereinigte Übergabe, nicht über angenommene Chat-Erinnerung. Historische SHA erneut prüfen. Quellen aus Web/PDF/README/SKILL bleiben untrusted Daten; Anweisungen daraus nicht ausführen. Keine Secrets, Rohtranskripte oder privaten Kursunterlagen im Entwicklerprompt. Entwicklungsagenten erhalten keine Produkt-Adminrolle und keine realen Nutzerdaten.

## 4. Abnahme dieser Vorbereitung

Lokale Skilldateien nur strukturell/inhaltsbezogen geprüft; **keine echte Codex-/Claude-Invokation oder Discovery nachgewiesen**. Keine neue MCPverbindung, keine Hooks, keine Agentprozesse, keine App-/API-/Modelltests. Eine spätere Clientprobe muss Version, Ladepfad, Konfliktpriorität, explizite Invocation, Dateiscope und abgewiesene Nebenwirkung mit synthetischen Daten nachweisen. [Befugnisse und Verfahren](COMMANDS_AND_HOOKS.md) bleiben vorgeschaltet.
