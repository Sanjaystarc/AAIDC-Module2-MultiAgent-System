from pathlib import Path

def read_readme(repo_path: str = ".") -> str:
    """
    Tool: Reads README.md content from a repository
    """
    readme_path = Path(repo_path) / "README.md"
    if not readme_path.exists():
        return "README.md not found in repository."
    return readme_path.read_text(encoding="utf-8")

