# S2 — Datenmigration, Datenportabilität und sichere Wiederherstellung

**Projekt:** Syllentra AI\
**Baustein:** S2 — Datenmigration (fachliche Soll-Spezifikation)\
**Version:** 0.4\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber\
**Bezugsstand:** `Viny005/syllentra`, PR #1, Branch `docs/spec/p1-p2-mobile-workspaces`, verifizierter HEAD `723af7fa1692f8dbaf888b694fa63806d7d5fc5f` (vor Erstellung dieses Entwurfs).\
**Methodik:** Fachbaustein S2 gemäß Siedersleben. Gelesene methodische Referenz: [Herold-Bausteinübersicht](https://github.com/carstenlucke/herold/blob/main/docs/spec/SIEDERSLEBEN.md), insbesondere „Schnittstellen zu Alt- und Nachbarsystemen“, und [Herold-README](https://github.com/carstenlucke/herold/blob/main/docs/spec/README.md), Abschnitt S2, im Git-Stand `fce50b47ae646a70bf4d796026dcd1a99d3ae3c2`. Herold erklärt S2 wegen fehlender Altdaten für nicht anwendbar und enthält keine eigene S2-Datei. Daher wird keine konkrete Herold-S2-Vertragsvorlage behauptet und Herolds Nichtanwendbarkeit nicht auf Syllentra übertragen. S1 beschreibt externe Nachbarn, S2 die Übernahme/Umwandlung eigener Daten und Bestände, S3 den sicheren Betriebsstart.\
**Wichtig:** Dieser Baustein übernimmt und prüft den beigefügten vollständigen Entwurf, ist jedoch keine technische Implementierung und keine Abnahme produktiver Sicherheitsmaßnahmen. Seine tatsächliche Git-Sicherung wird in [E3](E3-pruefnachweis.md) und der Git-Historie nachgewiesen. Identifikatoren `MIG-xx` und `AT-S2-xx` sind ausschließlich neue S2-interne Vertrags- und Prüfpunkte, **keine** neu vergebenen FE-/UC-/DM-/DT-Kennungen.

---

## S2.1 Auftrag, Ziele und Systemgrenze

S2 spezifiziert, wie Syllentra-Daten **sicher, nachvollziehbar, portabel und ohne unzulässige Nebenwirkungen** zwischen eigenen App-Versionen, eigenen Geräten, zulässigen Nutzerexporten, eigenen Kontoständen und kontrollierten Importquellen überführt werden. Migration ist weder allgemeiner Zugriff auf Fremdkonten noch die freie Ausführung beliebiger Dateiinhalte. S2 schließt an [P1](P1-ziele-rahmenbedingungen.md), [P2](P2-architekturueberblick.md), [D1](D1-datenmodell.md), [D2](D2-datentypen.md), [F2](F2-anwendungsfaelle.md), [F3](F3-anwendungsfunktionen.md), [B1](B1-dialogspezifikation.md), [B2](B2-batch.md), [S1](S1-nachbarsysteme.md), [N1](N1-nichtfunktional.md), [N2](N2-querschnittskonzepte.md) und [E3](E3-pruefnachweis.md) an.

**Verbindliche Ziele:** Datenhoheit und Weiterverwendbarkeit; sichere Wiederaufnahme nach Gerätewechsel/App-Upgrade; kein stiller Datenverlust, keine Kontenvermischung, keine Rechteausweitung und keine Wiederbelebung endgültig gelöschter Inhalte. Nutzer können Umfang und Konfliktbehandlung kontrollieren. Nur tatsächlich erfolgreiche Schritte gelten als erfolgreich. Syllentra V1 bleibt eine zentrale, mehrbenutzerfähige EU-Cloud-PWA mit getrennten Konten und Adminrollen (FE-33/42/55/59/60/70–72/75). Die V1 erfordert keine kostenpflichtige externe API und keinen obligatorisch laufenden eigenen PC. Infrastruktur- und Kapazitätskosten sind dennoch realistisch offenzulegen.

**Geltungsfälle:**
- Einmaliger und wiederholter Export eigener Daten einschließlich selektiver Exporte.
- Wiedereinlesen eines unterstützten Syllentra-Exports in das **berechtigte** Konto mit Vorschau, Auswahl, Konfliktentscheidung und Wirkungsnachweis.
- Interner Geräteabgleich, zulässige Offline-Nachlieferung und gesicherter Wiederanlauf.
- Interner Versions-/Schemawechsel beim Deployment und spätere Hosting-/Speicherwechsel.
- Betriebsinterne Sicherungs-/Wiederherstellung mit Mandantentrennung, Schutz vor Datenwiederbelebung und Revisions-/Löschregeln.
- Manuelle akademische Fremdimporte nur als eigenständiger, explizit unterstützter Format-/Zuordnungsweg; keine Behauptung universeller Migration aus Drittprodukten.

**Außerhalb von S2:** Fremd-API-Verträge (S1), Benutzeroberflächen im Detail (B1), Batch-Orchestrierung (B2), Datenfelddefinitionen (D1/D2), Hosting-/Admin-Bootstrap (S3), Datenbankprodukt, konkrete Cloud-/E-Mail-/KI-Anbieter und kryptografische Implementierung (N2/Architektur).

## S2.2 Verbindliche S2-Entscheidungen (MIG-01 bis MIG-36)

| Kennung | Entscheidung für V1 | Nachprüfbare Grenze |
|---|---|---|
| MIG-01 | Vollständiger persönlicher Datenexport auf Nutzeranforderung | Nur autorisierte, dem Konto zugehörige exportierbare Daten, kein Fremdinhalt |
| MIG-02 | Selektiver Export nach Modul, Semester, Projekt, Datentyp und Zeitraum | Auswahl wird vor Start angezeigt, Abhängigkeiten erklärt |
| MIG-03 | Versioniertes, offen dokumentiertes, maschinenlesbares Exportpaket | Manifest mit Schema-/Exportversion, Herkunft, Bestands- und Konsistenzhinweisen |
| MIG-04 | Für Menschen nutzbare Teilformate (z. B. JSON, CSV, Markdown) plus freigegebene Originaldateien | Nicht jeder Fachtyp sinnvoll als CSV; keine verlustfreie Darstellung versprechen, wo nicht möglich |
| MIG-05 | Erneuter kontrollierter Import eines kompatiblen persönlichen Syllentra-Pakets | Identität und Besitz überprüfen; Paketbesitz ist kein Zugriffsrecht |
| MIG-06 | Pflicht-Vorschau/Dry-Run vor **wirksamer** Rückübernahme | Was neu, geändert, gleich, konfliktbehaftet, unlesbar und gesperrt ist, wird ausgewiesen |
| MIG-07 | Selektive Wiederherstellung einzelner Themenbereiche/Objekte | Referenzabhängigkeiten und Datenschutzgrenzen sichtbar |
| MIG-08 | Konfliktwahl `behalten`, `zulässige Fassung übernehmen`, `überspringen`, `getrennte Kopie` wo fachlich sinnvoll | Kein universelles „alles überschreiben“; unveränderbare Nachweise geschützt |
| MIG-09 | Erkennung belegter Doppelimporte und Quellrevisionen | Idempotenz über Konto, Quellidentität, Version, Operation; Hash nicht als alleiniger Eigentumsbeweis |
| MIG-10 | Importprüfung mit Isolation/Quarantäne unsicherer oder unbekannter Inhalte | Kein Ausführen eingebetteter Skripte, Makros, HTML-Anweisungen oder Agentenprompts |
| MIG-11 | Sichere Archivbehandlung einschließlich ZIP und 7z gemäß FE-28; zusätzliche Formate nur mit ausdrücklich unterstütztem Profil | Größen-, Dateizahl-, Entpack- und Rekursionlimits; Pfadtraversal/ZIP-Bomben abweisen |
| MIG-12 | Nachvollziehbarer Fortschritt, Teilresultate, sichere Wiederaufnahme und Abbruch | Abbruch erklärt, was bereits wirksam ist; sichere Wiederholung nach FE-88 |
| MIG-13 | Persönliche Migrationshistorie mit Status, Kategorien, Umfang, Gründen und Fehlern | Keine Klartext-Geheimnisse, unverhältnismäßige private Lerninhalte oder Fremdkontodaten im Log |
| MIG-14 | Export-/Importnutzungsquoten und verständliche Kapazitätswarnungen | Konfigurierbar und transparent; keine stillen Löschungen oder unbegrenzte Gratiszusage |
| MIG-15 | Standardmäßig automatische betriebsinterne Sicherungen mit erklärter Retention | Betreiber-Backups sind **nicht** gleichbedeutend mit sofortiger Selbst-Restore-Funktion |
| MIG-16 | Berechtigte selektive Wiederherstellung eigener Daten, soweit Schlüssel/Quellen verfügbar und zulässig | Kein Umgehen von Löschmarkierungen, Konto-/Gerätewiderruf oder aktuellen Rechten |
| MIG-17 | Nichtwiederbelebung endgültig gelöschter Daten bei Import, Restore und Offline-Sync | Aktuelle Lösch-/Entzugsinformationen haben Vorrang, mit sicheren endlichen Aufbewahrungsregeln |
| MIG-18 | Verlaufs-/Versionsbindung und nachvollziehbare Differenzen | Ein altes Zitat wird nicht still einer neuen Quellenfassung zugeordnet |
| MIG-19 | Importierte KI-Ableitungen behalten Herkunft, Vertrauensgrad und Sensitivitätsklasse | Keine unbelegte Hochstufung zu verifizierter oder amtlicher Information |
| MIG-20 | Trennung: Datenexport versus Übernahme von Anmeldung/Sicherheitszustand | Niemals Passwort-Hashes, OTP, Sitzungstokens, OAuth-Tokens, Secrets, Super-Admin-Rolle, MFA-Vertrauen wiederherstellen |
| MIG-21 | Geschützte Exportoption für sensible Inhalte mit expliziter Nutzerentscheidung | Verschlüsselungs-/Schlüsselverfahren später N2-konform festlegen; keine Klartextexporte ohne informierte Entscheidung |
| MIG-22 | E2EE-gebundene Inhalte nur mit wirklich verfügbaren berechtigten Schlüsseln lesbar | Verlorener Schlüssel bleibt nicht durch Admin/Server magisch rekonstruierbar (FE-76/77) |
| MIG-23 | Mandantensichere Wiederherstellung auch bei Betriebsunfällen | Keine globale Sicherung als ungeprüfter Self-Service-Einspielweg, negatives A→B testen |
| MIG-24 | Keine stillen Rechteänderungen durch importierte Rollen, Konfiguration, Berechtigungen oder Integrationen | Integrationen nach Import grundsätzlich inaktiv, aktuelle Rechte separat verifizieren |
| MIG-25 | Kalender- und Lernplanübernahme mit Urheberschaft und Schutz manueller Planung | Manuell gesetzte Sitzungen niemals ohne ausdrückliche Bestätigung verschieben; externe Kalender nur lesend |
| MIG-26 | Wiederherstellen des Lernprofils mit Vorsicht bei zeitlichen Fortschritten | Ältere Profile/Ergebnisse überschreiben keine neuere Evidenz; Undo der Planung löscht keinen Lernfortschritt |
| MIG-27 | Gerätewechsel durch Anmeldung, Freigabe und berechtigten Cloudabgleich | Kein pauschaler Import von Gerätetrust/Biometrie; lokal nur bewusst freigegebene Kopien |
| MIG-28 | Offline-Konflikte und mehrfache Geräte über aktuelle Rechte, Revisionen und Löschstatus auflösen | Kein Wiederhochladen eines gelöschten oder widerrufenen Altobjekts |
| MIG-29 | Sichere App-/Datenmodell-Upgrades mit Migrationsplan und Validierung | Vorab kompatible Änderungen, Wiederaufnahme, keine ungesicherte destruktive Schemaänderung |
| MIG-30 | Migration des Syllentra-Betriebs zwischen geeigneten Hosting-/Speicherangeboten | EU-Grenze, Sicherheitsnachweise, Portabilität, Kontenisolierung, Audit vor Cutover |
| MIG-31 | Manuelle akademische Datei- und Fremddatenimporte, soweit konkret unterstützt | Quelle, Mapping, Vorschau, Zustimmung; keine universelle Plattformanmeldung oder Gmail-Inbox V1 |
| MIG-32 | Export vor freiwilliger Kontolöschung optional anbieten | Kein Löschverzicht durch Export; Aufbewahrung/Backups und externe Restdaten ehrlich darlegen |
| MIG-33 | Freigegebene Kopien optional für Offlinezugriff, keine „vollständiger Account offline“-Garantie | Sensible Daten und lokale Sperre beachten; Verlustrisiken erklären |
| MIG-34 | Kein automatischer Versand von Exportpaketen an E-Mail, GitHub oder externe Speicher | Lokale Bereitstellung als Standard; auch ein ausdrücklicher Zielauftrag hebt die V1-Lesegrenzen von NB-07/NB-10 nicht auf, kein Fremd-Upload durch S2 |
| MIG-35 | Möglichkeit, den Exportumfang und unbekannte/fehlende Bestandteile als Bericht einzusehen | Eine Teilausgabe nicht „vollständig“ nennen; Exportversion und Fehlstellen ausweisen |
| MIG-36 | Funktionen bei fehlender Kapazität/Schlüsseln/Kompatibilität sicher degradieren | Manueller Teilimport/Export und verständliche Fehler statt ungeschützter Fallbacks |

**V1-Implementierungsprinzip:** Der gesamte fachliche Funktionsumfang ist als Soll-Anforderung vorgesehen; tatsächlich produktiv freigeschaltete Teilfunktionen müssen implementiert, überprüft, sicher und durch den global/rollenbezogen konfigurierbaren Featurestatus kenntlich sein (FE-58/66–69). Ein „bald verfügbar“-Eintrag ist keine funktionsfähige Migration. Einzelne aufwendige Betriebs- und Cross-Provider-Automatismen sind erst nach Machbarkeits-, Sicherheits- und Kapazitätsnachweis freizuschalten. Fachlich und sicherheitlich essentielle Teilfunktionen haben Vorrang vor einer möglichst langen Schein-Featureliste.

### S2.2.1 V1-Sollumfang und Freischaltbedingungen

| Kategorie | Fachlicher Sollstand | Grenze der tatsächlichen Produktfreigabe |
|---|---|---|
| Standardmäßig vorgesehene V1-Wege | Eigener vollständiger/selektiver Export, unterstützter eigener Reimport mit Vorschau und Bestätigung, automatische interne Sicherungen, zugelassener Geräteabgleich und unterstützte manuelle akademische Importe | Erst nach implementierter Format-/Rechte-/Konsistenzprüfung nutzbar; kein „bald verfügbar“ als erfolgreicher Vorgang. Automatische Sicherung ist keine automatische Einspielung. |
| Bewusst gewählte Optionen | Selektiver Offlinebestand, zusätzliche Schutzoption des Exportpakets, ausgewählte Restorebereiche und Konfliktstrategie | Nutzerwahl, aktuelle Schlüssel/Rechte und verfügbare Kapazität erforderlich. Sensibler Quellschutz gilt auch ohne gewählte Komfortoption; unsicherer Export ist kein Standardfallback. |
| Betriebswege und technische Freigabe | Schema-/Releasewechsel, vollständiger Disaster Restore, Betreiber-/Speicherwechsel, weitere Drittformatadapter | V1-Sollverträge mit verpflichtenden Integritäts-/Sicherheits- und Wiederanlaufnachweisen; keine heute behauptete Betriebsautomatik. RPO/RTO, Parameter und Plattformfähigkeiten bleiben offen. |

Der S2-Auftrag ermächtigt keine neue allgemeine Produktautomatik. Aktuelle Feature-/Rollenrechte gelten bis zur tatsächlichen Wirkung. Eine fehlende optionale Fähigkeit darf einen sicheren verfügbaren Teilweg anbieten, aber keine beschlossene V1-Anforderung still streichen.

## S2.3 Migrationswege, Berechtigungen und Startbedingungen

| Weg | Initiator / Einwilligung | Richtung und Rechte | Fachlicher Abschluss |
|---|---|---|---|
| EXP — Persönlicher Export | Verifizierter Kontoinhaber, ggf. erneute Anmeldung vor sensiblen Daten | Eigene zulässige Objekte → Nutzergerät | Paket verfügbar, Manifest/Inhalt auf Konsistenz geprüft; lokaler Download **nicht** mit externer Speicherung gleichsetzen |
| IMP — Persönlicher Syllentra-Reimport | Verifizierter Kontoinhaber, Auswahl und konkrete Bestätigung | Nutzerpaket → **sein** aktuelles Konto | Nur bestätigte, erlaubte Teilwirkungen; Konflikte und Auslassungen protokolliert |
| ACA — Akademischer Import | Bewusste Nutzerdatei/-texteingabe | Externe Unterlagen → Importentwurf → nach Prüfung eigene Objekte | Zuordnung und Abgleich bestätigt; keine stillen amtlichen Noten oder Termine |
| DEV — Gerätesynchronisation | Zugelassenes Gerät und gültige Serversitzung; Offlinewarteschlange | Eigene lokale berechtigte Revisionen ↔ eigene zentrale Cloud | Aktuelle Objekt-/Lösch-/Rechtegrenzen eingehalten |
| BAK — Interner Backup/Restore | Berechtigte Betriebsfunktion mit dokumentierter Genehmigung | EU-interne betriebliche Sicherung ↔ interner Dienst | Konsistenzprüfungen und Wiederbelebungsschutz vor Wiederfreigabe bestanden |
| UPG — Versions-/Schema-Migration | Autorisierter Deploymentprozess | Alter interner Datenstand → kompatibler neuer Stand | Geprüfte Integrität, kontrollierter Cutover, nachvollziehbare Rollback-/Vorwärtsstrategie |
| MOV — Betreiber-/Speicherwechsel | Autorisierter administrativer Prozess | EU-konformer alter → EU-konformer neuer Betrieb | Vollständigkeits-/Sicherheitsnachweis, Zugriffsumstellung, geregelte Altaufbewahrung |

**Keine Autorisierung durch bloße Dateipräsenz:** Wiederherstellungsdateien sind untrusted input; selbst ein gültiges Manifest ist kein Ersatz für Kontoverifikation, aktuelles Recht, gültigen Schlüssel oder erneute Zustimmung. Konto A kann weder Export noch Backup noch Import von B einsehen oder in A als fremden privaten Datensatz übernehmen. Für eigene vor einem früheren Kontoverlust erzeugte Exporte ist vor Zuordnung ein gesondert festgelegter **starker Eigentums- und Recoverynachweis** erforderlich; bis zu dessen Ausarbeitung keine automatisierte Übernahme in ein fremdes/neues Konto. Ein Nutzerimport darf lediglich berechtigte **Inhalte**, nie fremde Identitäts- oder Rechteobjekte übernehmen.

### S2.3.1 Vollständige fachliche Operationsverträge

Die Signaturen benennen fachliche Eingaben und Ergebnisse, keine API-Endpunkte oder technische Transaktionsprodukte. Kontobezug, Zweck, Umfang, Versionsgrundlage, aktuelle Rechte und Ausführungsnachweis sind für alle Wege verpflichtend. Eine erfolgreiche Transportprüfung allein beweist weder zulässige Herkunft noch Eigentum oder fachliche Vollständigkeit. Nicht bekannte Pflichtberechtigung gilt nicht als Freigabe.

#### EXP — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | PersoenlichenExportErstellen(Konto, Auswahl, Schutzoption, erwarteterStand) → Paket/Teilpaket mit Bericht oder Sperre |
| Auslöser, Rechte und Vorbedingungen | Bewusster Auftrag des verifizierten Eigentümers; zulässige eigene Objekte, verfügbare Schlüssel, aktuelle Sitzung und Quota. |
| Erfolg und Datenwirkung | Ein unveränderter fachlicher Bestand wird als versionierter Export mit Stichtagsbasis und nachvollziehbaren Lücken bereitgestellt; Quelle bleibt unverändert. |
| Fehler und sichere Reaktion | Nicht verfügbare Schlüssel/Originale, Quote oder Schutzoption: begründete Sperre oder ausdrücklich gewähltes sicher geschütztes Teilpaket, kein ungeschützter Ersatz. |
| Idempotenz / Wiederanlauf | Eigentümer, Auswahlrevision, Auftrag und Stichtagsbasis; zweiter Abruf liest dasselbe Ergebnis, bewusst neuer Export darf eigenen Zeitpunkt tragen. |
| Rückverweise und Abnahme | S2.5; MIG-01 bis MIG-04, MIG-21, MIG-32, MIG-34, MIG-35; AT-S2-01 bis AT-S2-04, AT-S2-35 |

#### IMP — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | ImportVorschauErstellen(Konto, Paket, Zielstand) → Delta; ImportEntwurfBestaetigen(Konto, Vorschaufassung, Auswahl) → Lauf; ImportlaufPruefen(Lauf) → tatsächliche Teilwirkungen |
| Auslöser, Rechte und Vorbedingungen | Expliziter Nutzerwunsch; Paketbesitz ist kein Eigentumsnachweis; aktuelles eigenes Ziel, kompatibles Profil und konkrete Bestätigung. |
| Erfolg und Datenwirkung | Nur geprüfte zulässige Inhalte wirken je bestätigter Einheit. Ausgangs- und Zielrevision sowie tatsächliche Teilresultate bleiben unterscheidbar. |
| Fehler und sichere Reaktion | Manipulation/Unbekanntheit, fehlender Schlüssel, Löschmarkierung oder konkurrierende Änderung: sperren, auslassen oder neu prüfen; keine privilegierte Zustandsübernahme. |
| Idempotenz / Wiederanlauf | Eigentümer, Paket-/Quellidentität, Inhaltsrevision, Zielrevision und bestätigte Teilwirkung; unklare Wirkung vor Wiederholung abgleichen. |
| Rückverweise und Abnahme | S2.6/S2.9; MIG-05 bis MIG-14, MIG-17 bis MIG-20, MIG-24 bis MIG-26; AT-S2-05 bis AT-S2-30 |

#### ACA — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | AkademischenImportPruefen(Konto, bereitgestellteDatei, dokumentiertesFormatprofil, Zielkontext) → Zuordnungsentwurf; AkademischenImportBestaetigen(Entwurfsfassung, Auswahl) → eigene Inhalte/Termine |
| Auslöser, Rechte und Vorbedingungen | Freiwillig bereitgestellte rechtmäßige Datei, tatsächlich unterstütztes Format und erlaubter Kontext. |
| Erfolg und Datenwirkung | Herkunft, Unsicherheit, Originalnote und Quellenrevision erhalten; Zuordnung/Terminimport erst nach konkreter Übernahmeprüfung. |
| Fehler und sichere Reaktion | Unlesbare OCR, unklare Skala, unbekanntes Profil oder Archivlimit: Unsicherheit/Sperre und manuelle Korrektur; kein Universalmapping. |
| Idempotenz / Wiederanlauf | Eigentümer, Quelldokument, belegte Revision, Formatprofil und bestätigte Zielauswahl; Dateiname allein ist kein Beweis. |
| Rückverweise und Abnahme | S2.11; MIG-10, MIG-11, MIG-25, MIG-31, MIG-36; UC-59; AT-S2-08/09/12/31/32 |

#### DEV — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | GerätestandAbgleichen(Konto, autorisiertesGerät, Basisrevision, lokaleÄnderungen) → erlaubte Übernahmen/Konflikte |
| Auslöser, Rechte und Vorbedingungen | Gültige Sitzung und freigegebenes Gerät; offline nur zuvor berechtigte heruntergeladene Inhalte. |
| Erfolg und Datenwirkung | Gültige eigene Änderungen abgleichen, aktuelle Lösch-/Entzugsgrenzen priorisieren; kein Livevertrauen aus Datei übernehmen. |
| Fehler und sichere Reaktion | Alter PWA-Client, Widerruf oder endgültige Löschung: betroffene Übernahme blockieren; Konflikt sichtbar; keine Behauptung erfolgreicher Fernlöschung. |
| Idempotenz / Wiederanlauf | Eigentümer, Gerät, Objekt, Basis-/Änderungsrevision und Wirkung; abgeglichene Änderung wird kein zweites Objekt. |
| Rückverweise und Abnahme | S2.7/S2.8; MIG-17, MIG-27, MIG-28, MIG-33; UC-04/05; AT-S2-24/36 |

#### BAK — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | SicherungspunktPruefen(eigenerSicherungspunkt, aktuellerKontrollstand) → Restorevorschau/Sperre; WiederherstellungFreigeben(Vorschaufassung, Auswahl) → Nachweis zulässiger Wiederherstellung |
| Auslöser, Rechte und Vorbedingungen | Automatischer interner Sicherungsauftrag oder ausdrücklich genehmigter Restore; Betriebsrecht ist kein privates Inhaltsrecht. Eigene Auswahl UC-60 und betrieblicher Disasterfall getrennt. |
| Erfolg und Datenwirkung | Verschlüsselte EU-Sicherung; nur freigegebener kohärenter Datenstand nach erneuter Anwendung aktueller Lösch-/Entzugsgrenzen wird aktiv. |
| Fehler und sichere Reaktion | Sicherung korrupt, Kontrollstand/Schlüssel fehlt oder Integrität ungeklärt: keinen aktiven Restore freigeben, sichere Pause und Diagnose. |
| Idempotenz / Wiederanlauf | Sicherung, Zielkontext, aktueller Kontrollstand und genehmigte Wirkungseinheit; Wiederaufnahme restauriert keine bereits gefilterten Ziele. |
| Rückverweise und Abnahme | S2.7/S2.10; MIG-15 bis MIG-17, MIG-22, MIG-23; UC-60; AT-S2-18/21/22/23/26 |

#### UPG — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | VersionsmigrationVorpruefen(Quell-/Zielschema, Änderungsplan, Kontrollstand) → Prüfbericht; VersionsmigrationFreigeben(geprüfterPlan, Testnachweis) → Cutover/Teilstand/Abbruch |
| Auslöser, Rechte und Vorbedingungen | Autorisierter Betriebs-/Deploymentprozess mit aktueller MFA/Recht, belegtem Mapping und zulässigem Testbestand. |
| Erfolg und Datenwirkung | Geprüfte Besitzer, Beziehungen, Fachzustände und Clientkompatibilität vor Wiederfreigabe; tatsächlicher Cutover nachweisbar. |
| Fehler und sichere Reaktion | Unerklärte Unterschiede, veralteter Kontrollstand oder nicht sicher wiederherstellbare Daten: keine Freigabe; Pause, kompatibler Rückfall oder nachgewiesene Vorwärtskorrektur. |
| Idempotenz / Wiederanlauf | Planfassung, Quell-/Zielschema, Objekt/Bereich und belegte Teiltransformation; kein erneuter destruktiver Schritt nach Neustart. |
| Rückverweise und Abnahme | S2.10; MIG-18 bis MIG-20, MIG-23, MIG-29; BAT-25; AT-S2-36/37 |

#### MOV — Vertragspräzisierung

| Aspekt | Festlegung |
|---|---|
| Operation / Ein- und Ausgabe | BetriebswechselVorpruefen(Quell-/Zielbetrieb, EU-/Schutznachweise, Datenstand) → Transferplan; BetriebswechselFreigeben(geprüfterPlan, Abgleichbericht) → geregelte Umschaltung |
| Auslöser, Rechte und Vorbedingungen | Ausdrücklich autorisierter Betriebsprozess; geeignetes EU-Ziel, sichere Transfer-/Schlüsselverwaltung und aktueller Lösch-/Widerrufskontrollstand. |
| Erfolg und Datenwirkung | Eigentum, Kontenisolierung, Vollständigkeit und Schutz vor Cutover belegen; Altbetrieb mit geklärter Retention schließen. |
| Fehler und sichere Reaktion | Fehlende Region-/Rechte-/Integritätsnachweise oder doppelte aktive Schreibzuständigkeit: kein Umschalten; gesicherter Zwischenstand und Diagnose. |
| Idempotenz / Wiederanlauf | Quell-/Zielbetrieb, Plan-/Bestandsfassung, Teiltransfer und Umschaltentscheidung; keine doppelte Aktivierung. |
| Rückverweise und Abnahme | S2.10; MIG-23, MIG-24, MIG-30; BAT-25; AT-S2-38/40 |

## S2.4 Umfang der übertragbaren Daten (Fachmatrix)

| Datenbereich | Persönlicher Export | Reimport/Restore | Wichtige Grenzen |
|---|---|---|---|
| Fachliches Profil, Studienkontext, Module, Institution/Notenskala | Ja, soweit zulässig | Eigene Daten nach Kontextabgleich | Amtlicher Nachweis bleibt mit Quellenstatus; institutionelle Verifikation wird nicht erfunden |
| Persönliche Lernunterlagen, ZIP-Quellen, PDF, Bilder, Text, Mitschriften | Originale nur bei rechtlicher Freigabe; sonst Referenz/Metadaten | Mit Quellkennung, Format-/Sicherheitsprüfung | Sensitivität/Kopierrecht/Quellrevision; Malware-/Archivschutz |
| Transkripte, Timestamps, Notizen, Analysen und Quellenbezüge | Vorhandene dauerhaft freigegebene Werte; temporär gelöschtes Rohtranskript **nicht** rekonstruieren | Abhängigkeiten und echte Timestamp-Verfügbarkeit prüfen | Keine erfundenen Zeitstempel oder erneute Verarbeitung ohne Einwilligung |
| Begriffs-/Wissenskarten, Kapitel, Fragen, Antworten, Quiz, Übungen | Ja als fachliche Struktur plus Ergebnisse | Nur tatsächlich kompatible Daten | Grafische Ansichten werden aus Beziehungen neu aufgebaut; keine KI-Neuerfindung |
| Lernprofil, Kompetenzevidenz, Prüfungsversuche, geschätzte Noten | Ja | Mit Quellen-/Zeit-/Verlässlichkeitsmerkmalen | Aktuelle Fortschritte nicht durch alte Schätzung überschreiben; offizielle Note strikt getrennt |
| Lernheft, Wiederholungen, Prioritäten, Wochenziele, Focus-/Pausenpräferenzen | Ja | Nach Versionsabgleich und Herkunftsschutz | Manuelle Sitzungen/Locks dürfen nicht ungefragt umgeplant werden; keine E-Mails versenden |
| Interne Termine/Reminder und Entwürfe | Ja | Manuelle Termine nur nach Prüfung; KI-/Importvorschläge bestätigungspflichtig | Keine externen Kalender schreiben; Zeitzone, DST, Serienregeln prüfen |
| Chats, Korrekturen, Änderungen, Quellenzitate, zulässige Historien | Ja gemäß Umfang und Retention | Nur noch zulässige aktuelle und historische Werte | Gelöschte Inhalte/Revisionen bleiben gelöscht; kein Audit-Shadow-Archiv |
| Projekte, Repository-Referenzen, analysierte öffentliche Metadaten | Ja nach Lizenz/Scope | Links/Metadaten, keine GitHub-Anmeldungen | Verbindung/GitHub-Scopes nie wiederaktivieren; öffentliches Repo ≠ private Freigabe |
| Eigene Benachrichtigungs- und Integrationshistorie | Soweit datenschutz-/retentionskonform | Als rein historische, inaktive Information | Keine erneute Zustellung, Autorisierung, Wiederanlauf oder Integration durch Import |
| Nutzerkonfiguration, Sprache, Anzeige- und Lernpräferenzen | Ja | Nur erlaubte persönliche Einstellungen; aktuelles Schema validieren | Aktuelle Feature-Flags, Rollen, Pflichtkontrollen nicht überschreibbar |
| Admin-/Serviceobjekte, Nutzerrollen, Super-Admin-Status | Kein Nutzerportablexport fremder/privilegierter Objekte | Nein über Self-Service | Gesonderte sichere Betriebs-/S3-Verfahren nötig |
| Passwörter/Hashes, aktive Sessions, OTP, MFA-Secrets, OAuth-Tokens, API-Schlüssel, Gerätevertrauen | **Nicht exportieren** als persönliche Migrationsdatei | **Nie automatisch reaktivieren** | Session, neue Geräte und neue Anbieterfreigabe getrennt prüfen |
| Schlüsselmaterial/E2EE-Recovery | Keine stille Klartextbeigabe | Nur gesonderter klientseitiger, authentisierter Schlüsseltransfer/-Recovery | Bei verlorenen Schlüsseln bleibt verschlüsselter Dateninhalt unlesbar |
| Endgültig gelöschte Objekte und unzulässige Schattenkopien | Nein | Nein | Lösch-/Widerrufsmarker priorisiert, keine Rekonstruktion aus Backups |

## S2.5 Fachlicher Exportvertrag

`PersoenlichenExportErstellen(Konto, Auswahl, Schutzoption, erwarteterStand) → Exportpaket | Teilpaket + Bericht | Fehler`

**Vorbedingungen:** Verifiziertes Konto, gültige Sitzung und Rechteprüfung; bei sensiblen Kategorien ggf. Step-up-Authentisierung und verfügbarer Schlüssel; zulässige Auswahl; Speicher-/Größenprüfung. Nutzer wählt **vollständig** oder **selektiv**. Er sieht Kategorien, erwartete Größe soweit abschätzbar, möglicherweise fehlende Originale, ungesicherte/ausgeschlossene Drittdateien und Schutzoptionen. Kein Zwang zu einem Drittcloudspeicher.

**Paketvertrag (fachlich, kein festgelegtes Binärformat):**
- Versionsnummer für Paket- und Fachschema, Erstellzeit, Exportzeitpunkt und Konsistenz-/Stichtagsbasis.
- Eindeutige Export-ID ohne wiederverwendbare Liveberechtigung, Zuordnung zu Exportbereichen, Inhaltsverzeichnis mit Dateipfad, Typ, Größe, Integritäts-/Versionsmerkmal und sensibler Kategorie.
- Quell-/Zielkontexte soweit exportierbar: Modul, Semester, Originalquelle, Seiten-/Zeitreferenz, Revision, Nutzer-/amtlich-/KI-Nachweisstatus, Abhängigkeiten, Ursprungs-/Änderungsstand.
- Erfassungsumfang, bewusst ausgeschlossene und technisch ausgefallene Bestandteile, sowie Exportprüfergebnis.
- Zeit-/Zeitzoneninformationen und kompatible Datentyp-/Enumerationswerte; fremde private IDs als **nicht übertragbare** Referenzen.
- Standardoffene, dokumentierte Kodierungen; kein ausführbares Importprogramm. Schutz sensibler Pakete durch später verbindlich spezifizierte, starke Verschlüsselungsoption samt Wiederherstellungshinweisen.

**Nachbedingungen:** Datenzustand bleibt unverändert; Export erzeugt keine externe Integration und verlängert keine abgelaufenen Freigaben. Ein Downloadhinweis bestätigt nicht, dass eine externe Datei später verfügbar oder entschlüsselbar ist. Temporäre serverseitige Exportdateien werden nach endlicher konfigurierbarer Frist bereinigt. Logs enthalten minimalen Exportnachweis, keinen unverschlüsselten Vollinhalt. Konto-/Inhaltslöschung wird nicht durch den Export blockiert.

## S2.6 Fachlicher Import-/Restore-Vertrag

`ImportVorschauErstellen(Konto, Paket, Zielkontext) → Validierungsbericht + Delta + Auswahlmoeglichkeiten`
`ImportEntwurfBestaetigen(Konto, Entwurfsrevision, gewaehlteTeilwirkungen, Konfliktentscheidungen, aktuelleRechte) → Importlauf`
`ImportlaufPruefen(Importlauf) → Fortschritt, wirksame Teilresultate, verbleibende Fehler`
`ImportAbbrechen(Importlauf) → kontrollierter Stop + bereitsWirksameResultate`

**Verbindliche Prüfkette:**
1. Nutzer/Session/Device und Schritt-für-Schritt-Freigabe prüfen; Paket als nicht vertrauenswürdig isoliert und nur innerhalb zulässiger endlicher Prüfaufbewahrung behandeln.
2. Archiv/Format sicher analysieren: Dateitypen real feststellen; Archive gegen Path Traversal, Symlinks, Entpackbomben, Rekursion und Größen-/Zeitlimits absichern; Skripte/Makros/aktive HTML- oder Markdown-Prompts niemals ausführen.
3. Manifest, Schema, Datenklassen, Objektbezüge, Integrität und Schlüsselzugänglichkeit prüfen. Unbekannte Felder als **nicht verarbeitbar** markieren; nicht als Rechte- oder Löschregeln interpretieren.
4. Quellidentität **nicht** als Zielkontoberechtigung akzeptieren. Ziele aus bestehenden erlaubten eigenen Objekten oder neuen zulässigen Objekten ableiten. Mandantentrennung überall prüfen, auch bei Verweisen und Indizes.
5. Aktuelle Lösch-/Sperr-/Widerrufsstände **vor** fachlicher Zusammenführung auswerten. Dokument- und Originalversionen niemals still ersetzen. Rechte werden direkt vor Ausführung erneut validiert.
6. Fachliche Vorschau mit Menge `neu / identisch / Änderung möglich / Konflikt / ausgeschlossen / unsicher / fehlende Abhängigkeit`, inklusive manueller Termin- und Profilfortschrittswarnung.
7. Nutzer bestätigt genau die **konkrete** Vorschauversion, betroffene Objekte und Konfliktstrategie; Änderungen zwischen Vorschau und Wirkung erzwingen erneute Bewertung (TOCTOU).
8. Übernahme je sicher definierter fachlicher Wirkungseinheit konsistent durchführen; die technische Transaktionslösung bleibt offen; große Importe als wiederaufnehmbare Jobs mit stabiler idempotenter Wirkung.
9. Nachbearbeiten: Suchindizes und abgeleitete Ansichten nur autorisiert rekonstruieren; Quellen-/Versions-/Sensitivitätsmetadaten kontrollieren; nie neue Erinnerungen/Nachrichten ungefragt senden.
10. Vollständigen Wirkungsausweis bereitstellen: neu/aktualisiert/unverändert/übersprungen/gesperrt/Fehler, Zeit und noch offene manuelle Entscheidungen.

**Konfliktstrategien:**
- `BestehendeVersionBehalten`: Zielstand und jüngere Evidenz erhalten.
- `QuellfassungAnnehmen`: nur ausgewählte, freigegebene **Inhaltsfelder**; nie Rechte/IDs/Revisionshistorie/Löschstatus blind überschreiben.
- `AlsGetrennteKopieUebernehmen`: nur bei frei kopierbarem Inhalt, eigener neuer Identität und korrigierten Verweisen; bei amtlichen Noten, Terminen und Sicherheitseinstellungen ggf. verboten.
- `Ueberspringen`: keine Wirkung, begründeter Bericht.
- `ManuellZusammenfuehren`: Feld-/Objektvorschau bei echten Konflikten, erneute Freigabe der Ergebnisfassung.

**Rücknahme:** Ein noch nicht begonnener Entwurf kann folgenlos verworfen werden. Bereits wirksame Importe können ggf. mit einem **neuen autorisierten Korrekturvorgang** rückgängig gemacht werden; kein versprochener globaler Undo, der zwischenzeitliche Erfolge, externe Wirkungen oder geschützte Änderungen entfernt. Bei partiellen Fehlern wird der Status nicht als vollständig erfolgreich angezeigt.

## S2.7 Löschung, Papierkorb, Backups und Nichtwiederbelebung

1. **Prioritätsordnung:** geltender Kontostatus/Objekteigentum → endgültige Löschgrenze/Widerruf → aktuelle Rechte/Schlüssel → gültige neue Revision/Bestätigung → ältere Import-/Backupfassung. Weder „neueste Datei“ noch Adminrechte schlagen diese Ordnung.
2. Endgültig gelöschte Inhalte dürfen weder durch Paketimport noch durch historische Versionen, Offlinewarteschlangen, Snapshots, Indizes, Lernprofile, Auswertungen oder Betriebsrestore wieder **aktiv** werden. Notwendige minimale Löschmarker dürfen kein vollständiges Geheim-/Lerninhaltsarchiv sein.
3. Papierkorb und **widerruflich** gelöschte Objekte (FE-81) sind von abgeschlossener endgültiger Löschung (FE-80) und pausierten Accounts (FE-82) zu unterscheiden. Papierkorb-Restore innerhalb tatsächlich gültiger Frist kann möglich sein, aber nur nach aktueller Berechtigungs- und Versionsprüfung.
4. In Backups noch physisch gespeicherte Inhalte, die rechtlichen Aufbewahrungsgründen oder endlichen Backupzyklen unterliegen, sind vom *aktiven* Objektbestand getrennt. Die zugesagte Bereinigung muss real nachweisbar oder noch als ausstehend markiert sein; keine behauptete sofortige Löschung aus allen existierenden Sicherungen.
5. Betriebliches Restore und Datenbank-Migration müssen Lösch- und Widerrufsgrenzen aus einem belastbaren, vom Sicherungsstand getrennt überprüften Kontrollstand erneut anwenden; Mechanismus/Lebensdauer und Ausfallszenarien sind in N2/S3 konkret zu sichern.
6. Wiederhergestellte Integrationen bleiben **inaktiv**. Entzogene OAuth-Rechte, abgelaufene Gerätefreigaben, entfernte Supportfreigaben, deaktivierte Konten und Admin-Berechtigungen werden niemals aus alten Sicherungen aktiv gesetzt.
7. Temporäre Audio-/Video-Transkripte oder KI-Zwischenergebnisse, die nach FE-52 ausgelaufen sind, sind kein normales wiederherstellbares Archiv.

## S2.8 Sicherheit, Schlüssel, Identitäten und Vertraulichkeit

- Strikter Eigentümerbezug, serverseitige Autorisierung und Mandantenisolation über Paketvorschau, Download, Ergebnisprotokoll, Suchindex, Wiederaufnahme und Restore hinweg (FE-59, SEC-04).
- Authentifizierung, MFA, Gerätezulassung, lokales Entsperren und Dokumentenschlüssel sind verschieden; keine Übertragung aktiver Vertrauenszustände über Dateiexport.
- Für E2EE-Inhalte ist ein eigener, explizit geschützter Schlüsseltransport/-Recoveryplan notwendig; ein verschlüsseltes Backup ohne Schlüssel kann technisch korrekt gespeichert sein und trotzdem nicht entschlüsselt werden. Keine versteckten Server-Backdoor-Schlüssel.
- Zugriffe des Betreibers/Supportadmins auf fremde persönliche Inhalte bleiben standardmäßig verboten; Betriebs-Wiederherstellung ist keine Inhaltsfreigabe.
- Sensible Anhänge/Quellen und abgeleitete Zusammenfassungen erben ihre Schutzklasse (FE-79). Vertrauliche Cloudanalyse nach FE-78 erfordert einen gesonderten konkreten Auftrag; Import allein löst keine Klartextfreigabe an KI aus.
- Exportwarnung bei Zielgerät und unverschlüsselten Dateien; lokale Dateien nach Download liegen außerhalb der technischen Kontrolle des Syllentra-Servers. Dies wird transparent erklärt, nicht als Garantie „überall gelöscht“ dargestellt.
- Logs, Diagnose, Metriken und Fehlerberichte minimal und kontogebunden; keine unnötigen Lerndaten/Transkripte/Schlüssel in Betriebsaudit oder Adminoberfläche.

## S2.9 Laufzustände und sichere Wiederaufnahme

Fachliche Zustände: `entwurf` → `pruefung` → `vorschau_bereit` → `bestaetigung_ausstehend` → `ausfuehrung` → `erfolgreich` | `teilweise_erfolgreich` | `abgebrochen` | `pausiert` | `fehlgeschlagen` | `nicht_pruefbar` | `wirkung_unbekannt`.

Jeder Lauf kennt Eigentümer, Zweck, freigegebene Datenauswahl, Quelldaten-/Zielschemafassung, **wirksame** Teiloperationen, zulässigen Retryplan und Ablauf-/Abbruchstatus. Keine Doppelwirkung durch erneutes Klicken, Zeitüberschreitung, Worker-Neustart, Absturz oder Netzunterbruch. Für externe Aktionen unklare Wirkung zunächst prüfen statt blind neu ausführen (FE-88); S2 selbst startet keine externen Schreiboperationen. Alle erfolgreichen Teilschritte werden nachvollziehbar, weitere Schritte nur nach erneuter Rechte-/Lösch-/Kostenkontrolle fortgesetzt. Nicht bekannte Ergebnislage ist kein Erfolg.

**Fehlerklassen:** beschädigt/manipuliert, Format unbekannt, inkompatible Version, unvollständige Abhängigkeit, zu groß/Quote, Entpack- oder Sicherheitssperre, fehlender Schlüssel, abgelaufene Anmeldung, fehlende Objektberechtigung, Konto-Sperre, bereits endgültig gelöscht, konkurrierende Aktualisierung, korrupte Quellversion, unklare Wirkung, Speichermangel und Betriebsunterbrechung. Jede Klasse erhält eine konkrete und datenschutzgerechte Rückfallhandlung: Nutzerkorrektur, Teilimport, erneute Vorschau, Pause/Retry bei transientem Fehler, oder sicherer Abbruch ohne Zugriffserweiterung.

## S2.10 Release-, Schema- und Betriebsdatenmigration

| Schritt | Mindestanforderung | Negativer Schutzfall |
|---|---|---|
| Vorprüfung | Aktuellen Stand, Mengen, Sicherheits-/Eigentumsvoraussetzungen und Schema-Kompatibilität erfassen; echte Wiederherstellbarkeit der Sicherung in Testumgebung prüfen | „Backup existiert“ gilt nicht als Restorebeweis |
| Planung | Änderungs-/Feldmapping, Transformationsregeln, Invarianten, Alternativ-/Abbruchpfad und fachliche Impactliste definieren | Keine destruktive Spaltenlöschung ohne nachgewiesene Datenstrategie |
| Trockenlauf | Nichtproduktive Migration auf geeigneter repräsentativer Kopie; Datenschutz/Schlüssel beachten | Keine privaten Live-Daten in offenen Testsystemen |
| Kompatibilität | Gestaffelte App-/Schema-Versionen und alte PWA-Clients berücksichtigen; Versionsgrenze dokumentieren | Alter Client darf keine neue Löschmarkierung überschreiben |
| Ausführung | Berechtigt, überwacht, nachvollziehbar und wiederaufnehmbar; Wartungs-/Read-only-Phase wenn nötig | Paralleloperation erzeugt keine fremden oder doppelten Objekte |
| Nachprüfung | Mengenabgleich **plus** referenzielle Integrität, Eigentum, Lösch-/Schlüssel-/Rollenstatus, Quellen und fachliche Beispiele | Gleich hohe Datensatzanzahl allein genügt nicht |
| Freigabe | Tatsächlichen Sicherheits-/Integritäts- und Verfügbarkeitsstatus nachweisen, erst dann Umschalten | Unerklärte Unterschiede → kein stiller Go-live |
| Rückfall | Soweit machbar kompatibel auf letzten sicheren Zustand/Forward-Fix, mit aktuellen Lösch-/Widerrufsdaten | Älteres Backup nie ungesichert über heutige Löschgrenzen legen |

**Zielsystem-/Hostingwechsel:** Export und Import der **gesamten internen produktiven Betriebsdaten** ist ausschließlich ein administrativ kontrollierter MOV-/S3-Prozess, **nicht** die gewöhnliche benutzereigene Portabilitätsfunktion. EU-Speicherort, gesonderte Adminrechte, Backup-/Schlüsselverwaltung, Logging, Datenvollständigkeit, Rollback-Risiko und End-of-life der alten Umgebung prüfen. Anbieter und Transferdauer bleiben technische Entscheidungen, nicht erfundene Zusagen.

## S2.11 Zulässige Fremd- und Lehrmaterialimporte

**V1-Mindestumfang:** Syllentra-eigener versionierter Export/Reimport, manuelle Markdown-/TXT-/JSON-/CSV-Datenübernahme und die bereits in FE-27–29/48–49 vorgesehenen unterstützten PDF-/Bild-/Tabellen-/Kalender-/Archivimporte für konkrete Lern- und Studienzwecke. Diese Formate haben **verschiedene** zulässige Bedeutungen. PDF ist keine verlustfrei migrierbare persönliche Datenbank; OCR ist keine gesicherte amtliche Quelle. ICS hat Terminsemantik, kein automatisches Schreibrecht in ein fremdes Kalenderkonto. JSON/CSV wird nach **definiertem Profil** gemappt, nicht beliebig in interne Felder übernommen.

**Zusätzliche Importmöglichkeiten, wenn ein echter Adapter vorliegt:** Browser-/Markdown-Notizen, begrenzte Karteikarten-/Frageexporte und strukturierte Listen aus Drittlernapps. Ohne spezifische geprüfte Formatregeln keine Universalgarantie für Anki, Notion, Moodle, GitHub, Google Drive, OneDrive oder einen beliebigen Chatverlauf. Universelle Cloud-Accountmigration, automatische Inbox-Lektüre FE-56, fremde Backups und native OS-Keychain-Dumps bleiben ausdrücklich ausgeschlossen.

Ein identischer Dateiname oder eine gleichartige Übungsfrage genügt nicht für automatische Zusammenführung. Quellherkunft, Erstell- und Bearbeitungszeit, Format, Version, Kurszuordnung, Nutzereinwilligung und Sensitivität müssen erhalten/markiert werden. Bei unklarer Zuordnung Vorschlag mit Nutzerprüfung statt stiller Änderung.

## S2.12 Verhalten von Lernheft, Lernprofil und neuer V1-Pädagogik

Die nach S1 bestätigten `DEC-V1-01` bis `DEC-V1-25` waren am historischen S2-Ausgangsstand noch nicht vollständig harmonisiert. Die Konsolidierung vom 22.10.2026 ist jetzt in der [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md) mit Fachvarianten, Daten und Soll-Abnahmen nachgewiesen; keine dieser Vorgaben ist damit implementiert oder produktgetestet. S2 unterstützt ihre künftige Datenportabilität: einfache Wissenskarte, zitierfähige PDF-/Audioquellen, persönliche Lernpräferenzen, Kompetenzhistorie, fächerübergreifende Beziehungen, Wiederholungsplanung, automatische und manuelle Aufgaben/Sitzungen, Pausenhinweise, Fokusmodus, Lernbilanzen, Probeprüfungen, Dashboards und Wochenziele.

**Bewahrung bei Restore:**
- Eine **manuell terminierte Sitzung** behält Datum/Zeit und manuelle Herkunft; ein älteres Paket darf sie nicht unbemerkt verschieben. Jeder Vorschlag ist vor Wirkung konkret freizugeben.
- DEC-V1-10/11/13 und die jetzt integrierte Präzisierung L-08 erlauben nur ausdrücklich aktivierte persönliche pädagogische Reihenfolgeautomatik; sie erteilen keine Kalenderzustimmung. S2 stellt solche Einstellungen ausschließlich als inaktive oder erneut zu prüfende Präferenzen wieder her; es führt weder diese Neuordnung noch neue Lernaktivitäten durch. Das Undo einer Planänderung darf keine zwischenzeitlichen Fortschritte zurücksetzen. Ein Eintrag im internen Kalender unterliegt weiterhin dessen bestehenden Bestätigungsregeln; manuell gesetzte oder gesperrte Sitzungen bleiben geschützt.
- Nachweislich jüngere Lernergebnisse, manuelle Korrekturen und Nutzervorgaben haben Vorrang vor älteren automatischen Niveau-Schätzungen. Schätzung ≠ demonstrierte Kompetenz ≠ amtliche Leistung.
- Spaced-Repetition-Intervalle und Prioritäten müssen nachvollziehbar neu berechnet werden können; ältere oder fehlende Daten erzeugen keine erfundene abgeschlossene Wiederholung.
- Syllentra Games und fortgeschrittene automatisch generierte Wissensgraphen sind **nicht** Voraussetzung für V1-Migration; keine neuen, impliziten Game-Datenpflichten.

### S2.12.1 Vollständiger Abgleich des ergänzenden V1-Kontexts

Die folgenden DEC-V1-Schlüssel sind ausschließlich die temporären Auditbezüge der dritten Anlage. Sie werden nicht in FE umnummeriert. Am damaligen S2-Ausgangs-HEAD war keine separate vollständige Post-S1-Harmonisierung nachgewiesen. Diese S2-Tabelle bleibt auf Bewahrung kompatibler Daten und ehrliche Lückenhinweise beschränkt; die heutigen Fach-/Dialog-/Datenanschlüsse und Abnahmen stehen in der [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md). Keine technische Implementierung oder neue Lernformel wird behauptet.

| Auditbezug | Deutscher Fachkontext | S2-Grenze / Bewahrung |
|---|---|---|
| DEC-V1-01 | Klassische zugängliche PWA-Oberfläche | Nur unterstützte persönliche Anzeigepräferenzen übernehmen; keine Graphnavigation erzwingen. |
| DEC-V1-02 | Einfache interaktive Wissenskarte | Vorhandene Begriffe/Beziehungen versioniert übernehmen, Ansicht nur daraus aufbauen; fehlende Semantik nicht erfinden. |
| DEC-V1-03 | Direkter Quellenpassagenzugang | Originalrevision, PDF-Seite und nur belegbare Medienzeit erhalten; bei Fehlen Quelle/Seite als Rückfallweg. |
| DEC-V1-04 | Vorgeschlagene und manuell gestartete Übungen | Herkunft und freiwilligen Modus erhalten, keinen Übungsstart durch Import auslösen. |
| DEC-V1-05 | Adaptive Erklärungen und wählbare Alternativen | Vorhandene Rückmeldungen/Präferenzen mit Herkunft übernehmen; keine starren Lernstilklassen neu ableiten. |
| DEC-V1-06 | Sichtbares korrigierbares Lernprofil | Vorhandene erlaubte Profilinformationen übertragen; Deaktivierung/Reset und jüngere Korrekturen beachten, keine Gesundheitsinferenz. |
| DEC-V1-07 | Aktuelle geschätzte Beherrschung | Belegzeit und Schätzstatus erhalten; ältere Schätzung verdrängt keine jüngere Evidenz. |
| DEC-V1-08 | Freiwillige Sitzungsrückmeldung | Nur vorhandenes erlaubtes Feedback übernehmen; fehlende Rückmeldung ist keine bestätigte Selbsteinschätzung. |
| DEC-V1-09 | Erklärbare fächerübergreifende Bezüge | Nur belegte kompatible Relationen erhalten; kein automatischer Kompetenztransfer auf andere Fächer. |
| DEC-V1-10 | Automatische interne Lernheftordnung | Einstellung und Änderungshistorie als Präferenz/Historie, nicht als aktive Ausführungserlaubnis restaurieren; Kalender getrennt. |
| DEC-V1-11 | Rücknahme einer Planänderung | Planrevisionen erhalten, zwischenzeitliche Fortschritte niemals rücksetzen. |
| DEC-V1-12 | Schutz manuell gesetzter Sitzungen | Manuelle Herkunft und Terminbindung erhalten; Verschiebung nur nach konkreter ausdrücklicher Bestätigung. |
| DEC-V1-13 | Kurze zusätzliche Wiederholung bei vermutetem Vergessen | Vorhandene Wiederholungsvorschläge übertragen; Import erzeugt keine neue Wiederholung. |
| DEC-V1-14 | Adaptive veränderbare Wiederholungsintervalle | Vorhandene Regel/Grundlage übernehmen, keine erfundenen Erledigungen; Parameter bleiben überprüfbar. |
| DEC-V1-15 | Automatische, manuelle und hybride Priorisierung | Bewusste Sperren und gewählte Modi erhalten; importierter Modus startet keine Neuplanung. |
| DEC-V1-16 | Realistische Priorisierung bei Zeitmangel | Begründungen/gewählte Aufgaben erhalten; Restore überplant keine verfügbare Zeit. |
| DEC-V1-17 | Tatsächlich benötigte Lerndauer | Messung von Schätzung unterscheiden; keine erfundenen Zeitgewinne aus alter Historie. |
| DEC-V1-18 | Freiwillige diskrete Blockadehilfe | Gewählte Häufigkeit/Deaktivierung als Präferenz übernehmen; keine Hilfe oder Meldung auslösen. |
| DEC-V1-19 | Vorsichtige Pausenvorschläge | Nutzerwahl/Deaktivierung respektieren; keine Diagnosen oder automatische Sitzungsunterbrechung. |
| DEC-V1-20 | Optionaler Konzentrationsmodus | Kompatible persönliche Ansicht/Timerpräferenz, keine Unterdrückung notwendiger Sicherheitshinweise. |
| DEC-V1-21 | Optionale Sitzungsbilanz | Vorhandene Bilanz mit Herkunft/Revision/Deaktivierung erhalten; keine amtliche Note oder neue Bilanz erfinden. |
| DEC-V1-22 | Freiwillige Probeprüfung | Vorhandene Aufgaben, verfügbare Quellen und geschätzten Bewertungsstatus erhalten; kein Prüfungsstart durch Restore. |
| DEC-V1-23 | Prüfungs- und Trainingsmodus | Modus und Hilfen nachvollziehbar, Eigenleistung getrennt; nach Import keine Vermischung in aktuellem Versuch. |
| DEC-V1-24 | Begründetes persönliches Dashboard | Nur erlaubte eigene Datenbasis; Darstellung neu aus aktuellem Schutz-/Evidenzstand, keine private Notenvorschau. |
| DEC-V1-25 | Freiwilliges Wochenziel | Vorhandene Wahl, Ablehnung oder Aufschub übernehmen, keine erfundene Wochenpflicht. |

## S2.13 UI-/Benachrichtigungs- und Administrationsfolgen

- Nutzeroberfläche (B1): „Daten exportieren“, „Daten importieren/wiederherstellen“, Bereich-/Kursauswahl, verständliche Größen-/Datenschutzwarnung, Test/Vorschau, Seitenvergleich (alt/neu), Konfliktentscheidung, Bestätigung, Fortschritt, differenzierter Ergebnisbericht und Verlauf.
- Nutzer darf Export-/Importentwurf abbrechen; Hintergrundlauf nur innerhalb einer konkreten freigegebenen Aufgabe. Keine Pflichtverbindung zu externem Speicherdienst. Vorsicht bei Browser-/PWA-Größenlimits, Nutzerfallback vorab erklären.
- Serviceadmin: nur kontenfreie Summen/Fehlerdiagnose für Kapazitätsplanung; kein pauschaler Vollzugriff auf Nutzerexporte oder Schlüssel. Super Admin kann Quoten, technische Zulassung von Importformaten und Featureflags verwalten, **nicht** fremde Nutzerpakete beliebig lesen.
- Nichtdringende Migrationshinweise als Digest möglich; kritische Kontosicherheits-/Integritätsprobleme nach bestehenden Nachrichten- und Authregeln. Keine Massenzustellung oder exportierte Benachrichtigung rückwirkend automatisch verschicken.
- Barrierefreiheit: Screenreader-fähige konfliktfreie Alternativen, tastaturbedienbare Auswahl, nicht nur farbliche Differenzen, verständliche Fehlermeldungen, mobile PWA und mehrsprachige UI-DE/FR/EN gemäß FE-73.

## S2.14 Abnahmematrix (AT-S2-01 bis AT-S2-40)

| Prüffall | Gegeben / Aktion | Erwartetes Ergebnis |
|---|---|---|
| AT-S2-01 | Verifizierte Person fordert eigenen vollständigen Export an | Vollständiger **tatsächlich vorhandener** zulässiger Bestand samt Manifest, Ausschlüssen und Status |
| AT-S2-02 | Export nur von Kurs A | Keine privaten Daten von Kurs B, außer explizit erklärte referentielle Minimaldaten |
| AT-S2-03 | JSON-/CSV-Anzeige gegenüber PDF-Original | Struktur und Originale getrennt; keine falsche verlustfreie Extraktion |
| AT-S2-04 | Export zweimal ohne Datenänderung | Belegbarer vergleichbarer Bestand, keine erzeugten Doubletten |
| AT-S2-05 | Paket mit korrekter Kennung eines fremden Kontos | Keine Autorisierung/Anzeige von fremden Daten |
| AT-S2-06 | Reimport in identisches eigenes Konto | Vorschau und Bestätigung vor fachlicher Wirkung |
| AT-S2-07 | Paket beschädigt/manipuliert | Sperre/Fehler, kein partieller unbemerkter Code-/Datenimport |
| AT-S2-08 | ZIP enthält `../secret` oder Symlinkflucht | Schutzprüfung blockiert Pfadflucht |
| AT-S2-09 | Extrem große oder rekursive Archivdaten | Konfiguriertes Limit mit sicherer Fehlermeldung |
| AT-S2-10 | Gleiches Paket wird erneut importiert | Keine fachliche Doppelanlage |
| AT-S2-11 | Zwei konkurrierende Versionen einer Lernnotiz | Konfliktansicht, keine stille Überschreibung |
| AT-S2-12 | Fehlender Quellbezug oder alte Quellseite | Als fehlend/veraltet kenntlich, kein erfundener Quellenbeweis |
| AT-S2-13 | Import nur einer Modulgruppe | Andere Module und Einstellungen bleiben unverändert |
| AT-S2-14 | Import während bestehendes Zielobjekt geändert wurde | Vorschau wird ungültig; Neubewertung notwendig |
| AT-S2-15 | Nutzer bricht vor Bestätigung ab | Keine fachlich wirksamen Änderungen |
| AT-S2-16 | Lauf wird bei Hälfte unterbrochen | Bereits wirksame Teilresultate ausgewiesen; idempotente Fortsetzung |
| AT-S2-17 | Netzwerk trennt nach unklarem Erfolg | Abgleich statt blindem doppelten Import |
| AT-S2-18 | Nicht verfügbarer E2EE-Schlüssel | Inhalt nicht entschlüsselbar, keine Backdoor/kein vorgetäuschter Restore |
| AT-S2-19 | Export enthält Geheimnis-/Session-/OTP-Feld | Feld gesperrt, niemals erneut aktiviert |
| AT-S2-20 | Paket enthält Adminrollen/Integrationsfreigaben | Rollen/Tokens/Scopes werden nicht übernommen |
| AT-S2-21 | Nutzer hat Objekt endgültig gelöscht, altes Paket enthält es | Objekt bleibt gelöscht, kein Revival |
| AT-S2-22 | Backup von vor Löschung wird betrieblich eingespielt | Nach Löschkontrolle kein aktives Wiederauferstehen |
| AT-S2-23 | Objekt befindet sich nur im zulässigen Papierkorb | Restore entsprechend Frist und aktueller Autorisierung möglich |
| AT-S2-24 | Offlinegerät synchronisiert gelöschten Inhalt | Keine Wiederbelebung in Cloud/anderen Geräten |
| AT-S2-25 | Konto B versucht Import-/Exportjob von A abzurufen | Keine Metadaten, Inhalte oder Schlüssel sichtbar |
| AT-S2-26 | Frühere Supportfreigabe ist abgelaufen | Import/Backup stellt keinen Supportzugriff wieder her |
| AT-S2-27 | Manuell angesetzte Lernsitzung aus altem Export | Ohne spezifische Zustimmung keine Zeitänderung |
| AT-S2-28 | Automatische Planänderung wird zurückgenommen | Plan wiederhergestellt, neuer Lernerfolg bleibt erhalten |
| AT-S2-29 | Altes Profil mit niedriger Schätzung, neue Beweislage stärker | Jüngere Beweislage bleibt; Konflikt/Provenienz sichtbar |
| AT-S2-30 | Alte Quiznote war KI-Schätzung | Nach Import weiterhin „geschätzt“, keine amtliche Notenbestätigung |
| AT-S2-31 | Externer Kalender wird mitimportiert | Kein Schreibaufruf an Dritt-Kalender |
| AT-S2-32 | Zulässiger lokaler Dokumentimport bei FE-56 offen | Keine Mailboxanmeldung oder Inboxautomatik |
| AT-S2-33 | Ursprüngliche Podcast-/Videodatei nicht mehr vorhanden | Keine erdachten Transkriptzeitstempel oder Quellenkopie |
| AT-S2-34 | Browser kann großes Paket nicht lokal halten | Transparenter begrenzter Alternativablauf statt Speicherüberlauf |
| AT-S2-35 | Exportpaket verschlüsselt, Nutzerschlüssel verloren | Verständliche Nicht-Wiederherstellbarkeit dokumentiert |
| AT-S2-36 | Appupgrade mit altem PWA-Client | Alte Schreibversuche dürfen neue Sicherheits-/Löschregeln nicht aufheben |
| AT-S2-37 | Schemawechsel an repräsentativer Kopie | Eigentümer, Beziehungen und Fachzustand stimmen nach Validierung |
| AT-S2-38 | Betreiberwechsel in EU | Protokollierter Cutover, Zugriff-/Schlüsselprüfung und sichere Altretention |
| AT-S2-39 | Quoten-/Retentionsgrenze erreicht | Transparente Warnung; keine heimliche Nutzerlöschung oder Datenfreigabe |
| AT-S2-40 | Admin sieht Migrationsstatistik eines fremden Kontos | Nur zulässige technische Metadaten, keine privaten Dokument-/Noteninhalte |

**Teststatus:** Diese Fälle sind **Spezifikationsabnahmekriterien, keine tatsächlich ausgeführten Anwendungstests**. Sicherheits-, Last-, Restore-, Browser-, E2EE- und Konnektortests sind vor Freischaltung anhand echter Implementierungen nachzuweisen.

## S2.15 Dokumentübergreifende Zuordnung

| Querverweis | S2-relevante Festlegung und erwartete Ergänzung durch Codex |
|---|---|
| [P1](P1-ziele-rahmenbedingungen.md) | Portabilität, Datenhoheit, kostenlose zulässige Basis, V1/Sonderfälle, Nutzerkontrolle |
| [P2](P2-architekturueberblick.md) | Interne EU-Cloud und Geräte sind Produktbestandteile; externe Speicher und Kalender nach S1 streng read-only |
| [F1](F1-geschaeftsprozesse.md) | GP-15 Datenkontrolle/Export/Löschung; mögliche Nachträge für Migrations-/Wiederherstellungsprozesse |
| [F2](F2-anwendungsfaelle.md) | UC-04/UC-05 Geräte; UC-49 Export; UC-50 Löschfolgen; UC-60 Restore; neuer UC-64 eigener Reimport mit Vorschau/Bestätigung |
| [F3](F3-anwendungsfunktionen.md) | AF-01/AF-02 Rechte/Herkunft, AF-06 Vorschlagsfassung, AF-26 Export-/Löschumfang, AF-34 Löschfilter; neuer AF-36 Paket-/Mapping-/Deltaprüfung |
| [D1](D1-datenmodell.md) | DM-01 Eigentümer, DM-20..22 Materialien, DM-02 Lernpräferenzen und DM-33..DM-34 pädagogische Erinnerung, DM-35 Kalender, DM-37 Import, DM-39..42 Vorschläge, DM-44 Autorisierung, DM-50 Datenkontrolle, DM-68 Löschmarken; neue DM-72 Portabilitätspaket, DM-73 Migrationslauf, DM-74 MigrationsTeilwirkung; bestehende DM-69/DM-70 Sicherung/Restore bleiben getrennt |
| [D2](D2-datentypen.md) | DT-86 ExportmanifestDT, DT-87 MigrationszustandDT, DT-88 MigrationsdeltaDT, DT-89 MigrationswirkungDT, DT-90 MigrationswegDT; DT-77/78/79 Schutz/Schlüssel/Freigabe bleiben maßgeblich |
| [B1](B1-dialogspezifikation.md) | DLG-49 Export, DLG-61 Restore und neuer DLG-65 Portabilitätspaket, Vorschau, Konflikt, Fortschritt/Verlauf; Tastatur-/Screenreader-/DE-FR-EN-Prüfung |
| [B2](B2-batch.md) | BAT-23 Backup/Restore erhalten; BAT-24 Portabilitätsaufträge und BAT-25 Versions-/Betriebsmigration ergänzen, ohne stillen Erststart |
| [B3](B3-druckausgaben.md) | OUT-08 maschinenlesbarer Nutzerdatenexport samt Manifest und Vollständigkeits-/Migrationsbericht; keine neue OUT-Kennung und keine private Admin-Einsicht |
| [S1](S1-nachbarsysteme.md) | NB-01/03/04/06/07/08/10/12; keine zusätzlichen externen Schreibrechte, keine fiktiven Anbieteranschlüsse |
| [N1](N1-nichtfunktional.md) | Realistische Kapazität, Barrierefreiheit, Browser-/PWA-/Offline-/Performancegrenzen, technische Kennzahlen erst mit Messung |
| [N2](N2-querschnittskonzepte.md) | SEC-04 (Mandant), SEC-08 ff. (Schlüssel), SEC-15 (Löschung), SEC-16 (Konto), Backups, nicht wiederbelebende Restores |
| [E2](E2-glossar.md) / [E3](E3-pruefnachweis.md) / [README](README.md) | Begriffsklärungen, Änderungs-/Prüfnachweis, realer Dokumentstatus und korrekte Links |

**Traceability zu Bestandsanforderungen:** FE-08, FE-09, FE-12, FE-13, FE-26 bis FE-29, FE-33 bis FE-42, FE-47 bis FE-50, FE-53, FE-55, FE-58 bis FE-63, FE-64/65, FE-73 bis FE-83 und FE-84 bis FE-89. Neue spezifische FE-Kennungen nur nach Dublettenprüfung und laufendem Nummernkreis; die S2-internen MIG-IDs sind **keine offiziellen FE-Nachträge**.

## S2.16 Explizite Nichtziele V1 und spätere Ausbauten

Nicht V1-verbindlich: automatische Übernahme *aller* Daten beliebiger fremder Lernapps; Migration fremder/gelöschter fremder Konten; vollständiges Offline-Backup mit allen geheimen Schlüsseln in der PWA; automatische GitHub-/OneDrive-/Drive-Schreibsynchronisierung; aktivierte Mail-Inbox-Funktion FE-56; automatische kostenpflichtige Konverter; garantierter verlustfreier Export jeder proprietären Formatsemantik; native Mobile-Keychain-Funktionen auf allen Browsern; automatisch verifizierte amtliche Prüfungsdaten; freie Datenbank-Dumps als Nutzerselfservice. Zusätzliche Adapter später nur nach dokumentiertem Format-, Lizenz-, Datenschutz- und Sicherheitstest. Produktfeatures aus dem separat bestätigten DEC-V1-Katalog sind davon nicht insgesamt ausgeschlossen.

## S2.17 Offene technische Parameter und Nachweispflichten

| Punkt | Offener Nachweis / spätere Architekturfestlegung |
|---|---|
| O-S2-01 | Versionierte exakte Manifest-/Export-Schemata, Dateinamensregeln, Parser und erlaubte Unterformate |
| O-S2-02 | Sichere kryptografische Verfahren für Exportverschlüsselung, Schlüsselableitung, Signatur/Integritätsprüfung und Recovery; Plattformfähigkeit |
| O-S2-03 | Retentionswerte für Backups, Löschmarker, temporäre Exporte, Fehlerlogs und Papierkorb samt gesetzlicher Pflichten |
| O-S2-04 | Export-/Importgrößen, PWA-Speichergrenzen, Quoten, Bandbreite und Wiederholungsbudget — gemessen statt erfunden |
| O-S2-05 | Quellen-/Zielmappings und unterstützte konkrete Versionen für weitere Drittapp-Adapter |
| O-S2-06 | Betriebliches Disaster-Recovery-Verfahren, Disaster-Restore-Test, Schlüssel- und Integrationsberechtigungs-Neubewertung |
| O-S2-07 | Konsistenter Snapshot-/Cutover-Mechanismus bei Upgrade/Hostingwechsel unter parallelem Mehrbenutzerbetrieb |
| O-S2-08 | Nachweisbares widerrufs- und löschfestes Verfahren mit **endlicher** Tombstone-/Backupretention |
| O-S2-09 | Starkes Nachweisverfahren für Rückimport nach Verlust des Ursprungsaccounts ohne Übernahme fremder Berechtigungen |
| O-S2-10 | Dokumentierte rechtliche Exportfähigkeit von urheberrechtlich/lizenzrechtlich geschützten Drittmaterialien |
| O-S2-11 | Zentrale EU-Betriebskosten, Recovery-RPO/RTO und Kapazitätsstaffelung ohne verpflichtende Pay-API |
| O-S2-12 | Produktabnahme je V1-Feature und mobilem Browser, inklusive Realtests der oben formulierten Negativfälle |

**Gesamtergebnis:** Alle fachlichen S2-Grundsatzentscheidungen MIG-01 bis MIG-36 sind festgelegt. Die technische Machbarkeit, konkrete Verfahren und produktive Freischaltung bleiben prüfpflichtig. **FE-56 bleibt in S1 offen**, weil die pauschale Delegation zu S2 keine Entscheidung zur zukünftigen Mailbox-Lesefunktion darstellt. Eine Vollfunktionserweiterung von S2 erteilt keine neue externe Schreibberechtigung, keinen Datenzugriff auf fremde Konten und keine Genehmigung zum Merge von PR #1.

## S2.18 Nachverfolgbarkeit, Entscheidungsquellen und Konfliktauflösung

### S2.18.1 Lückenlose Zuordnung der Migrationsregeln

Die Definitionen bleiben ausschließlich in S2.2; jede nachfolgende „Bezug“-Zeile verweist auf genau eine vorhandene MIG-Regel. Die AT-S2-Fälle sind Spezifikationsabnahmefälle und keine ausgeführten Produktprüfungen.

| Bezug | Vertragsabschnitt / Weg | Fachliche Umsetzung in den Bausteinen | Zugehörige Abnahmefälle |
|---|---|---|---|
| Bezug MIG-01 | S2.5 / EXP | UC-49; AF-26; OUT-08 | AT-S2-01, AT-S2-04 |
| Bezug MIG-02 | S2.5 / EXP | UC-49; DLG-49 | AT-S2-02, AT-S2-13 |
| Bezug MIG-03 | S2.5 / EXP | DM-72; DT-86; AF-36 | AT-S2-01, AT-S2-03 |
| Bezug MIG-04 | S2.4/S2.11 / ACA | UC-59; OUT-08 | AT-S2-03, AT-S2-12 |
| Bezug MIG-05 | S2.6 / IMP | UC-64; DLG-65 | AT-S2-05, AT-S2-06 |
| Bezug MIG-06 | S2.6 / IMP | AF-36; DT-88 | AT-S2-06, AT-S2-14, AT-S2-15 |
| Bezug MIG-07 | S2.6 / IMP/BAK | UC-60; UC-64; DM-70 | AT-S2-13, AT-S2-23 |
| Bezug MIG-08 | S2.6 / IMP | DT-88; DLG-65 | AT-S2-11, AT-S2-14 |
| Bezug MIG-09 | S2.6/S2.9 / IMP | DM-74; DT-89 | AT-S2-04, AT-S2-10, AT-S2-17 |
| Bezug MIG-10 | S2.6 / ACA/IMP | AF-36; SEC-12 | AT-S2-07, AT-S2-08 |
| Bezug MIG-11 | S2.6 / ACA/IMP | DM-71; DT-83 | AT-S2-08, AT-S2-09 |
| Bezug MIG-12 | S2.9 / IMP | DM-73; DT-87; BAT-24 | AT-S2-15, AT-S2-16, AT-S2-17 |
| Bezug MIG-13 | S2.9 / EXP/IMP | DM-73; DLG-65; SEC-14 | AT-S2-25, AT-S2-40 |
| Bezug MIG-14 | S2.5/S2.13 / EXP/IMP | DM-59; NFR-09 | AT-S2-09, AT-S2-34, AT-S2-39 |
| Bezug MIG-15 | S2.7 / BAK | DM-69; BAT-23 | AT-S2-22, AT-S2-37 |
| Bezug MIG-16 | S2.6/S2.7 / BAK | UC-60; AF-34; DM-70 | AT-S2-18, AT-S2-23 |
| Bezug MIG-17 | S2.7 / IMP/DEV/BAK | DM-68; INV-31; SEC-15 | AT-S2-21, AT-S2-22, AT-S2-24 |
| Bezug MIG-18 | S2.4/S2.6 / IMP | DM-21; DT-76; DT-88 | AT-S2-11, AT-S2-12, AT-S2-33 |
| Bezug MIG-19 | S2.4/S2.8 / IMP | DM-64; DT-77; SEC-11 | AT-S2-12, AT-S2-29, AT-S2-30 |
| Bezug MIG-20 | S2.4/S2.8 / EXP/IMP | DT-85; SEC-03; SEC-05 | AT-S2-19, AT-S2-20, AT-S2-26 |
| Bezug MIG-21 | S2.5/S2.8 / EXP | DM-64; SEC-09; DLG-65 | AT-S2-18, AT-S2-35 |
| Bezug MIG-22 | S2.8 / IMP/BAK | DM-65; DT-78; SEC-09 | AT-S2-18, AT-S2-35 |
| Bezug MIG-23 | S2.7/S2.10 / BAK | DM-69; SEC-04; BAT-23 | AT-S2-05, AT-S2-22, AT-S2-25, AT-S2-40 |
| Bezug MIG-24 | S2.4/S2.7 / IMP/BAK | AF-28; SEC-04; DM-56 | AT-S2-20, AT-S2-26 |
| Bezug MIG-25 | S2.6/S2.12 / IMP | DM-35; DT-88; UC-64 | AT-S2-27, AT-S2-31 |
| Bezug MIG-26 | S2.12 / IMP | DM-02; DM-33; DM-34 | AT-S2-28, AT-S2-29, AT-S2-30 |
| Bezug MIG-27 | S2.8 / DEV | DM-03; UC-04; UC-05 | AT-S2-19, AT-S2-24, AT-S2-36 |
| Bezug MIG-28 | S2.7/S2.9 / DEV | AF-27; DM-68 | AT-S2-14, AT-S2-24, AT-S2-36 |
| Bezug MIG-29 | S2.10 / UPG | BAT-25; DT-90 | AT-S2-36, AT-S2-37 |
| Bezug MIG-30 | S2.10 / MOV | BAT-25; SEC-08 | AT-S2-38, AT-S2-40 |
| Bezug MIG-31 | S2.11 / ACA | UC-59; AF-33; AF-36 | AT-S2-03, AT-S2-08, AT-S2-12, AT-S2-31, AT-S2-32 |
| Bezug MIG-32 | S2.5 / EXP | UC-62; OUT-08; SEC-16 | AT-S2-01, AT-S2-39 |
| Bezug MIG-33 | S2.8 / DEV | DM-03; NFR-02; NFR-03 | AT-S2-24, AT-S2-34, AT-S2-36 |
| Bezug MIG-34 | S2.5/S2.16 / EXP | S1 NB-05/NB-07/NB-10; OUT-08 | AT-S2-20, AT-S2-31, AT-S2-32 |
| Bezug MIG-35 | S2.5/S2.13 / EXP/IMP | DM-72; OUT-08; DLG-65 | AT-S2-01, AT-S2-03, AT-S2-12, AT-S2-16 |
| Bezug MIG-36 | S2.9/S2.13 / alle Wege | NFR-02; NFR-09; DT-87 | AT-S2-09, AT-S2-18, AT-S2-34, AT-S2-35, AT-S2-39 |

### S2.18.2 Entscheidungsquellen und abgegrenzte Konflikte

Vollständig gelesen wurden `PROMPT_CODEX_SYLLENTRA_S2_MIGRATION_COMPLETE_2026-10-16.md`, `Syllentra_S2_Datenmigration_v0.1_Entwurf_2026-10-16.md` und `Syllentra_AI_Decisions_V1_Apres_S1_2026-10-16.md` aus dem beigefügten Archiv. Die Entscheidung über ihre Ausführung wurde vom Auftraggeber bestätigt. Die 36 MIG-Grundsätze sind fachlicher Sollumfang, der gesamte Spezifikationsstand bleibt zur Prüfung.

| Fundstelle / möglicher Widerspruch | Abgleich ohne eigenmächtige Produktentscheidung |
|---|---|
| Früher ergänzender Entscheidungsregister-Abschnitt G stellt Export/Reimport noch als offene Folgefrage dar; späterer S2-Auftrag und MIG-01/MIG-05 delegieren diesen Umfang ausdrücklich | Der ausgeführte S2-Arbeitsauftrag und sein MIG-Register konkretisieren Export/Reimport. Die alte Fragestellung wird als zeitlich frühere Quelle eingeordnet, nicht als neue notwendige Nutzerfrage ausgegeben. |
| Entwurf MIG-11 nennt ZIP und bedingte weitere Formate; FE-28/S1/UC-59 verlangen ZIP/7z | MIG-11 erhält ZIP und 7z als fachlichen Sollumfang; reale sichere Parserfähigkeit ist vor Freischaltung nachzuweisen. Keine ersatzlose Streichung von 7z. |
| Entwurf MIG-34 spricht von explizitem Fremdzielauftrag, S1 NB-07/NB-10 sind nur lesend | S2 startet keinerlei Fremd-Upload. Eine Nutzerzielwahl allein schafft keine zusätzliche Schreibintegration; externe Kalender einschließlich NB-12 bleiben ebenfalls nur lesend. |
| DEC-V1-10/13 und Entwurf S2.12 nennen automatische Lernheftordnung; FE-05/08 und interne Kalenderplanung verlangen Bestätigung | S2 bewahrt vorhandene kompatible Präferenzen/Planrevisionen, führt die Automatik nicht aus. Manuelle Sitzungen nur nach ausdrücklicher Verschiebebestätigung; interne Kalenderimports und KI-Planänderungen behalten ihren Schutz. L-08 vom 19.10.2026 konkretisiert diese Grenze jetzt in F2/D1/B2: Automatik ausschließlich für nichtterminierte pädagogische Reihenfolge, keine eigenmächtige Kalenderwirkung und kein Fortschrittsverlust durch Undo. Weitere Post-S1-Entscheidungen bleiben separat zu harmonisieren. |
| Entwurf S2.15 bezeichnet DM-33/34 als Lernprofil | DM-02 führt persönliche Präferenzen; DM-33/34 sind pädagogische Erinnerung und Revision. S2 erhält die bestehende Modellbedeutung und die echte Evidenzherkunft. |
| E2EE-Begriff könnte jede Serververarbeitung ausschließen oder als fertiges Verfahren verstanden werden | Gemeint ist der bestehende geräteseitige Zusatzschutz sensibler Dokumente gemäß FE-76/77. Konkretes Schlüsselverfahren bleibt offen. FE-78 erlaubt separat freigegebenen minimalen temporären Klartext bei interner Cloudanalyse; Migration erteilt diese Freigabe nicht. |

### S2.18.3 Verweise und Übergabe

[Projektvision](../PROJECT_VISION.md), „Design principles“, [Anforderungen](../REQUIREMENTS.md), Abschnitte 1/3/4, [Architekturentscheidungen](../ARCHITECTURE_DECISIONS.md), „Current position“, und [Roadmap](../ROADMAP.md), Phasen 2/3/5, begründen Datenhoheit, nachvollziehbare Verarbeitung und noch ausstehende Implementierungsvalidierung. Der S2-Umfang ist im aktuellen [Index](README.md) verzeichnet; tatsächliche Änderungen und Dokumentprüfungen stehen in [E3](E3-pruefnachweis.md). [S3](S3-inbetriebnahme.md) beschreibt jetzt Bootstrap, Betriebsverantwortung, unabhängigen Restore, Rollout und Rückweg als zukünftige Sollverfahren; technische Architektur bleibt separat.

## S2.19 Unabhängige Sicherung nach DEC-49

DEC-49 konkretisiert MIG-15/MIG-16/MIG-17/MIG-22/MIG-23 und UC-60/BAT-23, ohne die 36 bestehenden MIG-Definitionen oder 40 AT-S2-Fälle umzuschreiben. Verschlüsselte Sicherungen liegen in der EU bei einem vom primären Hostinganbieter unabhängigen Anbieter; eine zweite Primäranbieterregion/-konto reicht nicht. DM-69/DT-81 führen den tatsächlichen Unabhängigkeits-, Integritäts- und Restoreprüfstand, DM-70 den Wiederherstellungsvorgang. Sichere Schlüsselverwaltung und getrennte begrenzte Sicherungs-/Restore-/Löschrechte schützen gegen Ausfall, versehentliche Löschung, Korruption und Kompromittierung. Kein Admin erhält dadurch private Klartextschlüssel.

Periodische Restore-Proben weisen Portabilität, Integrität, Kontentrennung und Nichtwiederbelebung unter heutigem Lösch-/Widerrufsstand nach. Retention, Marker, Schlüssel und rechtliche Restpflichten müssen zusammenpassen. O-S2-02/03/06/08/11/12 bleiben technische Nachweispflichten; RPO/RTO, Frequenz, Testintervalle und Retention werden nicht erfunden. Kein Backupanbieter oder kostenpflichtiger Dienst wird festgelegt. DEC-48 priorisiert Oracle nur als Hostingbewertungskandidaten; bei späterer Oracle-Auswahl liegt die unabhängige Sicherung außerhalb von Oracle. [ADR-0004/0005](../ARCHITECTURE_DECISIONS.md) und die [Matrix](ENTSCHEIDUNGSMATRIX.md) trennen bestätigte Ziele von offenen Verfahren; der damalige Entscheidungsanschluss führte keine externe Probe oder S3-Erstellung aus. Der aktuelle fachliche Betriebsentwurf steht inzwischen in [S3](S3-inbetriebnahme.md); keine Betriebsprobe ist damit durchgeführt.
