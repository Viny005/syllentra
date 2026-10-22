# E2 — Glossar

**Projekt:** Syllentra AI\
**Version:** 0.4\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

## E2.1 Verbindliche Begriffsabgrenzung

Dieses Glossar erläutert die Verwendung in [P1](P1-ziele-rahmenbedingungen.md), [P2](P2-architekturueberblick.md) und [S1](S1-nachbarsysteme.md). Es trifft keine neuen Produktentscheidungen.

| Begriff | Bedeutung |
|---|---|
| Anwendungsdatenzugang | Zugriff auf eigene fachliche Inhalte nach Verifikation; beschränkte Registrierung/Recovery davor ist kein allgemeiner Zugang. |
| Bestätigung | Bewusste Entscheidung zu konkreter Fassung und Wirkung. Direkte manuelle Speicherung ist bereits eine bewusste Nutzeraktion; nicht jede Eingabe braucht eine zweite Bestätigung. |
| Bestätigte fachliche Entscheidung | Vom Auftrag festgelegte Anforderung; weder fertig implementiert noch vollständige Dokumentabnahme. |
| Zur Prüfung | Dokument ist zur Prüfung vorgelegt; keine eigenmächtige Freigabe durch Commit oder Audit. |
| Nutzerkonto / Mandant | Isolierter persönlicher Eigentumskontext; V1 hat mehrere Konten ohne gemeinsame private Teamräume. |
| Super Admin | Genau eine globale Eigentümerrolle; ausschließlich sie verwaltet sekundäre Administratoren, ohne dadurch private Lerninhalte lesen zu dürfen. |
| Sekundärer Administrator | Vom Super Admin begrenzt zugewiesene Rolle; keine Selbstbeförderung und keine Verwaltung anderer Administratoren. |
| Supportfreigabe | Freiwilliger zeit-, zweck-, personen- und objektbegrenzter Zugang, standardmäßig lesend und widerrufbar. |
| PWA | Installierbare Webanwendung mit eigener Identität auf unterstützten Browser-/OS-Konfigurationen; keine Zusage beliebiger nativer APIs. |
| Syllentra-Cloud | Eigene zentrale interne Daten-/Verarbeitungsumgebung mit EU-Hauptdaten und Sicherungen; unabhängig vom persönlichen PC. |
| Externer Speicher | Optionaler Nachbar NB-10 für ausgewählte fremde Dateien/Ordner nur lesend; kein notwendiger interner Syllentra-Betrieb. |
| Integration / Konnektor | Geprüfte offiziell unterstützte Verbindung mit tatsächlichen Fähigkeiten, minimalen Rechten und freiwilligem Scope. Eine URL allein installiert nichts. |
| Verbindungsstatus | Tatsächlicher Stand wie verbunden, abgelaufen, nicht verfügbar oder widerrufen; letzter belegter Erfolg ist davon getrennt. |
| Scope | Expliziter erlaubter Umfang nach Anbieter, Zweck, Datenkategorie und Quelle; bei GitHub einzelne oder alle eigenen öffentlichen Repositories. |
| Externe Synchronisation | Standardmäßig manueller Quellenabgleich; Automatik nur nach verbindungsspezifischem Opt-in mit Frequenz. |
| Interne Gerätesynchronisation | Abgleich eigener autorisierter Geräte mit zentraler Cloud, einschließlich Konflikten und Löschungen; nicht NB-10-Opt-in. |
| Serversitzung | Zeitlich begrenzter autorisierter Serverzugang; lokale Gerätesperre und OS-Entsperrung sind getrennte Zustände. |
| Kontorecovery | Wiedererlangung des Kontozugangs über verifizierte E-Mail und persönlichen Einmalcode; liefert keine Dokumentenschlüssel. |
| Schlüsselrecovery | Persönliche Wiederherstellung sensibler Dokumentenschlüssel, unabhängig von Konto- und Adminrecovery; technisches Verfahren offen. |
| Sensible Cloudanalyse | Konkrete freigegebene Verarbeitung minimaler entschlüsselter Ausschnitte in der eigenen Cloud; Server sieht dafür temporär Klartext, erhält keine privaten Klartextschlüssel. |
| Schutzvererbung | Ableitung und Nebenansichten erhalten mindestens den Schutz ihrer Quelle; Herabstufung/Teilen braucht explizite Entscheidung. |
| Quellrevision | Belegbarer externer Stand mit Quellenkennung und Revision/Hash/Zeit samt Unsicherheit; gleicher Dateiname reicht nicht. |
| Ableitung | Quellenbezogenes Ergebnis wie Zusammenfassung, Lernkarte oder Erinnerung; weder Original noch dessen amtlicher Ersatz. |
| Historie / Erinnerung | Nachrichtenverlauf, pädagogisches Langzeitwissen und private Integrationshistorie sind getrennte Datenbestände mit eigenen Zwecken und Löschregeln. |
| Papierkorb | Privater zeitlich begrenzter Löschzwischenstand mit Wiederherstellung; nicht Archivierung. |
| Löschmarkierung / Non-Resurrection | Minimaler inhaltsfreier Nachweis endgültiger Löschung verhindert ungewollte Wiederbelebung durch Offlinegeräte, Historie oder Backup. |
| Funktionsfreigabe | Serverseitig geprüfte Verfügbarkeit für Zielgruppen; verborgen, bald, Test und öffentlich sind keine frei umgehbaren UI-Zustände. |
| Veröffentlichungsfassung | Geprüfter Entwurfs-/Test-/Termin-/Releasezustand einer unterstützten Funktion oder Konfiguration; Ankündigung erst bei tatsächlicher Verfügbarkeit. |
| Idempotenz / Deduplizierung | Wiederholung derselben fachlichen Wirkung erzeugt keine zusätzliche Wirkung; unbekanntes Ergebnis zuerst prüfen. Keine pauschale physische Genau-einmal-Garantie fremder Zusteller. |
| FE-56 | Weiterhin offene Entscheidung zur optionalen Inboxlektüre; ausgehende OTP-/Sicherheitsmails erlauben keine automatische Hochschulpostlektüre. |

## E2.2 Ergänzende Migrationsbegriffe

| Begriff | Bedeutung |
|---|---|
| Portabilitätspaket | Versionierter eigener Inhaltsbestand mit Manifest, zulässigem Umfang und Schutz, ohne aktive Anmeldesecrets oder Privilegien; nicht gleich betrieblicher Sicherung. |
| Exportmanifest | Fachliches Inhalts-/Versions-/Abhängigkeits-/Abdeckungsverzeichnis; Integritätsmerkmal ist kein Konto- oder Eigentumsnachweis. |
| Syllentra-Reimport | Kontrollierte Übernahme eines kompatiblen eigenen Pakets nach aktueller Vorschau und konkreter Bestätigung; kein universeller Drittadapter. |
| Migrationsvorschau / Delta | An Quell-/Zielstand gebundener Unterschiedsausweis mit Auswahl, Konflikten und Ausschlüssen; geänderte Grundlage erfordert neue Bewertung. |
| Fachliche Teilwirkung | Kleinste sicher nachvollziehbare bestätigte Inhaltseinheit mit tatsächlichem Ergebnis; Wiederaufnahme erzeugt keine zusätzliche gleiche Wirkung. |
| Aktueller Kontrollstand | Belastbare heutige Konto-, Lösch-, Entzugs- und Rechteinformationen, die auch beim Restore eines älteren Bestands gelten. |
| Cutover | Kontrollierte Freigabe/Umschaltung auf einen nachgewiesen konsistenten und zulässigen Versions-/Betriebsstand. |
| Vorwärtskorrektur | Geprüfter Weg zu einem sicheren neueren Stand, wenn eine alte Fassung nicht gefahrlos rückspielbar ist; keine Umgehung heutiger Lösch-/Rechtegrenzen. |
| RPO / RTO | Noch festzulegende technische Wiederherstellungsziele für tolerierbaren Datenverlust beziehungsweise Wiederanlaufzeit; keine bereits zugesagten Zahlen. |
| MIG / AT-S2 / DEC-V1 | S2-interne Migrationsregel / künftiger S2-Abnahmefall / temporärer Post-S1-Auditbezug; keine neuen offiziellen FE-Kennungen. |

Verträge und offene Nachweise: [S2](S2-datenmigration.md). Eine Wiederherstellungsoption in der Spezifikation beweist keine heute implementierte Produktfähigkeit.

## E2.3 Begriffe der vier bestätigten Fachentscheidungen

| Begriff | Bedeutung |
|---|---|
| Hybride Wiederholung | Zeitliche Wiederholungsregeln plus evidenzabhängige Auswahl anhand Lernziel, Antworten, Schwierigkeiten, Prüfungsnähe und Zeit; konkrete Formel offen. |
| Pädagogische Lernreihenfolge | Persönliche nichtterminierte Reihenfolge/Priorisierung von Lernschritten; keine Buchung, Verschiebung oder Löschung im Kalender. |
| Lernheftautomatik | Ausdrücklich persönlich aktivierte automatische Änderung dieser Reihenfolge mit Grund, Verlauf, Abschaltung und sicherem Undo; keine Vorschlagsannahme für Kalender. |
| Plan-Undo | Neue konfliktgeprüfte Rücknahme einer konkreten pädagogischen Reihenfolgeänderung unter Erhalt jüngerer gültiger Lernfortschritte und manueller Termine. |
| Erinnerungsregel / pädagogische Erinnerung | Fälligkeits-/Kanal-/Ruhezeitvorgabe DM-77 versus personalisiertes Langzeitwissen DM-33; getrennte Zwecke und Löschfolgen. |
| Hinweis / Zustellnachweis | Logische geschützte Nutzerinformation DM-52 versus tatsächliche externe Zustellversuche DM-78; Providerannahme beweist weder Auslieferung noch Lesen. |
| Geltende Studienvorgabe | Belegte Regel einer Quellenfassung für die konkrete Hochschule, den Studiengang, die Ordnung, Kohorte und Übergangslage; neuer ist nicht automatisch anwendbar. |
| Soll-Ist-Abgleich | Vergleich bestätigter anwendbarer Anforderungen mit eigenen belegten/offenen Studienleistungen; keine amtliche Anerkennung. |
| Ablenkungsarmer Lernmodus | Freiwillige jederzeit beendbare Minimalansicht mit optionaler Zeitbegrenzung, zurückgestellten nicht dringenden Hinweisen und zugänglicher Bedienung; kein Leistungs-/Zeitdruck. |
| Fortschrittsaussagen | Bearbeitet, Verständnis überprüft, Wissensstand geschätzt und Kompetenz nachgewiesen sind eigenständige belegbezogene Aussagen, keine automatische Stufenleiter. |

UC-65 verwaltet Erinnerungsregeln/Zustellnachweise; UC-66 den geltungsgeprüften Studienabgleich. L-08, L-04, L-09 und L-02 sind die bestätigten Auftragspunkte vom 19.10.2026, keine neuen FE-Kennungen. [F2](F2-anwendungsfaelle.md) enthält ihre Vorgänge, [Entwicklungszuordnungen](ENTWICKLUNGSPLAN.md) den begrenzten Meilensteinstand.

## E2.4 Begriffe der dokumentarischen Konsolidierung

| Begriff | Abgrenzung |
|---|---|
| Wissenskarte | Freiwillige einfache Ansicht vorhandener eigener Themen-/Quellenbeziehungen; kein automatischer Kompetenztransfer und keine Pflichtnavigation. |
| Sitzungsrückmeldung / Sitzungsbilanz | Freiwillige manuelle Selbstaussage gegenüber einer optionalen Sicht auf tatsächliche Sitzungsbelege; keine amtliche Leistung und kein erfundener Messwert. |
| DEC-48 / DEC-49 | Bestätigte Hostingbewertungspriorität beziehungsweise unabhängige verschlüsselte Sicherung; getrennt von FE und DEC-V1, keine technische Anbieterwahl oder Betriebsfreigabe. |
| Anbieterunabhängige Sicherung | Verschlüsselter EU-Speicher außerhalb des Primäranbieters mit sicheren Rechten/Schlüsseln und verifizierbarem Restore; zusätzliche Region desselben Anbieters allein reicht nicht. |

[Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md), [ADR](../ARCHITECTURE_DECISIONS.md) und [S2](S2-datenmigration.md) enthalten Quellen, Grenzen und offene Nachweise.
