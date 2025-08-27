from core.agent import DebugAgent

def run_cli():
    agent = DebugAgent()
    print('Context-Aware Debugging Agent (CLI)')
    print("Type an error message (or 'exit') to get debugging suggestions.")
    while True:
        error = input('\nError> ').strip()
        if error.lower() in ('exit', 'quit'):
            print('Exiting.')
            break
        suggestions = agent.handle_error(error)
        print('\nSuggestions:')
        for s in suggestions:
            print('-', s)

if __name__ == '__main__':
    run_cli()
