# Kostenmodell und Machbarkeit

**Version:** 0.3 · **Stand:** 23.10.2026 · **Status:** Architekturprinzipien (A) in Mission 21 bestätigt; konkrete Zielwerte/Tarife (B) und Messnachweise (C) offen

> **Fortschreibung Mission 7:** Für künftige Vergleiche gilt jetzt bis zu **20 EUR brutto/Monat**, keine Ausgabe genehmigt. Die nachfolgenden 10-EUR-Aussagen/Rechnungen dokumentieren den früheren Untersuchungsstand aus Mission 5/6; sie sind keine aktuelle Obergrenze. Auch unter 20 EUR ist vollständige V1-Leistung nicht nachgewiesen. [Bestätigter Rahmen](../ARCHITECTURE_DECISIONS.md#adr-0006--persönlicher-qualitätsfokus-und-vergleichsrahmen-aus-mission-7).

## 1. Kostenstatus und Rechnungsmethode

**Keine Ausgabe genehmigt.** 10 EUR brutto/Monat ist eine Vergleichsgrenze, keine Buchungsfreigabe. Primärhost-/Mail-/Domainpreise waren aus offiziellen Websites nicht lesbar und sind **nicht verifiziert**. Deshalb gibt es keine scheinpräzise Gesamtpreisgarantie und keine behauptete vollständig kostenlose V1. [Quellen](QUELLEN.md), 22.10.2026. Softwarelizenzkosten, Infrastrukturverbrauch und eigene Betriebszeit getrennt führen.

Monatliche Gesamtkosten = Primärcompute + primärer Speicher/IO + Netz/IPv4/Transfer + Backupplatz/Requests/Restoretransfer + Domainjahrespreis/12 + DNS/Monitoring + notwendige Sicherheitsmail + Inferencehardware/-verbrauch + ggf. genehmigte optionale Dienste + Steuern/Umrechnung. Reserven, Retentionwachstum und Wartung getrennt ausweisen. Nicht gemessene Größen bleiben Variablen, keine Null. Eigenleistung = Stunden × bestätigter Bewertungsansatz; keine behauptete kostenlose Wartung.

## 2. Planungsszenarien, keine Produktzusagen

Die Zahlen sind explizite **Untersuchungshypothesen**, keine bestätigten Nutzer-/Datei-/Lastgrenzen und kein Benchmark. CPU/RAM vor Umsetzung messen. Ein registrierter Nutzer ist nicht gleich eine gleichzeitig laufende Inferenz.

| Szenario | Konten / gleichzeitige Nutzer | Material / angenommener Backupbestand | KI-/Medienlast als Messprofil | Compute-Messhypothese |
|---|---|---|---|---|
| Persönlicher Prototyp | 1 / 1 | 5 GB / 10 GB | 10 Antworten/Tag à 500 Ausgabetoken; 30 Min. Audio/Tag | 4 CPU / 8–16 GiB für kleine quantisierte Modelle und begrenzte Jobs; kein notwendiger persönlicher Dauer-PC |
| Kleine Multiuser-V1 | 5 / 2 | 50 GB / 100 GB | 50 Antworten/Tag; 2 Std. Audio/Tag | 4 CPU / 16–24 GiB; RAM-/Queuekoexistenz und Latenz offen |
| Simultane V1 | 20 / 5 | 200 GB / 400 GB | 250 Antworten/Tag, 5 Std. Audio/Tag; Burst gleichzeitiger KI-Anfragen | 8 CPU / 24–32 GiB als Prüfprofil, keine Eignung von 4 Gratis-OCPU zugesagt |
| Wachstum | 100 / 20 | 1.000 GB / 2.000 GB | 1.000 Antworten/Tag, 20 Std. Audio/Tag | Getrennte begrenzte Worker/GPU oder stärkere CPU erst nach Messung; kein Gratisprofil belegt |

Zweifacher Backupbestand ist eine Kostenhypothese, kein fixer Deduplizierungs-/Kompressionsfaktor. Modelle, Originale, tägliche Änderungen, Versionen, Logs und temporäre Dateien können darüber liegen; Videobitrate/Materialdauer gesondert bestimmen. Parallelität kann Warteschlange statt Parallelprozess bedeuten; das muss die später bestätigten Antwortziele erfüllen. Die [KI-Studie](KI_UND_MODELLE.md) zeigt Gewichtsspeicher, Ressourcenreserven und fehlende Benchmarks.

## 3. Tatsächlich belegte Teilpreise: R2 Standard

Offizieller Dokumentationsquelltext, nicht Vertragsangebot: [Preisseite im offiziellen Repository](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/r2/pricing.mdx). **USD**, keine EUR-/Bruttoangabe. Standard: 10 GB-Monat, 1 Mio. Class-A- und 10 Mio. Class-B-Operationen monatlich frei; darüber 0,015 USD/GB-Monat, 4,50 USD/Mio. A, 0,36 USD/Mio. B. Anbieter rundet abrechenbare Einheiten auf; tatsächlich kostenpflichtige Mengen/Requests prüfen. Laut Quelle kein R2-Internet-Egressentgelt, aber mögliche andere Dienst-/Primärhost-/Netzkosten bleiben.

| Hypothetischer Backupbestand | Kosten nur Speicher nach Freimenge | Nicht enthalten |
|---|---|---|
| 10 GB-Monat | 0 USD | Requests oberhalb Freimenge, Primärhost, Mail, Domain, Steuer, Wartung |
| 100 GB-Monat | (100 − 10) × 0,015 = **1,35 USD** | Wie oben; kein Gesamtpreis |
| 400 GB-Monat | (400 − 10) × 0,015 = **5,85 USD** | Wie oben; kein Gesamtpreis |
| 2.000 GB-Monat | (2.000 − 10) × 0,015 = **29,85 USD** | Wie oben; Vergleichsgrenze bereits offensichtlich kritisch, Wechselkurs/Steuer offen |

Infrequent Access kostet laut Quelle 0,01 USD/GB-Monat, hat aber zusätzliche Abrufpreise und Mindesthaltungsdauer und **keine Standard-Freimenge**. Für häufige Restore-/Prunetests nicht automatisch billiger. Änderungen an restic-Packs, Listing/Prune, Wiederholung und Restore generieren eigene Requests; nicht nur Dokumentzahl zählen. EU-Jurisdiction, Vertrags-/Steuer-/Abrechnungsbedingungen vor Auswahl bestätigen.

## 4. Architekturbezogene Kostenspannen als bedingte Formeln

| Architektur | Kostenlos / bedingt | Kostenpflichtig oder unklar | Gesamturteil |
|---|---|---|---|
| A OCI zentral + unabhängiges Backup | Open-Source-Bausteine nach Lizenzprüfung ohne Lizenzgebühr; OCI nur innerhalb tatsächlich zugeteilter bestätigter Freimenge; R2 Standardfreimenge nach offizieller Quelle | Backupmehrmenge oben, Mail/Domain/IO/Transfer, eventuell fehlende Gratiscompute-Kapazität; heutige OCI-Tarife nicht verifiziert | Kleinster laufender Geldbedarf möglich, **≤10 EUR brutto nicht nachgewiesen**; nicht einfach „0 EUR“ |
| B Hetzner zentral + unabhängiges Backup | Softwarelizenzen nach Prüfung, eigenes Monitoring ohne zusätzliche SaaS-Gebühr | VM/RAM/IPv4/Volumes, zuverlässige Mail, Domain und Backup; aktuelle Einzelpreise unbekannt | Planbarer bezahlter Compute als Konzept; **kein verifiziertes Angebot unter 10 EUR** |
| C Scaleway zentral/Managed + unabhängiges Backup | Softwarelizenzen nach Prüfung; Providerbündelung kann Koordinationsaufwand senken | Compute plus ggf. DB-/Objekt-/Mail-Mindestkosten; aktuelle Tarife/Regionen unbestätigt | Mehr Managed Services nicht gratis; **kein verifiziertes Angebot unter 10 EUR** |
| Nur bei Mehrwert: getrennte EU-Inferenz | Keine verpflichtende bezahlte KI-API, eigene Gewichte nach Lizenzprüfung möglich | Zusätzliche Hardware/Netz/Betrieb, optional explizit genehmigter Dienst | Gegenwärtig keine belastbare 10-EUR-Lösung; nicht automatischer Fallback |

Zu ergänzende Angebotsmatrix vor Entscheidung: SKU/Region/Architektur, Mengen und Messprofil, netto/brutto, Währung, Monats-/Stunden-/Mindestpreis, Freimengen/Überziehungsregel, IPv4/Egress/IO/Backup/Restore, Mail, Domain/DNS, mögliche Account-/Zahlmittelpflicht, Kündigung/Suspendierung und Preisstand. **Nur aktuelle Quellen oder konkretes schriftliches Angebot können die offenen Variablen schließen.** Keine hypothetischen VMpreise erfinden.

## 5. Machbarkeit und Kostenkontrolle

Ein finanziell kostenloser Prototyp kann funktional eingeschränkt sein; diese Einschränkung wird nicht zur stillen Kürzung bestätigter V1-Anforderungen. Sichere Kernfunktionen lassen sich ohne LLM bedienen, aber die bestätigten KI-Funktionen werden damit nicht als erfüllt ausgegeben. Wenn Ressourcen/Lizenzen/Antwortziele nicht zusammenpassen, Eigentümer muss nach Belegen Kapazität/Budget/Umfang ausdrücklich entscheiden; keine eigenmächtige Abschwächung oder Ausgabe.

Quoten vor Start und während Verarbeitung, globale und kontobezogene Limits, Modellresidenz, maximale Kontext-/Ausgabebudgets, faire Jobs und temporäre Bereinigung vorsehen. Warnung allein ist keine Kostensperre. Erforderliche bezahlte Wege ohne Freigabe blockieren, bereits gespeicherte zulässige Daten les-/exportier-/löschbar halten. Keine automatische Tarif-/GPU-/APIbuchung; kostenlose Modellgewichte machen Inference nicht kostenlos.


## 6. Vom Projektinhaber bestätigte Architekturprinzipien aus Mission 21 (TECH-O-12, TECH-O-13, TECH-O-14 und Kosten-/Quotenschutz)

Am 23.10.2026 hat der Projektinhaber die folgenden Leistungs-, Budget-, Lizenz- und Governanceprinzipien bestätigt ([ADR-0021](../ARCHITECTURE_DECISIONS.md#adr-0021--querschnittsentscheidung-kontrollierte-multi-provider-austauschbarkeit-und-fallback-grenzen), [ADR-0022](../ARCHITECTURE_DECISIONS.md#adr-0022--leistungsziele-rportoslo-quoten-und-20-eur-untersuchungsrahmen-tech-o-12), [ADR-0023](../ARCHITECTURE_DECISIONS.md#adr-0023--vollständiges-lizenz--artefakt--datenschutz--und-kommerzialisierungsinventar-tech-o-13), [ADR-0024](../ARCHITECTURE_DECISIONS.md#adr-0024--pace-berechtigungsmodell-und-freigabevorbehalt-vor-v1-entwicklung-tech-o-14)):

| Bezug | A. Bestätigtes Architekturprinzip | B. Offene technische Unterentscheidungen | C. Ausstehende Nachweise |
|---|---|---|---|
| **TECH-O-12 — Leistung, RPO/RTO/SLO und Budgetrahmen** | Systematische Messung von Last, Latenz, Verfügbarkeit, Warteschlangen und Ressourcen; Festlegung bezifferter **RPO-, RTO- und SLO-Ziele** vor Produktionsstart; datenklassenbezogene Retentionsregeln; faire Quoten und Limits pro Konto; indikativer Orientierungsrahmen von **20 EUR brutto/Monat für die persönliche Phase** ohne Ausgabenautorisierung; strikte Trennung zwischen persönlicher Erprobung und öffentlicher V1-Öffnung. | Konkrete Zahlenwerte für RPO/RTO/SLO, Retentionsfristen und Kontokontingente. | Ausführung der Messprotokolle (`T01`–`T08`), Verifikation aktueller Anbieterpreise und Nachweis technisch wirksamer Kosten-/Quotensperren (`N1.10`, `S3.6/14`, `REL-Q01..Q05`). |
| **TECH-O-13 — Lizenzen und Compliance** | Vollständiges Inventar für jede Komponente, Abhängigkeit, jedes Modell, Gewicht, jede Stimme und jedes Artefakt (Version, Provenienz, Lizenz, Vertragsbedingungen); Vorzug permissiver Lizenzen ohne automatischen Ausschluss kompatibler Lizenzen; Prüfung der DSGVO-Rollen, Regionen, Transfers und Unterauftragsverarbeiter sowie der künftigen Kommerzialisierbarkeit nach tatsächlich genutzten Komponenten. | Einzelfreigabe konkreter Modellgewichte, Stimmenkarten, Medienbibliotheken und Anbieterverträge. | Vollständige Lizenz-/Hash-/SBOM-Prüfung und datenschutzrechtliche Vertragsprüfung vor Einführung (`O-S3-10`, `REL-S17/A13/A18`). |
| **TECH-O-14 — PACE-Berechtigungen** | Getrennte PACE-Missionen (`READ_ONLY`, `EDIT/DRAFT`, `COMMIT/PUSH/PR`, `TEST_CLOUD/DEPLOY`); Agentenautonomie im ausdrücklich genehmigten Umfang; zusätzliche Genehmigungen für Installationen, große Downloads, Cloud-Tests, Ausgaben und sensible Aktionen; **kein automatischer Merge nach `main`**; Spezifikationsvalidierung und manueller Merge vor offiziellem V1-Entwicklungsstart. | Konkrete Einzelmandate für künftige Benchmark-, Cloud- oder Entwicklungsmissionen. | Formale Eigentümerabnahme der Spezifikation (`Zur Prüfung` → `Freigegeben`), genehmigte Testläufe und manueller Merge nach `main`. |
| **Querschnitt — Kosten- und Quotenschutz** | Niemals automatische Ausgaben oder Tarif-Upgrades auslösen; niemals Beschränkungen kostenloser Tarife (Free Tiers) umgehen; bei Erschöpfung autorisierter Quoten bleiben alle übrigen Anwendungsfunktionen nutzbar. | Konkrete Quoten-Schwellen und Degradationspfade je Adapter. | Negativtests für Quota-Erschöpfung und Kostenblockade (`AT-S3-18`, `AT-AUDIO-09`, `REL-Q01..Q03`). |
