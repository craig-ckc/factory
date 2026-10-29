# Code quality

Shared knowledge for Implementation, Refactoring, and Code Review; this is not an extra procedure or agent.

- Prefer cohesive modules, explicit ownership, narrow interfaces, and consistent naming. Separate responsibilities for maintainability, not by rigid universal directory patterns.
- Favor clear data contracts, predictable error handling, and deliberate state boundaries. Keep dependencies pointing toward stable abstractions where that helps.
- Reuse existing patterns rather than create equivalent layers. Abstractions must remove real repetition or stabilize a boundary.
- Keep functions and modules understandable through simple control flow; optimize for future debugging, not minimum lines.
- Respect repository conventions and language-specific lint/style (including notation preferences) without prescribing framework rules globally.
- When a recurring failure can be prevented structurally, prefer types, lint, tests, or architecture over another paragraph in instruction files.
