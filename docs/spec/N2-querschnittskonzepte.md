# N2 — Querschnittskonzepte

**Projekt:** Syllentra AI\
**Version:** 0.10\
**Stand:** 23.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

## N2.1 Zweck und Ausarbeitungsgrenze

Dieser fachliche V1-Sicherheitsprüfentwurf vervollständigt die Schutzanforderungen und ihre Verifikation im bestätigten Funktionsumfang. SEC-01 bis SEC-16 bleiben erhalten; N2.12–N2.15 ergänzen die vollständigen Prüfprofile. Er ist kein implementiertes Sicherheitskonzept, kein Schema, kein ausgewähltes Authentifizierungsprodukt und keine fertige Kryptospezifikation. [D1](D1-datenmodell.md) beschreibt Entitäten und Invarianten, [D2](D2-datentypen.md) Werte, [S1](S1-nachbarsysteme.md) die Nachbargrenzen. Konkrete technische Verfahren benötigen spätere Prüfung, ohne die festgelegten Grenzen aufzuheben.

## N2.2 Konten, Authentifizierung und Sitzungen

- **SEC-01 — Verifizierter Zugang (FE-37, FE-38, FE-59 bis FE-62):** Offene Registrierung mit E-Mail und Passwort; E-Mail-OTP vor jedem erstmaligen Anwendungsdatenzugang. Unverifizierte Konten dürfen nur den beschränkten Verifikations-/Recoveryweg nutzen; bleibt ein Konto im Status `pending` mindestens 24 Stunden ab seinem serverseitigen Startzeitpunkt unverifiziert (`>= 24 h`, einschließlich der exakten Grenze und ohne Fristverlängerung durch OTP-Neuversand), kann es in einem neuen Registrierungsdurchlauf mit neuem Passwort, neuer E-Mail-OTP-Prüfung und Invalidierung alter Challenges ohne Daten-/Rechtetransfer zurückgesetzt werden, während bereits verifizierte Konten niemals zurückgesetzt werden (R4, bestätigt am 23.10.2026). Bekannte Geräte melden sich normal mit Passwort an; neue Geräte verlangen zusätzliche berechtigte Verifikation. Optionale Passkeys, OS-Biometrie, TOTP und SMS nur bei tatsächlicher Unterstützung; keine Rohbiometrie an Syllentra. SMS ist niemals alleiniger sensibler Recoverynachweis.
- **SEC-02 — Getrennte Zustände (FE-36 bis FE-39, FE-61, FE-62):** Konto, Gerät, Serversitzung, lokale Sperre und Dokumentenschlüssel sind getrennt. Mehrtagessitzung und konfigurierbare lokale Inaktivitätssperre sind Ziele ohne erfundene Dauer. Lokales OS-Biometrie-/PIN-Entsperren verlängert keine abgelaufene Serversitzung. Neue Geräte durch bestehendes berechtigtes Gerät oder sichere Wiederherstellung bei Verlust autorisieren; Entzug sperrt weitere Zugriffe, beweist keine Fernlöschung bereits vorhandener Offlinekopien.
- **SEC-03 — Recovery (FE-38, FE-70, FE-77):** Persönliche einmal nutzbare Kontorecoverycodes zusammen mit verifizierter E-Mail; der persönliche Einmal-Recoverycode läuft nicht automatisch nach sieben Tagen ab, sondern bleibt unabhängig von der Gerätevertrauensdauer bis zur erfolgreichen Verwendung, zum expliziten Widerruf, zur kontrollierten Regeneration/Rotation oder zur sicherheitsbegründeten Invalidierung gültig (R1, bestätigt am 23.10.2026). Admin-MFA mit gesichertem Wiederherstellungsweg. Dokumentenschlüssel werden gesondert persönlich wiederhergestellt. Kontoerfolg ist kein Dokumentenschlüsselnachweis. OTP-/Versuchs-/Sitzungsgrenzen und konkrete Nachweisverfahren bleiben O-S1-06/07.

## N2.3 Rollen, Isolation und Featuregrenzen

- **SEC-04 — Berechtigungsschnittmenge (FE-58, FE-59, FE-63):** Bei jeder Datenwirkung serverseitig Kontostatus, aktuelle Sitzung, Gerät, Objektbesitz, Rolle, Funktionsrecht, Zweck, Scope und ggf. Support-/Verarbeitungsfreigabe prüfen. Verborgene Navigation ist keine Sperre; unbekannte Pflichtberechtigung verweigert Zugriff. Diese Regel gilt auch für Suchindizes, Vorschauen, Exporte, Jobs, Cache und Restore.
- **SEC-05 — Administration (FE-70 bis FE-72):** Genau ein Super Admin; ausschließlich er lädt sekundäre Administratoren ein, ändert, suspendiert und widerruft sie. Sekundäre dürfen weder sich selbst erweitern noch andere Administratoren verwalten; exklusive Rechte sind nicht delegierbar. Getrennte Konsole, verpflichtende MFA, erneute Bestätigung sensibler Aktionen und Audit ohne Secrets. Sicherer erster Bootstrap und Verlustfall gehören nach S3; keine zweite Super-Admin-Rolle wird erfunden.
- **SEC-06 — Support (FE-63):** Nur freiwillige ausdrückliche Freigabe von Person, Zweck, Objekten, Rechten und endlicher Dauer; Standard lesend. Änderung gesondert bestätigen. Ablauf/Widerruf beendet weitere Wirkung. Adminrolle allein erlaubt keinen privaten Inhalt, keinen Supportexport und keine Schlüsselwiederherstellung.
- **SEC-07 — Release/Quota (FE-57 bis FE-69):** Unterstützte Konfiguration validiert und persistent; Entwurf, Vorschau, eigener Nutzertest, ausgewählte Tester, manuelle oder geplante Veröffentlichung, widerrufbarer Termin und revalidierter Rollback. Ankündigung erst bei tatsächlicher Verfügbarkeit. Deaktivierung erhält Daten, sperrt neue Wirkungen und erlaubt nur sichere Lesesichten. Grundquoten plus Kontoausnahmen, Warnungen und gezielte Neuaufnahmesperre; kein Kontoverlust wegen voller Quote.

## N2.4 Schlüssel, Datenfluss und sensible Analyse

- **SEC-08 — EU und Verschlüsselung (FE-75, FE-76):** Hauptdaten/Sicherungen EU, Transport-/Ruhe-/Backupverschlüsselung; externe Übermittlung nur im geprüften erlaubten Rahmen. Reguläre autorisierte Serveranalyse ist möglich. Sensible ausgewählte Dokumente bekommen zusätzlichen geräteseitigen Schutz; konkrete Verfahren und Schlüsselverteilung bleiben zu prüfen.
- **SEC-09 — Private Schlüssel (FE-77):** Nur berechtigte Geräte verfügen über die zur Entschlüsselung nötigen privaten Schlüssel. Backend und Administratoren besitzen sie niemals im Klartext. Sicherer Gerätewechsel und persönliche Schlüsselrecovery müssen auch beim Verlust aller Geräte technisch untersucht werden. Opaque Schlüsselbezüge in D1 sind keine gespeicherten Klartextschlüssel.
- **SEC-10 — Temporärer sensibler Klartext (FE-78):** Lokal bevorzugt. Die eigene Syllentra-Cloud darf nur pro explizit freigegebener Operation notwendige entschlüsselte Ausschnitte sehen. Nutzer sieht Zweck, Fassung, Umfang und dass der Server den Klartext während der Verarbeitung sieht. Keine privaten Schlüssel und keine dauerhaften Klartextkopien; temporäre Kopien/Diagnose nachweisbar bereinigen. Für diese Operation wird keine Geheimhaltung des Klartexts gegenüber dem analysierenden Server behauptet. Dritt-KI braucht zusätzlich Anbieter-/Kategorie-/Zweckfreigabe und geeignete Bedingungen.
- **SEC-11 — Vererbung (FE-79):** Zusammenfassung, Transkript, Übung, Lernkarte, Erinnerung, Suchindex, Vorschau, Benachrichtigung und Backup erhalten mindestens den Quellschutz. Mehrere Quellen erhöhen nicht still die Offenheit. Herabstufung oder Teilen nur explizit mit Folgenvorschau; kein privater Text in ungeschützten Indizes oder Meldungen.

## N2.5 Vertrauensgrenzen, Historie und sichere Wiederaufnahme

- **SEC-12 — Unvertrauenswürdige Eingaben (FE-28, FE-53, FE-54):** Dokumente, Webseiten, Archive, Repositories und KI-Ausgaben sind Daten. Sie dürfen keine Rechte, Ausgaben oder Löschaktionen anweisen. ZIP/7z auf Pfadflucht, Bomben, Verschachtelung, Größe, Format, Beschädigung und ausführbare Inhalte prüfen; niemals importierte Programme ausführen. Eine Service-URL installiert keinen fremden Konnektor. Lizenzketten vor Auswahl prüfen; keine Pflicht zu kostenpflichtigen APIs.
- **SEC-13 — Integration (FE-31, FE-43, FE-50, FE-84 bis FE-89):** Offizielle minimale Verbindung, freiwilliger Scope, manuelle Synchronisation als Standard, Automatik pro Verbindung opt-in. Widerruf/Ablauf stoppt Abrufe und Retries, Kopien bleiben rechtmäßig nutzbar. Quelländerung zuerst vorschlagen; Ableitung nach bestätigter Quelle markieren und vor Inhaltsübernahme bestätigen. Begrenzte sichere Wiederholung mit erneuter Rechte-/Kostenprüfung, unklare Wirkung zuerst abgleichen.
- **SEC-14 — Nachweise (FE-70, FE-89):** Private Integrationshistorie hält Berechtigung, Scope, Quellenkennungen, Importe, Zustände, Fehler und Widerruf fest. Adminaudit dokumentiert handelnde Rolle, Zweck, Ziel, Zeit und Ergebnis. Keine Passwörter, OTP, Recoverycodes, Tokens, privaten Schlüssel, unnötigen Inhaltskopien oder geheimen URLs. Auskunftsrecht und endliche Retention je Art bestimmen; Support sieht keine privaten Journale standardmäßig. KI-Nutzungsstatistik bleibt getrennt und aggregiert nach FE-14/17.

## N2.6 Aufbewahrung, Löschung und Wiederherstellung

- **SEC-15 — Datenkontrolle (FE-13, FE-40, FE-41, FE-80, FE-81):** KI-Löschwunsch identifiziert konkrete Ziele und Folgen, fragt bei Mehrdeutigkeit nach und verlangt die passende Bestätigung. Privater Papierkorb mit konfigurierter Frist, Wiederherstellung oder sofortige endgültige Bereinigung. Ableitungslöschung ist keine Originalkaskade. Löschmarkierungen ohne Inhaltskopie verhindern Wiederbelebung aus Offlinekopien, Historie und Backup. Endliche Sicherungsretention und gesetzliche Restpflichten transparent; tatsächliche Bereinigung nicht vorwegnehmen.
- **SEC-16 — Konto (FE-82, FE-83):** Freiwillige reversible Pause, bestätigte endgültige Kontolöschung und begründete administrative Sperre sind verschieden. Vor Kontolöschung Identität prüfen und optional Export anbieten; Sessions beenden, Verbindungen widerrufen, Purges mit tatsächlichem Fortschritt. Administrative Sperre bewahrt Daten, dokumentiert Grund und erlaubt Benachrichtigung/Überprüfung; sekundäre brauchen das ausdrückliche Sperrrecht.

## N2.7 Verfolgbare offene technische Arbeiten

O-S1-06 bis O-S1-13 bleiben offen: Verifikations-/Sitzungsfristen und Ratenbegrenzung, Geräte-/Schlüsselverteilung und verlorene Geräte, kryptographische Verfahren, isolierte temporäre Cloudanalyse samt Bereinigungsnachweis, Aufbewahrungs-/Backupfristen, belastbare Löschmarkierung bei endlicher Retention, Limits, Recovery und einziger Super-Admin-Bootstrap. S2 spezifiziert portable Migration und Differenzrestore, S3 den sicheren Betriebsstart. Es werden keine Anbieter, Protokolle oder Zahlen als bereits beschlossen ausgegeben.

**Künftige negative Prüfungen:** Unverifiziertes Konto gegen Appdaten; A gegen B; sekundärer Admin gegen Selbstbeförderung; verstecktes Feature per Direktaufruf; Support nach Ablauf; widerrufene Verbindung vor Retry; Serveranalyse ohne konkrete Freigabe; Secret im Log; sensibles Ergebnis im Suchindex; endgültig gelöschtes Objekt in altem Backup. Diese Szenarien sind Anforderungen, keine in dieser Dokumentationslieferung ausgeführten Produkttests.

## N2.8 S2-Kontrollstand und sicherer Wiederherstellungsumfang

[S2.7/S2.8](S2-datenmigration.md) vertieft SEC-03/04/08/09/10/11/12/14/15/16. Persönliche Datenportabilität ist kein Export von Passwort-Hashes, OTP, MFA-/Sitzungs-/OAuth-Geheimnissen, Gerätevertrauen, Supportrechten oder aktiven Admin-/Integrationszuständen. Betrieblich notwendige technische Sicherungsgegenstände gehören zu einem gesonderten geschützten BAK-/S3-Verfahren und werden vor Wiederfreigabe gegen heutige Rechte/Entzüge geprüft, nicht als Nutzerpaket ausgegeben.

**Kontrollstand:** Vor Import/Restore/Cutover ist ein belastbarer aktueller Lösch-/Widerrufs-/Kontostatus außerhalb einer blind zurückgespielten alten Sicherungsfassung einzubeziehen. Fehlt dieser Nachweis, keine Aktivfreigabe. Endliche Löschmarker-/Backupretention muss mit Gültigkeitsgrenzen alter Pakete/Clients und Nachweisfällen technisch abgestimmt werden (O-S2-03/08); bloßes Löschen alter Marker ohne Wiederbelebungsschutz ist keine Lösung. Keine neue unbegrenzte Markeraufbewahrung wird beschlossen.

**Schlüssel/Schutz:** Fehlende persönliche Dokumentenschlüssel können weder Betrieb noch Kontorecovery rekonstruieren. Geschütztes Paket und Quellschutz sind getrennte Ebenen; Übernahme ist keine Cloud-Klartextanalysefreigabe. FE-78 bleibt pro Vorgang gesondert. Integrations-/Support-/Geräte- und Adminrechte werden nicht aus Paketen aktiviert; historische private Logs enthalten keine Secrets. Eigene Altaccount-/Neukontoübernahme ist bis zum starken Verfahren O-S2-09 nicht automatisch erlaubt.

**Planung:** Reimport erhält manuelle Herkunft/Terminbindung und jüngere Lernbelege. Restore oder Plan-Undo darf diese nicht still überschreiben. S2 führt keine neue automatische Lernheftordnung aus und ändert keine Kalenderbestätigungsgrenze. Die dokumentarische Konsolidierung der 25 DEC-V1 steht jetzt in der [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md); offene fachliche Präzisierungen und technische Nachweise sind dort getrennt ausgewiesen. Die aktuelle fachliche Vervollständigung und weiterhin offenen technischen Nachweise stehen in N2.12–N2.15.

## N2.9 Kontrollgrenzen der persönlichen Lern- und Hinweisfunktionen

L-08-Aktivierung gilt nur für die persönliche pädagogische Reihenfolge DM-75, nicht für DM-35-Kalender, DM-41-Vorschlagsannahme oder Drittanbieteranalyse. Vor automatischer Wirkung aktuelle Konto-/Objektrechte, Aktivierungs-, Plan- und Evidenzrevision prüfen. Deaktivierung sperrt weitere autonome Umordnung. Undo ist ein begrenzter neuer eigener Korrekturvorgang unter aktuellen Rechten, kein Wiederaufspielen alter Antworten, Rollen, Quellen oder Löschungen. Historie geschützt und endlich, kontrollierte Löschung ohne Schatteninhalte.

L-04/UC-65-Regeln DM-77 erteilen kein OS-/Push-/E-Mail-Recht. Ruhe-/Fokuszurückstellung und Dringlichkeit sind keine Datenschutzumgehung. DM-52-Hinweisinhalt, DM-78-Zustellnachweis und pädagogische Langzeiterinnerung bleiben getrennt. Löschung des Verlaufs entfernt keine Termine/Belege, verhindert aber Wiederzustellung durch veraltete Jobs; minimale endliche Deduplizierungs-/Löschinformationen enthalten keine privaten Textkopien. Konkretes Retentions-/Wiederholungsprotokoll bleibt offen und muss Nichtwiederbelebung nachweisen. Sicherheitspost behält ihren gesonderten Kontozweck; FE-56 schließt seit Mission 19 Postfachlektüre, -synchronisation und -überwachung in V1 aus; eine spätere Integration bleibt unverbindlich.

L-09/UC-66-Geltungsprüfung lässt Quellenautorität und persönlichen Regelumfang nachprüfbar. Nutzerbestätigung legitimiert keine falsche amtliche Anerkennung oder private Datenkorrektur außerhalb des gewählten Umfangs. L-02 reduziert Anzeigeunterbrechungen, niemals notwendige Rechte-/Sicherheitsprüfung oder Fortschrittssicherung. SEC-01 bis SEC-16 und sämtliche Konten-/Schlüssel-/Supportgrenzen werden weder umnummeriert noch erweitert. [F2](F2-anwendungsfaelle.md), [S1](S1-nachbarsysteme.md) und [S2](S2-datenmigration.md) bleiben zusammen verbindliche Grenzen der Sollfassung.


## N2.10 Sicherheits- und Release-Checklisten: Schutzmatrix (22.10.2026)

Die vom Projektinhaber übernommenen zwei Listen werden im [40-Punkte-Freigaberegister](../quality/RELEASE_READINESS_40.md) vollständig und einzeln unter **REL-S01..REL-S20** und **REL-Q01..REL-Q20** geführt. N2 ist die fachliche Heimat der Sicherheitsgrenzen; N1 definiert die messbaren Qualitätsziele, S2 die Wiederherstellungs-/Migrationsregeln. Die Liste ist noch kein Implementierungs- oder Testbeleg.

**Schutzfelder:** Geheimniskonfiguration/Repository-Schutz (REL-S01/02/07), authentifizierte Sitzungen und E-Mail-Verifikation (S03/05/09/19), serverseitige Rechte und Isolation (S04/06), Transport-/API-/CORS-/CSRF-/Webhook-Schutz (S08/10/13/17), Datei- und Archivgrenzen (S11/12, Q15), Schutz öffentlicher Fehlermeldungen und vertraulicher Logs (S14/15/16, Q18), Abhängigkeits-/Lizenzprüfung (S18), Backupverschlüsselung und Löschschutz (S20, Q20), Last- und Kostenmissbrauch (Q01/02/03), Datenminimierung und Cache-Isolation (Q11/16), Idempotenz/Retries/Timeout (Q07/08/09) sowie belastbare Mehrbenutzer-/Negativtests (Q19).

**Technologieneutral:** RLS ist eine mögliche Umsetzung der Datenisolation, nicht vor Stackentscheidung zwingend. Öffentlich freigegebene Konfigurationsschlüssel sind nur dann clientseitig zulässig, wenn sie wirklich keine Secrets sind. CORS/Webhookmaßnahmen gelten nur bei entsprechenden technischen Schnittstellen. Ein generischer Anti-Enumeration-Fehler bei Authentisierung verhindert nicht verständliche, hilfreiche Fehlermeldungen bei anderen Aufgaben. Für Logs gilt Datenminimierung, nicht das grundlose Abschalten notwendiger Betriebsnachweise. Keine kostenpflichtige Sicherheits-, KI- oder Monitoringlösung wird durch die Prüfliste bestellt.

**Release-Gate:** Anwendbare Sicherheitskontrollen sind vor Freigabe mit Negativtests und dokumentierten Ergebnissen zu belegen. Fehlgeschlagene Isolation, Autorisierung, Token-/Schlüsseloffenlegung, definitive Löschung oder Wiederherstellungsprüfungen sperren die entsprechende Freigabe. Die spätere S3-Inbetriebnahme enthält die formale Abnahme; bis dahin alle Nachweise offen. Die spätere Zahlungsfunktion (REL-Q10) und FE-56 werden dadurch nicht vorab freigegeben.

## N2.11 Begrenzter Anschluss der unabhängigen Sicherung

DEC-49 ergänzt SEC-08/09/14/15 und den heutigen Kontrollstand aus N2.8: sicher verwaltete Schlüssel, vom Primäranbieter unabhängiger EU-Speicher, begrenzte Sicherungs-/Abruf-/Restore-/Löschrechte und belegte Wiederherstellbarkeit auch bei Ausfall, Korruption, versehentlicher Löschung oder Kompromittierung. Backupunabhängigkeit hebt weder Benutzerlöschung noch Kontentrennung oder das Verbot privater Klartextschlüssel beim Backend/Admin auf. Periodische Restore-Proben und die Abstimmung endlicher Retention mit Nichtwiederbelebung bleiben nachzuweisen. [ADR-0005](../ARCHITECTURE_DECISIONS.md#adr-0005--anbieterunabhängige-verschlüsselte-sicherung-dec-49), [S2](S2-datenmigration.md), REL-S20/REL-Q20 und [Matrix](ENTSCHEIDUNGSMATRIX.md) konkretisieren Zuständigkeiten. Kein Anbieter, Kryptoverfahren oder Dienst wird gewählt; N2 bleibt ein fachlicher Prüfentwurf mit offenen technischen Nachweisen; [S3](S3-inbetriebnahme.md) liegt inzwischen als fachlicher Betriebsprüfentwurf vor.

## N2.12 Ergänzendes Schutzregister

SEC-01 bis SEC-16 bleiben in N2.2–N2.6 unverändert definiert. Neue Kennungen erweitern ausschließlich Schutz-/Prüfanforderungen bestehender V1-Funktionen, keine Produktbefugnisse.

| Kennung | Schutzanforderung |
|---|---|
| SEC-17 | Direkte und indirekte Prompt Injection |
| SEC-18 | Agentenrechte pro Operation |
| SEC-19 | Isolation von Kontext, Retrieval und Langzeitgedächtnis |
| SEC-20 | Minimale externe KI-Weitergabe |
| SEC-21 | Sichere Dokumente und ausgehende Abrufe |
| SEC-22 | Schlüssel- und Secretlebenszyklus |
| SEC-23 | Vertrauenswürdige CI/CD und Veröffentlichung |
| SEC-24 | Lieferkette von Code, Modellen und Daten |
| SEC-25 | Vorfälle, Schwachstellen und sicherer Rückweg |
| SEC-26 | Datenschutzverantwortung und Betroffenenrechte |
| SEC-27 | Temporäre Transkripte und Zwischenkopien |

## N2.13 Vollständige Schutz- und Prüfprofile

Alle folgenden Profile sind **nicht implementiert und nicht produktgetestet**. Ziele sind Soll-Vorgaben des vorliegenden Prüfentwurfs; technische Ausgestaltung und menschliche Freigaben bleiben erforderlich. [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md), [Referenzrahmen](../quality/REFERENZRAHMEN.md) und [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md) ergänzen Nachweis und Einordnung.

### SEC-01 — Verifizierter Zugang

| Merkmal | Festlegung |
|---|---|
| Ziel | Verifizierter Zugang als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Anmeldung, Registrierung, neue Geräte und optionale Faktoren. |
| Prüfmethode | Unverifiziertes Konto gegen sämtliche Appdaten; abgelaufene/mehrfach benutzte OTP, falsche Versuche, neue Geräte und gefälschte Verifikation. |
| Abnahmekriterium | Kein Datenzugang vor Verifikation; Rate-/Replaygrenzen wirksam; Rollen-MFA nach bestätigter Politik; keine Rohbiometrie oder alleinige SMS-Recovery. |
| Erforderlicher Beleg | Verifikations-/Geräte-/Fehlerversuchsmatrix; REL-S03/S19. |
| Technische Abhängigkeiten | Identitätsanbieter oder eigenes geprüftes Verfahren, serverseitige Statuskontrolle. |
| Offene Parameter | OTP-Fristen, Versuchslimits, unterstützte optionale Faktoren; keine neue allgemeine MFA-Pflicht für alle Nutzer. |

### SEC-02 — Sitzung und Geräteentzug

| Merkmal | Festlegung |
|---|---|
| Ziel | Sitzung und Geräteentzug als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Server-/Gerätesitzungen, lokale Sperre, Online-/Offlinewechsel. |
| Prüfmethode | Ablauf, Tokenreplay, Rotation, Logout auf mehreren Geräten; lokale Entsperrung bei abgelaufener Serversitzung. |
| Abnahmekriterium | Entzug/Ablauf sperrt Folgezugriff; lokale Entsperrung erzeugt keine Serverrechte; keine zugesagte Fernlöschung alter Offlinekopien. |
| Erforderlicher Beleg | Sitzungszustände und negative Folgeaufrufe; REL-S09. |
| Technische Abhängigkeiten | Sicherer Session-/Gerätespeicher und Entzugsmechanismus. |
| Offene Parameter | Sitzungs-/Inaktivitätsdauer, Rotation und Entzugserkennung bestimmen. |

### SEC-03 — Getrennte Recoverywege

| Merkmal | Festlegung |
|---|---|
| Ziel | Getrennte Recoverywege als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Kontorecovery, Admin-MFA-Verlust und persönliche Dokumentenschlüssel. |
| Prüfmethode | E-Mail plus einmaliger Recoverycode; Replay, Geräteverlust, alleinige SMS, erfolgreicher Login ohne Dokumentenschlüssel. |
| Abnahmekriterium | Kontozugriff stellt keine privaten Schlüssel her; Codes einmalig; Adminverlust kein Selbsternennungsweg; fehlender Schlüssel bleibt fehlend. |
| Erforderlicher Beleg | Recovery-/Missbrauchsmatrix; REL-S03/S05/S09/S19, S2. |
| Technische Abhängigkeiten | Persönliches Schlüsselrecoveryverfahren und sichere Identitätsnachweise. |
| Offene Parameter | Verlorene Geräte/Schlüssel, Admin-Bootstrap und Recoveryverfahren vor Aktivierung prüfen. |

### SEC-04 — Durchgängige Serverautorisierung

| Merkmal | Festlegung |
|---|---|
| Ziel | Durchgängige Serverautorisierung als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Alle API-/Objekt-/Job-/Such-/Agenten-/Restorewege. |
| Prüfmethode | Objekt-/Kontokennung manipulieren; Rolle/Flag/Scope ändern während Job wartet; unbekanntes Recht und direktes API trotz versteckter UI. |
| Abnahmekriterium | Aktuelle Schnittmenge sämtlicher Rechte vor Wirkung geprüft; standardmäßig verweigern; kein Vertrauen auf Client oder Modell. |
| Erforderlicher Beleg | Positive/negative Zugriffsmatrix inkl. zeitlicher Rennen; REL-S04/S06/Q19. |
| Technische Abhängigkeiten | Eigentum, Revisionskontrolle und zentrale durchgängige Autorisierung. |
| Offene Parameter | Konkrete Rechteabbildung und atomarer Wirkungszeitpunkt; keine RLS-Pflicht ohne Stackwahl. |

### SEC-05 — Einziger Super Admin

| Merkmal | Festlegung |
|---|---|
| Ziel | Einziger Super Admin als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Getrennte Adminoberfläche, Delegation, Rollenzuweisung und Verlustfall. |
| Prüfmethode | Zweiten Super Admin anlegen, parallele Ernennung, Selbstbeförderung und andere Adminverwaltung als Delegierter versuchen; MFA umgehen. |
| Abnahmekriterium | Genau ein Super Admin; keine exklusive Rechteübertragung; Delegierte eng begrenzt; MFA und sensible Bestätigung, kein pauschaler Privatinhaltzugriff. |
| Erforderlicher Beleg | Rollen-/Parallelitäts-/Auditfälle; REL-S06; Bootstrapnachweis später vor Produktstart. |
| Technische Abhängigkeiten | Identität, serverseitige unverletzliche Rollenregel, sichere Erstbesetzung. |
| Offene Parameter | Technischer Bootstrap/Verlustprozess für S3 vorzubereiten, keine neuen Adminrollen beschließen. |

### SEC-06 — Befristeter Support

| Merkmal | Festlegung |
|---|---|
| Ziel | Befristeter Support als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Freiwillige Hilfe für bestimmte Personen, Zwecke, Objekte und Operationen. |
| Prüfmethode | Kein Grant, falsches Ziel, Schreibversuch bei Leserecht sowie Ablauf/Widerruf zwischen Anzeige und Wirkung. |
| Abnahmekriterium | Nur freigegebener Umfang; keine automatische Verlängerung, kein Schlüsselerwerb; Entzug sperrt weitere Wirkung. |
| Erforderlicher Beleg | Grant-/Ablauf-/Auditmatrix ohne Privattexte; REL-S06/Q11. |
| Technische Abhängigkeiten | Endliche Grants und aktuelle Rechteprüfung, sichere Vorschau. |
| Offene Parameter | Dauergrenzen und minimale Auditfristen je Supportzweck. |

### SEC-07 — Konfiguration, Flags und Quoten

| Merkmal | Festlegung |
|---|---|
| Ziel | Konfiguration, Flags und Quoten als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Konfigurationsvorschau, Testgruppen, Veröffentlichung, Termin und Rollback. |
| Prüfmethode | Direktaufruf deaktivierter Funktion, manipulierte Konfiguration, abgebrochener Release, widerrufener Termin, volle Quote und Rollback nach Rechteentzug. |
| Abnahmekriterium | Unfertige/unfreigegebene Funktionen serverseitig gesperrt; Daten erhalten; Rollback revalidiert heutige Rechte; Vorschau kein Produktivrecht. |
| Erforderlicher Beleg | Release-/Flag-/Quoten-Negativfälle; REL-S06/Q06/Q19. |
| Technische Abhängigkeiten | Validierte persistente Konfiguration und getestetes Releaseartefakt. |
| Offene Parameter | Unterstützte Optionen, Veröffentlichungs-/Rollbackverfahren und Messschwellen offen. |

### SEC-08 — Verschlüsselung und Datenklassen

| Merkmal | Festlegung |
|---|---|
| Ziel | Verschlüsselung und Datenklassen als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Öffentliche Konfiguration, private Kontodaten, sensible Dokumente, Geheimnisse und Betriebsmetadaten. |
| Prüfmethode | Jede Klasse von Quelle bis Transport, Speicherung, Analyse, Ableitung und Backup verfolgen; unsichere Verbindung provozieren. |
| Abnahmekriterium | Mindestens Quellschutz; HTTPS und geschützte Speicher-/Backupebenen; keine Geheimnisse öffentlich; externe Datenweitergabe nur zulässig. |
| Erforderlicher Beleg | Klassifikations-/Datenfluss-/Regionsmatrix und Konfigurationsprüfung; REL-S01/S07/S08/S20. |
| Technische Abhängigkeiten | Technische Kryptokonzeption und Providerprüfung; SEC-26. |
| Offene Parameter | Verfahren, Verantwortliche, Rechtsgrundlagen und konkrete Speicherorte prüfen. |

### SEC-09 — Private Dokumentenschlüssel

| Merkmal | Festlegung |
|---|---|
| Ziel | Private Dokumentenschlüssel als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Geräteerzeugung/-übertragung, Verlust, Wiederherstellung und Rotation. |
| Prüfmethode | Backend-/Adminzugriff und Logs nach privaten Klartextschlüsseln prüfen; Gerätewechsel/Verlust mit und ohne persönlichem Recoverymaterial. |
| Abnahmekriterium | Kein privater Klartextschlüssel beim Backend/Admin; kein Entschlüsseln durch bloßen Kontorecoveryerfolg. |
| Erforderlicher Beleg | Schlüssel-/Zugriffsmatrix und Verlustfälle mit künstlichen Schlüsseln; SEC-22. |
| Technische Abhängigkeiten | Geeignetes geräteseitiges Schlüsselverfahren und persönlicher Recoveryweg. |
| Offene Parameter | Algorithmen, Verteilung, Rotation und Verlustfolgen technisch prüfen; kein Verfahren gewählt. |

### SEC-10 — Explizite temporäre Klartextanalyse

| Merkmal | Festlegung |
|---|---|
| Ziel | Explizite temporäre Klartextanalyse als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Sensible Ausschnitte in eigener Cloud; separate externe KI-Freigabe. |
| Prüfmethode | Keine, falsche, widerrufene oder auf andere Fassung bezogene Einwilligung; Prozessabbruch und Analysefehler; Nebenkanäle wie Diagnose/Queue prüfen. |
| Abnahmekriterium | Nur freigegebener Ausschnitt/Zweck/Vorgang; Servereinsicht ehrlich angezeigt; keine privaten Schlüssel/dauerhaften Kopien; Bereinigung auch im Fehlerpfad. |
| Erforderlicher Beleg | Freigabe-/Datenfluss-/Bereinigungsspuren ohne echten Inhalt; SEC-20/27, REL-Q11. |
| Technische Abhängigkeiten | Operationsbindung und kurzlebige isolierte Verarbeitung. |
| Offene Parameter | Technisch durchsetzbare Lösch-/Speicherfristen und externer Verarbeitungsvertrag offen. |

### SEC-11 — Schutzvererbung

| Merkmal | Festlegung |
|---|---|
| Ziel | Schutzvererbung als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Transkripte, OCR, Zusammenfassungen, Übungen, Karten, Speicher, Index, Push und Export. |
| Prüfmethode | Mehrere Quellen verschiedener Klassen ableiten; Quelle höherstufen/löschen; Vorschau, Suche, Nachricht und Modellkontext prüfen. |
| Abnahmekriterium | Keine stillschweigende Herabstufung; notwendiger Quellschutz bleibt; Teilen nur mit gültiger Folgefreigabe. |
| Erforderlicher Beleg | Schutz-/Ableitungsmatrix und Negativbeispiele; REL-Q11/Q16, SEC-19/27. |
| Technische Abhängigkeiten | Provenienz und Lebenszyklusabhängigkeiten D1/D2. |
| Offene Parameter | Technik für zusammengesetzte Quellen und Schutzänderungen; Fristen abstimmen. |

### SEC-12 — Unvertrauenswürdige Eingaben

| Merkmal | Festlegung |
|---|---|
| Ziel | Unvertrauenswürdige Eingaben als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Text, Markdown, Archiv, Medien, Webseite, Repository und Modellausgabe. |
| Prüfmethode | Pfadflucht, Bomben, Formatfälschung, Skript-/HTML-/Formelinjektion, schadhafte Ausgabe und unbekannte Konnektor-URL anbieten. |
| Abnahmekriterium | Keine Programmausführung/Privilegien aus Inhalt; sichere Anzeige und Ausgabevalidierung; begrenztes Entpacken/Verarbeiten; unbekannter Konnektor nicht installiert. |
| Erforderlicher Beleg | Angriffskorpus, Parser-/Darstellungs-/Grenzfälle; REL-S10/S11/S12, REL-A07. |
| Technische Abhängigkeiten | Isolierte begrenzte Verarbeitung, sichere Ausgabeencoder, geprüfte Connectorregistry. |
| Offene Parameter | Unterstützte Formate, Ressourcenlimits und Isolationsverfahren offen. |

### SEC-13 — Autorisierte Integrationen

| Merkmal | Festlegung |
|---|---|
| Ziel | Autorisierte Integrationen als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Offizielle Verbindungen, externe Kalender strikt lesend, GitHub nur ausdrücklich erlaubte Repositories. |
| Prüfmethode | Scopeausweitung, widerrufener Token, Jobretry und unbekannter Erfolg; Import-/KI-Kalendervorschlag gegen manuellen Speichervorgang vergleichen. |
| Abnahmekriterium | Keine externe Kalenderänderung; jede Wiederholung reautorisiert; Import und KI-Vorschlag vor Speicherung bestätigt, direktes manuelles Speichern ohne künstliche Zweitbestätigung. |
| Erforderlicher Beleg | Verbindungs-/Scope-/Kalender-/Retryfälle; REL-S06/Q07/Q08. |
| Technische Abhängigkeiten | Offizielle Anbieterrechte, freigegebene Adapter und Ergebnissynchronisation. |
| Offene Parameter | Konkrete Anbieter und Scopes; Abo ist kein automatisches API-Recht. |

### SEC-14 — Private endliche Auditnachweise

| Merkmal | Festlegung |
|---|---|
| Ziel | Private endliche Auditnachweise als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Anmeldung, Administration, Integration, KI-Verbrauch, Fehler und Diagnose. |
| Prüfmethode | Künstliche Passwörter/OTP/Tokens/URLs/Schlüssel/Inhalte in Fehlerpfaden; fremden Auditabruf sowie Fristablauf prüfen. |
| Abnahmekriterium | Keine Geheimnisse/unnötigen Inhaltskopien; privater zweckgebundener Zugriff; korrelierbare endliche Metadaten; keine Standard-Supporteinsicht. |
| Erforderlicher Beleg | Feldschema, Scan und Rechte-/Retentionsprüfung; REL-S14/S15/Q18. |
| Technische Abhängigkeiten | Redaktion vor Protokollierung, Zugriffskontrolle und Bereinigung. |
| Offene Parameter | Pflichtfelder, Aufbewahrungszwecke und rechtliche Reste festlegen. |

### SEC-15 — Löschen und Nichtwiederbelebung

| Merkmal | Festlegung |
|---|---|
| Ziel | Löschen und Nichtwiederbelebung als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Nutzerwünsche, Papierkorb, Derivate, Index, Cache, Offlineclients und Backups. |
| Prüfmethode | Mehrdeutigen KI-Löschauftrag, endgültige Löschung, altes Paket/Client/Backup, neue Ableitung und abgebrochenen Purge prüfen. |
| Abnahmekriterium | Konkrete Ziele bestätigt; keine ungewollte Originalkaskade; keine Wiederbelebung; noch bestehende legitime Reste/Fristen wahrheitsgemäß benannt. |
| Erforderlicher Beleg | Lebenszyklus-/Restore-Negativmatrix; S2, REL-Q16/Q20. |
| Technische Abhängigkeiten | Heutiger Kontrollstand unabhängig von altem Backup; endliche kompatible Marker. |
| Offene Parameter | Aufbewahrung, Backupablauf, Altclientgültigkeit und Löschbeweis abstimmen. |

### SEC-16 — Kontopause, Sperre und Löschung

| Merkmal | Festlegung |
|---|---|
| Ziel | Kontopause, Sperre und Löschung als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Nutzerkonto, administrative Sperre, Verbindungen, Sitzungen und Export. |
| Prüfmethode | Pause/Rückkehr, gesperrtes Konto, Löschung mit/ohne Identitätsnachweis und unterprivilegierter Admin; laufende Jobs einbeziehen. |
| Abnahmekriterium | Pause/Sperre nicht mit Löschung verwechseln; Löschung bestätigt, optionaler Export; Sessions/Verbindungen beendet; Sperrgrund und Prüfung nachvollziehbar. |
| Erforderlicher Beleg | Konto-/Session-/Job-/Purgefälle; REL-S06/S09/Q20. |
| Technische Abhängigkeiten | Konto-Zustandsmodell und geregelter Löschablauf. |
| Offene Parameter | Fristen, zulässige Pflichtreste und Verfahren für Überprüfung administrativer Sperren. |

### SEC-17 — Direkte und indirekte Prompt Injection

| Merkmal | Festlegung |
|---|---|
| Ziel | Direkte und indirekte Prompt Injection als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Systemanweisungen gegenüber Nutzertext, Dokumenten, Transkripten, Webseiten, Repositories, Retrieval und Werkzeugausgaben. |
| Prüfmethode | Rollentausch, kodierte/mehrsprachige Befehle, gefälschte Toolausgaben und gestufte Angriffe in vertrauensschwachen Quellen. |
| Abnahmekriterium | Inhalt kann keine Rechte, Scopes, Empfänger oder Systemregeln ändern; keine fremden Daten/Secrets oder unbestätigten Wirkungen. Restfehler als Befund, nicht als Modellgarantie behandeln. |
| Erforderlicher Beleg | Versionierter Angriffskorpus mit beobachteten Tool-/Datenwirkungen; REL-A01. |
| Technische Abhängigkeiten | Explizite Vertrauensgrenzen plus unabhängige Serverautorisierung; Filter allein reicht nicht. |
| Offene Parameter | Angriffskorpus, Restrisiko- und Wiederholungsbewertung bei Modell-/Promptwechsel. |

### SEC-18 — Agentenrechte pro Operation

| Merkmal | Festlegung |
|---|---|
| Ziel | Agentenrechte pro Operation als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Werkzeugauswahl, Parameter, Zielobjekt, externe Weitergabe, Lösch-/Kalender-/Kostenwirkung und Retry. |
| Prüfmethode | Manipulierte Toolargumente und Zieladressen; Rechteänderung nach Vorschau; Modell behauptet Bestätigung; doppelte Ausführung. |
| Abnahmekriterium | Nur erlaubtes Tool und validierte Operation im aktuellen Umfang; sensible Wirkung benötigt echte Nutzerbestätigung; Modelltext ist keine Autorisierung. |
| Erforderlicher Beleg | Tool-/Operationsmatrix, TOCTOU-/Deduplizierungsfälle; REL-S06/Q03/Q09. |
| Technische Abhängigkeiten | Serverseitige Toolregistry, Schemaprüfung, Vorschau- und Operationsbindung. |
| Offene Parameter | Technische Bestätigungsbindung und zulässige Aktionsklassen; keine generelle Agentenvollmacht. |

### SEC-19 — Isolation von Kontext, Retrieval und Langzeitgedächtnis

| Merkmal | Festlegung |
|---|---|
| Ziel | Isolation von Kontext, Retrieval und Langzeitgedächtnis als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Nachrichtenhistorie getrennt von pädagogischem Langzeitgedächtnis; Vektoren, Embeddings, Cache und geteilte Inferenceprozesse. |
| Prüfmethode | A/B mit ähnlichen Dokumenten, manipulierte Retrievalfilter, wiederverwendete Sessions/Batches und gelöschte Quellen; Indexneubau/Restore. |
| Abnahmekriterium | Keine kontofremde Information in Prompt, Treffer, Antwort, Cache oder Statistik; Rechte vor Kontextaufbau; Speicher nur aus zulässigen Belegen. |
| Erforderlicher Beleg | Kontext-/Retrieval-Negativmatrix und bereinigte Kontaminationsnachweise; REL-S04/Q16/Q19. |
| Technische Abhängigkeiten | Eigentums-/Quellschutzmetadaten auf jedem Indexeintrag und Lebenszykluspfad. |
| Offene Parameter | Gewählte Retrieval-/Vektortechnik und nachvollziehbare Speicherrevisionen offen. |

### SEC-20 — Minimale externe KI-Weitergabe

| Merkmal | Festlegung |
|---|---|
| Ziel | Minimale externe KI-Weitergabe als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Prompt, Kontext, Datei, Telemetrie und Fallback an externe Provider. |
| Prüfmethode | Falscher/kein Providergrant, zu großer Kontext, sensibler Ausschnitt, Scopewiderruf und Anbieterausfall; ausgehende Payload erfassen. |
| Abnahmekriterium | Nur genehmigter Anbieter/Zweck/Kategorie und minimal nötige Daten; kein stiller Fallback, Training/Retention nur nach geprüften Bedingungen; keine bezahlte API ohne Freigabe. |
| Erforderlicher Beleg | Provider-/Datenflussmatrix und geschützte Payloadprüfung; REL-Q11/S06/S15. |
| Technische Abhängigkeiten | Offizielle Anschlussbedingungen, Datenminimierung und ausgehende Zugriffskontrolle. |
| Offene Parameter | Provider, Aufbewahrung, Trainingseinstellungen, Regionen und Vertragsrollen prüfen. |

### SEC-21 — Sichere Dokumente und ausgehende Abrufe

| Merkmal | Festlegung |
|---|---|
| Ziel | Sichere Dokumente und ausgehende Abrufe als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Datei-/Archivverarbeitung und serverseitiger Abruf nutzer-/modellgelieferter URLs. |
| Prüfmethode | Private, Loopback-, Link-Local-/Metadatenziele, DNSwechsel, Redirectketten, andere Protokolle, riesige/aktive Dokumente und Repositories testen. |
| Abnahmekriterium | Unvertrauenswürdige Abrufe erreichen keine internen Netze/Metadaten; Zielprüfung auch nach Auflösung/Redirect; keine Codes aus Imports; zulässige Abrufe bleiben begrenzt. |
| Erforderlicher Beleg | SSRF-/Dokumentkorpus mit Netzwerkbelegen; REL-A07, REL-S10/S12. |
| Technische Abhängigkeiten | Ausgehende Netzgrenze, sichere Parser und Abrufregeln; intern nötige Dienste getrennt explizit autorisiert. |
| Offene Parameter | Adress-/Protokollregeln, DNS-/Redirectbehandlung und Parserisolation technisch ausarbeiten. |

### SEC-22 — Schlüssel- und Secretlebenszyklus

| Merkmal | Festlegung |
|---|---|
| Ziel | Schlüssel- und Secretlebenszyklus als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Servicecredentials, OAuth, CI, Sicherung, persönliche Dokumentenschlüssel und öffentliche Konfiguration. |
| Prüfmethode | Erzeugung, Speicherung, minimale Berechtigung, Rotation, Entzug, Verlust und Kompromittierung je Klasse durchspielen; Client/Git/Logs scannen. |
| Abnahmekriterium | Keine Secrets öffentlich; Rollen und Speicher getrennt; Rotation/Entzug stoppt alte Credentials; Backuprecovery ohne unzulässige persönliche Schlüsseloffenlegung. |
| Erforderlicher Beleg | Secret-/Schlüsselinventar ohne Werte und Rotation-/Entzugstest; REL-S01/S02/S07/S20. |
| Technische Abhängigkeiten | Später gewählte sichere Secretverwaltung und unabhängiger Recoveryzugang. |
| Offene Parameter | Verfahren, Verantwortliche, Rotationsanlässe und Fristen; kein konkreter Algorithmus gewählt. |

### SEC-23 — Vertrauenswürdige CI/CD und Veröffentlichung

| Merkmal | Festlegung |
|---|---|
| Ziel | Vertrauenswürdige CI/CD und Veröffentlichung als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Pull Requests, Build, Abhängigkeiten, Artefakte, Releasefreigabe und spätere Bereitstellung. |
| Prüfmethode | Unvertrauenswürdigen PR/Fork, manipuliertes Artefakt, veränderte Abhängigkeit und fehlende Freigabe simulieren; Berechtigungen prüfen. |
| Abnahmekriterium | Kein Produktionssecret für untrusted Code; minimale kurzlebige Rechte soweit unterstützt; überprüfbarer Quell-/Build-/Artefaktbezug; keine Veröffentlichung ohne Gates. |
| Erforderlicher Beleg | Pipeline-/Rechte-/Provenienz- und Manipulationstests; REL-A13. |
| Technische Abhängigkeiten | Spätere Pipeline-/Artefakt-/Branchschutzkonzeption; derzeit keine Apppipeline. |
| Offene Parameter | Technische Signatur-/Integritätsprüfung und Releaseverantwortung offen; keine CI hier einrichten. |

### SEC-24 — Lieferkette von Code, Modellen und Daten

| Merkmal | Festlegung |
|---|---|
| Ziel | Lieferkette von Code, Modellen und Daten als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Bibliotheken, Images, Modelle/Gewichte, Tokenizer, Prompts, Korpora, Konnektoren und Lizenzen. |
| Prüfmethode | Version/Herkunft/Hash/Lizenz inventarisieren; manipulierte Komponente und vergiftete Testquelle einschleusen; Schwachstellenbefunde bearbeiten. |
| Abnahmekriterium | Nur nachvollziehbar geprüfte Fassungen; keine unbekannte Konnektorinstallation; unvereinbare Lizenz oder kritische ungeklärte Manipulation blockiert Nutzung. |
| Erforderlicher Beleg | Komponenten-/Modell-/Lizenzinventar und Schwachstellen-/Integritätsbelege; REL-S18, REL-A13. |
| Technische Abhängigkeiten | Quellvertrauen, Integritätsprüfung und Updateprozess. |
| Offene Parameter | Komponentenauswahl, Scanningverfahren, Reaktionsfristen und akzeptable Restrisiken bestätigen. |

### SEC-25 — Vorfälle, Schwachstellen und sicherer Rückweg

| Merkmal | Festlegung |
|---|---|
| Ziel | Vorfälle, Schwachstellen und sicherer Rückweg als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Monitoring, Sicherheitsmeldung, Eindämmung, Schlüsselentzug, Artefaktrollback und Wiederanlauf. |
| Prüfmethode | Kompromittierung synthetisch melden; Zugriff entziehen; primären Provider verlieren; vorherige Version unter aktuellen Löschungen/Rechten wiederherstellen. |
| Abnahmekriterium | Vorfall erkannt/zugeordnet, Auswirkung begrenzt, verantwortliche Person erreichbar; Rollback umgeht keine heutigen Sicherheitszustände; Restore nach DEC-49 nachgewiesen. |
| Erforderlicher Beleg | Zeitlinie, bereinigte Alarme, Maßnahmen-/Restore-/Rollbacknachweis; REL-Q17/Q18/Q20. |
| Technische Abhängigkeiten | Monitoring, unabhängige Sicherung und vorbereitete Verantwortlichkeiten; keine fertige S3-Prozedur. |
| Offene Parameter | Reaktions-/Meldezeiten, Übungsrhythmus und Sicherheitskontakt vor Produktstart festlegen. |

### SEC-26 — Datenschutzverantwortung und Betroffenenrechte

| Merkmal | Festlegung |
|---|---|
| Ziel | Datenschutzverantwortung und Betroffenenrechte als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Verantwortlicher/Auftragsverarbeiter, Zweck, Datenkategorie, Rechtsgrundlage, Auskunft/Korrektur/Export/Löschung und Transfers. |
| Prüfmethode | Verarbeitungstätigkeiten zuordnen; synthetisches Auskunfts-/Löschgesuch durch alle Derivate verfolgen; Anbieterbedingungen und mögliche DSFA-Pflicht fachlich prüfen. |
| Abnahmekriterium | Keine ungeklärte unzulässige Verarbeitung freigeben; Rollen, Zweck/Grundlage und Fristen dokumentiert; Rechte ausführbar; EU-Standort allein ist kein DSGVO-Nachweis. |
| Erforderlicher Beleg | Verarbeitungs-/Vertrags-/Rechtematrix und Datenschutzprüfung; REL-Q11/Q20. |
| Technische Abhängigkeiten | Rechtlich geeignete Prüfung durch zuständige Personen; gültiger Normtext. |
| Offene Parameter | Aktueller konsolidierter Text, Rollen, Rechtsgrundlagen, besondere Kategorien, DSFA und Transferprüfung ausdrücklich offen. |

### SEC-27 — Temporäre Transkripte und Zwischenkopien

| Merkmal | Festlegung |
|---|---|
| Ziel | Temporäre Transkripte und Zwischenkopien als durchsetzbare Schutzgrenze. |
| Geltungsbereich | Audio/Video, Transkription, OCR, entpackte Dateien, Modell-/Job-Zwischenstände und temporärer Klartext. |
| Prüfmethode | Normalabschluss, Abbruch, Timeout, Worker-/Netzfehler, Backup/Log/Cacheaufnahme und verspäteten Retry prüfen. |
| Abnahmekriterium | Nur erforderliche Kopien und begründete endliche Lebensdauer; keine Schattenarchive; dauerhaft übernommene pädagogische Notiz ist eigener geschützter Datensatz mit Herkunft. |
| Erforderlicher Beleg | Temporärspeicher-/Queue-/Cache-/Loginventar und Bereinigungsbeleg je Fehlerpfad; REL-Q11/Q16/Q20. |
| Technische Abhängigkeiten | Lebenszyklussteuerung, sichere temporäre Verarbeitung und Löschkontrolle. |
| Offene Parameter | Fristen, sichere Löschgrenzen und zulässige dauerhafte Übernahmen bestimmen; keine garantierte physische RAM-Löschung behaupten. |

## N2.14 Bedrohungen und Vertrauensgrenzen

| Grenze / Schutzgut | Missbrauch oder Ausfall | Verbindliche Gegenprüfung |
|---|---|---|
| Nicht angemeldet → Konto / neues Gerät | Verifikation, Recovery oder Sessions umgehen | SEC-01/02/03; Rate-/Replay-/Entzugsfälle |
| Konto A → Konto B / Such- und Modellkontext | Fremde Kennung, Retrievalfilter, Batch- oder Cachevermischung | SEC-04/19; auch parallele Jobs und Restore |
| Delegierter → Super Admin / private Inhalte | Selbstbeförderung, zweiter Super Admin, unbegrenzter Support | SEC-05/06/07; aktuelle Serverrechte und MFA |
| Nutzer-/Quelltext → Steuerung / Werkzeug | Direkte oder indirekte Prompt Injection, schadhafte Ausgabe, erfundene Bestätigung | SEC-12/17/18; Toolparameter unabhängig vom Modell prüfen |
| Import/URL → Parser / internes Netz | Archivbombe, aktive Datei, SSRF, Redirect/DNSwechsel | SEC-12/21; begrenzte isolierte Verarbeitung und ausgehende Netzgrenze |
| Eigene Cloud → externer Anbieter | Geheimnis-/Sensitivdatenabfluss, Training/Retention unzulässig | SEC-08/10/20/26; zweckgebundene minimale Freigabe, keine stille Ersatz-KI |
| Privates Gerät → Cloudanalyse / Schlüsselspeicher | Klartext bleibt in Logs, temporären Dateien oder Backup; Kontoerfolg entschlüsselt alles | SEC-03/09/10/11/22/27 |
| Quellrepository → Build → Release | Fremder PR erhält Secret, Artefakt-/Modellmanipulation | SEC-23/24; Herkunft und Veröffentlichungsgates |
| Primäranbieter → unabhängige Sicherung / Restore | Anbieter-/Schlüsselverlust, alte Rechte oder gelöschte Daten kehren zurück | SEC-15/22/25; N2.8, DEC-49 und S2 |

**Betrachtete Akteure:** nicht angemeldete Angreifer, ein anderes Benutzerkonto, ein kompromittiertes Gerät/eine Sitzung, überberechtigte Delegierte, abgelaufener Support, manipulierte externe Quellen/Anbieter und eine kompromittierte Liefer-/Buildkette. Auch unbeabsichtigte Fehler, Ausfälle und Ressourcenmissbrauch sind einzubeziehen.

**Datenklassen und zulässiger Umgang:** Die Einordnung ist eine fachliche Schutzzuordnung, keine neue Rechtsgrundlage oder pauschale Freigabe.

| Klasse / Beispiele | Verarbeitung und Sichtbarkeit | Weitergabe / Lebenszyklus |
|---|---|---|
| Ausdrücklich öffentliche Inhalte, z. B. freigegebenes Branding | Nur tatsächlich veröffentlichte Fassung öffentlich; Entwurf und interne Konfiguration bleiben zugriffsgeschützt. | Veröffentlichung benötigt bestehendes Recht; kein Secret oder Privatinhalt wird durch Brandingkonfiguration öffentlich legitimiert. |
| Private Konto-/Lerndaten: Profil, Gespräche, Module, Projekte, Noten, Kompetenzen | Eigentumsgebunden, verschlüsselte Übertragung/Haltung; Administration ohne Standardinhaltsrecht. Nachrichtenhistorie und pädagogische Langzeitbelege getrennt verwalten. | Externe Verarbeitung nur erlaubter minimaler Umfang; Herkunft, Auskunft, Korrektur, Export und kontrollierte Löschung einschließlich Derivaten. |
| Zusätzlich geschützte sensible Dokumente und Ableitungen | Geräteseitiger Zusatzschutz; private persönliche Schlüssel nicht im Klartext an Backend/Admin. Eigene Cloud sieht nur pro Vorgang freigegebene notwendige Ausschnitte. | Drittanbieter zusätzlich separat zulässig/freigegeben; Quellschutz vererben; keine dauerhaften Cloud-Klartextschattenkopien. Rechtliche besondere Kategorien gesondert prüfen. |
| Service-/Sitzungs-/Recoverygeheimnisse und Schlüsselmaterial | Zweckgebunden getrennte geschützte Ablage und minimale Rechte; persönliche private Dokumentenschlüssel nur nach SEC-09. Keine Geheimniswerte in öffentlichem Client, Git oder Logs. | Kein persönlicher Datenexport aktiver Credentials; sichere technische Sicherung getrennt; Rotation/Entzug und endliche Gültigkeit nach bestätigtem Verfahren. |
| Temporäre Medien-/Transkript-/OCR-/Modellzwischenstände | Nur für notwendigen Vorgang, begrenzte Verarbeitung, gleiche oder höhere Schutzklasse als Quelle. | Endliche Bereinigung nach Erfolg, Fehler oder Abbruch; keine automatische Aufnahme in dauerhafte Logs/Backups. Bewusst übernommene pädagogische Notiz erhält eigenen Herkunfts-/Schutznachweis. |
| Audit-/Betriebsmetadaten und minimale Lösch-/Deduplizierungsmarker | Private zweckgebundene Metadaten ohne unnötige Inhalte; Zugriff nicht pauschal für Support oder fremde Konten. | Begründete endliche Fristen, zulässige Pflichtreste und Nichtwiederbelebung zusammen nachweisen; keine unbegrenzte Schattenhistorie. |

Die Auflistung ist eine auf Syllentra bezogene fachliche Bedrohungsanalyse, kein vollständiger Penetrationstest. Modellanweisungen, Inhaltsfilter und bloßes Verbergen der Oberfläche ersetzen niemals Autorisierung, Quellschutz oder Netzwerkgrenzen. Vertrauenswürdige Konfiguration ist versioniert, zugriffsgeschützt und validiert; fremde Quellen bleiben auch nach Import unvertrauenswürdige Daten.

## N2.15 Offene technische und menschliche Freigaben

Vor betroffener Aktivierung sind Identitäts-/Session-/Schlüsselverfahren, Recovery und einziger Super-Admin-Bootstrap, Datenschutzrollen/-grundlagen, zulässige Providerbedingungen, Secret-/CI-Konzept, Ressourcen-/Retentionsgrenzen und die unabhängige Restorefähigkeit zu bestätigen und technisch nachzuweisen. WCAG-Ziel und pädagogische Bewertungsrubriken brauchen die in N1 genannten Entscheidungen. FE-56 ist für V1 als Ausschluss von Postfachlektüre, -synchronisation und -überwachung bestätigt; eine spätere Integration bleibt unverbindlich; keine Inboxfunktion wird freigegeben. DEC-48 ist eine Bewertungspriorität, DEC-49 eine Sicherungsanforderung, keine Infrastrukturfreigabe.

Die [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md) ordnen Erstveröffentlichung, Funktionsaktivierung, Regression und periodische Nachweise zu. Sie liefern die Gates für [S3](S3-inbetriebnahme.md); dessen Bootstrap-, Recovery-, Freigabe- und Incidentabläufe sind spezifiziert, aber keine ausgeführten Betriebsverfahren. Kein Kryptoverfahren, Anbieter, Framework, Modell, kostenpflichtiger Dienst oder neues Nutzungsrecht wird durch N2 gewählt.

## N2.16 Schutzgrenzen für Töne und Stimmen

AUDIO-01/02/03 konkretisieren SEC-02/04/05/06/07/11/13/14/19/20/24/26/27; keine neue SEC-/FE-/DEC-V1-Kennung und durch diese Audioanforderungen keine Änderung der in N2.2 (Mission 14, R1/R4) bestätigten Identitäts- und Recoveryentscheidungen. Sollfälle: [B1.13](B1-dialogspezifikation.md#b113-abnahmeszenarien-für-töne-und-stimmen).

1. **Rechte und Steuerung:** TTS-Ausgabe, Mikrofonaufnahme und OS-/Push-Freigabe sind getrennte Vorgänge. Nur Hören verlangt kein Mikrofonrecht. Persönlicher Hörmodus ist freiwillig und standardmäßig aus; gespeicherte Präferenzen oder deren Geräteabgleich aktivieren nach Gerätewechsel/erneuter Anmeldung keine ungeprüfte Hörsitzung. Vor Start/Fortsetzen und weiterer Erzeugung heutige Konto-/Geräte-/Inhalts-/Anbieterrechte und Serverflags prüfen.
2. **Entzug:** Bei erkanntem Rechte-/Sitzungs-/Providerverlust laufende unzulässige Ausgabe, Warteschlange und Folgeaufträge sofort stoppen; temporäre zugängliche Kopien nach gültigen Löschregeln bereinigen. Technische Erkennungs-/Synchronisationsfristen bleiben nachzuweisen. Ein unerreichbares Gerät kann nicht garantiert augenblicklich unterbrochen oder rückwirkend „ungehört“ gemacht werden. Offlinefreigabe und zulässige lokale Gültigkeit sind vor Aktivierung zu klären, kein stiller Offline-Ausweg.
3. **Minimale Weitergabe:** Auch eine vom Browser angebotene Stimme ist nicht automatisch lokal. Tatsächlichen Verarbeitungsort, Motor und Datenfluss feststellen; kein persönlicher Inhalt an entfernten TTS-Motor ohne passende Anbieter-/Kategorie-/Zweckfreigabe und geprüfte Bedingungen. Vorschau nur mit neutralem Text, keine privaten Notizen/Gespräche im Vorschauauftrag, in Push/Sperrbildschirm oder Diagnosen. Stimme/Audiodateien dürfen ohne geeignete Einwilligung nicht zum Training Dritter genutzt werden. Play-Klick ist weder Trainings-, Mikrofon- noch pauschale Anbieterfreigabe.
4. **Kontentrennung und Lebenszyklus:** Persönliche Ton-/Stimmenwerte und temporäre Audioableitungen bleiben kontogebunden. Puffer, Caches, Vorschauen und Wiedergabeposition erben Schutz und endliche Retention; Quelllöschung/Entzug verbietet Wiederbelebung durch Replay, Restore oder veraltete Geräte. Statistik protokolliert keine gesprochenen Privattexte. Neutraler Referenztext ersetzt keine Lizenz-/Datenschutzprüfung eines Dienstes.
5. **Administrationsgrenze:** Getrennte Administration verwaltet Kataloge/Motoren/Stimmen, servergeprüfte Verfügbarkeit/Rollenflags, Quoten und Kostenrahmen samt Rücknahme. Sie besitzt dadurch weder Inhaltsleserecht noch persönliche Opt-in-Vollmacht. Globaler Providerentzug sperrt betroffene Ausgabe, Rollback umgeht keine heutigen Rechte. UI-Verbergen allein ist keine Sperre. Keine funktionsfähige Administration wird in Mission 15 implementiert.
6. **Vertrauenswürdige Kataloge und Kosten:** Keine Ton-/Motorinstallation oder Codeausführung durch bloße URL. Herkunft/Fassung, Audio-/Stimmenrechte, Software-/Gewichtslizenzen und Lieferkette prüfen; externe Region, Aufbewahrung, Training und Vertragsrollen bleiben zur Bewertung. Keine obligatorische bezahlte API und keine Kosten ohne ausdrückliche Freigabe; unklare Kosten sperren kostenpflichtige Nutzung statt stillen Fallbacks.

Lautlos für optionale Benachrichtigungen beseitigt keine visuellen Hinweise und ändert keine Zustellrechte/Ruhezeiten. Bewusstes Probehören und manuelles TTS sind getrennte Aktionen, kein Umgehen eines ausgeschalteten Hörmodus. Reset setzt keine Datenschutzentscheidung zurück. Verfahren für Entzugserkennung, sichere Audiopuffer und tatsächlich unterstützte lokale/entfernte Stimmen bleiben technische offene Punkte; kein Schutztest als bestanden behauptet.
