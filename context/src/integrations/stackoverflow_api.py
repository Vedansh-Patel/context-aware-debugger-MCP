import requests

def search_questions(query: str):
    url = "https://api.stackexchange.com/2.3/search"
    params = {"order": "desc", "sort": "activity", "intitle": query, "site": "stackoverflow"}
    resp = requests.get(url, params=params, timeout=10)
    if resp.status_code == 200:
        items = resp.json().get('items', [])
        return [it.get('title') for it in items]
    return [f"StackOverflow API error: {resp.status_code}"]
