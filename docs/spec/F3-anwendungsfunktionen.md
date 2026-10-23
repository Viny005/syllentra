# F3 — Anwendungsfunktionen

**Projekt:** Syllentra AI\
**Dokument:** F3 — Anwendungsfunktionen\
**Version:** 0.7\
**Stand:** 23.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber\
**Spezifikationsmethode:** Bausteine nach Johannes Siedersleben\
**Bezugsstand:** Vier bestätigte Entscheidungen vom 19.10.2026; Ausgangs-HEAD `53ef171be4783748b5c7e3a84bb0cc363d5b4194`, Branch `docs/spec/p1-p2-mobile-workspaces`, PR #1; aktuelle Fassungen im [Index](README.md).\
**Fachlich bestätigt:** FE-01 bis FE-11; FE-10 und FE-11 werden mit diesem Entwurf erstmals in F3 beschrieben.

## F3.1 Zweck, Abgrenzung und Begriffe

F3 beschreibt wiederverwendbare **fachliche Verarbeitungsvorschriften** für die in [F2](F2-anwendungsfaelle.md) definierten Anwendungsfälle. Anwendungsfunktionen sind keine Bildschirme, REST-Endpunkte, Datenbanktabellen, Dienste, Frameworks oder vollständigen Nutzerabläufe. Die Aufnahme in F3 ist durch nachvollziehbare Auswahl-, Berechnungs-, Ableitungs-, Vergleichs- oder Konsistenzregeln begründet; bloßes Anlegen, Lesen, Ändern oder Löschen wird nicht künstlich zu einer Anwendungsfunktion erhoben. Die Abgrenzung folgt der [F3-Referenz Herold](https://github.com/carstenlucke/herold/blob/main/docs/spec/F3-anwendungsfunktionen.md) und der Methode Siedersleben.

Ein **Ausführungsvorschlag** ist eine prüfbare, noch nicht zwingend angenommene Änderung. Eine **Vorschlagsfassung** ist die konkrete, auf bestimmte Eingaben, Quelle und Zielzustand bezogene Version eines Vorschlags. Eine **Entscheidungsaktion** (annehmen, ablehnen, bearbeiten oder später prüfen) ist vom daraus resultierenden fachlichen **Entscheidungsstand** und von der tatsächlichen **Ausführung** getrennt. „Später“ lässt die Fassung offen; Bearbeiten verlangt Prüfung der aktualisierten Fassung. Es entstehen dadurch keine zusätzlichen Endentscheidungen. **Original** ist ein bewusst aufbewahrtes Dokument; **Zuordnung** ist dessen Beziehung zu einem oder mehreren Arbeitsbereichen. **Gesprächsverlauf** und **pädagogische Erinnerung** sind unterschiedliche Datensorten. Eine **vorläufige Erinnerung** ist eine zweckgebundene, kenntlich nicht abschließend bestätigte Einschätzung, keine amtliche Tatsache.

Die ursprünglichen 27 Funktionen `AF-01` bis `AF-27` sind zunächst **fachliche Entwurfskennungen**. Ihre Identität und fachliche Zuordnung bleiben über Überarbeitungen hinweg erhalten; begründete Präzisierungen werden im Änderungsnachweis festgehalten. Referenzen auf `UC-01` bis `UC-50`, `GP-01` bis `GP-15`, `FE-01` bis `FE-11` gelten als feste Quellkennungen. Verfügbare Anbieter, Tarife und Grenzen sind zum Nutzungszeitpunkt erneut zu prüfen und nicht als dauerhafte Produkteigenschaften anzunehmen. Die hier benannten Statusbegriffe sind fachliche Aussagen, keine abschließenden technischen Zustandsmodelle; die maßgeblichen F2-Regeln werden nicht durch neue Synonyme ersetzt.

### F3.1.1 Übergreifende Regeln

1. **Zweckbindung und Berechtigung vor Optimierung:** Ein fachlich nützliches Ergebnis berechtigt weder zur Nutzung einer fremden Datenquelle noch zu einer weiteren Kostenfreigabe.
2. **Keine verdeckte Handlung:** KI-Vorschläge, Hochschulimporte, Planänderungen und Archivierung werden erst entsprechend den in F1/F2 festgelegten Bestätigungsregeln ausgeführt. Bewusst manuell gespeicherte Eingaben benötigen keine zusätzliche künstliche Freigabe.
3. **Externe persönliche Kalender sind ausnahmslos lesend.** Nur der interne Studienkalender kann durch Syllentra beschrieben werden.
4. **Quellen und Erkenntnisse unterscheiden:** Amtliche Leistungsnachweise, Nutzereingaben, KI-Schätzungen und ungesicherte externe Informationen dürfen nicht gleichgesetzt werden.
5. **Mehrfachverknüpfung ist keine Vervielfältigung:** Ein gemeinsam benutztes Dokument kann mehrere Bezüge haben; Entfernen eines Bezugs löscht nicht das Original.
6. **Anbieterzugang ist keine Fähigkeitssimulation:** Ein Consumer-Abonnement, ein kostenfreier Chat und ein API-Zugang sind verschiedene Betriebsformen. Ohne erlaubte offizielle Integration ist eine direkte Ausführung in Syllentra nicht verfügbar.
7. **Datenverarbeitung bleibt korrigierbar:** Vorläufige Lern- und Kompetenzableitungen werden mit Herkunft, Aktualität und Unsicherheit geführt; Löschwünsche und Widerrufe sind zu respektieren.
8. **Fehlende oder veraltete Zustände führen zum Abbruch oder zur erneuten Prüfung**, niemals zu stillschweigender Überschreibung, blindem kostenpflichtigem Wiederholen oder erfundener Gewissheit.

## F3.2 Funktionsverzeichnis

| ID | Anwendungsfunktion | Fachlicher Algorithmuskern | Wichtige fachliche Bezüge |
|---|---|---|---|
| AF-01 | Zulässigen Daten- und Berechtigungskontext bestimmen | Zweck, Rechte, Gerät und Quellenzugriff schneiden | UC-04, UC-05, UC-18, UC-42, UC-46 |
| AF-02 | Herkunft und Verlässlichkeit bewerten | Quellenqualität, Aktualität und Widersprüche kennzeichnen | UC-03, UC-09, UC-15, UC-36, UC-44 |
| AF-03 | Aufbereitetes Lernmaterial qualifizieren | Inhalt, Extraktionslücken und Ableitungen zuordnen | UC-11, UC-15, UC-16, UC-23 |
| AF-04 | Dokumentzuordnung vorschlagen | Klassifikationskandidaten und Bestätigungsbedarf ermitteln | UC-11, UC-12, UC-13, UC-38 |
| AF-05 | Gemeinsame Ressourcenbeziehungen bewerten | Mehrfachbezug, Trennung von Relation und Original | UC-13, UC-14, UC-22, UC-40, UC-50 |
| AF-06 | Vorschlagsfassung und Entscheidung abgleichen | Versionsbezug, Freigabe und getrennte Ausführung | UC-10, UC-12, UC-35, UC-37, UC-38 |
| AF-07 | Vorschläge kontextübergreifend konsolidieren | Ein Vorschlag in allen berechtigten Ansichten | UC-12, UC-35, UC-38, UC-46 |
| AF-08 | Studienstrukturen auf Konflikte prüfen | Dubletten, Zeitbezüge und widersprüchliche Studienrelationen | UC-03, UC-06, UC-07, UC-09 |
| AF-09 | Adaptive Lernaufgabe auswählen | Ziel, Schwierigkeitsgrad, Zeitpunkt und Evidenz nutzen | UC-23, UC-24, UC-27, UC-28 |
| AF-10 | Lernantwort begründet einschätzen | Ergebnis, Unsicherheit und verwendete Hilfen trennen | UC-24, UC-25, UC-28, UC-29 |
| AF-11 | Gestufte Hilfe bestimmen | Zunächst passende Hinweise, Lösung auf Verlangen | UC-25, UC-26, UC-28 |
| AF-12 | Lernfortschritt und Wissen differenzieren | Aktivität, Schätzung, Nachweis und Note trennen | UC-09, UC-29, UC-31, UC-43 |
| AF-13 | Studienplanung und Konflikte ableiten | Fristen, Prioritäten, freie Zeit, Planvarianten | UC-30, UC-33, UC-34, UC-35, UC-37 |
| AF-14 | Quellenänderung fachlich vergleichen | Neue Fassung, widersprüchliche Quellen, Folgen | UC-36, UC-37, UC-38 |
| AF-15 | Abschluss- und Archivierungseignung prüfen | Nachweise und offene Leistungen vor Archivvorschlag | UC-06, UC-10, UC-41 |
| AF-16 | Gesprächskontext zweckgebunden bilden | Sichtbare automatische Arbeitsbereichsbindung, Quellenumfang | UC-17, UC-18, UC-19, UC-20, UC-21 |
| AF-17 | KI-Zugangswege auf tatsächliche Berechtigung prüfen | Offizieller Zugang, Gratisangebot, Abo, API, lokal unterscheiden | UC-45, UC-46, UC-47 |
| AF-18 | Geeigneten KI-Dienst und geeignetes Modell auswählen | Harte Ausschlüsse, Qualität, Kosten, Datenschutz, freie Wahl | UC-15, UC-16, UC-23, UC-24, UC-46 |
| AF-19 | Kontingent und Ausgaben begrenzen | Quota, Restbudget, Freigabe, unbekannten Verbrauch prüfen | UC-15, UC-20, UC-45, UC-46 |
| AF-20 | Anbieterfehler und Ersatzoption beurteilen | Ausfall, Rate Limit, alternative Anbieter ohne stillen Wechsel | UC-20, UC-23, UC-24, UC-46 |
| AF-21 | Vorläufige pädagogische Erinnerungen ableiten | Relevanz, Herkunft, Vertraulichkeit, Widerspruch | UC-19, UC-24, UC-27, UC-31 |
| AF-22 | Erinnerungsänderung und -korrektur auswerten | Bestätigen, korrigieren, veralten, widerrufen, löschen | UC-02, UC-19, UC-22, UC-43, UC-49, UC-50 |
| AF-23 | Kompetenznachweise gewichten | Beleggrad, eigene Leistung, offizielle und vorläufige Aussage | UC-09, UC-28, UC-31, UC-43 |
| AF-24 | Studienoptionen nachvollziehbar vergleichen | Kriterien, Quellen, Unsicherheit und Entscheidungshoheit | UC-44 |
| AF-25 | Konfiguration regelkonform prüfen | Abhängigkeiten, Grenzen, Vorschau und Wiederherstellung | UC-45, UC-46, UC-47, UC-48 |
| AF-26 | Export- und Löschfolgen ermitteln | Datenarten, Abhängigkeiten, Grenzen und Nachweisstatus | UC-14, UC-22, UC-49, UC-50 |
| AF-27 | Geräteübergreifende Änderungen abgleichen | Versionen, Berechtigungen und Konfliktauflösung | UC-04, UC-05, UC-19, UC-21, UC-38, UC-48 |
| AF-28 | Berechtigungsschnittmenge und Supportumfang bestimmen | Aktuelle Rechte und Supportfreigaben schneiden | UC-51..UC-58 |
| AF-29 | Quotenwirkung und Neuaufnahme beurteilen | Quoten und erlaubte Neuaufnahme vergleichen | UC-55, UC-59 |
| AF-30 | Funktionssichtbarkeit und Veröffentlichungsreife prüfen | Feature-, Test- und Releasezustand bewerten | UC-55 |
| AF-31 | Quellversionsunterschiede und Ableitungsbedarf bestimmen | Quellrevision und betroffene Ableitungen vergleichen | UC-57 |
| AF-32 | Schutzvererbung und Analyseumfang bestimmen | Schutzklasse und konkreten Analyseumfang prüfen | UC-58 |
| AF-33 | Sichere Archivaufnahme fachlich qualifizieren | Datei-/Archivgrenzen und Herkunft prüfen | UC-59 |
| AF-34 | Wiederherstellungsmenge gegen Löschmarkierungen abgleichen | Restoreumfang gegen aktuelle Löschkontrolle prüfen | UC-60, UC-61 |
| AF-35 | Integrationswiederaufnahme und Historie qualifizieren | Aktuelle Verbindung, Wiederaufnahme und Historie qualifizieren | UC-56 |
| AF-36 | Portabilitätspaket und Importdifferenzen prüfen | Paketprofil und versionierte Importdifferenz prüfen | UC-49, UC-64 |
| AF-37 | Studienvorgaben auf Geltung und Abdeckung prüfen | Persönliche Regelgeltung und Soll-Ist-Abdeckung prüfen | UC-66 |

## F3.3 Fachliche Funktionsbeschreibungen

### AF-01 — Zulässigen Daten- und Berechtigungskontext bestimmen

**Zweck:** Vor einer Analyse nur die für den konkreten Zweck erforderlichen und verfügbaren Daten einbeziehen.\
**Eingaben:** Nutzeridentität, berechtigter Gerätezugriff, Zweck, explizit autorisierte Quellen, aktuelle Freigaben, beteiligte Arbeitsbereiche und angeforderte Verarbeitung.\
**Ausgaben:** Erlaubter Datenumfang, ausgeschlossene Quellen samt Begründung und erforderliche weitere Freigaben.

**Verarbeitung:**

1. Zweck und Verarbeitungsschritt konkretisieren.
2. Nutzer-, Geräte-, Daten- und Anbieterrechte jeweils prüfen; die Schnittmenge bildet den maximalen erlaubten Umfang.
3. Nur relevante Ausschnitte der zugelassenen Daten auswählen.
4. Widerrufe, abgelaufene Berechtigungen und externe Nur-Lese-Grenzen anwenden.
5. Fehlende notwendige Quellen offenlegen, ohne sie durch fremde Daten zu ersetzen.

**Algorithmischer Kern und Abgrenzung:** Algorithmischer Kern ist die aufgabenbezogene Auswahl relevanter Ausschnitte aus bereits nach N2 geprüften Berechtigungen. Identitätsprüfung, Authentifizierung, technische Zugriffskontrolle und deren Durchsetzung werden hier weder implementiert noch durch eine bloße fachliche Auswahl ersetzt. Die erlaubte Auswahl darf höchstens eine Teilmenge der relevanten zugelassenen Daten sein.

**Invarianten und Fehler:** Eine aus einem Kurs gestartete Unterhaltung schafft keine Rechte an einem anderen Kurs, einem fremden Repository oder einem externen Kalender. Ein verlorenes Geräteprivileg beendet neue Zugriffe; bereits vorhandene Offline-Daten erfordern eine gesonderte Behandlung nach N2. Fremde Texte dürfen niemals selbst neue Rechte erteilen.

**Prüfbeispiel:** Eine Projektunterhaltung kann auf freigegebene Projektdateien zugreifen, aber nicht auf ein lediglich verlinktes, nicht freigegebenes privates Repository.

**Zusätzlicher Grenzfall:** Wird ein Repository nur verlinkt, aber nicht ausdrücklich ausgewählt, bleibt es ausgeschlossen. Fehlt eine optionale Profilangabe, darf daraus keine allgemeine Zugangssperre entstehen.

**Verwendung:** UC-02, UC-04, UC-05, UC-15, UC-18, UC-19, UC-20, UC-23, UC-34, UC-42, UC-45, UC-46; FE-01, FE-04, FE-09, FE-10; GP-01, GP-03, GP-04, GP-06, GP-09, GP-10, GP-11, GP-13, GP-15.

### AF-02 — Herkunft und Verlässlichkeit bewerten

**Zweck:** Aussagen nach tatsächlicher Quelle, Aktualität, Bestätigung und Widerspruchslage unterscheidbar machen.\
**Eingaben:** Aussage, Originalquelle, Beobachtungs- und Veröffentlichungsstand, Quellentyp, Bestätigungsnachweise, widersprechende Aussagen.\
**Ausgaben:** Getrennte Herkunft (Nutzereingabe, externe Originalquelle oder KI-Ableitung), Prüfstand (etwa persönlich geprüft, amtlich belegt oder unbestätigt), Zeitbezug, verfügbare Belege und offen gebliebene Konflikte.

**Verarbeitung:**

1. Auf ursprüngliche Quelle oder tatsächlich vorhandenen Nachweis zurückführen.
2. Datum, Fachkontext und Quellenzuständigkeit unterscheiden.
3. Übereinstimmung und Widersprüche prüfen.
4. Unbelegte Teile sichtbar lassen, auch wenn eine Formulierung sprachlich überzeugend ist.
5. Spätere Erkenntnisse als neue Fassung einordnen, frühere Beleglage nachvollziehbar halten.

**Algorithmischer Kern und Abgrenzung:** Herkunft, zeitliche Gültigkeit, fachliche Zuständigkeit und Bestätigung werden getrennt verglichen. Eine selbst eingegebene und vom Nutzer geprüfte Aussage bleibt als manuell erfasst erkennbar; sie wird dadurch nicht amtlich. D1/D2 legen die Datenmerkmale fest, S1 den Quellenabruf.

**Invarianten und Fehler:** Ein KI-erzeugter Prüfungsplan beweist kein amtliches Prüfungsdatum. Ein erfolgreich abgeschlossenes Kapitel begründet keine amtliche Note. Bei fehlender Primärquelle keine fiktive Quellenadresse erfinden.

**Prüfbeispiel:** Aus einer Kursfolie und einem späteren offiziellen Prüfungshinweis mit anderem Datum resultiert ein offener Konflikt mit konkreten Quellenständen, kein heimlich aktualisierter Kalendereintrag.

**Zusätzlicher Grenzfall:** Eine vom Nutzer bestätigte KI-Schätzung bleibt eine Schätzung mit tatsächlicher Prüfgrundlage. Fehlt ein amtlicher Nachweis, ist die Aussage nicht amtlich belegt; zulässige manuelle Angaben werden trotzdem nicht pauschal blockiert.

**Verwendung:** UC-03, UC-09, UC-15, UC-29, UC-31, UC-36, UC-37, UC-43, UC-44; FE-02, FE-05; GP-01, GP-02, GP-03, GP-04, GP-05, GP-06, GP-07, GP-08, GP-11.

**Präzisierung L-09:** Herkunft/Verlässlichkeit und persönliche Geltung sind verschiedene Prüfachsen. Hochschul-/Studiengangs-/Ordnungsbezug, Einschreibung/Kohorte, Inkrafttreten und Übergangsregeln ausdrücklich prüfen. Weder „hochgeladen“ noch „neuer“ beweist Vorrang. Fehlende oder widersprüchliche Geltungsmerkmale bleiben offen; die Nutzerbestätigung ersetzt keine amtliche Autorität. AF-37 führt den fachlichen Soll-Ist-Abgleich aus.

### AF-03 — Aufbereitetes Lernmaterial qualifizieren

**Zweck:** Rechtmäßig bereitgestelltes Lernmaterial in nutzbare, herkunftsbezogene Abschnitte überführen und Qualitätslücken anzeigen.\
**Eingaben:** Ausgewähltes Original, erlaubter Verarbeitungszweck, Text-/Audio-/Videoinhalte, Metadaten, verfügbare Extraktionsergebnisse.\
**Ausgaben:** Strukturierte Abschnitte, Quellenanker, erkannte Kapitel/Themen, unlesbare Stellen, vorläufige Zusammenfassungen und begrenzte Nutzungsempfehlungen.

**Verarbeitung:**

1. Eignung und Nutzungsumfang prüfen.
2. Struktur, vorhandene Seiten/Abschnitte und Medienbezüge bestimmen.
3. Extraktionsergebnisse gegen vorhandene Originalanker plausibilisieren.
4. Nicht auflösbare Teile und mögliche Fehlinterpretationen markieren.
5. Zusammenfassungen und fachliche Indexierung vom Original unterscheiden.
6. Vor nachgelagerter Verarbeitung nur autorisierte Inhalte bereitstellen.

**Algorithmischer Kern und Abgrenzung:** Eigenständiger fachlicher Kern ist die Bewertung vorhandener Extraktionsergebnisse gegen verfügbare Originalanker und Nutzungszwecke. Der externe Erkennungs- oder Generierungsalgorithmus selbst und der Aufruf eines Dienstes gehören nicht zu AF-03; Schnittstellen werden in S1 beschrieben.

**Invarianten und Fehler:** Die Funktion spezifiziert nicht das technische Format eines Transkriptionsdienstes. Ein schlechtes Transkript wird nicht als wörtlich sicher ausgegeben. Verarbeitungskopien werden nicht mit bewusst gespeicherten Originalen verwechselt.

**Prüfbeispiel:** Sind Seiten einer PDF nicht lesbar, erhält der Nutzer eine lückenhafte, gekennzeichnete Materialgrundlage statt einer erfundenen vollständigen Mitschrift.

**Zusätzlicher Grenzfall:** Ein Dienst liefert ein Transkript ohne belastbaren Anker für einen Abschnitt. Dieser Abschnitt wird als unsicher beziehungsweise nicht belegbar ausgegeben, nicht als verifizierter Originalwortlaut.

**Verwendung:** UC-11, UC-15, UC-16, UC-23, UC-42; FE-02, FE-09; GP-03, GP-04, GP-09, GP-11.

**Präzisierung DEC-V1-03:** Quellenpassagen immer an echte Originalrevision und belegten PDF-/Medienanker binden. Unbekannte Zeit/Seite nicht interpolieren; Quelle/Abschnitt oder Lücke als Rückfallweg.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-04 — Dokumentzuordnung vorschlagen

**Zweck:** Eine passende Klassifizierung vorschlagen, ohne die Entscheidung des Nutzers vorwegzunehmen (FE-02).\
**Eingaben:** Qualifizierter Inhalt, zugängliche Semester/Module/Kurse/Projekte/Themen, gegenwärtige manuelle Angaben, mögliche Zielkonflikte.\
**Ausgaben:** Begründete und als vorläufig markierte Kandidaten, Mehrfachbezüge, offen gebliebene Fälle und bestätigungsfähige Fassung.

**Verarbeitung:**

1. Zugelassene Ziele und Hinweise zum Inhalt bestimmen.
2. Fachliche Nähe und aktuelle Zielzuordnung vergleichen.
3. Mehrdeutigkeit offenlegen.
4. Einen oder mehrere Zielvorschläge bilden und begründen.
5. Nutzerbestätigung, Korrektur oder Ablehnung entgegennehmen.
6. Ausschließlich die gültige bestätigte Fassung zur endgültigen Übernahme freigeben.

**Algorithmischer Kern und Abgrenzung:** Die Klassifikationsvorschrift bestimmt zulässige Ziele, fachliche Nähe, Mehrdeutigkeit und Begründung. Die Entgegennahme einer Entscheidung ist ein F2-Ablauf; AF-06 bewertet deren gültigen Fassungsbezug. AF-04 erzeugt aus dem automatischen Gesprächskontext keine endgültige Dokumentzuordnung.

**Invarianten und Fehler:** Eine explizite manuelle Zuordnung ist bereits Nutzerentscheidung; sie darf nicht durch einen KI-Vorschlag verdrängt werden. Automatischer Gesprächskontext (FE-04) ist keine Dokumentfreigabe. Ein aufgehobener Vorschlag führt nicht zur stillen Speicherung einer Klassifizierung.

**Prüfbeispiel:** Das Skript „Datenbanken“ wird sowohl dem Kurs „Datenbanksysteme“ als auch einem Projekt vorgeschlagen. Bis zur Bestätigung bleiben beide Zuordnungen Vorschlag, nicht endgültige Ablage.

**Zusätzlicher Grenzfall:** Ein Dokument passt zu zwei Kursen, einer ist nicht mehr zugänglich. Nur erlaubte Kandidaten erscheinen; eine frühere manuelle Zuordnung bleibt erhalten, solange keine gültige gegenteilige Nutzerentscheidung vorliegt.

**Verwendung:** UC-11, UC-12, UC-13, UC-15, UC-38; FE-02, FE-08, FE-09; GP-03, GP-06, GP-07, GP-09, GP-12.

### AF-05 — Gemeinsame Ressourcenbeziehungen bewerten

**Zweck:** Mehrfachnutzung desselben Originals von Duplikaten, Beziehungen und Löschfolgen unterscheiden (FE-09).\
**Eingaben:** Identität eines aufbewahrten Originals, verknüpfte Arbeitsbereiche, beantragtes Hinzufügen/Entfernen/Löschen, Herkunftsreferenzen und Berechtigungen.\
**Ausgaben:** Zulässige Relationsänderung, betroffene Verweise, Folgenhinweis und gegebenenfalls separat zu bestätigende Originallöschung.

**Verarbeitung:**

1. Identität und Aufbewahrungsstatus des Originals prüfen.
2. Betroffene Beziehungen ermitteln.
3. Angeforderte Operation als `Beziehung hinzufügen`, `Beziehung entfernen`, `Original gesondert löschen` unterscheiden.
4. Auswirkungen auf andere Kurse, Projekte, Gespräche und Belege aufzeigen.
5. Die bewusst gewählte manuelle Relationsänderung beziehungsweise separat bestätigte erlaubte Originallöschung fachlich freigeben. Eine reine Verknüpfung erhält keine künstliche zweite Bestätigung.

**Algorithmischer Kern und Abgrenzung:** Die Funktion bewertet fachliche Identität und Abhängigkeiten geteilter Ressourcen vor einer Relationsänderung. Sie ist kein generischer Datensatzschreiber. Projekt-Modul-Bezüge betreffen AF-05 nur, soweit gemeinsam genutzte Ressourcen oder Nachweisbeziehungen tatsächlich berührt werden. Konkrete Kardinalitäten bleiben D1 vorbehalten.

**Invarianten und Fehler:** Entkopplung löscht keine Datei. Nicht vorhandene Zuordnung rechtfertigt keine Veränderung anderer Links. Bei tatsächlicher Originallöschung bleiben fehlende Quellenhinweise als solche kenntlich und unabhängige Daten werden nur im ausdrücklich gewählten Umfang bearbeitet.

**Prüfbeispiel:** Entfernt der Nutzer die Zuordnung eines PDF zu Modul A, bleibt dasselbe Original über Projekt B verfügbar; seine Herkunft und andere Bezüge bleiben unverändert.

**Zusätzlicher Grenzfall:** Auch nach Entfernung des letzten Kurslinks bleibt ein bewusst dauerhaftes Original erhalten. Die gleiche Operation erneut zu prüfen darf keine anderen Beziehungen oder das Original verändern.

**Verwendung:** UC-07, UC-13, UC-14, UC-21, UC-22, UC-39, UC-40, UC-50; FE-09; GP-02, GP-03, GP-09, GP-10, GP-15.

**Präzisierung DEC-V1-02/09:** Für die einfache Wissenskarte bestehende eigene Themen-/Lernziel-/Quellenbezüge qualifizieren. Grund, Herkunft, Unsicherheit und Zugriffsrecht je fachlichem Bezug prüfen; kein erfundener Fachbezug oder automatischer Kompetenztransfer. Hierarchiekante und fächerübergreifende Relation nicht verwechseln.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-06 — Vorschlagsfassung und Entscheidung abgleichen

**Zweck:** Eine konkrete Vorschlagsfassung genau einer kohärenten fachlichen Entscheidung zuordnen, die von der Ausführung getrennt bleibt.\
**Eingaben:** Vorschlagskennung, Fassung, ursprüngliche Daten/Quellen, Zielzustand, Nutzerentscheidung, aktueller Berechtigungs- und Quellenstand.\
**Ausgaben:** Versionsbezogener Entscheidungsstand nach F2.11.1 (`Offen`, `Angenommen`, `Abgelehnt`, `Gegenstand entfallen`) und davon getrennter Ausführungsstand (`Nicht übernommen`, `Übernahme läuft`, `Übernommen`, `Teilweise übernommen oder fehlgeschlagen`, `Ergebnis unklar`). „Später“ bleibt `Offen`; eine neue Fassung wird erneut offen geprüft, ohne die historische Entscheidung umzuschreiben.

**Verarbeitung:**

1. Version und Zielzustand des Vorschlags bestimmen.
2. Zwischenzeitliche Quell-/Ziel-/Rechteänderungen feststellen.
3. Eine Entscheidung ausschließlich gegen die dem Nutzer gezeigte konkrete Fassung prüfen.
4. Gleichzeitige Entscheidungen für dieselbe Fassung konsistent zusammenführen.
5. Bei Annahme die fachlich zulässige einmalige Wirkung bestimmen beziehungsweise einen bereits bekannten Ausführungsstand berücksichtigen; die tatsächliche Ausführung erfolgt im jeweiligen Anwendungsfall.
6. Scheitern nicht als Ablehnung, Annahme nicht als bereits erfolgreiche Ausführung ausgeben.

**Algorithmischer Kern und Abgrenzung:** Verglichen werden angezeigte Fassung, aktuelle Grundlage, bereits getroffene Entscheidung und bekannte Wirkung. Das Ergebnis ist eine fachliche Übernahme- oder Sperrbeurteilung. Speicherung, technische Gleichzeitigkeitssicherung und konkrete Zustandsdefinitionen gehören nach D1/D2 und N2; die F2-Begriffe bleiben unverändert.

**Invarianten und Fehler:** `Später` ist keine Ablehnung. Eine geänderte Fassung benötigt neue Prüfung. Wiederholtes Klicken oder Synchronisieren darf kein zweites Dokument, keinen zweiten Termin und keinen zweiten kostenpflichtigen Auftrag erzeugen. Ein unbekannter externer Ausführungsstatus verlangt Klärung statt blindem Wiederholen.

**Prüfbeispiel:** Ein in der Kursansicht abgelehnter Prüfungstermin-Vorschlag ist in der zentralen Ansicht ebenfalls abgelehnt; die ältere offene Ansicht auf Gerät B darf keine widersprüchliche Annahme verarbeiten.

**Zusätzlicher Grenzfall:** Ein Vorschlag ist angenommen, die Übernahme aber nur teilweise gelungen. Alle Ansichten zeigen dieselbe Annahme mit Teilfehler; „Später“ erzeugt keinen eigenen Endzustand und ein erneuter Klick keine zweite Wirkung.

**Verwendung:** UC-03, UC-07, UC-08, UC-09, UC-10, UC-12, UC-13, UC-16, UC-30, UC-33, UC-35, UC-37, UC-38, UC-41, UC-44, UC-46, UC-48, UC-50; FE-02, FE-05, FE-06, FE-08; GP-01, GP-02, GP-03, GP-04, GP-05, GP-06, GP-07, GP-08, GP-09, GP-11, GP-12, GP-13, GP-14, GP-15.

### AF-07 — Vorschläge kontextübergreifend konsolidieren

**Zweck:** Einen fachlichen Vorschlag zugleich zentral und im jeweiligen Arbeitsbereich anzeigen, ohne zwei unabhängige Entscheidungen zu erzeugen (FE-08).\
**Eingaben:** Berechtigte offene und entschiedene Vorschläge, Fachbezüge, Sichtbarkeit, Fassung und aktueller Entscheidungs-/Ausführungsstand.\
**Ausgaben:** Einheitliche, gefilterte Vorschlagsübersichten für „Zu prüfen“, Kurs-, Projekt-, Semester- und Kalenderkontext.

**Verarbeitung:**

1. Zugängliche Vorschläge nach Identität und Fassung konsolidieren.
2. Betroffene Fachbezüge ohne Duplizierung ermitteln.
3. Status, Quelle und Folgen in jeder Ansicht aus derselben fachlichen Entscheidung ableiten.
4. Nicht berechtigte Vorschläge ausblenden, ohne Zugriffsrechte durch die Übersicht zu verändern.
5. Nach Entscheidung oder Ausführung alle Ansichten auf denselben erkennbaren Stand bringen.

**Algorithmischer Kern und Abgrenzung:** Konsolidierung erfolgt nach fachlicher Vorschlagsidentität und Fassung, nicht nach gleichlautendem Titel. Der Algorithmus bewertet Bezüge, Berechtigungen und Aktualität einer gemeinsamen Aussage; Sortierung und Bildschirmgestaltung allein sind kein Algorithmuskern und bleiben B1.

**Invarianten und Fehler:** Ein Vorschlag mit mehreren Bezügen bleibt derselbe Vorschlag. Reine Nachrichten ohne anstehende Nutzerentscheidung werden nicht zwanghaft als zu bestätigende Vorschläge geführt. Eine veraltete Offline-Ansicht muss ihren letzten bekannten Stand als veraltet oder unklar ausweisen; sie darf ihn weder als aktuell gesichert behaupten noch eine neue widersprüchliche Entscheidung autorisieren.

**Prüfbeispiel:** Ein Kursdokument mit Projektbezug erscheint zentral und in beiden Kontexten; die Bestätigung aktualisiert denselben Eintrag und löst genau eine endgültige Zuordnung aus.

**Zusätzlicher Grenzfall:** Zwei unterschiedliche Vorschläge besitzen denselben Titel: Sie werden nicht verschmolzen. Derselbe Vorschlag mit zwei Kontextbezügen besitzt dagegen weiterhin nur eine Entscheidung zur aktuellen Fassung.

**Verwendung:** UC-03, UC-07, UC-08, UC-09, UC-10, UC-12, UC-13, UC-16, UC-30, UC-33, UC-35, UC-37, UC-38, UC-41, UC-44, UC-46, UC-48, UC-50; FE-08; GP-01, GP-02, GP-03, GP-04, GP-05, GP-06, GP-07, GP-08, GP-09, GP-11, GP-12, GP-13, GP-14, GP-15.

### AF-08 — Studienstrukturen auf Konflikte prüfen

**Zweck:** Gleichartige und widersprüchliche Semester-, Modul- und Leistungsangaben vor einer fachlichen Zusammenführung kenntlich machen.\
**Eingaben:** Semester, Module, Kurse, Themen, Leistungsnachweise, Beziehungen, vorhandene Zuordnungen und Herkunft.\
**Ausgaben:** Plausibilitäts- und Dublettenhinweise, mögliche Zuordnungen und offen zu klärende Konflikte.

**Verarbeitung:**

1. Fachliche Identität und Zeitraum vergleichen.
2. Gleichnamige, aber verschiedene Kurse von tatsächlichen Dubletten unterscheiden.
3. Semester- und Modulbeziehungen auf unbeabsichtigte Konflikte prüfen.
4. Offizielle und persönliche Studieninformationen nicht still zusammenführen.
5. Bewusste manuelle Eingabe oder bestätigte importierte Korrektur zugrunde legen.

**Algorithmischer Kern und Abgrenzung:** Verglichen werden Studienidentität, Zeitbezug und Beleglage. Eine einfache Eingabevalidierung ohne fachlichen Vergleich ist kein eigener F3-Algorithmus; Formate und allgemeine Validierungsverfahren gehören D2/N2. Fehlende optionale Profilfelder sind kein Strukturkonflikt.

**Invarianten und Fehler:** Ein Modul darf in mehr als einem Studienabschnitt auftreten, wenn dies fachlich begründet ist. Wiederholungsprüfungen bleiben vom ersten Prüfungstermin unterscheidbar. Nicht bestätigte ECTS und Noten gelten nicht als amtlich anerkannt.

**Prüfbeispiel:** „Big Data“ aus zwei Semestern erzeugt zunächst einen Identitätshinweis und überschreibt nicht automatisch ältere Vorlesungsunterlagen oder Ergebnisse.

**Zusätzlicher Grenzfall:** Eine Wiederholungsprüfung liegt im folgenden Semester. Sie bleibt als offene eigenständige Verpflichtung erkennbar und wird weder mit dem ersten Versuch zusammengelegt noch allein wegen des Semesterwechsels geschlossen.

**Verwendung:** UC-03, UC-06, UC-07, UC-08, UC-09, UC-10, UC-33; FE-01, FE-08; GP-01, GP-02, GP-04, GP-06, GP-11, GP-12.

### AF-09 — Adaptive Lernaufgabe auswählen

**Zweck:** Eine geeignete nächste Erklärung, Frage oder Übung anhand von Ziel, Evidenz, Schwierigkeit und Belastung bestimmen (FE-03).\
**Eingaben:** Lernziel, Themenstruktur, verfügbarer Wissensstand, Antwortverlauf mit Hilfen, Nutzerpräferenzen, aktuelle Rückmeldung.\
**Ausgaben:** Begründete Empfehlung für Inhalt, Methode, Schwierigkeit und Zeitpunkt des nächsten Lernschritts.

**Verarbeitung:**

1. Aktuelles Lernziel und verfügbare fachliche Grundlage ermitteln.
2. Unsicherheiten und Wissenslücken priorisieren.
3. Geeignete Darstellungs- und Aufgabenarten vergleichen.
4. Unterstützungsgrad und letzten Antwortverlauf berücksichtigen.
5. Verständnisprüfung in einer für den Lernfluss geeigneten Situation anbieten, nicht nach starrem Absatz- oder Zeitraster.
6. Aus neuem Feedback die nächste Auswahl aktualisieren.

**Algorithmischer Kern und Abgrenzung:** Die Auswahl nutzt nur freigegebene fachliche Evidenz und unmittelbare Lernrückmeldung. Sie bestimmt weder unbelegte psychologische Eigenschaften noch allgemeine Leistungsfähigkeit. In einer gewählten Simulation sind deren erklärte Bedingungen zu berücksichtigen; die adaptive Begleitung verändert sie nicht heimlich.

**Invarianten und Fehler:** Eine richtige Antwort nach vollständiger Lösung ist schwächerer Beleg als eine selbstständig hergeleitete Antwort. Ohne ausreichende Evidenz ist die Schwierigkeit nur eine vorläufige Wahl. Die Funktion erzwingt keine Frage nach jeder Erklärung.

**Prüfbeispiel:** Nach wiederholten Fehlern bei SQL-JOIN-Aufgaben bietet Syllentra ein kleineres Beispiel und erst danach eine passend anspruchsvollere Aufgabe an, statt das nächste Kapitel mechanisch freizuschalten.

**Zusätzlicher Grenzfall:** Eine einzelne missverständliche Antwort reicht nicht für einen dauerhaften Schwächenstatus. Fehlt verlässliche Evidenz, bleibt die nächste Aufgabenwahl vorläufig und kann nach Nutzerkorrektur angepasst werden.

**Verwendung:** UC-23, UC-24, UC-27, UC-28, UC-30; FE-03, FE-07, FE-11; GP-04, GP-05, GP-06.

**Präzisierung L-08:** Regelbasierte zeitliche Wiederholung und adaptive Auswahl werden kombiniert. Lernziele/Konzepte/Themen/Kapitel, tatsächliche Antworten mit Hilfen, Schwierigkeiten, Prüfungsnähe, freie Lernzeit, abgeschlossene/verpasste Wiederholungen und Qualität/Aktualität der Evidenz sind nachvollziehbare Eingaben. Wiederholte Schwierigkeiten führen zu alternativen Erklärungen und geeigneten Übungen. Fehlende Evidenz bleibt unsicher; Versäumnis allein ist kein Wissensdefizit. Konkrete Wiederholungsformel, Gewichtungen und Wirksamkeitsnachweis bleiben zur Evaluation offen. Eine reine Reihenfolgeänderung unter aktivierter Automatik ist von einem Kalenderplan nach AF-13 getrennt; sie nutzt DM-75/DM-76 und DT-91/DT-92.

**Präzisierung DEC-V1-04/05/18/19:** Freiwillige manuelle Übung und vorgeschlagene Übung unterscheiden. Alternative Erklärungen und diskrete Hilfe/Pausen nur auf vorhandener zulässiger Grundlage anbieten; keine erzwungene Sitzung, Diagnose oder erfundene Ablehnungsevidenz. Häufigkeit/Schwellen bleiben offen.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-10 — Lernantwort begründet einschätzen

**Zweck:** Antworten anhand einer vorhandenen Aufgaben- und Bewertungsgrundlage nachvollziehbar beurteilen, einschließlich Unsicherheit und Hilfegrad.\
**Eingaben:** Aufgabe, verfügbare Lösungskriterien, Nutzerantwort, zugelassene Quellen, frühere Hilfen und Simulationsmodus.\
**Ausgaben:** Feedback mit begründeten Treffern, Fehlern, unklaren Punkten, Hilfestufe und vorläufiger Wissenseinschätzung.

**Verarbeitung:**

1. Prüfbarkeit der Aufgabe und Bewertungsgrundlage feststellen.
2. Antwort und nachvollziehbare Teilergebnisse vergleichen.
3. Fachliche Fehler von missverständlicher Formulierung unterscheiden.
4. Bereits verwendete Hinweise und Lösungen berücksichtigen.
5. Nur so weit urteilen, wie Quellen und Kriterien reichen; gegebenenfalls um Klärung bitten.

**Algorithmischer Kern und Abgrenzung:** Beurteilt werden fachlicher Gehalt, vorhandene Lösungskriterien und bekannte Hilfen, nicht bloß sprachliche Ähnlichkeit. Die Auswertung erzeugt keine amtliche Benotung. Ist der Hilfeverlauf unbekannt, ist „Hilfeumfang unbekannt“ zu kennzeichnen statt unabhängigen Erfolg anzunehmen.

**Invarianten und Fehler:** Sprachlich plausible Antworten sind nicht automatisch richtig. Ein unsicheres Bewertungsergebnis wird nicht als sichere Note oder offizieller Nachweis ausgegeben. Hilfe- und Bewertungsverlauf bleibt unterscheidbar.

**Prüfbeispiel:** Zwei mathematisch äquivalente Lösungswege werden akzeptiert, sofern die verfügbaren Kriterien dies tragen; bei unklarer Aufgabenstellung erscheint ein begründeter Unsicherheitshinweis.

**Zusätzlicher Grenzfall:** Die Musterlösung ist unvollständig und die Antwort auf anderem Weg plausibel. Ohne tragfähige Kriterien bleibt die Bewertung offen; der Nutzer erhält keine erfundene Fehlerdiagnose oder sichere Note.

**Verwendung:** UC-24, UC-25, UC-28, UC-29, UC-31; FE-03, FE-07; GP-04, GP-05, GP-11.

### AF-11 — Gestufte Hilfe bestimmen

**Zweck:** Lernende zuerst durch geeignete Hinweise unterstützen, ihnen aber eine ausdrücklich angeforderte vollständige Lösung nicht unnötig vorenthalten (FE-07).\
**Eingaben:** Aufgabe, erkennbarer Fehler, bisherige Hinweise, neue Lösungsversuche, ausdrücklicher Hilfewunsch, Simulationsregeln.\
**Ausgaben:** Fachlich passender Hinweis, weiterer Hilfeschritt oder vollständiger nachvollziehbarer Lösungsweg samt Hilfegrad.

**Verarbeitung:**

1. Ausdrücklichen Hilfewunsch zuerst prüfen: Bei vollständiger Lösungsanforderung und tragfähiger Grundlage direkt Schritt 5 verwenden; andernfalls Fehler oder Wissenslücke mit AF-10 eingrenzen.
2. Eine möglichst kleine zielführende Hilfestellung auswählen.
3. Neuen selbstständigen Versuch ermöglichen und auswerten.
4. Bei Bedarf Unterstützung gezielt vertiefen, nicht in festen Stufen zwanghaft abarbeiten.
5. Bei ausdrücklichem Lösungswunsch den vollständigen Lösungsweg liefern, sofern eine belastbare Grundlage existiert.
6. Tatsächlich genutzte Hilfe in der Leistungsinterpretation kennzeichnen.

**Algorithmischer Kern und Abgrenzung:** Die Auswahl des nächsten hilfreichen Eingriffs ist algorithmisch; der Dialog zum Anfordern gehört F2/B1. Ein ausdrücklicher Wunsch nach vollständiger Lösung wird vor obligatorischen Hinweisrunden berücksichtigt. Tatsächlich gezeigte Hilfe bleibt bei späterer Leistungsinterpretation erhalten.

**Invarianten und Fehler:** Direkte Lösungsanforderung überspringt Hinweisrunden. Fehlt die Grundlage für eine korrekte Lösung, wird Unsicherheit angegeben statt eine sichere Musterlösung zu behaupten. Hilfe darf keine falsche selbstständige Leistung erzeugen.

**Prüfbeispiel:** Nach falscher Vorzeichenumformung erhält der Nutzer zuerst einen Hinweis auf diese Zeile. Auf „Zeige mir die Lösung“ folgt unmittelbar die vollständige Erklärung, anschließend ist die Aufgabe als mit Hilfe bearbeitet kenntlich.

**Zusätzlicher Grenzfall:** Der Nutzer verlangt die vollständige Lösung ohne vorherigen Lösungsversuch. Bei ausreichender fachlicher Grundlage folgt der Lösungsweg direkt; erst einen Versuch oder alle Hinweise abzuverlangen wäre unzulässig.

**Verwendung:** UC-24, UC-25, UC-26, UC-28, UC-29; FE-07; GP-04, GP-05, GP-11.

### AF-12 — Lernfortschritt und Wissen differenzieren

**Zweck:** Bearbeitung, Verständnis, tatsächliche Nachweise und offizielle Leistungen fachlich getrennt bewerten.\
**Eingaben:** Bearbeitete Kapitel, Antworten mit Hilfestufen, Übungen, bestätigte Ergebnisse, Noten, ECTS, Kompetenzeinschätzungen.\
**Ausgaben:** Getrennte Indikatoren für Aktivität, vorläufiges Wissen, dokumentierte Kompetenz und amtliche Leistung; Beleg- und Zeitbezug.

**Verarbeitung:**

1. Daten nach Belegtyp gruppieren.
2. Eigenständige und unterstützte Lösungsversuche unterscheiden.
3. Wissenseinschätzungen nur aus vorhandener passender Evidenz ableiten.
4. Amtliche Noten/ECTS separat kennzeichnen.
5. Unbekanntes nicht durch Null oder erfundene Sicherheit ersetzen.
6. Neue Antworten unter Beibehaltung der bisherigen Herkunft berücksichtigen.

**Algorithmischer Kern und Abgrenzung:** Die Funktion ordnet Beobachtungen verschiedenen Aussagearten zu und begrenzt deren zulässige Interpretation. Sie berechnet keine unbegründete einheitliche Erfolgszahl aus Aktivität, Note und KI-Einschätzung. Anzeige und Persistierung der getrennten Werte sind keine zusätzlichen AF.

**Invarianten und Fehler:** „Kapitel gelesen“ bedeutet nicht „Kapitel beherrscht“. Eine KI-Schätzung ist keine amtliche Note. Eine archivierte Tätigkeit verliert nicht ihre historischen Nachweise, sofern keine bestätigte Datenlöschung erfolgt.

**Prüfbeispiel:** Bei 100 % gelesenen Folien und keiner beantworteten Aufgabe wird 100 % Bearbeitungsfortschritt möglich, aber nicht 100 % gesichertes Wissen.

**Zusätzlicher Grenzfall:** Eine mit vollständiger Lösungshilfe beantwortete Aufgabe bleibt als bearbeitet sichtbar, zählt aber nicht als unabhängig richtiger Simulationsnachweis. „Unbekannter Wissensstand“ ist nicht mit einer amtlichen Nullleistung gleichzusetzen.

**Verwendung:** UC-09, UC-24, UC-28, UC-29, UC-31, UC-43; FE-07, FE-11; GP-02, GP-04, GP-05, GP-11.

**Präzisierung L-02/L-08:** Bearbeitet, Verständnis überprüft, Wissensstand geschätzt und Kompetenz nachgewiesen getrennt führen; aus Lesen oder erledigter Wiederholung folgt keine sichere Beherrschung. Eigenständigkeit/Hilfen und zeitliche Evidenzbasis bleiben sichtbar. Undo der pädagogischen Reihenfolge verändert keine jüngeren gültigen Lernfortschritte. Ein ablenkungsarmer oder bewegungsreduzierter Modus darf weder Kategorien zusammenlegen noch zur Sicherung des Fortschritts zuerst beendet werden.

**Präzisierung DEC-V1-07/17/21/22/23:** Bilanz nur aus tatsächlichen eigenen Ergebnissen/Antworten/Hilfen bilden. Beobachtete Lerndauer, Schätzung und unbekannte Zeit getrennt; keine versteckte neue Telemetrie, Erfolgsquote oder amtliche Note. Trainingshilfe ist keine selbstständige Prüfungsantwort.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-13 — Studienplanung und Konflikte ableiten

**Zweck:** Studien-, Prüfungs- und Projektarbeit als überprüfbaren Vorschlag unter Beachtung verfügbarer Zeitfenster planen.\
**Eingaben:** Termine und Fristen, Lernbedarf, Ziele, Prioritäten, Zeiträume aus internem Kalender, ausdrücklich lesend erlaubte externe Verfügbarkeit, Zeitzonen und Unsicherheit.\
**Ausgaben:** Konflikthinweise, begründete interne Planvorschläge und alternative Lernzeitfenster.

**Verarbeitung:**

1. Termine, Zeitzonen und belegte Zeiträume normalisieren.
2. Überlappung, verfügbare Zeit und Abhängigkeiten bestimmen.
3. Umfang und Dringlichkeit der Aufgaben unter Unsicherheit gewichten.
4. Gegebenenfalls mehrere realistische Planvarianten bilden.
5. Quellenstand und Konflikte anzeigen.
6. Den vollständigen KI- oder Importvorschlag mit seinen Konflikten an AF-06 übergeben; eine Übernahmefreigabe setzt dessen gültige Nutzerentscheidung voraus. Manuelle Nutzererfassung bleibt separat direkt möglich; eine bewusst gewählte zeitliche Überschneidung wird kenntlich, aber nicht pauschal verboten.

**Algorithmischer Kern und Abgrenzung:** Der fachliche Kern ist der Abgleich von Zeitfenstern, Bedarf, Fristen, Abhängigkeiten und Unsicherheit. Die Funktion schreibt keinen Kalender und realisiert keinen Kalenderdienst. Nur Vorschlagsübernahme braucht AF-06; bewusst manuelle Eingaben nutzen gegebenenfalls die Konfliktprüfung ohne künstliche zweite Freigabe.

**Invarianten und Fehler:** Externe Kalender werden auch bei Einwilligung niemals beschrieben. Eine vom Nutzer nicht bestätigte importierte oder KI-geplante Änderung bleibt Vorschlag. Fehlt externer Kalenderzugriff, kann der Nutzer die Verfügbarkeit selbst angeben. Historische Planung wird nicht bei fehlenden Daten still überschrieben.

**Prüfbeispiel:** Ein Dienst am Samstag blockiert einen vorgeschlagenen Lernzeitraum; Syllentra schlägt Sonntag vor. Erst die Bestätigung schreibt den internen Studienkalender fort.

**Zusätzlicher Grenzfall:** Bei gescheitertem Kalenderabruf gilt das Zeitfenster nicht automatisch als frei. Der Plan nennt den fehlenden Stand und kann zulässige manuelle Verfügbarkeit berücksichtigen; externe Ereignisse bleiben unverändert.

**Verwendung:** UC-30, UC-32, UC-33, UC-34, UC-35, UC-37, UC-41; FE-05, FE-08; GP-02, GP-05, GP-06, GP-07, GP-09.

**Präzisierung L-08:** Automatisch begründete pädagogische Priorität in DM-75 verändert ausschließlich die Reihenfolge. Manuelle Fixierungen und bereits bestätigte DM-35-Termine begrenzen jeden Kalenderplan; dessen Verschiebung/Löschung verlangt weiterhin die erforderliche aktuelle Zustimmung. Ein Konflikt erzeugt einen prüfbaren Vorschlag, keine Termineingabe durch Nebenwirkung. AF-06/UC-35/BAT-09 bleiben maßgeblich. L-04/UC-65 verwenden nur aktuell wirksame Ereignis-/Regelfassungen für Erinnerungspunkte.

**Präzisierung DEC-V1-14/15/16/25:** Gewählte manuelle/automatische/hybride pädagogische Priorisierung und verfügbare Zeit berücksichtigen. Wochenziel nur vorschlagen, bewusste Annahme/Änderung/Ablehnung/Aufschub respektieren. Ziel ist kein Termin oder Lernstart; Konflikte bei Zeitmangel ausweisen, keine erfundene Machbarkeit. Kalenderänderung nur über bestehenden Bestätigungsweg.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-14 — Quellenänderung fachlich vergleichen

**Zweck:** Relevante Änderungen und widersprüchliche Quellenstände erkennen, ohne einen externen Vorgang zu fingieren.\
**Eingaben:** Frühere bekannte Quellenfassung, neu erlaubter Quellenstand, Aktualität, Zuständigkeit, vorhandene interne Ziele und Termine.\
**Ausgaben:** Änderungsbefund, Quellenbeleg, Unsicherheit, möglicherweise betroffene Studienaufgaben und ein optionaler Folgevorschlag.

**Verarbeitung:**

1. Quellidentität und Versionsstand vergleichen.
2. Inhaltliche Unterschiede von reinen Formatänderungen unterscheiden.
3. Zuständigkeit, zeitliche Gültigkeit und widersprechende Informationen prüfen.
4. Betroffene Prüfungs-, Abgabe- oder Lernpläne ermitteln.
5. Informationen unverbindlich anzeigen; echte Plananpassungen als gesonderte Vorschlagsfassung an AF-06/AF-13 übergeben.

**Algorithmischer Kern und Abgrenzung:** Die Änderungserkennung bewertet fachliche Unterschiede und mögliche Konsequenzen aus bereits zulässig vorliegenden Quellenfassungen. Abruf und Benachrichtigungszustellung gehören S1 beziehungsweise B2; Anzeige eines Hinweises ist noch keine freigegebene Planänderung.

**Invarianten und Fehler:** Fehlgeschlagene Quellenabfrage ist kein Beleg „keine Änderung“. Ein unbelegtes Forum-Gerücht überschreibt kein offizielles Prüfungsdatum. Eine neue Quellversion kann bisherige offene Vorschläge prüfbedürftig machen.

**Prüfbeispiel:** Der Fachbereich veröffentlicht eine neue Klausurzeit. Syllentra weist Quelle und Änderung aus, markiert kollidierende Lernzeiten und verlangt vor einer internen Umplanung eine Bestätigung.

**Zusätzlicher Grenzfall:** Nur die Formatierung einer Mitteilung ändert sich. Daraus entsteht keine vermeintliche Prüfungsverschiebung. Bei tatsächlich widersprüchlichen Terminen bleiben Quelle, Aktualität und Unsicherheit sichtbar.

**Verwendung:** UC-36, UC-37, UC-38, UC-44; FE-05, FE-08; GP-03, GP-06, GP-07, GP-08, GP-12.

### AF-15 — Abschluss- und Archivierungseignung prüfen

**Zweck:** Fachlich abgeschlossene Elemente von weiterhin aktiver oder ungeklärter Semesterarbeit unterscheiden (FE-06).\
**Eingaben:** Semesterstatus, Module, Wiederholungsprüfungen, Abgaben, laufende Projekte, nachgewiesener Abschluss, abhängige Beziehungen.\
**Ausgaben:** Begründete Liste archivierbarer Elemente, offene/unklare Elemente, nötige Nutzerentscheidungen und Auswirkungsübersicht.

**Verarbeitung:**

1. Offizielle und persönliche Abschlussinformationen mit AF-02 prüfen.
2. Jede relevante Prüfung, Abgabe und Projektabhängigkeit auf offene Arbeit untersuchen.
3. Nur belegbar abgeschlossene Elemente vorschlagen.
4. Nutzeränderungen und ausdrückliche Archivfreigabe abwarten.
5. Nur die abgeschlossene, bestätigte Auswahl zur Archivierung freigeben und alle offenen beziehungsweise unklaren Arbeiten als weiter aktiv ausweisen; tatsächliche Archivierung bleibt Anwendungsfallwirkung.

**Algorithmischer Kern und Abgrenzung:** Der Algorithmus bestimmt Abschlussfähigkeit und betroffene offene Verpflichtungen; er archiviert nicht selbst. Reine Neuanlage eines Projekts in UC-39 benötigt keine Abschlussprüfung. Dessen Entwurfsbezug zu AF-15 bezeichnet ausschließlich spätere Abschlussarbeit, insbesondere in UC-10 oder UC-41.

**Invarianten und Fehler:** Semesterdatum allein ist kein Abschlussnachweis. Wiederholungsprüfungen, offene Kurse und unvollständige Projekte werden nicht automatisch archiviert. Archivierung bewahrt grundsätzlich Inhalte und unterscheidet sich von Löschung.

**Prüfbeispiel:** Im Oktober endet formal das Sommersemester; ein Projekt ist noch nicht abgegeben. Der Archivvorschlag schließt das Projekt aus, selbst wenn andere Module bereits abgeschlossen sind.

**Zusätzlicher Grenzfall:** Ein Projekt hat alle internen Aufgaben markiert, aber eine nachweislich offene Abgabe. Es wird nicht allein aufgrund dieser Aufgabenmarkierung oder des Datums zur abgeschlossenen Archivierung freigegeben.

**Verwendung:** UC-06, UC-10, UC-39, UC-41; FE-06, FE-08; GP-02, GP-06, GP-09, GP-12.

### AF-16 — Gesprächskontext zweckgebunden bilden

**Zweck:** Für ein Gespräch den unmittelbar nachvollziehbaren Arbeitsbereich und nur die dort nutzbaren relevanten Ressourcen bestimmen (FE-04).\
**Eingaben:** Einstiegspunkt (allgemein, Kurs oder Projekt), vom Nutzer gewählte Zuordnung, erlaubte Materialien, verfügbarer Verlauf, explizite Kontextkorrekturen und Dienstrechte.\
**Ausgaben:** Sichtbarer Gesprächskontext, Herkunft der einbezogenen Informationen, fehlende Kontextteile und kontrollierbare Beziehung(en).

**Verarbeitung:**

1. Den bewussten Einstiegspunkt erkennen.
2. Bei Start aus Kurs/Projekt dessen Zugehörigkeit sofort zuweisen und sichtbar machen; allgemeiner Einstieg bleibt ohne Zwangsbezug.
3. Aktuelle Rechte nach AF-01 anwenden.
4. Für das Anliegen geeignete Kontextelemente aus verfügbaren Quellen auswählen.
5. Eine manuelle Umzuordnung berücksichtigen, ohne vergangene Aussagen umzuschreiben.
6. Fehlende oder unsichere Kontextteile offenlegen.

**Algorithmischer Kern und Abgrenzung:** Der Kern ist die zweckgebundene Kontextauswahl aus Einstieg, Zuordnung, Relevanz und bestehenden Rechten. Ein bloßes Umbenennen oder Laden des Verlaufs ist keine neue Analysepflicht. Die Zuordnung selbst ist eine kontrollierbare Beziehung, kein Zugriff auf beliebige Kontodaten.

**Invarianten und Fehler:** Die vorhersehbare Anfangszuordnung benötigt keine zweite Bestätigung. Automatische Gesprächsbindung bestätigt keine KI-Dokumentklassifizierung (FE-02). Verbindung zu einem anderen KI-Anbieter gestattet keinen unbemerkten Transfer des gesamten Gesprächs. Langfristige Erinnerung wird nicht mit dem Nachrichtentext gleichgesetzt.

**Prüfbeispiel:** Ein Chat startet innerhalb „Big Data“ automatisch mit diesem Kontext. Wird er nachträglich dem Projekt X zugeordnet, bleiben seine historischen Nachrichten unverändert, und ein zusätzliches nicht freigegebenes PDF bleibt ausgeschlossen.

**Zusätzlicher Grenzfall:** Nach Wechsel von Text zu Sprache bleibt die fachliche Unterhaltung dieselbe. Nicht verfügbare frühere Inhalte oder nachträglich entzogene Quellen werden benannt statt durch unberechtigte Daten ersetzt.

**Verwendung:** UC-17, UC-18, UC-19, UC-20, UC-21, UC-23, UC-27; FE-01, FE-04, FE-09, FE-11; GP-04, GP-09, GP-10.

### AF-17 — KI-Zugangswege auf tatsächliche Berechtigung prüfen

**Zweck:** Vor jeder möglichen Modellnutzung die **Betriebsform** und den tatsächlich erlaubten Zugang nachprüfbar unterscheiden. Dazu gehören kostenfreie Verbraucherangebote, bezahlte Verbraucherabonnements, offiziell nutzbare kostenfreie API-Kontingente, kostenpflichtige API-Zugänge und gegebenenfalls lokal ausführbare Modelle.\
**Eingaben:** Anbieter, angebotene offizielle Verbindung, gemeldete Nutzerberechtigung, Betriebsart, erlaubte Funktionen, Quoten/Preise, Datenverarbeitungsbedingungen und aktueller Verfügbarkeitsnachweis.\
**Ausgaben:** Eignungszustand (`direkt integrierbar`, `nur über offizielle externe Oberfläche verwendbar`, `lokal nutzbar`, `nicht berechtigt`, `unbekannt`), tatsächlich zulässiger Funktionsumfang und offene Prüfpunkte.

**Verarbeitung:**

1. Angebotsart und tatsächlichen Nutzungsweg unterscheiden.
2. Offizielle Autorisierung und zulässige Einbindung in eine fremde Anwendung überprüfen.
3. Identifizieren, ob ein kostenloses Nutzungsrecht auch **für die geplante Integration** gilt, statt lediglich für die Consumer-Oberfläche.
4. Kontingente, Regionen, Datenschutz, Geräteanforderungen und Ausgabenfolge prüfen.
5. Zugang als Kandidat für AF-18 freigeben oder auf einen zulässigen manuellen externen Nutzungspfad begrenzen. Das Öffnen einer offiziellen Oberfläche übermittelt keine persönlichen Inhalte automatisch; eine vom Nutzer gewählte Datenübergabe wird getrennt erklärt und begrenzt.
6. Bei veränderten Anbieterbedingungen die Einstufung erneut prüfen.

**Algorithmischer Kern und Abgrenzung:** Bewertet wird der tatsächlich nachweisbare zulässige Nutzungsweg, nicht Markenbekanntheit oder ein Anmeldestatus. Der offizielle Anmeldedialog, Tokens und konkrete API-Aufrufe sind S1/N2-Themen. Ein unbekannter oder nur extern bedienbarer Zugang ist kein intern ausführbarer Modellkandidat.

**Invarianten und Fehler:** **ChatGPT Free ist nicht gleich kostenlos nutzbare OpenAI-API. ChatGPT Plus/Pro und Claude Pro sind nicht automatisch API-Zugänge.** Andere Tarife können besondere offizielle Leistungen haben; ausschließlich die konkret nachweisbaren Rechte zählen. Ein Deep Link zur Anbieter-App ist keine vollständige Syllentra-Integration und liefert ohne erlaubte Schnittstelle keine automatische Antwort zurück. Session-Cookies, interne Webschnittstellen, Scraping gegen Vorgaben, übertragene fremde Konten und Umgehung von Ratenlimits sind keine zulässigen Integrationsmethoden. API-Schlüssel dürfen nicht in einem öffentlichen Repository oder für andere Benutzer zugänglich gespeichert werden. Unbekannte Dienstadressen installieren oder starten keinen Konnektor; offiziell unterstützter Verbindungstyp, Anbieteridentität und Rechte müssen nachgewiesen sein.

**Prüfbeispiel:** Der Nutzer besitzt ChatGPT Plus, aber keine freigegebene OpenAI-API-Berechtigung. Syllentra bietet die offizielle ChatGPT-Nutzung als externen Weg an, kennzeichnet diese ohne automatische Ergebnisrückführung und darf keinen integrierten kostenfreien API-Aufruf behaupten.

**Zusätzlicher Grenzfall:** Ein Claude-Verbraucherabonnement ohne belegten offiziellen Integrationszugang legitimiert keinen API-Aufruf. Das Öffnen der offiziellen Oberfläche wird ohne automatische Datenübertragung und ohne garantierte Antwortübernahme beschrieben.

**Verwendung:** UC-45, UC-46, UC-47; FE-10; GP-04, GP-13, GP-15.

### AF-18 — Geeigneten KI-Dienst und geeignetes Modell auswählen

**Zweck:** Aus den **bereits erlaubten und tatsächlich integrierbaren** Optionen ein geeignetes Modell für die Aufgabe bestimmen und eine manuelle Modellauswahl respektieren (FE-10).\
**Eingaben:** Aufgabe, erforderliche Fähigkeiten, Sensibilität der Daten, Zweck und Qualitätserfordernisse, Kandidaten aus AF-17, Nutzerpräferenz, aktueller Anbieterstatus, zulässige Kosten und Limits.\
**Ausgaben:** Gewählter geeigneter Zugang beziehungsweise geeignetes Modell samt Auswahlgrund, alternativ Auswahlmenge mit Ausschlussgründen oder verständlich begründetes Nichtverfügbarkeitsresultat.

**Verarbeitung:**

1. Kandidaten aus AF-17 auf nachgewiesene offizielle Autorisierung, zulässige Betriebsform und Datenschutz prüfen; verbotene, nicht integrierbare oder für die Daten ungeeignete Zugänge ausschließen.
2. Vorgegebene Aufgabenfähigkeiten und fachliche Mindestqualität bewerten. Nicht belegte Eignung bleibt offen; Markenname oder Preis beweisen keine Qualität. Bei hoher fachlicher Unsicherheit eine geeignete Prüfung verlangen.
3. Tatsächliche Verfügbarkeit, Quote, erwartbaren Verbrauch und den nach AF-19 zulässigen Kostenrahmen prüfen. Erschöpfte, nicht ausreichend freigegebene oder unklar abrechenbare Optionen sind für den geplanten Aufruf nicht ausführbar.
4. Bei automatischer Auswahl unter den verbleibenden geeigneten Optionen tatsächlich kostenfrei autorisierte Nutzung bevorzugen, soweit sie genügt; die weiteren zulässigen Alternativen nach Qualität, Zuverlässigkeit, Datenschutz, Verfügbarkeit und Kosten nachvollziehbar vergleichen.
5. Eine manuelle Nutzerauswahl jederzeit unter denselben harten Schutzgrenzen berücksichtigen; ihre konkrete Präferenz darf die automatische Kostenrangfolge übersteuern, aber niemals Berechtigung, Mindesteignung, Datenschutz oder Budget.
6. Gewählten zulässigen Zugang und Modell mit Auswahlgrund ausgeben; die tatsächliche Nutzung bleibt auf die konkret erlaubte Betriebsform und den geprüften Kosten- und Datenumfang begrenzt. Ist kein Kandidat zulässig, die Einschränkung statt einer unberechtigten Ausführung melden.

**Algorithmischer Kern und Abgrenzung:** Die Auswahl ist eine begründete Eignungs- und Kostenabwägung innerhalb der bereits erlaubten Kandidaten, kein universeller Nachweis des besten Modells. Unbelegte Fähigkeiten, Kostenfreiheit oder Gerätekompatibilität dürfen nicht als erfüllt angenommen werden; fehlende Nachweise bleiben offen.

**Invarianten und Fehler:** „Automatisch“ bedeutet Auswahl **innerhalb** vorhandener Autorisierungen, nicht automatische Anmeldung, Kauf oder Upgrade. Ein kostenloses Modell mit unzureichender Eignung darf nicht allein wegen des Preises gewählt werden. Ein manuell gewähltes Modell darf eine Sperre nicht umgehen. Ein nur extern nutzbares Consumer-Angebot erscheint als manueller Übergabepfad, nicht als intern aufrufbares Modell. Die fachliche Rangfolge ist ein begründbarer Vorschlag, kein mathematischer Beweis der besten Qualität.

**Prüfbeispiel:** Ist für eine einfache Zusammenfassung tatsächlich ein geeignetes, nachweislich offizielles Gratis-Kontingent zugelassen, wird dieses bevorzugt; für komplexe Prüfungskorrektur mit fehlender Gratis-Eignung wird ein erlaubtes anderes Modell **nur innerhalb bereits freigegebener Kosten** vorgeschlagen. Bei fehlender Freigabe erfolgt keine kostenpflichtige Ausführung.

**Zusätzlicher Grenzfall:** Ein kostenloser Kandidat erfüllt die vorgegebene fachliche Mindestqualität nicht. Er wird ausgeschlossen; ist nur ein nicht freigegebener kostenpflichtiger Kandidat übrig, erfolgt keine Ausführung. Eine manuelle Wahl darf diese Sperre nicht umgehen.

**Verwendung:** UC-15, UC-16, UC-20, UC-23, UC-24, UC-26, UC-42, UC-46; FE-10; GP-03, GP-04, GP-05, GP-09, GP-10, GP-11, GP-13.

### AF-19 — Kontingent und Ausgaben begrenzen

**Zweck:** Kostenloses, abonnementsgebundenes und gesondert abrechenbares Kontingent nur nach seinen tatsächlichen Regeln einsetzen.\
**Eingaben:** Zugangstyp, bekannte verfügbare Quoten, Kosten- und Verbrauchsinformationen, Nutzungsfenster, Nutzerfreigaben, Zweck, erwartbarer Verbrauch und fehlgeschlagene Aufrufe.\
**Ausgaben:** Freigabe oder Sperre eines konkreten Aufrufs, sichtbarer Rest-/Unsicherheitsstatus und gegebenenfalls neuer bestätigungspflichtiger Kostenvorschlag.

**Verarbeitung:**

1. Pro konkretem Zugang festhalten, ob ein Verwendungsrecht grundsätzlich besteht und ob aktuelle Nutzung innerhalb seines Kontingents zulässig ist.
2. Kostenlose Kontingente und bezahlte API-Budgets ausdrücklich getrennt behandeln.
3. Erwartbaren Verbrauch konservativ prüfen, soweit eine belastbare Information vorliegt.
4. Kostenpflichtige Mehrnutzung nur innerhalb eines explizit vorher genehmigten Umfangs zulassen.
5. Eigene Nutzungszählung bei gegebenenfalls verzögerten Anbieterständen als Schätzung kennzeichnen.
6. Bei erschöpftem oder unklarem Kontingent ohne neuen Aufruf warten, eine erneut geprüfte zulässige Option nach AF-20 anbieten oder eine zusätzliche Autorisierung vorbereiten. Reicht der nachweislich erlaubte Rahmen nicht aus, bleibt der Aufruf gesperrt; eine neue Kostenempfehlung folgt AF-06/AF-07.

**Algorithmischer Kern und Abgrenzung:** Der Kern ist der fachliche Vergleich eines konkreten erwartbaren Verbrauchs mit nachweislich verfügbarer Quote und genehmigtem Restbudget. Preis- und Quotenquellen liefern S1, technische Budgetdurchsetzung und sichere Parallelverarbeitung N2. Verzögerte oder gleichzeitige Aufträge sind soweit relevant als gebundener beziehungsweise unklarer Verbrauch zu berücksichtigen.

**Invarianten und Fehler:** Keine automatische Erhöhung eines Kostenlimits oder verdeckte Abrechnung. Ein Providerwechsel ist kein Ausweg aus einer fehlenden Berechtigung. Ein bereits bezahltes Verbraucherabonnement gilt nicht als API-Kostenguthaben ohne nachgewiesene Anbieterregel. Unklarer Ausführungsstand verbietet blindes Wiederholen mit möglichen doppelten Kosten.

**Prüfbeispiel:** Ein für dieses fiktive Beispiel tatsächlich erlaubtes kostenloses API-Kontingent ist erschöpft. Syllentra zeigt die Grenze, wartet auf erlaubte Erneuerung beziehungsweise bietet eine passende andere freie Option an. Es aktiviert keine kostenpflichtige API-Stufe ohne Zustimmung.

**Zusätzlicher Grenzfall:** Zwei mögliche Aufträge würden zusammen das genehmigte Budget überschreiten, obwohl jeder einzeln hineinpasst. Sie dürfen nicht unabhängig beide als finanzierbar freigegeben werden; unklare bereits entstandene Kosten bleiben gesperrt oder klärungsbedürftig.

**Verwendung:** UC-15, UC-16, UC-20, UC-23, UC-24, UC-25, UC-26, UC-45, UC-46, UC-47; FE-08, FE-10; GP-03, GP-04, GP-05, GP-10, GP-13, GP-15.

### AF-20 — Anbieterfehler und Ersatzoption beurteilen

**Zweck:** Fachlich geeignete Reaktion auf Ausfall, Quota-Erschöpfung, fehlende Funktion oder ungewissen Abrechnungsstand finden.\
**Eingaben:** Begonnener Aufruf, aktueller Anbieterzustand, Fehlertyp, Datenempfindlichkeit, verfügbare autorisierte Alternativen und mögliche bereits ausgeführte Verarbeitung.\
**Ausgaben:** Begründeter Fehlerhinweis, sicherer Wiederaufnahmeweg oder zur Entscheidung angebotene Ersatzoption.

**Verarbeitung:**

1. Fehler als vorübergehend, fehlende Berechtigung, Quota, ungeeignete Fähigkeit, Inhalts-/Sicherheitsproblem oder unklaren Ausführungsstand unterscheiden.
2. Bereits erfolgte Kosten oder Datenübermittlungen soweit erkennbar prüfen.
3. Zulässige Wiederholung nur bei sicherem Status und innerhalb des bewilligten Rahmens erwägen.
4. Alternative Kandidaten erneut AF-17, AF-18 und AF-19 unterziehen.
5. Jede Änderung des Anbieters oder der Datenweitergabe, die nicht vom bestehenden Nutzerauftrag gedeckt ist, ausdrücklich entscheiden lassen; bei fehlender Eignung nicht fortsetzen.

**Algorithmischer Kern und Abgrenzung:** Bewertet werden Fehlerbedeutung, vorhandene Wirkung und zulässige Fortsetzungsoptionen. Technische Wiederholungsmechanismen und Anbieterprotokolle gehören S1/N2. Ein Fehler ist keine Erlaubnis für neue Anbieter oder eine automatische kostenpflichtige Stufe.

**Invarianten und Fehler:** Keine stille Nutzung eines anderen Dienstes, der zuvor keine Freigabe für diese Daten hatte. Verbraucher-App-Ausfall ist keine API-Rechteausnahme. Fehlende Verbindung hindert nur die betroffene Funktion, nicht das allgemeine manuelle Studienmanagement.

**Prüfbeispiel:** Ein gewünschtes Sprachmodell ist im aktuellen Kontingent nicht erreichbar. Syllentra zeigt zulässige Alternativen und etwaige zusätzliche Datenfreigaben, statt den kompletten Gesprächsverlauf heimlich an einen anderen Anbieter weiterzuleiten.

**Zusätzlicher Grenzfall:** Nach einer unterbrochenen Übertragung ist unklar, ob der Anbieter bereits verarbeitet oder abgerechnet hat. Statt erneut zu senden wird der erreichbare Stand geklärt und die verbleibende Unsicherheit angezeigt.

**Verwendung:** UC-16, UC-20, UC-23, UC-24, UC-26, UC-45, UC-46; FE-08, FE-10; GP-03, GP-04, GP-05, GP-10, GP-13.

### AF-21 — Vorläufige pädagogische Erinnerungen ableiten

**Zweck:** Aus einer erlaubten Lernaktivität zweckrelevante Hinweise auf Vorwissen, Schwierigkeiten, Interessen, Lerngeschwindigkeit oder Präferenzen gewinnen, ohne daraus unmittelbar gesicherte Tatsachen zu machen (FE-11).\
**Eingaben:** Eigene freigegebene Lernantworten, autorisierter Gesprächskontext, Korrekturen, ausdrücklich gemeldete Präferenzen, frühere pädagogische Einträge, Verarbeitungs-/Aufbewahrungseinstellungen.\
**Ausgaben:** Relevante **vorläufige** Erinnerungskandidaten mit Zweck, Quellenreferenz, Zeitbezug, Unsicherheit und begrenztem Geltungsbereich oder Ergebnis „nichts speichern“.

**Verarbeitung:**

1. Prüfen, ob dauerhafte pädagogische Erinnerung für den Zweck zugelassen und vom Nutzer nicht deaktiviert ist.
2. Aussagen von Zufallstexten, Zitationen, Rollenspiel und fremden Angaben unterscheiden.
3. Nur lernrelevante und sparsame Erkenntnisse auswählen.
4. Vorhandenen Einträgen zuordnen und Übereinstimmungen/Widersprüche prüfen.
5. Kandidaten als vorläufig mit Herkunft und Korrekturmöglichkeit kennzeichnen.
6. Ohne ausreichende Aussagekraft, mit verbotenen Daten oder nach einschlägigem Widerruf nichts automatisch festhalten.

**Algorithmischer Kern und Abgrenzung:** Die Relevanz- und Evidenzbewertung erzeugt unter erlaubten Einstellungen automatisch vorläufige Erkenntnisse oder „nichts speichern“, keine automatisch bestätigten Tatsachen. Eine bloße Leseansicht, insbesondere UC-29, stößt keine neue externe Analyse oder dauerhafte Ableitung an; sie kann bereits erzeugte zulässige Ergebnisse nutzen.

**Invarianten und Fehler:** **Eine Vermutung ist nie automatisch bestätigt.** Keine unkontrollierte Speicherung vollständiger Gesprächsverläufe als „Memory“, keine Übernahme fremder personenbezogener Details und keine unbegründete Ableitung besonders sensibler Merkmale. Ein einmaliger Fehler begründet keine dauerhafte mangelnde Fähigkeit. FE-11 autorisiert nicht neue externe Datenquellen oder neue kostenpflichtige Analysen.

**Prüfbeispiel:** Mehrfach falsche JOIN-Bedingungen erzeugen einen vorläufigen Lernhinweis „benötigt Übung zu SQL JOIN“, nicht die gesicherte Behauptung „beherrscht SQL nicht“ oder ein offizielles Kompetenzurteil.

**Zusätzlicher Grenzfall:** Automatisches Merken ist ausgeschaltet. Eine neue falsche Antwort erzeugt keinen dauerhaften pädagogischen Eintrag, auch wenn der Nachrichtenverlauf nach eigener zulässiger Regel gespeichert bleibt.

**Verwendung:** UC-17, UC-18, UC-19, UC-23, UC-24, UC-27, UC-29, UC-31, UC-43; FE-11; GP-04, GP-05, GP-09, GP-10, GP-11.

**Präzisierung DEC-V1-06/08:** Freiwilliges Sitzungsfeedback bleibt manuelle Selbstaussage, automatisch daraus gewonnene Erinnerung vorläufig. Überspringen ist keine bestätigte schlechte Bewertung. Keine starren Lernstilklassen oder Gesundheitsinferenz; Erfassung/Verwendung nur im erlaubten Zweck.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-22 — Erinnerungsänderung und -korrektur auswerten

**Zweck:** Automatisch abgeleitete pädagogische Erinnerung für den Nutzer überprüfbar und korrigierbar halten; ihren Lebenszyklus von Nachrichtenverlauf und amtlichen Leistungsdaten trennen.\
**Eingaben:** Vorläufige oder bestätigte Erinnerung, Quellenverweis, Nutzerkorrektur, neuere Antworten, Lösch-/Widerrufsumfang, Aufbewahrungsregel.\
**Ausgaben:** Aktualisierte, getrennte Merkmale für Herkunft und fachlichen Prüfstand, Verwendbarkeit, Korrekturstand und Löschstand. Automatisch abgeleitete Aussagen bleiben zunächst `vorläufig`; `vom Nutzer geprüft` erfordert eine tatsächliche entsprechende Nutzerhandlung. `widersprüchlich`, `überholt`, `korrigiert` und `gelöscht` beschreiben jeweils einen anderen Aspekt und bilden keine gemeinsame exklusive Statusliste. Ein amtlicher Nachweis bleibt gesonderte Studienevidenz.

**Verarbeitung:**

1. Betroffene Aussage und Herkunft identifizieren.
2. Direkte Nutzerkorrektur in dem verlangten Umfang vorrangig auswerten, aber amtliche Nachweise nicht ohne tatsächliche Quelle umdeklarieren.
3. Neue widersprechende Evidenz gegenüber früherer Unsicherheit abwägen.
4. Nicht mehr zutreffende oder nicht mehr benötigte Annahmen aus aktiven Lernentscheidungen ausschließen.
5. Bei gewünschter Löschung Erinnerung und abhängige Ableitungen im gewählten Umfang nach AF-26 behandeln; ursprüngliche Nachrichten oder Materialien nur dann mitlöschen, wenn der gewählte Umfang diese tatsächlich einschließt. Kopierte alte Erinnerungen dürfen die Korrektur oder Löschung nicht umgehen.
6. Dem Nutzer tatsächlichen Status und bekannte verbleibende externe Spuren anzeigen.

**Algorithmischer Kern und Abgrenzung:** Bewertet werden Widerspruch, Nutzerkorrektur, Relevanz und künftig zulässige Verwendung. Reines Editieren oder Löschen eines Eintrags ist kein zusätzlicher Algorithmus. Löschstatus, fachlicher Prüfstand und Verwendbarkeit sind unabhängig zu behandeln; historische Nachvollziehbarkeit darf gelöschten Inhalt nicht versteckt erhalten.

**Invarianten und Fehler:** Gespräch löschen und Erinnerung löschen sind getrennt wählbar; ein aus einem gelöschten Original nicht mehr belegbares Zitat wird nicht weiterhin als verfügbar präsentiert. Archivieren ist keine Löschung. Die Korrektur einer Behauptung ist nicht automatisch die Löschung aller Inhalte, die sie ursprünglich begründet haben.

**Prüfbeispiel:** Der Nutzer korrigiert „Ich lerne gern nur mit Videos“ zu „Ich bevorzuge Text mit Beispielen“. Künftige Empfehlungen berücksichtigen die Korrektur; die vorherige unbelegte Präferenz wird nicht weiter aktiv als sicher verwendet.

**Zusätzlicher Grenzfall:** Ein Nutzer widerruft den Verwendungszweck einer alten Lernannahme. Sie wird nicht weiter für Aufgabenwahl benutzt. Die Bestätigung einer Löschung ohne Ausführungsnachweis darf nicht als bereits entferntes externes Datum erscheinen.

**Verwendung:** UC-02, UC-19, UC-21, UC-22, UC-24, UC-29, UC-31, UC-43, UC-49, UC-50; FE-09, FE-11; GP-01, GP-04, GP-05, GP-10, GP-11, GP-15.

**Präzisierung DEC-V1-06:** Einsehbare Annahmen/Präferenzen korrigieren, begrenzen oder nach gewähltem Umfang zurücksetzen; keine ungewollte Löschung amtlicher Nachweise. Fehlende Quelle/gelöschter Eintrag darf nicht aus Schattenhistorie wiederkehren.

Bezüge und Abnahme: [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md).

### AF-23 — Kompetenznachweise gewichten

**Zweck:** Eine fachliche Kompetenzbehauptung mit geeignetem Beleggrad und begrenzter Aussagekraft verknüpfen.\
**Eingaben:** Eigene Antworten, Einsatz von Hilfen, Projektergebnisse, behauptete Beiträge, Zertifikate, amtliche Nachweise und Aktualität.\
**Ausgaben:** Nachweisgestützte Kompetenzdarstellung, als vorläufig gekennzeichnete Ergänzungen und fehlende Belege.

**Verarbeitung:**

1. Fachgebiet und behaupteten Kompetenzumfang bestimmen.
2. Quellen und Beiträge zwischen Nutzer, Dritten und KI trennen, soweit nachweisbar.
3. Unabhängige korrekte Lösung, unterstützte Lösung, bloße Teilnahme und offiziellen Nachweis unterschiedlich behandeln.
4. Zeitliche und fachliche Übertragbarkeit prüfen.
5. Widersprüche und offene Belege ausweisen.
6. Nutzerkorrekturen oder externe Bestätigungen berücksichtigen, ohne fiktive Nachweise zu erzeugen.

**Algorithmischer Kern und Abgrenzung:** Die Gewichtung beschränkt sich auf fachlichen Aussageumfang, Herkunft, eigene Leistung, Hilfegrad und Aktualität. Eine rechnerische Skala oder allgemeingültige Kompetenzschwelle wird hier nicht erfunden; prüfbare Maßstäbe folgen F3-Detaillierung und N1. Amtliche Anerkennung bleibt extern.

**Invarianten und Fehler:** Eine Note ist nur Beleg des tatsächlich geprüften Umfangs; sie beweist nicht jede praktische Teilkompetenz. Ein gemeinsames GitHub-Projekt beweist nicht automatisch einen individuellen Beitrag. Die Funktion entscheidet nicht über amtliche Anerkennung oder Einstellungsfähigkeit.

**Prüfbeispiel:** Für ein Projekt ist die Teilnahme sicher, aber der einzelne Codebeitrag ungeklärt. Das Portfolio zeigt Projekterfahrung und eine ausdrücklich ungeklärte spezifische Implementierungskompetenz.

**Zusätzlicher Grenzfall:** Ein Teamprojekt ist belegt, die individuelle Arbeit aber nicht zuordenbar. Die Projekterfahrung kann dokumentiert werden; ein persönlicher unabhängiger Implementierungsnachweis wird nicht behauptet.

**Verwendung:** UC-09, UC-28, UC-29, UC-31, UC-41, UC-42, UC-43, UC-44; FE-07, FE-09, FE-11; GP-02, GP-04, GP-05, GP-06, GP-08, GP-09, GP-11.

### AF-24 — Studienoptionen nachvollziehbar vergleichen

**Zweck:** Akademische Entscheidungsoptionen sachlich anhand vom Nutzer vorgegebener Kriterien und überprüfbarer Quellen strukturieren.\
**Eingaben:** Entscheidungssituation, Ziele, verfügbare Zeit, Voraussetzungen, Studienregeln, Alternativen und ihre Quellenstände.\
**Ausgaben:** Gegenüberstellung mit erfüllten/unbekannten Bedingungen, Risiken, offenen Fragen und gegebenenfalls Hinweis auf zuständige Stelle.

**Verarbeitung:**

1. Anliegen und gewünschte Wirkung präzisieren.
2. Verfügbare rechtmäßige Informationen getrennt nach Quelle und Gewissheit einordnen.
3. Zulässige Handlungsoptionen vergleichen.
4. Zeitliche, organisatorische, fachliche und gegebenenfalls finanzielle Folgen erklären.
5. Fehlende verbindliche Auskunft kenntlich machen.
6. Nutzerentscheidung vorbereiten, ohne institutionelle Entscheidung zu ersetzen.

**Algorithmischer Kern und Abgrenzung:** Die Funktion vergleicht Optionen gegen nachvollziehbare Kriterien und Quellen. Sie führt weder eine Hochschulanmeldung noch einen Versand aus. Für echte bestätigungspflichtige Folgevorschläge gelten AF-06/AF-07; eine reine Beratung benötigt nicht automatisch einen Entscheidungseintrag.

**Invarianten und Fehler:** Das System meldet eine offizielle Zulassung oder Anerkennung nur, wenn ein tatsächlicher entsprechender Nachweis vorliegt. Eine Empfehlung darf ohne gesonderte Freigabe weder Nachricht an eine Hochschule noch kostenpflichtige Handlung auslösen.

**Prüfbeispiel:** Zwei Wahlpflichtmodule werden nach eigener Vorbildung, Zeitüberschneidung, Prüfungsform und anerkannten Voraussetzungen verglichen; die finale Modulwahl verbleibt beim Nutzer.

**Zusätzlicher Grenzfall:** Für eine Anerkennung fehlt eine aktuelle verbindliche Quelle. Die Option bleibt klärungsbedürftig und verweist auf die zuständige Stelle; sie wird nicht als amtlich genehmigt ausgegeben.

**Verwendung:** UC-44; FE-08; GP-08.

### AF-25 — Konfiguration regelkonform prüfen

**Zweck:** Administrativ veränderbare Parameter innerhalb unterstützter Grenzen nachvollziehbar prüfen und eine zulässige Rücknahme einer früheren Fassung vorbereiten.\
**Eingaben:** Konfigurationsentwurf, vorherige gültige Fassung, Einstellungsbereich CFG-01 bis CFG-17, Änderungsrechte, abhängige Einstellungen und unveränderliche Schutzregeln.\
**Ausgaben:** Validierter Entwurf, verständliche Konflikte, geeignete Vorschau und zulässige Wiederherstellungsoption.

**Verarbeitung:**

1. Geänderte unterstützte Felder bestimmen.
2. Datengültigkeit, Abhängigkeiten und aktuelle Berechtigungen prüfen.
3. Unveränderliche Beschränkungen für Kalender, Kosten, Quellcode, Plugins und Privatsphäre durchsetzen.
4. Bei geeigneten Einstellungen die Wirkung vor Speicherung anzeigen.
5. Nur bewusst gespeicherte gültige Fassung zur Anwendung übergeben.
6. Bei Wiederherstellung einer früheren Fassung sämtliche aktuellen Schutzregeln erneut prüfen.

**Algorithmischer Kern und Abgrenzung:** Die fachliche Abhängigkeitsprüfung betrifft ausdrücklich unterstützte Parameter und deren Auswirkungen, nicht generische Feldvalidierung oder neue Programmlogik. Formate und Rechteverfahren sind D2/N2-Themen, konkrete Vorschau B1. Das Resultat ist eine gültige oder abgelehnte Fassung, keine Behauptung beliebiger konfigurierbarer Software.

**Invarianten und Fehler:** Ein Textfeld führt keine Skripte aus. Ein verstecktes Menü entzieht keine Rechte. Eine Konfigurationsrücknahme macht weder frühere Ausgaben noch versandte Nachrichten oder bestätigte Löschungen rückgängig. Plattformgebundene App-Merkmale können Neuinstallation erfordern.

**Prüfbeispiel:** Der Administrator benennt „Mein Studium“ in „Studienübersicht“ um; die Beschriftung wird gültig gespeichert. Ein Versuch, externe Kalenderschreibrechte über einen Parameter zu aktivieren, wird abgelehnt.

**Zusätzlicher Grenzfall:** Eine alte Konfiguration würde heute widerrufene Anbieterrechte oder ein höheres ungenehmigtes Budget zurückbringen. Wiederherstellung wird insoweit abgelehnt; gelöschte Erinnerungen und Nachrichten werden nicht wiederhergestellt.

**Verwendung:** UC-45, UC-46, UC-47, UC-48; FE-08, FE-09, FE-10, FE-11; GP-04, GP-13, GP-14, GP-15.

### AF-26 — Export- und Löschfolgen ermitteln

**Zweck:** Vor einem Datenexport oder einer Löschung den tatsächlich betroffenen Umfang, Abhängigkeiten und verbleibende Spuren ermitteln.\
**Eingaben:** Gewählter Datenumfang, Dokumente/Beziehungen, Verlauf, pädagogische Erinnerung, externe Übermittlungen, Geräte/Backups, Aufbewahrungsgrenzen und Bestätigung.\
**Ausgaben:** Verständliche Auswirkungsübersicht, auswählbarer Lösch-/Exportumfang, erforderliche Bestätigung und nachvollziehbarer Ausführungs-/Reststatus.

**Verarbeitung:**

1. Ausgewählte Originale, Beziehungen, Nachrichten, Erinnerungen und Ableitungen getrennt auflisten.
2. Gemeinsam verwendete Quellen und Verweise feststellen.
3. Externe oder gerätelokale Daten und mögliche Aufbewahrungspflichten abgrenzen.
4. Bei folgenreichen oder irreversiblen Operationen den konkreten Umfang bestätigen lassen.
5. Nach Durchführung tatsächliche interne und erreichbare externe Folgen unterscheiden.
6. Nicht nachgewiesene vollständige Entfernung nicht behaupten; fehlende Beleganker markieren.

**Algorithmischer Kern und Abgrenzung:** Der Kern ist die Ermittlung und Abgrenzung fachlicher Abhängigkeiten und Folgewirkungen. Exportformat, sichere Bereitstellung, Löschverfahren, Aufbewahrungsfristen und Sicherungen gehören D1/D2, B3, S1 und N2. Die Bestätigung betrifft exakt den ausgewählten destruktiven Umfang, nicht jede reine Einsicht.

**Invarianten und Fehler:** Entfernen eines Projektbezugs löscht nicht automatisch das Original. Löschen einer Unterhaltung löscht nicht ohne Wahl jede pädagogische Erinnerung. Ein Export darf keine Zugangsschlüssel enthalten; fehlgeschlagene/partielle Exporte gelten nicht als vollständige Kopie.

**Prüfbeispiel:** Beim Löschen eines in drei Modulen verwendeten Originals nennt die Vorschau die drei Beziehungen sowie betroffene Belege. Ohne Bestätigung der tatsächlichen Originallöschung wird das Original nicht gelöscht und auch keine andere Operation ersatzweise ausgeführt. Hat der Nutzer ausdrücklich stattdessen eine einzelne Modulzuordnung zum Entfernen gewählt, wird ausschließlich diese Beziehung entfernt.

**Zusätzlicher Grenzfall:** Beim gewünschten Originallöschen wird die Bestätigung abgebrochen. Es erfolgt weder Originallöschung noch ersatzweise Linkentfernung. Ein Export ohne zugängliches Original benennt die Lücke und enthält keine Zugangsdaten.

**Verwendung:** UC-05, UC-14, UC-22, UC-49, UC-50; FE-09, FE-11; GP-03, GP-10, GP-15.

### AF-27 — Geräteübergreifende Änderungen abgleichen

**Zweck:** Veraltete, konkurrierende oder nach Zugriffsverlust unzulässige Änderungen zwischen berechtigten Geräten erkennen und nachvollziehbar zusammenführen.\
**Eingaben:** Geräteberechtigung, letzte bekannte Fassung, neue Änderung, betroffene Daten-/Vorschlagsversion, vorhandener Zielzustand und Konfliktregel.\
**Ausgaben:** Übernommene gültige Änderung, aufzulösender Konflikt, abgelehnter Zugriff oder bewusst ausstehender Abgleich.

**Verarbeitung:**

1. Gerätezulassung und aktuelle Rechte prüfen.
2. Ausgangs- und Zielversion vergleichen.
3. Konfliktfreie Änderungen zusammenführen, ohne Berechtigungsgrenzen zu verändern.
4. Bei widersprechenden Änderungen die unterschiedlichen Fassungen und Auswirkungen anzeigen.
5. Besonders für Vorschläge AF-06 anwenden und Entscheidungen/Arbeitsergebnisse nicht doppelt ausführen.
6. Nach Widerruf neue Zugriffe sperren und bereits vorhandene lokale Daten als gesondertes Sicherheits-/Löschthema kennzeichnen.

**Algorithmischer Kern und Abgrenzung:** Hier wird die fachliche Vereinbarkeit konkurrierender Änderungen, Wirkungen und aktueller Rechte beurteilt. Übertragung, technische Synchronisation, Sperrverfahren und Speicherung werden nicht festgelegt. Unabhängige Änderungen dürfen nur vereinigt werden, wenn dadurch keine fachliche Invariante verletzt wird.

**Invarianten und Fehler:** „Letzte Änderung gewinnt“ darf nicht pauschal eine jüngere bestätigte Entscheidung überschreiben. Offline oder auf einem abgemeldeten Gerät angezeigte Werte sind keine neue Berechtigung. Ein fehlgeschlagener Abgleich wird als solcher angezeigt und niemals als gesicherte Synchronisation ausgegeben.

**Prüfbeispiel:** Zwei Geräte bearbeiten denselben Kalendervorschlag. Gerät A lehnt die aktuelle Fassung ab; Gerät B kann eine alte Fassung nicht nachträglich unbemerkt bestätigen. Der Widerspruch wird angezeigt.

**Zusätzlicher Grenzfall:** Ein altes Gerät sendet nach bestätigter Löschung eine frühere Erinnerungsfassung. Sie darf weder als neue Nutzerkorrektur gelten noch die gelöschte Aussage unbemerkt wieder aktivieren; die Auswirkung bleibt als Konflikt beziehungsweise unzulässige Änderung erkennbar.

**Verwendung:** UC-04, UC-05, UC-19, UC-21, UC-32, UC-35, UC-38, UC-48; FE-08, FE-09, FE-11; GP-03, GP-06, GP-07, GP-10, GP-12, GP-14, GP-15.

## F3.4 Vertiefung: FE-10 — Kostenbewusste KI- und Modellauswahl

**Bestätigte Entscheidung FE-10:** Syllentra soll das für die konkrete Aufgabe geeignete KI-Modell unter den **bereits autorisierten** Angeboten automatisch bestimmen. Eignung berücksichtigt fachliche Qualität, Datenschutz, verfügbare Berechtigungen, Nutzungsgrenzen und Kosten. Der Benutzer kann jederzeit eine manuelle Präferenz festlegen. **Ergänzende Nutzerpräferenz:** Wenn ein tatsächlich berechtigter kostenfreier Zugang genügt, soll dieser bevorzugt werden; bereits vorhandene Verbraucherabonnements dürfen nur in einer offiziell erlaubten Betriebsform berücksichtigt werden.

### F3.4.1 Arten des Zugangs und fachliche Bedeutung

| Zugangsklasse | Beispiel / Verständnis | Interne automatische Modellverwendung erlaubt? | Regel |
|---|---|---|---|
| Kostenloses Verbraucherangebot | Offizielle ChatGPT-/Claude-Web- oder App-Nutzung im Free-Tarif | Nur wenn der Anbieter einen geeigneten offiziellen Integrationsweg tatsächlich gestattet | Sonst nur eigener externer Nutzungspfad; weder API-Recht noch automatische Freiquote ableitbar |
| Bezahltes Verbraucherabonnement | Beispielsweise ChatGPT Plus/Pro oder Claude Pro/Max | Nicht allein aufgrund des Abonnements | Einzelne offizielle Integrationsrechte und gegebenenfalls Sonderkontingente gesondert prüfen |
| Offiziell kostenfreier API-/Integrationszugang | Anbietergewährtes Free-Tier-Kontingent oder erlaubter Partnerzugang | Ja, sofern für Syllentra freigegeben und mit geeigneten Bedingungen | Anbieterquota, Modellfähigkeit, Region und Nutzungsbedingungen beachten |
| Bezahlter API-/Integrationszugang | Gesondert zugelassene API oder ein offiziell abrechenbarer Zugang | Nur im ausdrücklichen Kosten-/Datenfreigaberahmen | Kein stilles Upgrade, keine verborgene Ausgabe |
| Lokal verfügbares Modell | Auf eigenem berechtigtem Gerät ausführbare Modellfunktion | Nur bei tatsächlich vorhandener, legal nutzbarer Fähigkeit | Kein externer Modellaufruf; Geräte-, Lizenz-, Qualitäts- und Ressourcenbeschränkungen sowie mögliche Betriebskosten bleiben |
| Offizielle externe Oberfläche als manueller Weg | Der Nutzer öffnet die offizielle Anwendung selbst, falls kein integrierbarer Zugang nachgewiesen ist | Nein; Öffnen ist kein automatischer Modellaufruf und garantiert keinen Antwortimport | Keine automatische Inhaltsübergabe; bewusstes manuelles Übertragen und dessen Datenschutzfolgen getrennt behandeln |
| Unbekannter Zugang | Nicht verifizierte URL, inoffizieller Wrapper, übertragene Session | Nein | Keine Installation, Anmeldung oder Ausführung ohne gesicherte offizielle Berechtigung |

**Wichtig:** Ein Zugang zur offiziellen Consumer-Anwendung ist für den Menschen nutzbar, aber ohne passende Schnittstelle nicht automatisch als direktes Syllentra-Modell auswählbar. Ein erlaubtes manuelles Öffnen, Teilen oder Kopieren von Inhalten ist von einer durchgängig integrierten Ausführung mit automatischer Antwortübernahme zu unterscheiden. Es dürfen keine Sitzungscookies extrahiert, Web-UIs automatisiert entgegen Anbieterregeln bedient oder separate Gratis-Konten zur Quota-Umgehung zusammengeschaltet werden. Zugangsaussagen sind stets veränderlich und bedürfen aktueller Prüfung.

### F3.4.2 Entscheidungstabelle für Modellwahl

| Fall | Berechtigung, Eignung und Budget | Fachliche Auswahl |
|---|---|---|
| M-01 | Geeignetes offiziell integrierbares Gratis-Kontingent vorhanden | Dieses vorrangig anbieten/verwenden, sofern Qualität und Datenschutz genügen |
| M-02 | Nur Consumer-Free-/Abo-Oberfläche offiziell verfügbar | Externen offiziellen Nutzungspfad kenntlich anbieten; nicht als internes API-Modell ausgeben |
| M-03 | Freies Kontingent erschöpft, andere freigegebene Gratisoption geeignet | Nach Eignungsprüfung alternative Option anbieten; bestehende Anbieterwechselregeln beachten |
| M-04 | Freie Optionen ungeeignet, bezahlte API innerhalb bestehendem genehmigtem Budget | Erlaubte fachlich geeignete Option wählen und tatsächliche Kostengrenze beachten |
| M-05 | Bezahlte API benötigt neue Freigabe | Vorerst nicht ausführen, Umfang/Kosten erläutern und Bestätigung abwarten |
| M-06 | Nutzer wählt manuell ungeeignetes oder unberechtigtes Modell | Schutzgrenze erklären; zulässige Alternativen anbieten, nicht trotzdem ausführen |
| M-07 | Providerdatenbedingungen ungeeignet für ausgewählte Informationen | Kandidat ausschließen; Daten minimieren oder anderen erlaubten Weg anbieten |
| M-08 | Quota/Abrechnung/Erfolgsstatus nicht feststellbar | Status als unklar ausweisen; keine blinde potenziell kostenpflichtige Wiederholung |
| M-09 | Kein passendes integrierbares Modell verfügbar | Betroffene KI-Funktion begrenzt nicht verfügbar; manuelle/andere Funktionen bleiben nutzbar |
| M-10 | Lokales zulässiges Modell für den Zweck ausreichend | Als geeignete Option berücksichtigen; keine generelle Gleichwertigkeit garantieren |

Die Fälle M-01 bis M-10 sind bedingte fachliche Beispiele, keine Bestätigung eines heute verfügbaren kostenlosen API-Kontingents bei OpenAI, Claude oder einem anderen benannten Anbieter. Bereits vorhandene Abonnements sollen im offiziell erlaubten Rahmen möglichst einfach berücksichtigt werden, ohne Zugangsdaten zu übernehmen oder unbekannte Rechte zu unterstellen.

**Fachliche Rangfolge:** 1. zwingende Autorisierung und Datenschutz-/Schutzgrenzen; 2. vorgegebene Mindestqualität/Funktionsfähigkeit; 3. tatsächliche Verfügbarkeit und Quote; 4. unter geeigneten Optionen kostenlose Nutzung bevorzugen; 5. weiter nach nachvollziehbarer Qualität, Zweckmäßigkeit, Risiko und Kosten vergleichen. Diese Rangfolge ist keine starre Anbieter-Priorität. Ein manuelles Nutzerurteil kann innerhalb der harten Grenzen eine andere geeignete Option bestimmen.

**Abnahmekriterien:** Ein ChatGPT-Plus-Login ohne gesonderte API-/Integrationsberechtigung erzeugt keinen internen Modellaufruf. Eine als „gratis“ angebotene API mit erschöpftem Kontingent löst keine automatisch kostenpflichtige Fortsetzung aus. Ein explizit gewähltes kostenpflichtiges Modell wird ohne passende vorherige Freigabe blockiert. Bei zulässigen zwei kostenlosen Modellen wird nicht automatisch das weniger geeignete verwendet, wenn es die Aufgabe erkennbar nicht erfüllen kann.

### F3.4.3 Prüfstand der Anbieterquellen am 15.10.2026

Die in F3.9 verlinkten drei offiziellen Informationsseiten wurden am Bearbeitungstag direkt abzurufen versucht. Alle drei Abrufe scheiterten mit HTTP 403; auch die erneute Ausführung außerhalb der eingeschränkten Ausführungsumgebung ermöglichte keine Inhaltsprüfung. Der vorliegende Stand bestätigt daher keine aktuellen Tarifdetails, Quoten, konkreten API-Rechte oder vorhandenen Abonnementintegrationen.

| Offizielle Referenz | Zweck der geforderten Prüfung | Tatsächliches Ergebnis am 15.10.2026 |
|---|---|---|
| OpenAI: ChatGPT-/API-Abrechnung, siehe F3.9 | Abgrenzung von Consumer-Abonnement und tatsächlich erlaubter API-Nutzung | HTTP 403; Seiteninhalt nicht aktuell verifiziert |
| OpenAI: kostenloses ChatGPT, siehe F3.9 | Kostenloser Consumer-Zugang, Grenzen und Abgrenzung zu einem integrierbaren Kontingent | HTTP 403; Seiteninhalt nicht aktuell verifiziert |
| Claude: Abonnement und API, siehe F3.9 | Tarifbezogene Consumer-Rechte gegenüber gesonderter API-Nutzung | HTTP 403; Seiteninhalt nicht aktuell verifiziert |

Die Entscheidungsvorschriften bleiben konservativ: Aus einem Consumer-Login folgt für Syllentra kein nachgewiesenes Integrationsrecht. Vor Nutzung muss der konkrete offizielle Mechanismus mit aktuellen Bedingungen, Qualität, Datenschutz, Quote und zulässigen Kosten nachgewiesen werden. Unbekannte Rechte bleiben unbekannt; eine fehlgeschlagene Quellenprüfung darf keine Freigabe erzeugen. Die Referenzen bleiben für eine spätere tatsächliche Prüfung erhalten. Diese Einschränkung betrifft die zeitaktuelle Anbieterprüfung, nicht eine bereits implementierte Integration; eine solche wird hier nicht behauptet.

## F3.5 Vertiefung: FE-11 — Kontrollierbare vorläufige Lern-Erinnerung

**Bestätigte Entscheidung FE-11:** Syllentra darf aus eigenen autorisierten Lernaktivitäten und Gesprächen automatisch **zweckrelevante und vorläufige pädagogische Erinnerungen** gewinnen. Sie müssen für den Benutzer einsehbar, korrigierbar und löschbar sein. Automatisches Merken setzt die erlaubte Erinnerungsfunktion und ihren zulässigen Umfang voraus; es ist keine Generalerlaubnis, alle Gespräche vollständig und unbegrenzt zu speichern.

### F3.5.1 Geltungsbereich und Status

| Art der Information | Automatische vorläufige Erinnerung? | Grenze |
|---|---|---|
| Wiederholt beobachtete fachliche Unsicherheit | Ja, mit Quelle und Zeitpunkt | Nicht als endgültig fehlende Fähigkeit behaupten |
| Wiederholt selbstständig gelöste Aufgaben | Ja, als begründete vorläufige Kenntniseinschätzung | Kein amtlicher Kompetenznachweis |
| Explizit mitgeteilte Lernpräferenz | Ja, vorbehaltlich späterer Nutzerkorrektur | Gilt nicht zwingend für jedes Thema |
| Einmaliges sprachliches Missverständnis | Nur als eng begrenzter vorläufiger Hinweis bei tatsächlicher Lernrelevanz, sonst nicht | Keine dauerhafte Schwächenbehauptung oder pauschale Fähigkeitsbewertung aus einem Einzelfall |
| Offizielle Prüfungsergebnisse | Nicht als automatisch abgeleitete Erinnerung; gesonderte Studienevidenz nach UC-09 | Tatsächlichen Beleg und Herkunft erhalten; erforderliche Importbestätigung bleibt bestehen, keine Umdeklaration zur KI-Schätzung |
| Private Drittpersonendaten / besonders sensible vermutete Merkmale | Nicht im Rahmen dieser freien automatischen pädagogischen Ableitung | Keine unnötigen sensiblen Angaben oder fremden personenbezogenen Details aus Gesprächen ableiten; eine etwaige andere Verarbeitung bedürfte gesonderter fachlicher und rechtlicher Grundlage |
| Ganzer Gesprächsverlauf | Als Verlauf nach eigener Regel, nicht als „Memory“-Kurzfakt | Aufbewahrungs-/Löschregeln der DK-08 gelten getrennt |

### F3.5.2 Regeln der Verwendung und Korrektur

- Jeder aktive vorläufige Eintrag weist fachlichen Bezug, Grund, Quellenstand, Aktualität und Unsicherheit aus; unbekannte Quelle bleibt kenntlich.
- Die aktive Lerneinheit darf passende vorläufige Erkenntnisse nutzen, ohne sie als amtliche Fakten auszugeben.
- Neue belastbare eigene Antworten, Nutzerkorrekturen und widersprechende Quellen aktualisieren die Einordnung; vergangene Nachrichten bleiben davon getrennt.
- Der Nutzer kann die tatsächlich für eine Empfehlung berücksichtigten pädagogischen Erkenntnisse mit Quelle, Zeitbezug, Unsicherheit und Verwendungsgrund nachvollziehen; eine nicht belegbare Herkunft bleibt als unklar ausgewiesen. Interne Modellgedanken werden damit nicht als verfügbar behauptet.
- Automatisches Merken bleibt abschaltbar und im Aufbewahrungsumfang kontrollierbar. Abschalten verhindert neue entsprechende Ableitungen; die zulässige Verwendung vorhandener Einträge und deren Löschung werden getrennt steuerbar. Widerruf des Verwendungszwecks beendet auch die entsprechende aktive Nutzung bereits vorhandener Einträge.
- Nutzergewünschtes Löschen zeigt die getrennten Auswirkungen auf Nachrichten, Erinnerungen, Materialien und abgeleitete Einträge. Keine stillen Versprechen über externe Löschung.
- Ein vorläufiger Gedächtniseintrag autorisiert weder die Nutzung eines neuen KI-Anbieters noch eine Ausgabe.

Innerhalb des bereits erlaubten Erinnerungszwecks benötigt nicht jeder vorläufige Eintrag eine neue Einzelbestätigung. Automatische Ableitung darf aber niemals automatisch ihren Prüfstand auf „bestätigt“ erhöhen. Herkunft, Zeitpunkt, Grad der Gewissheit, Geltungsbereich und Verwendungsgrund bleiben neben dem aktuellen Korrektur- und Löschstand nachvollziehbar. Ein Nutzer kann solche Informationen prüfen, korrigieren, ihre weitere Verwendung oder Erfassung begrenzen und Löschung verlangen.

**Abnahmekriterien:** Einem wiederholten Fehler folgt höchstens eine als vorläufig gekennzeichnete Schwächeinschätzung. Eine ausdrücklich korrigierte Präferenz wirkt sich auf nachfolgende zulässige Empfehlungen aus. Nach tatsächlich ausgeführter Löschung wird der betreffende Eintrag nicht aus versteckten Kopien weiterverwendet oder aus der alten Ableitungsgrundlage entgegen dem gewählten Lösch- beziehungsweise Widerrufsumfang wiederbelebt. Eine bloße Bestätigung ist kein Löschbeleg; begrenzte oder ausstehende externe Schritte werden ausgewiesen. Neue spätere autorisierte Lernaktivitäten dürfen nur innerhalb weiterhin gültiger Einstellungen neue vorläufige Erkenntnisse begründen. Ein gelöschter Gesprächsverlauf führt nur dann zur Mitlöschung der getrennten Erinnerung, wenn dieser Umfang ausgewählt oder eine einschlägige Löschregel anwendbar ist.

## F3.6 Verwendungs- und Abdeckungsmatrix der Anwendungsfälle

Nicht jeder Anwendungsfall benötigt einen eigenen AF. Für rein dialogbezogene oder einfache manuelle Bearbeitung stehen in der Matrix nur tatsächlich wiederverwendbare Ableitungen; reine CRUD- und Layoutschritte verbleiben in F2/B1 beziehungsweise Implementierung. Alle UC-Kennungen bleiben unverändert.

**Begründung für UC-01 ohne AF:** Das freiwillige Beginnen, Überspringen und spätere Fortsetzen der Einrichtung ist ein Nutzerablauf mit Eingabe- und Navigationsentscheidungen. Dafür wird kein eigener algorithmischer Kern erfunden. Erst eine tatsächlich gewählte nachfolgende Profilbearbeitung, Quellenprüfung oder Unterhaltung kann die dort ausgewiesenen Funktionen benötigen. Das Prüfbeispiel T-01 umfasst diesen anschließenden zulässigen Gesprächseinstieg; es behauptet keinen obligatorischen AF-Aufruf beim Überspringen.

**Leseregel der Zuordnungen:** Katalog, Beschreibungen und Rückverweismatrix verwenden dieselben fachlichen Beziehungen; der Katalog zeigt wichtige Teilmengen. Eine Beziehung ist kein obligatorischer Aufruf bei jedem Besuch eines UC. Insbesondere stößt UC-29 als reine Fortschrittsanzeige keine neue AF-21-Ableitung an. UC-39 als einfache Projektneuanlage benötigt keine AF-15-Abschlussprüfung; der erhaltene Entwurfsbezug kennzeichnet die spätere Prüfung desselben Projekts in UC-10/UC-41. AF-05 bei UC-07/UC-39 betrifft nur tatsächlich vorhandene geteilte Ressourcenbeziehungen, nicht das bloße Anlegen eines Datensatzes. AF-14 bei UC-38 liefert gegebenenfalls den fachlichen Änderungshintergrund eines Vorschlags, nicht bei jedem Listenaufruf eine Quellenabfrage.

AF-06/AF-07 sind auch für bereits in F2 beschriebene bedingte Import-, Struktur-, Planungs-, Beratungs-, Konfigurations- und Bereinigungsvorschläge rückverfolgt. Die direkte manuelle Bearbeitung bleibt davon getrennt. Allgemeine Schutzgrenzen gelten für alle Aufrufer, auch wenn die Übersicht keinen generischen Prüfbaustein an jede reine Anzeige hängt.

| F2-Anwendungsfall | Fachlicher F3-Bezug (direkt oder bedingt) | Ziel aus F2 |
|---|---|---|
| UC-01 | —; reine optionale Einrichtung, siehe Begründung | Geführten Einstieg nutzen oder überspringen |
| UC-02 | AF-01, AF-22 | Mein Profil bearbeiten |
| UC-03 | AF-02, AF-06, AF-07, AF-08 | Studieninformationen und Nachweise aktualisieren |
| UC-04 | AF-01, AF-27 | Persönlichen Arbeitsstand auf einem berechtigten Gerät fortsetzen |
| UC-05 | AF-01, AF-26, AF-27 | Gerätezugriff beenden oder entziehen |
| UC-06 | AF-08, AF-15 | Semester anlegen, wechseln und verwalten |
| UC-07 | AF-05, AF-06, AF-07, AF-08 | Modul oder Kurs anlegen und zuordnen |
| UC-08 | AF-06, AF-07, AF-08 | Themen, Kapitel und Lernziele organisieren |
| UC-09 | AF-02, AF-06, AF-07, AF-08, AF-12, AF-23 | Noten, ECTS und Prüfungsleistungen erfassen |
| UC-10 | AF-06, AF-07, AF-08, AF-15 | Semesterabschluss und Archivierung bestätigen |
| UC-11 | AF-03, AF-04 | Lernmaterial als dauerhaftes Original aufnehmen |
| UC-12 | AF-04, AF-06, AF-07 | KI-Vorschlag zur Dokumentzuordnung entscheiden |
| UC-13 | AF-04, AF-05, AF-06, AF-07 | Ein Dokument mit mehreren Arbeitsbereichen verknüpfen |
| UC-14 | AF-05, AF-26 | Dokumentenverknüpfung entfernen ohne Original zu löschen |
| UC-15 | AF-01, AF-02, AF-03, AF-04, AF-18, AF-19 | Material analysieren und Quellenlage nachvollziehen |
| UC-16 | AF-03, AF-06, AF-07, AF-18, AF-19, AF-20 | Zulässige Audio- oder Videoinhalte aufbereiten |
| UC-17 | AF-16, AF-21 | Allgemeine Unterhaltung beginnen |
| UC-18 | AF-01, AF-16, AF-21 | Unterhaltung aus Kurs oder Projekt mit Kontext starten |
| UC-19 | AF-01, AF-16, AF-21, AF-22, AF-27 | Unterhaltung suchen und fortsetzen |
| UC-20 | AF-01, AF-16, AF-18, AF-19, AF-20 | Zwischen Text und Sprache im Gespräch wechseln |
| UC-21 | AF-05, AF-16, AF-22, AF-27 | Gespräch organisieren, zuordnen und archivieren |
| UC-22 | AF-05, AF-22, AF-26 | Unterhaltung mit abgestimmten Löschfolgen entfernen |
| UC-23 | AF-01, AF-03, AF-09, AF-16, AF-18, AF-19, AF-20, AF-21 | Interaktive Lerneinheit mit frei gewähltem Einstieg beginnen |
| UC-24 | AF-09, AF-10, AF-11, AF-12, AF-18, AF-19, AF-20, AF-21, AF-22 | Adaptives Verständnis überprüfen |
| UC-25 | AF-10, AF-11, AF-19 | Fehler mit schrittweisen Hinweisen bearbeiten |
| UC-26 | AF-11, AF-18, AF-19, AF-20 | Vollständige Lösung und Lösungsweg anfordern |
| UC-27 | AF-09, AF-16, AF-21 | Lernstrategie an Rückmeldung und Fortschritt anpassen |
| UC-28 | AF-09, AF-10, AF-11, AF-12, AF-23 | Prüfungsnahe Übung oder Simulation durchführen |
| UC-29 | AF-02, AF-10, AF-11, AF-12, AF-21 (vorhandene Ergebnisse, keine neue Ableitung durch Anzeige), AF-22, AF-23 | Lernfortschritt und Wissensstand unterscheiden |
| UC-30 | AF-06, AF-07, AF-09, AF-13 | Prüfungsvorbereitung für mehrere Prüfungen planen |
| UC-31 | AF-02, AF-10, AF-12, AF-21, AF-22, AF-23 | Lernergebnis in Kompetenzportfolio überführen |
| UC-32 | AF-13, AF-27 | Internen Studienkalendereintrag manuell pflegen |
| UC-33 | AF-06, AF-07, AF-08, AF-13 | Stundenplan importieren und bestätigen |
| UC-34 | AF-01, AF-13 | Persönliche Kalender ausschließlich lesend berücksichtigen |
| UC-35 | AF-06, AF-07, AF-13, AF-27 | KI-Lernplanung in internen Kalender übernehmen |
| UC-36 | AF-02, AF-14 | Änderung an autorisierter Studienquelle erkennen und anzeigen |
| UC-37 | AF-02, AF-06, AF-07, AF-13, AF-14 | Prüfungsverschiebung prüfen und neu planen |
| UC-38 | AF-04, AF-06, AF-07, AF-14, AF-27 | Zentralen Eingang „Zu prüfen“ und kontextuelle Vorschläge verwalten |
| UC-39 | AF-05, AF-15 (nur nachgelagerte Abschlussprüfung) | Projekt unabhängig oder modulbezogen anlegen |
| UC-40 | AF-05 | Projekt mit mehreren Modulen verknüpfen |
| UC-41 | AF-06, AF-07, AF-13, AF-15, AF-23 | Projektaufgaben und Ergebnisse verfolgen |
| UC-42 | AF-01, AF-03, AF-18, AF-23 | Ausgewähltes Repository lesend analysieren |
| UC-43 | AF-02, AF-12, AF-21, AF-22, AF-23 | Kompetenzen, Zertifikate und Nachweise pflegen |
| UC-44 | AF-02, AF-06, AF-07, AF-14, AF-23, AF-24 | Studienentscheidung mit Quellen vorbereiten |
| UC-45 | AF-01, AF-17, AF-19, AF-20, AF-25 | Unterstützte Integration aus Katalog verbinden |
| UC-46 | AF-01, AF-06, AF-07, AF-17, AF-18, AF-19, AF-20, AF-25 | KI-Dienst aufgabenbezogen auswählen und Kosten freigeben |
| UC-47 | AF-17, AF-19, AF-25 | Integrationsberechtigung deaktivieren oder widerrufen |
| UC-48 | AF-06, AF-07, AF-25, AF-27 | Administrationskonfiguration ändern und zurücksetzen |
| UC-49 | AF-22, AF-26 | Persönliche Daten kontrolliert einsehen und exportieren |
| UC-50 | AF-05, AF-06, AF-07, AF-22, AF-26 | Originale, persönliche Daten und Beziehungen kontrolliert löschen |

### F3.6.1 Zuordnung zu den fünfzehn Geschäftsprozessen

| F1-Prozess | Fachlich beteiligte Funktionen | Zuordnungsgrundlage |
|---|---|---|
| GP-01 | AF-01, AF-02, AF-06, AF-07, AF-08, AF-22 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-02 | AF-02, AF-05, AF-06, AF-07, AF-08, AF-12, AF-13, AF-15, AF-23 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-03 | AF-01, AF-02, AF-03, AF-04, AF-05, AF-06, AF-07, AF-14, AF-18, AF-19, AF-20, AF-26, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-04 | AF-01, AF-02, AF-03, AF-06, AF-07, AF-08, AF-09, AF-10, AF-11, AF-12, AF-16, AF-17, AF-18, AF-19, AF-20, AF-21, AF-22, AF-23, AF-25 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-05 | AF-02, AF-06, AF-07, AF-09, AF-10, AF-11, AF-12, AF-13, AF-18, AF-19, AF-20, AF-21, AF-22, AF-23 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-06 | AF-01, AF-02, AF-04, AF-06, AF-07, AF-08, AF-09, AF-13, AF-14, AF-15, AF-23, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-07 | AF-02, AF-04, AF-06, AF-07, AF-13, AF-14, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-08 | AF-02, AF-06, AF-07, AF-14, AF-23, AF-24 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-09 | AF-01, AF-03, AF-04, AF-05, AF-06, AF-07, AF-13, AF-15, AF-16, AF-18, AF-21, AF-23 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-10 | AF-01, AF-05, AF-16, AF-18, AF-19, AF-20, AF-21, AF-22, AF-26, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-11 | AF-01, AF-02, AF-03, AF-06, AF-07, AF-08, AF-10, AF-11, AF-12, AF-18, AF-21, AF-22, AF-23 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-12 | AF-04, AF-06, AF-07, AF-08, AF-14, AF-15, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-13 | AF-01, AF-06, AF-07, AF-17, AF-18, AF-19, AF-20, AF-25 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-14 | AF-06, AF-07, AF-25, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |
| GP-15 | AF-01, AF-05, AF-06, AF-07, AF-17, AF-19, AF-22, AF-25, AF-26, AF-27 | Zugeordnete tatsächliche F2-Anwendungsfälle; nur ihr jeweils zutreffender Funktionsanteil |

Die Zuordnung bezeichnet die fachlichen Funktionsanteile an den bereits in F2 festgelegten Prozessen. Sie erklärt keine technische Aufrufkette und macht einfache Erfassungsschritte nicht zu algorithmischen Funktionen.

### F3.6.2 Nachweis der bestätigten Entscheidungen

| Entscheidung | Fachliche Wirkung in F3 | Primäre Abnahme |
|---|---|---|
| FE-01 | AF-08/AF-16 dürfen unvollständige freiwillige Profile nicht als allgemeine Sperre behandeln; Einstieg in F2/B1 | UC-01, UC-17, UC-23 |
| FE-02 | AF-04 und AF-06 klassifizieren nicht ohne Zustimmung endgültig | UC-11, UC-12 |
| FE-03 | AF-09/AF-10 bestimmen adaptive Prüfzeitpunkte, keine starre Frage nach jedem Abschnitt | UC-24, UC-27 |
| FE-04 | AF-16 bildet sichtbaren Kurs-/Projektkontext sofort, erlaubt Korrektur | UC-18, UC-21 |
| FE-05 | AF-13/AF-14 erzeugen nach Quellenänderung nur bestätigungspflichtige interne Planung | UC-37 |
| FE-06 | AF-15 schließt offene Prüfungen und Projekte vom automatischen Archivieren aus | UC-10 |
| FE-07 | AF-11 bietet Hinweise und auf ausdrückliches Verlangen vollständige Lösung | UC-25, UC-26 |
| FE-08 | AF-06/AF-07 teilen **eine** Vorschlagsfassung und Entscheidung über mehrere Ansichten | UC-38 |
| FE-09 | AF-05 erhält das Original beim Entfernen einer einzelnen Beziehung | UC-13, UC-14 |
| FE-10 | AF-17 bis AF-20 wählen autorisierte geeignete KI-Angebote, bevorzugen zulässige freie Nutzung und sperren ungeplante Kosten | UC-45, UC-46 |
| FE-11 | AF-21/AF-22 erzeugen und pflegen vorläufige, korrigierbare pädagogische Erinnerung | UC-19, UC-24, UC-49, UC-50 |

## F3.7 Fachliche Prüfbeispiele und Grenzfälle

| Test | Eingabe / Situation | Erwartetes Ergebnis | Funktionen |
|---|---|---|---|
| T-01 | Student überspringt alle freiwilligen Profilfelder | Allgemeine Unterhaltung und zulässige Lernarbeit möglich; optionale Felder bleiben offen | AF-01, AF-16 |
| T-02 | KI möchte Dokument eigenmächtig einem Modul zuweisen | Erst Vorschlag; keine endgültige Änderung ohne Nutzerbestätigung | AF-04, AF-06 |
| T-03 | Gespräch wird aus Projekt gestartet | Kontext sichtbar automatisch gesetzt, korrigierbar, keine neue Ressourcenerlaubnis | AF-01, AF-16 |
| T-04 | Falsche Übungsantwort, Nutzer verlangt „nur einen Hinweis“ | Passender begrenzter Hinweis, nicht sofort vollständige Lösung | AF-10, AF-11 |
| T-05 | Danach „vollständige Lösung“ | Vollständige, bei Unsicherheit gekennzeichnete Erklärung; Hilfegrad bleibt sichtbar | AF-11, AF-12 |
| T-06 | Zwei Geräte beantworten denselben Vorschlag gegensätzlich | Keine widersprüchliche Doppelentscheidung; Konflikt sichtbar | AF-06, AF-07, AF-27 |
| T-07 | Eine PDF mit drei Arbeitsbereichen, einer wird gelöst | Original bleibt in anderen beiden verfügbar | AF-05 |
| T-08 | Semester beendet, Wiederholungsprüfung offen | Kein Archivvorschlag für offene Prüfung | AF-15 |
| T-09 | Externes Kalenderereignis kollidiert mit vorgeschlagener Revision | Verfügbarkeit nur lesend; Änderung ausschließlich nach interner Freigabe | AF-13 |
| T-10 | Prüfungstermin widerspricht neuer offizieller Quelle | Konflikt mit Herkunft und Hinweis; keine automatische interne Terminänderung | AF-02, AF-14, AF-06 |
| T-11 | Offiziell kostenlose integrierbare KI-Option fachlich geeignet | Kostenfreie Option wird innerhalb der Rechte bevorzugt | AF-17, AF-18, AF-19 |
| T-12 | Nutzer hat ChatGPT Plus, keine API-Berechtigung | Kein direkter API-Aufruf; nur zulässiger offizieller anderer Nutzungsweg | AF-17 |
| T-13 | Gratisquota erschöpft | Keine bezahlte Nutzung ohne bestätigten Kostenrahmen | AF-17, AF-19, AF-20 |
| T-14 | Manueller Modellwunsch widerspricht Datenschutzrechten | Modell ausgeschlossen, zulässige Alternative oder Abbruch | AF-01, AF-18 |
| T-15 | Modell fällt während unklar abgerechneten Aufrufs aus | Keine blinde Wiederholung, Status und Optionen erläutert | AF-19, AF-20 |
| T-16 | Wiederholt Fehler in SQL JOIN | Vorläufiger Lernhinweis, keine amtliche oder endgültige Minderkompetenz | AF-21, AF-23 |
| T-17 | Nutzer korrigiert eigene Lernpräferenz | Spätere Empfehlungen verwenden korrigierte Information | AF-22, AF-09 |
| T-18 | Nutzer löscht Chat, möchte pädagogische Erkenntnis behalten | Verlauf getrennt löschen; erhaltene Erkenntnis bleibt gekennzeichnet und kontrollierbar | AF-22, AF-26 |
| T-19 | Nutzer löscht eine pädagogische Erinnerung ausdrücklich | Eintrag nicht weiter aktiv verwenden, Löschstatus korrekt anzeigen | AF-22, AF-26 |
| T-20 | Verbundener Cloud-/Gerätekonflikt bei Datenlöschung | Nicht erreichter externer/lokaler Bereich bleibt als offen kenntlich | AF-26, AF-27 |
| T-21 | Admin versucht Sicherheitsgrenze als Konfigurationswert zu ändern | Änderung abgewiesen; vorheriger gültiger Zustand bleibt | AF-25 |
| T-22 | Projekt mit nicht nachgewiesenem Einzelbeitrag | Portfolio zeigt Unsicherheit statt erfundener persönlicher Kompetenz | AF-02, AF-23 |

## F3.8 Bewusst nicht in F3 spezifiziert

- **Oberflächengestaltung und Dialogsequenzen:** B1, soweit anwendungsfallbezogen F2; F3 spezifiziert keine Menüs oder Smartphone-Bildschirme.
- **Datenstruktur, Kardinalität, Lösch- und Versionszustände als Entitätsdefinition:** D1 und D2. F3 beschreibt die fachliche Entscheidung darüber, keine Datenbanktabellen.
- **Nichtfunktionale Schwellwerte, Verfügbarkeit, Sicherheit, Zugriffsverfahren, Aufbewahrungsfristen:** N1/N2 mit später überprüfbaren Zahlen und Verfahren.
- **Schnittstellenvertrag von externem ChatGPT, Claude, API-Modellen, Hochschulportalen, Kalendern, Benachrichtigungsdiensten und GitHub:** S1. Offizielle Integration nur, wenn tatsächlich nachgewiesen.
- **Interne Komponentenarchitektur, Frameworks, Sprachen, Speicherung, Hosting und Deployment:** spätere Architektur/Implementierung, nicht F3.
- **Generisches Anlegen/Löschen und Dateizugriff:** keine eigenständige F3-Funktion ohne algorithmische Besonderheit.
- **Rechtswirksame Hochschulentscheidung, amtliche Prüfung, tatsächliche Ergebnisvergabe:** verbleibt bei zuständigen externen Stellen.

## F3.9 Verweise und Nachvollziehbarkeit

| Dokument | Bedeutung |
|---|---|
| [P1 — Ziele und Rahmenbedingungen](P1-ziele-rahmenbedingungen.md) v0.5 | Ziele, Qualitätsanspruch, Kosten- und Datenschutzgrenzen, insbesondere CON-26/CON-34 und SC-48 |
| [P2 — Architekturüberblick](P2-architekturueberblick.md) v0.6 | Nachbarsysteme, nur lesende externe Kalender, KI-Integrationen, CFG-01–17, Datenklassen DK-01–12 |
| [F1 — Geschäftsprozesse](F1-geschaeftsprozesse.md) v0.2 | GP-01–15 und bereits bestätigte FE-01–06; fachliche Gesamtabläufe |
| [F2 — Anwendungsfälle](F2-anwendungsfaelle.md) v0.1 | Feste UC-01–50 und FE-07–09; Nutzerinteraktionen und Bestätigungsregeln |
| [Spezifikationsindex und Leseanleitung](README.md) | Bausteinabgrenzung und Status; nur der F3-Eintrag wird in dieser Überarbeitung aktualisiert |
| [Herold F3](https://github.com/carstenlucke/herold/blob/main/docs/spec/F3-anwendungsfunktionen.md) | Methodische Referenz der Anwendungsfunktion gegenüber F2, D1/D2, S1 und N2; keine fachliche Übernahme |
| [OpenAI: ChatGPT-/API-Abrechnung](https://help.openai.com/en/articles/9039756-managing-billing-settings-on-chatgpt-web-and-platform) | Zeitgebundene Primärquelle zum getrennten API-Zugang |
| [OpenAI: kostenloses ChatGPT](https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq) | Zeitgebundene Primärquelle zum kostenlosen Consumer-Angebot und seinen Nutzungsgrenzen |
| [Claude: Abonnement und API](https://support.claude.com/en/articles/9876003-i-have-a-paid-claude-subscription-pro-max-team-or-enterprise-plans-why-is-claude-api-usage-billed-separately-from-my-paid-claude-plan) | Zeitgebundene Primärquelle; Sonderrechte sind tarifbezogen zu verifizieren |

### F3.9.1 Änderungsnachweis gegenüber dem bereitgestellten Entwurf

| Präzisierung | Grund und fachliche Wirkung |
|---|---|
| AF-02: Herkunft und Prüfstand getrennt | Manuelle Eingabe, KI-Ableitung, Nutzerprüfung und amtlicher Nachweis sind unabhängige Merkmale; keine automatische amtliche Bestätigung durch einen überzeugenden Text |
| AF-06/AF-07: Begriffe aus F2.11.1 und Versionsbezug | „Später“ bleibt offen; Bearbeiten ist keine zusätzliche Endentscheidung. Annahme, laufende, teilweise, fehlgeschlagene und unklare Ausführung bleiben getrennt. Alte Entscheidungen werden nicht auf neue Fassungen übertragen |
| AF-05/AF-26: Linkentfernung und Originallöschung | Keine künstliche zweite Freigabe für bewusst manuelle Zuordnung; ohne Bestätigung der tatsächlichen Originallöschung erfolgt auch keine ersatzweise Linkentfernung |
| AF-11: direkte vollständige Lösung | Ausdrücklicher Lösungswunsch kann unmittelbar zur vollständigen Erklärung führen, ohne erzwungenen Vorversuch oder Hinweisrunde; Hilfegrad bleibt kenntlich |
| AF-01/AF-03/AF-15/AF-19/AF-25/AF-27: Algorithmusgrenzen | Fachliche Auswahl, Qualitätsbewertung, Abschlussfähigkeit, Budgetvergleich und Konfliktbewertung bleiben beschrieben. Authentifizierung, technische Durchführung, Statusdatenmodell und Protokolle werden nicht als F3-Algorithmen ausgegeben |
| AF-17 bis AF-20 und FE-10 | Consumer Free, Consumer-Abonnement, erlaubte freie API-Quote, kostenpflichtige Integration, lokales Modell und manueller externer Weg sind getrennt. Kostenlose geeignete erlaubte Nutzung wird bevorzugt; manuelle Wahl bleibt möglich innerhalb derselben Grenzen. Kein kostenpflichtiger automatischer Wechsel bei Erschöpfung |
| AF-21/AF-22 und FE-11 | Automatisch abgeleitete Erkenntnisse bleiben vorläufig; Herkunft, Gewissheit, Verwendbarkeit, Korrektur und Löschstand sind getrennt. Abschalten, Zweckwiderruf und Löschung haben unterscheidbare Folgen; Bestätigung allein ist kein ausgeführter Löschvorgang |
| Vollständige Rückverweise und fünfzehn GP | Katalog, Funktionsverwendung und UC-Matrix hatten unterschiedliche Teilmengen. Alle ursprünglichen AF-/UC-Zuordnungen sind erhalten und abgeglichen; vorhandene bedingte FE-08-Varianten sind ergänzt. Reine Neuanlage oder Anzeige löst daraus keine künstliche Abschlussprüfung oder neue Erinnerungsanalyse aus |
| Quellenstand und Status | Bearbeitungsstand 15.10.2026; die drei offiziellen Anbieterquellen sind wegen HTTP 403 nicht zeitaktuell inhaltlich verifiziert. Die Dokumentaufnahme wird von fachlicher Freigabe und tatsächlich implementierter Fähigkeit getrennt |

Die zusätzlichen Grenzfälle prüfen die jeweilige fachliche Regel und ersetzen keinen vorhandenen Prüfbedarf. Kein AF wurde entfernt, neu erfunden oder umnummeriert. Die grammatische Präzisierung des Titels von AF-18 ändert seine Identität und Auswahlaufgabe nicht. F3 ist auf dem vollständig übermittelten Entwurf aufgebaut; die in F2 dokumentierte Rekonstruktion der dortigen UC-17 bis UC-50 wird nicht durch eine abweichende Herold-Zuordnung ersetzt.

## F3.10 Prüfstand und offene Detaillierung

Die aktuelle Fassung enthält 37 algorithmisch begründete Anwendungsfunktionen (AF-01..37). F3.6 bewahrt die vollständige Ausgangsmatrix UC-01..50; die späteren UC-/DEC-V1-/FE-21-Anschlüsse stehen in F3.11–F3.14 und der [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md); `UC-01` benötigt aus methodischen Gründen keine künstliche Anwendungsfunktion. Die bestätigten Entscheidungen FE-01 bis FE-09 bleiben unberührt; FE-10 und FE-11 ergänzen die ausdrücklich bestätigten Anforderungen. Kostenloser Consumer-Chat ist ausdrücklich nicht mit kostenloser API gleichzusetzen. Es wird **kein bereits vorhandener API-Zugang, keine konkrete kostenlose API, keine verfügbare Abonnementintegration und keine Implementierung** behauptet.

Zur späteren Detaillierung in D1/D2, N1/N2, S1, B1 und Architektur bleiben insbesondere offen: konkrete erlaubte Anbieteranbindungen und ihr jeweiliger Gratis-/Abo-Status; überprüfbare Qualitätskriterien und Mindestleistung; Gebühren- und Quotalimits einschließlich unbekannter Provider-Verbrauchszustände; genaue Speicher-, Export- und Aufbewahrungsformate; Löschfristen und Backupprozesse; fachliche Kardinalitäten; Synchronisationskonfliktregeln und Authentisierungsdetails. Diese offenen Punkte berechtigen **nicht**, FE-01 bis FE-11 still umzudeuten oder Ereignisse in persönlichen externen Kalendern anzulegen, zu ändern oder zu löschen.

**Freigabestatus:** Zur Prüfung durch den Projektinhaber. Die Aufnahme dieser Dokumentfassung in die Spezifikationsbranche ist keine fachliche Freigabe und kein Nachweis implementierter Funktionen. Die ursprüngliche F3-Einzellieferung änderte P1/P2/F1/F2 nicht; die nachfolgenden Harmonisierungslieferungen einschließlich der DEC-V1-/FE-21-Konsolidierung betreffen die jeweils in E3 ausgewiesenen Bausteine.


## F3.11 Ergänzte fachliche Prüf- und Auswahlfunktionen

Die Entscheidungen FE-27 bis FE-89 ergänzen den Bestand. FE-56 war beim historischen Abgleich noch offen; seit der Eigentümerentscheidung aus Mission 19 vom 23.10.2026 sind Postfachlektüre, -synchronisation und -überwachung in V1 ausgeschlossen. Ausgehende OTP-/Sicherheitsmails, autorisierte Benachrichtigungen und manueller Import ausgewählter Inhalte bleiben möglich; eine spätere Integration ist unverbindlich. Die übrigen bestätigten Vorgaben bleiben erhalten. Die vollständige deutsche Entscheidungsmatrix und die zwölf Nachbarverträge stehen in [S1](S1-nachbarsysteme.md). Eine fachliche Entscheidung ist keine Aussage über implementierte Funktionen oder aktuell erteilte Anbieterrechte. Alle Bausteine bleiben **Zur Prüfung**. Historische Prüfstände, frühere FE-Teilmengen und alte Versionsbezüge bezeichnen ausschließlich ihre damalige Grundlage; maßgeblich ist der aktuelle Index mit [Änderungs- und Prüfnachweis](E3-pruefnachweis.md).

Diese Funktionen beschreiben fachliche Entscheidungen, keine Kryptographie, Middleware oder technische Authentifizierungsimplementierung.

### AF-28 — Berechtigungsschnittmenge und Supportumfang bestimmen

**Aufrufer:** UC-53, UC-54, UC-63; zugehörige B1-/B2-Abläufe.

**Eingabe:** Konto, Rolle, Objekt, Sitzung, Gerät, Feature, Freigabezweck und Ablauf.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Nur die Schnittmenge aktueller Rechte ist zulässig; explizite Verbote und Widerruf sperren. Support ist zeit- und objektgebunden standardmäßig lesend. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Sekundäradministrator kann sich trotz eigener Anfrage kein Super-Admin-Recht verleihen.

### AF-29 — Quotenwirkung und Neuaufnahme beurteilen

**Aufrufer:** UC-55, UC-59; zugehörige B1-/B2-Abläufe.

**Eingabe:** Globale Quotenvorgabe, Kontoausnahme, bestätigter Verbrauch und Neuaufnahmeumfang.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Ausdrückliche Kontoausnahme geht dem Grundwert vor; neue Konten erben Grundwerte. Bei Überschreitung nur neue betroffene Aufnahmen sperren und vor Grenzerreichung warnen. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Volle Medienquote lässt vorhandene Dokumente und Konto zugänglich.

### AF-30 — Funktionssichtbarkeit und Veröffentlichungsreife prüfen

**Aufrufer:** UC-55; zugehörige B1-/B2-Abläufe.

**Eingabe:** Featurefassung, Zustand, Testerrolle, Termin, unterstützte Funktion und aktuelles Recht.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Verborgen, bald, ausgewählte Tester und öffentlich unterscheiden; Termin allein ersetzt keinen tatsächlich erfolgreichen Release. Deaktivierung bewahrt Daten und sperrt neue Wirkungen. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Abgesagte Veröffentlichung erzeugt keine Ankündigung und keinen Direktzugriff.

### AF-31 — Quellversionsunterschiede und Ableitungsbedarf bestimmen

**Aufrufer:** UC-57; zugehörige B1-/B2-Abläufe.

**Eingabe:** Eigentümer, Quellidentität, belegte Revisionen, Annahme und Ableitungsbeziehungen.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Änderungsvorschlag vor Quellenübernahme; erst nach bestätigter neuer Version abhängige Ableitungen markieren und Aktualisierung zur Inhaltsprüfung vorbereiten. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Dateiname allein beweist keine identische Quelle; eine Ableitung wird nicht ungefragt ersetzt.

### AF-32 — Schutzvererbung und Analyseumfang bestimmen

**Aufrufer:** UC-58; zugehörige B1-/B2-Abläufe.

**Eingabe:** Quellschutz, abgeleitete Objekte, Geräte-/Schlüsselzustand und Vorgangsfreigabe.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Schutz erbt auf alle Ableitungen und Nebenansichten; lokale Verarbeitung bevorzugen; nur notwendiger eigener Cloudausschnitt pro ausdrücklich freigegebenem Vorgang. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Eine Zusammenfassung sensibler Quellen wird nicht als öffentlich indexierbar ausgegeben.

### AF-33 — Sichere Archivaufnahme fachlich qualifizieren

**Aufrufer:** UC-59; zugehörige B1-/B2-Abläufe.

**Eingabe:** Formaterkennung, Eintragsliste, Ordnerstruktur, Rechte, Quoten und bekannte Extraktionsgrenzen.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Pfadflucht, Bomben, ausführbare Inhalte und beschädigte Teile ablehnen beziehungsweise isolieren; Original und Extrakte getrennt, Provenienz und Fehlteile kenntlich. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Ein abgewiesener Teil gilt nicht als erfolgreich importiert; kein Extrakt überschreibt ein anderes Objekt.

### AF-34 — Wiederherstellungsmenge gegen Löschmarkierungen abgleichen

**Aufrufer:** UC-60, UC-61; zugehörige B1-/B2-Abläufe.

**Eingabe:** Eigene Sicherung, aktueller Objektstand, bestätigter Umfang und endgültige Löschmarkierungen.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Gelöschte Ziele und widerrufene Zugänge ausnehmen; neuere Fassungen schützen; Konflikte vor Übernahme anzeigen. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Ältere Sicherung und Offlinekopie heben eine endgültige Löschung nicht auf.

### AF-35 — Integrationswiederaufnahme und Historie qualifizieren

**Aufrufer:** UC-56; zugehörige B1-/B2-Abläufe.

**Eingabe:** Verbindungszustand, Scope, Einwilligung, Quellstand, Ergebnisnachweis und Restversuche.

**Vorbedingung:** Eigentum und tatsächliche Verfügbarkeit sind bekannt oder ausdrücklich unklar; unklare Pflichtberechtigung ist keine Erlaubnis.

**Regel und Ergebnis:** Manuell als Standard; Automatik nur pro Verbindung opt-in. Vor jedem begrenzten Retry Rechte, Kosten und tatsächliche frühere Wirkung prüfen; private minimale Historie führen. Das Ergebnis ist zulässig, gesperrt oder prüfbedürftig mit nachvollziehbarem Grund; die Funktion selbst erzeugt keine externe Nebenwirkung.

**Abnahmebeispiel:** Widerruf beendet geplante Läufe; unbekannter Erfolg wird nicht blind erneut ausgeführt.

## F3.12 Fachliche Paket- und Differenzprüfung für S2

### AF-36 — Portabilitätspaket und Importdifferenzen prüfen

**Zweck / Aufrufer:** UC-49, UC-60, UC-64 und BAT-24/25; [S2.5/S2.6](S2-datenmigration.md). AF-26 grenzt Umfang/Folgen ab, AF-34 filtert Lösch-/Entzugsgrenzen; diese Funktion ergänzt Schema-/Manifestabbildung und das konkrete fachliche Delta.

**Eingaben:** Eigentumskontext, unterstütztes Paket-/Fachschema, Manifest DT-86, ausgewählte Inhaltsbereiche, belegte Quellrevisionen, aktueller Ziel- und Kontrollstand, Schlüsselverfügbarkeit, Schutz und Quota.

**Ausgabe:** Versionierter exportierbarer Bestandsbericht oder Importdelta DT-88 mit Zuordnung neu/identisch/änderbar/konfliktbehaftet/ausgeschlossen/unsicher/fehlende Abhängigkeit; notwendige Bestätigung und begründete Auslassungen. Keine Nebenwirkung durch die Prüfung selbst.

**Fachliche Regeln:**

1. Nur dokumentiertes kompatibles Formatprofil auswerten; unbekannte Felder/Enumerationen als unverarbeitbar ausweisen, niemals als Code, Autorisierung oder Löschauftrag interpretieren.
2. Integritätsmerkmale und Mengen prüfen, ohne daraus automatisch Eigentum oder Inhaltsrecht abzuleiten. Gleicher Dateiname/Hash ist kein Kontonachweis.
3. Jede Referenz im eigenen Kontext auflösen oder als fehlend kennzeichnen; historische Zitate bleiben an ihrer Originalrevision.
4. Exportable Inhalte von ausgeschlossenen Geheimnissen, Sicherheits-/Rollenobjekten und Fremddaten trennen; importierte Historie bleibt inaktiv.
5. AF-28/AF-34 anwenden, Schutzvererbung und aktuelle Quota prüfen. Endgültige Löschung lässt sich auch nicht als neue Kopie umgehen.
6. Quell-/Zielrevisionen gegenüberstellen; jüngere Evidenz und manuelle/gesperrte Sitzungen erhalten. Keine KI-Schätzung wird zur amtlichen Note.
7. Ergebnisfassung mit tatsächlicher Auswahl und Vergleichsgrundlage binden. Ändert sich die Grundlage, Ergebnis vor Wirkung neu prüfen und relevante Entscheidung erneut einholen.
8. Nur tatsächlich erfolgreiche Wirkungen als angewandt kennzeichnen; fachliche Wiedererkennung von erneutem Jobstart unterscheiden.

**Prüfbeispiele:** Ein unbekanntes Feld `super_admin=true` ist nicht übernehmbar. Ein Paket ohne Quellseite erhält eine Quellenlücke statt erfundener Seiten-/Zeitpräzision. Gleiche Paketdatei nach endgültiger Originallöschung bleibt für dieses Ziel gesperrt. Ein Export ohne passende Schlüssel wird nicht als entschlüsselt vollständig ausgewiesen.

**Abgrenzung:** Konkretes Serialisierungsschema, Parser, Signatur/Kryptographie, Speichermechanismus und technische Transaktionsstrategie bleiben N2/Architektur; AF-36 bestimmt fachliche Zulässigkeit und erwartetes Ergebnis.

## F3.13 Geltungs- und Anforderungsabgleich

### AF-37 — Studienvorgaben auf Geltung und Abdeckung prüfen

**Aufrufer / Eingabe:** UC-66, gegebenenfalls UC-03/UC-44/UC-57; persönlicher DM-04-Kontext, versionierte DM-21/DM-23-Quellen und bestätigte strukturierte DM-24-Ableitungen, persönliche Module/Leistungen/Prüfungsversuche. Datentyp DT-95.

**Verarbeitung:**

1. Zulässige Quellen nach AF-01/AF-02 prüfen; offiziellen Charakter, Versionsdatum und persönliche Geltung getrennt bestimmen.
2. Hochschule, Studiengang, Prüfungsordnung, Einschreibung/Kohorte, Inkrafttreten und Übergangsregeln abgleichen; unzureichende Geltung als ungeklärt statt gültig ausgeben.
3. Nur bestätigte nachvollziehbare Extraktionsfassung verwenden. Pflicht-/Wahlpflichtgruppe, ECTS-Grenze, Voraussetzungen und Prüfungsform/-versuchsbezug mit Quellenstelle führen; unbekannte Semantik nicht durch KI-Gewissheit ersetzen.
4. Istbelege passend zuordnen, Originalskala/Nachweisgrad erhalten. Doppelte ECTS-Anrechnung oder Zuordnung zu Wahlpflichtalternativen braucht belegte Regel; keine erfundene Fehlprüfung.
5. Ergebnis je Anforderung als belegt erfüllt, Abweichung belegt, Nachweis fehlt oder nicht prüfbar samt Beleg/Geltungsfassung ausweisen. Nur über den bestätigten abgedeckten Umfang eine Aussage machen.
6. Bei Quellen-/Kontextwechsel neuen Vergleich vorbereiten; keine automatische Übernahme in Leistungen, Kalender oder institutionelle Anerkennung.

**Ausgabe / Grenzen:** Eigene geschützte Inhaltsableitung mit Soll/Ist/Differenz, fehlenden Nachweisen und Unsicherheiten. Die Funktion führt keine Hochschulanmeldung oder Datenkorrektur aus und benötigt keinen Konnektor oder verpflichtenden LLM-Aufruf. Bekannte strukturierte Regeln sind KI-frei vergleichbar; KI-Extraktion bleibt ein gesondert zulässiger, prüfpflichtiger Weg.

**Abnahme:** Neueres Handbuch mit anderer Kohorte wird nicht automatisch gültig. Bei passender Übergangsregel kann die ältere belegte Ordnung maßgeblich sein. Fehlendes ECTS-Feld bleibt unbekannt, nicht null; Abgleich bestätigt keine amtliche Anerkennung.

## F3.14 FE-21 — Fachliche Prüfung der Ausgabevariante

Die FE-21-Ausgabevariante in UC-20 ist von FE-20-Spracherkennung/Live-Eingabe getrennt. Sie verwendet vorhandene Funktionen: AF-01 prüft aktuellen Zugriff auf DM-25/DM-26 und das Gerät, AF-16 bildet nur den gewählten zulässigen Antwortkontext, AF-17/AF-18 beurteilen tatsächlich verfügbare offizielle TTS-Optionen, AF-19 Kosten/Quota und AF-32 Schutzvererbung. AF-25 validiert ausschließlich unterstützte persönliche Sprach-/Ausgabepräferenzen in DT-61/DM-48. Kein neuer AF und kein fachlich fingierter TTS-Algorithmus; die technische Synthese gehört nach S1/Architektur.

**Fachliches Ergebnis:** Zulässiger Ausgabetext, tatsächlich unterstützte Sprache/Stimme/Geschwindigkeit und Freigabeumfang oder nachvollziehbare Ablehnung. Laufende Wiedergabe, Pause, Fortsetzung, Replay und ein ausdrücklich aktivierter Hörmodus werden von UC-20/DLG-26 gesteuert, nicht durch periodische Analysejobs. Hören benötigt kein Mikrofonrecht, nimmt keine neue Lernleistung an und erzeugt keine dauerhafte pädagogische Erinnerung allein durch Abspielen.

**Negative Abnahme:** Verbraucherabo ohne API-Recht, unbekannte TTS-Kosten, widerrufene Inhaltsfreigabe oder nicht verfügbare Stimme ergeben keine automatische andere Verbindung. Text bleibt zugänglich. Automatische Ausgabe ohne Aktivierung bleibt aus. [D1](D1-datenmodell.md), [D2](D2-datentypen.md), [B1](B1-dialogspezifikation.md), [S1](S1-nachbarsysteme.md) und die [FE-21-Matrix](ENTSCHEIDUNGSMATRIX.md#4-fe-21--getrennte-ausgabevariante-und-abnahme) führen die Nachweise.

### F3.14.1 Audioauswahl und Konfigurationsprüfung (Mission 15)

AUDIO-01/02/03 vertiefen bestehende AF-01/AF-17/AF-18/AF-19/AF-25/AF-28/AF-32; keine neue AF oder Motorimplementierung. Eingaben sind aktuelles Konto, Sprach-/Geltungsbereich, persönliche Auswahlfassung, Gerätefähigkeit, zulässiger Ton-/Stimmenkatalog, Anbieterfreigaben, aktuelle Serverflags und Quoten. UC-65 nutzt dieselbe validierte Tonpräferenz wie DLG-50, keine konkurrierende zweite Einstellung.

1. Zwingende Konto-/Inhalts-/Geräte-/Anbieterrechte und administrative Verfügbarkeit schneiden; Nutzerpräferenz kann keine Grenze erweitern, Adminstandard kein ausdrückliches Aus überschreiben.
2. Für Benachrichtigung den In-App-Ton oder Lautlos unabhängig vom visuellen Hinweis bestimmen; OS-/Push-Fähigkeit separat bewerten. Bestehende Ruhe-/Ereignis-/Kanalregeln bleiben vorgeschaltet.
3. Für Sprachausgabe Audiosprache unabhängig von der Oberfläche und dort gewünschte verfügbare Stimme prüfen; je Sprache mehrere erlaubte Stimmen nur bei tatsächlicher Motorfähigkeit anbieten. Unbekannte/entfernte Stimme als unverfügbar erklären, keine unbemerkte Ersatzroute.
4. Vorschau nur nach ausdrücklicher Aktion auf neutralem Text/Ton und innerhalb der Anbieter-/Kostenrechte zulassen. Unterstütztes Tempo/Volumen validieren; fehlende Fähigkeiten nicht als erfolgreiche Änderung ausgeben.
5. Aktive Hörsitzung getrennt von gespeicherter Präferenz prüfen. Standard aus; Wiederanmeldung/Gerätewechsel reaktiviert sie ohne bestätigte geprüfte Regel nicht. Entzug beendet betroffene Ausgabe/Warteschlange; Fortsetzen prüft heutige Rechte erneut.
6. Rücksetzen zeigt den konkreten Bereich und wirksame Standards, wahrt persönliche Datenschutzentscheidungen und Rechte; es startet weder Vorschau noch Hörmodus und löscht keine Nachrichten oder Erinnerungen.

**Ergebnis/Abnahme:** Gültige effektive Auswahl samt Herkunft/Fähigkeitsgrenze oder begründete Ablehnung; bei Lautlos bleibt visueller Hinweis, bei Mikrofonverweigerung bleibt zulässiges TTS. Administration kann einen Motor sperren, aber weder Kosten ohne Freigabe auslösen noch ein persönliches Opt-in ersetzen. [B1.13](B1-dialogspezifikation.md#b113-abnahmeszenarien-für-töne-und-stimmen) enthält die Sollfälle.
