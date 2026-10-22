# Syllentra AI

Syllentra AI is a documentation-first project for an adaptive AI learning companion that helps students understand and master complex academic subjects.

## Mission

The mission of Syllentra AI is to transform university lectures, documents, and audio recordings into personalized learning experiences. The project aims to support learners with explanations, structured guidance, and interactive study workflows that adapt to individual needs, context, and progress.

## Current status

This repository is in its planning and research phase. The project vision, requirements, and architecture direction are being documented before implementation begins. At this stage, no application code, AI workflows, or production-ready features are being claimed.

## Long-term vision

Syllentra AI is intended to help students engage more effectively with educational materials by combining document understanding, audio comprehension, and adaptive tutoring. Planned capabilities include:

- Analysis of PDF files, lecture slides, notes, and other educational materials
- Processing of lecture recordings and transcripts to surface key explanations and concepts
- Adaptive tutoring based on learner understanding, preferences, and progress
- Guidance for page-by-page, concept-by-concept, or overview-based study approaches
- Verification and supplementation of explanations using reliable external sources
- Generation of explanations, exercises, quizzes, and practical examples
- Longitudinal learning continuity and progress awareness when authorized
- Initial support for French, German, and English
- A modular architecture that can evolve with additional models, tools, and specialized agents

## Preliminary roadmap

The project is currently focused on the following areas:

1. Research and problem framing
2. Requirements gathering and prioritization
3. Architecture design and decision recording
4. Prototype exploration
5. Validation and testing strategy
6. Iterative implementation using verified milestones

## Project principle

This project follows a disciplined, incremental approach: research and document decisions before implementation, prioritize security and privacy, and avoid premature technology choices.

## Note

Syllentra AI is intentionally not claiming finished features at this stage. The project is being structured for future, evidence-based development using GitHub Issues and Pull Requests.

## AI development workflow

Start with [AGENTS.md](AGENTS.md), the [PACE workflow](docs/ai/WORKFLOW.md), and the [verified project context](docs/ai/PROJECT_CONTEXT.md).


## Vorbereitung von Gestaltung und Entwicklung

[Design System](docs/design/DESIGN_SYSTEM.md), [Integration und offene Entscheidungen](docs/development/INTEGRATION_ROADMAP.md), [Codex-/Claude-Verfahren](docs/ai-tooling/CODEX_CLAUDE_WORKFLOW.md) sowie [Quellen und Lizenzen](docs/development/SOURCES.md) sind Vorschläge **Empfohlen / Zur Entscheidung**. Drei deklarative lokale Skills, keine Anwendung oder neue Toolaktivierung. Persönliche Qualitätspriorität und künftiger Vergleichsrahmen bis 20 EUR brutto/Monat sind bestätigt; **keine Ausgabe genehmigt**, V1-Multiuser-/Schutzanforderungen unverändert.


## Lokaler interaktiver Prototyp aus Mission 8

Der [Frontend-Prototyp](prototypes/frontend/README.md) enthält acht navigierbare Bereiche, DE/FR/EN, Hell/Dunkel/System und ausschließlich fiktive lokale Daten. Start mit Node 24.x: im Verzeichnis `prototypes/frontend` zuerst `npm ci --ignore-scripts`, dann `npm run dev`. Keine operative V1, echte KI, Anmeldung, Synchronisierung oder Kontoisolation. [Prüfungen und Screenshots](docs/design/PROTOTYPE_REVIEW.md), [installierte Lizenzen](prototypes/frontend/LICENSES.md). Experimenteller Stack, TECH-O-03 offen; keine Ausgabe oder Veröffentlichung.


## Lokale experimentelle Backendgrundlage aus Mission 9

[Backendanleitung](prototypes/backend/README.md) und [Prüfbericht](docs/development/BACKEND_PROTOTYPE_REVIEW.md): FastAPI-/PostgreSQL-Probe mit synthetischen Sicherheitsprüfungen, Sessions, Kontofilterung und Serverflags. Normale Anmeldung bleibt blockiert; keine produktive Identität, Administration, KI oder Cloud. Frontend bleibt getrennte Demo, technische Auswahl offen. Keine Veröffentlichung oder Ausgabe.
