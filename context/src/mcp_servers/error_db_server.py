import json, os
DB_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'src', 'config', 'error_db.json')

def query_error_database(error_signature: str):
    """Return known fixes from a small JSON DB (simulated)."""
    results = []
    try:
        with open(DB_PATH, 'r') as f:
            db = json.load(f)
        for key, fixes in db.items():
            if key in error_signature:
                results.extend([f"ErrorDB: {s}" for s in fixes])
    except FileNotFoundError:
        results.append("ErrorDB: database not initialized.")
    return results
