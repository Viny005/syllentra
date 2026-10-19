# N1 — Nichtfunktionale Anforderungen

**Projekt:** Syllentra AI\
**Version:** 0.3\
**Stand:** 19.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

## N1.1 Zweck und begrenzter Ausarbeitungsstand

Dieser Folgeaufgabenentwurf hält bereits entschiedene Qualitätsgrenzen nachvollziehbar fest. Er ersetzt weder eine ausgemessene Betriebsarchitektur noch Last-, Sicherheits- oder Barrierefreiheitstests. Zahlen, Anbieter und Messverfahren werden nicht eigenmächtig festgelegt. [S1](S1-nachbarsysteme.md) beschreibt fachliche Nachbarverträge; [N2](N2-querschnittskonzepte.md) die gemeinsamen Schutzgrenzen. N1 spezifiziert Qualität, keine Use-Case-Alternative oder interne Komponentenstruktur.

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
