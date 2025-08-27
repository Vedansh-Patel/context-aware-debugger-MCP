# Architecture

The system is separated into these parts:
- **Core**: DebugAgent and ContextManager. Coordinates fetching context and producing suggestions.
- **MCP-style servers**: Small modules that expose context from a source (IDE logs, GitHub issues, error DB, StackOverflow, LeetCode).
- **Integrations**: API wrappers for external services.
- **UI**: CLI for MVP and Streamlit for optional web demo.
- **Tests**: Unit tests for core modules and servers.
