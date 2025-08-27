from core.context_manager import ContextManager

class DebugAgent:
    """High-level agent that orchestrates context retrieval and generates suggestions."""
    def __init__(self):
        self.context_manager = ContextManager()

    def handle_error(self, error_message: str):
        """Return a list of suggestions for the given error message."""
        # 1. Retrieve structured context from context manager
        contexts = self.context_manager.get_context(error_message)
        # 2. Simple heuristic summarization (replace with LLM later)
        suggestions = []
        suggestions.append(f"Error: {error_message}")
        suggestions.extend(contexts)
        # Very simple "fix" templates for demo
        if "ZeroDivisionError" in error_message:
            suggestions.append("Suggested fix: check denominator before division and handle zero-case.")
            suggestions.append("Code hint: if y != 0: result = x / y else: raise ValueError('denominator zero')")
        return suggestions
