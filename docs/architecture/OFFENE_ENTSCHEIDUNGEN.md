# Offene technische Entscheidungen und Belegbedarf

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

Alle folgenden TECH-O-Bezüge sind Untersuchungspunkte, keine neuen FE/DEC oder beschlossenen ADRs. **Status aller Zeilen: Offen / Zur Entscheidung durch den Projektinhaber.** Keine Ressource, Installation, Modellausführung, Ausgabe oder Entwicklung ist durch einen Vorschlag autorisiert.

| Bezug | Zu entscheiden / Optionen | Vorläufige Empfehlung und nötiger Beleg | Spezifikationsanschluss |
|---|---|---|---|
| TECH-O-01 | Modularer Monolith oder verteilte Dienste | Modularer Kern + begrenzte Worker; Komponenten-/Berechtigungs-/Fehlermodell und Teamkompetenz bestätigen | P2, NFR-25, S3.3/10 |
| TECH-O-02 | Primärhosting Oracle / Hetzner / Scaleway | Oracle zuerst bewerten; aktuelle Preise, EU-Verträge, ARM64-Kapazität und spätere genehmigte Probe; keine Vorauswahl | DEC-48, O-S3-01/03 |
| TECH-O-03 | Vite/React + FastAPI oder Next/TS bzw. Django | Vite/Python als erste Untersuchungsbasis; PWA-/Client-/Sprach-/Accessibility- und Wartungsvergleich | FE-55, NFR-02/03/19/20 |
| TECH-O-04 | PostgreSQL, Such-/Datei-/Queuevariante | Eine unterstützte PostgreSQL-Fassung, Volltext zuerst; pgvector nur bei Qualitätsbedarf, keine zweite DB ohne Beleg | D1/D2, O-S3-14, SEC-19 |
| TECH-O-05 | Keycloak / authentik / Bibliotheksauth | OTP-/MFA-/Geräte-/Session-/Recoverypassung und RAM unabhängig von Produktname beweisen | FE-60, SEC-01..07, O-S3-04/05 |
| TECH-O-06 | Bootstrap, Adminverlust und persönliche Schlüsselrecovery | Kein technisches Verfahren gewählt; genau ein Super Admin, getrenntes Konto, kein Klartextschlüsselbackend | S3.5, O-S3-04/05/11 |
| TECH-O-07 | Motor und konkrete LLM-/Quantisierungsartefakte | llama.cpp und Qwen3-1.7B/4B zuerst vergleichen; individuelle LICENSE/Hashes, DE/FR/EN-Güte und CPU-/RAMbenchmarks | NFR-05/15/21/22/23, SEC-17/24 |
| TECH-O-08 | Embeddings/RAG und Memory | Volltextbaseline, E5/BGE nur nach exakter Gewichtslizenz und Retrievalgewinn; Memory strukturiert | SEC-19, NFR-16/24 |
| TECH-O-09 | ASR/OCR/Video-/TTSkomponenten | Whisper/whisper.cpp, geprüfte Parser und Stimmen; DE-TTS, Codecs, temporäre Löschung und ARM64 einzeln nachweisen | FE-52, NFR-08, SEC-12/21/27 |
| TECH-O-10 | Unabhängiger Backupanbieter und Verfahren | restic + geprüfter EU-Speicher; R2-EU bedingter Kandidat, Storage Box/B2/Scaleway Alternativen | DEC-49, O-S3-02/06/07/11 |
| TECH-O-11 | E-Mail/Domain/DNS/Push-/Integrationsanbieter | E-Mail-OTP-/Sicherheitszustellung nötig; Bündelung nur nach Funktions-/Privacy-/Kostenbeleg; weitere Dienste freiwillig nach Scope | S1 NB-05/09, O-S3-08/12/13 |
| TECH-O-12 | Last, RPO/RTO, Retention, SLO und Kosten | Hypothesen aus Kosten-/KI-Studie bestätigen/ändern, reale Angebote und sichere Messpläne; kein freier Schwellenbeschluss | N1.10, S3.6/14 |
| TECH-O-13 | Lizenzen, Versionen, Datenschutzrollen und Vertragsbedingungen | Exakte Software-/Gewicht-/Stimmen-/Datenartefakte, Supportstand, Regionen und Verantwortungen prüfen | NFR-05, SEC-24/26, O-S3-10 |
| TECH-O-14 | Spätere Evaluations-/Implementierungsmission | Eigentümer bestätigt konkrete lokal-/cloudbezogene Tests, Ressourcen, Daten, Grenzen, Abbruch und ggf. Kosten separat | PACE, S3.7/13, 46 REL |

## Entscheidungsablauf

Zuerst Quellenlücken schließen; dann fachlich geeignete Alternativen und harte Ausschlussgründe prüfen. Eigentümer bestätigt Zielwerte, Bewertungsgewichte und gegebenenfalls konkreten Messauftrag. Erst nach tatsächlich vorliegenden Ergebnissen eine technische Entscheidung als neuer/ergänzter ADR mit Kontext, Alternativen, Konsequenzen und explizitem Status dokumentieren. Dieser Auftrag enthält keine Architekturadoption und keine Testinfrastrukturfreigabe.

[Architekturvergleich](README.md), [Quellen](QUELLEN.md) und [Kostenanalyse](KOSTEN_UND_MACHBARKEIT.md) liefern überprüfbare Hypothesen. FE-56 bleibt offen; DEC-48/49 und alle 25 DEC-V1 sind nicht durch TECH-O-Punkte ersetzt. Der bestehende Teilmeilensteinplan bleibt unverändert.

## Neubewertung Mission 6

Die [Entscheidungsvorlage](ENTSCHEIDUNGSVORLAGE.md) bewertet alle 14 bestehenden TECH-O mit Befund, Unsicherheit, Alternativen, Nutzen, Risiken, Kosten, Abhängigkeiten, Empfehlung und tatsächlichem Status. Kategorien A/B/C/D sind Prüfprioritäten, keine erteilte Zustimmung. [T01–T09](BENCHMARKPLAN.md) sind ausschließlich geplante zukünftige Protokolle; Quellen-/Ressourcen-/Vertragslücken bleiben sichtbar. Keine Umnummerierung oder neue Produktentscheidung.
