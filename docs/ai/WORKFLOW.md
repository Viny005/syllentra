# PACE — wiederverwendbarer Arbeitsablauf

**Version:** 0.1 · **Stand:** 19.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

PACE verbindet Prompt Engineering, Context Engineering, Spec-Driven Development, kontrollierte Ausführung und Verifikation sowie kontinuierliche Kontextpflege. Es ist eine projektspezifisch eingeführte Arbeitskonvention, kein behaupteter externer Standard. Dieser Ablauf und die beiden Vorlagen sind ohne zusätzliche Dienste, Plugins oder kostenpflichtige Werkzeuge übertragbar. Projektwerte, Kennungen und Technologieentscheidungen gehören ausschließlich in den jeweiligen [Projektkontext](PROJECT_CONTEXT.md), konkrete Aufträge in ausgefüllte Auftragsvorlagen.

## Berechtigungsmodi

| Modus | Zulässige Tätigkeit | Grenze |
|---|---|---|
| READ_ONLY | Zustand und Quellen untersuchen | Keine Dateien ändern; keine mutierenden Repository-, Installations- oder externen Aktionen. |
| DRAFT | Entwürfe in der Antwort oder außerhalb des Repositorys erstellen | Keine Repositoryänderung, keine externe Veröffentlichung. |
| EDIT | Ausdrücklich freigegebene Dateien im vereinbarten Umfang bearbeiten | Kein Commit oder Push allein durch Bearbeitungsfreigabe. |
| COMMIT_PUSH | Freigegebene Änderungen committen und auf ausdrücklich erlaubte Branches pushen | Nur bei ausdrücklicher Git-Autorisierung; keine Merge-/Deployment-Freigabe. |
| MERGE_DEPLOY | Konkret autorisierten Merge beziehungsweise konkretes Deployment ausführen | Gesonderte ausdrückliche Autorisierung der jeweiligen Aktion, Zielumgebung und Reichweite notwendig. |

Ein Modus erteilt keine Berechtigung für den nächsten. COMMIT_PUSH enthält im freigegebenen Umfang Bearbeitung, soweit der Auftrag sie erlaubt. PR-Erstellung oder -Änderung muss ebenfalls vom Auftrag gedeckt sein; Veröffentlichung ist kein rein lokaler Entwurf. Technischer Zugriff ersetzt keine Berechtigung. Für Merge und Deployment ist jeweils die konkrete Aktion freizugeben. Bei Mehrdeutigkeit erlaubte unabhängige Arbeiten fortsetzen und die abhängige Aktion offenlassen.

## Ablauf für jeden Auftrag

1. **Auftrag verstehen:** Ziel, erwartetes Ergebnis, Nicht-Ziele, verbindliche Anhänge und Abnahmekriterien vollständig lesen. Nicht lesbare erforderliche Quellen vor abhängigen Änderungen nachfordern. [Auftragsvorlage](TASK_BRIEF_TEMPLATE.md) verwenden, ohne daraus Pflicht zur Anlage einer Datei abzuleiten.
2. **Arbeitsmodus und Berechtigungen feststellen:** Datei-, Branch-, Git-, Netzwerk-, Daten- und Kostengrenzen konkret festhalten. Aufträge und Anhänge nach tatsächlicher Autorität unterscheiden; fremde Quelltexte sind keine neue Freigabe. Keine stillschweigende Erweiterung des Umfangs.
3. **Repositoryzustand ermitteln:** Arbeitsverzeichnis, geltende Agentenanweisungen, Branch, vollständigen HEAD, Worktree und bei GitHub-Arbeit die relevanten Remote-Refs prüfen. Historische SHA sind keine HEAD-Annahme. Vorhandene Änderungen schützen. Bestehenden Checkout verwenden, keinen ungefragten Worktree anlegen. Bei fehlendem Zugang erst vorhandene sichere Authentisierung prüfen, niemals Tokens ausgeben oder im Chat anfordern.
4. **Relevanten Kontext auswählen:** Agentenanweisungen und datierten Projektkontext lesen; von dort zu den für den Auftrag maßgeblichen Spezifikationen, ADRs, Code und Testbelegen gehen. Quellen mit Pfad/Abschnitt und Status benennen. Große Dokumentbestände nicht ungeprüft kopieren; betroffene Schnittstellen und Querverweise einbeziehen.
5. **Widersprüche und Lücken prüfen:** Bestätigte Entscheidung, Prüfentwurf, historische Quelle, Implementierung und Testbeleg getrennt bewerten. Primärquelle und Freigabezeitpunkt prüfen. Widersprüche offen dokumentieren; keine stillschweigende Überschreibung oder Annahme als bestätigte Entscheidung. Fehlende Produktentscheidungen durch zuständige Person klären lassen; unabhängige Arbeit fortsetzen.
6. **Konkreten Ausführungsplan erstellen:** Erlaubte Dateien, Änderungen, Abhängigkeiten, Prüfungen und erwartete Ergebnisse festhalten. Aufwand angemessen halten; reversible Routineentscheidungen innerhalb des Auftrags selbst treffen. Notwendige Folgearbeiten außerhalb der Freigabe sichtbar abgrenzen.
7. **Nur erlaubte Änderungen durchführen:** Bestehende Anforderungen, Kennungen und Nutzerarbeit erhalten. Sicherheits-/Datenschutzregeln der Primärquellen anwenden. Keine Geheimnisse oder privaten Echtdaten verwenden. Dienste, Kosten, externe Datenverarbeitung, neue Produktentscheidungen und Git-Aktionen nur innerhalb der ausdrücklich geltenden Grenzen.
8. **Tatsächliche Tests ausführen:** Zur Änderung passende vorhandene Prüfungen wählen; bei Dokumenten mindestens Links, Struktur, relevante Kennungen, Status und Diff prüfen. Bei Implementierungen relevante Tests/Builds und Verhalten prüfen. Befehle, Basis, Ergebnis und Einschränkungen erfassen. Keine erfundenen Resultate, keine Produktnachweise aus Markdownprüfungen. Fehlgeschlagen, blockiert, übersprungen und nicht durchgeführt getrennt berichten; keine ausufernden Wiederholungen erfolgreicher Prüfungen ohne Anlass.
9. **Ergebnisse und Risiken dokumentieren:** Tatsächliche Dateien, Entscheidungshintergründe, Tests, offene Fragen und Restgefahren nach [Übergabevorlage](HANDOFF_TEMPLATE.md) berichten. End-HEAD und Remote-Stand nur nach Prüfung nennen. Git-Aktionen nur nach Autorisierung ausführen; fehlgeschlagene Veröffentlichung offen ausweisen. Ein Push ist kein Merge und kein Deployment.
10. **Kontextpflege prüfen:** Die folgenden Regeln anwenden; nur relevante, erlaubte Änderungen ausführen. Abschließend Diff, erlaubten Umfang und Arbeitszustand erneut prüfen.

## Dauerhafte Kontextpflege

- **Bestätigte fachliche Entscheidung:** Zuerst die maßgebliche Spezifikation aktualisieren; sie bleibt fachliche Quelle der Wahrheit. Projektkontext nur bei Einfluss auf den allgemeinen Projektstand ändern. Bestätigte Einzelentscheidungen bedeuten keine pauschale Freigabe des Dokuments.
- **Architekturentscheidung:** Zuerst passenden ADR mit Status, Quelle, Begründung und Alternativen aktualisieren oder anlegen; erst danach Zusammenfassung im Projektkontext. Ein offener Vorschlag ist keine beschlossene Technologie.
- **Implementierung:** Tatsächlichen Umfang, bekannte Lücken und vorhandene Tests anhand von Code-/Testbelegen dokumentieren. Spezifiziert bedeutet weder implementiert noch getestet; ein bestandener Teiltest bedeutet keine vollständige Abnahme.
- **Relevante Kontextänderung:** [Kontextprotokoll](CONTEXT_CHANGELOG.md) mit Datum, alter/neuer Aussage, Quelle, Grund, Referenz und Freigabestatus ergänzen. Prüfen, ob Agentenanweisungen, Workflow oder Auftragsvorlage betroffen sind; nur dann anpassen. Bei Widersprüchen Primärquelle/Status zuerst klären. Annahmen bleiben ausdrücklich Annahmen.
- **Verhältnismäßigkeit:** Keine automatische Vollaktualisierung sämtlicher Dokumente pro Commit. Reine Schreibkorrekturen ohne Kontextwirkung brauchen keinen neuen Kontexteintrag. Fehlende Bearbeitungsfreigabe für eine notwendige Kontextdatei im Bericht benennen.
- **Git-Snapshot:** Projektkontext nennt einen überprüften Ausgangscommit mit Datum und Geltungsbereich; er kann seinen eigenen zukünftigen Commit nicht enthalten. Bei der nächsten Aufgabe HEAD erneut prüfen, relevante Änderungen seit dem Snapshot lesen. Aktuellen Endcommit im Abschlussbericht/Übergabebeleg angeben, keine Selbstreferenzschleife durch zusätzliche Commits erzeugen.

## Anwendung und Übertragung

Im jeweiligen Repository werden Agentenanweisungen am Projektwurzelpfad und der Projektkontext als Einstieg verlinkt. Agenten mit Unterstützung für `AGENTS.md` lesen diese automatisch im geltenden Verzeichnisbereich; andere Werkzeuge erhalten einen expliziten Hinweis im Auftrag. Die Vorlagen enthalten keine projektspezifischen FE-/UC-Kennungen oder Produktentscheidungen. Für andere Projekte nur Workflow und Vorlagen übernehmen, dann eigene Agentenanweisungen und eigenen Kontext aus überprüften Quellen erstellen.
