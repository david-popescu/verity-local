from difflib import SequenceMatcher


def string_similarity(user_input: str, pattern: str) -> float:
    return SequenceMatcher(None, user_input, pattern).ratio()
