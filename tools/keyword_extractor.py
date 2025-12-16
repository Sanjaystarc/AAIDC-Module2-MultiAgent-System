def extract_keywords(text: str) -> list:
    """
    Tool: Simple keyword extraction
    """
    words = text.lower().split()
    keywords = set(word.strip(".,") for word in words if len(word) > 6)
    return list(keywords)[:10]
