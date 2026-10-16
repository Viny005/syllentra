# S1 — Nachbarsysteme und fachliche Schnittstellenverträge

**Projekt:** Syllentra AI\
**Version:** 0.2\
**Stand:** 16.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber\
**Ausgangsstand:** `ace1d80e80245379beed02296c3c4dd184c8dd70` auf `docs/spec/p1-p2-mobile-workspaces`, bestehende [PR #1](https://github.com/Viny005/syllentra/pull/1).

## S1.1 Zweck, Systemgrenze, Quellen und Vertragskonventionen

S1 beschreibt Operationen, Austauschrichtungen, fachliche Eingaben/Ergebnisse, Rechte, Fehler und Wiederanlauf an den zwölf in [P2](P2-architekturueberblick.md) definierten Nachbarn. Die [Herold-S1-Referenz](https://github.com/carstenlucke/herold/blob/main/docs/spec/S1-nachbarsysteme.md) wurde am 16.10.2026 im Git-Stand `fce50b47ae646a70bf4d796026dcd1a99d3ae3c2` gelesen. Übernommen wird die Vertragsmethode, nicht Herolds kostenpflichtige Anbieter, GitHub-Schreiboperationen oder rein synchrone Verarbeitung. Konkrete Endpunkte, Scopestrings, Verschlüsselungsprodukte, Framework, Datenbank und Anbieter bleiben offen. Eine fachliche Signatur ist keine technische API und kein Nachweis vorhandener Implementierung.

V1 ist eine offene Mehrbenutzerplattform mit isolierten persönlichen Konten, einem Super Admin und eingeschränkt delegierten sekundären Admins. Verifikation per E-Mail-OTP geht dem erstmaligen Zugriff auf Anwendungsdaten voraus; zuvor bleiben nur beschränkte Verifikations-/Recoveryfunktionen erreichbar. Normale Wiederanmeldung und Sitzungsentsperrung folgen FE-61/62. Der eigene PWA-Client, die eigene zentrale EU-Cloud, interne KI und Sicherungen gehören zur Produktgrenze. Der persönliche PC ist kein notwendiger Server; andere Konten sind keine freigegebenen Quellen. Adminrolle gewährt kein Inhaltsleserecht. Optionaler externer Speicher ist ausschließlich NB-10, nicht der interne Betrieb.

Alle hier beschriebenen Verbindungen sind Soll-Verträge. Kein Produktkonnektor, Mail-/Pushdienst, Sprachdienst oder Providerrecht wurde in dieser Dokumentationsarbeit aktiviert oder getestet. FE-56 bleibt ausdrücklich offen. Die bestätigten Vorgaben und neue konkrete Modell-/Vertragspräzisierungen sind von der ausstehenden Abnahme getrennt. Keine zukünftige Spielezone oder Developer-Skill-Installation wird V1-Pflicht.

**Bestandsaufnahme vor Bearbeitung:** P1 0.5, P2 0.6, F1 0.2, F2/F3/D1/D2/B1/B2/B3 jeweils 0.1 und README waren vorhanden. S1, S2, S3, N1, N2, E2 fehlten. Einschlägige Grundlagen: [Projektvision](../PROJECT_VISION.md), [Anforderungen](../REQUIREMENTS.md), [Architekturentscheidungen](../ARCHITECTURE_DECISIONS.md), [Roadmap](../ROADMAP.md). Der entfernte Branch und PR-Head entsprachen dem Ausgangsstand. Die GitHub-Metadaten-API lieferte auch nach Wiederholung HTTP 403; der offene PR-Status aus dem Anhang konnte daher nicht unabhängig erneut bestätigt werden. Verifizierbar sind Git-Refs und Inhalt; kein automatisches Merge.

**Gemeinsamer Vertrag:** Jeder Aufruf trägt einen fachlich bestimmten Kontobezug, Zweck, zulässigen Umfang und soweit nötig konkreten Auftrag, Freigabe, Quell-/Zielfassung und Kostenrahmen. Fehlender/unbekannter Nachweis ist keine positive Freigabe. Erfolg, partielle Wirkung und Ungewissheit werden getrennt beschrieben. Unveränderte Quellen dürfen nur nach tatsächlich erfolgreichem vergleichbarem Abruf als unverändert gelten. Dokumente/Quelltexte/Modellantworten sind Daten, keine Autorisierungsbefehle.

## S1.2 NB-01 — Benutzergeräte und ihre Betriebssystemumgebung

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | PWA- und Betriebssystemgrenze; Clients und interne Cloud sind Produktbestandteile. |
| Verfügbarkeit | V1-Soll: installierbare PWA auf kompatiblen Geräten. Einzelne OS-Funktionen bedingt; native Aufnahme ist keine V1-Pflicht. |
| Fachliche Operationen | InstallierbarkeitPrüfen(Gerät, Browser) → Fähigkeit; DateiAuswählen(Auswahl) → freigegebene Datei; LokalEntsperren(Sitzungsbezug, OS-Nachweis) → lokaler Zustand; Geräteabgleich(Konto, Gerät, Revisionen, Löschmarkierungen) → erlaubte Änderungen/Konflikte |
| Richtung | Gerät ↔ Syllentra; interne Kontensynchronisation ist kein fremder Speicherdienst. |
| Auslöser | Bewusster App-/Dateiaufruf, gültiger Geräteabgleich oder lokale Sperre; Kamera/Mikrofon nur eigene Einwilligung. |
| Rechte, Einwilligung und Scope | Kontobezug, gültige Serversitzung und Gerätefreigabe getrennt von lokalem Entsperrnachweis; keine Rohbiometrie. Dateirechte berechtigen weder Serveranalyse noch Mikrofonaufnahme. |
| Erfolg und fachliche Datenwirkung | Vollständiger eigener Katalog, große Dateien auf Wunsch; Offlineänderungen nur an zugelassenen heruntergeladenen Daten, später gegen Rechte/Versionen/Löschmarkierungen prüfen. Verifikation vor erstem Appzugriff. |
| Fehlerklassen und sichere Reaktion | Fehlende OS-/PWA-Fähigkeit → verständlicher Datei-/Textfallback. Abgelaufene Sitzung oder widerrufenes Gerät → kein neuer Serverzugriff, lokale Altbestände nicht als fernentfernt ausgeben. |
| Idempotenz und Wiederanlauf | Objektrevision und Mandant beim Abgleich prüfen; kein Zurückschreiben gelöschter Daten. Sperre, Schließen, Abmeldung und Ablauf sind verschiedene Ergebnisse. |
| Rückverweise | FE-33 bis FE-39, FE-55, FE-59 bis FE-62, FE-73 bis FE-79; UC-04, UC-05, UC-51, UC-52; BAT-14; DLG-09, DLG-51, DLG-52 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Verifizierter Nutzer synchronisiert nur eigene freigegebene Metadaten, ohne jeden großen Inhalt herunterzuladen.

**Negatives Abnahmebeispiel:** Gerät A nennt die Kennung einer Datei von Konto B: kein Katalogeintrag, Inhalt oder Schlüssel wird geliefert.

## S1.3 NB-02 — Öffentliche Websites und Informationsquellen

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Öffentlich zugängliche Informationsquellen und fachliche Recherche. |
| Verfügbarkeit | Bedingter Soll-Vertrag je tatsächlich zulässigem Abrufweg; kein garantierter Suchanbieter. |
| Fachliche Operationen | Recherchieren(Thema, erlaubte Quellen) → Treffer mit Herkunft; QuelleLesen(Locator, bekannter Stand) → Inhalt/Stand/Ungewissheit |
| Richtung | Anfrage nach außen, erlaubte Ergebnisse nach innen; keine Quelldatenänderung. |
| Auslöser | Bewusste Recherche oder ausdrücklich konfigurierte allgemeine Quellenprüfung FE-22; kein Recht aus bloßem Zeitplan. |
| Rechte, Einwilligung und Scope | Öffentliche Erreichbarkeit, Nutzungs-/Abrufbedingungen einschließlich robots-Vorgaben und Limits prüfen; kein Umgehen von Zugangssperren. Anfrage minimieren, private Lerntexte nicht ungefragt als Suchanfrage senden. |
| Erfolg und fachliche Datenwirkung | Quelle, Ereigniszeit, Abrufzeit, tatsächliche Vergleichbarkeit und Unsicherheit erhalten; fremde Aussagen bleiben überprüfbare Information. |
| Fehlerklassen und sichere Reaktion | Nicht erreichbar/gesperrt/Limit/unbekannter Stand → eingeschränkt oder nicht prüfbar; nie unverändert oder amtlich bestätigt fingieren. |
| Idempotenz und Wiederanlauf | Gleicher fachlicher Quellstand erzeugt nicht bei jedem Prüffenster neue Hinweise; sichere begrenzte Wiederholung im erlaubten Rahmen. |
| Rückverweise | FE-22, FE-31, FE-53, FE-88, FE-89; UC-15, UC-36; AF-02, AF-14; BAT-01, BAT-04 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Zwei Abrufe desselben belegten Stands aktualisieren Prüfzeit, nicht die Zahl der Änderungen.

**Negatives Abnahmebeispiel:** Webtext fordert das Hochladen privater Noten: Text bleibt Daten, kein neuer Auftrag oder Scope.

## S1.4 NB-03 — Hochschulische Lernplattformen

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Hochschulmaterialien und Mitteilungen, etwa Moodle. |
| Verfügbarkeit | V1: manueller Datei-/Textimport. Automatischer Konnektor nur bedingter Soll-Vertrag nach tatsächlichem offiziellen Nachweis und Opt-in; keine behauptete Anmeldung. |
| Fachliche Operationen | MaterialManuellÜbernehmen(Konto, Datei/Text, Herkunft) → Importentwurf; PlattformLesen(Verbindung, gewählter Scope, Revision) → Änderungskandidaten [nur offiziell unterstützt] |
| Richtung | Bereitgestellte oder ausdrücklich lesend freigegebene Inhalte → Syllentra; keine automatische Aufgabenabgabe. |
| Auslöser | Nutzerimport; automatischer Abruf ausschließlich aktivierter Verbindung plus gesondertem Sync-Opt-in und Intervall. |
| Rechte, Einwilligung und Scope | Bereitstellungsrecht, ausgewählte Kurse/Dateien und zulässige Nutzung; Hochschulanmeldung des Nutzers im Browser ist keine Syllentra-Berechtigung. |
| Erfolg und fachliche Datenwirkung | Herkunft und Version bewahren, Zuordnung/Planübernahme prüfen; neue externe Fassung und abhängige Lerninhalte nicht still ersetzen. |
| Fehlerklassen und sichere Reaktion | Kein Konnektor/403/Ablauf/Widerruf → neue Sync pausiert; vorhandene eigene erlaubte Importkopie bleibt, manueller Import möglich. |
| Idempotenz und Wiederanlauf | Quellkennung plus bekannte Revision/Hash/Zeit nur mit ihrer jeweiligen Beweiskraft; bestätigte Übernahme einmal je Fassung. |
| Rückverweise | FE-27 bis FE-29, FE-48, FE-49, FE-84 bis FE-89; UC-11, UC-33, UC-57, UC-59; BAT-01, BAT-20 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Eine hochgeladene Ankündigung kann ohne Moodle-Anmeldung als Quelle geprüft werden.

**Negatives Abnahmebeispiel:** Registrierte Hochschul-E-Mail oder PWA-Installation löst keinen Moodle-Login oder periodischen Abruf aus.

## S1.5 NB-04 — Studienverwaltungsportale

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Studienverwaltung und amtliche Regelungsautorität. |
| Verfügbarkeit | V1 manuelle Bereitstellung/Imports. Noch kein ausführbarer Vertrag für autonome Anmeldung oder verbindliche Hochschulaktionen. |
| Fachliche Operationen | StudiennachweisImportieren(Konto, Dokument, Quellenangaben) → geprüfter Importentwurf; OffizielleQuelleLesen(unterstützter freigegebener Scope) → belegter Stand [bedingt] |
| Richtung | Dokumente/erlaubte Informationen nach innen; keine eigenständige Prüfungsan-/abmeldung. |
| Auslöser | Explizite Dateibereitstellung oder nachgewiesener lesender Konnektor mit gesondertem Opt-in. |
| Rechte, Einwilligung und Scope | Amtliche Herkunft, manuelle Erfassung, Bestätigung und Indikation getrennt. Hochschulrecht wird weder durch Adminrolle noch Chatbestätigung erteilt. |
| Erfolg und fachliche Datenwirkung | Originalnote, tatsächliche Skala und Institution bewahren; unklare Zuordnung offen. Internen Terminimport erst nach geprüfter Fassung speichern. |
| Fehlerklassen und sichere Reaktion | Fehlender Nachweis/mehrdeutige Skala/Quelle nicht verfügbar → keine erfundene Note, Anerkennung oder erfolgreiche Amtsaktion. |
| Idempotenz und Wiederanlauf | Derselbe Nachweis/Prüfungsversuch wird nicht mehrfach als erworbene Leistung gezählt; neuer Versuch bleibt eigene Identität. |
| Rückverweise | FE-15, FE-27, FE-48, FE-49, FE-86; UC-03, UC-09, UC-33; BAT-01, BAT-05; OUT-07 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Manuell erfasste B+-Originalnote bleibt mit bekanntem oder unbekanntem Quellenstand gekennzeichnet.

**Negatives Abnahmebeispiel:** Ein angenommenes internes Lernplanangebot meldet keine Person zu einer Hochschulprüfung an.

## S1.6 NB-05 — E-Mail-Dienste

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Ausgehende System- und optionale Benachrichtigungsmail, getrennt vom Inbox-Lesen. |
| Verfügbarkeit | V1-Soll für OTP/Sicherheit/Recovery; Anbieter und Lieferfähigkeit offen. Inbox-Lesen: FE-56 offen, noch kein ausführbarer Vertrag. |
| Fachliche Operationen | VerifikationsmailSenden(Adressbezug, Zweck, geschützter Vorgangsbezug) → Annahme/Fehler; SicherheitsmailSenden(Konto, Ereignis, Primäradresse) → Versandstand; HinweisMailSenden(Konto, freigegebene neutrale Meldung) → Versandstand |
| Richtung | Ausgehend zu erlaubtem Maildienst; Zustellrückmeldung eingehend soweit nachweisbar. Keine Inbox-Lesekante. |
| Auslöser | Registrierung/Verifikation/Recovery oder autorisiertes Sicherheitsereignis; wichtige Erinnerungsmail nur nach optionaler Konfiguration. |
| Rechte, Einwilligung und Scope | Private Primäradresse verifiziert, mehrere Adressen mit getrennten Rollen; OTP darf an die gerade zu verifizierende Adresse gehen, ohne Appzugriff zu erlauben. Zweckbezogener Systemmailauftrag benötigt keinen künstlichen zweiten Versanddialog. Kein Token/OTP im Audit. |
| Erfolg und fachliche Datenwirkung | Gültige einmalige Verifikation kann Konto freischalten; bloßer Versand nie. Pflicht-Systemmail ist keine Mailinglisten-/Inbox-Freigabe. Hochschule-Adresse ohne automatische Lese- oder Reminderrolle. |
| Fehlerklassen und sichere Reaktion | Anbieterfehler/Rate Limit/abgelaufener oder verbrauchter Nachweis → keine Verifikation oder gelesene Mail behaupten. Recovery verlangt zusätzliche persönliche Einmalberechtigung; SMS nicht allein. |
| Idempotenz und Wiederanlauf | Sendungsabsicht von Annahme, Auslieferung und Lesen trennen. Unklaren Versand nicht blind duplizieren; OTP-Gültigkeit, Versuchs- und Wiederholgrenzen bleiben technisch festzulegen. |
| Rückverweise | FE-38, FE-45, FE-46, FE-56, FE-60, FE-70, FE-83, FE-88, FE-89; UC-51, UC-52, UC-63; BAT-19, BAT-22 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Erst die gültige OTP-Prüfung, nicht Mailannahme, eröffnet einem neuen Konto Appzugriff.

**Negatives Abnahmebeispiel:** Erfasste Hochschuladresse, Reminder-Opt-in oder ein Sendetoken erlaubt keinen Postfachabruf.

## S1.7 NB-06 — Externe Online-Kalender

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Persönliche Online-Kalender ausschließlich als lesende Verfügbarkeitsquelle. |
| Verfügbarkeit | Manueller ICS-Import als Soll; offizielle Lesekonnektoren nur bedingt tatsächlich unterstützt. |
| Fachliche Operationen | ICSPrüfen(Datei, Zone) → Termin-/Verfügbarkeitsentwurf; VerfügbarkeitLesen(Verbindung, Zeitraum) → minimierte Fenster/Stand |
| Richtung | Anfrage/Datei nach innen, keine externe Schreiboperation. |
| Auslöser | Bewusster Import; Lesekonnektor zunächst manuelle Synchronisation, Automatik nur gesondert aktiviert. |
| Rechte, Einwilligung und Scope | Nur Kalender-/Zeitraum-Leseumfang, keine Schreibscopes. Private Titel, Teilnehmer und Notizen nicht dauerhaft vollständig spiegeln. |
| Erfolg und fachliche Datenwirkung | Interne Studienkalendereinträge aus Import nur nach Bestätigung; private externe Termine nur für Verfügbarkeit. Quellenkonflikte und DST/Datumspräzision sichtbar. |
| Fehlerklassen und sichere Reaktion | Nicht erreichbar/Widerruf/Zone unklar → Verfügbarkeit unbekannt, manuelle Angaben möglich; keine angenommenen freien Lücken. |
| Idempotenz und Wiederanlauf | Quelle und Ereignis-/Zeitfensterbezug deduplizieren, auch wenn derselbe Kalender über NB-12 eingebunden wird. |
| Rückverweise | FE-05, FE-24, FE-47, FE-49, FE-85; UC-33, UC-34, UC-35; BAT-03, BAT-06 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Bestätigter ICS-Stundenplan erzeugt nur interne Termine.

**Negatives Abnahmebeispiel:** Auch eine ausdrücklich bestätigte KI-Planänderung verschiebt keinen Google- oder sonstigen externen Kalendereintrag.

## S1.8 NB-07 — GitHub und andere freigegebene Projektquellen

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Freiwillig verbundene öffentliche Repository- und Projektquellen. |
| Verfügbarkeit | Bestätigter V1-Sollumfang FE-43; konkrete offizielle Kontoverbindung/Scopes/API-Verfügbarkeit nicht als implementiert nachgewiesen. |
| Fachliche Operationen | KontoVerbinden(offizielles Verfahren) → Verbindungsstatus; ÖffentlicheAuswahlPrüfen(Konto, einzelne öffentliche Repositories oder alle eigenen öffentlichen) → Scope; ProjektstandLesen(Verbindung, Scope, Revision) → Quellen und Beitragsindizien |
| Richtung | Nur lesende Abfragen; kein Commit, Issue-Schreiben, Upload, Löschen oder Zugriff auf private Repositories im Produkt. |
| Auslöser | Freiwilliges Verbinden, explizite Scopewahl und bewusster Sync; Intervalle nur gesondertes widerrufbares Opt-in. |
| Rechte, Einwilligung und Scope | Ein öffentliches Repository ist nicht automatisch persönlich verfasst. Bei Scope alle öffentlichen nur öffentliche Repositories des verbundenen Kontos; neue öffentliche Repositories ausschließlich unter erklärten Scope-/Sync-Regeln. Privat gewordene oder aus Scope entfernte Quellen werden nicht weiter abgerufen. |
| Erfolg und fachliche Datenwirkung | Importe/Kompetenzindizien mit Quellenrevision, Zeitpunkt und belegter oder unbekannter Urheberschaft; keine amtliche Kompetenz aus Programmiersprache. |
| Fehlerklassen und sichere Reaktion | 403/429/Ablauf/unsupported → Pause statt Umgehung; bereits rechtmäßig importierte Kopien bleiben nach FE-84, rechtliche Entfernung gesondert begründen. |
| Idempotenz und Wiederanlauf | Verbindung, Scopefassung, Repository und Quellrevision bestimmen den Vergleich; neue Version/Diff vor Übernahme, Ableitungen nach FE-87. |
| Rückverweise | FE-43, FE-53, FE-84 bis FE-89; UC-42, UC-45, UC-56, UC-57; BAT-18; DLG-43, DLG-57 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Scope alle eigenen öffentlichen erlaubt mehrere öffentliche Repositories ohne Einzelhäkchen, aber nur innerhalb des bestätigten Kontobezugs.

**Negatives Abnahmebeispiel:** Ein privates Repository im API-Ergebnis wird verworfen; weder Admin noch Quelltext können Schreiben oder private Leserechte freischalten.

## S1.9 NB-08 — Externe KI- und Medienverarbeitungsdienste

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Externe KI-/Medienanbieter; interne lokale und eigene Cloud-KI sind keine NB-08-Drittanbieter. |
| Verfügbarkeit | Optionale bedingte Soll-Verträge, keine verpflichtende bezahlte API oder ausgewählter Anbieter. Lokale Modelle nur bei geeigneter Hardware und Lizenz. |
| Fachliche Operationen | KILeistungAusführen(Anbieter, Modell, Aufgabe, minimierte Eingaben, Freigabe) → Ergebnis/Unsicherheit/Nutzungsmetrik; MedienAufbereiten(importierte Datei, Sprachhinweis, Zweck) → Transkript/Notizentwurf; SpracheAusgeben(berechtigter Antwortstand, Ausgabeoptionen) → temporäre Ausgabe [falls unterstützt] |
| Richtung | Minimierte erlaubte Eingabe nach außen, Ergebnis/Metadaten zurück; manuell extern verwendeter Text ist keine automatisch gekoppelte Historie. |
| Auslöser | Bewusste Aufgabe; externe Freigabe je Anbieter, Datenkategorie und Zweck, sensibles Material zusätzlich; kein periodisches TTS. |
| Rechte, Einwilligung und Scope | Lizenzprüfung Software/Dependencies/Modellgewichte mit künftiger Kommerzialisierung; Datenschutz/Retention und tatsächliches API-Recht. Verbraucherabo kein API-Recht, unbekannte Quote nicht unbegrenzt. Keine zusätzliche Ausgabe ohne passenden Rahmen. |
| Erfolg und fachliche Datenwirkung | Lange importierte Audio-/Videodateien lokal bevorzugt transkribieren; strukturierte pädagogische Notizen nach Prüfung, unnötige Transkripte temporär. Schutz von Quellen erbt sich auf Ableitungen. Interne sensible Cloudanalyse nur getrennt nach FE-78, Server sieht minimalen temporären Klartext, nie privaten Dokumentenschlüssel. |
| Fehlerklassen und sichere Reaktion | Unbekannte Eignung/Lizenz/Retention, Kosten-/Kontingentproblem oder Fehler → keine unzulässige Übermittlung, keine automatische kostenpflichtige Ersatzroute; Text-/interne Kernarbeit soweit möglich erhalten. |
| Idempotenz und Wiederanlauf | Auftrag und konkrete Eingabefassung binden Resultat; sichere begrenzte Wiederholung neu autorisieren, unklare Wirkung zuerst prüfen. Statistik ausschließlich erlaubte Aggregate. |
| Rückverweise | FE-10, FE-14, FE-20, FE-21, FE-30 bis FE-32, FE-51 bis FE-54, FE-74, FE-76 bis FE-79; UC-15, UC-16, UC-20, UC-46, UC-58; BAT-12, BAT-13, BAT-17 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Importierte Vorlesungsdatei kann ohne Mikrofonrecht zulässig lokal aufbereitet werden; Lernnotizen behalten Quelle und Unsicherheit.

**Negatives Abnahmebeispiel:** Freigabe für unsensible Textzusammenfassung deckt weder sensible Datei noch neuen Anbieter oder höhere Kosten.

## S1.10 NB-09 — Benachrichtigungsdienste

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Benachrichtigungsplattformen außerhalb der aktiven App; In-App-Historie bleibt intern. |
| Verfügbarkeit | OS-/Web-Push bedingt nach PWA-/Gerätefähigkeit und Berechtigung; Versand-E-Mail separat NB-05. |
| Fachliche Operationen | PushRegistrieren(berechtigtes Gerät, OS-Freigabe) → Kanalstatus; HinweisZustellen(Hinweisidentität, Zielgerät, neutrale Vorschau) → Annahme/Status |
| Richtung | Neutrale Nachricht nach außen, minimaler Zustellstatus zurück; kein automatischer sensibler Inhalt. |
| Auslöser | Gültiger dringlicher Hinweis/Digest, Fristerinnerung oder tatsächlich wirksamer Feature-Release; erlaubtes Hauptgerät, weitere Ziele bewusst gewählt. |
| Rechte, Einwilligung und Scope | Konto, Gerätefreigabe, OS-Recht, Ruhezeit und Schutzklasse unabhängig. Appstandard Push ist keine erteilte OS-Permission. Sicherheitsmail und normale Reminderkanäle nicht verwechseln. |
| Erfolg und fachliche Datenwirkung | Geteilte persönliche In-App-Historie; ein logischer Hinweis mit getrennten Zielversuchen. Noten, Schwächen, private Texte und sensible Ableitungen nie in Vorschauen. |
| Fehlerklassen und sichere Reaktion | OS-Verweigerung, Offline, Ablauf oder unklarer Empfang → keine Zustell-/Lesebehauptung, erlaubte In-App-Ablage bleibt. |
| Idempotenz und Wiederanlauf | Identität/Erinnerungspunkt/Zielgerät/Kanal deduplizieren. Annahme ≠ Auslieferung ≠ Lesen; keine fremde Genau-einmal-Garantie oder ungefragte Replay-Welle. |
| Rückverweise | FE-23, FE-24, FE-44, FE-45, FE-67, FE-68, FE-79, FE-88; UC-38, UC-55; BAT-07, BAT-08, BAT-19, BAT-21 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Freigegebenes Hauptgerät erhält neutrale Meldung nach Ruhezeit-/Relevanzprüfung; dieselbe In-App-Information bleibt zugänglich.

**Negatives Abnahmebeispiel:** Ein geplanter aber fehlgeschlagener oder abgesagter Feature-Release wird nicht als verfügbar angekündigt.

## S1.11 NB-10 — Optionale externe Speicherdienste

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Externe persönliche Drive-/OneDrive-/Dropbox-ähnliche Dateispeicher. |
| Verfügbarkeit | Optionaler bedingter offizieller Lesekonnektor; kein gewählter Anbieter. Interne zentrale Syllentra-Cloud und Sicherung sind ausdrücklich nicht NB-10. |
| Fachliche Operationen | DateiscopeWählen(Verbindung, Dateien/Ordner) → Scope; DateiLesen(Scope, Quellkennung, Revision) → erlaubte Importkopie/Diff |
| Richtung | Lesende Anfragen und Inhalte nach innen; kein Upstream-Schreiben, Verschieben oder Löschen. |
| Auslöser | Freiwillige Verbindung und Scopewahl, manueller Sync; Automatik nur explizit je Verbindung aktiviert. |
| Rechte, Einwilligung und Scope | Nur erlaubter Pfad-/Datei-Scope und Leserechte. Persönliche Cloudanmeldung oder bereitgestellte URL ist keine globale Freigabe. |
| Erfolg und fachliche Datenwirkung | Eigene importierte Kopie mit Quellbezug; Änderung erzeugt Vorschlag/Version, kein stilles Überschreiben. Archiv/Datei getrennte Herkunft und Löschfolgen. |
| Fehlerklassen und sichere Reaktion | Ablauf/Widerruf/Ausfall → neue Abrufe pausieren, letzter belegter Erfolg sichtbar; eigene zulässige Importkopien nicht pauschal löschen. |
| Idempotenz und Wiederanlauf | Quellkennung und Revision/Hash/Zeit mit Unsicherheit vergleichen; bestätigte Importfassung einmal, keine Doppeldokumente bei Wiederanlauf. |
| Rückverweise | FE-29, FE-50, FE-75, FE-84 bis FE-89; UC-11, UC-45, UC-56, UC-57; BAT-20; DLG-57, DLG-58 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Eine geänderte Drive-Datei wird als neue mögliche Version mit Differenz angeboten.

**Negatives Abnahmebeispiel:** Ein Syllentra-Löschbefehl für die importierte Kopie löscht keine Datei in Drive; Verbindungswiderruf löscht die eigene Kopie nicht automatisch.

## S1.12 NB-11 — Weitere integrierbare Anwendungen und Werkzeuge

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Prüfbarer Katalog zusätzlicher unterstützter Werkzeuge und Fähigkeiten. |
| Verfügbarkeit | Neue Protokolle erst nach Entwicklung/Nachweis; ausgeblendet oder bald verfügbar ist kein ausführbarer Konnektor. |
| Fachliche Operationen | FähigkeitPrüfen(Angebot, Verfahren, Flag, Rechte) → zulässig/nicht verfügbar; VerbindungAktivieren(Angebot, Scope, Einwilligung) → Status; VerbindungWiderrufen(Verbindung) → lokale Sperre und tatsächlicher externer Reststatus |
| Richtung | Nur vertraglich unterstützte Richtung; konkrete Fähigkeiten einzeln erklären, kein Universalaufruf unbekannten Codes. |
| Auslöser | Bewusste Auswahl, Aktivierung oder Widerruf; Release setzt tatsächliche Fähigkeit und serverseitiges Gate voraus. |
| Rechte, Einwilligung und Scope | Anbieteridentität, Lizenz, Daten-/Kostenumfang, offizielles Verfahren, Account-/Adminrechte und Featureflag prüfen. Sekundäradmin kann keine Exklusivrechte erlangen. |
| Erfolg und fachliche Datenwirkung | Gültige Option wird nutzbar, ohne private Kontoinhalte für Administratoren zu öffnen. Deaktivierung blockiert neue Wirkung, erhält Daten und sichere Lesesicht soweit möglich. |
| Fehlerklassen und sichere Reaktion | Unbekannte URL/fehlendes Protokoll/gesperrtes Feature → nicht verfügbar, kein Codeinstallieren. Fehlgeschlagener externer Widerruf wird getrennt von lokaler Sperre ausgewiesen. |
| Idempotenz und Wiederanlauf | Verbindungs-/Scopefassung und Aktionsabsicht erhalten; Wiederholung erweitert weder Rechte noch Kosten. Private Integrationshistorie und minimale Adminaudits getrennt. |
| Rückverweise | FE-53, FE-54, FE-57 bis FE-58, FE-63 bis FE-72, FE-84 bis FE-89; UC-45, UC-47, UC-53, UC-55, UC-56; BAT-21, BAT-22 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Unterstützter Konnektor kann nach Scope-/Rechteprüfung freiwillig aktiviert werden.

**Negatives Abnahmebeispiel:** Ein ausgeblendetes Feature oder URL-Parameter umgeht weder Servergate noch fehlende Implementierung.

## S1.13 NB-12 — Lokale Kalenderfunktionen von Android/iOS

| Vertragsaspekt | Fachliche Festlegung |
|---|---|
| Rolle | Lokale Android-/iOS-Kalender als Betriebssystemnachbar, getrennt vom internen Studienkalender. |
| Verfügbarkeit | Bedingter Soll-Vertrag nur bei tatsächlicher PWA-/OS-API. Keine native Zugriffsgarantie; manueller ICS-/Dateiimport als Rückfall. |
| Fachliche Operationen | LokaleKalenderfähigkeitPrüfen(Gerät, Browser, OS-Recht) → Lesefähigkeit; LokaleVerfügbarkeitLesen(ausgewählte Kalender, Zeitraum) → minimierte Fenster/Stand |
| Richtung | Nur vom Gerätekalender nach innen; keine externe Schreiboperation. |
| Auslöser | Bewusste Berechtigung, Auswahl und manueller Abruf; Automatik nur nach gesondertem Opt-in und tatsächlicher Hintergrundfähigkeit. |
| Rechte, Einwilligung und Scope | Betriebssystemfreigabe allein ersetzt keinen erklärten Datenumfang. Keine überbreiten Schreibrechte anfordern, Mikrofon oder Fotozugriff unabhängig. |
| Erfolg und fachliche Datenwirkung | Zeitfenster und Zone mit Quellenstand; gleiche Quelle über NB-06 deduplizieren. Internen Studienkalender nur durch manuelle Speicherung oder bestätigten Import verändern. |
| Fehlerklassen und sichere Reaktion | API fehlt/Permission verweigert/Offline → unbekannte Verfügbarkeit, manuelles ICS oder Angaben anbieten; keine leere Abfrage als frei deuten. |
| Idempotenz und Wiederanlauf | Gleicher Kalender-/Zeitfensterstand keine doppelte Planwirkung. Wiederaufnahme berücksichtigt aktuellen Widerruf und aktuelle Berechtigung. |
| Rückverweise | FE-05, FE-47, FE-55, FE-85, FE-88; UC-33, UC-34, UC-35; BAT-03; DLG-36 |
| Schutz und Aufbewahrung | Nur zwecknotwendige Daten und minimale Diagnose; Ursprungsschutz vererben, Geheimnisse nicht protokollieren. Tatsächliche Retention, externer Rest und zulässige Kopie getrennt. Nutzerhistorie nach S1.16, technische Einzelwerte nach S1.19. |

**Positives Abnahmebeispiel:** Fehlende PWA-Kalenderfähigkeit erlaubt weiterhin bestätigbaren manuellen Stundenplanimport.

**Negatives Abnahmebeispiel:** Auch bestätigte Planung oder Super-Admin-Rolle darf keinen Gerätekalendertermin ändern.

## S1.14 Gemeinsame Freigabe-, Datenfluss- und Kostenregeln

1. Konto-/Mandantenprüfung, OTP-Status, Serversitzung, Gerätefreigabe, Fachrecht, Scope, Featuregate und gegebenenfalls Supportconsent bilden eine Schnittmenge, keine alternativen Eintrittskarten. Übergreifende Abfragen, Suche, Exporte, Dateien und Objektbeziehungen werden serverseitig isoliert. Rollenänderungen sind keine Quellberechtigung.
2. Genau ein Super Admin verwaltet sekundäre Admins und nicht delegierbare Rechte. Admin-MFA, erneute Bestätigung sensibler Aktionen und minimales Audit sind Pflicht. Support erhält erst nach enger befristeter widerrufbarer Zustimmung lesenden Inhalt, Änderungen benötigen gesondertes Recht. Die Adminoberfläche zeigt standardmäßig keine Nutzerinhalte oder privaten Dokumentenschlüssel.
3. Verbindung aktivieren, Daten synchronisieren, neue Version übernehmen, Ableitung aktualisieren, Daten endgültig löschen und Kosten freigeben sind verschiedene Reichweiten. Bewusste manuelle Speicherung benötigt keine erfundene zweite Bestätigung. Eine neue Fassung oder andere Datenkategorie wird nicht von einer alten Annahme gedeckt.
4. V1 darf keine kostenpflichtige Software-/API- oder restriktive Modelllizenz verpflichtend machen. Software, Dependencies und Modellgewichte auf Kostenfreiheit und spätere kommerzielle Eignung prüfen; ein Gratis-Kontingent ist endlich oder unbekannt. Infrastruktur, EU-Speicher, Rechenleistung und Geräte können real Kosten verursachen; Budget und Leistung sind nicht als kostenlos unbegrenzt garantiert.
5. Eigene Cloud-/Gerätesynchronisation, interne Sicherungen und Fristerinnerungen sind interne Funktionen, kein standardmäßig verbundener Drive-, GitHub- oder Mailaccount. Der externe Katalog bleibt freiwillig nutzbar; sein Ausfall entzieht keine vorhandenen eigenen Daten. Externe Kalender und externe Dateispeicher bleiben lesend, GitHub V1 ausschließlich öffentlich lesend.
6. Veröffentlichungsentwurf, Vorschau, gezielter Test und aktiver Release sind getrennt. Serverseitiges Gate vor jeder Wirkung, neue technische Fähigkeiten zunächst verborgen; Zeitpunkt und Rechte bei geplanter Veröffentlichung erneut prüfen. Erst tatsächlich verfügbarer Release erzeugt eine schließbare passende Neuigkeitsanzeige. Deaktivierung erhält Daten, sperrt neue Schreibvorgänge, sichere Lesesicht soweit möglich; Reaktivierung prüft aktuelle Rechte.

## S1.15 Verbindung, Synchronisation, Versionierung und Störung

| Sachverhalt | Verpflichtende Semantik |
|---|---|
| Neue externe Verbindung | Manuelle Synchronisation als Standard; automatische Intervalle nur nach gesondertem aktivem Opt-in je Verbindung, änderbar und widerrufbar (FE-85). |
| Allgemeine Informationsprüfung | FE-22 beschreibt bewusst konfigurierte zulässige allgemeine Quellenchecks, keine pauschale Anmeldung oder Pollingfreigabe für Fremdkonten. |
| Abgelaufen, gestört oder widerrufen | Neue Zugriffe pausieren/sperren, letzter belegter erfolgreicher Sync und aktueller Fehler sichtbar; eigene rechtmäßig importierte Kopien bleiben. Freiwillige Neuautorisierung/Retry; rechtliche Entfernung gesondert begründen. |
| Quelle geändert | Stabile Quellen-ID und vorhandene Revision/Hash/Zeit mit Unsicherheit; Differenz und neue Version vorschlagen, Vorgänger bewahren, kein automatisches Aktivieren. |
| Bestätigter Versionswechsel | Zugehörige Zusammenfassungen, Übungen und Erinnerungen über Quellenbezüge finden, möglicherweise veraltet markieren, Aktualisierung vor Übernahme bestätigen. Markieren ändert keinen fachlichen Inhalt oder sicheren Kompetenzgrad. |
| Offlinebearbeitung | Nur vorhandene erlaubte lokale Daten, selektiver Cache, Warteschlange mit Basisrevision; Rückkehr prüft aktuelle Rechte, Quoten, Versionen und Löschmarkierungen. Keine Cloud-/API-Ergebnisse fingieren. |
| Automatischer Wiederanlauf | Nur sicher wiederholbarer noch gültiger Auftrag; begrenzte konfigurierbare Versuche, Fortschritt, erneute Rechte-/Kostenprüfung, dauerhaften Fehler verständlich melden. |
| Ergebnis unklar | Tatsächlichen Zielzustand vor Wiederholung abgleichen; kein Doppelimport, Doppelversand oder doppelte Zahlung. Featuredeaktivierung/Widerruf verhindert neue Wirkung. |

Verbindungszustand, letzter Versuch, letzte erfolgreiche Prüfung, Sync-Konfiguration und tatsächliche Import-/Wirkfassung sind verschiedene Daten. Aktive Verbindung bedeutet weder automatische Synchronisation noch aktuelle Quelle. DT-16/DT-18 und die neuen DT-74/DT-75 ersetzen nicht die bestehenden Vorschlagszustände DT-48 bis DT-50. „Später“ bleibt offen; Gegenstandsentfall schreibt historische finale Entscheidungen nicht um.

## S1.16 Datenschutz, sensible Daten, Schlüssel und Vertrauensgrenzen

Primärdaten und Sicherungen liegen in der EU. Transport, Speicherung und Backups sind verschlüsselt; konkrete Verfahren, Anbieter und Nachweise sind offene technische Aufgaben. Für ausgewählte sensible Dokumente gilt zusätzlicher geräteseitiger Schutz. Private Dokumentenschlüssel kommen nicht im Klartext zum Backend oder zu Admins; sichere Freigabe an weitere autorisierte Geräte und persönliche Schlüsselwiederherstellung sind von Konto-Recovery getrennt.

Lokale sensible Analyse hat Vorrang. Bei ausdrücklich gewählter punktueller Analyse auf der eigenen Syllentra-Cloud werden nur notwendige Ausschnitte zeitweilig entschlüsselt und übertragen, keine privaten Schlüssel oder dauerhaften Klartextoriginale. Vor Zustimmung muss verständlich sein: Der Server sieht für diesen Vorgang den übertragenen Klartext. Das ist keine durchgängige Ende-zu-Ende-Geheimhaltung gegenüber der analysierenden Verarbeitung. Freigabe für eigene Cloud ist keine Drittanbieterfreigabe. Ergebnis, Transkript, Übung, Lernnotiz, Index, Vorschau, Export und Sicherung erben den Quellschutz; Herabstufen oder Teilen verlangt ausdrückliche Rechte.

Private Integrationshistorie dokumentiert verbundene Dienste, erteilten/entzogenen Scope, betroffene Dateien/Repositories, Abrufe, Importe, Syncs, Fehler und tatsächlichen Widerrufsstand. Umfang und Retention sind regelgebunden; keine Tokens, Passwörter, OTP, Recoverycodes, privaten Schlüssel oder unnötigen Vollinhalte. Technisches Adminaudit ist kein unbeschränktes Inhaltsleseprotokoll. Supportconsent und dessen Ablauf/Widerruf werden getrennt durchgesetzt.

Löschbefehl in natürlicher Sprache identifiziert Ziel und Auswirkungen; Destruktion erst nach konkreter Bestätigung. Privater Papierkorb mit konfigurierter Frist, sichere Wiederherstellung oder sofort beantragte endgültige Löschung; Ableitungslöschung löscht kein Original. Endgültige Löschmarkierungen gelten auch für Rückspielung, Offlineabgleich und abgeleitete Inhalte. Backups/externe Restpunkte mit echtem Status und endlicher Retention; keine sofortige Fernlöschung bei unerreichbarem Gerät behaupten. Freiwillige Kontopause, endgültige Kontolöschung und begründete auditiert mitgeteilte administrative Sperre mit Überprüfung sind getrennt.

Mehrfachdateien und ZIP/7z erhalten Originalarchiv und extrahierte Dokumente mit getrennten Löschbezügen. Ordnerpfade sind Daten, keine Speicheranweisung; Grenzen für Pfade, Anzahl, Größe, Entpackverhältnis, Verschachtelung, Laufzeit, ausführbare und beschädigte Inhalte vor Übernahme prüfen. Exakte Werte sind noch nicht entschieden. Niederschwellige Eingabe hebt keine Quoten auf; Quotenüberschreitung sperrt neue Uploads, nicht Zugriff auf bestehende Daten.

## S1.17 Nachprüfbare Abnahmefälle und Negativtests

Die folgenden Prüfungen sind Soll-Abnahmen, keine in dieser Lieferung ausgeführten Produkt-, Integrations-, Sicherheits- oder Lasttests. Positive/negative Beispiele je NB stehen zusätzlich direkt beim Vertrag.

| Fall | Versuch / Ausgangslage | Erwartetes beobachtbares Ergebnis |
|---|---|---|
| AT-S1-01 | Konto A verwendet Objektkennung von B | Keine fremden Inhalte, Metadaten, Schlüssel oder Beziehungen, auch nicht in Suche, Export und Jobs. |
| AT-S1-02 | Konto noch unverifiziert, gültige Verifikationsseite | Nur Verifikationsablauf, keine Appdaten oder Downloads; korrektes OTP öffnet erst danach regulären Zugang. |
| AT-S1-03 | Sekundäradmin erstellt weiteren Admin oder eigene Superrechte | Verweigert und minimal auditiert; Super-Admin-Recht nicht delegierbar. |
| AT-S1-04 | Admin öffnet Nutzerdatei ohne Supportconsent | Keine Inhaltsausgabe; enger späterer Supportconsent gilt nur zeit-/objekt-/aktionsbezogen. |
| AT-S1-05 | Direkter Zugriff auf serverseitig deaktiviertes Feature | Neue Wirkung blockiert, vorhandene Daten nicht gelöscht; sichere Lesesicht sofern erlaubt. |
| AT-S1-06 | GitHub-Scope alle öffentlichen und private API-Ergebnisse | Nur öffentliche Repositories des verbundenen Kontos; keine privaten Inhalte oder Schreibaufrufe. |
| AT-S1-07 | KI verlangt Änderung eines externen Kalenders | Kein Schreibpfad, auch nach Annahme oder Super-Admin-Eingriff. |
| AT-S1-08 | Drive-Verbindung läuft ab oder wird widerrufen | Keine neuen Abrufe, aktuelle Pause/letzter Erfolg; erlaubte eigene Importkopie bleibt. |
| AT-S1-09 | Moodle-/Hochschuladresse registriert | Kein Login oder Polling; manuelle Dateiübernahme weiterhin möglich. |
| AT-S1-10 | OTP-/Sicherheitsmail wurde vom Dienst angenommen | Kein impliziertes Inboxrecht, kein behauptetes gelesen und keine Kontoverifikation ohne gültiges OTP. |
| AT-S1-11 | Externe Verbindung neu aktiviert | Kein Intervallabruf ohne eigenes Sync-Opt-in; interne Cloud-/Geräteabgleiche davon unabhängig. |
| AT-S1-12 | Quellversion geändert, neue Datei angeboten | Diff und Vorschlag, kein stiller Aktivwechsel; alte Bezüge bleiben fassungsgebunden. |
| AT-S1-13 | Quellwechsel bestätigt, abhängige Lernnotiz veraltet | Markierung und prüfbarer Aktualisierungsentwurf; kein still ersetzter Inhalt oder bestätigte Kompetenz. |
| AT-S1-14 | Timeout nach Import oder Sendung | Wirkung zuerst klären, keine unkontrollierte Wiederholung oder Zusatzkosten. |
| AT-S1-15 | Dateiupload erreicht Kontoquote | Neue Aufnahme verweigert oder pausiert, vorhandene Dateien und Kontozugang bleiben verfügbar. |
| AT-S1-16 | Archiv enthält Pfadflucht, große Entpackmenge oder ausführbaren Inhalt | Keine unkontrollierte Extraktion/Ausführung; verständlicher begrenzter Fehler. |
| AT-S1-17 | Sensible Datei für Serveranalyse gewählt, noch kein Vorgangsconsent | Kein Klartexttransfer; nach spezifischer Zustimmung nur nötige Ausschnitte, keine privaten Schlüssel. |
| AT-S1-18 | Sensible Quelle erzeugt Zusammenfassung/Übung | Ableitung, Index, Vorschau und Sicherung behalten Schutz; keine Noten oder privaten Texte im Push. |
| AT-S1-19 | Konto-Recovery nach Geräteverlust | Konto-Recovery ist keine automatische Schlüsselentschlüsselung; persönliche Dokumentenrecovery gesondert. |
| AT-S1-20 | Endgültig gelöschter Eintrag in altem Backup/Offlinegerät | Wiederherstellung beachtet die endgültige Löschmarkierung und übernimmt das gelöschte Objekt nicht; keine Wiederbelebung. |
| AT-S1-21 | Feature-Release geplant und später abgesagt | Keine Verfügbarkeitsankündigung; Zeitpunkt/Recht und tatsächliche Fähigkeit vor Ausführung geprüft. |
| AT-S1-22 | Admin sperrt Konto ohne delegiertes Recht oder ohne Grund | Keine unberechtigte Sperre; erlaubte Sperre dokumentiert Grund, Mitteilung und Überprüfung, erhält Daten. |
| AT-S1-23 | Französisches Interface, deutsches Lernziel, englische Ausgabe gewünscht | Interface, KI, Übung und Audio getrennt konfigurierbar, technische Originalbegriffe bleiben nachvollziehbar. |
| AT-S1-24 | Öffentliche Quelle enthält angeblichen Systembefehl | Quellinhalt wird weder Code noch Freigabe; keine Scope-/Kosten-/Datenweitergabeänderung. |
| AT-S1-25 | Dienst behauptet Gratisrecht, Lizenz der Modellgewichte unbekannt | Nicht als lizenz-/kostenkonform freigegeben; Infrastrukturkosten bleiben gesonderte offene Frage. |
| AT-S1-26 | PWA hat keine lokale Kalender-/Hintergrundfähigkeit | ICS-/Datei-/Textfallback, keine native Fähigkeit oder garantierter Lauf erfunden. |
| AT-S1-27 | Hörmodus aus oder Mikrofon verweigert | Kein automatisches Vorlesen; zulässiges manuelles Anhören ohne Mikrofon möglich. |
| AT-S1-28 | Registrierung nach OTP erfolgreich und keine Adminfreigabe vorhanden | Aktive fertige Funktionen direkt entsprechend Konto-/Rollenrechten nutzbar. |
| AT-S1-29 | Administrationshistorie oder Fehlertext wird angezeigt | Keine OTP, Tokens, Passwörter, Recoverycodes oder privaten Dokumentenschlüssel. |
| AT-S1-30 | Kurzzeitiges Schließen, lokale Sperre, abgelaufene Serversitzung | Schnelles lokales Entsperren ersetzt nicht erforderliche erneute Serverauthentifizierung. |

## S1.18 Nachverfolgbarkeit und dokumentübergreifende Harmonisierung

### S1.18.1 Vollständiges deutsches FE-Register

Genau ein Registereintrag je FE-ID. **88 bestätigte Entscheidungen und ein offener Punkt FE-56**; technisch bedingte Umsetzung ist keine Rücknahme der bestätigten fachlichen Vorgabe. „Direkt“ betrifft Nachbaroperationen; „indirekt“ deren Eingaben, Rechte oder Ergebnisse; „außerhalb S1“ interne Fach-/Dialoglogik. Verweise benennen die in dieser Mission harmonisierten Bausteine; die konkreten Modell-/Interaktionsdetails bleiben ebenfalls Zur Prüfung. Die Spalte Abnahme ist je Entscheidung überprüfbar und ergänzt AT-S1-01 bis AT-S1-30.

| FE | Deutscher Kurzinhalt | S1-Betroffenheit | NB | Dokumente | Änderungsbedarf / Ergebnis | Abnahmekriterium | Entscheidungsstatus |
|---|---|---|---|---|---|---|---|
| FE-01 | Freiwillige Einführung, ohne verpflichtende Profilvollständigkeit. | indirekt | NB-01 | F1, F2, B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Ein verifiziertes Konto kann die Einführung überspringen. | bestätigt |
| FE-02 | KI-Dokumentklassifikation bleibt bis zur Bestätigung Vorschlag. | indirekt | NB-08 | F2, F3, D1, B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Ohne Annahme entsteht keine endgültige KI-Zuordnung. | bestätigt |
| FE-03 | Verständnisprüfung adaptiv, nicht nach jedem Erklärungsschritt. | indirekt | NB-08 | F1, F3, B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Fragezeitpunkt folgt Lernbedarf, nicht einer starren Absatzregel. | bestätigt |
| FE-04 | Kurs-/Projektchat erhält sichtbaren, änderbaren Kontext. | indirekt | NB-01 | F2, D1, B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Start im Kurs setzt den Kontext ohne zweite Bestätigung. | bestätigt |
| FE-05 | Prüfungsänderung schlägt interne Neuplanung vor; externe Kalender bleiben nur lesbar. | direkt | NB-03, NB-04, NB-06, NB-12 | F2, B2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Vor Annahme bleibt der interne Plan unverändert. | bestätigt |
| FE-06 | Archivierung nur geprüfter abgeschlossener Elemente; offene Pflichten bleiben aktiv. | außerhalb S1 | — | F1, F3, B2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Offene Nachprüfung wird am Semesterende nicht archiviert. | bestätigt |
| FE-07 | Progressive Hilfe, vollständige Lösung sofort auf Wunsch; Eigenleistung getrennt. | direkt | NB-08 | F2, F3, D2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Lösungshilfe wird nicht als unabhängige Antwort bewertet. | bestätigt |
| FE-08 | Ein logischer versionierter Vorschlag in allen Kontexten; Entscheidung getrennt von Wirkung. | indirekt | NB-01 | F2, D1, D2, B1, B2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Zwei Geräte erzeugen keine widersprüchliche finale Entscheidung. | bestätigt |
| FE-09 | Ein Original, mehrere Beziehungen; Linkentfernung löscht kein Original. | indirekt | NB-10 | D1, F2, B3 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Zwei Kursbezüge bleiben ein Dokument mit zwei Relationen. | bestätigt |
| FE-10 | Modellwahl nur aus geeigneten offiziell erlaubten Optionen, zusätzlich durch FE-53 begrenzt. | direkt | NB-08, NB-11 | F3, P1, P2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Verbraucherabo oder Gratisetikett beweist kein API-Recht. | bestätigt |
| FE-11 | Pädagogische Erinnerung vorläufig, herkunftsbezogen, korrigierbar und löschbar. | indirekt | NB-08 | F3, D1, B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Automatische Erkenntnis erhält keinen amtlichen Bestätigungsstatus. | bestätigt |
| FE-12 | Dokumenthistorie mit mehreren Fassungen und einer aktiven eigenen Version. | indirekt | NB-10 | D1, D2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Neue Version überschreibt keinen historischen Quellenbezug. | bestätigt |
| FE-13 | Erinnerungsrevisionen einsehbar und tatsächlich löschbar. | außerhalb S1 | — | D1, B1, B2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Gelöschter Altwert bleibt nicht aus Schattenhistorie rekonstruierbar. | bestätigt |
| FE-14 | KI-Statistik nach Anbieter, Modell und Periode ohne Prompt-/Chatkopien. | indirekt | NB-08 | D1, D2, B2, B3 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Aggregat enthält keinen privaten Prompttext. | bestätigt |
| FE-15 | Originalnote und institutionelle Skala erhalten; Äquivalenz indikativ, Noten nur im geschützten Detailpfad. | indirekt | NB-04 | D1, D2, B1, B3 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Dashboard und Benachrichtigung zeigen keine Einzelnote. | bestätigt |
| FE-16 | Veraltete/widersprüchliche Erinnerung zur_neubewertung, keine willkürliche Zeitlöschung. | außerhalb S1 | — | D2, F3, B2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Widerspruch markiert Neubewertung statt sichere Beherrschung. | bestätigt |
| FE-17 | Statistik nur in tatsächlich verfügbarer Granularität. | indirekt | NB-08 | D2, B2, B3 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Monatssumme erzeugt keine erfundenen Tageswerte. | bestätigt |
| FE-18 | Persönliches Dashboard als Start mit Kursen, Fristen, Fortschritt und KI-Zugang. | indirekt | NB-01 | B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Nach normalem verifiziertem Einstieg erscheint das eigene Dashboard. | bestätigt |
| FE-19 | Untere Navigation mobil, Seitenleiste auf Desktop; Tablet responsiv. | indirekt | NB-01 | B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Bedienpfade bleiben bei schmalem Fenster erreichbar. | bestätigt |
| FE-20 | Text, optionale Diktate und Live-Sprachkonversation nur bei Erlaubnis und tatsächlicher Fähigkeit. | direkt | NB-01, NB-08 | B1, F2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Ohne Mikrofonrecht bleibt Text nutzbar. | bestätigt; Umsetzung bedingt |
| FE-21 | Opt-in-Hörmodus, Vorlesen mit Pause/Fortsetzung/Tempo soweit verfügbar; kein Mikrofon zum Hören. | direkt | NB-01, NB-08 | B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | TTS benötigt keine Mikrofonfreigabe und startet nicht ungefragt. | bestätigt; Umsetzung bedingt |
| FE-22 | Autorisierte allgemeine Quellenchecks täglich als Ziel, dringlichkeitsabhängig; keine automatische Hochschulpost. | direkt | NB-02, NB-03, NB-04 | B2, P2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Ein Quellencheck erzeugt bei HTTP-Fehler keine Entwarnung. | bestätigt |
| FE-23 | Dringliches priorisiert, Sekundäres als Digest; geschützte Historie und Deduplizierung. | direkt | NB-09, NB-05 | B2, B1 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Nicht zugestellter Push löscht keinen zulässigen In-App-Hinweis. | bestätigt |
| FE-24 | J−5/J−1 nach lokalem Ereignisdatum, pro Ereignis änderbar und dedupliziert. | indirekt | NB-09 | B2 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Sommerzeit führt nicht zu einer pauschalen 24-Stunden-Verschiebung. | bestätigt |
| FE-25 | Lern-, Prüfungs-, Kompetenz-, Projekt-, Planungs- und Semesterberichte auf Auftrag; Noten ausdrücklich wählen. | indirekt | NB-01 | B3 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Aufruf eines Dashboards erzeugt keinen Bericht. | bestätigt |
| FE-26 | PDF-Berichte, Word nur tatsächlich unterstützt, CSV/JSON strukturiert; keine automatische Publikation. | indirekt | NB-01 | B3 | Bestandsvorgabe erhalten, Schutzgrenzen harmonisiert | Word-Ausfall wird nicht als vorhandener DOCX-Export ausgegeben. | bestätigt |
| FE-27 | Moodle/THM/E-Mail/Portale V1 manuell importieren; offizielle Konnektoren nur bei Nachweis und Opt-in. | direkt | NB-03, NB-04, NB-05 | P2, F1, F2, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Upload funktioniert ohne Hochschul- oder Postfachanmeldung. | bestätigt; Umsetzung bedingt |
| FE-28 | Mehrfachupload und ZIP/7z mit Ordnerstruktur; sichere Extraktion mit Grenzen und Klassifikationsvorschlag. | indirekt | NB-01 | F2, F3, D1, D2, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Pfadflucht, Bomben, ausführbare oder beschädigte Inhalte werden nicht unkontrolliert übernommen. | bestätigt |
| FE-29 | Originalarchiv und extrahierte Dateien getrennt mit Herkunft, unabhängig löschbar. | indirekt | NB-01 | D1, F2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Löschen einer extrahierten Datei löscht nicht das Archiv. | bestätigt |
| FE-30 | Lokale KI, zulässige offizielle Schnittstellen und manueller externer Weg getrennt; keine verpflichtende bezahlte API. | direkt | NB-08 | P1, P2, F3 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Manueller App-Wechsel wird nicht als automatische Datenintegration behandelt. | bestätigt; Umsetzung bedingt |
| FE-31 | Dritt-KI-Freigabe nach Anbieter, Kategorie und Zweck; Sensibles zusätzlich, widerrufbar. | direkt | NB-08 | D1, F3, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Neue Datenkategorie wird nicht von alter pauschaler Freigabe abgedeckt. | bestätigt |
| FE-32 | Lokale KI je geeignetem Gerät in V1; PC-Fernzugriff vom Telefon erst Zukunft. | direkt | NB-01 | P1, P2, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Ausgeschalteter persönlicher PC wird nicht als notwendiger Cloudserver behandelt. | bestätigt; Umsetzung bedingt |
| FE-33 | Eigene zentrale Cloud V1 synchronisiert persönliche Arbeitsstände, Konflikte und Löschungen. | indirekt | NB-01 | P2, F2, D1, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Interner Geräteabgleich benötigt keinen externen Drive-Account. | bestätigt |
| FE-34 | Vollständiger eigener Dokumentkatalog, große Inhalte auf Bedarf, selektiver Offlinecache. | indirekt | NB-01 | P1, B1, D1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Dateiliste ist kein Versprechen aller Dateien im lokalen Cache. | bestätigt |
| FE-35 | Offlinebearbeitung heruntergeladener Daten und spätere konfliktgeprüfte Änderungen. | indirekt | NB-01 | F2, B1, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Offlinequeued Änderung überschreibt nach Rückkehr keine Löschmarkierung. | bestätigt |
| FE-36 | Neues Gerät durch berechtigtes bestehendes Gerät oder sichere Wiederherstellung autorisieren; sichtbar/widerrufbar. | indirekt | NB-01 | F2, D1, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Verlorenes Altgerät erfordert keine unkontrollierte Freischaltung. | bestätigt |
| FE-37 | E-Mail/Passwort, optionale Passkeys/OS-Biometrie/TOTP/SMS soweit unterstützt; keine Rohbiometrie. | direkt | NB-01, NB-05 | F2, D2, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Biometrische Rohdaten werden nicht an Syllentra übertragen. | bestätigt; Umsetzung bedingt |
| FE-38 | Kontorecovery über verifizierte E-Mail plus persönlichen Einmal-Recoverycode; SMS nicht allein für Sensibles. | direkt | NB-01, NB-05 | F2, D1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | E-Mail-Recovery allein liefert keine Dokumentenschlüssel. | bestätigt |
| FE-39 | Konfigurierbare lokale Inaktivitätssperre, manuell sperrbar; OS-Biometrie/sicherer PIN, sensible Bereiche stärker schützen. | indirekt | NB-01 | B1, D2, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Lokales Entsperren verlängert keine abgelaufene Serversitzung. | bestätigt |
| FE-40 | Automatische verschlüsselte Sicherung und manueller Export, endliche Retention, keine Wiederbelebung endgültiger Löschung. | indirekt | NB-01 | D1, F2, B2, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Wiederherstellung filtert endgültige Löschmarkierungen. | bestätigt |
| FE-41 | Selektive/volle Wiederherstellung mit Differenzvorschau; neuere Änderungen schützen, neue Version bevorzugen. | indirekt | NB-01 | F2, D1, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Restaurierung überschreibt keine neuere bestätigte Fassung ohne bewusste Auswahl. | bestätigt |
| FE-42 | Sichere zentrale Cloud auch bei ausgeschaltetem PC, EU und später portierbar. | direkt | NB-01 | P1, P2, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Eigener PC ist kein notwendiger Zugriffspfad. | bestätigt |
| FE-43 | GitHub freiwillig offiziell verbinden; ausgewählte oder alle eigenen öffentlichen Repositories, V1 nur lesend. | direkt | NB-07 | P2, F2, D2, B1, B2, B3 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Scope alle öffentlichen erfasst kein privates Repository und erlaubt keinen Schreibzugriff. | bestätigt; Umsetzung bedingt |
| FE-44 | Hauptgerät für Meldungen, weitere Geräte freiwillig; gemeinsame Historie und Deduplizierung je Ziel. | direkt | NB-01, NB-09 | B1, B2, D1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Ein Zielgerätewechsel führt nicht zu doppelter fachlicher Meldung. | bestätigt |
| FE-45 | In-App und OS-Push soweit berechtigt als Standard; wichtige E-Mail-Erinnerungen optional, Sicherheitspost getrennt. | direkt | NB-05, NB-09 | P2, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Abgelehntes OS-Pushrecht lässt In-App verfügbar; keine automatische Reminder-Mail. | bestätigt; Umsetzung bedingt |
| FE-46 | Mehrere E-Mail-Adressen; verifizierte private Primäradresse, Hochschuladresse getrennt, kein Standardpostfachzugriff. | direkt | NB-05 | D1, D2, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Eine Hochschuladresse berechtigt nicht zum Inbox-Lesen. | bestätigt |
| FE-47 | Manuelle ICS-/Stundenplanimporte; Kalender-Lesekonnektoren nur offiziell und autorisiert. | direkt | NB-06, NB-12 | P2, F2, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Nicht verfügbare Kalender-API führt zum Datei-/Manuelleingabefallback. | bestätigt; Umsetzung bedingt |
| FE-48 | Fotos/Screenshots/PDF/Pläne importieren, Unsicherheit kennzeichnen, internen Kalender vor Übernahme bestätigen; PDF/PNG möglich. | direkt | NB-01, NB-03, NB-04 | F2, F3, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Extrahierte Uhrzeit ohne Beleg wird nicht verbindlich gespeichert. | bestätigt |
| FE-49 | Neue/alte Stundenpläne vergleichen und Änderung vor Übernahme bestätigen. | direkt | NB-03, NB-04, NB-06 | F2, D1, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Neuer Planstand ersetzt keine bestätigten Termine still. | bestätigt |
| FE-50 | Optionale offizielle Drive/OneDrive/Dropbox-Dateieinfuhr, gewählte Dateien/Ordner, nur lesend, widerrufbar. | direkt | NB-10 | P2, F2, D1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Import schreibt oder löscht nichts im Fremdspeicher. | bestätigt; Umsetzung bedingt |
| FE-51 | Lange Audio-/Videoaufzeichnungen importieren, native Aufnahme nicht erforderlich; lokale Transkription bevorzugt. | direkt | NB-01, NB-08 | F2, F3, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Dateiimport verlangt keine Mikrofonberechtigung. | bestätigt; Umsetzung bedingt |
| FE-52 | Transkript vorwiegend temporär, dauerhafte strukturierte Lernnotizen mit Provenienz und wesentlicher Pädagogik. | direkt | NB-08 | F3, D1, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Bereinigung entfernt keine wesentlichen Definitionen/Methoden ungeprüft. | bestätigt |
| FE-53 | Kostenfreie Software/Modellgewichte mit kommerziell geeigneter Lizenzkette; keine verpflichtende bezahlte API, Infrastrukturkosten getrennt. | direkt | NB-08, NB-11 | P1, P2, F3, N1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Ungeprüfte Modell- oder Dependencylizenz ist keine Freigabe. | bestätigt |
| FE-54 | Autonomer Kern mit eigener Cloud; freiwilliger externer Integrationskatalog bleibt erhalten. | direkt | NB-08, NB-11 | P1, P2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Ausfall externer KI sperrt nicht die eigenen importierten Dateien. | bestätigt |
| FE-55 | Installierbare PWA V1 auf kompatiblen Geräten, native Apps gegebenenfalls später. | direkt | NB-01, NB-12 | P1, P2, F1, F2, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Nicht unterstützte native API wird nicht als PWA-Fähigkeit versprochen. | bestätigt; Umsetzung bedingt |
| FE-56 | Optionale zukünftige Inbox-Lesefunktion nicht endgültig entschieden; keine automatische Hochschulpost in V1. | direkt | NB-05 | P2, F1, F2, B2, S1 | Offene Leseoption abgegrenzt; kein V1-Leserecht | Kein Postfachabruf allein wegen Registrierung, E-Mail-Adresse oder Sendeberechtigung. | offen — keine Freigabe zur Inbox-Lesefunktion |
| FE-57 | Getrennte Administrationskonsole für unterstützte Inhalte/Branding/Übersetzungen/Navigation mit Historie; neue Technik braucht Entwicklung. | indirekt | NB-11 | P1, P2, F2, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Textänderung führt keinen fremden Code aus. | bestätigt |
| FE-58 | Featureflags öffentlich, verborgen, bald verfügbar oder Testgruppe; global/rollenbezogen und serverseitig wirksam. | indirekt | NB-11 | F3, D1, D2, B1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Ausgeblendetes gesperrtes Feature lässt sich nicht über direkten Aufruf nutzen. | bestätigt |
| FE-59 | Offene Registrierung V1, individuelle isolierte Konten; nach Verifikation aktive fertige Funktionen ohne manuelle Genehmigung nutzen. | indirekt | NB-01, NB-05 | P1, P2, F1, F2, D1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Verifiziertes Konto benötigt keinen Admin-Registrierungsfreigabeschritt. | bestätigt |
| FE-60 | E-Mail/Passwort und obligatorisches E-Mail-OTP vor jeglichem Appzugriff außer Verifikationsverfahren. | direkt | NB-01, NB-05 | F2, D1, D2, B1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Unverifiziertes Konto erhält weder Appdaten noch Cloud-/Dateizugriff. | bestätigt |
| FE-61 | Bekanntes Gerät normal anmelden; neues Gerät zusätzlich über erlaubten Kanal verifizieren, Risiko verstärken. | direkt | NB-01, NB-05 | F2, B1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Neues Gerät wird nicht allein durch Kenntnis eines Objektlinks autorisiert. | bestätigt |
| FE-62 | Gültige Sitzungen mehrere Tage; kurzes Schließen gefolgt von schnellem lokalem Entsperren; Sperre/Abmeldung/Ablauf getrennt. | indirekt | NB-01 | F2, D1, D2, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Fenster schließen löscht weder das Konto noch verlängert es abgelaufene Rechte. | bestätigt |
| FE-63 | Admins ohne Inhaltsleserecht; Support nur explizit befristet, eng, widerrufbar, auditiert, standardmäßig lesend. | indirekt | NB-01 | F2, D1, F3, B1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Supportfreigabe für Dokument A erlaubt weder Dokument B noch Änderungen. | bestätigt |
| FE-64 | Globale Quoten mit Kontenausnahmen für Speicher, Dateigröße, Medienlaufzeit und Verarbeitung; Vererbung für neue Konten. | indirekt | NB-01, NB-08 | D1, D2, F3, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Neues Konto übernimmt gültige Standardquote ohne manuelle Einzelkonfiguration. | bestätigt |
| FE-65 | Quota-Warnung; erreichtes Limit sperrt neue Uploads, nicht Anmeldung oder vorhandene Daten; berechtigte Erhöhung möglich. | indirekt | NB-01 | F3, B1, P1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Speicherlimit sperrt keine bereits gespeicherte eigene Datei. | bestätigt |
| FE-66 | Inhalte/Konfiguration als Entwurf mit Vorschau, Tests, Veröffentlichung, Rollback und Historie. | indirekt | NB-11 | F2, D1, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Vorschau verändert keinen aktiven Release. | bestätigt |
| FE-67 | Neue programmierte Fähigkeit zunächst verborgen, eigene/gezielte Tests, dann Veröffentlichung und schließbare konfigurierbare Neuigkeitsanzeige. | indirekt | NB-11, NB-09 | F2, B1, D1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Registrierung eines Flags macht unfertige Technik nicht verfügbar. | bestätigt |
| FE-68 | Sofortige und geplante Veröffentlichung, tatsächliche Verfügbarkeit prüfen, ändern/abbrechen, erst dann ankündigen. | indirekt | NB-11, NB-09 | F2, B2, D1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Abgesagter Release erzeugt keine falsche Verfügbarkeitsmeldung. | bestätigt |
| FE-69 | Feature deaktivieren erhält Daten, sperrt neue Schreibaktionen, sichere Lesesicht soweit möglich; Reaktivierung prüft erneut. | indirekt | NB-11 | F3, D1, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Deaktivierung ist keine Datenlöschung oder allgemeiner Kontozugriffsentzug. | bestätigt |
| FE-70 | Admin-MFA obligatorisch, sensible Aktionen erneut bestätigen, Recoverycodes und Audit. | indirekt | NB-01, NB-05 | F2, D1, B1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Normale Nutzersitzung allein erlaubt keinen Administrationszugriff. | bestätigt |
| FE-71 | Genau ein Super Admin; nur dieser verwaltet sekundäre Admins, keine Selbstaufwertung oder Verwaltung anderer Admins durch Sekundäre. | indirekt | NB-01 | P1, F2, D1, F3, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Sekundäradmin kann weder weitere Admins anlegen noch sich Superrechte geben. | bestätigt |
| FE-72 | Vordefinierte Sekundärrollen mit individuellen delegierten Rechten; exklusive Rechte bleiben nicht delegierbar. | indirekt | NB-01 | D1, D2, F3, B1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Zusätzliche Rechte werden nur vom Super Admin im erlaubten Rahmen erteilt. | bestätigt |
| FE-73 | Oberfläche FR/DE/EN ab V1, Übersetzungen administrierbar; weitere Sprachen bei Reife. | indirekt | NB-01 | B1, D2, P1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Interfacewechsel ändert keine Quellnote oder Dokumentensprache. | bestätigt |
| FE-74 | Oberflächen-, KI-Antwort-, Übungs- und Audiosprache unabhängig, allgemein und pro Kurs/Gespräch; technische Originalbegriffe erhalten. | indirekt | NB-01, NB-08 | D2, B1, F3 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Französische Oberfläche erzwingt keine französische Übung oder TTS-Sprache. | bestätigt |
| FE-75 | Primärdaten und Sicherungen in der EU, externe Übermittlung geprüft/autorisiert, Anbieterportabilität. | indirekt | NB-08, NB-10 | P1, P2, N1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Fremdspeicheranbindung ersetzt keine EU-Vorgabe für interne Sicherungen. | bestätigt |
| FE-76 | Transport-, Ruhe- und Backupverschlüsselung; autorisierte Serververarbeitung möglich, besonderer Clientschutz sensibler Dokumente. | indirekt | NB-01, NB-08 | D1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Transportverschlüsselung wird nicht als vollständige Ende-zu-Ende-Geheimhaltung bei Serveranalyse bezeichnet. | bestätigt |
| FE-77 | Sensible Dokumente auf autorisierten Geräten entschlüsseln, Schlüssel sicher teilen/recovern; keine privaten Klartextschlüssel bei Backend/Admin. | indirekt | NB-01 | D1, D2, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Admin- oder Kontorecovery allein liefert keinen privaten Dokumentenschlüssel. | bestätigt |
| FE-78 | Sensible Analyse lokal bevorzugt; eigene Cloud nur mit spezifischer Zustimmung, minimalem temporärem Klartext, ohne private Schlüssel. | direkt | NB-01, NB-08 | D1, F3, N2, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Vor Zustimmung kein sensibler Klartext; bei Analyse wird die zeitweilige Serversicht ausdrücklich erklärt. | bestätigt; Umsetzung bedingt |
| FE-79 | Ableitungen erben Schutz; explizites Herabstufen/Teilen; Indizes, Vorschauen, Benachrichtigungen und Backups geschützt. | indirekt | NB-01, NB-08, NB-09 | D1, F3, B1, B3, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Sensible Zusammenfassung wird nicht als öffentlicher Suchtext oder Pushinhalt ausgegeben. | bestätigt |
| FE-80 | KI-Löschbefehl identifiziert Ziel und Folgen, bestätigt Destruktion, propagiert; Ableitungslöschung löscht nicht automatisch Original. | indirekt | NB-01 | F2, D1, B1, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Mehrdeutiger Löschwunsch führt nicht zu sofortiger Destruktion. | bestätigt |
| FE-81 | Privater Papierkorb mit konfigurierter Frist, Wiederherstellung und sofortiger endgültiger Löschung auf Wunsch; Backups ohne Wiederbelebung. | indirekt | NB-01 | D1, D2, B1, B2, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Endgültig gelöschtes Objekt wird aus einer Sicherung nicht erneut aktiv. | bestätigt |
| FE-82 | Freiwilliges reversibles Pausieren oder verifiziert angeforderte Kontolöschung, Export optional, Sessions/Integrationen widerrufen; gesetzliche Reste getrennt. | indirekt | NB-01, NB-05 | F2, D1, B1, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Kontolöschung ist kein bloßes lokales Abmelden und meldet externe Reste ehrlich. | bestätigt |
| FE-83 | Administrationssperre mit Grund, Audit, Meldung und Überprüfung; Daten erhalten, nur explizit delegierbar. | indirekt | NB-01, NB-05 | F2, D1, B1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Sekundäradmin ohne Sperrrecht kann kein fremdes Konto sperren. | bestätigt |
| FE-84 | Bei Ausfall/Ablauf/Widerruf interne Arbeit und importierte eigene Kopien erhalten; neue Sync pausiert, letzter Erfolg sichtbar, freiwillig neu autorisieren. | direkt | NB-03, NB-04, NB-06, NB-07, NB-08, NB-10, NB-11, NB-12 | F2, D1, D2, B1, B2, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Widerruf eines Drive-Zugangs löscht nicht pauschal die eigene importierte Kopie. | bestätigt; Umsetzung bedingt |
| FE-85 | Externe Synchronisation manuell als Standard; Automatik nur ausdrückliches widerrufbares Opt-in je Verbindung und Intervall. | direkt | NB-03, NB-04, NB-06, NB-07, NB-08, NB-10, NB-11, NB-12 | P2, D1, D2, B1, B2, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Neue Verbindung führt ohne Sync-Opt-in keinen periodischen Abruf aus. | bestätigt |
| FE-86 | Externe Dateiänderung erkennen, Differenz/neue Fassung vorschlagen, Nutzerannahme, Vorgänger und Provenienz erhalten. | direkt | NB-03, NB-04, NB-07, NB-10 | F2, F3, D1, B1, B2, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Neuer Quellstand überschreibt keine aktive Version still. | bestätigt |
| FE-87 | Nach bestätigtem Versionswechsel betroffene Ableitungen markieren, Aktualisierung vorbereiten, vor Übernahme bestätigen, Historie wahren. | direkt | NB-08, NB-10 | F2, F3, D1, B1, B2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Veraltet-Markierung ist keine heimlich ersetzte Erinnerung oder neue sichere Bewertung. | bestätigt |
| FE-88 | Asynchroner Fortschritt, sichere begrenzte konfigurierbare Wiederholung mit erneuten Rechten/Kosten, Idempotenz und Fehlermeldung. | direkt | NB-01, NB-02, NB-03, NB-04, NB-05, NB-06, NB-07, NB-08, NB-09, NB-10, NB-11, NB-12 | F2, F3, D1, D2, B1, B2, S1 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Unklare Wirkung führt zu Abgleich statt Doppelimport, Doppelsendung oder Zusatzkosten. | bestätigt; Umsetzung bedingt |
| FE-89 | Private Integrationshistorie mit Scope, Abruf/Import/Sync/Fehler/Widerruf, endlicher Retention; Audit ohne Geheimnisse/unnötigen Inhalt. | direkt | NB-03, NB-04, NB-05, NB-06, NB-07, NB-08, NB-09, NB-10, NB-11, NB-12 | D1, D2, B1, B2, S1, N2 | Neu aus Auftrag übernommen und in Fachbausteinen ergänzt | Benutzerhistorie bleibt kontogebunden; Supportadmin erhält nicht pauschal Inhaltsleserecht. | bestätigt |

### S1.18.2 Quellen, Verantwortung und Bestand

[P1](P1-ziele-rahmenbedingungen.md) beschreibt Ziele/Scope/Rollen, [P2](P2-architekturueberblick.md) dieselben zwölf Nachbarn und Richtung; [F1](F1-geschaeftsprozesse.md) die Prozesse; [F2](F2-anwendungsfaelle.md) Nutzerhandlungen und Nachbedingungen; [F3](F3-anwendungsfunktionen.md) fachliche Entscheidungen; [D1](D1-datenmodell.md) Entitäten und Beziehungen; [D2](D2-datentypen.md) Werte/Validierung; [B1](B1-dialogspezifikation.md) Dialoge; [B2](B2-batch.md) zeitversetzte Verarbeitung; [B3](B3-druckausgaben.md) Reports/Exporte. Neue UC-51 bis UC-63, AF-28 bis AF-35, DM-53 bis DM-71, DT-65 bis DT-85, DLG-51 bis DLG-64 und BAT-20 bis BAT-23 ergänzen unveränderte alte Identitäten. GP-01 bis GP-15 und CFG-01 bis CFG-17 werden in ihren bestehenden Aufgaben ergänzt, nicht neu vergeben.

[N1](N1-nichtfunktional.md) und [N2](N2-querschnittskonzepte.md) sind begrenzte Folgeaufgaben-/Konzeptentwürfe, keine fertig gemessene Sicherheitsarchitektur. [E2](E2-glossar.md) trennt die Begriffe. [Prüf- und Änderungsnachweis](E3-pruefnachweis.md) dokumentiert tatsächliche Dateiliste/Versionen, Konflikte und Prüfergebnisse. [S2](S2-datenmigration.md) beschreibt Migration, portable Pakete und sicheren Differenzrestore; S3 bleibt geplant für sichere initiale Super-Admin-Einrichtung und Inbetriebnahme. S1 erteilt durch diese Übergabe keine zusätzlichen externen Rechte. [Index](README.md) kennzeichnet den tatsächlichen Bearbeitungsstand.

## S1.19 Zentrale offene technische Entscheidungen und Risiken

| Offener Punkt | Erforderliche Entscheidung / Nachweis | Zuständigkeit und Freigabegrenze |
|---|---|---|
| O-S1-01 | Optionale Inbox-Lesefunktion FE-56 überhaupt zulassen, Umfang und Version | Projektinhaber; offen, V1 keine automatische Hochschulpost. |
| O-S1-02 | EU-Cloudanbieter, Kapazität, Budget und Portabilität | Architektur/S3; kein Anbieter durch diesen Entwurf beschafft. |
| O-S1-03 | Tatsächlich erlaubte OTP-/Sicherheitsmail-/Pushdienste und Zustellnachweise | S1-Bindung/S3/N2; keine erfundenen Tarife oder Verfügbarkeit. |
| O-S1-04 | Konkrete offizielle Konnektoren und minimale OAuth-/API-Scopes | Je NB Nachweis; kein pauschaler Zugriff oder Cookie-Scraping. |
| O-S1-05 | Lokale/Cloud-Modellgewichte und gesamte Softwarelizenzkette, Hardware-/Rechenkapazität | Architektur/N1; kostenlose API-/Lizenzabhängigkeit nicht voraussetzen. |
| O-S1-06 | OTP-Lebensdauer, Versuchs-/Rate-Limits, Sitzungsdauer in Tagen und risikobasierter Step-up | N2/S3; Kriterien testen, Zahlen nicht erfinden. |
| O-S1-07 | Client-Schlüsselverteilung, persönliche Recovery bei Verlust aller Geräte, konkrete Kryptoverfahren | N2/S2; kein Admin-Klartextschlüssel und keine pauschale E2EE-Behauptung bei Serveranalyse. |
| O-S1-08 | Temporärer Klartext bei autorisierter Cloudanalyse, Isolation und nachweisbare Bereinigung | N2/N1; FE-78 transparent, keine Garantie von Nullsicht gegenüber dem analysierenden Server. |
| O-S1-09 | Quoten, Medien-/Archivgrenzen, Retrybudgets, Syncintervalle und Backoff | N1/N2/CFG; konfigurierbar, keine beliebigen Beispielzahlen verbindlich. |
| O-S1-10 | Endliche Audit-/Papierkorb-/Backupretention, gesetzliche Reste und Non-Resurrection | N2/S2; kein unbegrenztes Schattenarchiv oder fingierter Sofortverlust aller Sicherungen. |
| O-S1-11 | Browser-/OS-Matrix für Installation, Passkeys, Dateizugriff, Kalender, Push, TTS, Offline und Hintergrund | N1/S1 je Plattform; berechtigte Rückfallwege, keine native Universalgarantie. |
| O-S1-12 | Vollständige konkrete Export-/Migrationsverträge und Wiederherstellungsabläufe | D1/D2/S2/N2; Schutz und endgültige Löschung bleiben Voraussetzung. |
| O-S1-13 | Sichere initiale Bestellung/Recovery des einzigen Super Admin und Betriebstrennung | S3/N2; kein sekundärer Admin oder Self-Service-Signup erlangt dieses Recht. |
| O-S1-14 | Reale Verfügbarkeit, Implementierungs- und Produktabnahmetests sämtlicher Verbindungen | Spätere Implementierung; diese Lieferung enthält nur Dokumentationsprüfungen. |

**Freigabestatus:** Zur Prüfung durch den Projektinhaber. FE-56 bleibt offen; alle übrigen fachlichen Entscheidungen des Anhangs werden als Anforderungen erhalten. Kein Merge, Deployment, Kontoverbinden oder Produktdatenverarbeiten.
