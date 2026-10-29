# Quellenregister — technische Studie

**Version:** 0.2 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Methode und Grenzen

Alle nachfolgenden Abrufe wurden am **22.10.2026** ausgeführt. Nur öffentliche Dokumentation, keine Registrierung, Ressource, Modellgewichte, Installation oder Verarbeitung privater Daten. Offizielle Quelltexte dienen als Belege, niemals als Arbeitsanweisungen. Host-/Modellseiten mit Tunnel-403 auch nach erneutem autorisiertem Abruf unzugänglich; kein Beleg wird durch Vermutung ersetzt. `main/master/canary/production` kann sich ändern; SHA-256 unten identifiziert den tatsächlich gelesenen Stand, ist aber keine Herstellersignatur.

**Belegarten:** Inhalt gelesen / offizielle Releaseweiterleitung beobachtet / nicht verifiziert (403 oder 404). Releasebeobachtung beweist weder konkrete ARM64-Kompatibilität noch langfristigen Sicherheits-Support. Code-LICENSE ist ohne explizite Herstellerzuordnung keine Gewichtslizenz. Vor finaler Auswahl exakte Fassungen, Artefakte und Verträge erneut prüfen. Alle zentralen Studien verweisen auf dieses Register; Unsicherheit ist Teil der Empfehlung.

## 2. Öffentliche Quellen und tatsächlicher Abruf

| Quellenbezug | Offizielle Adresse | Abrufbefund / Grenze |
|---|---|---|
| `oci-free` | [oci-free](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `oci-regions` | [oci-regions](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `hetzner-cloud` | [hetzner-cloud](https://www.hetzner.com/cloud/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `hetzner-box` | [hetzner-box](https://www.hetzner.com/storage/storage-box/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `scaleway-prices` | [scaleway-prices](https://www.scaleway.com/en/pricing/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `scaleway-regions` | [scaleway-regions](https://www.scaleway.com/en/docs/console/account/reference-content/products-availability/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `r2-prices` | [r2-prices](https://developers.cloudflare.com/r2/pricing/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `r2-location` | [r2-location](https://developers.cloudflare.com/r2/reference/data-location/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `b2-prices` | [b2-prices](https://www.backblaze.com/cloud-storage/pricing) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `pg-policy` | [pg-policy](https://www.postgresql.org/support/versioning/) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `node-release` | [node-release](https://raw.githubusercontent.com/nodejs/Release/main/schedule.json) | Inhalt gelesen (HTTP 200) |
| `pgvector` | [pgvector](https://raw.githubusercontent.com/pgvector/pgvector/master/README.md) | Inhalt gelesen (HTTP 200) |
| `ollama` | [ollama](https://raw.githubusercontent.com/ollama/ollama/main/README.md) | Inhalt gelesen (HTTP 200) |
| `llama` | [llama](https://raw.githubusercontent.com/ggml-org/llama.cpp/master/README.md) | Inhalt gelesen (HTTP 200) |
| `vllm` | [vllm](https://raw.githubusercontent.com/vllm-project/vllm/main/README.md) | Inhalt gelesen (HTTP 200) |
| `whisper` | [whisper](https://raw.githubusercontent.com/openai/whisper/main/README.md) | Inhalt gelesen (HTTP 200) |
| `qwen3` | [qwen3](https://huggingface.co/Qwen/Qwen3-4B/raw/main/README.md) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `gemma3` | [gemma3](https://huggingface.co/google/gemma-3-4b-it/raw/main/README.md) | **Nicht verifiziert**: Tunnel-403 / Netzwerkzugriff verweigert |
| `keycloak` | [keycloak](https://raw.githubusercontent.com/keycloak/keycloak/main/README.md) | Inhalt gelesen (HTTP 200) |
| `restic` | [restic](https://raw.githubusercontent.com/restic/restic/master/README.md) | Inhalt gelesen (HTTP 200) |
| `r2-price-mirror` | [r2-price-mirror](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/r2/pricing.mdx) | Inhalt gelesen (HTTP 200) |
| `r2-location-mirror` | [r2-location-mirror](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/r2/reference/data-location.mdx) | Inhalt gelesen (HTTP 200) |
| `qwen3-official` | [qwen3-official](https://raw.githubusercontent.com/QwenLM/Qwen3/main/README.md) | Inhalt gelesen (HTTP 200) |
| `qwen25-official` | [qwen25-official](https://raw.githubusercontent.com/QwenLM/Qwen2.5/main/README.md) | Inhalt gelesen (HTTP 200) |
| `gemma-official` | [gemma-official](https://raw.githubusercontent.com/google/gemma_pytorch/main/README.md) | Inhalt gelesen (HTTP 200) |
| `e5-official` | [e5-official](https://raw.githubusercontent.com/microsoft/unilm/master/e5/README.md) | Inhalt gelesen (HTTP 200) |
| `bge-official` | [bge-official](https://raw.githubusercontent.com/FlagOpen/FlagEmbedding/master/README.md) | Inhalt gelesen (HTTP 200) |
| `whisper-cpp` | [whisper-cpp](https://raw.githubusercontent.com/ggml-org/whisper.cpp/master/README.md) | Inhalt gelesen (HTTP 200) |
| `kokoro` | [kokoro](https://raw.githubusercontent.com/hexgrad/kokoro/main/README.md) | Inhalt gelesen (HTTP 200) |
| `keycloak-license` | [keycloak-license](https://raw.githubusercontent.com/keycloak/keycloak/main/LICENSE.txt) | Inhalt gelesen (HTTP 200) |
| `authentik-license` | [authentik-license](https://raw.githubusercontent.com/goauthentik/authentik/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `authjs-license` | [authjs-license](https://raw.githubusercontent.com/nextauthjs/next-auth/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `next-license` | [next-license](https://raw.githubusercontent.com/vercel/next.js/canary/license.md) | Inhalt gelesen (HTTP 200) |
| `vite-license` | [vite-license](https://raw.githubusercontent.com/vitejs/vite/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `fastapi-license` | [fastapi-license](https://raw.githubusercontent.com/fastapi/fastapi/master/LICENSE) | Inhalt gelesen (HTTP 200) |
| `pg-license` | [pg-license](https://raw.githubusercontent.com/postgres/postgres/master/COPYRIGHT) | Inhalt gelesen (HTTP 200) |
| `pg-version` | [pg-version](https://raw.githubusercontent.com/postgres/postgres/master/configure.ac) | Inhalt gelesen (HTTP 200) |
| `pgvector-license` | [pgvector-license](https://raw.githubusercontent.com/pgvector/pgvector/master/LICENSE) | Inhalt gelesen (HTTP 200) |
| `ollama-license` | [ollama-license](https://raw.githubusercontent.com/ollama/ollama/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `llama-license` | [llama-license](https://raw.githubusercontent.com/ggml-org/llama.cpp/master/LICENSE) | Inhalt gelesen (HTTP 200) |
| `vllm-license` | [vllm-license](https://raw.githubusercontent.com/vllm-project/vllm/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `whisper-license` | [whisper-license](https://raw.githubusercontent.com/openai/whisper/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `restic-license` | [restic-license](https://raw.githubusercontent.com/restic/restic/master/LICENSE) | Inhalt gelesen (HTTP 200) |
| `restic-doc` | [restic-doc](https://raw.githubusercontent.com/restic/restic/master/doc/030_preparing_a_new_repo.rst) | Inhalt gelesen (HTTP 200) |
| `ffmpeg-license` | [ffmpeg-license](https://raw.githubusercontent.com/FFmpeg/FFmpeg/master/LICENSE.md) | Inhalt gelesen (HTTP 200) |
| `piper-license` | [piper-license](https://raw.githubusercontent.com/OHF-Voice/piper1-gpl/main/COPYING) | Inhalt gelesen (HTTP 200) |
| `fastapi-doc` | [fastapi-doc](https://raw.githubusercontent.com/fastapi/fastapi/master/README.md) | Inhalt gelesen (HTTP 200) |
| `next-support` | [next-support](https://raw.githubusercontent.com/vercel/next.js/canary/docs/01-app/01-getting-started/01-installation.mdx) | Inhalt gelesen (HTTP 200) |
| `next-release` | [next-release](https://github.com/vercel/next.js/releases/latest) | Offizielle Weiterleitung beobachtet: `v16.4.2` |
| `vite-release` | [vite-release](https://github.com/vitejs/vite/releases/latest) | Offizielle Weiterleitung beobachtet: `v8.3.5` |
| `fastapi-release` | [fastapi-release](https://github.com/fastapi/fastapi/releases/latest) | Offizielle Weiterleitung beobachtet: `0.159.1` |
| `keycloak-release` | [keycloak-release](https://github.com/keycloak/keycloak/releases/latest) | Offizielle Weiterleitung beobachtet: `26.8.1` |
| `ollama-release` | [ollama-release](https://github.com/ollama/ollama/releases/latest) | Offizielle Weiterleitung beobachtet: `v0.40.8` |
| `llama-release` | [llama-release](https://github.com/ggml-org/llama.cpp/releases/latest) | Offizielle Weiterleitung beobachtet: `v0.7.0` |
| `vllm-release` | [vllm-release](https://github.com/vllm-project/vllm/releases/latest) | Offizielle Weiterleitung beobachtet: `v0.32.0` |
| `restic-release` | [restic-release](https://github.com/restic/restic/releases/latest) | Offizielle Weiterleitung beobachtet: `v0.19.1` |
| `pgvector-release` | [pgvector-release](https://github.com/pgvector/pgvector/releases/latest) | Releaseübersicht erreichbar; kein eindeutiger Latest-Tag nachgewiesen |
| `pdf-license` | [pdf-license](https://raw.githubusercontent.com/jsvine/pdfplumber/stable/LICENSE) | **Nicht verifiziert**: HTTP Error 404: Not Found |
| `pymupdf-license` | [pymupdf-license](https://raw.githubusercontent.com/pymupdf/PyMuPDF/main/COPYING) | Inhalt gelesen (HTTP 200) |
| `tesseract-license` | [tesseract-license](https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/LICENSE) | Inhalt gelesen (HTTP 200) |
| `qdrant-license` | [qdrant-license](https://raw.githubusercontent.com/qdrant/qdrant/master/LICENSE) | Inhalt gelesen (HTTP 200) |
| `redis-license` | [redis-license](https://raw.githubusercontent.com/redis/redis/unstable/LICENSE.txt) | Inhalt gelesen (HTTP 200) |
| `valkey-license` | [valkey-license](https://raw.githubusercontent.com/valkey-io/valkey/unstable/COPYING) | Inhalt gelesen (HTTP 200) |

## 3. Beobachtete Fassungen und Support

| Projekt | Beobachteter offizieller Stand | Interpretation |
|---|---|---|
| Next.js | [v16.4.2](https://github.com/vercel/next.js/releases/tag/v16.4.2) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| Vite | [v8.3.5](https://github.com/vitejs/vite/releases/tag/v8.3.5) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| FastAPI | [0.159.1](https://github.com/fastapi/fastapi/releases/tag/0.159.1) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| Keycloak | [26.8.1](https://github.com/keycloak/keycloak/releases/tag/26.8.1) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| Ollama | [v0.40.8](https://github.com/ollama/ollama/releases/tag/v0.40.8) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| llama.cpp | [v0.7.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.7.0) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| vLLM | [v0.32.0](https://github.com/vllm-project/vllm/releases/tag/v0.32.0) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| restic | [v0.19.1](https://github.com/restic/restic/releases/tag/v0.19.1) | Releaseweiterleitung am Abrufdatum; kein Deploymentpin oder Support-/Sicherheitsbeweis |
| Node.js | Gelesener offizieller Releaseplan: 24.x seit 20.10.2026 Maintenance-LTS bis 30.04.2028; 26.x LTS laut Plan erst ab 28.10.2026 | 26 am 22.10.2026 nicht vorzeitig als LTS ausgeben; 20.x laut Plan bereits EOL. Aktuelle Patchfassung separat auswählen. |
| PostgreSQL | Quelllizenz/Entwicklungszweig lesbar, Supportwebsite 403 | Aktuelle unterstützte Major-/Patchfassung und Supportzeitraum **nicht verifiziert**; keinen `master`-Stand als Produktionsrelease vorschlagen. |
| pgvector | README-Installationsbeispiel 0.8.7; Latest-Aufruf führte nur zur Releaseübersicht | Kein aus dem Installationsbeispiel abgeleiteter Support-/Neuheitsbeweis |
| Python / Django / SQLite / MariaDB | Aktuelle Support-/Einzellizenzprüfung hier nicht vollständig belegt | Kandidaten, keine impliziten Versionspins; vor Auswahl schließen |

## 4. Zuordnung wichtiger Schlussfolgerungen

| Schlussfolgerung | Tatsächlicher Beleg und verbleibende Unsicherheit |
|---|---|
| OCI-Freikapazität nicht zugesagt | OCI-Quoten-/Regionsabruf blockiert; historische 4-OCPU-/24-GB-Größenordnung im Hostingvergleich ausdrücklich nicht aktuell verifiziert |
| R2-Standardpreise und Freimenge | `r2-price-mirror` offizieller Dokumentationsquelltext gelesen; Gebührenwährung USD, Steuer/Vertrag und andere Dienste separat |
| R2-EU statt Location Hint | `r2-location-mirror`: EU-Jurisdiktion für Bucketobjekte, Hint keine Garantie; gesamte Verarbeitungs-/Metadaten-/Vertragslage bleibt zu prüfen |
| ARM64 ist keine Leistungszusage | llama.cpp/whisper.cpp/vLLM-README gelesen; whisper.cpp nennt Linux-ARM64-Image, konkrete OCI-/Modell-/Bibliothekskombination nicht gebaut/getestet |
| Kleine Modelle können Gewichtsspeicher reduzieren | Offizielle Quantisierungsfähigkeit plus eigene Formel; Gesamtspeicher/Tokenrate nicht benchmarked |
| Modelllizenzen separat | Qwen3-README erklärt Open-Weight-Modelle Apache-2.0, konkrete Checkpointdateien unlesbar; Whisper erklärt Code/Gewichte MIT; Kokoro erklärt Apache-Gewichte, Stimmen-/DE-Passung offen; E5/BGE/Gemmaartefakte nicht pauschal freigegeben |
| Werkzeuge nicht beliebig permissiv | Motor-/Auth-/DB-/Backup-LICENSE gelesen; authentik hat Bereichsausnahmen, Piper GPL-3.0, FFmpeg konfigurationsabhängig; Quelllizenz ist kein Recht an Nutzerdaten/Codecs/Stimmen |
| PostgreSQL + pgvector zuerst statt zweiter DB | Technische Analyse der D1-/D2-Beziehungen; pgvector-README beschreibt Filter-/ANN-/iterative-Scan-Grenzen; Qdrant-Quelllizenz gelesen, kein Skalierungsbenchmark |
| Preise/Benchmarks fehlen teilweise | Alle fehlenden Hostangebote und Modelleigenschaften als nicht verifiziert markiert; keine bezahlte API, Ressource oder Konto für bessere Belege aktiviert |

## 5. Prüfsummen der tatsächlich gelesenen Quellen

Die öffentlichen Abrufinhalte wurden für diese Recherche außerhalb des Repositorys gesichert. Keine privaten Inhalte oder Zugangsdaten. Für spätere Wiederholung URL, Datum, Status und Hash vergleichen; ein identischer Hash belegt nicht die spätere Gültigkeit von Tarifen oder Nutzungsbedingungen.

| Quellenbezug | SHA-256 des Abrufinhalts |
|---|---|
| `node-release` | `26c8e4743fc3a76d686a038c2df40426bc3bdc7a018cb83f3b88bbf89f45436f` |
| `pgvector` | `19cebadeeb8d3181d01ef00399674ec41bd2f0363850cdccc7685d4260c5a1c6` |
| `ollama` | `9e5a7d406950fdd2742084065ab38a3ea09b5aab5e2f13ef7d64147229ae0d8b` |
| `llama` | `dc2d34687c844ecf929d9e9a9c9c78e8023b52abf3b2b3d039600c79016673b6` |
| `vllm` | `4dc7399323b9660117f8cc1226afb7a81cdbb912dbb4ae74b66d89052417d11c` |
| `whisper` | `38c180c2a8d8ba628a3e131ad42bf06c8a51bb681efb30fbe28d5a0f4b65f288` |
| `keycloak` | `5a5b61cb4caa1e113cc53fd07794fc8b78cafce254761ab6c690dcfb7355879c` |
| `restic` | `4684f85db668903f6b0e66c3c677efa62fb291e9fe56f2e909b57e84d5740587` |
| `r2-price-mirror` | `bee9f44fb8feaf6331039d32eb24aaad864aaa83e3c1488277a7a0e1cc22e6b7` |
| `r2-location-mirror` | `2efcd824885ced99e92acc11946d9a48411724cfcf07b0e3d9daae8e59e5e60c` |
| `qwen3-official` | `0b2c2bb11806f7a00c8465f2586e2e99f15de28622fd5c9b70b83ae1ab18c75d` |
| `qwen25-official` | `0b2c2bb11806f7a00c8465f2586e2e99f15de28622fd5c9b70b83ae1ab18c75d` |
| `gemma-official` | `86f6cd7c50eec67f1ad74b54a59c40c40748dde840b405bda897f92a754f201d` |
| `e5-official` | `4930b1d912bf86b69d9b8722d1382ad8678cc6c3ec9d590059df0281ca31c120` |
| `bge-official` | `46500109787496a729e233c6a74ac5be2148a48108ad26e39e7de964dc0f5ca3` |
| `whisper-cpp` | `43451813ec96b5ea286c6d676f467bdffb053224c110c257ce3d67d911e774e7` |
| `kokoro` | `b50b84220668f8247a2405b249c34c7083acc24114279ff1429fd79f46a2c04b` |
| `keycloak-license` | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| `authentik-license` | `bcf8a408c1e07975835399bcafa455c2d173fcd86a2dc0c79dcb88bc2bda94bc` |
| `authjs-license` | `c886e96e9dea78ac2526e820e92f11b82b090c9dda36c7737d00797f539f0216` |
| `next-license` | `ee765244e2d59f5234d474f62e0766fa0c8b99af967fdd4c0cb8dcb0c76ea224` |
| `vite-license` | `692057af3d664cbb79ac38293eb50aa3c4987f8182e2a440136e59e08f1b4a54` |
| `fastapi-license` | `4ec89ffc81485b97fec584b2d4a961032eeffe834453894fd9c1274906cc744e` |
| `pg-license` | `3d6af92ff8a4c2cdf69afb1cf44edea727922f5cd0cf8b5f72b11cdecac8fdfd` |
| `pg-version` | `6a84060a4c90dbaf97ec1ab5f356e075e2ea4e8046dd8f9ffe3ca613b4f44b01` |
| `pgvector-license` | `6bba9ebeb73e27477463b05e5ef1bf303bccbddb3db9bbc95905d351604d6a87` |
| `ollama-license` | `5934ed2ce0d15154bcdb9c85203210abac0da4314af34081e36df4599f90b226` |
| `llama-license` | `94f29bbed6a22c35b992c5c6ebf0e7c92f13b836b90f36f461c9cf2f0f1d010d` |
| `vllm-license` | `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` |
| `whisper-license` | `b5d65a59060e68c4ff940e1eddfa6f94b2d68fdf58ed7f4dd57721c997e35e9d` |
| `restic-license` | `6f08a01a9fab5b24e139a09f15cc24a73087c7bc09e3bacf099fdf2d767bf897` |
| `restic-doc` | `b04c34c964603e71f17576b2d005c7d63692e02268eb56381fd9e6df6c48008b` |
| `ffmpeg-license` | `e6dc72d5665a1ebd6dcc841de59278dad4ca77ecc47b03f1064a55c3e9ea8bb8` |
| `piper-license` | `0ae0485a5bd37a63e63603596417e4eb0e653334fa6c7f932ca3a0e85d4af227` |
| `fastapi-doc` | `9b44160901909b924c7520227f5cdb44f7785560957b73987ff12379b3f82faa` |
| `next-support` | `e1a5d7738e2ca0e0b3400e8e290e4ee5919e860a3d729ed564574e6ad55fcd40` |
| `next-release` | `a74cc01178d9d9d229345aabbbfc70ce1a64feeb6d9132af2c52c611c879d5c9` |
| `vite-release` | `454ffae8499dc50a752c98e369d770a0ca3d411fe00abb8e464665401c39afd8` |
| `fastapi-release` | `6c10c26e11425d96e32c23f451957770a2c02f5ad4cf8b638133e58e753ce1bc` |
| `keycloak-release` | `23995a8d5b45deff87f2f88363fcfb7304e12e49cd1b7439d2b1b89af9bb6d02` |
| `ollama-release` | `f11efc1ad4154a8196d808391ba22f9c40a59ba13ba69ef2622add8344aa1218` |
| `llama-release` | `36f0b1dbad19c764b42b04c3b473ef48068b662c90e59173ad4dd02df0610187` |
| `vllm-release` | `738cd260eb61399dff008041ed46bf2a907d7fe33d32f0820953d21fb0ad4fc7` |
| `restic-release` | `4d98d17533e3e8f2ab06ef8caaaa9cc29027a3c1359a185c2a8620f55bc720c3` |
| `pgvector-release` | `2a512d5dbae06536be23ddf7a5ed3f77d9ccccafd682b42a6c028de5f837d9fc` |
| `pymupdf-license` | `57c8ff33c9c0cfc3ef00e650a1cc910d7ee479a8bc509f6c9209a7c2a11399d6` |
| `tesseract-license` | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| `qdrant-license` | `210b508429e913d9de5301f90508bc2cbf5b2281de5b45e607c04d58f0f3bd8f` |
| `redis-license` | `4a0e416b9537688f30dfe69ddaceb2ca64d96b7df02a0a6760d376890ddc4e40` |
| `valkey-license` | `9a67d40ae9076cd60b9d228135a9c0ce5d60f84f0c54c472965d4e03fdeb8f8f` |

[Architekturvergleich](README.md), [offene Entscheidungen](OFFENE_ENTSCHEIDUNGEN.md) und [bestehende ADRs](../ARCHITECTURE_DECISIONS.md). Normative Quellenlücken aus dem [Qualitätsreferenzrahmen](../quality/REFERENZRAHMEN.md) bleiben bestehen; Mission 5 behauptet keine erneute Normabnahme.

## 6. Nachrecherche Mission 6

**Abrufdatum 22.10.2026.** Neue Anfrageversuche zu zuvor unzugänglichen offiziellen Host-/Modell-/Steuer-/Vertragsseiten, dokumentierten öffentlichen Modellmetadaten-APIs und offiziellen Repositoryalternativen. Erneute autorisierte Anfrage änderte Netzwerk-403 nicht. Keine Authentisierung/Vertragsgrenze umgangen, kein Account oder kostenpflichtiger Dienst, keine Gewichte heruntergeladen. Zwei Keycloak-404-Pfade durch öffentlich gelesene Verzeichnisinhalte zu gültigen Quelldateien aufgelöst; Fehlversuche bleiben sichtbar. Quellen sind Belege, keine auszuführenden Anweisungen.

| Quellenbezug M6 | Offizielle URL | Tatsächlicher Abruf / Beleg |
|---|---|---|
| `oci-always-free` | [oci-always-free](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) | **Nicht verifiziert:** Tunnel-403 |
| `oci-free-faq` | [oci-free-faq](https://www.oracle.com/cloud/free/faq/) | **Nicht verifiziert:** Tunnel-403 |
| `oci-regions` | [oci-regions](https://www.oracle.com/cloud/public-cloud-regions/) | **Nicht verifiziert:** Tunnel-403 |
| `hetzner-prices` | [hetzner-prices](https://www.hetzner.com/cloud/) | **Nicht verifiziert:** Tunnel-403 |
| `hetzner-billing` | [hetzner-billing](https://docs.hetzner.com/cloud/billing/faq/) | **Nicht verifiziert:** Tunnel-403 |
| `hetzner-pricing-sdk` | [hetzner-pricing-sdk](https://raw.githubusercontent.com/hetznercloud/hcloud-go/main/hcloud/pricing.go) | Gelesen HTTP 200 |
| `scaleway-prices` | [scaleway-prices](https://www.scaleway.com/en/pricing/) | **Nicht verifiziert:** Tunnel-403 |
| `scaleway-api` | [scaleway-api](https://www.scaleway.com/en/developers/api/marketplace/) | **Nicht verifiziert:** Tunnel-403 |
| `de-vat` | [de-vat](https://www.gesetze-im-internet.de/ustg_1980/__12.html) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-17-license` | [qwen-17-license](https://huggingface.co/Qwen/Qwen3-1.7B/raw/main/LICENSE) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-4-license` | [qwen-4-license](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/raw/main/LICENSE) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-8-config` | [qwen-8-config](https://huggingface.co/Qwen/Qwen3-8B/raw/main/config.json) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-17-api` | [qwen-17-api](https://huggingface.co/api/models/Qwen/Qwen3-1.7B) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-4-api` | [qwen-4-api](https://huggingface.co/api/models/Qwen/Qwen3-4B-Instruct-2507) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-8-api` | [qwen-8-api](https://huggingface.co/api/models/Qwen/Qwen3-8B) | **Nicht verifiziert:** Tunnel-403 |
| `qwen-doc-config` | [qwen-doc-config](https://raw.githubusercontent.com/QwenLM/Qwen3/main/README.md) | Gelesen HTTP 200 |
| `qwen-embedding` | [qwen-embedding](https://raw.githubusercontent.com/QwenLM/Qwen3-Embedding/main/README.md) | Gelesen HTTP 200 |
| `keycloak-email` | [keycloak-email](https://raw.githubusercontent.com/keycloak/keycloak/main/docs/documentation/server_admin/topics/users/con-email.adoc) | **Nicht verifiziert:** HTTP 404 |
| `keycloak-otp` | [keycloak-otp](https://raw.githubusercontent.com/keycloak/keycloak/main/docs/documentation/server_admin/topics/authentication/otp.adoc) | **Nicht verifiziert:** HTTP 404 |
| `authentik-email` | [authentik-email](https://raw.githubusercontent.com/goauthentik/authentik/main/website/docs/add-secure-apps/flows-stages/stages/email/index.mdx) | Gelesen HTTP 200 |
| `authentik-doc-tree` | [authentik-doc-tree](https://github.com/goauthentik/authentik/tree/main/website/docs/add-secure-apps/flows-stages/stages/email) | Gelesen HTTP 200 |
| `restic-append` | [restic-append](https://raw.githubusercontent.com/restic/restic/master/doc/060_forget.rst) | Gelesen HTTP 200 |
| `r2-lock` | [r2-lock](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/r2/buckets/bucket-locks.mdx) | Gelesen HTTP 200 |
| `r2-legal` | [r2-legal](https://www.cloudflare.com/cloudflare-customer-dpa/) | **Nicht verifiziert:** Tunnel-403 |
| `keycloak-users-tree` | [keycloak-users-tree](https://github.com/keycloak/keycloak/tree/main/docs/documentation/server_admin/topics/users) | Gelesen HTTP 200 |
| `keycloak-auth-tree` | [keycloak-auth-tree](https://github.com/keycloak/keycloak/tree/main/docs/documentation/server_admin/topics/authentication) | Gelesen HTTP 200 |
| `whisper-catalog` | [whisper-catalog](https://raw.githubusercontent.com/openai/whisper/main/whisper/__init__.py) | Gelesen HTTP 200 |
| `piper-voices-doc` | [piper-voices-doc](https://raw.githubusercontent.com/OHF-Voice/piper1-gpl/main/docs/VOICES.md) | Gelesen HTTP 200 |
| `keycloak-verify-email` | [keycloak-verify-email](https://raw.githubusercontent.com/keycloak/keycloak/main/docs/documentation/server_admin/topics/users/proc-verify-user-email.adoc) | Gelesen HTTP 200 |
| `keycloak-otp-policies` | [keycloak-otp-policies](https://raw.githubusercontent.com/keycloak/keycloak/main/docs/documentation/server_admin/topics/authentication/otp-policies.adoc) | Gelesen HTTP 200 |

Neue belegte Präzisierungen: Keycloak Verify Email verwendet einen Link; seine OTP-Policy beschreibt Generator-TOTP/HOTP. authentik Email-Stage dokumentiert tokenisierte Rückkehr und mögliche standardmäßige Reaktivierung inaktiver Konten bei Recovery. R2 dokumentiert Bucketlocks mit konfigurationsberechtigtem Entfernen; daraus folgt kein unentfernbarer Schutz gegen kompromittierte Hauptcredentials. restic beschreibt physische Prunebereinigung, Scratchspace und append-only-Risiken. Qwen3-Embedding-Herstellerkatalog nennt für 0,6B 32K/1024 sowie multilingualen Support; sein großer Modellbenchmark beweist keine Didaktik oder Leistung des kleinen Kandidaten. Hetzner-SDK-Preisstruktur ist kein aktuelles Tarifangebot. Dokumentierte Fähigkeiten bleiben vor Integration und Vertrags-/Ausführungsfreigabe zu prüfen.

| Gelesener M6-Beleg | SHA-256 des tatsächlich gelesenen Inhalts |
|---|---|
| `hetzner-pricing-sdk` | `08f41db394b84109032ff6e2525e5c262bcd7f3c33efac842c5afd3b0d594707` |
| `qwen-doc-config` | `0b2c2bb11806f7a00c8465f2586e2e99f15de28622fd5c9b70b83ae1ab18c75d` |
| `qwen-embedding` | `cb77a65d92c429684ce41c839f959d151021b9fc37a40b9dfddfdb7449790599` |
| `authentik-email` | `468724cc5cad8c1225a3c2980f72ef873aee22ec2cd134dcb7ccfb74401826f1` |
| `authentik-doc-tree` | `75912a4c5ea15a713a33457791c6c45e9905ab1d403606613ea4b231a25f943c` |
| `restic-append` | `deed2c7aa2cd6fb5c5bd2da0daab184281aac4f92e17b11e3355f88cbd130aee` |
| `r2-lock` | `49b9c4ede9e0bfbda4fd068f00ab36f7d877e7f6ea1abd6019eb99c5391b56ba` |
| `keycloak-users-tree` | `78020597f5f336b3abf188aaf18e9521c2c1a4530b0b0fd4c71eee704bd4d8a6` |
| `keycloak-auth-tree` | `b4d47bf2a06f20699f70f3e2c87da8ed1d35214278481425da30cb1e2f075de7` |
| `whisper-catalog` | `79ecbed714783b6230931a3dba6d5da6d386e2d44f9fc27256e4fc72751e1f62` |
| `piper-voices-doc` | `cc724e58206cfaa94e2894544b9a1aca89ea45c85b36df1645a1719b029fdb55` |
| `keycloak-verify-email` | `833fe0c0c93a729a66f519376d15367d5278b8e4208f661cc1821959526fe626` |
| `keycloak-otp-policies` | `fe4c28eec49cb0b35ef53e87bbb6faa1ea6571f249c29bf1bd76ed6cd3f58cd2` |

[Machbarkeit](MACHBARKEITSPRUEFUNG.md), [Ressourcen](RESSOURCENBEDARF.md), [Testprotokolle](BENCHMARKPLAN.md) und [Entscheidungsvorlage](ENTSCHEIDUNGSVORLAGE.md) trennen Herstellerangaben, Vertragslücken, Benchmarkklassen und Rechnungen. Alle früheren Quellenbezüge bleiben erhalten; keine unlesbare individuelle LICENSE oder Preisliste als bestätigt ausgegeben.
