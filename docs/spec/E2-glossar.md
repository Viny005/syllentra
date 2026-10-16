# E2 — Glossar

**Projekt:** Syllentra AI\
**Version:** 0.1\
**Stand:** 16.10.2026\
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
