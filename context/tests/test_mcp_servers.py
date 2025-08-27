from mcp_servers.ide_logs_server import fetch_ide_logs

def test_ide_logs_no_file():
    # Should not raise when log file missing; returns a list
    res = fetch_ide_logs('DummyError')
    assert isinstance(res, list)
