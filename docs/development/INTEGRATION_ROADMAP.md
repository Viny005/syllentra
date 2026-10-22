# Integrationsfolge — von Vorbereitung zu prüfbaren Funktionen

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Bestätigter Rahmen und ausdrückliche Nichtfreigaben

Mission 7 bestätigt Priorität einer hochwertigen persönlichen Lernassistenz und für **künftige Vergleiche** bis 20 EUR brutto/Monat anstelle der früheren 10-EUR-Hypothese. Keine Ausgabe, kein Account oder Deployment. V1-Ziel Registrierung/Multiuser, strikte Kontoisolation, getrennte Administration und kontrollierte Aktivierung bleiben vollständig erhalten. Finanzierungsbeiträge später untersuchen, **kein V1-Zahlungssystem genehmigt**. KIqualität/UX/Leistung nach Belegen verbessern, keine Schutzkürzung für „persönlichen Prototyp“.

## 2. Abhängige Phasen als Vorschlag

Phasen A–F sind neue **Orientierung**, keine Ersetzung/Umnummerierung des unvollständigen Meilensteinplans. [Bestehende Zuordnungen](../spec/ENTWICKLUNGSPLAN.md) bleiben verbindlicher Teilstand: M2b grundlegende Projekte früh; M5 Noten/ECTS und interne UC-65-Regeln; M8 erweiterte Zustellung nur mit Rechten. Keine erfundenen Termine oder Gesamtmeilensteinfreigabe.

| Phase | Umfang | Voraussetzungen | Prüfbarkeit / Exitkriterium | Heute |
|---|---|---|---|---|
| A Entwicklungsfundament | AGENTS/CLAUDE, kleine deklarative Skills, Review-/Scope-/Quellenverfahren | Mission-7-Dokumentfreigabe, geprüfte Formate | Dokument-/Link-/Erhaltungsprüfungen; spätere echte Clientdiscovery separat | Dokumente/Skills vorbereitet, Invocation offen |
| B Design System | Token/Theme, wenige Grundkomponenten, Navigation/Responsive/A11y | Eigentümer bestätigt Richtung und TECH-O-03 bzw. isolierten Probeumfang | Kontraste, Zustände und echte Aufgabenpfade auf bestätigten Geräten/DEFR/EN; keine produktive Authumgehung | Lokale UIprobe durch Mission 8 autorisiert und umgesetzt; Review offen, keine Stackfreigabe |
| C Anwendungsfundament | Genehmigtes Front-/Backend, Auth/Registrierung, strikte Isolation, Konfig/Flags, separater Admin | Stack-/Auth-/Bootstrapentscheidung, technische Probe T01/T06/T09 separat; Datenschutz-/Schlüsselgates | A/B-/Direkt-/Altclient-/Entzugs-/Recoverytests, keine privaten Adminleserechte; anwendbare 46 REL | Kein Kern-/Backendcode, kein Produktnachweis; nur getrennte lokale UIprobe |
| D Akademische Basis | Profil, Semester/Module, grundlegende unabhängige Projekte, Quellen, Gespräche, interner Kalender, Notizen/Progression | Sicherer C-Kern, geprüfte Daten-/Migrations-/Löschverträge | Beziehungen/Herkunft/Revisionen/Sync/Export/Löschung, Kalender außen read-only, Bestätigung korrekt | Fachlich spezifiziert, nicht implementiert |
| E KI-Tutor | Begrenzte Modelladapter, Streaming, Rechtefilter-RAG/Zitate, kontrollierte Notizen/Übungen | Lizenz-/Artefakt-/Datengates, T02/T03/T09 und menschliche Fachrubrik; D-Quellmodell | DE/FR/EN-Güte/Quelltreue, Injection-/Budget-/Entzugnegativfälle; kein externer Fallback ohne Freigabe | Konzept/Tests geplant |
| F Medien / Vertiefung | Audio/ASR/TTS/Video, Wissenskarte, vertiefte Lernanalyse | Isolierte Parser/Medien, echte Sprach-/Stimmen-/Codec-/Schutzbelege, T04; zugängliche Alternative | Temporäre Bereinigung nach Erfolg/Fehler/Abbruch, Zeitquellen, erreichbare Textwege, realer Ressourcenbeleg | Keine Ausführung |

Sicherheitsgrundlagen sind keine späte Phase. DEC-49-/S3-Betriebsnachweise einschließlich unabhängigem verschlüsseltem Restore sind **vor jeder Produktveröffentlichung** nötig, auch wenn die Umsetzung nur C/D erreicht. Optionale Medien/Graphfunktionen dürfen hinter Serverflags später folgen; das bestätigt ihre fachliche Erfüllung nicht. V1-Ziel bleibt umfassender als ein begrenzter erster Technikversuch.

## 3. Erster sinnvoller Folgeauftrag

**Zuerst Mission-7-Vorschläge prüfen und einen engen Technikversuch definieren**: lokal isolierte, synthetische Komponenten-/Adapter-/Identitätsprobe ohne Cloud und ohne Echtdaten, nur ausdrücklich gewählte Tests aus T01/T02/T03/T06/T09. Vorab Eigentümer bestätigt Stackkandidat, genaue Installations-/Downloadliste mit Lizenz/Hash, Hardware, Daten, erwartete Nachweise und Abbruchgrenzen. Keine Installation oder Modellausführung aus diesem Plan ableiten. Vor einer Cloudprobe zusätzlich Account-/Regions-/Kosten-/Restoreumfang separat erlauben; Oracle gemäß DEC-48 zuerst untersuchen, unabhängig von hier vorgeschlagenen UIbibliotheken.

Persönlicher Qualitätserfolg als späterer Referenzpfad: synthetisches Modulmaterial → belegte Erklärung → überprüfte Notiz → passende Übung → nachvollziehbarer Kompetenzbeleg, auf Smartphone und Desktop in DE/FR/EN. Qualität und akzeptable Wartezeit vorher vereinbaren. Ressourcen-/Angebotslücken der Mission 6 schließen, bevor aus 20 EUR ein plausibles Hostingversprechen wird.


## Fortschreibung aus Mission 8

Der neue konkrete Eigentümerauftrag autorisiert eine lokale experimentelle UIprobe. Die früheren Nichtimplementierungs-/Nichtinstallationsaussagen dieses Mission-7-Studienstands sind historische Grenzen, keine Sperre des neueren Auftrags. [Code/Anleitung](../../prototypes/frontend/README.md) und [tatsächlicher UI-Prüfbericht](../design/PROTOTYPE_REVIEW.md) dokumentieren den begrenzten Fortschritt. Keine allgemeine Stack-/Bibliotheks-/Produktfreigabe; TECH-O-03 offen. Eigene CSS-Token und native Controls genügen für die Probe, daher keine Tailwind-/shadcn-/Richtext-/PDF-/Graph-/Kalenderinstallation. Fach- und Releaseziele bleiben vollständig bestehen, Backend-/Geräte-/Assistenztechnik-/Sicherheitsabnahmen offen.
