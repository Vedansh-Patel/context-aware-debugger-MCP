from core.agent import DebugAgent

def main():
    print("Starting Context-Aware Debugging Agent (MVP)...")
    agent = DebugAgent()
    # Example usage
    example_error = "ZeroDivisionError: division by zero at main.py:42"
    suggestions = agent.handle_error(example_error)
    print("\nSample suggestions for demo error:\n")
    for s in suggestions:
        print("-", s)

if __name__ == '__main__':
    main()
