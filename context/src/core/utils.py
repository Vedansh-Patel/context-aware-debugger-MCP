def safe_truncate(text, max_len=500):
    if text is None:
        return ''
    return text if len(text) <= max_len else text[:max_len] + '...'
