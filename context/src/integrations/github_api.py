import requests

def fetch_issues(repo: str, token: str):
    """Minimal GitHub issues fetch (requires token)."""
    url = f"https://api.github.com/repos/{repo}/issues"
    headers = {"Authorization": f"token {token}"} if token else {}
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code == 200:
        items = resp.json()
        return [it.get('title') for it in items]
    return [f"GitHub API error: {resp.status_code}"]
