def search_stackoverflow(error_signature: str):
    """Simulated StackOverflow search results."""
    if 'ZeroDivisionError' in error_signature:
        return ["StackOverflow: check division operands; common bug when parsing inputs."]
    return ["StackOverflow: no obvious matches."]
