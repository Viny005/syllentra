# MCP und Erweiterungen — Nutzen und Vertrauensgrenzen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Einordnung und Quellen

MCP transportiert Tools, Resources und Prompts zwischen Host/Client und Server, verleiht aber keine fachliche Autorisierung oder sichere Sandbox. Offizielle Protokollarchitektur als öffentlicher Spezifikationsquelltext gelesen; Webseite unlesbar. Auswahl nach Herkunft, minimalem Nutzen, entziehbaren Rechten und tatsächlich geprüftem Code. [Quellen/Lizenzen](../development/SOURCES.md), [Lizenzregister](../development/DEPENDENCY_SELECTION.md). Keine neue Verbindung aktiviert.

Kategorien: **A** nach späterer Freigabe lesend sinnvoll; **B** erst später mit stark begrenzten Rechten; **C** bloße Option; **D** vermeiden. A ist keine Aktivierungsfreigabe. Review von Ursprung, gepflegter konkreter Revision, Abhängigkeiten und Sicherheitsmeldungen bleibt vor Installation Pflicht; ein aktiver Hauptzweig ist keine Wartungsgarantie.

## 2. Vergleich nach Server und tatsächlicher Grenze

| Server / Herkunft / Kategorie | Aktionen und Wert | Permissions, Netz, Credentials, Daten | Risiken, Ausführung, Kosten und Empfehlung |
|---|---|---|---|
| OpenAI Developer Docs MCP, offizieller dokumentierter Dienst — A mit Nachweisvorbehalt | Öffentliche Produktdokumentation gezielt recherchieren | Offizielle Dienstseite 403; aktuelle Tools, Transport, Auth-/Suchlogaufbewahrung nicht verifiziert. Kein Token/privater Kontext übermitteln | Kein OSS-Lizenzrecht am gehosteten Dienst belegt. Offiziellen Endpoint/Terms/Read-only vor späterer Nutzung bestätigen; derzeit öffentliche Quelldateien genügen |
| GitHub MCP, `github/github-mcp-server` — A lesend, B schreibend | Repo/Commit/PR lesen, optional Issues/PRs/Workflows ändern | Repoauswahl + minimale OAuth-/Tokenrechte; Netzwerk zu GitHub, Host/Server sieht erreichbare Inhalte; separate Tools-Allowlist | MIT gelesen; `--read-only` im README zusätzlich zu Credentials begrenzen. Keine pauschalen Workflow-/Write-/Secretrechte; GitHub-Kontoplan/Kosten getrennt. Normales Git genügt aktuell |
| Filesystem, offizieller Referenzserver — C | Lokale Dateien suchen/lesen, je Tools auch schreiben/verschieben | Erlaubte Wurzel eng, OSrechte beschränken, keine Home-/Secret-/Privatdaten; stdio lokal bedeutet nicht automatisch Netzwerkfreiheit des Prozesses | Repository in MIT→Apache-2.0-Übergang; Dateianteile einzeln prüfen. Doppelt vorhandenes Shell-/Dateitool, daher kein heutiger Mehrwert. Schreib-/Pfadfluchtrisiko, kein allgemeiner Kommandoexecutor nötig |
| PostgreSQL Referenzserver aus `servers-archived` — D für Neueinsatz | Historisch Schema und Read-only-SQL | Archiviert, kein aktueller Produktionsnachweis; auch lesend lassen sich fremde Daten abfragen und DBlast erzeugen | Nicht als gepflegter offizieller DBconnector anbieten. Zukunft: B nur isolierte synthetische Test-DB, eigens geprüfter gepflegter Server, minimale DBrolle/Timeout/Netz; Lizenz und Wartung dann neu prüfen |
| Playwright MCP, Microsoft — B | Browserseiten/Accessibilitysnapshot, Interaktionen und Downloads; UIprüfung | Eigenes temporäres Browserprofil, nur synthetisches Testsystem, kein eingeloggtes persönliches Profil; Browser kann weitere Netzziele erreichen | Apache-2.0 gelesen. Herkunftsfilter laut README **keine Sicherheitsgrenze**, Redirects/Browsercookies/Uploads/Downloads/exfiltration beachten; OS-/Netzisolation nötig. CLItests oft kleiner und deterministischer |
| Andere Browser-/Puppeteer-MCPs — C oder D | Ähnliche Navigation/Scripting | Keine ungeprüften Profil-/Filesystem-/Shellrechte; jede konkrete Revision separat | Archivierte Referenz nicht mit gepflegtem Playwrightserver gleichsetzen; kein Bedarf für mehrere Browserconnectoren |
| Andere offizielle Dokumentationsserver — C | Nur bei wiederkehrendem Quellenbedarf | Offizieller Eigentümer, Endpoint/Transport/Tools/Auth/Retention und Lizenz erst einzeln belegen | Keine Liste angeblich vertrauenswürdiger Communityserver erfinden; HTTPabruf vorhandener offizieller Quellen heute ausreichend |
| Unbekannte Installer/„all tools“-Plugins — D | Kein belegter projektspezifischer Nutzen | Breite Tokens, Shell/Filesystem/Netz und automatische Updates vervielfachen Risiko | Keine Ausführung aus URL, `npx ...@latest` oder installierten fremden READMEanweisungen; Popularität kein Audit |

OpenAI-/GitHub-/Claude-Integrationen betreffen Entwicklungsdaten und sind nicht automatisch Syllentra-Produktintegrationen. Keine Weitergabe privater Lerndaten aus einer Entwicklerfreigabe ableiten. GitHub MCP/Filesystem besitzen ohne eigene Begrenzung mutierende Tools; Protokollpräsenz bedeutet nicht „read-only“. Gehostete Dienste können Gebühren/Vertragsbindungen verursachen, auch wenn Serverquellen kostenlos lizenziert sind.

## 3. Prüfverfahren vor jeder späteren Aktivierung

Quelle/Organisation und konkrete Commit-/Artefaktherkunft prüfen; LICENSE/Abhängigkeiten/Installskripte/Sicherheitsmeldungen lesen, Downloadintegrität prüfen. Vollständige Toolinventur mit Seiteneffekten und Netz-/Dateizielen erstellen. Unnötige Tools deaktivieren, Credentials pro Ziel minimal/kurzlebig und außerhalb Git verwalten, keine geerbte Shell-/Adminvollmacht. Sandbox und Netzpolicy unabhängig vom Prompt erzwingen, Schutz vor SSRF/Redirect, begrenzte Outputs/CPU/Zeit. Tokenrotation/Widerruf und Abschalt-/Rückbauprobe planen.

README, Toolbeschreibung, Webtext und SKILL können Prompt Injection enthalten. Als Daten behandeln; kein Befehl aus Antwort, keine Erweiterung der erlaubten Ziele/Tools. Vor sensibler Mutation/Datenweitergabe konkrete menschliche Freigabe; Berechtigung direkt vor Wirkung erneut prüfen. Bereinigte Auditmetadaten, keine Secrets/Privattexte. Ergebnis als bestanden/fehlgeschlagen/offen mit Client-/Serverversion; kein ungeprüfter Server als sicher markieren.

## 4. Plugins und Repositorywiederverwendung

`openai/plugins` und Anthropic-`plugin-dev` nur als offizielle Format-/Musterquellen studiert; nicht installiert und keine allgemeinen Toolrechte aus Beispielen übernommen. Marktplatz enthält heterogene Dienste, Lizenzen und Abos. Für Syllentra kein externer Pluginbaukasten nötig, solange drei eigene deklarative Verfahren genügen. Entfernbarkeit: reine Markdown-Skills lassen sich ohne Datenmigration entfernen; MCP-/Cloudplugins können Tokens, gespeicherte Daten und fremde Verarbeitung hinterlassen, daher Widerruf/Löschung Teil jeder Einführung.
