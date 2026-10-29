# Auftragsvorlage

Universell verwendbar; Platzhalter vor Arbeitsbeginn ausfüllen. Nur tatsächlich erforderlichen Kontext auswählen, keine ganzen Projektarchive kopieren. Nicht gewählte Aktionen erhalten keine Freigabe. Regeln und Modusdefinitionen: [Workflow](WORKFLOW.md).

- **Aufgaben-ID / Datum / Auftraggeber:** ⟨eintragen⟩
- **Ziel und konkretes Problem:** ⟨eintragen⟩
- **Arbeitsmodus:** ⟨READ_ONLY | DRAFT | EDIT | COMMIT_PUSH | MERGE_DEPLOY; autorisierte konkrete Aktionen benennen⟩
- **Erwartetes Ergebnis / Nicht-Ziele:** ⟨Artefakte und Grenzen⟩
- **Aktuelle Ausgangsbasis:** ⟨Repository, Branch, tatsächlich erneut zu prüfender vollständiger Commit, Worktree, relevante Remote-Refs⟩
- **Relevante Kontextquellen:** ⟨geltende Agentenanweisungen, Projektkontext, konkrete Primärquellen mit Abschnitt, Datum und Entscheidungsstatus; erforderliche Anhänge vollständig lesen⟩
- **Betroffene freigegebene Dateien:** ⟨konkrete Pfade; erlaubte Neuanlagen; Kontextpflege ausdrücklich ein-/ausschließen⟩
- **Fachliche Anforderungen:** ⟨bestehende Kennungen, bestätigte Vorgaben, noch offene Fragen; Annahmen gesondert⟩
- **Sicherheits- und Datenschutzbedingungen:** ⟨Datenarten, Rechte, externe Verarbeitung, Secrets, zulässige Testdaten⟩
- **Kosten-/Lizenzgrenzen:** ⟨Untersuchungslimit getrennt von tatsächlicher Ausgabenfreigabe; erlaubte Software-/Modelllizenzen⟩
- **Git-/Veröffentlichungsberechtigungen:** ⟨Basis-/Arbeits-/Zielbranch, Commit, Push und PR jeweils konkret; Merge/Deployment nur gesondert ausdrücklich autorisieren⟩
- **Nicht erlaubte Aktionen:** ⟨Dateien, Produktentscheidungen, Datenzugriffe, Installationen, Ausgaben, Merge/Deployment und sonstige Ausschlüsse⟩
- **Akzeptanzkriterien:** ⟨beobachtbare, überprüfbare Ergebnisse ohne erfundene Produktfreigabe⟩
- **Prüfverfahren:** ⟨tatsächlich auszuführende Befehle/Verhaltensprüfungen, benötigte Voraussetzungen, Belege und Umgang mit Blockaden⟩
- **Gewünschter Abschlussbericht:** ⟨geänderte Dateien, Basis/Endzustand, tatsächliche Tests und Grenzen, Entscheidungen, offene Punkte, Kontextpflege, Git-/PR-Ergebnis⟩

Vor Ausführung Widersprüche und fehlende erforderliche Freigaben sichtbar machen. Ein Entwurf ist keine automatische Autorisierung zur Bearbeitung oder Veröffentlichung. Für den Abschluss die [Übergabevorlage](HANDOFF_TEMPLATE.md) nutzen.
