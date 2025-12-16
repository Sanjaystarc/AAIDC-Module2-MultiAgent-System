from tools.repo_reader import read_readme

def repo_analyzer_agent(state: dict) -> dict:
    readme_text = read_readme()
    state["readme"] = readme_text
    return state
