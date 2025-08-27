from integrations.leetcode_api import fetch_leetcode_discussions

def test_leetcode_sim():
    res = fetch_leetcode_discussions('ZeroDivisionError')
    assert isinstance(res, list)
