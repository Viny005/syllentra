# Architekturmuster — Nutzen, Aufwand und Einführung

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Leitplanke

Vertiefung des [bestehenden Architekturvergleichs](../architecture/README.md), keine zweite Stackentscheidung. Ein modularer Kern mit begrenzten isolierten Workern ist Untersuchungsempfehlung, kein implementiertes Muster. Tabellen beschreiben Entwurfsabwägungen auf Basis der vorhandenen Fach-/Schutzanforderungen, keine Herstellerbenchmarks. Methoden dürfen Sicherheitsgrundlagen vereinfachen, aber nicht umgehen.

## 2. Mustervergleich

| Muster | Problem / Vorteil | Komplexitätskosten | Syllentra-Anwendung | Einfachere Alternative | Geeigneter Zeitpunkt |
|---|---|---|---|---|---|
| Modular Monolith | Zusammenhängende Regeln bei wenigen Releases/Transaktionen | Modulgrenzen trotz gemeinsamer DB diszipliniert halten | Konto, Studium, Gespräche, Pädagogik als begrenzte Module | Kleiner einzelner Kern mit klaren Funktionen | Erste genehmigte Kernimplementierung; keine Microservices vor Lastbeleg |
| Hexagonal / Ports and Adapters | Fachlogik von Technik entkoppeln, separat testbar | Zusätzliche Schnittstellen/Zuordnung, Überabstraktion vermeiden | KI-/Datei-/Kalender-/Identitygrenzen | Direkte Funktionen mit kleiner injizierter Schnittstelle | An variablen/externen Grenzen früh; kein Interface für jede Klasse |
| Dependency Injection | Austauschbare Abhängigkeiten und deterministische Tests | Lebensdauer/Transaktionen müssen klar sein | Uhr, Rechteprüfung, Provider, Quoten | Explizite Funktionsparameter/Konstruktoren | Im kleinen Umfang ab erster testbarer Fachlogik; kein DIcontainer nötig |
| Repository | Einheitliche persistente Zugriffe/Schutzfilter | Generisches CRUD kann Fachsemantik verstecken | Konto-/quellgebundene Datenabfrage | Kleine konkrete Queryfunktionen | Bei wiederkehrenden Abfragen; keine Doppelabstraktion über ORM |
| Unit of Work | Mehrere Änderungen atomar behandeln | Transaktionsgrenzen/Nesting/Fehlerpfade | Bestätigte Lernnotiz + Beleg + Auftrag | Bestehende DBtransaktion | Nur bei mehreren zusammengehörigen Effekten |
| Domain Events | Nachgelagerte Fachreaktionen entkoppeln | Reihenfolge, Handlerfehler, Nachvollziehbarkeit | Neuer Prüfungsrevision folgt Hinweisneuberechnung | Direkter Funktionsaufruf in klarer Transaktion | Bei mehreren unabhängigen Reaktionen, nicht sofort Eventbus |
| Transactional Outbox | DBcommit und ausgehender Job nicht auseinanderlaufen lassen | Zusteller, Retry, Deduplikation und Bereinigung | Erinnerung/Importfolge trotz Prozessabbruch | Jobzeile in gleicher DBtransaktion | Sobald DBänderung dauerhaft externe/asynchrone Wirkung benötigt |
| State Machine | Zulässige Übergänge explizit, Abbruch/Entzug prüfbar | Übergangstabelle und Versionierung | Importvorschau → Bestätigung → Verarbeitung; Lösch-/Releasezustände | Enum + geprüfte Übergangsfunktion | Vor erstem mehrstufigem sensiblen Workflow |
| Idempotency Keys | Retry/Doppelklick ohne doppelte Wirkung | Scope, Payloadbindung, Ablauf und Ergebnisaufbewahrung | Jobannahme/Terminübernahme/Toolaktion | Eindeutiger fachlicher Schlüssel | Vor erster wiederholbaren Mutation; keine Exactly-once-Zusage für Fremddienste |
| Optimistic Concurrency | Parallele Geräte überschreiben nicht still | Konfliktanzeige/-auflösung | Notiz-/Profil-/Kalenderrevision | Explizite Versionsprüfung | Ab Mehrgeräteänderung, fachlich konfliktbewusst |
| CQRS | Unterschiedliche Schreib-/Leseanforderungen trennen | Projektionen, Konsistenzverzug, weitere Datenkopien | Erst später belegte Reportingengpässe | Gleiche DB + passende Readqueries | Zurückstellen; keine Event-Sourcing-Pflicht |
| Rate Limiting | Missbrauch/CPU-/Kostenlast begrenzen | Globale/Konto-/Gerätezuordnung, faire Bursts | Login, Upload, KI, Suche | Kleine serverseitige Limits | Von Beginn der jeweiligen API; keine reine UIbremse |
| RBAC + ABAC | Rolle plus Objekt/Zweck/Zustand korrekt schneiden | Einheitliche Policy/Tests/Entzug | Adminflags, Eigentum, Supportscope, Quelle | Zentraler expliziter Policycheck | Grundkern vor Daten-/Adminzugriff; kein Clientrollenvertrauen |
| Feature Flags | Unfertiges schrittweise kontrolliert aktivieren | Version/Abhängigkeiten/Rollback/Altclients | Eigener Preview/Testerkreis, spätere Nutzer | Serverseitige boolsche Konfiguration | Früh mit Autorisierung, nicht nur Menüverstecken |
| Audit Logging | Sensible Handlungen zurechenbar und überprüfbar | Private endliche Aufbewahrung, Manipulationsschutz | Admin-/Freigabe-/Integrationsentscheidung | Kleine strukturierte Ereignistabelle | Bei erster sensibler Mutation; niemals Prompt-/Secretarchiv |
| Structured Logging | Fehler/Korrelation ohne frei formatierte Inhaltssammlung | Schema, Redaction, Rotation, Zugriff | Jobstatus, Fehlercode, Korrelations-ID | Strukturierte lokale endliche Logs | Früh; keine externe Monitoringplattform nötig |
| Retry / Backoff | Kurzzeitfehler sicher behandeln | Jitter/Attempts/Abbruch/Retry-After, doppelte Wirkung | Lesender Abruf und klar idempotenter Job | Fehler anzeigen / manuell wiederholen | Nur bei transienten Fehlern; Berechtigung vor jedem Versuch |
| Circuit Breaker | Dauerfehler nicht verstärken | Schwellen/Half-open-Zustand/Gemeinschaftslast | Instabiler erlaubter Modellendpoint | Kurzer Timeout + geringe Versuche | Nach beobachteter Wiederholungsstörung; kein automatischer Außenfallback |
| Queue Worker | Lange Jobs ohne Requestblockade, begrenzte Fairness | Leases, aktuelle Rechte, Stop, Deduplikation, Wiederanlauf | PDF/ASR/KI/temporäre Bereinigung | Begrenzter synchroner Job nur für kleine sichere Aufgaben | Vor langen/untrusted Arbeiten; PGjobkandidat vor Zusatzbroker prüfen |
| Provider Adapter / Strategy | Anbieter-/Aufgabenwahl aus Fachlogik heraushalten | Capability-/Fehler-/Kostenabweichungen testen | llama.cpp/Ollama/erlaubte API | Ein kleiner konkreter Adapter | Erster KIvertrag; Strategie serverseitig, kein User-URLexecutor |
| Capability Routing | Nur tatsächlich geeignete Modelle verwenden | Fähigkeitskatalog/Güte-/Versionspflege | Schemaausgabe, Sprache, ASR statt blindem Namenrouting | Explizite Auswahl aus kleinem freigegebenem Katalog | Sobald mehrere erlaubte Modelle/Tasks bestehen |
| Timeouts / Budget Guard | Unbegrenzte Dauer/Verbrauch verhindern | Reservierung, Streamingabbruch und Abrechnung | Input-/Output-/Queue-/Geldbudget | Kleine harte Obergrenzen | Vor jedem teuren/externen Pfad; Kostenfreigabe unabhängig |
| Backend for Frontend | Gerätespezifische Aggregation kann Roundtrips senken | Zusätzliche Schicht/Verträge/Angriffsfläche | Nur falls UI messbar zu viele berechtigte Datenabfragen braucht | Bestehende autorisierte API aggregiert | Später bei Messbeleg, kein zweites Nodebackend nur für Muster |

## 3. Nicht empfohlen ohne Nachweis

Kein Event Sourcing, Kubernetes, verteilte Microservices, universeller Agentenorchestrator oder separate Vektordatenbank aus Prinzip. Muster nicht als Paketliste missverstehen. **Frühe Pflichtziele** sind Isolation, Autorisierung, Schutz-/Löschlebenszyklus, sichere Konfiguration, Fehler-/Kostenbegrenzung und testbare Grenzen. Konkrete Bibliotheken bleiben separat entscheidungspflichtig. [Adapter](../integrations/AI_PROVIDER_ADAPTERS.md), [Integrationsfolge](INTEGRATION_ROADMAP.md), [N2](../spec/N2-querschnittskonzepte.md).
