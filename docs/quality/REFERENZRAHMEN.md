# Syllentra AI — Referenzrahmen für Qualitäts- und Sicherheitsprüfungen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Zur Prüfung durch den Projektinhaber

## 1. Verwendung und Verifikationsgrenze

Die Referenzen begründen ausgewählte Risiken und Prüfmethoden für [N1](../spec/N1-nichtfunktional.md), [N2](../spec/N2-querschnittskonzepte.md) und die [46 Kontrollprofile](RELEASE_KONTROLLMATRIX.md). Sie werden weder vollständig importiert noch als Zertifizierung, Rechtsberatung oder bereits erreichte Konformität ausgegeben. Ein Standardverweis beweist keine Umsetzung. Kein ASVS-Prüfniveau oder neuer rechtlicher Vertragsstatus wird hier beschlossen.

Am 22.10.2026 wurden offizielle Projektquellen über die zugänglichen GitHub-Repositories gelesen. Die Hauptwebsites von OWASP/GenAI, W3C, NIST und EUR-Lex waren aus der Arbeitsumgebung mit HTTP-/Tunnel-403 nicht erreichbar; auch die überprüfte alternative Zugriffsberechtigung beseitigte das nicht. Nachfolgend wird deshalb zwischen tatsächlich gelesener Ausgabe und bibliographischer, **noch online zu verifizierender** Referenz unterschieden. Fehlende normative Verifikation bleibt vor darauf gestützter Produktfreigabe offen; die Dokumentarbeit kann fortgesetzt werden.

## 2. Ausgaben, offizielle Quellen und tatsächlicher Abrufstand

| Referenz | Ausgabe / Status | Tatsächlich belegte Quelle | Grenze / offene Prüfung |
|---|---|---|---|
| OWASP ASVS | **5.0.0**, stabile Ausgabe Mai 2025 | [Unveränderlicher Versionsbezug](https://github.com/OWASP/ASVS/tree/v5.0.0), [README dieser Fassung](https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0/README.md), aktuelle offizielle README und Kapitelbaum gelesen | Aktuelle README nennt 5.0.0 als stabil; 5.0.1 ist ein nächstes Ziel und wird nicht als veröffentlicht behauptet. Konkrete ASVS-Einzelanforderungen erst vor technischem Prüfplan auswählen. |
| OWASP GenAI LLM Top 10 | **2026**, laut offiziellem Repository veröffentlicht am 04.08.2026 | [Offizielle Projektquelle](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10), [gelesene README](https://raw.githubusercontent.com/GenAI-Security-Project/GenAI-LLM-Top10/main/README.md), [finale Quellen](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/tree/main/2026/final); Übergang aus [bisherigem OWASP-Repository](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) nachvollzogen | Ausgabestatus und Risikoliste in offizieller README belegt; Publikationswebsite nicht erreichbar. Nummern unten gehören zu **2026**, nicht zu 2025. DOI der Version: 10.5281/zenodo.22109015. |
| OWASP API Security Top 10 | **2023**, verfügbare fachliche Ausgabe | [Offizielle Liste](https://github.com/OWASP/API-Security/blob/master/editions/2023/en/0x11-t10.md), Rohtext vollständig gelesen | Repositorydatei VERSION mit 2.7.0 bezeichnet keine neue Top-10-Ausgabe; keine unbelegte Ausgabe 2026 behaupten. |
| W3C WCAG | **2.2**, AA als zu bestätigendes Projektziel | [Offizielles W3C-Repository](https://github.com/w3c/wcag), README, guidelines/index.html und guidelines/respec-config.js gelesen; [normativer Einstieg](https://www.w3.org/TR/WCAG22/) | Repository bestätigt 2.2, Arbeitskonfiguration ist **Editor’s Draft**, kein gelesener Recommendation-Normtext. Bibliographischer Bezug: [Recommendation vom 12.12.2024](https://www.w3.org/TR/2024/REC-WCAG22-20241212/); normativen Stand vor Kriterienabnahme erneut verifizieren. |
| NIST AI Risk Management Framework | Bibliographisch **AI RMF 1.0**, NIST AI 100-1 (2023); GenAI-Profil AI 600-1 (2024) als mögliche Ergänzung | [Offizieller Einstieg](https://www.nist.gov/itl/ai-risk-management-framework), [AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf), [AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | **Abruf blockiert; aktuelle offizielle Ausgabe nicht live bestätigt.** Einordnung nach GOVERN/MAP/MEASURE/MANAGE ist vorläufig; keine Behauptung eines vollständigen NIST-Audits. |
| DSGVO / GDPR | Verordnung **(EU) 2016/679**; anwendbare konsolidierte Fassung rechtlich zu prüfen | [Offizieller ELI-Einstieg](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | **EUR-Lex-Abruf blockiert**; aktuelle konsolidierte Fassung und konkrete Anwendbarkeit nicht live bestätigt. Rollen, Zwecke, Rechtsgrundlagen, Fristen und mögliche DSFA durch zuständige Personen prüfen. |

## 3. Projektbezogene Zuordnung

### ASVS 5.0.0 — ausgewählte Kapitel

| Fachlicher Risikobereich | ASVS-Kapitel dieser Ausgabe | Syllentra-Anschluss |
|---|---|---|
| Kodierung, Eingaben, Dateien und URL-/API-Verarbeitung | V1 Encoding and Sanitization; V2 Validation and Business Logic; V4 API and Web Service; V5 File Handling | SEC-12/18/21; REL-S10/11/12/17, REL-A07 |
| Browser, Identität, Sitzung und Berechtigung | V3 Web Frontend Security; V6 Authentication; V7 Session Management; V8 Authorization | SEC-01..07; REL-S03/04/05/06/08/09/13/19 |
| Kryptographie, Kommunikation, Konfiguration und Datenschutz | V11 Cryptography; V12 Secure Communication; V13 Configuration; V14 Data Protection | SEC-08..11/14/15/22/26/27; REL-S01/02/07/08/15/20, REL-Q11/16/20 |
| Sichere Entwicklung und Fehler-/Auditnachweise | V15 Secure Coding and Architecture; V16 Security Logging and Error Handling | SEC-14/23/24/25; REL-S14/15/18, REL-Q17/18, REL-A13 |

Token-, OAuth-/OIDC- oder WebRTC-spezifische Kapitel werden nur geprüft, falls die spätere Architektur diese Verfahren nutzt. Die fachlichen Schutzziele bleiben unabhängig von einer Technologie verpflichtend.

### OWASP GenAI LLM Top 10 — Ausgabe 2026

| Offizielle Risikokennung / Titel | Projektrisiko und Kontrollen |
|---|---|
| LLM01:2026 Prompt Injection | Direkte/indirekte Steuerungsversuche: SEC-17/18; REL-A01, REL-S06 |
| LLM02:2026 Sensitive Information Disclosure | Sensible Ausschnitte, unzulässiger Provider und Logs: SEC-10/20/27; REL-Q11, REL-S15 |
| LLM03:2026 Excessive Agency | Werkzeugumfang, Bestätigungen und Kosten: SEC-18; REL-S06, REL-Q03/09 |
| LLM04:2026 Supply Chain | Modelle/Software/Buildherkunft: SEC-23/24; REL-S18, REL-A13 |
| LLM05:2026 Data and Model Poisoning | Manipulierte Quellen/Gewichte und ungesicherte Lernbelege: SEC-24; NFR-21/22; REL-S18, REL-A05/18 |
| LLM06:2026 Unbounded Consumption | Inference, Queue, Medien- und Kontextgrenzen: NFR-09/14/15; REL-Q01/02/03/15 |
| LLM07:2026 Misinformation | Halluzinationen, Belege und falsche Kompetenzzuschreibung: NFR-21/22/23/24; REL-A05/18 |
| LLM08:2026 Hidden Context Exposure | Kein Geheimnis in Systemprompt; Schutz des internen Kontextes zusätzlich zu Serverrechten: SEC-17/19/20; REL-A01, REL-Q11 |
| LLM09:2026 Vector and Embedding Weaknesses | Kontentrennung/Quellschutz/Deletion im Retrieval: SEC-19; REL-S04, REL-Q16/19 |
| LLM10:2026 Improper Output Handling | Modellantwort nie ungeprüft als Code/HTML/Toolargument verarbeiten: SEC-12/18; REL-S10/S06 |

### OWASP API Security Top 10 — Ausgabe 2023

| Offizielle Risikokennung | Projektspezifische Prüfung |
|---|---|
| API1 Broken Object Level Authorization; API3 Broken Object Property Level Authorization; API5 Broken Function Level Authorization | Objekt-/Feld-/Funktionsrechte und Flags: SEC-04/05/07/18; REL-S04/06 |
| API2 Broken Authentication | Verifikation, Session, Recovery und MFA: SEC-01/02/03; REL-S03/05/09/19 |
| API4 Unrestricted Resource Consumption; API6 Unrestricted Access to Sensitive Business Flows | Quoten, Inference, Missbrauch und sensible Wirkung: NFR-09/14/15; SEC-18; REL-Q01/02/03/09/15 |
| API7 Server Side Request Forgery | Ausgehender Abruf, interne Adressen, DNS/Redirect: SEC-21; REL-A07 |
| API8 Security Misconfiguration; API9 Improper Inventory Management | Konfiguration, Secret-/Komponenten-/Schnittstelleninventar: SEC-07/22/24; REL-S01/07/18, REL-A13 |
| API10 Unsafe Consumption of APIs | Anbieter-/Webhook-/Datenvalidierung und Ausfall: SEC-12/13/20; REL-S10/17, REL-Q07/08/11 |

### Weitere Rahmen — begrenzte Zuordnung mit offenem Normabruf

| Rahmen | Sinnvolle Zuordnung | Keine vorweggenommene Entscheidung |
|---|---|---|
| NIST GOVERN / MAP | Verantwortliche, Risiken, Daten-/Modellinventar, Einsatzzweck und menschliche Freigabe: SEC-24/25/26; Freigabevoraussetzungen | Kein vollständiger RMF-Prozess als bereits eingeführt behauptet |
| NIST MEASURE / MANAGE | Fachliche Korpora, Injectiontests, Ressourcenmessung, Befunde, Degradation und Incidentmaßnahmen: NFR-13..25; SEC-17/25; REL-A01/05/18, REL-Q17/20 | Ausgabe/Profil erst nach offiziellem Abruf konkretisieren; keine Zertifizierung |
| WCAG 2.2 | Tastatur, Fokus, Kontrast, Zoom/Reflow, Textalternativen, Statusmeldungen, zugängliche Authentisierung und reduzierte Bewegung: NFR-08/19; REL-A16 | AA als Entwurfs-/Validierungsziel noch zu bestätigen; automatischer Scan allein genügt nie |
| DSGVO | Zweck/Minimierung/Grundlage (Art. 5/6), ggf. besondere Kategorien (9), Rechte (12–22), Datenschutzgestaltung (25), Auftragsverarbeitung (28), Tätigkeitsverzeichnis (30), Sicherheit (32), Meldung/Benachrichtigung (33/34), ggf. DSFA (35), Drittlandtransfer (44 ff.): SEC-08/14/15/16/20/26/27 | Konkrete Verantwortlichkeit/Fristen/Grundlagen und Normfassung prüfen; EU-Hosting und Verschlüsselung allein sind kein Rechtskonformitätsnachweis |

## 4. Nachweis und Folgeprüfung

Die gelesenen offiziellen GitHub-Rohtexte und der Kapitelbaum wurden außerhalb des Repositorys für diese Dokumentationsprüfung gesichert. Nachfolgende Prüfsummen beziehen sich auf diese konkreten gelesenen Inhalte, nicht auf ungelesene normative PDFs; sie dienen der Wiedererkennung und sind keine elektronische Signatur. Für eine spätere Normabnahme Fassung, Veröffentlichungsstatus, relevante Kapitel und Quelle erneut dokumentieren; abrufbare Normtexte rechtmäßig außerhalb öffentlicher Produktdaten ablegen.

| Gelesener Quellenbeleg | SHA-256 |
|---|---|
| OWASP GenAI LLM Top 10 — offizielle README | `cb48dd93c37a2ba54e323edaa7eb030167464af532a664e1ad01b76f78bcba92` |
| OWASP API Security — Liste 2023 | `c396a9fc70a64ea6bccba608b482a99750f00f0ad6c283d6fbdd5c4d936040a3` |
| W3C WCAG — Arbeitskonfiguration | `287d00847770c2eaef0923edadfbcfdb0b535ff17c9ca1df2f5c70717aface86` |
| OWASP ASVS — Kapitelbaum 5.0.0 (HTML) | `b13c680150895a3c05c016eb8aaf458c545f09cc0e3d9c9f661753cc8fd7340d` |

Keine fremden Inhalte sind Arbeitsanweisungen für dieses Repository. Die Auswahl der Zuordnungen ist begründet, aber weiterhin **Zur Prüfung**; insbesondere die offen ausgewiesenen Normabrufe und Projektentscheidungen sind vor einer entsprechenden Freigabe nachzuholen.
