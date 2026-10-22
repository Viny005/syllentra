# S3 — Inbetriebnahme, Rollout und Betriebsaufnahme

**Projekt:** Syllentra AI\
**Version:** 0.2\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber\
**Ausgangsbasis:** `1885a9c76ed549367097ac15d3960399a8651b88`, bestehender Spezifikationsbranch und [PR #1](https://github.com/Viny005/syllentra/pull/1).

## S3.1 Zweck, Geltung und tatsächlicher Stand

S3 spezifiziert nach Siedersleben Voraussetzungen, Verantwortungen, Ablauf, Freigabe und Nachweise der künftigen Betriebsaufnahme. [P1](P1-ziele-rahmenbedingungen.md) und [P2](P2-architekturueberblick.md) setzen Ziele und Kontext; [S1](S1-nachbarsysteme.md) regelt Nachbarn, [S2](S2-datenmigration.md) die Daten-/Migrationsverträge. [N1](N1-nichtfunktional.md) beschreibt Qualität, [N2](N2-querschnittskonzepte.md) Schutzgrenzen. S3 ordnet diese Anforderungen dem Betriebsablauf zu und wählt keine interne Architektur. Methodischer Bezug: [Herold-Bausteinübersicht](https://github.com/carstenlucke/herold/blob/main/docs/spec/SIEDERSLEBEN.md) und [Leseanleitung](README.md); keine Herold-Technologie wird übernommen.

**Iststand:** Am Ausgangscommit ausschließlich Dokumentation und `.gitignore`; keine Anwendung, Apppipeline, Infrastruktur oder ausgeführten Betriebsverfahren. Alle folgenden Schritte und AT-S3-Fälle sind **zukünftige Sollverfahren**, nicht während Mission 4 ausgeführte Aktionen. Für Produktfreigabe fehlen Architekturentscheidungen, Implementierung, Zielwerte und reale Nachweise. Der Auftrag autorisiert Dokumentation sowie Commit/normalen Push, **keinen Merge, Deployment, Account, Infrastrukturtest oder Ausgabe**.

89 FE, 66 UC, 25 DEC-V1, DEC-48/49 und alle 46 Release-Kontrollen bleiben erhalten. FE-56 bleibt offen, REL-Q10 außerhalb V1. Keine neue Produktfunktion oder neue REL-Kontrolle. Fachlich bestätigte Einzelentscheidungen sind keine Gesamtabnahme dieser Spezifikation.

## S3.2 Verantwortungen, Auftrag und Nachweisakte

| Zuständigkeit | Aufgabe und Entscheidungsgrenze | Erforderlicher Nachweis |
|---|---|---|
| Projektinhaber | Bestätigt Produktumfang, offene fachliche Entscheidungen, zulässige Einschränkungen und konkrete Veröffentlichung. Gesonderte Ressourcen-/Kostenfreigabe; keine Umgehung verbindlicher Schutzgrenzen. | Datierte Entscheidung mit Umfang, Zielumgebung, Fassung, Bedingungen und Gültigkeit |
| Architekturverantwortung | Begründete Auswahl von Komponenten, Umgebungs-/Deployment-, Bootstrap-, Schlüssel- und Recoveryverfahren; führt ADRs mit Alternativen. | Geprüfte Architektur und Kompatibilitäts-/Abhängigkeitsanalyse |
| Betriebsverantwortung | Autorisierte Vorbereitung, Durchführung, Beobachtung, Sicherung, Restore und sichere Unterbrechung. Kein pauschales privates Inhaltsleserecht. | Versionsbezogener Ablauf-/Zustandsbericht und verantwortlicher Kontakt |
| Sicherheitsprüfung | Prüft Identität, Rechte, Isolation, Secrets, Lieferkette und Befunde unabhängig vom bloßen Erfolgsstatus eines Builds. | Negative/positive Tests, Befundbewertung und Nachprüfung |
| Datenschutzverantwortung | Prüft Rollen/Grundlagen, Anbieterbedingungen, Datenflüsse, Rechte, Retention und gegebenenfalls DSFA-/Meldepflichten. | Fachlich geeignete Datenschutzprüfung; keine Rechtskonformität durch EU-Hosting allein |
| Fach-/Qualitätsprüfung | Bewertet Funktion, Pädagogik, Übersetzungen, Accessibility, Kompatibilität und gemessene Qualitätsziele. | Versionierte Test-/Fachberichte, Rubriken und Abdeckung |
| Einziger Super Admin / berechtigte Delegierte | Nur bereits vorgesehene Produktrechte aus FE-70..72 und SEC-05; Betriebstitel erteilen keine Approlle oder privaten Inhaltsrechte. | Verifizierte Rollen-/MFA-/Delegations- und Auditnachweise |

Das sind **Aufgabenverantwortungen**, keine neuen Kontotypen. Vor einer Ausführung sind konkrete Personen und Vertretungs-/Eskalationskontakte zu benennen. Mehrere Aufgaben können in einem kleinen Projekt bei derselben Person liegen; Ausführung, Prüfung und Freigabe trotzdem getrennt dokumentieren. Wo Unabhängigkeit fachlich nötig ist, eine geeignete zusätzliche Prüfung vorsehen; kein kostenpflichtiges Team wird vorausgesetzt. Delegierte erlangen keine exklusiven Super-Admin-Rechte.

**Freigabeakte:** Releasekennung, Commit/Artefakt- und Modell-/Promptfassungen, Schema-/Konfigurationsrevision, Ziel und aktive Funktionen, verantwortliche Personen, bestätigte Architektur, zugeordnete REL-Belege, Testdatenherkunft, Ausgangs-/Zielzustand, Risiken, Abbruch-/Rückweg, menschliche Entscheidung, Ausführungszeitraum, tatsächliche Teilwirkungen und Nachprüfung. Keine Geheimniswerte oder privaten Lerninhalte. Personenbezogene Belege geschützt und endlich aufbewahren; öffentliche Zusammenfassung nur bereinigt. „Geplant“, „nicht durchgeführt“, „blockiert“, „fehlgeschlagen“ und „bestanden mit Beleg“ getrennt führen.

## S3.3 Umgebungen und Übergänge

| Umgebung | Zweck / Daten | Trennungs- und Zugriffsanforderung |
|---|---|---|
| Entwicklung | Entwurf, lokale Umsetzung und frühe Tests; künstliche Konten/Materialien | Keine Produktionscredentials oder produktiven Nebenwirkungen; minimale Entwicklerrechte; lokale Diagnose ohne Privatdaten |
| Test | Reproduzierbare Funktions-, Sicherheits-, Migrations-, Last- und Restoreprüfung | Getrennte Konten, Speicher, Schlüssel, Queues, Suchindizes, Caches und Endpunkte bzw. gleichwertig nachweisbare Isolation; keine Zustellung an echte Nutzer |
| Vorproduktion, sofern begründet | Produktionsnahe Prüfung von Komponenten-/Client-/Migrationszusammenspiel | Risikobegründet vorsehen, wenn übrige Tests die relevanten Grenzen nicht belegen. Kein zwingender zusätzlicher kostenpflichtiger Dauerbetrieb; isolierte zeitweise Nachbildung möglich, wenn gleichwertig nachgewiesen und gesondert autorisiert. |
| Produktion | Nur ausdrücklich freigegebener tatsächlicher Nutzungsumfang | Eigene minimale Rechte/Secrets, freigegebene Artefakte/Konfiguration und aktuelle Gates; Entwickler-/Testidentität erhält keinen automatischen Produktionszugang |

Umgebungskennung in Konfiguration und Nachweisen führen. Gemeinsame Hardware ist keine automatische Zulässigkeit: logische Isolation, Ressourcen-/Zugriffstrennung und fehlende Querwirkungen müssen belegt sein. Keine produktiven Datenbanken, Buckets, Queues oder OAuth-/Mail-/Pushzugänge in Tests wiederverwenden. Test-DNS, Callbackziele und Konnektoren dürfen keine produktiven Kalender, Repositories oder KI-Anbieter aufrufen. Produktionsdaten sind nicht der Standardtestbestand; eine ausnahmsweise erforderliche Kopie braucht vorherige rechtliche Prüfung, Minimierung/Anonymisierung, Schutz, Befristung und konkrete Freigabe.

**Übergang:** geprüfte unveränderliche Artefaktidentität plus validierte zielbezogene Konfiguration übernehmen, nicht Testdaten oder Secrets. Zielparameter separat sicher binden; öffentliche Konfiguration von Geheimnissen trennen. Quelle, Build, Abhängigkeiten/Lizenzen, Schema, Modell/Prompt und Konfigurationsschema versionieren. Unbekannte/inkompatible Parameter, falsche Umgebung oder fehlende Pflichtgeheimnisse sperren den Übergang. Derselbe technische Build darf nur mit nachgewiesener Integrität weitergereicht werden; kein ungeprüfter Neubau nach Testfreigabe.

## S3.4 Infrastrukturvorprüfung ohne Anbieterfestlegung

DEC-48 verlangt **Oracle Cloud Infrastructure zuerst bewerten**, nicht auswählen. Bei fehlender Eignung Alternativen vergleichen; [ADR-0004/0005](../ARCHITECTURE_DECISIONS.md) bleiben maßgeblich. Kein notwendiger privater Dauer-PC, keine verpflichtende kostenpflichtige KI-API. Der seit Mission 7 geltende Vergleichsrahmen bis zu 20 EUR brutto/Monat (ersetzt die frühere 10-EUR-Hypothese) ist **keine Ausgabe- oder Kontoanlagefreigabe**.

| Prüfbereich | Voraussetzung vor tatsächlicher Einrichtung / Freigabe | Beleg und Stopgrund |
|---|---|---|
| EU-Region und Verarbeitung | Hauptdaten, Sicherung, Unterauftragnehmer und externe Flüsse zulässig; konkrete Standorte und Vertragsbedingungen geprüft | Regions-/Datenfluss-/Vertragsnachweis; ungeklärter Standort/Zweck blockiert |
| Kapazität und Speicher | N1.10-Lastprofil, CPU/RAM/Modell-/Netz-/Speicherbedarf einschließlich temporärer Kopien, Index und Backup messen | Reale Angebotslimits, Quoten, Spitzenlast und Reserven; keine unbegrenzte Gratiszusage |
| Netzwerk und HTTPS | Nur notwendige Dienste erreichbar; interne Zugriffe, ausgehende Abrufe und Providerziele begrenzen; Zertifikatsprüfung, sichere Cookies und keine Mischinhalte | Erreichbarkeits-/Transport-/SSRF-/Rechtefälle; ungeschützte Schnittstelle blockiert |
| Domain, DNS und Zertifikate | Eigentum, minimale Verwaltungsrechte, Zielumgebung, Verlängerungs-/Ablaufüberwachung und Wiederherstellungszugang klären | Zuständigkeit, geprüfte Auflösung/Zertifikate und Rückweg; keine Domainbestellung in dieser Mission |
| Zugänge und Secrets | Getrennte Umgebungen, minimale Service-/Betriebsrechte, sichere Ablage/Rotation und unabhängiger Recoveryzugang | Inventar ohne Werte und Entzugs-/Rotationsnachweise; keine Secrets in Repo, Logs oder Client |
| Wartung und Überwachung | Verantwortliche, Kapazitäts-/Ausfallalarme, Updates, Schwachstellen und Wiederanlauf vorbereiten | REL-Q17/18, REL-S18, geprüfter Kontakt-/Eskalationsweg |
| Sicherung und Kosten | DEC-49-Unabhängigkeit einschließlich Schlüssel-/Zugangsverlust belegen; Verbrauch/Transfer/Backup-/Betriebskosten vollständig prüfen | S3.6, genehmigte Budgets und wirksame technische Stopps; Alarm allein verhindert keine Kosten |

Erst separat autorisierte technische Arbeiten dürfen diese Voraussetzungen umsetzen. Freigaben müssen Ziel, Ressourcen, Daten, Laufzeit und gegebenenfalls Kosten abdecken; Empfehlung und vorhandener Cloudzugriff sind keine Autorisierung. Keine automatisch kostenpflichtige Ersatz-KI, Skalierung oder Tarifänderung.

## S3.5 Sicherer Erstbootstrap und administrative Kontinuität

**Unveränderliche Grenzen:** Nach abgeschlossener Erstbesetzung genau ein hauptverantwortlicher Super Admin, getrennt vom gewöhnlichen Benutzerkonto. Keine öffentliche Selbstregistrierung als Super Admin, Standardkennwörter, hart codierten Zugangsdaten oder automatische bekannte Administratoridentität. Produktrechte nur serverseitig; verpflichtende Admin-MFA, sensible Bestätigung und privates Audit. Keine automatische Einsicht in persönliche Dokumente und keine privaten Klartext-Dokumentenschlüssel am Backend/Admin.

### S3.5.1 Voraussetzungen und erste Anmeldung

1. Projektinhaber benennt die berechtigte Person und bestätigt den Zweck der Erstbesetzung. Identitätsnachweis und sicheres Erstzugangsverfahren müssen vorher als Architekturentscheidung geprüft sein; bloßer Besitz einer URL oder einer gewöhnlichen E-Mail-Adresse reicht nicht.
2. In isolierter Testumgebung nachweisen: Anfangszustand ohne Super Admin, ausschließlich autorisierter Übergang zur einmaligen Hauptbesetzung, Konkurrenz-/Replay-/Fehlerfälle ohne zweiten Hauptaccount. Das technische Verfahren bleibt offen; Einmaligkeit, Bindung an berechtigte Person, kurze begründete Gültigkeit und Ausschluss öffentlicher Selbstbeförderung sind Schutzziele, keine Produktwahl.
3. Berechtigter Betriebsauftrag ermöglicht ausschließlich den geprüften Bootstrap. Tatsächliche Umgebungs-/Kontobindung prüfen; kein Geheimniswert in Commit, Log oder Beleg. Teilfehler halten privilegierte Nutzung gesperrt; Wiederaufnahme erzeugt keine weitere Super-Admin-Identität.
4. Erste Anmeldung verifiziert die vorgesehene getrennte Adminidentität und bindet geprüfte MFA sowie den bestätigten Recoveryweg. Privilegierte reguläre Nutzung erst nach vollständiger Verifikation; keine MFA-Umgehung über Initialzustand oder normalen Nutzerlogin.
5. Serverseitig Einzigkeit, exklusive Rechte, Delegationsgrenzen, Sessions und Audit testen. Bootstrapzugang danach nicht erneut nutzbar; unvollständige oder unbekannte Anfangslage vor Wiederholung untersuchen. Eigentümer bestätigt den Abschluss anhand bereinigter Belege.

Vor Produktstart ist dieser Ablauf tatsächlich zu prüfen. O-S3-04/05 bleiben technische Voraussetzungen; S3 enthält keine auszuführenden Bootstrapbefehle, Tokens oder vorgewählte Authentifizierungslösung.

### S3.5.2 Verlust, Abwesenheit und Kompromittierung

| Ereignis | Zukünftiger sicherer Ablauf | Freigabegrenze / Beleg |
|---|---|---|
| Gewöhnliche Adminanmeldung / Delegation | Aktuelle Identität, MFA, Rolle und konkrete Operation prüfen; Einladung/Entzug ausschließlich durch den Super Admin; Delegierte eng begrenzen | SEC-04/05/06; Rollen-/Session-/Auditfälle; keine Selbstbeförderung oder weitere Adminverwaltung durch Delegierte |
| Session-/Geräteverlust | Betroffene administrative Sessions/Geräte widerrufen; Folgewirkung und Jobs erneut prüfen; lokale Entsperrung ersetzt keine Serverrechte | SEC-02/03/22; negative Folgeaufrufe, keine behauptete Fernlöschung |
| Verlust der MFA-Mittel / Kontorecovery | Vorab geprüftes starkes Wiederherstellungsverfahren mit Identitäts-/Eigentumsnachweis; alte Faktoren/Sessions nach Bedarf entziehen, neue sicher binden | Kein ad hoc E-Mail-/SMS-/Support-Bypass; keine Dokumentenschlüsselwiederherstellung durch bloßen Kontoerfolg |
| Kompromittierung des Super Admin | Privilegierte Wirkungen eindämmen, Sessions/Credentials entziehen, betroffene Änderungen/Delegationen untersuchen; sichere erneute Bindung nur nach geprüftem Recoveryverfahren | Kein zweiter paralleler Super Admin und kein rückgespieltes altes Vertrauen; S3.12 und erneute Sicherheitsfreigabe |
| Vorübergehende Abwesenheit | Vorher zulässige Delegation deckt nur nicht exklusive Aufgaben; geplante privilegierte Schritte warten, wenn kein berechtigter Entscheider verfügbar ist | Keine automatische Vollmacht, Notfallselbsternennung oder Weitergabe von Login/MFA; geplante Verfügbarkeit dokumentieren |
| Dauerhafter Verlust / unbekannte Hauptinhaberschaft | Betroffene privilegierte Änderungen gesperrt halten; Sicherheits-/Eigentumsnachweise untersuchen; autorisierte Nachfolge-/Recoverylösung erst nach eigener geprüfter Entscheidung | O-S3-05; keine neue Nachfolgerrolle beschlossen, kein öffentliches Bootstrap-Reset, keine Accountneuanlage aus altem Backup |

Eine vorab genehmigte eng begrenzte technische Eindämmungsberechtigung kann den Betrieb sichern, ist aber kein Recht zur Übernahme exklusiver Appmacht. Fehlt ein zulässiger Notfallweg, sicher pausieren und eskalieren statt die Schutzgrenze aufzuheben.

## S3.6 Unabhängige Sicherung und nachgewiesener Restore

[DEC-49](../ARCHITECTURE_DECISIONS.md#adr-0005--anbieterunabhängige-verschlüsselte-sicherung-dec-49) verlangt verschlüsselte EU-Sicherung **bei einem vom Primäranbieter unabhängigen Anbieter**. Zweites Konto/andere Region desselben Anbieters genügt nicht. Sicherung, Schlüsselerreichbarkeit, Zugriff und heutiger Lösch-/Widerrufskontrollstand müssen bei Verlust des Hauptzugangs nutzbar bleiben. Keine konkrete Backupplattform oder Kryptographie wird gewählt.

### S3.6.1 Zukünftiger Sicherungslauf

1. Autorisierten Sicherungsumfang, konsistente Stichtagsbasis und Abhängigkeiten bestimmen: Fachbestand, Originale soweit erforderlich/zulässig, Quellschutz, Konfiguration, Schema-/Software-/Modellreferenzen und zur Rekonstruktion nötige Betriebsmetadaten. Temporäre abgelaufene Transkripte/Klartexte und unnötige Diagnosen nicht zum Schattenarchiv machen.
2. Konsistenz-/Integritätsmerkmale und verschlüsseltes Manifest mit Fassung, Umfang, Zeitpunkt, Schutzklasse und Prüfergebnis erzeugen. Unvollständige Sicherung als Teilstand kennzeichnen. Schlüsselverwaltung von Datenablage und Erstell-/Lese-/Restore-/Löschrechten angemessen trennen.
3. Über geschützten autorisierten Weg zum unabhängigen EU-Ziel übertragen; Integrität und Lesbarkeit prüfen. Ein erfolgreicher Upload allein beweist keine Entschlüssel-/Restorefähigkeit. Sicherungsausfall alarmieren und bis zur Klärung als Befund führen.
4. Notwendige geschützte Service-/Konfigurations-Recoverygegenstände getrennt vom persönlichen Nutzerexport verwalten; keine Schlüsselwerte im Manifest/öffentlichen Beleg. Persönliche private Dokumentenschlüssel werden dadurch nicht dem Betrieb bekannt. Aktive Sessions, Geräte-/Support-/Anbieter-/Adminrechte niemals ungeprüft reaktivieren.
5. Endliche genehmigte Retention, Löschung, Zugriffsrevision und periodische tatsächliche Restore-Proben nachweisen. Aktuelle Lösch-/Widerrufsinformation gegen Zurückrollen alter Sicherungen absichern. Aufbewahrungs-/Marker-/Altclientfristen gemeinsam abstimmen; keine unbegrenzte Markerhaltung oder sofortige physische Löschung sämtlicher Backups behaupten.

### S3.6.2 Selektive und vollständige Wiederherstellung

| Phase | Erforderliches zukünftiges Vorgehen | Erfolg / sichere Sperre |
|---|---|---|
| Auftrag und Auswahl | Berechtigtes Ziel, Zweck, Sicherung/Fassung, Teil-/Vollumfang und menschlichen Restoreauftrag festhalten; UC-60-Selfservice von betrieblichem Disasterfall trennen | Kein privates Inhaltsrecht aus Betriebsrolle; kein fremder Restore in Konto A |
| Unabhängige Quelle | Zugriff bei Verlust des Hauptanbieters und erforderliche zulässige Schlüssel prüfen; Integrität/Unversehrtheit der Sicherung bewerten | Fehlender Schlüssel, Korruption oder unklarer Quellzustand → kein aktiver Restore |
| Isolierter Aufbau | Geprüfte kompatible Software, Konfiguration und Schema herstellen; externe Zustellungen/Jobs zunächst gesperrt; Daten in abgegrenztem Ziel prüfen | Kein Test greift auf Privatkonten oder produktive externe Kalender zu |
| Heutige Kontrolllage | Aktuelle Kontozustände, Eigentum, Löschungen, Entzüge, Rechte und Schlüsselstatus unabhängig vom alten Sicherungsstand einbeziehen | Fehlt belastbarer aktueller Kontrollstand, kein produktives Freischalten |
| Daten-/Beziehungsprüfung | Mengen, Inhalte/Stichproben, Referenzen, Quellschutz und A/B-Isolation prüfen; Index/Cache nur aus noch berechtigtem Bestand aufbauen | Keine Wiederbelebung gelöschter Originale/Derivate, verlorener temporärer Transkripte oder alter Rechte |
| Selektiver Umfang | Referenzabhängigkeiten, jüngere Fortschritte, manuelle Termine und Konflikte nach S2 erhalten; notwendige Vorschau/Bestätigung | Kein stilles Zurücksetzen jüngerer Lernbelege und kein Löschkaskadenfehler |
| Wiederfreigabe | Bestätigte RPO/RTO messen, relevante REL-/AT-S2-/AT-S3-Fälle bestehen; menschliche Freigabe; Integrationen/Automatik nur nach heutigen separaten Rechten | Alte OAuth-, Support-, Geräte-, MFA-/Session- oder Adminzustände nicht blind aktivieren |
| Abschluss | Tatsächliche wiederhergestellte/fehlende Daten, Einschränkungen, Zeiten, Ursache und Restarbeiten dokumentieren; Zwischenkopien geschützt bereinigen | Teilwiederherstellung nicht als vollständig ausgeben; zulässige Reste und Fristen transparent |

**RPO/RTO ermitteln:** Verlustfolgen je Daten-/Vorgangsklasse und akzeptablen Stillstand mit Projektinhaber analysieren. Abhängigkeiten einschließlich unabhängiger Schlüssel, Kontrollstand, DNS, Modelle und erreichbarer Personen erfassen. Mit realistisch großen synthetischen Beständen vollständigen Recoveryweg messen; Zielvorschlag, Kosten-/Kapazitätsverträglichkeit und Restrisiko menschlich bestätigen **vor** Abnahme. Kein fester Stunden-/Tageswert. Testintervall und Retention ebenso risikobasiert bestätigen. Nicht erreichte Ziele bleiben Befund, kein nachträgliches Absenken ohne neue dokumentierte Entscheidung.

Bei Daten-/Schlüsselkompromittierung Sicherungszeitpunkte und verwendete Schlüssel als potenziell betroffen prüfen; sauberen Stand und aktuelle Kontrolllage belegen. Verschlüsselung macht bereits offengelegte Daten nicht wieder geheim. Rotation ohne Wiederherstellbarkeitsprüfung kann alte Sicherungen unlesbar machen. Ohne sauberen entschlüsselbaren Stand bleibt der betreffende Umfang gesperrt; ehrliche Verlust-/Incidentmeldung statt fingierter Recovery.

## S3.7 Kontrollierte erste Veröffentlichung

Jeder Schritt gilt **erst in einer gesondert autorisierten zukünftigen Ausführung**. Ein erfolgreiches Dokumentreview, Commit, Push oder Test erteilt keine Veröffentlichungsfreigabe. Vorwärts nur mit erfüllten Voraussetzungen, sonst sicher pausieren und S3.13 anwenden.

| Schritt | Voraussetzung / Aktion | Zuständig und benötigter Abschlussbeleg |
|---|---|---|
| 1 | Geplanten V1-Umfang, Nutzer-/Testgruppe, aktive Funktionen, Einschränkungen und Zielumgebung abgrenzen | Projektinhaber + Fachprüfung; versionierte Umfangsentscheidung |
| 2 | Für diesen Umfang genehmigte Architektur, technische Verfahren und offene Entscheidungen prüfen | Architektur + Sicherheitsprüfung; passende ADRs und Abhängigkeitsprüfung |
| 3 | Code, Buildherkunft, Komponenten/Modelle, Lizenzen und Schwachstellen reviewen | Entwicklung/Architektur + Sicherheitsprüfung; REL-S18/A13 und geprüfte Artefaktidentität |
| 4 | Tatsächliche Testberichte, Abdeckung, Umgebung und Defekte prüfen | Fach-/Qualitätsprüfung; keine leeren, übersprungenen oder rein dokumentarischen Tests als Produkterfolg |
| 5 | Anwendbare Sicherheits-/Negativtests bestehen | Sicherheitsprüfung; aktuelle REL-Belege insbesondere Isolation, Authentisierung, Agenten und Secrets |
| 6 | Datenflüsse, Zwecke, Anbieterbedingungen, Retention und Betroffenenrechte prüfen | Datenschutzverantwortung; zulässiger dokumentierter Verarbeitungsumfang |
| 7 | Konten, Rollen, genau einen Super Admin, MFA, Recovery und Entzug prüfen | Sicherheit + Betrieb; S3.5-Nachweise und keine Standard-Privatinhaltsrechte |
| 8 | Flags, Rollen, Testgruppen und direkte API-/Jobaufrufe gegen unfertige Funktionen prüfen | Sicherheit + Fachprüfung; vollständige serverseitige Sperre |
| 9 | Migration, Client-/Schema-/Datenkompatibilität und sichere Unterbrechung im Trockenlauf validieren | Architektur + Betrieb + Fachprüfung; S2-UPG/MOV-Nachweise |
| 10 | Unabhängige Sicherung und tatsächlichen Restore samt heutigem Kontrollstand belegen | Betrieb + Sicherheit/Datenschutz; REL-S20/Q20, bestätigte RPO/RTO |
| 11 | Funktionale Endabläufe des aktivierten Umfangs und relevante UC-/DEC-Sollfälle prüfen | Fachprüfung; Datenwirkungen/Fehlerpfade, 28 AT-L soweit betroffen |
| 12 | Unterstützte Geräte/PWA, DE/FR/EN, Zugänglichkeit und bestätigtes WCAG-Ziel prüfen | Qualitätsprüfung; REL-A16/Q04/Q06 mit manuellen Nachweisen |
| 13 | Last, Kapazität, Antwortzeiten, Quoten und Degradation gegen bestätigte Ziele prüfen | Betrieb + Qualitätsprüfung; N1.10 und passende REL-Q-Berichte |
| 14 | Zielkonfiguration, Secretschutz, DNS/HTTPS, Monitoring, Empfänger, Backup und Rückweg validieren | Betrieb + Sicherheit; Konfigurations-/Umgebungsrevision und Änderungsdifferenz |
| 15 | Gesamte Freigabeakte und Restbefunde entscheiden; konkrete menschliche Veröffentlichungsgenehmigung einholen | Projektinhaber; Fassung, Ziel, Umfang, Zeitraum/Bedingungen und ggf. getrennte Kostenfreigabe. Fehlt sie, kein Deployment. |
| 16 | Ausschließlich genehmigtes Artefakt kontrolliert ausrollen; Schreiber/Jobs/Migration nach Plan koordinieren | Autorisierter Betrieb; Beginn, Teilwirkungen, Zustand und Abbruchgründe protokollieren |
| 17 | Nach Deployment Erreichbarkeit, Anmeldung/MFA, synthetische A/B-Isolation, Flags, Datenintegrität, Queue, Modell-/Providerstatus und Alarme prüfen | Betrieb + zuständige Fach-/Sicherheitsprüfer; tatsächlicher Smoke-/Gesundheitsbericht ohne private Inhalte |
| 18 | Beobachtungsfenster bewerten: akzeptieren, begrenzen, stoppen oder geprüften Rückweg ausführen | Betrieb + Projektinhaber mit Sicherheitsprüfung; S3.9/10/13, endgültiger Iststand und nächste Kontrollfälligkeit |

Die Genehmigung aus Schritt 15 gilt nur für die geprüfte Fassung und Bedingungen. Abweichender Build, Rechte-/Datenflussänderung oder neuer kritischer Befund macht erneute Prüfung/Freigabe nötig. Für Stopp/Isolation ist eine zuvor klar begrenzte Eingriffsberechtigung festzulegen; ein Incident ist keine pauschale Befugnis für neue Provider, Ausgaben oder private Datenweitergabe.

## S3.8 Einbindung aller 46 Release-Kontrollen

**Verweisregel je Zeile:** Der verlinkte stabile Profilanker in der [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md) liefert verbindlich Risiko, Anforderungen, Funktionen, **Anwendbarkeit, Prüfmethode, erwartetes Ergebnis und erforderliche Belege**. Ein Erfolg liegt ausschließlich vor, wenn das dortige Soll unter den vorab bestätigten Parametern mit tatsächlichen Belegen erreicht ist. Die folgende Tabelle ergänzt je Kontrolle Ausführungszeitpunkt, Ergebnisprüfer, Sperrwirkung und Neuprüfung, ohne den Katalog zu duplizieren.

Für jede anwendbare Kontrolle sind auch die relevanten Nachprüfungen nach Deployment aus S3.7 Schritt 17 nötig. „Blockiert bei Anwendbarkeit“ bedeutet: fehlender/negativer Beleg sperrt den abhängigen Umfang; bei gemeinsamem Grundschutz den ganzen Produktivstart. Dies gilt auch für als „Hoch“ klassifizierte Kontrollen. Ein Nichtanwendbarkeitsentscheid muss begründet und durch zuständige Prüfung plus Projektinhaber bestätigt sein; bloß ungeprüft ist nicht nichtanwendbar. Alle Kontrollpunkte sind aktuell **nicht implementiert / nicht produktgetestet**.

| Kontrolle: Soll, Beleg und Geltung | Pflichtzeitpunkt | Wer prüft das Ergebnis? | Sperrwirkung | Neuprüfung nach Änderung |
|---|---|---|---|---|
| [REL-S01](../quality/RELEASE_KONTROLLMATRIX.md#rel-s01) | Vor erster Veröffentlichung und Secret-/Konfigurationsänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Relevante Funktions-/Architekturänderung; passende Regression vor Freigabe |
| [REL-S02](../quality/RELEASE_KONTROLLMATRIX.md#rel-s02) | Vor Veröffentlichung, bei Änderungen und nach Secretvorfall | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Relevante Funktions-/Architekturänderung; passende Regression vor Freigabe |
| [REL-S03](../quality/RELEASE_KONTROLLMATRIX.md#rel-s03) | Vor Zugangsfunktion; nach Authänderung und periodisch | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | nach Authänderung und periodisch |
| [REL-S04](../quality/RELEASE_KONTROLLMATRIX.md#rel-s04) | Vor jeder datenführenden Veröffentlichung; relevante Regression | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | relevante Regression |
| [REL-S05](../quality/RELEASE_KONTROLLMATRIX.md#rel-s05) | Vor Identitätsfunktion und Verfahren-/Bibliothekswechsel | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Relevante Funktions-/Architekturänderung; passende Regression vor Freigabe |
| [REL-S06](../quality/RELEASE_KONTROLLMATRIX.md#rel-s06) | Vor jeweiliger Aktivierung; jede Rechte-/Agenten-/Flagänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | jede Rechte-/Agenten-/Flagänderung |
| [REL-S07](../quality/RELEASE_KONTROLLMATRIX.md#rel-s07) | Vor Veröffentlichung und Build-/Konfigurationsänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Relevante Funktions-/Architekturänderung; passende Regression vor Freigabe |
| [REL-S08](../quality/RELEASE_KONTROLLMATRIX.md#rel-s08) | Vor Netzfreigabe; nach Netz-/Authänderungen und periodisch | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | nach Netz-/Authänderungen und periodisch |
| [REL-S09](../quality/RELEASE_KONTROLLMATRIX.md#rel-s09) | Vor Anmeldung/Sync; nach Sitzungsänderung und periodisch | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | nach Sitzungsänderung und periodisch |
| [REL-S10](../quality/RELEASE_KONTROLLMATRIX.md#rel-s10) | Vor betroffenen Eingabefunktionen; Parser-/Rendereränderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Parser-/Rendereränderung |
| [REL-S11](../quality/RELEASE_KONTROLLMATRIX.md#rel-s11) | Vor Import/Medienfunktion; nach Format-/Limitänderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | nach Format-/Limitänderung |
| [REL-S12](../quality/RELEASE_KONTROLLMATRIX.md#rel-s12) | Vor Import/Vorschau; Parser-/Formatwechsel | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Parser-/Formatwechsel |
| [REL-S13](../quality/RELEASE_KONTROLLMATRIX.md#rel-s13) | Vor betroffener API; Origin-/Sessionänderung | Sicherheitsprüfung | Bei entsprechender Technik blockierend; sonst begründet nicht anwendbar | Origin-/Sessionänderung |
| [REL-S14](../quality/RELEASE_KONTROLLMATRIX.md#rel-s14) | Vor Veröffentlichung; Fehlerpfadänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Fehlerpfadänderung |
| [REL-S15](../quality/RELEASE_KONTROLLMATRIX.md#rel-s15) | Vor Veröffentlichung; Log-/Provider-/Jobänderung und periodisch | Sicherheits- + Datenschutzprüfung | Blockiert bei Anwendbarkeit | Log-/Provider-/Jobänderung und periodisch |
| [REL-S16](../quality/RELEASE_KONTROLLMATRIX.md#rel-s16) | Vor Auth-/UI-Freigabe; Text-/Authänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Text-/Authänderung |
| [REL-S17](../quality/RELEASE_KONTROLLMATRIX.md#rel-s17) | Vor Webhookaktivierung; Schlüssel-/Handleränderung | Sicherheitsprüfung | Bei entsprechender Technik blockierend; sonst begründet nicht anwendbar | Schlüssel-/Handleränderung |
| [REL-S18](../quality/RELEASE_KONTROLLMATRIX.md#rel-s18) | Vor Auswahl/Release; bei Updates und periodisch | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | bei Updates und periodisch |
| [REL-S19](../quality/RELEASE_KONTROLLMATRIX.md#rel-s19) | Vor Registrierung; Authregression | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Authregression |
| [REL-S20](../quality/RELEASE_KONTROLLMATRIX.md#rel-s20) | Vor erster Produktion; nach Backup-/Schlüsseländerung und periodisch | Betrieb + Sicherheits-/Datenschutzprüfung | Blockiert bei Anwendbarkeit | nach Backup-/Schlüsseländerung und periodisch |
| [REL-Q01](../quality/RELEASE_KONTROLLMATRIX.md#rel-q01) | Vor jeweiliger Aktivierung; Last-/Limit-/Modelländerung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Last-/Limit-/Modelländerung |
| [REL-Q02](../quality/RELEASE_KONTROLLMATRIX.md#rel-q02) | Vor betreffendem Dienst; Budget-/Retryänderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Budget-/Retryänderung |
| [REL-Q03](../quality/RELEASE_KONTROLLMATRIX.md#rel-q03) | Vor kostenrelevantem Weg; Preis-/Modell-/Providerwechsel | Projektinhaber + Betrieb | Blockiert bei Anwendbarkeit | Preis-/Modell-/Providerwechsel |
| [REL-Q04](../quality/RELEASE_KONTROLLMATRIX.md#rel-q04) | Vor UI-Freigabe; Text-/Lokalisierungsänderung | Fach-/Qualitätsprüfung; Datenschutz bei Personenbezug | Blockiert bei Anwendbarkeit | Text-/Lokalisierungsänderung |
| [REL-Q05](../quality/RELEASE_KONTROLLMATRIX.md#rel-q05) | Vor Jobfunktion; Zustands-/Queueänderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Zustands-/Queueänderung |
| [REL-Q06](../quality/RELEASE_KONTROLLMATRIX.md#rel-q06) | Vor Client-/Funktionsfreigabe; Browser-/PWA-/Flagänderung | Fach-/Qualitätsprüfung; Datenschutz bei Personenbezug | Blockiert bei Anwendbarkeit | Browser-/PWA-/Flagänderung |
| [REL-Q07](../quality/RELEASE_KONTROLLMATRIX.md#rel-q07) | Vor Wiederholungsfunktion; Job-/Rechteänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Job-/Rechteänderung |
| [REL-Q08](../quality/RELEASE_KONTROLLMATRIX.md#rel-q08) | Vor Abhängigkeit; Timeout-/Provideränderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Timeout-/Provideränderung |
| [REL-Q09](../quality/RELEASE_KONTROLLMATRIX.md#rel-q09) | Vor schreibender Funktion; Transaktions-/Deduplizierungsänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Transaktions-/Deduplizierungsänderung |
| [REL-Q10](../quality/RELEASE_KONTROLLMATRIX.md#rel-q10) | Vor späterer Zahlungsaktivierung; nicht als V1-Produkttest ausgeben | Erst nach neuer Fachfreigabe: Fach-/Sicherheitsprüfung | Nicht V1; spätere Aktivierung ohne neue Entscheidung und Nachweis gesperrt | nicht als V1-Produkttest ausgeben |
| [REL-Q11](../quality/RELEASE_KONTROLLMATRIX.md#rel-q11) | Vor Datenverarbeitung; Datenfluss-/Provider-/Retentionänderung | Sicherheits- + Datenschutzprüfung | Blockiert bei Anwendbarkeit | Datenfluss-/Provider-/Retentionänderung |
| [REL-Q12](../quality/RELEASE_KONTROLLMATRIX.md#rel-q12) | Vor Suche/Listennutzung; Schema-/Indexänderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Schema-/Indexänderung |
| [REL-Q13](../quality/RELEASE_KONTROLLMATRIX.md#rel-q13) | Vor Listenfreigabe; Pagination-/Sortieränderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Pagination-/Sortieränderung |
| [REL-Q14](../quality/RELEASE_KONTROLLMATRIX.md#rel-q14) | Vor betroffener Übertragung; Format-/Transportänderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Format-/Transportänderung |
| [REL-Q15](../quality/RELEASE_KONTROLLMATRIX.md#rel-q15) | Vor Import; Parser-/Kapazitäts-/Limitänderung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Parser-/Kapazitäts-/Limitänderung |
| [REL-Q16](../quality/RELEASE_KONTROLLMATRIX.md#rel-q16) | Vor Cache/Offline; Speicher-/Sync-/Retentionänderung | Sicherheits- + Datenschutzprüfung | Blockiert bei Anwendbarkeit | Speicher-/Sync-/Retentionänderung |
| [REL-Q17](../quality/RELEASE_KONTROLLMATRIX.md#rel-q17) | Vor erster Produktion; Monitoringänderung und periodische Übung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | Monitoringänderung und periodische Übung |
| [REL-Q18](../quality/RELEASE_KONTROLLMATRIX.md#rel-q18) | Vor Produktion; Loggingänderung und periodisch | Sicherheits- + Datenschutzprüfung | Blockiert bei Anwendbarkeit | Loggingänderung und periodisch |
| [REL-Q19](../quality/RELEASE_KONTROLLMATRIX.md#rel-q19) | Vor erster Freigabe; relevante Parallelitäts-/Daten-/Modelländerung | Betrieb + Qualitätsprüfung; Sicherheit bei Schutzwirkung | Blockiert bei Anwendbarkeit | relevante Parallelitäts-/Daten-/Modelländerung |
| [REL-Q20](../quality/RELEASE_KONTROLLMATRIX.md#rel-q20) | Vor Produktion; Backup-/Schlüssel-/Formatänderung und periodisch | Betrieb + Sicherheits-/Datenschutzprüfung | Blockiert bei Anwendbarkeit | Backup-/Schlüssel-/Formatänderung und periodisch |
| [REL-A01](../quality/RELEASE_KONTROLLMATRIX.md#rel-a01) | Vor KI-Aktivierung; Modell-/Prompt-/Tool-/Retrievaländerung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Modell-/Prompt-/Tool-/Retrievaländerung |
| [REL-A05](../quality/RELEASE_KONTROLLMATRIX.md#rel-a05) | Vor Ausgabe; Modell-/Prompt-/Retrieval-/Quelllogikänderung | Fach-/Qualitätsprüfung; Datenschutz bei Personenbezug | Blockiert bei Anwendbarkeit | Modell-/Prompt-/Retrieval-/Quelllogikänderung |
| [REL-A07](../quality/RELEASE_KONTROLLMATRIX.md#rel-a07) | Vor Import/Abruf; Parser-/URL-/Netzänderung | Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Parser-/URL-/Netzänderung |
| [REL-A13](../quality/RELEASE_KONTROLLMATRIX.md#rel-a13) | Vor Pipeline-/Produktveröffentlichung; Pipeline-/Build-/Berechtigungsänderung | Architektur + Sicherheitsprüfung | Blockiert bei Anwendbarkeit | Pipeline-/Build-/Berechtigungsänderung |
| [REL-A16](../quality/RELEASE_KONTROLLMATRIX.md#rel-a16) | Vor UI-Freigabe; Zielentscheidung vorher, UI-/Authänderung und periodische Stichprobe | Fach-/Qualitätsprüfung; Datenschutz bei Personenbezug | Grundzugänglichkeit verbindlich; AA-Ziel vorher bestätigen, kein Konformitätsversprechen | Zielentscheidung vorher, UI-/Authänderung und periodische Stichprobe |
| [REL-A18](../quality/RELEASE_KONTROLLMATRIX.md#rel-a18) | Vor Bewertungs-/Adaptionsfunktion; Modell-/Prompt-/Bewertungslogikänderung | Fach-/Qualitätsprüfung; Datenschutz bei Personenbezug | Blockiert bei Anwendbarkeit | Modell-/Prompt-/Bewertungslogikänderung |

Es sind genau REL-S01..S20, REL-Q01..Q20 und REL-A01/05/07/13/16/18 eingebunden. Nicht vergebene REL-A-Kandidaten bleiben ausschließlich Herkunftsverweise im Register. Keine 47. Kontrolle entsteht. Ausgewählte Ergebnisprüfung ersetzt nicht die abschließende menschliche Veröffentlichungsentscheidung.

## S3.9 Progressiver Rollout und Funktionsaktivierung

Ausrollen einer geprüften Softwarefassung und Freischalten ihrer Funktionen sind getrennte Entscheidungen. Zunächst eigene isolierte Testkonten, dann nur bestätigte Tester/Umfänge; Erweiterung erst nach passender Abnahme und dokumentierter Entscheidung. Größe/Dauer der Stufen und Beobachtungsfenster aus Risiko, Last und realer Plattformfähigkeit bestimmen, nicht erfinden. Wo die Architektur keinen sicheren Parallel-/Stufenbetrieb ermöglicht, einen genehmigten kompatiblen Wartungs-/Umschaltplan nutzen statt eine nicht vorhandene Canarytechnik zu behaupten.

Aktivierung prüft globalen Funktionsstatus, Rolle, Konto, Objekt, Scope und aktuelle Zustimmung **serverseitig** je Operation, auch für Jobs, Tools, Altclients und Retry. Feature-Flags sind Teil dieser Prüfung, kein Ersatz dafür. Bereits gespeicherte Daten bei Deaktivierung bewahren; neue unsichere Wirkungen stoppen, sichere Lesesicht nur soweit zulässig. Nutzerankündigung erst bei tatsächlich berechtigter Verfügbarkeit; abgesagte Planung erzeugt keine falsche Ankündigung (FE-66..69).

Jede Stufe dokumentiert Fassung, Konfiguration, freigegebene Gruppe, Belege, Beobachtung, Stoppschwellen, Verantwortliche und Rückweg. Testkonten dürfen keine Echtdaten anderer Nutzer sehen. Neue Gruppen erhalten keine stillen Provider-/Kalender-/Kostenrechte. Bei Fehlern Erweiterung stoppen, betroffene Funktion begrenzen und heutige Rechte/Löschungen auch bei Rücknahme erhalten.

## S3.10 Schemawechsel, Unterbrechung und Rückweg

| Schritt / Entscheidung | Zukünftige Anforderung und Nachweis |
|---|---|
| Änderungsanalyse | Daten-/Schema-/Konfigurations-/Modell-/Clientfassungen und Wirkungen inventarisieren; S2-UPG/MOV, Eigentums-/Schutz-/Löschinvarianten prüfen. Vorwärts-/Rückwärtskompatibilität einschließlich alter PWA-Serviceworker/Clients nachweisen. |
| Trockenlauf und Sicherung | Repräsentativer isolierter Migrationslauf und unabhängiger Restore getestet; neue Daten-/Konfigurationsfassung validiert; keine destruktive Änderung ohne nachgewiesenen sicheren Weg. |
| Kontrollierter Stopp | Zulässige Wartungs-/Lesesicht, Ende neuer Aufträge, Umgang mit laufenden Jobs und noch bestätigungsbedürftigen Aktionen vorher festlegen. Grenzen atomarer Teilwirkungen und unbekannte externe Erfolge protokollieren. |
| Schreibzuständigkeit | Während Cutover eindeutig bestimmen, welcher Stand schreiben darf; kein doppelter aktiver Betrieb mit widersprechenden Queues, Locks oder Quoten. DNS-Umschaltung allein belegt keine Exklusivität. |
| Wiederaufnahme | Protokollierte Teilwirkungen und Deduplizierung berücksichtigen; aktuelle Rechte, Quoten, Löschungen und Kostenfreigaben je Versuch; keine doppelten Importe, Hinweise, Lernbelege oder externen Wirkungen. |
| Konfigurationsrücknahme | Vorherige Fassung nur gegen heutiges Schema und Sicherheitslage validiert übernehmen. Keine wieder aktivierten unzulässigen Flags, Tokens, Supportgrants, Konten oder Datenweitergaben. |
| Software-/Datenrückweg | Geprüfte kompatible Altsoftware, selektive Wiederherstellung oder nachgewiesene Vorwärtskorrektur wählen; kein pauschales Zurückspielen einer alten Gesamtdatenbank. Jüngere Belege, manuelle Termine und bestätigte Löschungen bewahren. |
| Wiederfreigabe | S2-Nachprüfung, A/B-Negativfälle, Daten-/Referenz-/Cache-/Indexprüfung und relevante REL-Regressionen bestehen; zuständige menschliche Entscheidung und tatsächlichen Endstand dokumentieren. |

**Gefährlicher oder unmöglicher Rollback:** irreversible Transformation/Löschung, fehlende kompatible Altsoftware, nicht lesbares Backup, kompromittierter Ausgangsstand/Schlüssel, unbekannter heutiger Kontrollstand, inzwischen gültige Nutzerlöschungen, neuere Lernergebnisse oder bereits externe Wirkung. In diesen Fällen keinen unsicheren Rücksprung erzwingen: betroffenen Umfang sperren, Integrität sichern und geprüfte Vorwärtskorrektur/selektiven Recoveryweg entscheiden. Extern versendete Daten werden durch Rollback nicht zurückgeholt. Keine Produktionsverfügbarkeit durch Umgehen von Sicherheitsgates erzwingen.

## S3.11 Pflichten nach Veröffentlichung

Die folgende Tabelle beschreibt künftige Pflichten, **keinen bestehenden Betrieb**. Für jede Pflicht konkrete Person, Vertretung, genehmigte Intervalle und Alarm-/Eskalationsweg vor Produktstart festlegen. Ereignisbezogene Prüfung unabhängig vom Rhythmus. Überfällige kritische Nachweise werden Befund; nicht automatisch „weiter bestanden“.

| Bereich / Auslöser | Verantwortung und Handlung | Beleg / Eskalation |
|---|---|---|
| Erreichbarkeit, Appgesundheit, kritische Pfade | Betrieb prüft Anmeldung, Kernabläufe, Queue/Modell-/Integrationszustand und abgestimmte SLO; synthetische Checks ohne private Inhalte | REL-Q17/18; bei Grenzverletzung Alarm an Betrieb, bei Schutzwirkung Sicherheit/Projektinhaber |
| Wiederkehrende Fehler / unbekannte Wirkung | Betrieb korreliert minimale Ereignisse, unterscheidet transient/permanent, begrenzt Retry und untersucht Ursache | REL-Q07/08/18; wiederholte oder unklare Wirkung → betroffene Jobs pausieren, Fach-/Sicherheitsprüfung |
| Speicher, Queue, Inference und Last | Betrieb beobachtet genehmigte Quoten, Reserven und Fairness; Warngrenzen prüfen; nur neue betroffene Aufnahme stoppen | REL-Q01/02/15/19; keine Sperre von Lesen/Export/Löschen bestehender Daten wegen voller Quote |
| Kosten, Gratislimits und Angebotsänderung | Betrieb/Projektinhaber prüfen Verbrauch, Transfer, Restkontingent und Preiskonditionen; unzulässige Kostenpfade technisch stoppen | REL-Q03; keine automatische bezahlte Skalierung/Ersatz-API; Freigabe vor zusätzlicher Ausgabe |
| Sicherung und Restorefälligkeit | Betrieb überwacht Läufe, Integrität, unabhängigen Zugriff, Fristen und tatsächliche Übungen | REL-S20/Q20; Ausfall/überfälliger kritischer Restorebeleg → Incident-/Freigaberisiko, keine falsche Recoveryzusage |
| Updates, Modelle, Lizenzen und Schwachstellen | Architektur/Sicherheit inventarisieren, bewerten und testen Änderungen; kritische Befunde behandeln, betroffenen Weg gegebenenfalls deaktivieren | REL-S18/A13; keine ungeprüften Autoupgrades oder kompatibilitätsblinden Modellwechsel |
| Sicherheitsvorfall / Missbrauch | Sicherheit + Betrieb dämmen im vorab autorisierten Umfang ein; Belege schützen, Datenschutzfolgen prüfen, Wiederfreigabe vorbereiten | S3.12; kritischer Befund sofort eskalieren, keine Privatdaten in öffentlichen Issues |
| Auskunft, Korrektur, Export, Löschung / Fristablauf | Datenschutz + berechtigter Betrieb prüfen Identität/Umfang, Derivate/Index/Cache/temporäre Kopien/Backupreste und rechtliche Fristen | SEC-15/16/26/27, S2; Frist-/Löschfehler an Verantwortliche; keine Bearbeitung fremder Daten ohne Recht |
| Audit, Berechtigungen und Support | Sicherheit/Datenschutz prüfen Datenminimierung, Endlichkeit, Rollen/Scopes/Grants und Delegationen; Super Admin exklusiv für vorgesehene Adminverwaltung | REL-S06/15/Q18; überbreite Rechte entziehen, ungewöhnliche Aktivitäten untersuchen |
| Schlüssel-/Secretablauf, Rotation, Entzug | Berechtigte Betriebs-/Sicherheitsverantwortung rotiert nach geprüftem Verfahren, validiert Folgewirkung und Recovery; Dokumentenschlüssel persönlich getrennt | SEC-09/22; alte Credentials nicht weiter nutzbar; unlesbare Sicherung oder Leak → S3.12/6 |
| Geräte-/Browser-/Sprach-/UIänderung | Qualitätsprüfung aktualisiert reale Fähigkeits-/Zugänglichkeitsmatrix und Einschränkungen; Nutzer verständlich informieren | REL-Q04/06/A16; keine ungetestete Universalunterstützung behaupten |

## S3.12 Sicherheitsvorfall und größerer Ausfall

1. **Erkennen und klassifizieren:** Zeit, betroffenen Umfang, Schutzziel, Quelle und Evidenz erfassen; Ausfall, Datenintegrität, Datenabfluss, Privilegien-/Secretkompromittierung unterscheiden. Unklare Lage bleibt unklar, keine voreilige Entwarnung.
2. **Eindämmen:** Nur vorab berechtigte Sperren/Session-/Secretentzüge, Netz-/Featurebegrenzung und Jobpause ausführen; minimale sichere Betriebsbelege sichern. Schutz vor Datenverlust und unzulässiger weiterer Verarbeitung priorisieren; nicht ad hoc private Dokumente lesen.
3. **Bewerten und informieren:** Projektinhaber, zuständige Sicherheits-/Datenschutzverantwortung und nötige Kontakte erreichen. Betroffene, Umfang, mögliche Melde-/Benachrichtigungspflichten und geltende Fristen fachlich prüfen. Keine gesetzlichen Fristen frei erfinden; nicht abrufbare aktuelle Normtexte aus dem [Referenzrahmen](../quality/REFERENZRAHMEN.md) rechtzeitig verifizieren.
4. **Bereinigen und wiederherstellen:** Ursache/kompromittierte Artefakte/Schlüssel prüfen; saubere Fassung, unabhängige Sicherung und aktueller Kontrollstand nachweisen. Anbieterverlust, DNS-/Zugangsverlust und Super-Admin-Verlust getrennt behandeln. Kein Restore alten Vertrauens und keine unautorisierte Ersatzplattform.
5. **Nachprüfen und freigeben:** Betroffene REL-/AT-S2-/AT-S3-Fälle erneut ausführen; Rechte, Löschung, Isolation, Datenvollständigkeit und Kosten prüfen. Eigentümer genehmigt den konkreten Wiederanlauf; Rückkehr zur Verfügbarkeit allein ist kein Sicherheitsnachweis.
6. **Abschließen und lernen:** Ursache, Folgen, tatsächliche Zeiten, Datenverluste, Maßnahmen und offene Risiken dokumentieren; Verantwortliche/Fristen für Nacharbeit; Retention der geschützten Belege und bereinigte Kommunikation. Wiederkehrende Übung mit bestätigtem Rhythmus und tatsächlichem Wiederherstellungs-/Rollbacknachweis.

## S3.13 Ablehnung, Einschränkung und menschliche Genehmigung

| Kategorie | Beispiele / Entscheidung | Wirkung |
|---|---|---|
| Absoluter Blocker im betroffenen Umfang | Kontenleck, Privilegieneskalation, unsicherer Adminzugang, offenes Secret, unzulässige Datenweitergabe/Löschwiederbelebung, gefährliche Migration, unfertige erreichbare Funktion, fehlende notwendige unabhängige Recovery oder nicht erfüllter Pflichtschutz | Keine Aktivierung; bei gemeinsamen Schutz-/Datenpfaden gesamte Veröffentlichung stoppen. Keine Ausnahme durch Flag, Tests oder pauschale Risikoakzeptanz. |
| Entscheidung/Voraussetzung fehlt | Keine menschliche Veröffentlichungsgenehmigung, ungeklärte Architektur, erforderlicher Grenzwert/Beleg/Verantwortlicher fehlt, Anwendbarkeit unklar, Kosten nicht autorisiert | Keine davon abhängige Ausführung bis konkrete Entscheidung und Nachweise vorliegen; Auftrag zur Dokumentation genügt nicht. |
| Dokumentierbare akzeptable Einschränkung | Nicht sicherheitskritische belegte Plattformgrenze mit brauchbarem Rückfallweg, klar abgegrenzter deaktivierter optionaler Umfang | Nur mit Auswirkungsanalyse, Quelle, Zuständigkeit, Frist bzw. Neubewertungsanlass und ausdrücklicher menschlicher Bestätigung; kein Verstoß gegen verbindliche Schutzziele. |
| Begründet nicht anwendbar | Keine Webhooks, keine entsprechende Cross-Origin-Technik, REL-Q10 mangels genehmigtem Zahlungsumfang | Fachlich prüfen und begründen; keine Umdeutung von „nicht implementiert“ bei einer benötigten Funktion zu Nichtanwendbarkeit. Bei späterer Aktivierung neu bewerten. |

**Genehmigungsdatensatz:** Entscheider, geprüfte Fassung/Artefakt, Ziel, Umfang/aktive Funktionen, anwendbare Kontrollen und Ergebnisse, zulässige Einschränkungen, Belege, Ausführungsbedingungen/-zeitraum, Rückweg und explizites Ja/Nein. Kosten-/Cloud-/Datentransferfreigaben gesondert passend nachweisen. Technische Zugriffsmöglichkeit, grüne CI, PR-Merge oder allein bestandene Tests erteilen keine Genehmigung. Neue kritische Erkenntnisse oder wesentliche Fassungsänderung setzen die betroffene Freigabe außer Kraft, bis neu entschieden ist.

## S3.14 Offene Entscheidungen und Abhängigkeiten

Die folgenden O-S3-Kennungen sind Arbeits-/Nachweisbezüge, **keine neuen Produktentscheidungen**; keine offene Frage wird hier als genehmigt geschlossen.

| Kennung | Zu bestätigender Gegenstand | Zuständig / Voraussetzung |
|---|---|---|
| O-S3-01 | Primärhosting und EU-Verarbeitungs-/Unterauftragnehmernachweise; Oracle zuerst bewerten, Alternativen offen | Projektinhaber/Architektur, DEC-48; O-S1-02 |
| O-S3-02 | Unabhängiger EU-Backupanbieter, Nachweis der Zugangs-/Schlüsselunabhängigkeit und Kosten | Projektinhaber/Betrieb/Sicherheit, DEC-49; S2.19 |
| O-S3-03 | Stack, Deploymentarchitektur, Umgebungsisolation, Build-/Artefaktvertrauen und Vorproduktionsbedarf | Architektur/Sicherheit; ADRs vor Umsetzung |
| O-S3-04 | Sicheres technisches Bootstrap-/Identitäts-/MFA-Verfahren, Atomizität/Einmaligkeit und erste Anmeldung | Projektinhaber/Architektur/Sicherheit; SEC-01..05, O-S1-06/13 |
| O-S3-05 | Admin-Recovery, MFA-/Zugangsverlust, Kompromittierung und dauerhafte Unverfügbarkeit ohne zweiten Hauptadmin | Projektinhaber/Sicherheit; keine ad hoc Nachfolgeentscheidung |
| O-S3-06 | Datenklassenbezogene RPO/RTO, Sicherungsfrequenz, Übungsrhythmus und Kapazität | Projektinhaber/Betrieb; S3.6, N1.10; O-S2-06/11 |
| O-S3-07 | Endliche Retention, Löschbeweise, Marker-/Backup-/Altclientkompatibilität und Pflichtreste | Datenschutz/Sicherheit/Betrieb; S2.7/8, O-S1-10 |
| O-S3-08 | Verfügbarkeits-/Antwort-/Last-/Queue-/Quota-/Alarmziele und Beobachtungsfenster | Projektinhaber/Qualitätsprüfung/Betrieb; N1.10, O-S1-09/14 |
| O-S3-09 | Unterstützte Geräte/Browser/OS und assistive Kombinationen, Offlineumfang, DE/FR/EN, WCAG-AA-Ziel | Projektinhaber/Qualitätsprüfung; NFR-02/03/08/19/20, O-S1-11 |
| O-S3-10 | Datenschutzrollen, Rechtsgrundlagen, Verträge, etwaige DSFA/Transfers, Incidentkommunikation und aktuelle Normfassungen | Projektinhaber/zuständige Datenschutzprüfung; SEC-26 und Referenzrahmen |
| O-S3-11 | Operative Schlüssel-/Secretverwaltung, Rotation, Verlust-/Recoveryverfahren und Sicherungsentschlüsselung | Architektur/Sicherheit; persönliche Dokumentenschlüssel strikt getrennt, O-S1-07/08 |
| O-S3-12 | Reale Verbrauchs-/Kostengrenzen, technische Stopps, Lizenzen und Gratislimits | Projektinhaber/Betrieb; keine Ausgabe oder Pflicht-Pay-API, O-S1-05 |
| O-S3-13 | Namentliche Verantwortliche, Vertretung, Reaktions-/Prüfintervalle, eng begrenzte Notfallrechte und Belegretention | Projektinhaber; vor Produktion bestätigen |
| O-S3-14 | Rolloutstufen, Migrations-/Rollbackkompatibilität, Kontrollstand und technische Smoke-/Regressionstests | Architektur/Betrieb/Qualitätsprüfung; S2-UPG/MOV und NFR-25 |

FE-56 bleibt unabhängig hiervon offen. Pädagogische Rubriken und zulässiger Funktionsumfang bleiben nach N1/Entscheidungsmatrix zu bestätigen. Bestehende M2b/M5/M8-Zuordnungen aus dem [Teilplan](ENTWICKLUNGSPLAN.md) unverändert; S3 schafft keinen Gesamtmeilensteinplan und keine Termine.

## S3.15 Künftige Abnahmeszenarien

Alle folgenden Fälle sind geplante **Soll-Abnahmen**, während Mission 4 nicht ausgeführt. Ein Fall benötigt konkrete Umgebung, Schritte, Sollquelle, Istbefund und verantwortliche Prüfung nach S3.2; Negativfälle mit erlaubtem Gegenfall ergänzen. Keine neuen Releasekontrollen, sondern Ablaufnachweise zu bestehenden REL-/SEC-/NFR-Vorgaben.

| Kennung | Geplanter Prüfgegenstand | Erwartetes Ergebnis / maßgeblicher Anschluss |
|---|---|---|
| AT-S3-01 | Testkonfiguration zeigt auf Produktion oder enthält Produktionssecret | Übergang/Jobstart gesperrt, keine produktive Wirkung; S3.3, REL-S01/S07/A13 |
| AT-S3-02 | Unberechtigter öffentlicher Bootstrap, bekannter Defaultzugang oder konkurrierender Erstbootstrap | Kein öffentlicher Adminzugang; nur berechtigte einmalige Hauptbesetzung, nie zwei; S3.5, REL-S06/S19 |
| AT-S3-03 | Erstzugang mit ungeprüfter Identität oder fehlender Admin-MFA | Keine reguläre privilegierte Nutzung; REL-S03/S06/S09/S19 |
| AT-S3-04 | Delegierter befördert sich oder verwaltet weitere Admins / liest private Dokumente | Serverseitig verweigert; autorisierte enge Aufgaben bleiben möglich; REL-S04/S06 |
| AT-S3-05 | Adminsession widerrufen, MFA verloren oder Super Admin abwesend | Kein alter Sessionzugriff, kein zweiter Hauptadmin/Recoverybypass; exklusive Aktionen warten; S3.5.2 |
| AT-S3-06 | Primärplattform und Hauptzugang vollständig verloren | Unabhängiger EU-Zugriff und geprüfter Recoveryweg; bestätigte RPO/RTO gemessen; REL-S20/Q20 |
| AT-S3-07 | Sicherung korrupt oder notwendiger Schlüssel/aktueller Kontrollstand fehlt | Kein aktiver Restore, sichere Diagnose/Unterbrechung; S2.7/8, REL-Q20 |
| AT-S3-08 | Altes Backup enthält endgültig gelöschte A/B-Daten, alte Grants und temporäre Transkripte | Keine Wiederbelebung/Querzugriffe; heutige Zustände maßgeblich; REL-S04/Q11/Q16/Q20 |
| AT-S3-09 | Selektiver Restore gegen jüngere Fortschritte/manuelle Termine | Konflikte/Abhängigkeiten nachvollziehbar; keine stille Rücksetzung/Umplanung; S2, NFR-24 |
| AT-S3-10 | Tests grün, Eigentümergenehmigung fehlt oder Build nach Prüfung verändert | Kein Deployment/Freigabe; neue Fassung erneut prüfen; S3.7/13, REL-A13 |
| AT-S3-11 | Unfertige Funktion trotz versteckter UI per API/Tool/Job/Altclient erreichbar | Serverseitige Sperre, keine Daten-/Kostenwirkung; REL-S06/Q06 |
| AT-S3-12 | Stufenrollout erweitert Gruppe oder aktiviert externe Verbindung ohne Recht | Keine automatische Scope-/Provider-/Kalenderfreigabe; geprüfter Umfang begrenzt; S3.9 |
| AT-S3-13 | Inkompatibles Schema, alter PWA-Client und parallel aktiver Alt-/Neuschreiber | Kein unsicherer Cutover/Schreibsplit, nachgewiesene Kompatibilität oder sichere Wartungsphase; S2-UPG/MOV |
| AT-S3-14 | Jobabbruch nach Teilwirkung, unbekannter externer Erfolg und Wiederaufnahme | Aktuelle Rechte/Kosten/Löschung geprüft; keine Doppelwirkung; REL-Q07/Q08/Q09 |
| AT-S3-15 | Rollback würde gelöschte Daten/alte Rechte aktivieren oder Transformation ist irreversibel | Unsicherer Rückweg gesperrt; geprüfte Vorwärtskorrektur/selektive Recovery oder Pause; S3.10 |
| AT-S3-16 | Nach Deployment A/B-Isolation, Gesundheit oder Pflichtgate fehlerhaft | Keine Ausweitung; Eindämmung, dokumentierter sicherer Rückweg und neue Freigabe; S3.7/12 |
| AT-S3-17 | Backup-/Zertifikats-/Kapazitäts-/Incidentalarm oder kritische Prüffälligkeit | Zuständige erreichbar, Reaktion/Eskalation und Befund dokumentiert; REL-Q17/Q18/Q20 |
| AT-S3-18 | Gratislimit erschöpft, Kostenpfad/Providerfallback nicht autorisiert | Betroffener neuer Weg stoppt; keine bezahlte Ersatz-API, keine neue Ausgabe; REL-Q01/Q02/Q03 |
| AT-S3-19 | Datenschutzgesuch, Retentionsablauf oder Schlüsselkompromittierung | Identität/Umfang und Pflichten geprüft, Kopien/Derivate einbezogen; keine falsche Lösch-/Geheimhaltungszusage; SEC-15/22/26/27 |
| AT-S3-20 | REL-Nachweis fehlt, Technik nicht anwendbar oder Einschränkung vorgeschlagen | Pflichtbeleg blockiert; Nichtanwendbarkeit begründet, zulässige Einschränkung explizit entschieden; keine automatische Veröffentlichung; S3.8/13 |

## S3.16 Rückverfolgbarkeit und Verweise

| Primärquelle | Betriebsanschluss in S3 |
|---|---|
| P1 Ziele/Kosten/Datenschutz und P2 System-/Admin-/Nachbargrenzen | S3.1–4, S3.9/13; keine Änderung fachlicher G-/CON-/SC-/NB-/CFG-Kennungen |
| FE-55/58..72, SEC-01..07 | PWA, Konten, serverseitige Flags, Konfiguration, Quoten, Release und einziger Super Admin: S3.3/5/7/8/9 |
| FE-40..42/75..83, DEC-49, SEC-08..11/15/16/22/27 | EU, Daten-/Schlüsselschutz, unabhängiger Restore und Nichtwiederbelebung: S3.4/6/10/11/12 |
| FE-84..89, SEC-12/13/17..21/24 | Verbindungen, sichere Agenten-/Import-/Retrywirkung: S3.7/8/9/10/11 |
| S2 BAK/UPG/MOV; UC-60, BAT-23/BAT-25, DM-69/DT-81 | Datenverträge, Sicherung, Migration und heutiger Kontrollstand: S3.6/10; keine Datenmodelländerung |
| NFR-01..25, SEC-01..27 und 46 REL-Profile | Qualitäts-/Schutzprüfungen mit späterer tatsächlicher Ausführung: S3.7/8/11/15 |
| 25 DEC-V1 und 28 AT-L; Entscheidungsmatrix | Bei betroffener Funktion fachliche Regression und Bewahrung gültiger Lernbelege: S3.6/7/10 |
| DEC-48, offene O-S1/O-S2 und Teilmeilensteine | Bewertungspriorität statt Anbieterwahl; offene technische Nachweise: S3.4/14 |

[Spezifikationsindex](README.md), [P1](P1-ziele-rahmenbedingungen.md), [P2](P2-architekturueberblick.md), [S1](S1-nachbarsysteme.md), [S2](S2-datenmigration.md), [N1](N1-nichtfunktional.md), [N2](N2-querschnittskonzepte.md), [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md), [Teilplan](ENTWICKLUNGSPLAN.md), [E3](E3-pruefnachweis.md), [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md), [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md), [Referenzrahmen](../quality/REFERENZRAHMEN.md), [ADR](../ARCHITECTURE_DECISIONS.md), [historische Vision](../PROJECT_VISION.md), [ursprüngliche Anforderungen](../REQUIREMENTS.md), [historische Roadmap](../ROADMAP.md) und [PACE-Workflow](../ai/WORKFLOW.md).

S3 legt fachliche Betriebsanforderungen zur Prüfung vor. Daraus folgt weder eine finale technische Architektur noch eine Ausführungsfreigabe. Sämtliche Produkt-/Betriebsnachweise und die in S3.14 benannten Entscheidungen stehen noch aus.
