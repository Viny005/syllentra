# Übergabevorlage

Nur überprüfte Tatsachen eintragen; unbekannte, fehlgeschlagene und nicht ausführbare Punkte ausdrücklich kennzeichnen. Keine erfundenen Testergebnisse oder behaupteten Erfolge. Bezug: [Workflow](WORKFLOW.md).

## Auftrag und Zustand

- Aufgaben-ID, Datum, Quelle, Modus und erlaubter Umfang: ⟨eintragen⟩
- Ausgangszustand: ⟨Repository, Branch, vollständiger Basiscommit, Worktree, relevante Remote-Refs mit Prüfzeitpunkt⟩
- Endzustand: ⟨tatsächlicher Branch/Commit, Worktree, verifizierter Remote-Stand oder lokale Änderungen; Commit/Push/PR/Merge/Deployment jeweils getrennt⟩
- Tatsächlich geänderte Dateien: ⟨Pfade und jeweilige Wirkung; beabsichtigte, aber nicht erfolgte Änderungen getrennt⟩

## Entscheidungen und Funktionsstand

- Entscheidungen und Begründungen: ⟨Primärquelle, Status; bestätigte Vorgabe gegenüber Entwurf/Annahme abgrenzen⟩
- Implementiert: ⟨konkreter Codebeleg oder ausdrücklich keine Implementierung⟩
- Nicht implementiert: ⟨geplante Funktionen, bekannte Lücken⟩
- Getestetes Verhalten: ⟨nur durch tatsächliche Prüfungen gedeckter Umfang; keine Gleichsetzung von Spezifikation, Implementierung und Test⟩

## Tatsächliche Verifikation

| Prüfung / Befehl | Basis und Voraussetzungen | Ergebnis / Beleg | Einschränkung |
|---|---|---|---|
| ⟨eintragen⟩ | ⟨eintragen⟩ | ⟨bestanden / fehlgeschlagen / nicht ausführbar / nicht durchgeführt⟩ | ⟨Grund und Folgen⟩ |

## Übergabe und Kontextpflege

- Fehler, Blockaden und offene Punkte: ⟨Ursache, Auswirkungen, noch erforderliche Freigabe⟩
- Sicherheitsrelevante Erkenntnisse: ⟨ohne Geheimnisse/private Daten⟩
- Kontextänderungen: ⟨Primärquelle, Projektkontext, ADR, Protokoll oder begründeter fehlender Änderungsbedarf; fehlende Bearbeitungsfreigabe benennen⟩
- Nächste empfohlene Schritte: ⟨Empfehlung gegenüber bereits autorisierter Aufgabe unterscheiden⟩
- Links: ⟨Commit, PR und überprüfte Belege soweit vorhanden; fehlenden Zugriff offen angeben⟩
