# MCP-style Servers

Each server implements a simple function interface to return pieces of context given an error signature.
Example servers are:
- `ide_logs_server` - reads a local log file and extracts recent errors
- `github_issues_server` - queries GitHub for issues/PR titles containing the error signature
- `error_db_server` - local JSON database of known errors to fixes
- `stackoverflow_server` - queries StackOverflow (simulated in MVP)
- `leetcode_server` - fetches discussions for algorithmic errors (simulated in MVP)
