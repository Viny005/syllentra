# Austauschbare KI-Anbieter und kontrolliertes Routing

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Schmaler Aufgabenvertrag

Vorschlag zu TECH-O-01/07/08/13, keine Implementierung. Fachkern beschreibt Aufgabe (Dialog, belegte Erklärung, Notiz, Quiz, Embedding, ASR/TTS), Konto-/Operation-ID, Sprache, Quell-/Kontextrevision, Schutzklasse, genehmigte Verarbeitung, Fähigkeiten und begrenztes Zeit-/Ressourcen-/Ausgabebudget. Ergebnis enthält Status, validierbare strukturierte Daten, Quellenverweise, tatsächliche Modell-/Promptfassung, Verbrauch und Fehler; kein Geheimnis. Ein OpenAI-kompatibles JSONformat garantiert weder identische Funktionen noch gleiche Datenschutzrechte.

Port → expliziter Policy-/Capabilityfilter → Budgetreservierung → zugelassener Adapter → validiertes Ergebnis. Kandidaten: llama.cpp für CPUbaseline; Ollama als bequeme, aber kontrolliert zu betreibende Alternative; freigegebene APIs nur nach separatem Gate. Motor-/Modellrechte und Ressourcenbelege aus [bestehender KI-Studie](../architecture/KI_UND_MODELLE.md), nicht erneut als beschlossen ausgeben.

Serverkatalog: Provider/Endpointallowlist/Modellrevision, lokale oder externe Verarbeitung, Fähigkeiten (Tools/Streaming/Schema/Sprachen/Modalitäten), geprüfte Lizenz/Vertragsfassung, zulässige Kategorie/Zwecke, Region/Retention, Kostenformel/Limit, Timeout/Retry und Aktivierungsrechte. Endpointänderung erzeugt keine Installation oder Rechte. Providercredential nur geschützter Serversecretstore, nie Frontend/Logs/Prompt; private persönliche Dokumentenschlüssel bleiben getrennt.

## 2. Reihenfolge einer Anfrage

1. Authentisierten Kontostatus, Sitzung/Gerät, Rolle, Objekt, Flag, Zweck und aktuelle Operation prüfen. Retrieval bereits auf zulässige Quellen beschränken.
2. Schutzklasse und explizite Freigabe schneiden. Externe Kategorien/Aufgaben/Provider standardmäßig abweisen. Eine Nutzerbestätigung hebt ungeeignete Anbieterbedingungen nicht auf.
3. Fähigkeiten/Sprachen/Kontextgrenze gegen Aufgabe prüfen; nur passende tatsächlich verfügbare Katalogeinträge. Lernqualität gemessen, keine automatische „größtes Modell ist bestes“ Regel.
4. Konten-/globale Token-, Rate-, Queue- und Geldgrenze prüfen, Worst-case-Verbrauch atomar reservieren. Ohne Ausgabenfreigabe alle kostenpflichtigen Wege sperren. Warnung reicht nicht; Mehrverbrauch/Abbruch/Streaming reserviert berücksichtigen.
5. Begrenzten Job mit Konto/Zweck/Quellrevision und Idempotenzschlüssel erstellen; vor tatsächlicher Wirkung Rechte/Entzug nochmals prüfen. Provider-Request-ID zum Abgleich verwenden soweit unterstützt.
6. Timeout, Abbruch und bounded Retry mit Backoff/Jitter; Retry-After respektieren. Kein erneuter Tool-/Kalenderschreibaufruf bei unbekanntem Ausgang ohne Abgleich. Streamabbruch als unvollständig ausweisen, kein falscher Erfolg.
7. Ausgabe gegen Schema, Größe, Quellen und erlaubte Aktionen validieren. Modelltext führt keine Tools aus. Toolbestätigung separat operationsgebunden, Rechte erneut serverseitig prüfen.
8. Tatsächlichen Verbrauch abrechnen, Reserve korrekt freigeben, minimale private Auditmetadaten, temporäre Daten kontrolliert löschen. Keine Promptbodies standardmäßig loggen.

## 3. Fehler und kontrollierter Fallback

| Fall | Sicherer Weg | Unzulässiger Automatismus |
|---|---|---|
| Lokales Modell aus / Kontext zu groß | Wartestatus, begrenzte Wiederholung, Kürzungsvorschlag oder erlaubte reine Datenfunktion | Private Ausschnitte an externen Gratisprovider senden |
| Externe Quote/Rate erschöpft | 429/402 verständlich anzeigen, Job zurückstellen/stoppen und Reserve prüfen | Bezahltarif aktivieren, Credits kaufen oder andere Provider automatisch versuchen |
| Vertrag/Einwilligung widerrufen | Adapter sperren, Queue/Retry abbrechen, vorhandene zulässige Inhalte les-/löschbar lassen | Alter Job/Token als dauerhafte Zustimmung |
| Stream teilweise / externe Wirkung unklar | Unvollständige Antwort kennzeichnen, Wirkung abgleichen | Ganze Unterhaltung/Operation duplizieren |
| Routingdienst (OpenRouter/HF) mit Upstreams | Nur explizit erlaubte Zielprovider, keine sonstigen automatischen Fallbacks; Einstellungen anhand echter API nachweisen | Routervertrag als Erlaubnis für beliebige Upstream-/Servertools behandeln |

Circuit Breaker stoppt wiederkehrende Fehler eines Ziels, er erteilt keine Fallbackrechte. Auch Wechsel zwischen externen Anbietern braucht passenden Daten-/Zweck-/Kategorieumfang. Lokaler Fallback nur wenn aktuelle Rechte/Modell-/Kapazitätsregeln passen. Fehlt Unterstützung für harte Providerbindung, Router für diesen Schutzumfang nicht verwenden.

## 4. Kleiner eigener Adapter gegenüber LiteLLM

| Variante | Nutzen | Aufwand / Lizenz / Empfehlung |
|---|---|---|
| Wenige eigene Adapter hinter kleinem Port | Transparente Rechte-/Kostenkontrolle, wenige Abhängigkeiten, leicht mockbar | Protokollabweichungen selbst testen; **zuerst prüfen**, bei 1–3 tatsächlich verwendeten Backends oft ausreichend |
| LiteLLM Core | Einheitliche Provideranbindung, Routing-/Budgethilfen | MIT außerhalb Enterprisebereich, Enterprisebedingungen separat; großer Abhängigkeits-/Update-/Konfigurationsumfang, zusätzlicher Proxy falls betrieben. Keine eingebaute Funktion ersetzt Syllentra-Konto-/Quellrechte. Erst bei belegtem Pflegevorteil, derzeit zurückgestellt |

[Patternabwägung](../development/ARCHITECTURAL_PATTERNS.md), [APIbefunde](LLM_API_COMPARISON.md), [Lizenzregister](../development/DEPENDENCY_SELECTION.md). Keine dieser Varianten implementiert/getestet oder ausgewählt. Künftige Nachweise: Providercontracttests ohne Netz, synthetische Policy-/Budget-/Retry-/Abbruchtests, A/B-Kontoisolation und erst dann einzeln autorisierte Liveprobe. Verknüpfung T02/T03/T09, SEC-17..20/24/27 und REL-A01/05/18.
