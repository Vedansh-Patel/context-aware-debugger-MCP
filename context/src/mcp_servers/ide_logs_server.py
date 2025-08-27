import os
from typing import List

LOG_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'example_logs', 'app.log')

def fetch_ide_logs(error_signature: str) -> List[str]:
    """Read the example log file and return lines that contain part of the error signature."""
    results = []
    try:
        with open(LOG_PATH, 'r') as f:
            for line in f.readlines()[-200:]:  # check last 200 lines
                if any(token in line for token in error_signature.split()):
                    results.append(f"Log: {line.strip()}")
    except FileNotFoundError:
        results.append("Log file not found (example logs not present)." )
    return results
