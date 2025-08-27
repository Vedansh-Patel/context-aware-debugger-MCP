def fetch_github_issues(repo: str, error_signature: str):
    """Simulated GitHub issue fetch. Replace with real API calls in integrations/github_api.py."""
    # Simple heuristic: if 'ZeroDivisionError' in signature, return a mock issue
    if 'ZeroDivisionError' in error_signature:
        return [f"GitHub issue: Possible division by zero reported in {repo} (issue #123)"]
    return ["GitHub: no matching issues found."]
