# Entscheidungsabdeckung — konsolidierter Fachstand

**Projekt:** Syllentra AI\
**Version:** 0.2\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

## 1. Quelle, Kennungsgrenzen und Leseregel

Quelle ist der bestätigte Nutzerauftrag „Syllentra AI — Mission 2: Consolidation documentaire et harmonisation des décisions“, insbesondere Abschnitte 2–7, auf überprüftem Ausgangscommit `f12a46881f54dccc8568d9982bba0c41564b052e`. Das kanonische DEC-V1-Register bleibt [S2.12](S2-datenmigration.md#s212-verhalten-von-lernheft-lernprofil-und-neuer-v1-pädagogik), das 89-FE-Register [S1.18.1](S1-nachbarsysteme.md). Diese Matrix ersetzt/nummeriert keine Entscheidung und ist kein neuer Siedersleben-Produktblock. DEC-48/49 waren dort nicht vergeben und bleiben getrennt von DEC-V1 und FE.

Jede DEC-V1 besitzt genau eine Zuordnungszeile je Matrix. FE-Bezüge benennen bestehende einschlägige Grenzen, **keine Gleichsetzung oder Änderung der FE**. Neue Varianten werden innerhalb der bestehenden 66 UC und vorhandenen AF/DM/DT/DLG/BAT beschrieben. „—“ bedeutet kein eigener Batch, nicht fehlende Funktionsabdeckung. Gemeinsame Schutzkontrollen gelten zusätzlich für jeden Weg. Funktionale Nachweise sind Soll-Abnahmen, keine implementierten oder bestandenen Produkttests. Abweichende konkrete Produktentscheidungen brauchen den Projektinhaber.

## 2. Funktionale Abdeckung und zuvor fehlende Anschlüsse

| Entscheidung | Bestätigter Kurzinhalt | FE-Bezüge | UC | AF | DLG | Ergebnis der Konsolidierung |
|---|---|---|---|---|---|---|
| DEC-V1-01 | Klassische zugängliche PWA-Oberfläche | FE-19, FE-55 | UC-04, UC-23 | AF-01, AF-25 | DLG-03, DLG-27 | Vorhandene PWA-/Navigationsvorgabe; heutige Verweise ergänzt |
| DEC-V1-02 | Einfache interaktive Wissenskarte | FE-09, FE-11 | UC-08, UC-15, UC-29 | AF-03, AF-05 | DLG-13, DLG-21 | Lücke: Kartenbedienung/sekundäre Beziehungen; jetzt vorhandene Themen-/Quellenwege vertieft |
| DEC-V1-03 | Direkter Quellenpassagenzugang | FE-12, FE-51, FE-52 | UC-15, UC-16, UC-57 | AF-02, AF-03 | DLG-19, DLG-21 | Original-/Ankerweg explizit ergänzt |
| DEC-V1-04 | Vorgeschlagene und manuell gestartete Übungen | FE-03, FE-07 | UC-23, UC-24, UC-28 | AF-09, AF-10 | DLG-27, DLG-28 | Manueller Start gegenüber Empfehlung präzisiert |
| DEC-V1-05 | Adaptive Erklärungen und wählbare Alternativen | FE-03, FE-07, FE-11 | UC-23, UC-27 | AF-09, AF-21 | DLG-27, DLG-29 | Bestehende Alternativerklärung um Rückmeldungsgrenze ergänzt |
| DEC-V1-06 | Sichtbares korrigierbares Lernprofil | FE-01, FE-11, FE-13 | UC-02, UC-27, UC-49, UC-50 | AF-21, AF-22, AF-26 | DLG-05, DLG-44, DLG-49 | Sichtbarer Korrektur-/Resetumfang konkretisiert |
| DEC-V1-07 | Aktuelle geschätzte Beherrschung | FE-11, FE-16 | UC-24, UC-29, UC-43 | AF-10, AF-12, AF-23 | DLG-28, DLG-31 | Vorhandene aktuelle Evidenz-/Unsicherheitsgrenze bestätigt |
| DEC-V1-08 | Freiwillige Sitzungsrückmeldung | FE-01, FE-11 | UC-23, UC-27 | AF-09, AF-21 | DLG-27 | Lücke: freiwillige Nachsitzungsrückmeldung; jetzt UC-27/DM-28 angeschlossen |
| DEC-V1-09 | Erklärbare fächerübergreifende Bezüge | FE-09, FE-11, FE-15 | UC-08, UC-29, UC-43 | AF-05, AF-12, AF-23 | DLG-13, DLG-31 | Lücke: sekundäre fächerübergreifende Relation gegenüber Hierarchie; jetzt präzisiert |
| DEC-V1-10 | Automatische interne Lernheftordnung | FE-05, FE-08, FE-11 | UC-23, UC-30, UC-35 | AF-09, AF-13 | DLG-32, DLG-37 | L-08 bereits integriert; Modus-/Wirkungsgrenze konsolidiert |
| DEC-V1-11 | Rücknahme einer Planänderung | FE-08, FE-35 | UC-23, UC-30, UC-35 | AF-13, AF-27 | DLG-32 | L-08-Undo mit jüngerer Evidenz erhalten |
| DEC-V1-12 | Schutz manuell gesetzter Sitzungen | FE-05, FE-08, FE-47 | UC-32, UC-35, UC-37 | AF-06, AF-13 | DLG-34, DLG-37 | Bestehende Terminbestätigung erhalten |
| DEC-V1-13 | Kurze zusätzliche Wiederholung bei vermutetem Vergessen | FE-03, FE-08, FE-11 | UC-23, UC-24, UC-30 | AF-09, AF-13 | DLG-27, DLG-32 | L-08-Präzisierung ergänzt; kein erzwungener Sitzungsstart |
| DEC-V1-14 | Adaptive veränderbare Wiederholungsintervalle | FE-03, FE-11 | UC-23, UC-27, UC-30 | AF-09, AF-13 | DLG-27, DLG-32 | Vorhandene hybride Regel um bewusste Änderbarkeit präzisiert |
| DEC-V1-15 | Automatische, manuelle und hybride Priorisierung | FE-05, FE-08 | UC-30, UC-35 | AF-13 | DLG-32, DLG-37 | Manuell/automatisch/hybrid im vorhandenen Plan angeschlossen |
| DEC-V1-16 | Realistische Priorisierung bei Zeitmangel | FE-03, FE-05, FE-08 | UC-30, UC-35 | AF-09, AF-13 | DLG-32 | Vorhandenen Zeitkonflikt/Begründung konkretisiert |
| DEC-V1-17 | Tatsächlich benötigte Lerndauer | FE-11, FE-17 | UC-23, UC-29 | AF-12 | DLG-27, DLG-31 | Lücke: tatsächliche Dauer gegenüber Schätzung; jetzt Quellen-/Lückenangabe |
| DEC-V1-18 | Freiwillige diskrete Blockadehilfe | FE-03, FE-07, FE-11 | UC-23, UC-25, UC-27 | AF-09, AF-11 | DLG-27, DLG-29 | Lücke: diskretes freiwilliges Hilfsangebot/Deaktivierung; jetzt beschrieben |
| DEC-V1-19 | Vorsichtige Pausenvorschläge | FE-01, FE-03 | UC-23, UC-27 | AF-09 | DLG-27 | Lücke: vorsichtiges Pausenangebot; jetzt ablehnbar/deaktivierbar |
| DEC-V1-20 | Optionaler Konzentrationsmodus | FE-19, FE-58 | UC-23, UC-29 | AF-01, AF-25 | DLG-27, DLG-31 | L-02 bereits integriert; Nachverfolgung vervollständigt |
| DEC-V1-21 | Optionale Sitzungsbilanz | FE-11, FE-25 | UC-23, UC-29 | AF-12, AF-23 | DLG-27, DLG-31 | Lücke: optionale Sitzungsbilanz; jetzt Sicht auf reale Ergebnisse |
| DEC-V1-22 | Freiwillige Probeprüfung | FE-03, FE-07, FE-15 | UC-28, UC-29 | AF-09, AF-10, AF-12 | DLG-28, DLG-30, DLG-31 | Bestehende Simulation als freiwillige Probeprüfung konkretisiert |
| DEC-V1-23 | Prüfungs- und Trainingsmodus | FE-07, FE-15 | UC-26, UC-28, UC-29 | AF-10, AF-11, AF-12 | DLG-29, DLG-30 | Trainings-/Prüfungsmodus und Hilfenkennzeichnung konsolidiert |
| DEC-V1-24 | Begründetes persönliches Dashboard | FE-15, FE-18, FE-58 | UC-29, UC-43, UC-48 | AF-12, AF-23, AF-25 | DLG-03, DLG-31 | Bestehendes Dashboard um nachvollziehbare Datenbasis präzisiert |
| DEC-V1-25 | Freiwilliges Wochenziel | FE-01, FE-08, FE-18 | UC-23, UC-30, UC-35 | AF-09, AF-13 | DLG-03, DLG-32 | Lücke: freiwilliges Wochenziel; jetzt Wahl, Zeitraum und Wirkungsgrenze beschrieben |

### 2.1 Daten, Hintergrundverarbeitung und Schutz

| Entscheidungsbezug | DM | DT | BAT / Ausführungsgrenze | NFR | SEC |
|---|---|---|---|---|---|
| DEC-V1-01 | DM-02, DM-48 | DT-61 | —; kein eigener Batch | NFR-02, NFR-08 | SEC-04, SEC-07 |
| DEC-V1-02 | DM-09, DM-10, DM-21, DM-23 | DT-11, DT-35 | —; Ansicht ohne neuen Abruf | NFR-01, NFR-08 | SEC-04, SEC-11 |
| DEC-V1-03 | DM-20, DM-21, DM-23, DM-24 | DT-09, DT-11, DT-36 | BAT-17; nur vorher autorisierte Aufbereitung | NFR-08, NFR-11 | SEC-04, SEC-11 |
| DEC-V1-04 | DM-28, DM-29, DM-30 | DT-40, DT-42 | —; kein automatischer Übungsstart | NFR-08 | SEC-04 |
| DEC-V1-05 | DM-02, DM-28, DM-33 | DT-40, DT-45, DT-61 | —; kein neuer Hintergrundauftrag | NFR-08 | SEC-04, SEC-11 |
| DEC-V1-06 | DM-02, DM-33, DM-34, DM-48 | DT-12, DT-45, DT-61 | BAT-16; nur erlaubte Löschfolgen | NFR-01, NFR-12 | SEC-04, SEC-15 |
| DEC-V1-07 | DM-30, DM-31, DM-32, DM-33 | DT-14, DT-44, DT-45 | BAT-11; Neubewertung, kein erfundener Nachweis | NFR-08 | SEC-04, SEC-11 |
| DEC-V1-08 | DM-28, DM-02, DM-33 | DT-12, DT-44, DT-61 | —; keine erzwungene Feedbackabfrage | NFR-08, NFR-10 | SEC-04, SEC-11, SEC-15 |
| DEC-V1-09 | DM-09, DM-10, DM-14, DM-23 | DT-35, DT-56 | —; keine automatische Kompetenzübernahme | NFR-01, NFR-08 | SEC-04, SEC-11 |
| DEC-V1-10 | DM-75, DM-76, DM-35 | DT-91, DT-92 | BAT-26; BAT-09 nur Kalenderplanvorschlag | NFR-07 | SEC-04, SEC-07 |
| DEC-V1-11 | DM-75, DM-76, DM-32 | DT-54, DT-91, DT-92 | BAT-26; kein altes Gesamtbackup als Undo | NFR-07, NFR-12 | SEC-04, SEC-15 |
| DEC-V1-12 | DM-35, DM-40, DM-41 | DT-49, DT-52 | BAT-09; keine Terminwirkung durch BAT-26 | NFR-03, NFR-07 | SEC-04 |
| DEC-V1-13 | DM-10, DM-29, DM-75 | DT-40, DT-91 | BAT-26 nur aktiviert; BAT-09 bei Terminvorschlag | NFR-07, NFR-08 | SEC-04 |
| DEC-V1-14 | DM-10, DM-75, DM-76 | DT-44, DT-91, DT-92 | BAT-26 nur aktuelle aktivierte Basis | NFR-07, NFR-08 | SEC-04 |
| DEC-V1-15 | DM-75, DM-76, DM-35 | DT-91, DT-92 | BAT-26 nur im ausdrücklich aktiven Modus | NFR-03, NFR-07 | SEC-04, SEC-07 |
| DEC-V1-16 | DM-10, DM-11, DM-75 | DT-05, DT-53, DT-91 | BAT-09/BAT-26 mit getrennten Wirkungen | NFR-08 | SEC-04 |
| DEC-V1-17 | DM-28, DM-32 | DT-02, DT-05, DT-44 | —; kein zusätzlicher Telemetriejob | NFR-08, NFR-10 | SEC-04, SEC-14 |
| DEC-V1-18 | DM-02, DM-28, DM-31 | DT-14, DT-43, DT-61 | —; kein erzwungener Hilfebatch | NFR-08 | SEC-04, SEC-11 |
| DEC-V1-19 | DM-02, DM-28, DM-48 | DT-05, DT-61 | —; kein automatischer Pausenjob | NFR-08 | SEC-04 |
| DEC-V1-20 | DM-02, DM-28, DM-48 | DT-40, DT-61 | —; Fokus aktiviert keine Automatik | NFR-08 | SEC-04, SEC-07 |
| DEC-V1-21 | DM-28, DM-30, DM-31, DM-32 | DT-14, DT-44 | —; Bilanzansicht ohne neuen Analyseauftrag | NFR-08, NFR-11 | SEC-04, SEC-11 |
| DEC-V1-22 | DM-28, DM-29, DM-30, DM-31 | DT-40, DT-42, DT-43 | —; kein Start durch Plan/Restore | NFR-08 | SEC-04, SEC-11 |
| DEC-V1-23 | DM-28, DM-30, DM-31 | DT-40, DT-42, DT-43 | —; Modus ist keine Jobfreigabe | NFR-08 | SEC-04 |
| DEC-V1-24 | DM-14, DM-32, DM-48 | DT-44, DT-58, DT-61 | —; Dashboard ist kein neuer Analysejob | NFR-01, NFR-08 | SEC-04, SEC-07, SEC-11 |
| DEC-V1-25 | DM-02, DM-10, DM-48, DM-75 | DT-05, DT-44, DT-61 | —; keine Kalender-/Sitzungswirkung durch Zielwahl | NFR-08 | SEC-04, SEC-07 |

**Fundstellen:** UC-Einzelvarianten in [F2](F2-anwendungsfaelle.md), qualifizierende Funktionen in [F3](F3-anwendungsfunktionen.md), optionale Felder/Beziehungen direkt bei den genannten [D1](D1-datenmodell.md)-/[D2](D2-datentypen.md)-Definitionen und beobachtbare Aktionen in den genannten [B1](B1-dialogspezifikation.md)-Dialogen. [F1.13](F1-geschaeftsprozesse.md#f113-konsolidierte-dec-v1-varianten-ohne-neue-prozesse) führt Prozessvarianten, [B2.19](B2-batch.md#b219-ausführungsgrenzen-der-konsolidierten-dec-v1) begrenzt Hintergrundwirkung; [B3.17](B3-druckausgaben.md#b317-dec-v1-sichten-und-berichtsumfang) begrenzt Berichte. Die Tabelle bewahrt die bestätigten Schutz-/Qualitätsziele; Mission 3 vervollständigt N1/N2 fachlich, ohne technische Auswahl oder Produktfreigabe.

## 3. Prüffähige fachliche Abnahme je DEC-V1

AT-DEC-V1 bezeichnet ausschließlich lokale Soll-Prüffälle dieser Matrix, keine neuen FE oder erfolgreich ausgeführten Tests. Bestehende 28 AT-L-Fälle in E3.13 bleiben wortgleich erhalten und ergänzen diese Abdeckung.

| Lokaler Fall / Entscheidung | Gegeben / Aktion | Erwartetes Ergebnis einschließlich negativer Grenze |
|---|---|---|
| AT-DEC-V1-01 / DEC-V1-01 | Schmale Ansicht mit Tastatur bedienen | Klassische zugängliche Navigation bleibt nutzbar; weder Wissenskarte noch Audio ist Pflicht. |
| AT-DEC-V1-02 / DEC-V1-02 | Karte mit belegtem Link und fehlender Beziehung öffnen | Eigene Knoten/Links sind bedienbar und belegt; fehlende Kante wird nicht erfunden, Listenansicht bleibt erreichbar. |
| AT-DEC-V1-03 / DEC-V1-03 | Ableitung mit PDF-Seite, Audiozeit und fehlendem Anker wählen | Nur belegte Originalrevision/Position öffnen; fehlender Anker ergibt kenntliche Lücke oder Quellenrückfall, keinen erfundenen Zeitwert. |
| AT-DEC-V1-04 / DEC-V1-04 | Übungsvorschlag ablehnen und andere Übung manuell starten | Ablehnung startet nichts und bewertet nichts als falsch; tatsächlicher manueller Versuch bleibt kenntlich. |
| AT-DEC-V1-05 / DEC-V1-05 | Beispiel statt bisheriger Erklärung wünschen | Unterstützte Alternative innerhalb aktueller Rechte anbieten; keine starre Lernstilklasse oder neue Anbieterfreigabe. |
| AT-DEC-V1-06 / DEC-V1-06 | Unzutreffende Lernannahme korrigieren und nur Präferenzen zurücksetzen | Korrektur/gewählter Reset wirkt nachvollziehbar; amtliche Leistungen bleiben, gelöschte Altannahme nicht aus Schattenkopie nutzen. |
| AT-DEC-V1-07 / DEC-V1-07 | Alte Schätzung widerspricht neuer Antwort | Aktualität/Quelle und Neubewertung zeigen, weder Nullwissen noch gesicherte Kompetenz erfinden. |
| AT-DEC-V1-08 / DEC-V1-08 | Sitzungsfeedback überspringen, später freiwillig angeben/korrigieren | Kein Nachteil oder erfundener negativer Selbstbericht bei Auslassen; manuelle Herkunft/Korrektur von KI-Schätzung getrennt. |
| AT-DEC-V1-09 / DEC-V1-09 | Belegten Themenbezug zwischen zwei eigenen Kursen öffnen | Grund/Quelle/Unsicherheit sichtbar; Beziehung ersetzt keine eigene Kompetenzprüfung und erschließt kein Fremdkonto. |
| AT-DEC-V1-10 / DEC-V1-10 | Automatik an/aus und bestätigter Termin zugleich vorhanden | Nur ausdrücklich aktive pädagogische Reihenfolge darf sich ändern; Termin bleibt ohne konkrete Zustimmung unverändert. |
| AT-DEC-V1-11 / DEC-V1-11 | Nach Planänderung neue richtige Antwort, anschließend Undo | Nur gewählte Reihenfolgeänderung rücknehmen, Antwort/Fortschritt erhalten; bei manuellem Konflikt aktuelle Korrektur verlangen. |
| AT-DEC-V1-12 / DEC-V1-12 | Neue Priorität kollidiert mit manuell gesetzter Sitzung | Keine stille Verschiebung/Löschung; ausdrücklich bestätigte aktuelle Kalenderfassung erforderlich. |
| AT-DEC-V1-13 / DEC-V1-13 | Vergessen nur vermutet, kurze Wiederholung angeboten | Unsicherheit zeigen, keine sichere Wissenslücke; Wiederholung wird nicht ohne Nutzerstart ausgeführt oder ungefragt terminiert. |
| AT-DEC-V1-14 / DEC-V1-14 | Neue Evidenz oder bewusste Intervalländerung prüfen | Grundlage/Unsicherheit und neue Priorität nachvollziehbar, keine erfundene feste Formel und keine Kalenderwirkung. |
| AT-DEC-V1-15 / DEC-V1-15 | Manuelle Fixierung bei aktivierter hybrider Priorität | Fixierung respektieren, autonome Wirkung nur im erlaubten Umfang; Modus ist keine pauschale Kalenderzustimmung. |
| AT-DEC-V1-16 / DEC-V1-16 | Restzeit reicht nach verfügbaren Angaben nicht für alle Ziele | Konflikt und priorisierte Auswahl/Unsicherheit zeigen, keine unrealistische Vollplanung oder Erfolgsgarantie. |
| AT-DEC-V1-17 / DEC-V1-17 | Unterbrochene Sitzung mit nur teilweise belegter Aktivität auswerten | Nur belegbare Dauer mit Messbasis/Lücken zeigen; keine erfundene Nettozeit oder versteckte Zusatzprofilierung. |
| AT-DEC-V1-18 / DEC-V1-18 | Hilfe bei belegter Schwierigkeit anbieten, Nutzer lehnt ab | Ablehnung respektieren, weder Diagnose noch erzwungene Lösung; Häufigkeit/Schwellen bleiben offen. |
| AT-DEC-V1-19 / DEC-V1-19 | Pausenangebot ablehnen, Antwortentwurf vorhanden | Weiterarbeit/Entwurf erhalten; keine automatische Unterbrechung, Gesundheitsdiagnose oder feste neue Schwelle. |
| AT-DEC-V1-20 / DEC-V1-20 | Fokusmodus mit Tastatur aktivieren/verlassen, Antwort begonnen | Jederzeit ohne Verlust verlassen, notwendige Sicherheitshinweise erreichbar, keine Rechte- oder Automatikaktivierung. |
| AT-DEC-V1-21 / DEC-V1-21 | Bilanz mit Hilfen und fehlenden Leistungsbelegen öffnen/überspringen | Tatsächliche Ergebnisse und Unsicherheit zeigen; keine neue amtliche Note oder Analyse nur durch Ansicht. |
| AT-DEC-V1-22 / DEC-V1-22 | Simulation freiwillig starten, Hilfe verwenden | Kriterien und tatsächliche Hilfe/Antwort sichtbar; keine amtliche Note oder sichere Bestehensprognose. |
| AT-DEC-V1-23 / DEC-V1-23 | Mit Hilfe trainieren, danach Prüfungsmodus wählen | Frühere Hilfen nicht aus Ergebnis tilgen; Wechsel macht unterstützte Antwort nicht zur unabhängigen Leistung. |
| AT-DEC-V1-24 / DEC-V1-24 | Leeres/teilweise belegtes persönliches Dashboard öffnen | Unbekanntheit statt Nullkompetenz, nur eigene erlaubte Daten, keine Einzelnote in Widgets oder Vorschau. |
| AT-DEC-V1-25 / DEC-V1-25 | Wochenziel annehmen/ändern/ablehnen/aufschieben | Nur bewusste Zielwahl wirksam, keine Pflicht, keine negative Bewertung und kein Termin durch Annahme; Fortschritt braucht Beleg. |

## 4. FE-21 — Getrennte Ausgabevariante und Abnahme

FE-20 betrifft Eingabe/Sprachdialog; FE-21 betrifft gewählte Einzelwiedergabe und freiwillig eingeschalteten Hörmodus für neue zulässige Antworten, ohne Mikrofonrecht. Vorhandene Träger:

| Baustein | Konkreter Anschluss |
|---|---|
| F2 | UC-20 mit expliziter Ausgabevariante; Kommunikation und Textkontext bleiben erhalten |
| F3 | F3.14: AF-01/16/17/18/19/25/32 qualifizieren Inhalt, Fähigkeit, Anbieter, Kosten, Präferenz und Schutz |
| D1 | DM-02/48/49 persönliche Parameter; DM-25/26 Antwortfassung und temporärer Ausgabestand, keine neue Original-/Lernleistung |
| D2 | DT-07 und DT-61 für Sprache/unterstützte Parameter; D2.15 trennt Lauf/Pause/Fehler vom Gesprächsstatus |
| B1 | DLG-26 Wiedergabe und DLG-50 Einstellungen mit konkreten Typ-/Kontextbezügen |
| S1 | NB-01/NB-08 und S1.22: tatsächliche zulässige Ausgabe, keine Aufnahme-/Fremdrechte durch Hören |
| Schutz / Batch | NFR-02/08/11, SEC-04/10/11/13; kein periodischer TTS-Batch |

| Lokaler Sollfall | Aktion | Erwartetes Ergebnis |
|---|---|---|
| AT-FE21-01 | Antwort ohne Mikrofonfreigabe anhören | Erlaubte tatsächliche TTS-Fähigkeit nutzbar, keine Aufnahme oder Mikrofonpflicht |
| AT-FE21-02 | Neue Antwort ohne aktivierten Hörmodus | Keine automatische Wiedergabe; Text und manuelles Anhören verfügbar soweit berechtigt |
| AT-FE21-03 | Hörmodus ausdrücklich einschalten, neue zulässige Antwort | Wiedergabe nur im aktuellen Inhalts-/Geräte-/Anbieter-/Kostenumfang; ausschaltbar |
| AT-FE21-04 | Ausgabe pausieren, fortsetzen, erneut abspielen, unterstütztes Tempo wählen | Tatsächliche Zustände sichtbar, Text/Gespräch erhalten; keine nicht verfügbare Option vortäuschen |
| AT-FE21-05 | OS verweigert Medienstart oder TTS-Kosten nicht freigegeben | Verständlicher Fehler, Text nutzbar; kein stiller Providerwechsel, keine Ausgabe oder Mikrofonaufnahme gegen Freigabe |
| AT-FE21-06 | Inhalt gelöscht oder Recht während Pause entzogen | Keine weitere verbotene Ausgabe oder Rekonstruktion aus Audio-/Positionskopie; keine neue Lernleistung behauptet |

## 5. DEC-48 und DEC-49 — Quellen, Zuständigkeiten und Nachweise

| Entscheidung | Bestätigter Rahmen | Spezifikation / Architektur / künftiger Betrieb | Lokale Soll-Abnahme |
|---|---|---|---|
| DEC-48 | Oracle Cloud Infrastructure zuerst bewerten, Alternativen bei unzureichender Eignung; keine endgültige Auswahl | P1.10.4, P2.9.7, NFR-04/05; ADR-0004 definiert Kriterien; S3 später, hier nicht begonnen | AT-DEC48-01: Dokumentierter Vergleich deckt EU, PC-Unabhängigkeit, Kapazität, Speicher, Verfügbarkeit, Netz, Betrieb, Kosten/Gratislimits, Abrechnungsrisiken, Sicherheit, Lizenzen und Skalierung ab. Fehlender Nachweis ist offen, keine kostenfreie Eignung oder Auswahl behaupten. |
| DEC-48 | 10 EUR brutto/Monat nur Vergleichslimit, keine Ausgabe/Konto-/Infrastrukturfreigabe | ADR-0004, PACE-Projektkontext; kein Test dieses Auftrags | AT-DEC48-02: Auftrag zur Dokumentation erzeugt keinen Account, keine Ressource, Rechnung oder externe Probe. |
| DEC-49 | Verschlüsselte EU-Sicherung unabhängig vom Primäranbieter; sichere Schlüssel und begrenzte Rechte | P1.10.4, P2.9.7; UC-60, DM-69/70, DT-81, DLG-61, BAT-23, S2.19; NFR-04/11/12, SEC-08/09/14/15; ADR-0005 | AT-DEC49-01: Nur zweite Region/Konto beim Primäranbieter reicht nicht; unabhängiger Speicher/Schlüsselzugang und Integrität sind belegbar, kein Admin-Klartextschlüssel. |
| DEC-49 | Portabilität und periodische verifizierbare Wiederherstellung mit Lösch-/Retentiongrenzen | S2/N2, REL-S20/REL-Q20; künftige Betriebsverfahren in S3 | AT-DEC49-02: Restore-Proben berücksichtigen Ausfall, versehentliche Löschung, Korruption, Kompromittierung, heutigen Entzug/Löschstand und Kontentrennung. Ohne tatsächlichen Beleg nicht bestanden; RPO/RTO, Frequenz/Testintervall/Retention offen, kein Backupanbieter gewählt. |

## 6. Verbleibende Präzisierungen und Entscheidungsgrenzen

- **Nicht erneut offen:** Die 25 fachlichen DEC-V1, FE-21 sowie DEC-48/49 sind in ihrem bestätigten Rahmen zu erhalten. Neue Ausgestaltung darf sie nicht durch Annahmen ersetzen. Die hier ergänzten Zuordnungen und Details bleiben als Dokumentfassung zur Prüfung.
- **Weitere fachliche Präzisierung mit Projektinhaber:** Unterstützter Umfang einer einfachen Wissenskarte/Relationssemantik und zitierfähiger Quellenformate, konkrete messbare Lern-/Bewertungskriterien, Häufigkeit/Deaktivierung von Hilfe-/Pausenangeboten und zulässige Zeitmessbasis/Datensparsamkeit. Keine neue Schwelle, Gesundheitsinferenz, versteckte Erhebung, Pflicht oder feste Formel wurde beschlossen. Wo eine neue Produktwirkung nötig wäre, vor Änderung eine explizite Entscheidung einholen.
- **Technische Auswahl/Nachweise später:** Oracle-/Alternativvergleich, unabhängiger Backupanbieter und Rechte-/Schlüsselverfahren, tatsächliche PWA-/TTS-/OCR-/Modellfähigkeiten, Kosten und kommerziell passende Lizenzkette; Quoten, RPO/RTO, Frequenzen und Retention bleiben die vorhandenen O-S1/O-S2-Arbeiten. Keine externe Infrastrukturprobe in dieser Mission.
- **Planung:** Bestehende M2b/M5/M8-Zuordnungen bleiben unverändert. Für übrige DEC-V1 und technische Abhängigkeiten ist ein vollständiger Meilensteinplan separat zu erarbeiten; keine neuen Termine/Meilensteinnummern.
- **Abnahme:** Die Spezifikation insgesamt, konkrete Darstellungen, Typausprägungen und alle Produktnachweise bleiben zur Prüfung beziehungsweise noch auszuführen. S3 bleibt Folgeaufgabe. N1/N2 sind jetzt fachlich vervollständigt; technische Konkretisierung, Zielwertbestätigung und tatsächliche Produktprüfungen bleiben offen. FE-56 bleibt offen. REL-Q10 bleibt außerhalb V1.

## 7. Verweise

[Spezifikationsindex](README.md), [S2-Quellenregister](S2-datenmigration.md), [S1-FE-Register](S1-nachbarsysteme.md), [Prüfnachweis](E3-pruefnachweis.md), [Entwicklungszuordnungen](ENTWICKLUNGSPLAN.md), [ADR](../ARCHITECTURE_DECISIONS.md), [Release-Register](../quality/RELEASE_READINESS_40.md), [PACE-Kontext](../ai/PROJECT_CONTEXT.md).

## 8. Qualitäts- und Schutzanschluss aus Mission 3

[N1](N1-nichtfunktional.md) führt NFR-01..25 und [N2](N2-querschnittskonzepte.md) SEC-01..27 mit Prüfprofilen. Die [Kontrollmatrix](../quality/RELEASE_KONTROLLMATRIX.md) bewahrt die 40 ursprünglichen Kontrollen und ergänzt sechs eigenständige Kontrollen; [Referenzrahmen](../quality/REFERENZRAHMEN.md) und [Freigabevoraussetzungen](../quality/FREIGABEVORAUSSETZUNGEN.md) dokumentieren Quellen-/Nachweisgrenzen. Alle 25 DEC-V1- und lokalen Sollfallzeilen oben bleiben unverändert. Die Auswahl von Grenzwerten, Geräten, Verfahren, Quellen-/Bewertungsrubriken und dem WCAG-AA-Ziel benötigt menschliche Bestätigung; FE-56 bleibt offen.
