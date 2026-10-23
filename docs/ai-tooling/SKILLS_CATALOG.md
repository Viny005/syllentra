# Lokale Skills — Zweck, Wiederverwendung und Grenzen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Aufnahmeentscheidung

Vor Mission 7 kein lokaler `SKILL.md` und kein `CLAUDE.md`; PACE regelt bereits den allgemeinen Ablauf. Deshalb nur drei kleine spezialisierte Checkverfahren ergänzen. Keine fremden Skills importiert, kein Quelltext aus Beispielen kopiert, keine ausführbaren Dateien, Toolfreigaben oder Netzwerkabhängigkeit. Eigenes gemeinsames Inhaltsformat mit ausschließlich `name` und `description` im YAML-Frontmatter; Verzeichnisname gleich Skillname, maximal 64 bzw. 1024 Zeichen. Format durch offizielle [Quellen](../development/SOURCES.md) bestätigt.

| Skill | Wiederkehrender Bedarf / Trigger | Eingabe → Ausgabe | Entscheidung |
|---|---|---|---|
| [syllentra-spec-review](../../.agents/skills/syllentra-spec-review/SKILL.md) | Review einer Spezifikationsänderung, Kennungs-/Traceabilitykonflikt | Ausgangs-SHA, Dokumente, bestätigte Entscheidung → Befundliste und Erhaltungs-/Statusnachweis | Jetzt deklarativ erstellt; keine automatische Bearbeitung |
| [syllentra-documentation](../../.agents/skills/syllentra-documentation/SKILL.md) | Quellen-/Dokumentpflege und Übergabe | Auftrag/Scope, Primärquellen, Diff → konsistente Dokumente nur bei EDIT und tatsächlicher Prüfbericht | Jetzt erstellt; PACE verlinkt statt vollständig kopiert |
| [syllentra-release-readiness](../../.agents/skills/syllentra-release-readiness/SKILL.md) | Wiederholte Frage nach Freigabereife / fehlenden Belegen | Releaseumfang, Artefakte, 46 REL → anwendbar/bestanden/fehlgeschlagen/offen mit Evidenz | Jetzt erstellt, heute Ergebnis „nicht produktabnahmefähig“; niemals Release ausführen |
| syllentra-feature-implementation | Erst bei freigegebenem Stack und konkreter genehmigter Funktion | FE/UC, Pfade, Abnahmen → Code-/Testbelege | Zurückgestellt: kein Anwendungscode; würde heute PACE nur wiederholen |
| syllentra-security-review | Bei implementierter Auth-/Daten-/Integrationsgrenze | Threatmodel/Scope → priorisierte Negativbefunde | Zurückgestellt; N2 und lesende Reviewrolle decken Dokumentstand |
| syllentra-ui-review | Bei ausführbaren Komponenten / visueller Probe | Designfassung/Geräte → UX-/A11y-Befunde | Zurückgestellt; Frontendplan liefert zunächst Verfahren |
| syllentra-test-review | Bei Tests mit echtem Runner | Sollfälle/Testdiff → Abdeckungslücken / reale Ergebnisse | Zurückgestellt; keine triviale Testhülle erzeugen |
| syllentra-ai-evaluation | Bei konkret erlaubtem Modell-/Adapterversuch | Artefakte/Korpus/Grenzen → Güte-/Kosten-/Schutzbericht | Zurückgestellt; bestehende T01–T09 bleiben maßgeblich |

## 2. Nutzung ohne Scheinkompatibilität

Codex-Projektdiscovery unter `.agents/skills` durch offiziellen Quelltext bestätigt; konkrete Cloud-/CLIversion muss die Dateien tatsächlich aufnehmen. Erst nach echter Invocation als getestet bezeichnen. Für Claude Code kanonischen Skillpfad ausdrücklich im Auftrag lesen lassen; `.claude/skills` hier **nicht** eingerichtet. Kein Symlink oder zweiter Inhaltsstand. Eine spätere offiziell unterstützte gemeinsame Discovery erst an tatsächlichen Clients nachweisen; bis dahin explizites Lesen statt erfundener Slashkompatibilität.

Alle Skills sind Beschreibungen, keine Securitysandboxes. Keine Autorisierung durch Skillname, automatische Empfehlung oder `allowed-tools`; letzteres wurde bewusst nicht gesetzt. Keine externen Inhalte als Anweisung übernehmen. Änderungen an einem Skill wie Code reviewen: Herkunft, Diff, Trigger, Befugnisse, Links, Seiteneffekte, Sensitivität. Kein Skill ist im Zuge dieser Mission in Codex oder Claude Code funktional aufgerufen/getestet worden.
