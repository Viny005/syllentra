# Syllentra AI — 40 Prüfungen für Sicherheit, Betriebsfähigkeit und Produktfreigabe

**Stand:** 22.10.2026  
**Status:** Zur Prüfung durch den Projektinhaber  
**Geltung:** V1-Soll und spätere Versionsfreigaben; keine Behauptung einer Implementierung oder bestandener Produkttests.  
**Herkunft:** Zwei vom Projektinhaber am 22.10.2026 übernommene Checklisten mit je 20 Punkten (Sicherheit und Betrieb/Performance). Die Originalzählung bleibt vollständig erhalten.  
**Einordnung:** Nichtfunktionale Ziele unter [N1](../spec/N1-nichtfunktional.md), Schutzkonzepte unter [N2](../spec/N2-querschnittskonzepte.md), externe Schnittstellen unter [S1](../spec/S1-nachbarsysteme.md), Migration/Backup unter [S2](../spec/S2-datenmigration.md), Nachweisführung unter [E3](../spec/E3-pruefnachweis.md). Die spätere produktive Inbetriebnahme gehört in S3.

## 1. Verbindliche Verwendung und Statusregeln

- **Jetzt dokumentieren:** Alle 40 Punkte in ihrer ursprünglichen Reihenfolge, mit fachlicher Schutzzielpräzisierung, Anwendbarkeit und überprüfbarem Nachweis. Die Liste ergänzt bereits getroffene FE-Entscheidungen, ersetzt oder umnummeriert keine FE-/UC-/SEC-/NFR-Kennung.
- **Bei der Implementierung:** Nur passende Maßnahmen im gewählten, separat genehmigten Stack realisieren; keine vorgezogene Anbieter-, ORM-, Hosting- oder Authentifizierungsentscheidung. Schutzmaßnahmen müssen **vor Freischaltung der davon abhängigen V1-Funktion** nachweisbar vorhanden sein.
- **Vor jeder Produktivfreigabe:** Die für tatsächlich aktivierte Funktionen anwendbaren Prüfungen durchführen; Befund, Datum, Testumgebung, Messwerte und verantwortliche Person dokumentieren. **Nicht implementiert** und **nicht getestet** gelten niemals als **bestanden**. Keine automatische Freigabe aus erfolgreicher Markdownprüfung.
- **Bedingt:** RLS, Browser-CORS, Webhooks und ähnliche Mechanismen sind nur dann als konkrete Technik vorgeschrieben, wenn die gewählte Architektur sie verwendet. Das zugrunde liegende Schutzziel (Datenisolation, kontrollierte Herkunft, Integrität) bleibt verbindlich.
- **Später:** Zahlungsvorgänge sind kein V1-Umfang. Nur bei später ausdrücklich freigegebener Zahlungsfunktion werden transaktionale Zahlungs-/Webhook-/Buchungstests produktionskritisch. Kein Bezahlanbieter wird ausgewählt oder aktiviert.
- **Ohne erfundene Werte:** Verbindliche Raten, Zeitlimits, Speicherobergrenzen, RPO/RTO, Parallelitätsziele, Budgetgrenzen und Alertschwellen werden erst anhand eines separaten Betriebs-/Architekturentscheids bestimmt. Die Grundregel FE-53 (keine verpflichtende kostenpflichtige KI-API) und das Verbot unautorisierter Ausgaben bleiben bestehen.
- **Prüfstatus pro Eintrag:** `OFFEN` (noch nicht umgesetzt/geprüft), `BEDINGT` (Architektur- oder Funktionsabhängigkeit), `SPÄTER` (nicht V1), `BESTANDEN` (nur mit echtem Prüfbeleg), `NICHT BESTANDEN` oder `NICHT ANWENDBAR` (begründet). Die nachstehende Liste dokumentiert Ziele; aktuell ist **kein Kontrollpunkt als technisch bestanden nachgewiesen**.

## 2. Sicherheitscheckliste aus der ersten Quelle — 20/20

| ID | Ursprünglicher Punkt | Syllentra-Soll und späterer Nachweis | Einordnung |
|---|---|---|---|
| REL-S01 | Clés API dans `.env` | Servergeheimnisse nur in geschützter Laufzeitkonfiguration/Secret-Verwaltung; `.env` kann lokal dienen, ist aber keine zwingende Produktionslösung. Secret-Scan auf Code, Builds, Logs und Konfiguration. | N2; V1 |
| REL-S02 | `.env` dans `.gitignore` | Geheimnistragende `.env`-Dateien dürfen nicht versioniert werden; ungefährliches `.env.example` ohne Realwerte möglich. Historie, CI-Artefakte und öffentliches Repository auf Lecks prüfen. | N2; V1 |
| REL-S03 | Rate limiting sur le login | Login, OTP, Verifikation, Recovery und Gerätefreigabe gegen Brute Force/Spam begrenzen; legitime Recovery ermöglichen. Last- und Negativtests pro Konto/IP/Kontext. | N2/N1; V1 |
| REL-S04 | RLS activée | Bei direkt nutzbarer PostgreSQL-RLS: passende Policies inklusive negativer Tests. Andernfalls gleichwertige verbindliche serverseitige Mandantenisolation; RLS-Status niemals ohne Stack-Nachweis behaupten. | N2; bedingt Technik, V1-Schutzziel |
| REL-S05 | Mots de passe hashés | Passwörter ausschließlich mit geeignetem adaptivem Passwort-Hash (z. B. Argon2id) und sicherer Authentisierungsbibliothek; keine Klartextpasswörter oder reversible Speicherung. | N2; V1 |
| REL-S06 | Droits vérifiés côté serveur | Pro Operation serverseitig Sitzungs-, Rollen-, Eigentums-, Feature-Flag-, Scope- und Supportrechte prüfen; horizontalen und vertikalen Privilegienmissbrauch testen. | N2; V1 |
| REL-S07 | Clé publique côté client | Nur explizit öffentliche Schlüssel/Konfigurationswerte in Browserbundle; niemals API-Secret, privater Signaturschlüssel oder ungeschützter Benutzer-Token. Build- und Netzwerkanalyse. | N2; V1 |
| REL-S08 | HTTPS partout | Browser, Backend und notwendige Integrationsverbindungen verschlüsselt; keine Mischinhalte oder unverschlüsselte Authentifizierungsdaten, sichere Cookies. | N2; V1 |
| REL-S09 | Sessions qui expirent | Serverseitiges Ablauf-, Widerrufs-, Geräteentzug- und Sitzungsrotationsverhalten prüfen; lokale Gerätesperre ersetzt keine Serversitzung. | N2; V1 |
| REL-S10 | Inputs validés | Servervalidierung aller Eingaben einschließlich API, Markdown, Konfiguration und importierter Metadaten; strukturierte, ungefährliche Fehlerrückgabe. | N2; V1 |
| REL-S11 | Taille max des uploads | Konto-/Datei-/Gesamtgrößen, Archive, Verschachtelung und entpackte Gesamtmenge kontrolliert begrenzen; Quoten vor unnötiger Verarbeitung durchsetzen. | N1/N2; V1 |
| REL-S12 | Type de fichier vérifié | Tatsächliche Dateisignatur/Inhalt gegen erlaubte Formate prüfen; MIME/Dateiendung allein reicht nicht; Archive gegen Zip-Slip/Bomben und schädliche Inhalte sichern. | N2; V1 |
| REL-S13 | CORS configuré | Bei Cross-Origin-Browser-APIs explizite zulässige Origins/Methoden/Header, Credentials- und CSRF-Regeln; kein permissives `*` mit Credentials. Ohne solche API begründet nicht anwendbar. | N2; bedingt |
| REL-S14 | Erreurs détaillées coupées | Keine Stacktraces, SQL, Pfade, Tokens oder internen Details in öffentlichen Fehlerantworten; diagnostische Details nur geschützt intern. | N2; V1 |
| REL-S15 | `console.log` clean | Keine Secrets/Personen-/Lerninhalte in Browserkonsole, Server- oder CI-Logs; notwendige Betriebsereignisse strukturiert und datensparsam protokollieren. | N2; V1 |
| REL-S16 | Message d'erreur unique | Bei Login/Recovery keine Kontenexistenz verratenden Antworten (Anti-Enumeration); ansonsten verständliche, zugängliche und zustandsspezifische Nutzerfehler mit optionaler Support-Korrelation. Nicht alle Fehler pauschal gleich machen. | N1/N2; V1 |
| REL-S17 | Webhooks signés | Falls Webhooks angenommen werden: Signatur/Quelle, Replay-Schutz, Ablauf, Idempotenz und passende Rechte verifizieren; ohne Webhook begründet nicht anwendbar. | N2/S1; bedingt |
| REL-S18 | Dépendances à jour | Abhängigkeiten, transitive Pakete und Container/Images auf bekannte Schwachstellen und Lizenzverstöße prüfen; getestete Updates statt blindem Auto-Upgrade. | N1/N2; V1 |
| REL-S19 | Email confirmé | FE-60: Erstzugang zu Anwendungsdaten erst nach verifizierter E-Mail/OTP, Ratenbegrenzung und Ablauf; Konto- und Recoverystatus getrennt halten. | N2; V1 |
| REL-S20 | Backup auto | Regelmäßige verschlüsselte, zugriffsbeschränkte Sicherungen mit EU-Aufbewahrung, Löschkonzept, Wiederherstellungsproben und dokumentierten RPO/RTO. Keine Wiederbelebung endgültig gelöschter Inhalte. | N1/N2/S2; V1 |

## 3. Betriebs-, Leistungs- und UX-Checkliste aus der zweiten Quelle — 20/20

| ID | Ursprünglicher Punkt | Syllentra-Soll und späterer Nachweis | Einordnung |
|---|---|---|---|
| REL-Q01 | Rate limiting général | Missbrauchsschutz für alle kosten-/lastrelevanten API-, KI-, Import-, Such- und Jobendpunkte einschließlich fairer Nutzerquoten; legitime Aktionen nicht grundlos sperren. | N1/N2; V1 |
| REL-Q02 | Limites des appels API | Zeit-, Mengen-, Parallelitäts- und Konnektorbudgets abhängig von tatsächlichen Funktionen; automatische Wiederholung nur nach FE-88 und erneuter Rechteprüfung. | N1/S1; V1 |
| REL-Q03 | Contrôle des dépenses | Kosten-/Rechenbudgets, Nutzerfreigaben und harte Stopps bei explizit kostenpflichtigen optionalen Wegen; keine automatisch entstehenden Kosten, keine Pflicht-Pay-API. | N1/N2; V1 |
| REL-Q04 | Messages d'erreur compréhensibles | Verständliche, übersetzbare und handlungsfähige Fehlermeldungen ohne sensible Technikdetails, inkl. Offline-/Fehler-/Wiederaufnahmezustand. | N1/B1; V1 |
| REL-Q05 | Indicateurs de chargement | Asynchronen Fortschritt und Wartezustände zugänglich anzeigen; wiederholte Aktion nicht unkontrolliert starten; lange Jobs unterbrechbar wo vorgesehen. | N1/B1; V1 |
| REL-Q06 | États particuliers | Leere Daten, fehlende Berechtigung, ausgeschaltete Features, Offlinezustand, unbekannte Quelle und Dienststörung korrekt und zugänglich unterscheiden. | N1/B1; V1 |
| REL-Q07 | Échecs et nouvelles tentatives | Retry nur begrenzt, mit Backoff, Rechte-/Kosten-/Idempotenzprüfung, korrekter Unterscheidung transient/permanent und sichtbarem Status (FE-88). | N1/N2/B2; V1 |
| REL-Q08 | API timeouts | Explizite, geprüfte Timeouts und Abbruch-/Kompensationsregeln für synchrone und asynchrone Aufrufe; sichere Zustandsaufnahme bei unbekannter Wirkung. | N1/B2; V1 |
| REL-Q09 | Doubles soumissions | Idempotenz-/Deduplizierungsschlüssel und serverseitiger Schutz bei Formularen, Imports, Jobstarts und Bestätigungen; nicht nur Button deaktivieren. | N1/N2; V1 |
| REL-Q10 | Doubles paiements | **Kein Zahlungsumfang in V1**. Falls später ausdrücklich beschlossen: idempotente Zahlungstransaktionen, robuste Webhookverarbeitung, doppelte Requests/Callbacks und Abstimmung testen. | Später, nicht V1 |
| REL-Q11 | Données strictement nécessaires | Datenminimierung bei API, Client, Suche, Lernmodell, Logs und KI-Kontext; keine kontofremden/unnötig sensiblen Daten übertragen. | N1/N2; V1 |
| REL-Q12 | Index de base de données | Relevante Zugriffswege/Abfragen messen, erforderliche Indizes nach gewähltem Datenbanksystem und Isolation anlegen; keine ORM-/DB-Vorauswahl. | N1; V1 |
| REL-Q13 | Pagination | Große Listen, Auditverlauf, Integrationshistorie, Suche und Materialien mit begrenzten Seiten/Streams; Grenzen und Berechtigungen auch bei Folgeseiten prüfen. | N1; V1 |
| REL-Q14 | Compression | Geeignete Dateien/Antworten sparsam komprimieren; Bild/Audio/Video nicht blind doppelt komprimieren; Schutz gegen Seitenkanäle beim Reflektieren von Secrets berücksichtigen. | N1/N2; V1 |
| REL-Q15 | Limite de taille des uploads | REL-S11 zusätzlich als Betriebs-/Ressourcenlast prüfen: Speicher, Parserlaufzeit, Dekompression, Uploadabbruch und fairen Parallelbetrieb testen. | N1/N2; V1 |
| REL-Q16 | Stratégie de cache | Zielgerichtetes Caching mit Konto- und Berechtigungsisolation, Sensitivitätsvererbung, Ablauf, Widerruf, sicherem Offlinezustand und endgültiger Löschung. | N1/N2/S2; V1 |
| REL-Q17 | Monitoring des indisponibilités | Erreichbarkeit und kritische Pfade datensparsam überwachen; dokumentierte Alarmierungs- und Reaktionswege ohne Pflicht zu kostenpflichtigem Monitoring. | N1/S3; vor Freigabe |
| REL-Q18 | Journaux d'erreurs exploitables | Korrelation/Schweregrad, nachvollziehbare sichere Diagnose, Zugriffsschutz, Retention und Datenschutz; keine Secrets oder unnötigen Nutzerinhalte. | N1/N2; V1 |
| REL-Q19 | Plusieurs utilisateurs simultanés | Repräsentative Mehrnutzer-/Parallel-/Race-/Mandantentrennungstests für Auth, Upload, Suche, KI, Offlineabgleich, Quoten und Jobs. Verbindliche Lastziele zuvor festlegen. | N1/N2; vor Freigabe |
| REL-Q20 | Backups et restauration vérifiée | REL-S20 ergänzen: Wiederherstellung wirklich üben, Integrität, Schlüsselfall, Gerät, Mandantentrennung, Löschmarkierung, Restore-Rechte und RPO/RTO messen. | N1/N2/S2; vor Freigabe |

## 4. Ausführung über Projektphasen

| Phase | Was jetzt oder später verlangt wird | Bedingung |
|---|---|---|
| Spezifikation, **jetzt** | Diese 40 Punkte als Querverweis in N1/N2/Index aufnehmen, Kollisionen mit FE/UC vermeiden; offene Entscheidungen und Nachweispflichten sichtbar lassen. | Rein dokumentarisch; Status „Zur Prüfung“. |
| Architekturentscheidung, **später** | Passende Schutzmechanismen, Grenzwerte, Datenbank-/RLS-Variante, Betriebs- und Backupverfahren, Kosten-/Monitoringlösung samt Alternativen und Lizenz-/Privacyprüfung verbindlich auswählen. | Vor jeweiliger technischer Umsetzung; keine automatische Ausgabe oder Fremdanbindung. |
| Implementierung, **später** | Anwendbare Prüfungen durch tatsächlich implementierte technische Kontrollen und automatisierte negative Tests nachweisen. | Funktionen bleiben verborgen/gesperrt, bis sie einschließlich Rechteprüfung überprüft sind (FE-58/59/69). |
| Test und Produktfreigabe, **später** | Sicherheits-, API-, Browser-, Performance-, Backup-/Restore-, Last- und Mandantentrennungstests mit realen Testprotokollen; alle anwendbaren Punkte entscheiden. | Offene/blockierende Befunde verhindern Aktivierung der betroffenen Funktion bzw. den Produktivstart. |
| Zahlungsfunktion, **nur auf neue Freigabe** | REL-Q10 und ggf. dafür bestimmte Zahlungs-Webhooks/Transaktionen spezifizieren, implementieren und testen. | Keine stillschweigende Aktivierung oder monetarisierende V1-Funktion. |

## 5. Minimaler Nachweisdatensatz pro Prüfung

Pro REL-ID später in einem testbaren Prüfprotokoll führen: **ID, geprüfte Funktion und Version, Anwendbarkeit mit Begründung, gewählter Sollwert/Quelle, Testart und Befehl/Schritte, Testumgebung und Datum, Istwert bzw. Befund, Status, Ticket/Beleg, Verantwortliche, offenes Risiko**. Automatisierte CI-Befunde und manuelle Wiederherstellungsübungen unterscheiden. Belege nur anonymisiert oder künstlich, niemals private Studierendendaten oder Geheimnisse in ein öffentliches Repository.

**Freigaberegel:** Keine Veröffentlichung auf Basis bloßer Checklisten-Abhakung; ein negativer Sicherheits- oder Löschtest ist ein Blocker für die betroffene Funktion. Abweichungen dokumentiert bewerten und durch den Projektverantwortlichen freigeben, soweit das Schutzziel nicht verletzt wird. Testplanung und reale Durchführung sind getrennt; E3 dokumentiert nur tatsächlich nachgewiesene Schritte. Der bestehende Stand enthält noch keinen lauffähigen Anwendungscode und **keinerlei Produktabnahme**.

## 6. Abgrenzung und spätere Ergänzungen

- **N1** übernimmt Qualitätsanforderungen, messbare Leistungsziele und Laufzeit-/Last-/UX-Nachweise; **N2** übernimmt Bedrohungs- und Schutzkontrollen; **B1/B2** konkretisieren Nutzerzustände und sichere Hintergrundverarbeitung erst bei entsprechendem fachlichem Auftrag.
- **S1** bleibt die Spezifikation von Nachbarsystemen und Integrationsverträgen, nicht ein globales Performancehandbuch. **S2** bleibt zuständig für Sicherungen, Restore, Datenmigration und Nichtwiederbelebung.
- **S3 (noch zu erstellen)** wird später den Freigabeprozess, Bootstrap und Betriebsstart inklusive dieser Nachweise und Alarmierungsverfahren regeln. Die Checkliste ersetzt S3 nicht.
- **FE-56** (optionale Postfachlesefunktion) bleibt offen. **Syllentra Games** ist ein zukünftiger Konzeptvorschlag, keine aktivierte oder genehmigte V1-Funktion. Keine neuen FE-, Zahlungs- oder Anbieterentscheidungen werden durch diese Liste geschaffen.

## 7. Verweise

- [N1 — Nichtfunktionale Anforderungen](../spec/N1-nichtfunktional.md)
- [N2 — Querschnittskonzepte](../spec/N2-querschnittskonzepte.md)
- [S1 — Nachbarsysteme](../spec/S1-nachbarsysteme.md)
- [S2 — Datenmigration](../spec/S2-datenmigration.md)
- [E3 — Änderungs- und Prüfnachweis](../spec/E3-pruefnachweis.md)
- [Roadmap](../ROADMAP.md)
- [Architecture Decisions](../ARCHITECTURE_DECISIONS.md)

## 8. Ergänzung aus Mission 3 ohne Änderung der ursprünglichen 40 Punkte

Die [konsolidierte Kontrollmatrix](RELEASE_KONTROLLMATRIX.md) enthält die Bewertung von 20 Ergänzungskandidaten, vertiefte Prüfprofile für alle ursprünglichen Kontrollen und sechs eigenständige zusätzliche Kontrollen (REL-A01/05/07/13/16/18): insgesamt 46. Die Originalfassung oben bleibt vollständig erhalten. [Referenzrahmen](REFERENZRAHMEN.md) und [Freigabevoraussetzungen](FREIGABEVORAUSSETZUNGEN.md) begründen Zuordnung und spätere Nachweise; keine Kontrolle ist technisch bestanden, keine S3-Inbetriebnahme erfolgt.

## 9. Aktueller S3-Verweis

Der historische Planungsstand „S3 noch zu erstellen“ in Abschnitt 6 ist durch den fachlichen [S3-Prüfentwurf](../spec/S3-inbetriebnahme.md) abgelöst. Die ursprünglichen 40 Kontrollen bleiben vollständig unverändert; [S3.8](../spec/S3-inbetriebnahme.md#s38-einbindung-aller-46-release-kontrollen) ordnet alle inzwischen 46 Kontrollen der künftigen Ausführung zu. Kein produktiver Betrieb oder bestandener Produkttest wird dadurch behauptet.
