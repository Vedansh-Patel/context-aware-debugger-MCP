# Context-Aware Debugging Agent

## Overview
Context-Aware Debugging Agent is an AI-assisted developer tool that helps identify and resolve runtime errors faster by combining local IDE logs, repository issue context, and community sources. It uses a modular context interface (MCP-style servers) to fetch context from multiple sources and synthesize actionable debugging suggestions.

## Features
- Parse local IDE logs and extract error signatures
- Fetch related GitHub issues and community answers (StackOverflow/LeetCode) via integrator modules
- Provide concise debugging suggestions through a CLI interface
- Simple, extensible architecture for adding more context servers (MCP-style)

## Project Structure
- `docs/` : Design notes and roadmap
- `src/` : Source code (core logic, MCP servers, integrations, UI)
- `tests/` : Basic unit tests
- `requirements.txt` : Python dependencies
- `Dockerfile` : Containerization setup

## How to Run (MVP)
1. Clone the repository and enter the folder:
   ```bash
   git clone https://github.com/your-username/context-aware-debugger.git
   cd context-aware-debugger
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run example (CLI):
   ```bash
   python src/ui/cli.py
   ```

## Notes
- This repository contains a working starter implementation with simulated context servers. Replace API keys and enable real API calls in `src/integrations/` to connect to live services.
- The project is structured to be extended into real MCP servers and real LLM integrations.
