# N1 — Nichtfunktionale Anforderungen

**Projekt:** Syllentra AI\
**Version:** 0.8\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

<a id="n11-zweck-und-begrenzter-ausarbeitungsstand"></a>

## N1.1 Zweck und fachlicher Ausarbeitungsstand

Dieser fachliche V1-Prüfentwurf ergänzt die bestehenden Qualitätsgrenzen um vollständige Prüfprofile für den bestätigten Funktionsumfang. Maßgeblich sind zusätzlich die Prüfprofile und das Messprotokoll in N1.8–N1.10. Er ersetzt weder eine ausgemessene Betriebsarchitektur noch Last-, Sicherheits- oder Barrierefreiheitstests. Zahlen und Anbieter werden nicht eigenmächtig festgelegt. Die fachlichen Messmethoden werden beschrieben; ihre technische Ausgestaltung und die Zielwerte benötigen spätere Bestätigung. [S1](S1-nachbarsysteme.md) beschreibt fachliche Nachbarverträge; [N2](N2-querschnittskonzepte.md) die gemeinsamen Schutzgrenzen. N1 spezifiziert Qualität, keine Use-Case-Alternative oder interne Komponentenstruktur.

## N1.2 Verfolgbare Qualitätsanforderungen und spätere Nachweise

| Kennung | Anforderung / Entscheidung | Nachweis und offener Vertiefungsschritt |
|---|---|---|
| NFR-01 | Strikte Kontoisolation in allen Datenwegen, keine privaten Admininhalte standardmäßig (FE-59, FE-63) | Negative Versuche Konto A gegen Kennungen, Suche, Export, Cache, Jobs und Restore von B; konkrete Zugriffstests nach Implementierung. |
| NFR-02 | PWA installierbar auf tatsächlich unterstützten Android-/iOS-Konfigurationen, responsiv auf Tablet/Computer (FE-55) | Browser-/OS-Matrix mit Versionen für Installation, Dateien, Push, Mikrofon, Audio, Passkeys, Kalender und Hintergrund erstellen; fehlende Fähigkeiten mit brauchbarem Rückfallweg. Keine Universalgarantie. |
| NFR-03 | Offlinearbeit mit heruntergeladenen eigenen Daten und kontrolliertem Wiederabgleich (FE-33 bis FE-35) | Konflikt-, Entzugs- und Löschmarkierungsszenarien; Cloud-KI und nicht gecachte Inhalte bleiben offline ausdrücklich unverfügbar. |
| NFR-04 | Eigene zentrale Cloud und verschlüsselte Sicherungen in der EU, portierbare Daten (FE-40 bis FE-42, FE-75) | Hosting-/Unterauftragsverarbeiter-/Backupregion nachweisen; Anbieter, Wiederanlaufziel und maximal tolerierbarer Datenverlust offen für S2. Kein persönlicher PC als notwendiger Server. |
| NFR-05 | Kostenfreie kommerziell geeignete Software-/Modelllizenzkette ohne verpflichtende bezahlte API (FE-30, FE-53) | Code, Modellgewichte, Datennutzungsbedingungen und Unterabhängigkeiten vor Auswahl prüfen; Hardware-/Cloud-/Speicherkosten getrennt budgetieren. Kostenloser Softwarezugang ist keine Zusage kostenloser Infrastruktur. |
| NFR-06 | Widerruf und Ablauf sperren Folgezugriffe, Fehler lassen zulässig importierte Daten nutzbar (FE-84, FE-85) | Widerruf vor geplantem Abruf und Retry testen; Scope/letzten Erfolg wahrheitsgemäß anzeigen. Verbindungsautomatik muss explizit je Verbindung aktiviert sein. |
| NFR-07 | Begrenzte sichere Wiederaufnahme ohne doppelte Wirkung oder ungewollte Zahlung (FE-88) | Unterbrechung vor/nach Wirkung, partieller Erfolg und unbekannte Wirkung prüfen; Versuchszahl, Backoff, Laufzeit und Fortschrittsanzeige noch festzulegen. |
| NFR-08 | Bedienung ohne Sicht-/Hörzwang, verständliche Fehler und unabhängige Sprachwahl (FE-19 bis FE-21, FE-73, FE-74) | Tastatur-/Screenreader-/Fokus-/Kontrastprüfung, Textalternative zu Audio, keine ungefragte Aufnahme/Ausgabe; UI FR/DE/EN und getrennte KI-/Übungs-/Audiosprache testen. Qualitätsziel und Messverfahren weiter ausarbeiten. |
| NFR-09 | Warnungen vor Quoten, bei voller Quote nur neue betroffene Aufnahmen sperren (FE-64, FE-65) | Speicher-, Datei-, Archiv-, Medien- und Rechengrenzen pro Konto prüfen; Zahlen/Einheiten und Warnschwellen vor Produktfreigabe bestimmen. |
| NFR-10 | Geheimnisfreie, private, endliche Integrations-/Administrationsnachweise (FE-70, FE-89) | Logs und Exporte mit künstlichen Secrets auf verbotene Offenlegung prüfen; Retention je Nachweisart und notwendige rechtliche Reste bestimmen. |
| NFR-11 | Verschlüsselter Transport, Datenhaltung und Sicherungen; sensible geräteseitige Zusatzverschlüsselung (FE-76 bis FE-79) | Schlüsselverlust-, Gerätewechsel-, Schutzvererbungs- und temporäre Cloudklartexttests; keine privaten Klartextschlüssel beim Backend/Admin. Konkrete Kryptoprüfung N2. |
| NFR-12 | Nachweisbare endgültige Löschung ohne Wiederbelebung (FE-80 bis FE-82) | Offlineabgleich, Suche, Historie und Restore mit endgültig gelöschten Zielen testen; physische Bereinigung/Backupablauf wahrheitsgemäß trennen. |

## N1.3 Offene Mess- und Betriebsentscheidungen

Die offenen Punkte O-S1-02 bis O-S1-14 im [S1-Risikoregister](S1-nachbarsysteme.md) bilden den Arbeitsvorrat: EU-Anbieter und Budget, Geräte-/Hardwarekapazität, Lizenzprüfung, unterstützte Konnektoren, Antwort-/Verarbeitungszeiten, Lastprofil, Verfügbarkeit, Quoten, Retrygrenzen und Aufbewahrungsfristen. Es gibt keine verbindlichen erfundenen Millisekunden-, Speicher-, Tages- oder Prozentwerte. Vor Produktfreigabe sind Zielwerte mit dem Projektinhaber festzulegen und unter repräsentativen Bedingungen zu messen.

**Abgrenzung:** Diese Lieferung prüft Dokumente, keine laufende PWA oder Cloud. S2 behandelt Migration und Wiederherstellung, S3 Inbetriebnahme und sichere Erstbesetzung des einzigen Super Admin. FE-56 bleibt eine offene fachliche Entscheidung, keine noch zu messende bereits genehmigte Inboxfunktion.

## N1.4 Offene Qualitätsnachweise der S2-Portabilität

[S2](S2-datenmigration.md) vertieft NFR-02/03/04/07/08/09/10/11/12. Vor Produktfreigabe sind sichere Export-/Importkapazität, Browser-/PWA-Speichergrenzen, unterstützte Paketfassungen, Quoten, Wiederholungsbudgets und Disaster-Recovery-Ziele RPO/RTO zu messen und festzulegen. O-S2-01 bis O-S2-12 bleiben technische offene Arbeiten; keine erfundenen Paketgrößen, Zeiten, Retentionwerte oder unbegrenzte Gratisrechenleistung.

**Künftige Qualitätsprüfungen:** Großer/rekursiver Archivbestand bleibt begrenzt; fehlender Schlüssel führt zu sicherem Teilweg oder Sperre; abgebrochener Lauf legt nichts doppelt an; definitive Löschung überlebt Restore und alten PWA-Client. Oberfläche für Export/Vorschau/Konflikt/Teilbericht in DE/FR/EN mit Tastatur, Screenreader, Fokus-/Fehler-/Fortschrittsanzeigen und textlichen Differenzen prüfen. Diese Dokumentationslieferung führt keine dieser Produktprüfungen aus und installiert keine neue Laufzeitabhängigkeit.

## N1.5 Qualitätsanforderungen für L-08, L-04, L-09 und L-02

**NFR-08 konkretisiert:** Ablenkungsarmer Modus jederzeit mit Tastatur/Screenreader beendbar; kein Fokusverlust, keine verworfenen Antworten/Entwürfe/Fortschritte. Reduzierte Bewegung und deaktivierbare Motivation prüfen; keine Ranglistenpflicht, Serienzwänge oder künstlicher Zeitdruck. Vier Fortschrittsarten durch Text und Beleg verständlich, nicht nur Farbe/Animation. UI DE/FR/EN bleibt von Lern-/Audiosprache unabhängig.

**Nachweise für L-08:** Aktivierungs-/Deaktivierungsrennen, parallele manuelle Planänderung, fehlende/veraltete Evidenz und konfliktgeprüftes Undo an repräsentativen Fällen evaluieren. Geeignete alternative Erklärungen nach belegten Schwierigkeiten pädagogisch prüfen, ohne feste Wiederholungsformel oder Erfolgsquote zu erfinden. Manuelle/bestätigte Termine und jüngere gültige Lernbelege bleiben erhalten.

**Nachweise für L-04/UC-65 und L-09/UC-66:** M5-Kandidaten/Regelpriorität/J−5/J−1 und M8-DST-/Ruhezeit-/Geräte-/Kanal-/Zustellfehler getrennt testen; Ausgangsruhezeit 22:00–08:00 ist ausdrücklich bestätigt, konkrete Timer-/Retry-/Retentionsgrenzen weiterhin offen. Quellen-/Kohorten-/Übergangsfälle, unvollständige Sollabdeckung und fehlende Nachweise prüfen; kein Konnektorzwang. [F2](F2-anwendungsfaelle.md) enthält Soll-Abnahmen, [E3](E3-pruefnachweis.md) tatsächliche Dokumentprüfungen. Hier keine behaupteten Produkt-/Accessibility-/Pädagogiktests.


## N1.6 Produktionsreife, Lastverhalten und Freigabekontrollen (zwei Checklisten vom 22.10.2026)

Der Projektinhaber hat zwei ergänzende Prüflisten mit zusammen **40 Einzelpunkten** für die spätere Produktfreigabe übernommen. Das Original mit eindeutigen Kennungen **REL-S01 bis REL-S20** (Sicherheit) und **REL-Q01 bis REL-Q20** (Betrieb, Performanz, UX) steht in [Release Readiness — 40 Prüfungen](../quality/RELEASE_READINESS_40.md). Die Nummerierungen sind keine neuen FE-Kennungen und keine Implementierungsbehauptungen.

**Nichtfunktionale Verantwortung von N1:** Raten-/API-/Rechenlimits, bewilligte Budgets, Antwort- und Abbruchverhalten, klare Lade-/Leer-/Fehlerzustände, deduplizierte Aktionen, Datenminimierung, Indizes, Paginierung, passende Kompression und Zwischenspeicherung, Datei-/Archivlast, Verfügbarkeitsüberwachung, aussagekräftige datensparsame Betriebslogs, parallele Nutzung, Restore-Proben und gemessene Wiederherstellungsziele. Die Security-Details stehen in [N2](N2-querschnittskonzepte.md). S2 bleibt für Daten-/Restoreverträge zuständig.

**Freigabebedingung:** Vor Aktivierung bzw. Produktivstart sind die einschlägigen Tests tatsächlich durchzuführen und nachzuweisen. Technische Grenzwerte, Kapazitäten, Warnschwellen und RPO/RTO sind noch offen und dürfen nicht erfunden werden. Zahlungstransaktionen und Schutz vor Doppelzahlung (REL-Q10) sind ausdrücklich nur für eine später eigens genehmigte kommerzielle Funktion relevant. Die übrigen Punkte gelten für die V1 insoweit, wie die jeweils geprüften Funktionen/Techniken vorhanden sind. Produktprüfungen wurden durch diese Dokumentänderung nicht ausgeführt.

## N1.7 Begrenzter Anschluss von DEC-48 und DEC-49

NFR-04/05/11/12 werden durch DEC-48/49 präzisiert: Oracle zuerst bewerten, Alternativen offenhalten; EU, Kapazität, Speicher, Verfügbarkeit, Netz, Betrieb, tatsächliche Kosten/Gratislimits, Sicherheit und Lizenzen nachweisen. Verschlüsselte EU-Sicherung unabhängig vom Primäranbieter, periodische tatsächliche Restore-Proben und Portabilität sind Pflichtziele. Der frühere Vergleichsrahmen von 10 EUR gilt seit Mission 7 für künftige Studien mit bis zu 20 EUR brutto/Monat; keine Ausgabe. RPO/RTO, Frequenz, Retention und Messverfahren bleiben offen. [ADR](../ARCHITECTURE_DECISIONS.md), [S2](S2-datenmigration.md), [Matrix](ENTSCHEIDUNGSMATRIX.md) und REL-S20/REL-Q20 führen die Nachweise. Dieser historische Anschluss aus Mission 2 wird durch N1.8–N1.10 fachlich vervollständigt; eine Produktprüfung oder technische Freigabe erfolgt weiterhin nicht.

## N1.8 Ergänzendes Anforderungsregister

NFR-01 bis NFR-12 bleiben unverändert erhalten. Die folgenden Kennungen ergänzen eigenständige Qualitätsaspekte. Alle 25 Profile sind Soll-Anforderungen, nicht implementierte oder getestete Produkteigenschaften.

| Kennung | Ergänzter Qualitätsaspekt |
|---|---|
| NFR-13 | Antwort- und Ladeverhalten |
| NFR-14 | Asynchrone Verarbeitung und Fairness |
| NFR-15 | Ressourcen und Modellverbrauch |
| NFR-16 | Suche, Index, Pagination und Cache |
| NFR-17 | Verfügbarkeit und Degradation |
| NFR-18 | Verständliche Zustände und Fehlerrückmeldung |
| NFR-19 | Barrierefreiheit als überprüfbares Ziel |
| NFR-20 | Mehrsprachige Konsistenz |
| NFR-21 | Belegte Erklärungen und Unsicherheit |
| NFR-22 | Übungen, Quiz, Korrektur und Kompetenzbelege |
| NFR-23 | Pädagogische Anpassung |
| NFR-24 | Ziele, Sitzungen und Fortschrittskonsistenz |
| NFR-25 | Wartbarkeit und reproduzierbare Qualitätsprüfung |

## N1.9 Verbindliche Prüfprofile der V1-Sollfassung

Für jedes Profil gelten zusätzlich die Beleg- und Freigaberegeln aus [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md). Fehlende Zielwerte werden als offen ausgewiesen und sperren die betroffene Produktabnahme, nicht die redaktionelle Prüfung dieses Dokuments.

### NFR-01 — Kontoisolation

| Merkmal | Festlegung |
|---|---|
| Ziel | Private Informationen bleiben ausschließlich berechtigten Konten zugänglich. |
| Geltungsbereich | API, Suche, Aufgaben, Speicher, Exporte, KI-Kontext, Offlinecache und Restore; auch Administratoren. |
| Prüfmethode | Konten A/B mit gleichen Objektnamen und verschiedenen Rechten; IDs, Suchfilter, Seitenzeiger, Jobs und Paketziele vertauschen; parallele Läufe. |
| Abnahmekriterium | Kein Inhalt, Metadatum oder Existenzhinweis von B für A; zulässiger Eigenzugriff bleibt möglich. |
| Erforderlicher Beleg | Negativ-/Positivmatrix mit synthetischen Konten und bereinigten Antworten; REL-S04/06, REL-Q19. |
| Technische Abhängigkeiten | Durchgängiger Eigentumsbezug, serverseitige Autorisierung, SEC-04/19. |
| Offene Parameter | Konkrete Speicher-/Indextechnik und Testumgebung; keine Ausnahme für Adminrolle. |

### NFR-02 — Geräte- und PWA-Kompatibilität

| Merkmal | Festlegung |
|---|---|
| Ziel | Installation und Kernbedienung auf belegbar unterstützten Geräten. |
| Geltungsbereich | Android/iOS, Smartphone/Tablet/Computer; Installation, Dateien, Audio, Push, Kalenderzugriff und Hintergrundverhalten. |
| Prüfmethode | Versionierte OS-/Browser-/Gerätematrix; Installation, Update, Startsymbol, Anmeldung und Kernabläufe real prüfen; verweigerte Fähigkeiten simulieren. |
| Abnahmekriterium | Jede als unterstützt veröffentlichte Kombination besteht die zugehörigen Kernfälle; Einschränkungen und bedienbarer Rückfallweg sind sichtbar. |
| Erforderlicher Beleg | Matrix mit Versionen, Geräten, beobachteten Fähigkeiten und Fehlfällen; REL-Q06/19. |
| Technische Abhängigkeiten | PWA-/Browserfähigkeiten, Berechtigungen und verfügbare Testgeräte. |
| Offene Parameter | Unterstützte Versionen, Mindestgeräte und Aktualisierungszeitraum vor Freigabe bestätigen. |

### NFR-03 — Offlinebetrieb und Synchronisation

| Merkmal | Festlegung |
|---|---|
| Ziel | Eigene freigegebene Daten ohne Verlust kontrolliert abgleichen. |
| Geltungsbereich | Gezielt heruntergeladene Inhalte, lokale Entwürfe und spätere Synchronisation; keine Offline-Cloud-KI. |
| Prüfmethode | Netztrennung, gleichzeitige Änderungen, Geräteentzug, Quoten und alte Clients mit Tombstones prüfen; Uhrabweichung einbeziehen. |
| Abnahmekriterium | Kein stiller Verlust und keine Wiederbelebung; Konflikte nachvollziehbar; nach Wiederverbindung aktuelle Rechte vor Übernahme prüfen. Bereits geladene Kopien sind nicht fernlöschbar garantiert. |
| Erforderlicher Beleg | Konflikt-/Lösch-/Entzugsprotokoll mit Ausgangs-/Endrevisionen; S2, REL-Q16/19. |
| Technische Abhängigkeiten | Versions-/Konfliktmodell, lokale sichere Speicherung, aktueller Kontrollstand nach N2.8. |
| Offene Parameter | Offlineumfang, Speichergrenzen, Konfliktverfahren, erlaubtes Clientalter und Abgleichziele. |

### NFR-04 — Betrieb, Sicherung und Portabilität

| Merkmal | Festlegung |
|---|---|
| Ziel | Zentraler EU-Betrieb ohne privaten Dauer-PC und unabhängige Wiederherstellbarkeit. |
| Geltungsbereich | Hauptdaten, Unterauftragnehmer, verschlüsselte EU-Sicherung außerhalb des Primäranbieters, Nutzerexport und Anbieterwechsel. |
| Prüfmethode | Regionen und Abhängigkeiten prüfen; Hauptanbieterzugang im isolierten Test entziehen; Daten-/Schlüssel-/Kontrollstand aus unabhängigen Belegen wiederherstellen. |
| Abnahmekriterium | Nach DEC-49 unabhängig wiederherstellbar, Datenvollständigkeit und heutige Rechte/Löschungen erhalten; gemessene RPO/RTO erfüllen vorab bestätigte Ziele. |
| Erforderlicher Beleg | Anbieter-/Regionsnachweise, Exportvergleich und protokollierte Restore-Probe; REL-S20/Q20, S2. |
| Technische Abhängigkeiten | Auszuwählende EU-Provider, getrennte Zugänge/Schlüssel, Recovery- und Paketverfahren. |
| Offene Parameter | RPO/RTO, Frequenz, Retention und Kapazität mittels Schadens-/Wiederanlaufanalyse bestimmen; keine Ressourcenbuchung. |

### NFR-05 — Lizenz- und Kostenverträglichkeit

| Merkmal | Festlegung |
|---|---|
| Ziel | Kommerziell zulässige kostenlose Software/Modelle ohne verpflichtende bezahlte KI-API. |
| Geltungsbereich | Code, Gewichte, Datennutzung, Bibliotheken, Distribution sowie reale Infrastruktur-/Inferencekosten. |
| Prüfmethode | Versioniertes Lizenzinventar mit Nutzungsfällen prüfen; Ausfall des Gratisangebots und Verbrauch unter Referenzlast modellieren. |
| Abnahmekriterium | Keine unvereinbare oder ungeklärte notwendige Lizenz; keine automatische kostenpflichtige Ausweichlösung; reales Ressourcenangebot belegt. |
| Erforderlicher Beleg | Lizenzquellen, Einschränkungen, Verbrauchs-/Kostenrechnung, Freigaben; REL-S18/Q03. |
| Technische Abhängigkeiten | Auswahlprüfung von Software, Modellen und Anbietern. |
| Offene Parameter | Lizenzauslegung, konkrete Angebote und Kapazität; seit Mission 7 bis zu 20 EUR brutto/Monat nur Untersuchungsrahmen (zuvor 10 EUR), keine Ausgabe. |

### NFR-06 — Widerruf und kontrollierter Ausfall

| Merkmal | Festlegung |
|---|---|
| Ziel | Externe Verbindungen verlieren nach Entzug ihre Wirkung. |
| Geltungsbereich | Manuelle bzw. ausdrücklich aktivierte automatische Verbindungen, Warteschlange und Wiederholungen. |
| Prüfmethode | Entzug zwischen Planung und Abruf, Scopewechsel, Ablauf und Anbieterausfall injizieren; bereits zulässige Importkopien öffnen. |
| Abnahmekriterium | Keine neuen externen Zugriffe nach Entzug; Kopien bleiben im zulässigen Umfang nutzbar; Status zeigt letzten Erfolg und Einschränkungen. |
| Erforderlicher Beleg | Zeitlich geordnete Verbindungs-/Jobnachweise ohne Tokens; REL-S06/Q07. |
| Technische Abhängigkeiten | Aktuelle Berechtigungsprüfung je Versuch, offizielle Konnektoren. |
| Offene Parameter | Zeitgrenzen für Entzugserkennung und Abgleichverfahren; kein pauschales Automatikrecht. |

### NFR-07 — Fehler, Unterbrechung und Idempotenz

| Merkmal | Festlegung |
|---|---|
| Ziel | Wiederaufnahme erzeugt keine doppelten oder unerlaubten Wirkungen. |
| Geltungsbereich | Import, Jobs, Synchronisation, Agentenaktionen, Veröffentlichung und externe Operationen. |
| Prüfmethode | Abbruch vor/nach Commit oder externem Erfolg, doppelter Klick, Replay und unbekannter Ausgang; parallele Wiederholung testen. |
| Abnahmekriterium | Höchstens die beabsichtigte zulässige Wirkung; unbekannte externe Wirkung zuerst abgleichen; begrenzte Versuche mit aktuellen Rechten/Quoten, keine Zusatzkosten ohne Freigabe. |
| Erforderlicher Beleg | Zustandsübergänge, Wirkungszählung, Idempotenz- und Fehlerspuren; REL-Q07/08/09. |
| Technische Abhängigkeiten | Deduplizierung, atomare Zustandswechsel, externe Abgleichmöglichkeit. |
| Offene Parameter | Versuchsbudgets, Backoff, Timeout und Haltefristen der Deduplizierung aus Fehler-/Lastmessungen bestimmen. |

### NFR-08 — Zugängliche Kernbedienung

| Merkmal | Festlegung |
|---|---|
| Ziel | Alle Kernaufgaben ohne Sicht- oder Hörzwang und ohne erzwungene Aufnahme. |
| Geltungsbereich | Anmeldung, Lernen, Import, Gespräch, Kalender, Export, Administration und Fokusmodus. |
| Prüfmethode | Vollständige Tastatur-/Screenreaderabläufe einschließlich Dialogen, Fehlern und Fortschritt; Audio-/Textwechsel und verweigerte Medienrechte. |
| Abnahmekriterium | Kein Tastaturfang; Fokus sinnvoll erhalten; Textalternative verfügbar; keine ungefragte Aufnahme/Ausgabe; Pflichtinformationen zugänglich. |
| Erforderlicher Beleg | Aufgabenprotokolle mit assistiven Werkzeugen und manuellen Beobachtungen; NFR-19/20, REL-A16. |
| Technische Abhängigkeiten | Semantische Oberflächen, Fokusführung und textliche Alternativen. |
| Offene Parameter | Konkrete assistive Testkombinationen; Standardziel nach NFR-19 noch zu bestätigen. |

### NFR-09 — Quoten und Importgrenzen

| Merkmal | Festlegung |
|---|---|
| Ziel | Überlastung vermeiden, bestehende Daten zugänglich halten. |
| Geltungsbereich | Speicher, Dateizahl, entpackte Archive, Audio/Video, Transkription, CPU-/Inferencekontingente je Konto und global. |
| Prüfmethode | Grenzen vor und während Verarbeitung, Archivverschachtelung, Parallelimport, volle Quote und Quotenänderung testen. |
| Abnahmekriterium | Warnung rechtzeitig; nur neue betroffene Aufnahme sperren; Lesen/Export/Löschen vorhandener Daten bleibt möglich; Ressourcen bleiben begrenzt. |
| Erforderlicher Beleg | Grenzwert-/Lastfälle mit Verbrauch vor/nach Abbruch; REL-S11/Q01/Q02/Q15. |
| Technische Abhängigkeiten | Verlässliche Verbrauchszählung, Streaming-/Abbruchfähigkeit, faire Planung. |
| Offene Parameter | Größen, Einheiten, Warnschwellen, reservierte Ressourcen und Grenzfälle aus NFR-15 ableiten. |

### NFR-10 — Datensparsame Nachweise

| Merkmal | Festlegung |
|---|---|
| Ziel | Betriebs- und Integrationsvorgänge endlich und ohne private Schattenarchive belegen. |
| Geltungsbereich | Adminaudit, Integrationshistorie, Fehler, Monitoring und Diagnoseexporte. |
| Prüfmethode | Künstliche Geheimnisse/Privattexte durch Erfolgs-, Fehler- und Debugpfade schicken; Zugriff, Ablauf und Export prüfen. |
| Abnahmekriterium | Keine verbotenen Inhalte; Zugriff nur zweckgebunden; bereinigte korrelierbare Ereignisse; abgelaufene Einträge entfernt. |
| Erforderlicher Beleg | Feldinventar, Negativscan und Retentions-/Rechteprüfung; REL-S15/Q18, SEC-14. |
| Technische Abhängigkeiten | Klassifikation, Redaktion vor Speicherung und geregelte Aufbewahrung. |
| Offene Parameter | Felder, begründete Fristen und zulässige rechtliche Reste je Nachweisart. |

### NFR-11 — Schutz über alle Speicherstufen

| Merkmal | Festlegung |
|---|---|
| Ziel | Transport, Speicherung und sensible Inhalte ihrem Schutzbedarf entsprechend sichern. |
| Geltungsbereich | Übertragung, Server, Geräte, Sicherungen und explizit freigegebene temporäre Analyse. |
| Prüfmethode | Daten-/Schlüsselwege nachvollziehen; Gerätewechsel, Schlüsselverlust, Serverzugriff und temporäre Kopien kontrolliert prüfen. |
| Abnahmekriterium | Verschlüsselung auf allen vorgesehenen Ebenen; keine privaten Klartextschlüssel am Backend; kein falsches Ende-zu-Ende-Versprechen für Serverklartextanalyse. |
| Erforderlicher Beleg | Schutz-/Schlüsselmatrix und negative Zugriffs-/Bereinigungstests; SEC-08..11/22, REL-S08/S20. |
| Technische Abhängigkeiten | Geprüfte technische Kryptokonzeption, Geräte-/Schlüsselrecovery. |
| Offene Parameter | Verfahren, Schlüsselverteilung, Rotation und Wiederherstellung technisch festlegen. |

### NFR-12 — Endgültige Löschung

| Merkmal | Festlegung |
|---|---|
| Ziel | Löschungen bleiben nach Synchronisation und Restore wirksam. |
| Geltungsbereich | Originale, Ableitungen, Historie, KI-Speicher, Index, Cache, Offlinekopien und endliche Backups. |
| Prüfmethode | Objekt/Konto löschen; alten Client und alte Sicherung einspielen; Such-/Export-/Jobpfade kontrollieren. |
| Abnahmekriterium | Kein wieder aktivierter gelöschter Inhalt; physische Bereinigung und noch bestehende rechtmäßige Backup-/Nachweisreste transparent. |
| Erforderlicher Beleg | Lebenszyklusmatrix mit Fristen, Löschmarkern und Restore-Negativfällen; S2, REL-Q16/Q20. |
| Technische Abhängigkeiten | Aktueller Kontrollstand außerhalb alter Sicherung, abgestimmte Marker-/Client-/Backupgültigkeit. |
| Offene Parameter | Lösch-/Backupfristen, Reste und Beweisverfahren; keine unbegrenzte Markeraufbewahrung voraussetzen. |

### NFR-13 — Antwort- und Ladeverhalten

| Merkmal | Festlegung |
|---|---|
| Ziel | Wartezeit vom Nutzerereignis bis nutzbarem Ergebnis messbar begrenzen. |
| Geltungsbereich | Start, Navigation, Gespräch Text/Audio, Dateivorschau, Suche, Exportstart und KI-Antwort; kalt/warm, Netz- und Gerätekategorien getrennt. |
| Prüfmethode | Referenzabläufe unter Einzel- und Parallelbetrieb messen: Ladebeginn, erste sinnvolle Rückmeldung, erste nutzbare Ausgabe und vollständiges Ergebnis einschließlich Fehlern. |
| Abnahmekriterium | Vorab bestätigte Zielwerte je Ablauf/Lastklasse erfüllt; Ausreißer und Fehlversuche ausgewiesen; Wartezustand und Abbruch verfügbar. |
| Erforderlicher Beleg | Rohmessungen, Verteilungen, Fehleranteile, Geräte-/Netzprofil und bestätigte Zielwerttabelle; REL-Q05/Q08. |
| Technische Abhängigkeiten | Frontendmessung, Backendkorrelation, Modell-/Netzkapazität. |
| Offene Parameter | Messprotokoll N1.10 anwenden; keine pauschale Millisekunden- oder Perzentilgrenze behaupten. |

### NFR-14 — Asynchrone Verarbeitung und Fairness

| Merkmal | Festlegung |
|---|---|
| Ziel | Lange Jobs blockieren weder Bedienung noch andere Konten. |
| Geltungsbereich | Import, Medienaufbereitung, Indexierung, KI-Läufe, Export, Abgleich und Bereinigung. |
| Prüfmethode | Verschiedene Jobgrößen und Konten parallel; Warteschlange füllen; Workerabbruch und Stornierung vor/nach Start prüfen. |
| Abnahmekriterium | Begrenzte Parallelität und Ressourcen; sichtbare Zustände; kein unkontrolliertes Verhungern anderer Konten; Stornierung stoppt weitere nicht bereits wirksame Arbeit. |
| Erforderlicher Beleg | Queue-/Fortschritts-/Fairnessmessung mit Zustands- und Verbrauchsbelegen; REL-Q01/Q02/Q05/Q19. |
| Technische Abhängigkeiten | Persistente Jobzustände, Rechteprüfung bei Ausführung, Deduplizierung. |
| Offene Parameter | Fairnessregel, Parallelitäts-/Warteschlangenlimits und maximale Warteziele nach Lastversuch bestätigen. |

### NFR-15 — Ressourcen und Modellverbrauch

| Merkmal | Festlegung |
|---|---|
| Ziel | V1 muss mit real nachgewiesener kostenloser Software und verfügbaren Ressourcen tragfähig sein. |
| Geltungsbereich | CPU, RAM, temporärer/persistenter Speicher, Modellkontext, Inference, Beschleuniger falls benötigt und Netzwerk. |
| Prüfmethode | Repräsentative Text-/Dokument-/Audio-/Videolasten und Modellklassen messen; Speicher-/RAM-Grenzen und Gratisangebotsausfall simulieren. |
| Abnahmekriterium | Keine unbeschränkte Ressourcenzusage; sichere Begrenzung ohne Datenverlust; keine bezahlte Ersatz-API automatisch; belegte Kapazität für bestätigte V1-Last. |
| Erforderlicher Beleg | Spitzen-/Dauerverbrauch, Durchsatz, Modell-/Lizenzfassung, Angebotsbedingungen und Engpassbericht; REL-Q01/Q02/Q03/Q15. |
| Technische Abhängigkeiten | Spätere Hardware-/Modell-/Cloudbewertung, SEC-24. |
| Offene Parameter | Lastklassen, Reserven und verfügbare Kapazität bestimmen; mangelnde Gratisinferenz bleibt Auswahlrisiko, keine neue Architekturentscheidung. |

### NFR-16 — Suche, Index, Pagination und Cache

| Merkmal | Festlegung |
|---|---|
| Ziel | Zulässige Ergebnisse korrekt und unter wachsendem Bestand nutzbar liefern. |
| Geltungsbereich | Profil, Gespräche, Lernmaterialien, Module, Projekte und pädagogische Langzeitdaten. |
| Prüfmethode | Bestände steigern; Rechte/Quellen ändern und löschen; Seitenwechsel bei parallelen Änderungen; kalte/warme Suche vergleichen. |
| Abnahmekriterium | Keine fremden/veralteten gesperrten Inhalte; definierte Sortierung, stabile bzw. nachvollziehbar aktualisierte Seiten; Index-/Cachealter und Laufzeit erfüllen bestätigte Ziele. |
| Erforderlicher Beleg | Ergebnisvergleich gegen Referenzbestand, Query-/Index-/Cachemessung und Zugriffstests; REL-Q12/Q13/Q16. |
| Technische Abhängigkeiten | Auszuwählende Speicher-/Suchtechnik, Revisionen, Cacheinvalidierung; RLS nicht vorgeschrieben. |
| Offene Parameter | Suchrelevanz, Indexaktualität, Seitengröße und Cachegültigkeit aus Bestandsmessungen bestimmen. |

### NFR-17 — Verfügbarkeit und Degradation

| Merkmal | Festlegung |
|---|---|
| Ziel | Kernfunktionen bleiben bei begrenzten Ausfällen sicher nutzbar. |
| Geltungsbereich | Zentraler Dienst, Netzwerk, Authentisierung, Modelle, Konnektoren und Sicherungen. |
| Prüfmethode | Abhängigkeiten einzeln ausfallen lassen; Überlast und Wiederkehr simulieren; kritische Nutzerwege und Monitoring beobachten. |
| Abnahmekriterium | Kein unsicherer Bypass; verfügbare eigene Daten bleiben zulässig lesbar; fehlende KI/Verbindung klar benannt; kein stiller Anbieter-/Kostenwechsel. |
| Erforderlicher Beleg | Ausfallmatrix, gemessene Ausfall-/Erholzeiten und Alarmbelege; REL-Q06/Q17/Q20. |
| Technische Abhängigkeiten | Abhängigkeitsinventar, Statusführung und Wiederanlaufkonzept. |
| Offene Parameter | Verfügbarkeitsdefinition, Beobachtungsfenster, Wartungsanteile und Wiederanlaufziele nach Risikoanalyse bestätigen. |

### NFR-18 — Verständliche Zustände und Fehlerrückmeldung

| Merkmal | Festlegung |
|---|---|
| Ziel | Nutzer erkennen Wirkung, Wartezeit und sicheren nächsten Schritt. |
| Geltungsbereich | Leer, Laden, Offline, fehlende Rechte, deaktiviert, Teilerfolg, unbekannte Wirkung, Quoten- und Modellfehler. |
| Prüfmethode | Kernabläufe mit absichtlich ausgelösten Zuständen in DE/FR/EN prüfen; verspätete/mehrfache Antworten und Entwürfe einbeziehen. |
| Abnahmekriterium | Keine falsche Erfolgsmeldung; Eingaben erhalten soweit sicher; zugängliche Rückmeldung und passende Aktion; Authfehler verraten keine Kontenexistenz. |
| Erforderlicher Beleg | Zustands-/Textmatrix und aufgabenbezogene Bedienprüfung; REL-Q04/Q05/Q06, REL-S16. |
| Technische Abhängigkeiten | Einheitliche fachliche Zustände und Übersetzungen, NFR-08. |
| Offene Parameter | Verständlichkeitsverfahren und Nutzerstichprobe vor Umsetzung festlegen. |

### NFR-19 — Barrierefreiheit als überprüfbares Ziel

| Merkmal | Festlegung |
|---|---|
| Ziel | Kernabläufe gleichwertig zugänglich gestalten. |
| Geltungsbereich | Gesamte UI einschließlich Administration, PWA-Installation, Authentisierung, Medien und Fokusmodus; WCAG 2.2 AA als zu bestätigendes Entwurfs-/Validierungsziel. |
| Prüfmethode | Automatische Hinweise plus manuelle Tastatur-, Screenreader-, Kontrast-, Zoom/Reflow-, Fokus-, Bewegungs- und Fehlerprüfungen; keine reine Scannerabnahme. |
| Abnahmekriterium | Bestätigte grundlegende Zugänglichkeit aus NFR-08 erfüllt; zusätzlich nach Zielbestätigung alle anwendbaren A-/AA-Kriterien belegt. Kein WCAG-Konformitätsanspruch ohne vollständige Prüfung. |
| Erforderlicher Beleg | Kriterien-/Seiten-/Aufgabenmatrix, manuelle Beobachtungen, Defekte und Nachprüfungen; REL-A16. |
| Technische Abhängigkeiten | Semantik, Plattform-/Assistenzmatrix, zugängliche Medienalternativen. |
| Offene Parameter | AA-Ziel und Prüfumfang ausdrücklich bestätigen; normative Quellenfassung nach REFERENZRAHMEN prüfen. |

### NFR-20 — Mehrsprachige Konsistenz

| Merkmal | Festlegung |
|---|---|
| Ziel | DE, FR und EN bieten fachlich gleiche verständliche Bedienung. |
| Geltungsbereich | UI und unabhängig gewählte KI-, Übungs- und Audiosprache; Fallback, Fehlermeldungen, Datum/Zeit/Zahlen. |
| Prüfmethode | Alle Kernzustände je Sprache, lange Texte und fehlende Übersetzung prüfen; Nutzer-/Geräte-/Inhaltssprache gegeneinander variieren. |
| Abnahmekriterium | Keine unbeabsichtigte Kopplung; keine fehlenden Schlüssel/abgeschnittenen Pflichttexte; gleiche Sicherheitsbedeutung; Fallback sichtbar. |
| Erforderlicher Beleg | Sprach-/Zustandsmatrix und fachliche Übersetzungsprüfung; FE-21, REL-Q04/Q06. |
| Technische Abhängigkeiten | Lokalisierung, Sprachmetadaten und Qualitätssicherung für Inhalte. |
| Offene Parameter | Sprachspezifische Prüfer und Bewertungsrubrik; keine automatische Gleichsetzung von Übersetzung und pädagogischer Güte. |

### NFR-21 — Belegte Erklärungen und Unsicherheit

| Merkmal | Festlegung |
|---|---|
| Ziel | Erklärungen sind nachvollziehbar; unbelegte Aussagen werden nicht als gesichert dargestellt. |
| Geltungsbereich | KI-Antworten, Zusammenfassungen, Studienvorgaben und Quellenbezüge einschließlich fehlender/widersprüchlicher Quellen. |
| Prüfmethode | Versionierter Referenzkorpus mit lösbaren, unklaren, falschen und unbeantwortbaren Fragen; Zitatstellen öffnen und Aussagebezug fachlich bewerten. |
| Abnahmekriterium | Zitate verweisen auf erlaubte tatsächliche Quelle/Fassung/Stelle; Unsicherheit und Widersprüche sichtbar; keine erfundene Quelle oder amtliche Anerkennung. Fachliche Fehlerrate muss bestätigte Rubrik erfüllen. |
| Erforderlicher Beleg | Korpusprovenienz, menschliche Bewertungen, Fehlerklassen und Gegenbeispiele; REL-A05. |
| Technische Abhängigkeiten | Quellmetadaten, berechtigte Retrievalwege, fachlich geeignete Prüfer. |
| Offene Parameter | Korpusumfang und Akzeptanzrubrik vor Evaluation bestätigen; kein erfundener Genauigkeitsprozentsatz. |

### NFR-22 — Übungen, Quiz, Korrektur und Kompetenzbelege

| Merkmal | Festlegung |
|---|---|
| Ziel | Bewertungen stützen sich auf tatsächlich gezeigte Leistung. |
| Geltungsbereich | Generierte Aufgaben, Lösungen, Rückmeldungen, Kompetenz-/ECTS-/Notenangaben und Fortschrittsableitungen. |
| Prüfmethode | Referenzaufgaben mit korrekten, falschen und teilweise richtigen Antworten; mehrdeutige/fehlerhafte Aufgaben; Vergleich unabhängiger fachlicher Bewertungen. |
| Abnahmekriterium | Aufgabe/Ziel/Lösung konsistent; Teilfehler erklärbar; manuell, bestätigt und KI-geschätzt unterscheidbar; kein Kompetenznachweis allein durch Lesedauer oder KI-Behauptung. |
| Erforderlicher Beleg | Versionierter Bewertungsmaßstab mit Quellen, Beispiellösungen, Abweichungsentscheidungen und Korrekturfolgen; REL-A18. |
| Technische Abhängigkeiten | Nachweis-/Herkunftsmodell D1/D2, zugängliche Aufgabenformate. |
| Offene Parameter | Rubrik, Prüfpersonen, Abdeckungsumfang und Toleranzen vor Produktabnahme festlegen. |

### NFR-23 — Pädagogische Anpassung

| Merkmal | Festlegung |
|---|---|
| Ziel | Anpassung reagiert nachvollziehbar auf belegte Bedürfnisse statt ungesicherte Zuschreibungen. |
| Geltungsbereich | Erklärung, Schwierigkeit, Wiederholung, Lernpräferenzen und optionale Lernheftreihenfolge L-08. |
| Prüfmethode | Unterschiedliche bestätigte/geschätzte Profile und jüngere Belege; geringe Datenlage, Ablehnung, Deaktivierung und Undo gegeneinander prüfen. |
| Abnahmekriterium | Begründung und Korrektur möglich; keine fingierten Gesundheitsdiagnosen; nur freigegebene persönliche Reihenfolge autonom, keine Kalender-/Drittanbieterwirkung. |
| Erforderlicher Beleg | Profil-/Evidenz-/Planrevisionen, Alternativvorschläge und fachliche Fallbewertung; REL-A18, AT-L08. |
| Technische Abhängigkeiten | Aktuelle Evidenz, Aktivierungszustand und Herkunft, NFR-22/24. |
| Offene Parameter | Adaptionsrubrik, Wiederholungsverfahren und Erfolgsauswertung ohne neue Produktentscheidung konkretisieren. |

### NFR-24 — Ziele, Sitzungen und Fortschrittskonsistenz

| Merkmal | Festlegung |
|---|---|
| Ziel | Lernfortschritt bleibt aus gültigen Belegen rekonstruierbar. |
| Geltungsbereich | Ziel, Sitzung, Antwort, Korrektur, Kompetenzen, Fortschritt, Hinweise und Studienvorgaben L-04/L-09. |
| Prüfmethode | Unterbrechung, Doppelabgabe, korrigierte Antwort, gelöschte Quelle, verspäteter Sync und Plan-Undo; jüngere gültige Belege vergleichen. |
| Abnahmekriterium | Keine doppelte Anrechnung; Korrektur nachvollziehbar; jüngere Belege bleiben erhalten; Kalendertermine werden nicht durch Reihenfolge-Undo geändert. |
| Erforderlicher Beleg | Durchgängige Ziel-/Sitzungs-/Ergebnis-/Evidenzspur; alle 28 AT-L-Sollfälle erhalten; REL-Q09/Q19, REL-A18. |
| Technische Abhängigkeiten | Versionierte Beziehungen und atomare fachliche Wirkungen nach D1/S2. |
| Offene Parameter | Konflikt- und Neuberechnungsregeln sowie begrenzte Historienfristen technisch prüfen. |

### NFR-25 — Wartbarkeit und reproduzierbare Qualitätsprüfung

| Merkmal | Festlegung |
|---|---|
| Ziel | Änderungen bleiben prüfbar, rückverfolgbar und sicher zurücknehmbar. |
| Geltungsbereich | Konfiguration, Software, Modelle, Prompts, Datenformate und Releaseartefakte; keine beliebige neue Funktion per Variable. |
| Prüfmethode | Gleichen Referenzsatz mit fixierten Fassungen erneut ausführen; inkompatible Konfiguration und Rückkehr zur vorherigen Fassung prüfen. |
| Abnahmekriterium | Version/Abhängigkeiten/Quelle und relevante Regressionen belegt; Rollback bewahrt heutige Rechte, Löschungen und Datenkompatibilität. |
| Erforderlicher Beleg | Änderungs-/Artefaktinventar, reproduzierbare Prüfkonfiguration und Vergleichsbericht; REL-S18, REL-A13. |
| Technische Abhängigkeiten | Versionierung, validierte Konfiguration, Migrations-/Rollbackkonzept. |
| Offene Parameter | Reproduzierbarkeitsgrenzen nichtdeterministischer Modelle und Vergleichskriterien dokumentieren; kein Stack gewählt. |

## N1.10 Messprotokoll und offene Zielwerte

1. Projektinhaber bestätigt V1-Nutzungswege, aktive Funktionen, repräsentative Kontenzahl/Parallelität und Bestands-/Datei-/Medienklassen. Synthetische oder rechtmäßig freigegebene Testdaten verwenden; keine privaten Echtdaten veröffentlichen.
2. Geräte, OS/Browser, Netz, Hardware, Region, Modell-/Softwarefassung und Angebotsgrenzen erfassen. Kalte und warme Zustände, Einzel-/Parallellast, lange Eingaben, Abbruch und Fehler getrennt messen. Ressourcenverbrauch einschließlich temporärer Kopien, Inference, Queue und Speicherwachstum erfassen.
3. Zeitmarken vom Auslösen bis Rückmeldung/Teilresultat/fertigem Ergebnis, Durchsatz, Wartezeiten, Spitzen-/Dauerverbrauch, Fehler und Ausreißer protokollieren. Verteilungen und begründet ausgewählte Quantile statt nur Mittelwerten berichten; fehlgeschlagene Versuche nicht ausblenden. Stichprobenumfang, Wiederholbarkeit und Unsicherheit ausweisen.
4. Aus Baseline, realer Kapazität, Nutzerbedarf und Ausfallfolgen Vorschläge für Latenz, Last, Quoten, Verfügbarkeit, Index-/Cachealter und Wiederherstellung ableiten. Ziele und Messfenster **vor dem Abnahmelauf** menschlich bestätigen; nicht nachträglich an schlechte Ergebnisse anpassen. Keine Zahl wird durch diese Methode bereits beschlossen.
5. Gegen bestätigte Ziele prüfen; bestanden, fehlgeschlagen, blockiert und nicht durchgeführt getrennt führen. Änderungen an Modellen, Prompts, Datenformaten, Geräten oder Kapazitäten lösen relevante Regressionen aus. Pädagogische Qualität erhält separat fachlich bestätigte Korpora und Rubriken; schnelle Antwort ist kein Gütenachweis.

Offen bleiben insbesondere Last-/Gerätematrix, Schwellen und Reserven, SLO samt Wartungsdefinition, Fristen/RPO/RTO sowie pädagogische Rubriken. Der [Referenzrahmen](../quality/REFERENZRAHMEN.md) trennt belegte Ausgaben und nicht abrufbare normative Quellen. Die [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md) ordnet alle 46 eigenständigen Kontrollen zu. Der verlinkte Freigabekatalog bleibt die Grundlage der Gates. [S3](S3-inbetriebnahme.md) ordnet sie inzwischen zukünftigen Abläufen, Verantwortungen und Belegen zu; Qualitätsziele und reale Betriebsnachweise bleiben offen.
