# N2 — Querschnittskonzepte

**Projekt:** Syllentra AI\
**Version:** 0.2\
**Stand:** 16.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

## N2.1 Zweck und Ausarbeitungsgrenze

Dieser begrenzte Konzeptentwurf verbindet bereits beschlossene Schutzanforderungen. Er ist kein implementiertes Sicherheitskonzept, kein Schema, kein ausgewähltes Authentifizierungsprodukt und keine fertige Kryptospezifikation. [D1](D1-datenmodell.md) beschreibt Entitäten und Invarianten, [D2](D2-datentypen.md) Werte, [S1](S1-nachbarsysteme.md) die Nachbargrenzen. Konkrete technische Verfahren benötigen spätere Prüfung, ohne die festgelegten Grenzen aufzuheben.

## N2.2 Konten, Authentifizierung und Sitzungen

- **SEC-01 — Verifizierter Zugang (FE-37, FE-38, FE-59 bis FE-62):** Offene Registrierung mit E-Mail und Passwort; E-Mail-OTP vor jedem erstmaligen Anwendungsdatenzugang. Unverifizierte Konten dürfen nur den beschränkten Verifikations-/Recoveryweg nutzen. Bekannte Geräte melden sich normal mit Passwort an; neue Geräte verlangen zusätzliche berechtigte Verifikation. Optionale Passkeys, OS-Biometrie, TOTP und SMS nur bei tatsächlicher Unterstützung; keine Rohbiometrie an Syllentra. SMS ist niemals alleiniger sensibler Recoverynachweis.
- **SEC-02 — Getrennte Zustände (FE-36 bis FE-39, FE-61, FE-62):** Konto, Gerät, Serversitzung, lokale Sperre und Dokumentenschlüssel sind getrennt. Mehrtagessitzung und konfigurierbare lokale Inaktivitätssperre sind Ziele ohne erfundene Dauer. Lokales OS-Biometrie-/PIN-Entsperren verlängert keine abgelaufene Serversitzung. Neue Geräte durch bestehendes berechtigtes Gerät oder sichere Wiederherstellung bei Verlust autorisieren; Entzug sperrt weitere Zugriffe, beweist keine Fernlöschung bereits vorhandener Offlinekopien.
- **SEC-03 — Recovery (FE-38, FE-70, FE-77):** Persönliche einmal nutzbare Kontorecoverycodes zusammen mit verifizierter E-Mail; Admin-MFA mit gesichertem Wiederherstellungsweg. Dokumentenschlüssel werden gesondert persönlich wiederhergestellt. Kontoerfolg ist kein Dokumentenschlüsselnachweis. OTP-/Versuchs-/Sitzungsgrenzen und konkrete Nachweisverfahren bleiben O-S1-06/07.

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

**Planung:** Reimport erhält manuelle Herkunft/Terminbindung und jüngere Lernbelege. Restore oder Plan-Undo darf diese nicht still überschreiben. S2 führt keine neue automatische Lernheftordnung aus und ändert keine Kalenderbestätigungsgrenze. Die separate vollständige Post-S1-Harmonisierung der DEC-V1-Vorgaben bleibt offen.
