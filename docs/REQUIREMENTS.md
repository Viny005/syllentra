# Requirements

## 1. Functional requirements

### 1.1 Document understanding
- The system should be able to process educational documents such as PDFs, lecture slides, notes, and similar materials.
- It should extract key concepts, explanations, and relationships between ideas.
- It should support structured summaries and topic organization.

### 1.2 Audio understanding
- The system should be able to process lecture recordings and transcripts.
- It should identify key explanations, examples, and important concepts.
- It should connect audio-based learning content to related document content when applicable.

### 1.3 Adaptive tutoring
- The system should personalize explanations based on learner understanding and context.
- It should adjust teaching strategy and depth depending on the learner's progress.
- It should provide educational guidance that is clear, aligned with intent, and appropriate to the level of study.

### 1.4 Learning strategy selection
- The system should support multiple learning approaches, including:
  - page-by-page explanations
  - concept-by-concept teaching
  - broader overview explanations
- The chosen learning mode should reflect the educational task and user needs.

### 1.5 Research and verification
- The system should be able to consult reliable sources when needed to validate or enrich explanations.
- It should clearly distinguish between educational synthesis and external factual verification.

### 1.6 Interactive learning support
- The system should generate explanations, practice questions, quizzes, and exercises.
- It should support active learning and reinforcement of key concepts.

### 1.7 Progress awareness
- When explicitly authorized, the system may maintain learning continuity and progress tracking.
- Progress insights should support personalization without placing undue reliance on sensitive personal data.

### 1.8 Multilingual support
- The project should consider support for French, German, and English.
- Multilingual capabilities should be introduced with careful evaluation of content quality and user needs.

## 2. Non-functional requirements

- The architecture should remain modular and easy to evolve.
- The system should be designed for maintainability and testability.
- The project should prioritize privacy, consent, and secure handling of user data.
- The design should support future integration with additional AI models and tools.
- It should be possible to introduce new capabilities incrementally without destabilizing the entire system.

## 3. Security and privacy

- The project must not store, expose, or commit credentials, secrets, or personal information.
- User consent should be explicit before recording, analyzing, or persisting learning data.
- Private lecture recordings, private notes, or restricted educational materials should not be included in the repository or test data without authorization.
- Data minimization should be applied wherever possible.
- Access controls and auditability should be considered for any future deployment.

## 4. Accessibility and usability

- The system should be designed to be understandable and usable by a diverse learner population.
- Future interfaces should accommodate accessibility needs, including readable content, clear navigation, and inclusive design.
- Explanations should be understandable across varying levels of academic background.

## 5. Unresolved questions

The following items remain open and require research before implementation:

- Which document formats and ingestion workflows should be prioritized first?
- Which AI capabilities are needed for initial prototypes versus later phases?
- What level of transcript and audio processing should be supported in early versions?
- Which user data features are essential versus optional?
- How will user consent and privacy be enforced in future products?
- What type of learning progress tracking, if any, should be included under authorization?
- Which user interfaces and interaction models are most appropriate for the target audience?

## 6. Constraints

- No technology stack decisions should be treated as final without evaluation.
- No application functionality should be claimed before it is validated.
- The project must emphasize educational quality, trustworthiness, and learner safety.
