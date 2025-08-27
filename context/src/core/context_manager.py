from mcp_servers import ide_logs_server, github_issues_server, error_db_server, stackoverflow_server

class ContextManager:
    """Fetches context fragments from multiple MCP-style servers and aggregates them."""
    def __init__(self):
        pass

    def get_context(self, error_message: str):
        # Query each server (they return lists of strings)
        ctx = []
        try:
            ctx.extend(ide_logs_server.fetch_ide_logs(error_message))
        except Exception:
            ctx.append("IDE logs: unavailable or no matching entries.")
        try:
            ctx.extend(github_issues_server.fetch_github_issues('your-repo-name', error_message))
        except Exception:
            ctx.append("GitHub: unavailable or no matching issues.")
        try:
            ctx.extend(error_db_server.query_error_database(error_message))
        except Exception:
            ctx.append("Error DB: unavailable.")
        try:
            ctx.extend(stackoverflow_server.search_stackoverflow(error_message))
        except Exception:
            ctx.append("StackOverflow: unavailable.")
        return ctx
