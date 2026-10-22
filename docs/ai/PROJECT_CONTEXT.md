# Syllentra AI — überprüfter Projektkontext

**Version:** 0.11 · **Stand:** 22.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

## Git-Snapshot und Geltung

Repository: `Viny005/syllentra` — <https://github.com/Viny005/syllentra>.
Aktueller Arbeitsbranch: `docs/spec/p1-p2-mobile-workspaces`, zugeordnet zu [PR #1](https://github.com/Viny005/syllentra/pull/1).
Am 22.10.2026 lokal, per entferntem Branch und PR-Git-Ref überprüfter Ausgangscommit der Mission 9: `8ad51e8ef1ed010b20907602fe742268d799621e`. Arbeitsbaum vor Bearbeitung sauber, PR #1 auf der öffentlichen GitHub-Seite als offen geprüft. PACE ist durch PR #2 seit `39261a5816a99f7c10c79344e5a1adc03b685d49` integriert. Der Snapshot ist eine datierte Ausgangsbasis, kein dauerhaft aktueller HEAD; bei jeder Aufgabe erneut prüfen. Endcommit/Push werden im Abschlussbericht nachgewiesen.

## Ziel und Aufbau

Adaptiver Lernbegleiter für Studierende: Materialien, Audio und Gespräche mit persönlichen Lernzielen, Studienorganisation und nachvollziehbarer Lernentwicklung verbinden. Dokumentation zuerst; Spezifikation, Architektur, Implementierung und Testbelege getrennt halten. PACE beschreibt die Arbeit am Repository, keine neue Produktfunktion.

## Maßgebliche Quellen

| Quelle | Zuständigkeit und Status |
|---|---|
| [Spezifikationsindex / E1](../spec/README.md) | Einstieg, Versions-/Statusübersicht und Siedersleben-Konvention. Alle ausgearbeiteten Dokumente weiterhin Zur Prüfung durch den Projektinhaber. |
| [P1](../spec/P1-ziele-rahmenbedingungen.md), [P2](../spec/P2-architekturueberblick.md) | Ziele/Rahmen, Systemkontext und Nachbarsysteme; keine technische Stackentscheidung. |
| [F1](../spec/F1-geschaeftsprozesse.md), [F2](../spec/F2-anwendungsfaelle.md), [F3](../spec/F3-anwendungsfunktionen.md) | Prozesse, 66 Anwendungsfälle und fachliche Funktionen. |
| [D1](../spec/D1-datenmodell.md), [D2](../spec/D2-datentypen.md) | Fachliche Daten, Beziehungen, Invarianten und Datentypen. |
| [B1](../spec/B1-dialogspezifikation.md), [B2](../spec/B2-batch.md), [B3](../spec/B3-druckausgaben.md) | Dialoge, Hintergrundverarbeitung und Ausgaben. |
| [S1](../spec/S1-nachbarsysteme.md), [S2](../spec/S2-datenmigration.md) | Nachbarverträge, kanonische 89 FE in S1.18.1, Migration/Export/Wiederherstellung. |
| [S3](../spec/S3-inbetriebnahme.md) | Version 0.2: zukünftige Betriebsaufnahme, Super-Admin-Grenzen, unabhängiger Restore, 46 Kontrollverweise und menschliche Freigabe; keine technische Umsetzung. |
| [N1](../spec/N1-nichtfunktional.md), [N2](../spec/N2-querschnittskonzepte.md) | Fachlich vervollständigte V1-Prüfentwürfe: 25 NFR- und 27 SEC-Profile; Zielwerte, Verfahren und Produktnachweise offen. |
| [40-Punkte-Release-Checkliste](../quality/RELEASE_READINESS_40.md) | Zwei vom Projektinhaber am 22.10.2026 bestätigte Quellenlisten mit je 20 Prüfpunkten (REL-S01..20, REL-Q01..20); V1-Freigabekriterien, REL-Q10 Zahlung nur spätere Option. Ohne Produktnachweise. |
| [Qualitäts-/Freigabeergänzungen](../quality/RELEASE_KONTROLLMATRIX.md) | 20 Kandidaten konsolidiert: sechs neue Kontrollen, 46 insgesamt. Verlinkter Referenzrahmen und Freigabevoraussetzungen liegen dem S3-Prüfentwurf zugrunde; keine Produktprüfung. |
| [E2](../spec/E2-glossar.md), [E3](../spec/E3-pruefnachweis.md) | Begriffe sowie datierte tatsächliche Dokumentationsprüfungen; kein Produktabnahmetest. |
| [Entscheidungsmatrix](../spec/ENTSCHEIDUNGSMATRIX.md) | Aktuelle DEC-V1-/FE-21-Zuordnung und DEC-48/49, Soll-Abnahmen und verbleibende Präzisierungen; zur Prüfung. |
| [Entwicklungszuordnungen](../spec/ENTWICKLUNGSPLAN.md) | Bestätigter Teilstand, kein vollständiger freigegebener Meilensteinplan. |
| [Technische Vergleichsstudie](../architecture/README.md) | 13 Dokumente einschließlich Mission-6-Machbarkeit/Testplanung: Empfehlungen zu Architektur/Hosting/KI/Daten/Stack/Backup/Kosten, offene technische Punkte und Quellen; Empfohlen / Zur Entscheidung, keine Auswahl. |
| [ADR-Konvention](../ARCHITECTURE_DECISIONS.md), [Roadmap](../ROADMAP.md) | Noch keine finale Stackwahl; historische Forschungs-/Entwicklungsphasen. |
| [Vision](../PROJECT_VISION.md), [ursprüngliche Anforderungen](../REQUIREMENTS.md) | Historische Grundlagen; bei Abweichungen aktuelle bestätigte Entscheidungen und deren Quellenstatus prüfen. |
| [PACE-Auftrag im Kontextprotokoll](CONTEXT_CHANGELOG.md) | Quelle der neuen Arbeitskonvention und des Untersuchungslimits; keine Änderung fachlicher FE/UC. |

## Bestätigter fachlicher Rahmen

Die Zusammenfassung ersetzt keine Primärquelle: S1.18.1 enthält **89 FE, davon 88 bestätigt und FE-56 offen**. F2 enthält **66 UC**. Dokumente sind weiterhin Prüfentwürfe; bestätigte Einzelentscheidungen sind keine Gesamtabnahme.

- V1: voneinander isolierte Benutzerkonten, installierbare PWA, eigene zentrale EU-Cloud ohne erforderlichen privaten Dauer-PC. Getrennte Administration, serverseitige Rechteprüfung; Adminrolle allein erlaubt kein Lesen privater Inhalte (S1/N2).
- Kalender außen strikt lesend; interner Kalender getrennt. Importe und KI-Kalenderänderungen vor Speicherung bestätigen; manuelles direktes Speichern verlangt keine künstliche zweite Bestätigung (P1/P2/S1).
- Sensible Dokumente besonders schützen; private Schlüssel nicht im Klartext an Backend/Admins. Gesondert freigegebene minimale temporäre Klartextverarbeitung ist keine durchgängige Ende-zu-Ende-Verschlüsselung (S1/S2/N2).
- Nur geeignete ausdrücklich freigegebene externe Integrationen; URLs berechtigen weder zur Installation noch Ausführung unbekannter Konnektoren. Anbieterabonnement bedeutet kein automatisches API-Recht (S1).
- Vier zuletzt integrierte Entscheidungen L-08/L-04/L-09/L-02 betreffen adaptive Wiederholung mit kontrollierter Reihenfolgeänderung, persönliche Erinnerungsregeln (UC-65), Studienvorgabenabgleich (UC-66) und optionalen ablenkungsarmen Lernmodus. Inhalt, Grenzen und Belege: E3.11–16 und Entwicklungszuordnungen.

## Offene Entscheidungen und Status

**FE-56 bleibt offen:** keine automatische Hochschulpost-/Inbox-Lesefunktion in V1. Technische Nachweise/Parameter aus S1.19 und S2.17 bleiben offen; insbesondere konkrete Provider, Verfahren für Schlüssel/Recovery, sichere PWA-/Offline-Fähigkeiten, Betriebs-/Lösch-/Backupnachweise sowie messbare Qualitäts- und Lizenznachweise. Die [Entscheidungsmatrix](../spec/ENTSCHEIDUNGSMATRIX.md) dokumentiert jetzt alle 25 DEC-V1 einschließlich ergänzter Varianten und Soll-Abnahmen; weitere fachliche Präzisierungen und der vollständige Meilensteinplan bleiben offen. Keine offenen Fragen durch Agentenannahmen schließen.

**Architektur:** ADR-Konvention vorhanden, keine finale Framework-, Datenbank-, Hostinganbieter- oder KI-Modellwahl. [S3](../spec/S3-inbetriebnahme.md) liegt als fachlicher Prüfentwurf vor; keine Betriebsaufnahme oder technische Prozedur wurde ausgeführt. DEC-48 priorisiert Oracle Cloud Infrastructure zur späteren Bewertung; Alternativen bleiben bei fehlender Eignung offen, kein Anbieter endgültig ausgewählt. DEC-49 verlangt verschlüsselte EU-Sicherung unabhängig vom Primäranbieter mit sicheren Schlüsseln/Rechten und periodischen verifizierbaren Restore-Proben. [ADR-0004/0005](../ARCHITECTURE_DECISIONS.md) halten Rahmen und offene Verfahren fest. Keine externen Accounts, Cloudinfrastrukturtests, Cloudressourcen oder Ausgaben sind autorisiert; RPO/RTO, Frequenz und Retention bleiben offen.

**Historischer Entwicklungsstand Mission 8:** Am Mission-8-Ausgang ausschließlich Dokumentation und `.gitignore`. Jetzt experimenteller [Frontend-Prototyp](../../prototypes/frontend/README.md) mit synthetischen Daten: acht UIbereiche, DE/FR/EN, Themes und lokale Interaktionen. Build/Lint/Format, 7 Unit- und 9 Chromium-Szenarien tatsächlich bestanden; [Prüfbericht](../design/PROTOTYPE_REVIEW.md). Keine operative Produktfunktion, echte Authentisierung/Kontoisolation, Backend, KI, Sync oder Produktfreigabe; keine App-CI eingerichtet. Frühe Dokumentprüfungen ersetzen diese eng begrenzten neuen UIbelege nicht und umgekehrt.

## Sicherheits- und Kostengrenzen

Keine Geheimnisse, privaten Lernmaterialien oder personenbezogenen Echtdaten ins öffentliche Repository. Nachvollziehbare Nutzerentscheidungen, Rechte-/Kontentrennung und geschützte Dokumente sind verbindlicher Rahmen. Externe Datenverarbeitung erfordert passende ausdrückliche Freigabe. Kein verpflichtender kostenpflichtiger KI-API-Zugang; kostenlose kommerziell geeignete Software-/Modelllizenzen bevorzugen, Sicherheit erhalten.

**Künftiger Vergleichsrahmen: bis zu 20 EUR brutto pro Monat. Keine Ausgabe genehmigt.** Mission 7 ersetzt ausdrücklich die frühere 10-EUR-Hypothese aus PACE/Mission 2–6; historische Rechnungen bleiben als solche erhalten. [ADR-0006](../ARCHITECTURE_DECISIONS.md#adr-0006--persönlicher-qualitätsfokus-und-vergleichsrahmen-aus-mission-7) dokumentiert persönliche Qualitätspriorität bei unverändertem V1-Multiuserziel, keine Buchungs-, Kontoeröffnungs- oder Betriebsfreigabe. Keine kostenpflichtigen Dienste oder Infrastruktur aktivieren.

## Auftragsumfang und nächste Schritte

Historisch: Mission 8 autorisierte ausdrücklich lokalen experimentellen Frontendcode, notwendige kostenfreie geprüfte Installationen, Lockfile, UItests und Captures sowie zugehörige Dokumentation mit Commit/normalem Push auf derselben Spezifikationsbranch zur Aktualisierung von PR #1. Der vollständige Auftrag umfasst 13 Abschnitte. Kein Merge, main unverändert, keine echte KI/Backendauth, Cloudressource, Account, Ausgabe oder Deployment. Fachentwürfe Zur Prüfung; technische Empfehlungen zur Entscheidung, Prototyp experimentell. Die frühere Nichtimplementierungsgrenze der Mission 7 ist für diesen konkreten UIumfang durch den neueren Auftrag ersetzt.

**Aktueller Untersuchungsstand:** Modularer Kern mit PostgreSQL, begrenzten separaten Workern und austauschbaren KI-Adaptern empfohlen; Vite/React + FastAPI, llama.cpp/kleine Qwen3-Kandidaten und selbst gehostete Identitätsoptionen zu prüfen. OCI zuerst bewerten; Hetzner/Scaleway echte Vergleichsoptionen. Keine komplette kostenlose Multiuser-KI nachgewiesen. Primärcloudpreise/-quoten und viele konkrete Gewichtslizenzen bleiben nicht verifiziert (Netzwerk-403); offizielle GitHub-Quellen belegen u. a. Softwarelizenzen, Releaseweiterleitungen und R2-Standardpreise/EU-Jurisdiktion. Gesamte R2-Vertrags-/Datenschutzlage noch offen. Gewichtete Scores sind transparente Hypothesen, keine Auswahl; Quellen-, Angebots-, Lizenz- und Benchmarklücken vor Entscheidung schließen.

**Aktueller Qualitätsstand:** NFR-01..25 und SEC-01..27 fachlich mit Ziel, Geltung, Methode, Abnahmekriterium, Beleg, Abhängigkeiten und offenen Parametern ausgearbeitet. [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md): REL-A01/05/07/13/16/18 zusätzlich, insgesamt 46. [Referenzrahmen](../quality/REFERENZRAHMEN.md): ASVS 5.0.0, LLM Top 10 2026 und API Top 10 2023 über offizielle Projektquellen belegt; WCAG-Normtext, NIST- und DSGVO-Aktualitätsprüfung durch Zugriffsverweigerung offen. WCAG 2.2 AA bleibt zu bestätigendes Ziel. [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md) bündeln künftige Nachweise; [S3](../spec/S3-inbetriebnahme.md) ordnet sie 18 Veröffentlichungsschritten, Zuständigkeiten, Rollout-/Rückwegen, Incidentverfahren und 20 Soll-Abnahmen zu. 14 O-S3-Arbeiten bleiben offen. Die 46 Produktkontrollen sind nicht vollständig implementiert/getestet (begrenzte Prototypevidenz siehe nachfolgende Mission 9); Grenzwerte, technische Entscheidungen, pädagogische Rubriken und menschliche Freigaben fehlen weiterhin. Dokumente bleiben Zur Prüfung; der Kontext erteilt keinen Folgeauftrag.

Die Übernahme der 40 Release-Kontrollen vom 22.10.2026 bleibt als historische Kontextänderung im [Protokoll](CONTEXT_CHANGELOG.md) und in E3.18 nachvollziehbar; sie ist kein bestandener Produkttest oder Zahlungsumfang.

Arbeitsregeln: [AGENTS.md](../../AGENTS.md), [Workflow](WORKFLOW.md). Übergaben und Kontextänderungen verwenden die dort verlinkten Vorlagen und das [Protokoll](CONTEXT_CHANGELOG.md).

## Aktuelle Machbarkeitspräzisierungen Mission 6

[Neue Quellen/Prüfung](../architecture/MACHBARKEITSPRUEFUNG.md): Keycloak Link/Generator-OTP nicht mit E-Mail-OTP gleichsetzen; authentik-Recoveryreaktivierung und Anti-Enumeration gezielt prüfen. R2 dokumentiert entfernbare Bucketlocks; restic-Prune/Retention/Schutz gegen kompromittierte Credentials abstimmen. Host-/Modellhost-/Vertragsseiten trotz neuer offizieller API-/Repositorywege teils unlesbar. Keine Preise, garantierte Zuteilung oder Gewichtsrechte erfinden. [Ressourcenrechnungen](../architecture/RESSOURCENBEDARF.md) sind keine Messung; [T01–T09](../architecture/BENCHMARKPLAN.md) nicht ausgeführt. [14 TECH-O](../architecture/ENTSCHEIDUNGSVORLAGE.md) in A/B/C/D gegliedert, keine genehmigt. Historischer Befund aus Mission 6: persönlicher begrenzter Prototyp theoretisch prüfbar, vollständige Multiuser-V1 auf Always Free oder unter damaligen 10 EUR unbewiesen; auch der neue 20-EUR-Vergleichsrahmen erbringt keinen Leistungsnachweis. 89 FE, FE-56 offen, 66 UC, 25 DEC-V1, DEC-48/49 und 46 REL unverändert.


## Vorbereitung aus Mission 7

[Neue Übersicht](../development/INTEGRATION_ROADMAP.md): hochwertige persönliche Lernassistenz zuerst, V1-Registrierung/Isolation/Admin/Serverflags unverändert, keine Zahlung genehmigt. [Design](../design/DESIGN_SYSTEM.md) mit Token/Themes/Responsive; kleine UIauswahl, keine Installation. [Codex/Claude](../ai-tooling/CODEX_CLAUDE_WORKFLOW.md) trennt Formate; drei lokale Markdown-Skills strukturell vorbereitet, tatsächliche Invocation/Discovery nicht getestet. Keine aktiven Hooks/MCP-/Agentenkonfigurationen.

[APIvergleich](../integrations/LLM_API_COMPARISON.md): Cloudflare-/OpenRouter-Dokumente belegen begrenzte Freeangebote, HF-Free ohne Credits laut neuer offizieller Quelle; Groq/Gemini/Mistral/Cerebras kommerziell/vertraglich weiter nicht verifiziert. Keine Liveinferenz. [Lizenzen](../development/DEPENDENCY_SELECTION.md) an konkreten Quellrevisionen gelesen, vollständige Paket-/Transitiv-/Modellrechte vor Einführung offen. Kleinere Adapter/PG-Volltext und menschliche pädagogische Evaluation empfohlen, keine Stack-/Hosting-/APIwahl. Bestehende T01–T09 nicht ausgeführt; 14 TECH-O weiter offen. Finanzielle Tragfähigkeit auch unter neuem 20-EUR-Rahmen nicht nachgewiesen.


## Tatsächlicher UIstand nach Mission 8

[ADR-0007](../ARCHITECTURE_DECISIONS.md#adr-0007--lokale-frontendprobe-aus-mission-8), [Prüfbericht](../design/PROTOTYPE_REVIEW.md) und [lokale Anleitung](../../prototypes/frontend/README.md) trennen ausführbare Oberfläche von Fach-/Sicherheitsimplementierung. 17 axeanalysen ohne gemeldeten Verstoß, 18 lokale Bilder erzeugt und visuell geprüft; vier versioniert. Rückfokus/Tabzyklus von Dialogen nach Testbefund korrigiert. Alle 46 REL einzeln über vollständige Gruppierung auf Prototypevidenz/Nichtumfang eingeordnet, keine gesamte Produktkontrolle bestanden erklärt. Keine externen Laufzeitrequests im geprüften Hauptparcours; nur Sprache/Theme gespeichert. Alle FE/UC/DEC bleiben erhalten, FE-56 und 14 TECH-O offen. Die vollständige V1-Leistung und Kosten unter 20 EUR sind weiterhin nicht nachgewiesen. Nächster Schritt: Eigentümerreview, anschließend separat genehmigte sichere Backendtranche, kein automatischer Auftrag.


## Aktuelle lokale Backendprobe nach Mission 9

Neuer vollständiger Nutzerauftrag Mission 9 autorisiert lokale reversible Backendimplementierung, notwendige geprüfte Open-Source-Pakete, synthetische Tests und Commit/normalen Push ausschließlich auf bestehender Spezifikationsbranch. Kein Cloud-/Account-/Kosten-/Merge-/Deploymentauftrag und keine neue Branch/PR. [ADR-0008](../ARCHITECTURE_DECISIONS.md#adr-0008--lokale-backendprobe-aus-mission-9) und [Anleitung](../../prototypes/backend/README.md): FastAPI/Python mit direktem psycopg und PostgreSQL als Experiment, keine endgültige Auswahl. Argon2id, begrenzte widerrufbare Hashsitzungen, Kontofilter, aktuelle Rollen-/Serverflags und eingeschränkte DBrechte implementiert. Normale Anmeldung bleibt 503; keine Seeds und kein realer Super Admin. OTP-/Geräteverifikation/MFA/Recovery fehlen; nur interne Testfixtures autorisieren künstliche verifizierte Identitäten gegen separate Testdatenbank. Browserintegration gesperrt, Frontend unveränderte Demo.

[Prüfbericht](../development/BACKEND_PROTOTYPE_REVIEW.md): 44 lokale Tests einschließlich realem PostgreSQL, strict Mypy, Ruff/Format, HTTP-Smoke; Python- und npm-Audit ohne bekannte Schwachstellen am Prüftag. UIregression erneut sieben Unit-/neun Browserszenarien bestanden. Alle 46 REL einzeln mit begrenzten Belegen/Restlücken eingeordnet, keine Gesamtabnahme. Testclient meldet nicht unterdrückte HTTPX-Deprecation; native/Imageinventur, produktive Konkurrenzfälle und Lieferkette weiter offen. Flüchtige DBspeicherung, Softdelete und APItests belegen keine dauerhafte Speicherung, finale Löschung, unabhängige Sicherung oder Wiederherstellung. 89 FE, 66 UC, 25 DEC-V1, DEC-48/49 und alle Sollabnahmen unverändert, FE-56 und 14 TECH-O offen. Nächste Empfehlung: Eigentümerreview und gesonderte Identitätsprobe vor Browseranschluss.
