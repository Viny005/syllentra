# Mission 7 — Quellen, Revisionen und Evidenzgrenzen

**Version:** 0.1 · **Stand:** 22.10.2026 · **Status:** Empfohlen / Zur Entscheidung

## 1. Verfahren und Aktualität

Öffentliche offizielle Dokumentations-/Lizenz-/SDKdateien am **22.10.2026** abgerufen. SHA-256 bezieht sich auf gelesene vollständige Antwortbytes; bei Repositorydateien im Lizenzregister ist zusätzlich der konkrete Commit verlinkt. Keine externen Installskripte ausgeführt, keine Keys/Accounts oder Inferenzaufrufe. Primäre Webseiten mit Netzwerk-403 auch beim erlaubten erneuten Versuch unlesbar; offizielle öffentliche Repositoryquellen als Alternative genutzt. Falsche Dateipfade mit 404 sind kein technischer oder kommerzieller Befund; nachgefundene korrekte Quellen unten. Keine Zugangsbarriere umgangen.

Offizielle Quellcodeaussage belegt Mechanismus/Lizenz am bezeichneten Stand, kein Verhalten eines nicht getesteten Clients. SDKbeispiele belegen keine aktuellen Modellangebote/Preise. Herstellerdokumente sind keine unabhängigen Benchmarks, abgeschlossenen Verträge oder vollständigen Datenschutzgutachten. Unverifizierte Daten bleiben ausdrücklich offen. Empfehlungen unter [offenen Entscheidungen](OPEN_DECISIONS.md), früherer Quellenbestand unverändert unter [Architekturquellen](../architecture/QUELLEN.md).

## 2. Gelesene Quellen und gesperrte Primärreferenzen

| Bezug | URL | Abrufbefund | SHA-256 der gelesenen Quelle |
|---|---|---|---|
| codex-skills | [Offizielle Quelle](https://developers.openai.com/codex/skills/) | Nicht verifiziert: Netzwerk-403 | — |
| codex-agents | [Offizielle Quelle](https://developers.openai.com/codex/guides/agents-md/) | Nicht verifiziert: Netzwerk-403 | — |
| codex-subagents | [Offizielle Quelle](https://developers.openai.com/codex/subagents/) | Nicht verifiziert: Netzwerk-403 | — |
| codex-config | [Offizielle Quelle](https://developers.openai.com/codex/config-basic/) | Nicht verifiziert: Netzwerk-403 | — |
| codex-mcp | [Offizielle Quelle](https://developers.openai.com/codex/mcp/) | Nicht verifiziert: Netzwerk-403 | — |
| codex-security | [Offizielle Quelle](https://developers.openai.com/codex/security/) | Nicht verifiziert: Netzwerk-403 | — |
| codex-review | [Offizielle Quelle](https://developers.openai.com/codex/integrations/github/) | Nicht verifiziert: Netzwerk-403 | — |
| openai-skills | [Offizielle Quelle](https://raw.githubusercontent.com/openai/skills/main/README.md) | Gelesen, HTTP 200 | `0f6a07580f3c627253e15a58dd0439e135049ec38eb16cf3587f7e50abc6f590` |
| claude-skills | [Offizielle Quelle](https://code.claude.com/docs/en/skills) | Nicht verifiziert: Netzwerk-403 | — |
| claude-memory | [Offizielle Quelle](https://code.claude.com/docs/en/memory) | Nicht verifiziert: Netzwerk-403 | — |
| claude-agents | [Offizielle Quelle](https://code.claude.com/docs/en/sub-agents) | Nicht verifiziert: Netzwerk-403 | — |
| claude-hooks | [Offizielle Quelle](https://code.claude.com/docs/en/hooks) | Nicht verifiziert: Netzwerk-403 | — |
| claude-permissions | [Offizielle Quelle](https://code.claude.com/docs/en/permissions) | Nicht verifiziert: Netzwerk-403 | — |
| claude-mcp | [Offizielle Quelle](https://code.claude.com/docs/en/mcp) | Nicht verifiziert: Netzwerk-403 | — |
| claude-plugins | [Offizielle Quelle](https://code.claude.com/docs/en/plugins) | Nicht verifiziert: Netzwerk-403 | — |
| skills-format | [Offizielle Quelle](https://agentskills.io/specification) | Nicht verifiziert: Netzwerk-403 | — |
| openai-docs-mcp | [Offizielle Quelle](https://developers.openai.com/mcp) | Nicht verifiziert: Netzwerk-403 | — |
| mcp-docs | [Offizielle Quelle](https://modelcontextprotocol.io/docs/learn/architecture) | Nicht verifiziert: Netzwerk-403 | — |
| groq-quota | [Offizielle Quelle](https://console.groq.com/docs/rate-limits) | Nicht verifiziert: Netzwerk-403 | — |
| groq-models | [Offizielle Quelle](https://console.groq.com/docs/models) | Nicht verifiziert: Netzwerk-403 | — |
| groq-privacy | [Offizielle Quelle](https://console.groq.com/docs/your-data) | Nicht verifiziert: Netzwerk-403 | — |
| groq-prices | [Offizielle Quelle](https://groq.com/pricing) | Nicht verifiziert: Netzwerk-403 | — |
| gemini-prices | [Offizielle Quelle](https://ai.google.dev/gemini-api/docs/pricing) | Nicht verifiziert: Netzwerk-403 | — |
| gemini-quota | [Offizielle Quelle](https://ai.google.dev/gemini-api/docs/rate-limits) | Nicht verifiziert: Netzwerk-403 | — |
| gemini-terms | [Offizielle Quelle](https://ai.google.dev/gemini-api/terms) | Nicht verifiziert: Netzwerk-403 | — |
| cf-ai-prices | [Offizielle Quelle](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/workers-ai/platform/pricing.mdx) | Gelesen, HTTP 200 | `4fc5ecfdd85c435770f134896bc4ad5db3b901e2fac3b100d56286225ac5504f` |
| cf-ai-limits | [Offizielle Quelle](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/workers-ai/platform/limits.mdx) | Gelesen, HTTP 200 | `5e549327a4b791940ee73ba644c5a758376c040fd15a1ccfc954fc79f527aa77` |
| cf-ai-data | [Offizielle Quelle](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/workers-ai/platform/data-usage.mdx) | Gelesen, HTTP 200 | `e76df1e96054efc88b28bf1feb4057b7638a5509d5ab983bdd17069135c72ad7` |
| openrouter-quota | [Offizielle Quelle](https://openrouter.ai/docs/api-reference/limits) | Nicht verifiziert: Netzwerk-403 | — |
| openrouter-privacy | [Offizielle Quelle](https://openrouter.ai/docs/features/privacy-and-logging) | Nicht verifiziert: Netzwerk-403 | — |
| hf-inference | [Offizielle Quelle](https://huggingface.co/docs/inference-providers/en/pricing) | Nicht verifiziert: Netzwerk-403 | — |
| hf-security | [Offizielle Quelle](https://huggingface.co/docs/inference-providers/en/security) | Nicht verifiziert: Netzwerk-403 | — |
| mistral-prices | [Offizielle Quelle](https://mistral.ai/pricing) | Nicht verifiziert: Netzwerk-403 | — |
| mistral-limits | [Offizielle Quelle](https://docs.mistral.ai/deployment/ai-studio/tier) | Nicht verifiziert: Netzwerk-403 | — |
| cerebras-limits | [Offizielle Quelle](https://inference-docs.cerebras.ai/support/rate-limits) | Nicht verifiziert: Netzwerk-403 | — |
| cerebras-models | [Offizielle Quelle](https://inference-docs.cerebras.ai/models/overview) | Nicht verifiziert: Netzwerk-403 | — |
| cerebras-privacy | [Offizielle Quelle](https://www.cerebras.ai/privacy) | Nicht verifiziert: Netzwerk-403 | — |
| assistant-ui-readme | [Offizielle Quelle](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/README.md) | Gelesen, HTTP 200 | `91f519bdf12a72584e13dcca4bb42bb1d6aff47e3ea0692dcccd6ab1213a9b3c` |
| tiptap-readme | [Offizielle Quelle](https://raw.githubusercontent.com/ueberdosis/tiptap/main/README.md) | Gelesen, HTTP 200 | `8cd77367d0107be7325a3915847fda194416805b268bb1d1b993a8332b8a7448` |
| reactflow-readme | [Offizielle Quelle](https://raw.githubusercontent.com/xyflow/xyflow/main/README.md) | Gelesen, HTTP 200 | `be7df4c1810d7c7d0e44e26d08404a97fa9ab62d3fdf3e5fd4c31f3070472d63` |
| fullcalendar-readme | [Offizielle Quelle](https://raw.githubusercontent.com/fullcalendar/fullcalendar/main/README.md) | Gelesen, HTTP 200 | `f7b473014333c8840f94c7ab7fcb8af506881b810d0eadd83cfdd50d12568cf9` |
| mcp-servers-readme | [Offizielle Quelle](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/README.md) | Gelesen, HTTP 200 | `c112784223279665bda02d79105eff6f268c629f18c4590a50e9305b72bf1f9e` |
| github-mcp-readme | [Offizielle Quelle](https://raw.githubusercontent.com/github/github-mcp-server/main/README.md) | Gelesen, HTTP 200 | `371e8c991df6e5e61ca6a864d692141dbf1a728ae0790d376b54c96b91e4ff13` |
| playwright-mcp-readme | [Offizielle Quelle](https://raw.githubusercontent.com/microsoft/playwright-mcp/main/README.md) | Gelesen, HTTP 200 | `b33aa71a13d655e96e6b736d0c9de1e5ddea52f205916ca20b876387ff830e87` |
| litellm-readme | [Offizielle Quelle](https://raw.githubusercontent.com/BerriAI/litellm/main/README.md) | Gelesen, HTTP 200 | `a32872a5bdf5548edb26a44488ebe7a576419272c0dc51cc44799ee6b0c54a93` |
| ragas-readme | [Offizielle Quelle](https://raw.githubusercontent.com/explodinggradients/ragas/main/README.md) | Gelesen, HTTP 200 | `af20b2258507b12bf930e897b63ee5bb87aac4a4696da078ea5a3c29addb6db7` |
| deepeval-readme | [Offizielle Quelle](https://raw.githubusercontent.com/confident-ai/deepeval/main/README.md) | Gelesen, HTTP 200 | `7720fa66b5288458942be1169ee2dcbfcac1940e03cbf2144dd2101f51a546e2` |
| claude-readme | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/README.md) | Gelesen, HTTP 200 | `aa0d8b80ac083e1591be0789273f447058cc9187b4331634a5614155da27778d` |
| skills-spec-repo | [Offizielle Quelle](https://raw.githubusercontent.com/agentskills/agentskills/main/docs/specification.mdx) | Gelesen, HTTP 200 | `b9079c0c10b7930e8c6a20ff2bc10cda2a3343c55185120e3f1116a1a529b220` |
| claude-skill-example | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md) | Gelesen, HTTP 200 | `dcd4803e61e913e6fc27294184cd3a71f09f5e924ff20c8a9a20173e7b3c2bcf` |
| claude-plugin-dev | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/plugin-dev/README.md) | Gelesen, HTTP 200 | `67a23d324462b1f30044b66ec77b59edf6a55547b5e0000a1d886d1906b8073d` |
| claude-hooks-example | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/plugin-dev/skills/hook-development/SKILL.md) | Gelesen, HTTP 200 | `d14528f389cae485ac50583a22be326485c83fc9c8ef7ce700213e1583cf8fbe` |
| claude-skill-dev | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/plugin-dev/skills/skill-development/SKILL.md) | Gelesen, HTTP 200 | `d40080c45d652dd3cc481d1e381cd7e6258091a87351fa1de67c6c8ecec3446e` |
| claude-agents-example | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/plugin-dev/skills/agent-development/SKILL.md) | Gelesen, HTTP 200 | `ff3324078bbeef3e214157391795360e148892e9c6735f1fc049f397aa939c80` |
| hf-price-repo | [Offizielle Quelle](https://raw.githubusercontent.com/huggingface/hub-docs/main/docs/inference-providers/pricing.md) | Gelesen, HTTP 200 | `eda3a6ccd84b164ee148b9fc1fef04944534e641bcb93e8b21ac3cf7113de311` |
| hf-security-repo | [Offizielle Quelle](https://raw.githubusercontent.com/huggingface/hub-docs/main/docs/inference-providers/security.md) | Gelesen, HTTP 200 | `af636231fbd974eaa1eb65225a9b82a695541f992f9892595080c4cf8c8a9947` |
| groq-readme | [Offizielle Quelle](https://raw.githubusercontent.com/groq/groq-python/main/README.md) | Gelesen, HTTP 200 | `fbe2d274b599ac6cb9bf4a201bd80301f8274edfa3f6e6718da6794afc1473ae` |
| gemini-sdk | [Offizielle Quelle](https://raw.githubusercontent.com/googleapis/python-genai/main/README.md) | Gelesen, HTTP 200 | `66952d47594d7a9c588782f57cb02d04fa4fd27b108112fd06b036234cdebc34` |
| mistral-sdk | [Offizielle Quelle](https://raw.githubusercontent.com/mistralai/client-python/main/README.md) | Gelesen, HTTP 200 | `6350dd706fcf8fa38de0d8336d7f4d4944b9bc66d2e729dcd93bf2e3ff122239` |
| cerebras-sdk | [Offizielle Quelle](https://raw.githubusercontent.com/Cerebras/cerebras-cloud-sdk-python/main/README.md) | Gelesen, HTTP 200 | `ef5782798d14b72ab7e08261737d969142870e1d4d582fc76dbeec1984bb9cb7` |
| codex-skills-doc | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/docs/skills.md) | Gelesen, HTTP 200 | `e59789d09692310bbf94e2ef8db0aaf00d97f2226982c8c5330d2d260583a97d` |
| codex-config-doc | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/docs/config.md) | Gelesen, HTTP 200 | `745768b4da6cd73e414fc49c5c6ef3d6bf8a0c08289fab23a7dd79776ab31d9d` |
| codex-agent-doc | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/docs/getting-started.md) | Gelesen, HTTP 200 | `210187b0199e42d71beabab773f6b8f3c01fe897037df1b16f88dd4efe007e90` |
| codex-agents-doc | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/docs/agents_md.md) | Gelesen, HTTP 200 | `56f5b6026b15fad40fe8b1f6f8910b9fccdf66da3b39dd943c91877e2299619e` |
| codex-creator | [Offizielle Quelle](https://raw.githubusercontent.com/openai/skills/main/skills/.system/skill-creator/SKILL.md) | Gelesen, HTTP 200 | `a17383bfb1448637ac1f757ad891ddb9676fa30b0eff620200f0e1cbc0cc0d50` |
| plugins-readme | [Offizielle Quelle](https://raw.githubusercontent.com/openai/plugins/main/README.md) | Gelesen, HTTP 200 | `b3681ebd15797bdee1d638c6520c7ba10a36e676760ea5c251530f53f843c852` |
| claude-changelog | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) | Gelesen, HTTP 200 | `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49` |
| filesystem-readme | [Offizielle Quelle](https://raw.githubusercontent.com/modelcontextprotocol/servers/main/src/filesystem/README.md) | Gelesen, HTTP 200 | `e3b18670bb05bfe2720322b00436b96d57a5825890faa0a51327f98cf9c2b5c1` |
| mcp-spec-repo | [Offizielle Quelle](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/main/docs/specification/2025-11-25/architecture/index.mdx) | Gelesen, HTTP 200 | `95c1e8ff98fc651b13ed9b38e7f8fde3c623a9f639b843c35f49c8936967e288` |
| codex-config-example | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/docs/example-config.md) | Gelesen, HTTP 200 | `8c360f977c2f5971b36bbda5721ec51b2604e7013eca46b3d4f51433461909c3` |
| codex-skill-tests | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/lib.rs) | Gelesen, HTTP 200 | `d5331b581372831c355c3b578dec627cca40d07c544ed4f2ac2273b965528a28` |
| codex-loading | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/skills/src/loading.rs) | Gelesen, HTTP 200 | `731255be7976e46b7bb7c19103215731adaf0b7f2e0869f176651aa0b8fe0955` |
| codex-config-ref | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/config.md) | Gelesen, HTTP 200 | `0b109608f1054fb5e1123d2b670ca391031186c8a16dfaccc10ed5a6789d90ed` |
| openrouter-docs-json | [Offizielle Quelle](https://raw.githubusercontent.com/OpenRouterTeam/docs/main/docs.json) | Gelesen, HTTP 200 | `753e79a8c9328fc26f4daf46d8e837152c25fd8dc5ae618f8b9bf567d4b4af32` |
| openrouter-limits-v2 | [Offizielle Quelle](https://raw.githubusercontent.com/OpenRouterTeam/docs/main/api_reference/limits.mdx) | Gelesen, HTTP 200 | `71d88572e56497734d50a0d8b0c8a2240bb5fafb174400b035a839c309af7a7c` |
| claude-root-instructions | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/CLAUDE.md) | Gelesen, HTTP 200 | `0fafa0a267c1a7320c4d9ccb4acaa27bdb7062e34cb23569f32a7a472ed0c7ac` |
| openrouter-data | [Offizielle Quelle](https://raw.githubusercontent.com/OpenRouterTeam/docs/main/guides/privacy/data-collection.mdx) | Gelesen, HTTP 200 | `9e244021d502115d4d038667f29d06e60d0124055403c6da5bd9c09a88ea4f8e` |
| openrouter-provider | [Offizielle Quelle](https://raw.githubusercontent.com/OpenRouterTeam/docs/main/guides/privacy/provider-logging.mdx) | Gelesen, HTTP 200 | `d3ae62191fe4af8ad0bb954c01fed9054b567b9a492bf00110d1cc119509ef81` |
| cf-ai-openai | [Offizielle Quelle](https://raw.githubusercontent.com/cloudflare/cloudflare-docs/production/src/content/docs/workers-ai/configuration/open-ai-compatibility.mdx) | Gelesen, HTTP 200 | `4f7133ebb4798fc6cc5eb786d8c82ba27e3992cbe6958d7e8512bf84d8bcbe23` |
| claude-plugin-agents | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/main/plugins/plugin-dev/agents/plugin-validator.md) | Gelesen, HTTP 200 | `e639a6faa931d60708dd2fbc936fab1fbf9c87308f93330a21277246c661b352` |
| codex-project-skills | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/skills.rs) | Gelesen, HTTP 200 | `5c48f010e5de81fd56d7fefa4829b83e21bd9531c127438edd770fc4f1dc81c2` |
| codex-agents-source | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/src/agents_md.rs) | Gelesen, HTTP 200 | `97427a870741b904a3f3c143f5990eaaa65b5bfa99ddac1808b2980052b5fc78` |
| codex-skill-config | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/config/src/skills_config.rs) | Gelesen, HTTP 200 | `df7e8bcd53b9aef6309a930a25203bfb052345b71091b4e2000e200dedeb2d6b` |
| codex-schema | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/core/config.schema.json) | Gelesen, HTTP 200 | `81c0d6818fbe971eaf2256129197f0cf96051e58f85a9b8b96d0cdeae7e8f5a5` |
| openrouter-catalog | [Offizielle Quelle](https://raw.githubusercontent.com/OpenRouterTeam/docs/main/api_reference/overview.mdx) | Gelesen, HTTP 200 | `63dfb0c40cc0b354117c921d4ff2409779e189bced70711b067aae949a2e4091` |
| codex-ext-lib | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/ext/skills/src/lib.rs) | Gelesen, HTTP 200 | `726790f7d2ffe939e16b416b6007d2382c656d199a3e7e0c24d9f2807159dad9` |
| codex-host-roots | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/ext/skills/src/host_roots.rs) | Gelesen, HTTP 200 | `d4290ba4d783110e7533586ad19719536aa9b23f517b43e3147d3afb40c91d56` |
| codex-sources | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/main/codex-rs/ext/skills/src/sources.rs) | Gelesen, HTTP 200 | `99e8addafa45bd29672bbab56337bf5fda998ce1bbf8326b3de75359c3fc509f` |
| openrouter-quota-constants | [Offizielle Quelle](https://raw.githubusercontent.com/OpenRouterTeam/docs/main/snippets/exports/constants.mdx) | Gelesen, HTTP 200 | `ed3f8100dde89afa21b7ea95274fb10539c3c93fdfa62825ec035da54ba1e8ab` |
| tailwind-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/tailwindlabs/tailwindcss/8cc0551b1217d36dc565840b90920964d37cb46c/LICENSE) | Gelesen, HTTP 200 | `60e0b68c0f35c078eef3a5d29419d0b03ff84ec1df9c3f9d6e39a519a5ae7985` |
| shadcn-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/shadcn-ui/ui/25af02b1b467fcd53b63e0c6d6d324c57c16ef18/LICENSE.md) | Gelesen, HTTP 200 | `1564074e13439397221ffd522e2e504d56561994a23d371aa5e3ad43e4f5423f` |
| lucide-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/lucide-icons/lucide/20aef31db93fe4d9f398dbb15b120d99c48eef95/LICENSE) | Gelesen, HTTP 200 | `b495047bd93a9b06913511076f504daba17d5bbeb3e0650f3bb53a4220329c57` |
| radix-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/radix-ui/primitives/eb3a2b7091293e27df8f9ba906632d8daa3d81a3/LICENSE) | Gelesen, HTTP 200 | `0e80a2d229d2fd4fc7e8636142ec5d0ff0bc031f14c15b682e2ac01dfd5b5138` |
| baseui-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/mui/base-ui/c0f792328bdd96128b44723b5bab317031395a64/LICENSE) | Gelesen, HTTP 200 | `07fc1b39d69d14bc7d40482a628f47226258eb01265db68ae684944b916beb2a` |
| react-aria-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/adobe/react-spectrum/e36b8c2869a0c7ca435f8e62307da50066836437/LICENSE) | Gelesen, HTTP 200 | `7dfe6526888bac51759c99f9a51262ba2711a8c12a067f2181609dd9a4066b84` |
| assistant-ui-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/assistant-ui/assistant-ui/770a07f355641e8dbf7f75a9d3427b457258d188/LICENSE) | Gelesen, HTTP 200 | `eafb05991a572efa34097474b31fef45b14a8879ed1d1a8fd77de62e6fa7d275` |
| tiptap-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/ueberdosis/tiptap/14a2cfcda9e534515cfeb2658d9f0cebaf9ed7ee/LICENSE.md) | Gelesen, HTTP 200 | `c96e5ecb55ac593157ad1d21d1f44a611187f494a0f04c235a1ae692c88d6ba9` |
| pdfjs-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/mozilla/pdf.js/d774262d9e01dc83e2c7a52b0cca0d05b250a3cb/LICENSE) | Gelesen, HTTP 200 | `0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594` |
| reactflow-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/xyflow/xyflow/8523d8dd9f1551954bc221dccabd6a3119ef9e22/LICENSE) | Gelesen, HTTP 200 | `023119ac20fb1c8c9930abe0bcd196989a1960388529a96fc43cebf96f07c9ff` |
| fullcalendar-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/fullcalendar/fullcalendar/6b890e803c66d1e6db2fb21c449936155b7e81fc/LICENSE.md) | Gelesen, HTTP 200 | `000882c713ee4c9729c7eeafbebb04a98a633517c2e95f1258fc488853124df3` |
| query-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/TanStack/query/75e64b5a1a4ecda73fbd88065180c6d7fb84fe57/LICENSE) | Gelesen, HTTP 200 | `a405ee70c632bb938acb7ac5f210e814409b3760ea9d2329d8ed8ffcfd11a0e7` |
| table-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/TanStack/table/c14e0221b1e656c7bb35e7b3d4cdf188719a3599/LICENSE) | Gelesen, HTTP 200 | `9db3f8ddd7031ab264b99bec49c221155d0c8649b53dd4aa007f2041d36cdf5f` |
| virtual-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/TanStack/virtual/5d51f1d972c8c22b9cb0b767741a9c544bd89299/LICENSE) | Gelesen, HTTP 200 | `a405ee70c632bb938acb7ac5f210e814409b3760ea9d2329d8ed8ffcfd11a0e7` |
| rhf-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/react-hook-form/react-hook-form/a72bcd7f73a44be6b4ad3e8f855d5d8fc588ec67/LICENSE) | Gelesen, HTTP 200 | `e8eeb472f0a5889c2c51625b86a3f9b8630680adb9f49a125352e2e426392780` |
| zod-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/colinhacks/zod/afdac65e0f80c0ccf9e8909da97c411567908b57/LICENSE) | Gelesen, HTTP 200 | `3f1189b28e3866e0d979968d466b78f813f76827cfdca1fbb124cc0a5c8841f8` |
| i18next-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/i18next/react-i18next/a6352f83232cad18a432fe269a6c4faab2e71a95/LICENSE) | Gelesen, HTTP 200 | `29b8ae456ef442e53a98df183ad088cf98c2ece73aa84c462330c43e665b8ab2` |
| katex-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/KaTeX/KaTeX/8f0d9bc9deac8165cca5c04c0beda5a17424909f/LICENSE) | Gelesen, HTTP 200 | `766ccc1f306c885aa45542a9846bbd0a505b27a0374f146778171c2254ce18e3` |
| mermaid-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/mermaid-js/mermaid/6d8921f94f9a12b76586eddcf45a566080d4767e/LICENSE) | Gelesen, HTTP 200 | `ec9fb67dcb25eccc416ed56e1aab819222c805a2a4bfe4cb19e7556bf2ffde80` |
| recharts-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/recharts/recharts/14aed3f2f1894f7f491e64f98729ed7542dc7813/LICENSE) | Gelesen, HTTP 200 | `2d3aa48a8d1d3b93093680e8e68d3a64cfb590c3ade377ffcaefc69dac7c2ce5` |
| visx-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/airbnb/visx/485c0359664ee8e612992defb16e1f035ed40b23/LICENSE) | Gelesen, HTTP 200 | `8c766533b7d4200b4dfb1a1afff396e3665460d21d7b4c34d059efcb5a332c84` |
| motion-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/motiondivision/motion/b7e4d5af1ded78585e1478ea235718ec0a61caec/LICENSE.md) | Gelesen, HTTP 200 | `1bf0dc3f7727723e5a032ed12164a47cf92c05204cb1a3485f123c24e2833ed1` |
| dnd-kit-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/clauderic/dnd-kit/e9215e820798459ae036896fce7fd9a6fe855772/LICENSE) | Gelesen, HTTP 200 | `537607e3f1533ad2c5b12978967f5ab27f34ffb7e626e321017a7ccca6cc24ff` |
| sonner-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/emilkowalski/sonner/8e4662b39255120b62138312058f5d77c0139a5e/LICENSE.md) | Gelesen, HTTP 200 | `da9201378c36ffd81f51ad0b305f3f0981e90bc558789210ad65d1161eec3b7d` |
| playwright-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/microsoft/playwright/ca7ca36145b84183cf423c2a099bd7e9cd8b1cb3/LICENSE) | Gelesen, HTTP 200 | `45873d00a0dd243596deb4aa23b2493b3d1f0671921bf2538ea431d7380220eb` |
| vitest-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/vitest-dev/vitest/7a5c083fc9ee460c5d724b062086f1ec62132ca9/LICENSE) | Gelesen, HTTP 200 | `04575fc5bfae19a9b63100f8691f901a2e15a399011ac02db435a9ef27295551` |
| testing-library-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/testing-library/react-testing-library/20ce75f2907ca0e5c5a8ae595c0e9a4e368c7800/LICENSE) | Gelesen, HTTP 200 | `9680978280d509520d2a7b51e93ffbf7d9ec2b9de4411a6989daba5b659048e0` |
| storybook-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/storybookjs/storybook/dbf5e3cded2efa6cbd296933a1bd62f0ffd398e3/LICENSE) | Gelesen, HTTP 200 | `bc90586179d44dcb313a9a289d687a2f26226303b2066bd21dbefd2378e894e5` |
| axe-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/dequelabs/axe-core/6b52b841461bd23345970b91ec75fdaff6bad31a/LICENSE) | Gelesen, HTTP 200 | `af175b9d96ee93c21a036152e1b905b0b95304d4ae8c2c921c7609100ba8df7e` |
| lighthouse-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/GoogleChrome/lighthouse/f8afbc790e2b51f4047c9edfc1c93c13aa6271fa/LICENSE) | Gelesen, HTTP 200 | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30` |
| mcp-servers-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/modelcontextprotocol/servers/51b6382a3e827aceb6bce430b1208d69b93d95ea/LICENSE) | Gelesen, HTTP 200 | `0382b0057770ca05e9c350a50aa3b1c1fea84da0bc81d723bf00b9aa841be58a` |
| github-mcp-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/github/github-mcp-server/f38526264abb14961b32cea386e38ec6d3cf674f/LICENSE) | Gelesen, HTTP 200 | `9e48ecfa18e2b15169746a3c97beda4d1d6c6796097038498ca434ca7e0ccd44` |
| playwright-mcp-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/microsoft/playwright-mcp/ab6d67cbf8b619338f096980806fdbe29432cc4d/LICENSE) | Gelesen, HTTP 200 | `9a7110fc2d2f964038e5dc49128f908f29f47a574c961cba16085914e879cbda` |
| litellm-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/BerriAI/litellm/f2118fc7670ba3fa736d9b8f4deef9077a45a720/LICENSE) | Gelesen, HTTP 200 | `b170d6bf8e8835dd357e011681db028f4d51e2fb0ea892058f56e01fb39b8273` |
| pypdf-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/py-pdf/pypdf/3dd71129a058b08856cc6e8d65e8d1e07399ca55/LICENSE) | Gelesen, HTTP 200 | `a97ac230e5f33ef10a5367a850eb01f91f1a0b064e34742c7794d2294557f524` |
| sentence-transformers-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/huggingface/sentence-transformers/a5f62a56d86990ad490b6eb29439b48487494b65/LICENSE) | Gelesen, HTTP 200 | `624b030fd62b8b989dd502d5bb6322cbc0dbb524ab9c9708f32efe33d7275735` |
| ragas-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/explodinggradients/ragas/298b68274234c060deacab3cf5fb52aa3a20e885/LICENSE) | Gelesen, HTTP 200 | `664b930830f291c2936ab30bcd6ef9ca6c9c7384cc475ae0c526156a27d5a6c6` |
| deepeval-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/confident-ai/deepeval/727203702cddf68e4f01a6ef95b23d9cb9036654/LICENSE.md) | Gelesen, HTTP 200 | `d004e4b8bbfa420b094c13835070b945a93f3c0ac0ea0bf6b7b8a72733533f7f` |
| ruff-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/astral-sh/ruff/b0f95269f9dc6e14dd4ac8738d99f211f75d73bc/LICENSE) | Gelesen, HTTP 200 | `2597d854122b77ddc71971564ca2350a37608575ce324adc5650a2b2051c8f18` |
| mypy-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/python/mypy/0cdcbfd08e246d22d3a2fa5e65d6d09d885fa21e/LICENSE) | Gelesen, HTTP 200 | `fdf1cd17f50e1305ed8cfd37467312d27a984648dba622cef70573b5512e4e1b` |
| pytest-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/pytest-dev/pytest/c9bf1edf9e0d388f3e7bebc88576e608ffbc40a4/LICENSE) | Gelesen, HTTP 200 | `ca836a5f9ecca3b2f350230faa20a48fb8b145653b5568d784862df864706b9b` |
| eslint-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/eslint/eslint/0c699d52d2c4596a56e8f8aa0c8f5732558cf552/LICENSE) | Gelesen, HTTP 200 | `3b6be04f862a077a4b97929dbf247299360824d9365f8603c263769303ace18c` |
| prettier-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/prettier/prettier/ffebe63f65e869a5e4a030eb9f78e68844be51ef/LICENSE) | Gelesen, HTTP 200 | `b0f2417199889f1c0d28ec4e0244eacf1a15de5819d61f641dd7d8f45153ac9c` |
| typescript-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/microsoft/TypeScript/98add1bbed1c814e97457587c2da407dc3f78330/LICENSE.txt) | Gelesen, HTTP 200 | `a7d00bfd54525bc694b6e32f64c7ebcf5e6b7ae3657be5cc12767bce74654a47` |
| pip-audit-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/pypa/pip-audit/828e77a4d4aa6bee8d315681db6928771d951a7c/LICENSE) | Gelesen, HTTP 200 | `0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594` |
| renovate-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/renovatebot/renovate/1a80c538f88ad9c2a2b570e75a574597c362a01c/license) | Gelesen, HTTP 200 | `8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef` |
| gitleaks-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/gitleaks/gitleaks/b58d3f102cf3a2c84cb7f923d05c25c9b1aed84b/LICENSE) | Gelesen, HTTP 200 | `e3884b252b3bfc045e55be43a34d1e80da070bc6f804ac95bf4660e97d62ebc6` |
| trivy-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/aquasecurity/trivy/2f4aaf7e7caa9eb91fb6abefc05a78a899698b5b/LICENSE) | Gelesen, HTTP 200 | `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` |
| semgrep-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/semgrep/semgrep/087e93b3a1fdf44f97bc92b5b9c2ba221cb2488b/LICENSE) | Gelesen, HTTP 200 | `20c17d8b8c48a600800dfd14f95d5cb9ff47066a9641ddeab48dc54aec96e331` |
| otel-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/open-telemetry/opentelemetry-python/74544f0501b76d328d61da635fec2f85ebe6c7ed/LICENSE) | Gelesen, HTTP 200 | `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` |
| syft-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/anchore/syft/b55707f60fddfb1bd69b5c6e9fbc1798c93f718c/LICENSE) | Gelesen, HTTP 200 | `c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4` |
| precommit-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/pre-commit/pre-commit/8cb5845c835b1ff72240eb2484239411ec481d92/LICENSE) | Gelesen, HTTP 200 | `ea2ca27cba7cc35822d95a46d59bcd3cc88e196592e6390d1949a359ffc990e8` |
| codex-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/openai/codex/94350a910143c406013683ae634708320f93f1f6/LICENSE) | Gelesen, HTTP 200 | `d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc` |
| claude-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/anthropics/claude-code/5ed799e5cc56bea9efff57398ca43e31d82784ff/LICENSE.md) | Gelesen, HTTP 200 | `728158fd1037143fad6907e8fa34804177e598b7326519503fe83cafdef849e6` |
| dependabot-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/dependabot/dependabot-core/9933aa69365f44c2e5c509f067be403618933e41/LICENSE) | Gelesen, HTTP 200 | `2510b446bc1f0cf9702453075d20cd88631e20e5642658edb7325d9c1eb534f7` |
| npm-license-pinned | [Offizielle Quelle](https://raw.githubusercontent.com/npm/cli/ae98c62586b6fea44114f72e249e246a2981de70/LICENSE) | Gelesen, HTTP 200 | `7610d223851f421d315df5e77974f1c68a04b97e02060e5bbbcf13d95e3ca257` |

## 3. Reproduzierbarkeit und Entscheidungssicherheit

Bei beweglichem Zweig gehört Abrufdatum plus Datei-Hash zum Beleg; konkrete Client-/Paketversion vor Aktivierung erneut fixieren. Alle untersuchten Lizenztexte sind unter dem jeweils vollständigen Commit im [Lizenzregister](DEPENDENCY_SELECTION.md) erreichbar. Lizenz-, API-/Quoten- und SDKquellen haben unterschiedliche Aussagekraft. Kein kopierter Fremdquelltext oder ausführbarer Download im Repository. Netzwerkfehler werden nicht als fehlende Herstellerfunktion interpretiert; insbesondere Groq/Gemini/Mistral/Cerebras bleiben kommerziell/datenschutzrechtlich unvollständig geprüft.
