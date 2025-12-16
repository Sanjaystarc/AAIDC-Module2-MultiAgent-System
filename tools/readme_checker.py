def check_missing_sections(readme_text: str) -> list:
    """
    Tool: Checks for missing README sections
    """
    required_sections = ["installation", "usage", "license"]
    missing = []

    for section in required_sections:
        if section not in readme_text.lower():
            missing.append(section)

    return missing
