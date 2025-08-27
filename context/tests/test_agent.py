from core.agent import DebugAgent

def test_handle_error_basic():
    agent = DebugAgent()
    out = agent.handle_error('ZeroDivisionError at main.py:10')
    assert any('ZeroDivisionError' in s or 'Suggested fix' in s for s in out)
