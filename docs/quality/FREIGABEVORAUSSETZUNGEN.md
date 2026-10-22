# Syllentra AI — fachliche Voraussetzungen für spätere Freigaben

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

## 1. Zweck und Grenze gegenüber S3

Dieses Dokument bündelt Anforderungen an Nachweise und Entscheidungen für die spätere Ausarbeitung von S3. Es beschreibt **keine Inbetriebnahmeprozedur**, keinen eingerichteten Betrieb und keine Freigabe eines Deployments. Ausgangspunkt sind [N1](../spec/N1-nichtfunktional.md), [N2](../spec/N2-querschnittskonzepte.md), [S2](../spec/S2-datenmigration.md), die [40 Originalkontrollen](RELEASE_READINESS_40.md) und [alle 46 Prüfprofile](RELEASE_KONTROLLMATRIX.md). Gegenwärtig fehlen Anwendung, technische Umsetzung und Produktprüfungen; keine Produktveröffentlichung ist abnahmefähig. Die Dokumente bleiben Zur Prüfung.

## 2. Vor erster Produktveröffentlichung

| Gate | Erforderlicher Umfang / Nachweis | Referenz |
|---|---|---|
| Fachlicher Umfang und Freigabeverantwortung | Aktive V1-Funktionen, unterstützte Geräte, Daten-/Nutzergruppen, menschliche Verantwortliche und offene Einschränkungen ausdrücklich bestätigen; keine erfundenen Freigaben aus Git-Merge/Push. | NFR-02/25; SEC-07/26 |
| Identität und Kontentrennung | Verifizierter Zugang, Rollen-MFA, Session-/Geräteentzug, sichere getrennte Recovery und kontoübergreifende Negativtests. Bei Administration sichere Erstbesetzung **genau eines** Super Admin und begrenzte Delegation vor Produktstart belegen. | REL-S03/04/05/06/09/19, REL-Q19 |
| Schutz der gesamten erreichbaren Oberfläche | HTTPS, Secretschutz, sichere Eingabe-/Ausgabeverarbeitung, minimierte Daten, private endliche Logs, gültige Rechte/Flags auch bei Direktaufruf, Jobs und Restore. Keine unfertige Funktion erreichbar, auch nicht über alte Clients/API. | REL-S01/02/07/08/10/14/15/16/18, REL-Q11/16/18 |
| Qualität und tragfähige Ressourcen | Last-/Latenz-/Kapazitätsziele, Quoten und Fehler-/Degradationsverhalten vor Tests bestätigen; unter realistischen Ressourcen messen. Kosten-/Lizenzprüfung; keine Pflicht-Pay-API und keine Ausgabe ohne Freigabe. | N1.10; REL-Q01/02/03/04/05/06/08/12/13/14/19 |
| EU-Datenschutz und Lebenszyklus | Verantwortliche, Zwecke/Grundlagen, Providerbedingungen, erforderliche Verträge und ggf. DSFA-/Transferprüfung; Schlüssel-, Retentions-, Export-/Lösch- und Derivatschutz nachweisen. | SEC-08..11/15/16/20/22/26/27; REL-Q11/16/20 |
| Unabhängige Sicherung und Wiederanlauf | DEC-49-konforme verschlüsselte unabhängige EU-Sicherung und tatsächlich geübte Wiederherstellung ohne Hauptanbieter, mit heutiger Lösch-/Rechtelage und bestätigten RPO/RTO. Keine unbelegte „Backup vorhanden“-Abnahme. | REL-S20/Q20; S2; DEC-49 |
| Sichere Veröffentlichung und Incidentfähigkeit | Geprüfte Artefaktherkunft, minimale CI-/Releaseberechtigung, Verantwortliche, sichere Alarme, Schwachstellenbehandlung und nachgewiesener sicherer Rückweg. | REL-A13, REL-S18, REL-Q17/18/20; SEC-23/24/25 |
| Zugänglichkeit und Belegpaket | NFR-08-Kernbedienung; WCAG-2.2-AA-Ziel vorher entscheiden; anwendbare Kriterien/Sprachen prüfen. Vollständiges Belegpaket und nachvollziehbare menschliche Releaseentscheidung. | REL-A16, REL-Q04/06; NFR-19/20 |

Die Tabelle ersetzt nicht die individuelle Anwendbarkeitsprüfung **aller 46 Kontrollen**. Insbesondere benötigte Funktionstests aus Abschnitt 3 werden Teil der Erstfreigabe, wenn diese Funktionen bereits veröffentlicht werden. Schutz des einzigen Super Admin und der Kontentrennung ist nicht durch eine Risikoakzeptanz abdingbar. Grundschutz, Löschwirksamkeit, unabhängige Sicherung und Incidentfähigkeit dürfen nicht durch einen Feature-Flag als angeblich später behandelt werden, solange die dazugehörigen Daten verarbeitet bzw. produktiv betrieben werden.

## 3. Funktionsabhängige Aktivierung

| Aktivierte Funktion / gewählte Technik | Zuvor tatsächlich nachzuweisen |
|---|---|
| KI, Retrieval oder Agenten | REL-A01/05; ggf. REL-A18 für Bewertung/Anpassung; REL-S04/06/10/15/18, REL-Q01/02/03/07/08/09/11/16/19; aktuelle Provider-/Zweck-/Operationsrechte. Modell nicht verfügbar: sicherer Text-/Datenweg soweit möglich, keine stille kostenpflichtige Ersatz-KI. |
| Dateien, Audio/Video, Transkription, OCR, Archive | REL-S10/11/12, REL-Q11/15/16/20 und REL-A07 für relevante Teile; temporäre Kopien auch nach Abbruch/Fehler bereinigen. |
| Serverseitiger URL-/Web-/Repositoryabruf | SSRF-/DNS-/Redirectteil von REL-A07 zusätzlich; keine unbekannte Konnektorinstallation aus URL. |
| PWA, selektives Offline und Synchronisation | Reale OS-/Browser-/Gerätematrix; REL-Q06/07/09/16/19; Rechte-, Konflikt-, Entzugs- und Löschfälle. Keine Fernlöschgarantie bereits geladener Offlinekopien. |
| Externe Kalender / interne Kalenderimporte | Außen strikt lesen; innere Übernahme von Import/KI-Vorschlag bestätigen; direktes manuelles Speichern ohne Zweitbestätigung. REL-S06, REL-Q07/08/09/11. |
| Sensible geräteseitig geschützte Dokumente / Cloudanalyse | SEC-09/10/11/22/27; kein privater Klartextschlüssel am Backend; eigene explizite Operationsfreigabe, Drittanbieter zusätzlich prüfen. |
| Support, Administration oder Konfigurationsrelease | SEC-04..07; REL-S06/09/15, REL-A13; kein zweiter Super Admin, Selbstbeförderung oder Standardleserecht privater Inhalte. |
| Cross-Origin-API, Webhooks, konkrete RLS-Technik | REL-S13/S17/S04 nur technisch passend; Nichtanwendbarkeit begründen, zugrunde liegende Autorisierungs-/Integritätsziele dennoch erfüllen. |
| Zahlung oder FE-56-Inbox | **Nicht durch Mission 3 freigegeben.** REL-Q10 erst nach neuer ausdrücklicher Fachentscheidung; FE-56 bleibt offen. Keine Aktivierung zur vermeintlichen V1-Vervollständigung. |

Eine noch nicht geprüfte optionale Funktion bleibt serverseitig unerreichbar. Versteckte Navigation allein genügt nicht. Abhängige Jobs, Toolaufrufe, Altclients und externe Hooks ebenfalls sperren. Ein Pflichtschutz einer bereits aktiven Funktion ist keine optionale Teilfunktion.

## 4. Änderungen und wiederkehrende Prüfungen

| Anlass | Erneut erforderlicher Nachweis |
|---|---|
| Auth-, Rollen-, Flag-, Support- oder Datenmodelländerung | REL-S03/04/06/09/19 und relevante REL-Q09/16/19/20; negative Direkt-/Race-/Altclientfälle; heutige Rechte auch bei Rollback. |
| Modell, Prompt, Retrieval, Tool, Bewertungslogik oder Providerwechsel | REL-A01/05/18 nach Funktion, REL-S04/06/10/18, REL-Q01/02/03/11/16/19; Quellen-, Kontext-, Kosten- und Datenweitergaberegression. |
| Import-/Parser-/Medien-/URLänderung | REL-S10/11/12, REL-Q11/15/16, REL-A07; Ressourcen-, SSRF- und temporäre Bereinigungspfade. |
| PWA-, Browser-, UI-, Sprach- oder Assistenzänderung | NFR-02/03/08/19/20; REL-Q04/05/06/16/19, REL-A16. |
| Pipeline-, Abhängigkeits-, Schlüssel-, Backup-/Paket-/Regionänderung | REL-S01/02/07/08/18/20, REL-A13, REL-Q20; Integrität, Rotation, unabhängiger Restore und Nichtwiederbelebung. |
| Wiederkehrender Betrieb | Schwachstellen-/Lizenzinventar, Secret-/Rechte-/Sessionprüfung, sichere Alarme, Retentions-/Löschlauf und tatsächliche unabhängige Restore-/Incident-/Rollbackübung; relevante Kontrollen nach Abschnitt 3. |

Für periodische Aufgaben sind verantwortliche Person, risikobegründeter Rhythmus, Fälligkeit und Belegablage **vor Produktion** zu bestätigen. Noch keine Tages-/Wochenzahl erfunden. Versäumte kritische Fälligkeit wird als Befund und Freigaberisiko behandelt, niemals automatisch als weiterhin bestanden. Anlassbezogene Wiederholung ist unabhängig vom Kalender erforderlich.

## 5. Blocker und dokumentierte Entscheidung

- Fehlende oder fehlgeschlagene Konto-/Rollen-/Serverautorisierung, Super-Admin-Sicherung, Secret-/Schlüsselschutz, zulässige Datenweitergabe, endgültige Löschung oder Wiederherstellbarkeit blockieren den betroffenen Umfang. Betrifft der Fehler gemeinsamen Grundschutz oder Datenintegrität, ist die gesamte Produktfreigabe blockiert.
- Fehlende relevante Produktprüfung, ungeklärte Anwendbarkeit, unbelegte kritische Parameter oder abgelaufene Nachweise sind kein bestandenes Gate. Dokumentarische Vollständigkeit ersetzt keinen Laufzeittest.
- Unzulässige Lizenz/Verarbeitung, ungenehmigte Kosten oder unfertige erreichbare Funktion verhindern die entsprechende Freigabe. Ein Komfortfallback darf keine Schutzgrenze umgehen.
- Nichtkritische Abweichungen nur mit Befund, Auswirkungsanalyse, Zuständigkeit, Frist und ausdrücklicher menschlicher Entscheidung behandeln, soweit kein verbindliches Schutzziel verletzt wird. Kein pauschaler Sicherheitsverzicht durch Projektinhaber oder Agent.

## 6. Zu erhaltende Nachweise und offene Entscheidungen

**Belegdatensatz je Kontroll-ID:** Funktion/Artefakt-/Modell-/Promptfassung; Anwendbarkeit und Quelle; vorab bestätigter Sollwert; Schritte/Befehl und Testdatenherkunft; Gerät/OS/Browser/Hardware/Netz; Datum und verantwortliche Person; Rohbefund/Istwert; bestanden/fehlgeschlagen/blockiert/nicht durchgeführt; Defekt-/Nachprüfverweis; geschützter Artefaktort und endliche Aufbewahrung. Automatisierte Prüfung, manuelle Fachbewertung und tatsächliche Restoreübung unterscheiden. Öffentliche Nachweise ausschließlich bereinigt und künstlich; keine Secrets, Privatdaten, echten Studentendokumente oder wiederherstellbaren Sicherungen im Repository.

**Menschlich offen:** technischer Stack und geprüfte Anbieter/Modelle; Oracle-Bewertung ohne vorweggenommene Auswahl; Untersuchungslimit ist keine Ausgabe; Auth-/Schlüssel-/Recovery-/Bootstrapverfahren; Datenschutzrollen und zulässige Verarbeitungen; Last-/Kapazitäts-/SLO-/RPO-/RTO-/Retentionswerte; Lizenzbeurteilung; WCAG-AA-Ziel; pädagogische Korpora/Rubriken; Release-/Incidentverantwortliche und Prüfintervalle. Nicht abrufbare offizielle Normfassungen aus dem [Referenzrahmen](REFERENZRAHMEN.md) nachprüfen.

Diese Eingaben ermöglichen später S3 und einen getrennt autorisierten Implementierungsplan. Sie sind keine Anweisung, jetzt Infrastruktur anzulegen, Accounts zu eröffnen, einen Anbieter zu verbinden oder eine Veröffentlichung auszulösen. Aktueller Prüfstand: ausschließlich Dokumentation; **keine Produktfreigabe**.
