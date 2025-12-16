from tools.readme_checker import check_missing_sections

def reviewer_agent(state: dict) -> dict:
    readme = state.get("readme", "")
    missing = check_missing_sections(readme)

    state["review_feedback"] = (
        f"Missing sections: {missing}" if missing else "README looks complete."
    )
    return state
