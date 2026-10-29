# Entwicklungszuordnungen — bestätigter Teilstand

**Projekt:** Syllentra AI\
**Version:** 0.2\
**Stand:** 22.10.2026\
**Status:** Zur Prüfung durch den Projektinhaber

## 1. Herkunft und Ausarbeitungsgrenze

Am Ausgangs-HEAD `53ef171be4783748b5c7e3a84bb0cc363d5b4194` existiert im Repository kein vollständiger Meilensteinplan mit M2b/M5/M8. Die historische [Roadmap](../ROADMAP.md) enthält Forschungs-/Entwicklungsphasen, keine freigegebene entsprechende Meilensteinliste. Diese Arbeitsunterlage hält ausschließlich die bestätigten Zuordnungen des Auftrags vom 19.10.2026 fest; keine weiteren Meilensteine, Termine, Budgets, Anbieter oder Gesamtfreigabe werden erfunden. Bestehende Meilensteine eines Gesprächsentwurfs werden weder ersetzt noch umnummeriert; der vollständige Entwurf bleibt als Quelle nachzureichen/gesondert abzugleichen.

## 2. Bestätigte Zuordnungen

| Bezug | Bestätigter Umfang / Änderung | Voraussetzung und Abnahmegrenze |
|---|---|---|
| M2b | UC-39: grundlegende persönliche Projektverwaltung früh verfügbar vorsehen | Eigene Projektanlage/Basisorganisation ohne Pflichtmodul; Konto-, Daten- und Dateirechte. Keine Repositoryanalyse oder generative Projektassistenz als Voraussetzung. |
| M5 | UC-09: eigene Noten, ECTS und dokumentierte Prüfungsleistungen erfassen | Institutionelle Skala, Herkunft, geschützte Notendetails, keine Gleichsetzung mit KI-Kompetenz. |
| M5 | UC-65 intern: persönliche Regeln, Ereignispunkte, In-App-Hinweise und geschützter Verlauf | Wirksame Ereignisrevisionen, J−5/J−1, individuelle Regelpriorität, Ruhezeit 22:00–08:00 konfigurierbar; kein LLM oder Pushdienst nötig. |
| M8 | UC-65 erweitert: OS-Push, bevorzugtes Hauptgerät/freiwillige weitere Geräte, Tagesdigest, optionale E-Mail-Erinnerungen und externe Zustellnachweise | Interne M5-Hinweise/Regeln, tatsächliche OS-/Dienstrechte, Widerruf, Ruhe-/Datenschutz-/Deduplizierungsregeln. Keine automatische Erinnerungsmail. |
| Früh vorbereiten; Meilensteinnummer nicht bestätigt | UC-16/UC-59: zulässiger Audioimport und Transkription | Datei-/Archivgrenzen, Rechte, Herkunft/Quellrevision, Speicher-/Hardwarefähigkeit; Aufnahme ist keine Pflicht. Transkription braucht ggf. ein spezialisiertes Sprachmodell, keinen LLM als solchen. |
| Mit KI-Kern; Meilensteinnummer nicht bestätigt | Strukturierte KI-Lernnotizen aus tatsächlich verfügbaren Materialien/Transkripten | KI-Kern, geeignete rechtmäßig nutzbare Modelle, geprüfte Quellen, Schutzvererbung und kontrollierte Transkriptbereinigung; kein Pflicht-Pay-API. |
| Nach Daten-/Planungsgrundlagen; Meilensteinnummer nicht bestätigt | L-08: hybride adaptive Wiederholung und aktivierbare pädagogische Reihenfolge | Lernziel-/Themenstruktur, tatsächliche Antworten/Hilfen/Evidenz, verfügbare Zeit, revisionierter DM-75/DM-76-Plan und Konflikt-/Undo-Grenzen zuerst; Kalenderbestätigung bleibt getrennt. |

M5-/M8-Zuordnung ordnet Entwicklung, ist keine Behauptung heute implementierter Funktionen. Sichtbarkeit und Nutzbarkeit folgen weiterhin realer Implementierung, Tests und aktuellen Funktions-/Rollenrechten.

## 3. Abhängigkeit vom LLM, anderen Modellen und KI-freien Funktionen

| Funktionsbereich | KI-frei möglicher Grundumfang | LLM-/sonstige Modellabhängigkeit und Grenze |
|---|---|---|
| Lernreihenfolge / L-08 | Zeit-/Evidenzregeln, beobachtete Wiederholungen, Priorisierung, Aktivierung/Verlauf/Undo und Kalendergrenzen | Erzeugte alternative Erklärungen/Übungen können geeigneten KI-Kern benötigen; vorhandene geprüfte Alternativen bleiben nutzbar. Konkrete Wiederholungsformel und pädagogische Wirksamkeit offen, kein willkürlich festgelegter Algorithmus. |
| Erinnerungen / L-04 | Datum-/Zeitregeln, individuelle Einstellungen, Ruhezeiten, In-App-Verlauf und Deduplizierung | Kein LLM erforderlich. Externe Push-/Mailzustellung ist Dienst-/OS-Abhängigkeit, keine LLM-Abhängigkeit. |
| Studienvorgaben / L-09 | Manueller Dokumentimport, strukturierte Eingabe/Geltungsprüfung und Soll-Ist-Vergleich bekannter Regeln | OCR/Formatanalyse kann spezialisiertes Modell benötigen, semantische KI-Extraktion ggf. LLM. Beides nur tatsächlich unterstützt, rechtmäßig und geprüft; Nutzerprüfung/Quellgeltung bleiben erforderlich, kein Hochschulkonnektorzwang. |
| Lernmodus / L-02 | Zugängliche Minimalansicht, Bewegungsreduktion, Zustands-/Entwurferhalt und getrennte Fortschrittsanzeigen | Keine LLM-Pflicht; generative Tutorantworten folgen unabhängig bestehenden KI-Rechten und Verfügbarkeit. |
| Audioaufbereitung | Dateiimport, sichere Ablage, Quellen-/Versionsbezug und zulässige manuelle Textbereitstellung | Automatische Transkription ggf. spezialisiertes Sprachmodell; strukturierte KI-Lernnotizen mit KI-Kern erst danach. Keine nicht nachgewiesene Browser-/Hardware-/Gratisgarantie. |

## 4. Offene Planungs-/Nachweisarbeit

Gesamtmeilensteinplan samt übrigen Zuordnungen ist nicht im Repository belegt. Es werden keine Meilensteine hinzugefügt oder Reihenfolgen zwischen unbenannten Gesprächsmeilensteinen behauptet. Unterstützte Sprach-/OCR-/LLM-Fähigkeiten, Hardware, Lizenzen, Kosten, Pädagogikevaluation und Produktabnahmetests bleiben nachzuweisen. Keine Framework-/Datenbank-/Hosting-/Modellwahl. Die vier L-Entscheidungen allein deckten nicht alle 25 DEC-V1 ab; deren dokumentarische Konsolidierung steht nun in der [Entscheidungsmatrix](ENTSCHEIDUNGSMATRIX.md). Dieser Teilplan wird dadurch weder zu einem Gesamtplan noch um neue Meilensteine erweitert. DEC-48/49 sind Bewertungs-/Schutzziele nach [ADR](../ARCHITECTURE_DECISIONS.md), keine autorisierten Infrastrukturtests oder Ausgaben.

Verträge und Belege: [F2](F2-anwendungsfaelle.md), [F3](F3-anwendungsfunktionen.md), [D1](D1-datenmodell.md), [B2](B2-batch.md), [S1](S1-nachbarsysteme.md), [N1](N1-nichtfunktional.md), [E3](E3-pruefnachweis.md) und [Index](README.md). Alle Prüfentwürfe bleiben zur Prüfung.
