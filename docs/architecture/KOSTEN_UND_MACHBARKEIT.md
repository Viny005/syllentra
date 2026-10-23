# Kostenmodell und Machbarkeit

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

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
