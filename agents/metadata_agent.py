import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from tools.keyword_extractor import extract_keywords


def metadata_agent(state: dict) -> dict:
    """
    Agent: Metadata Recommender
    Uses Gemini LLM to generate an improved title and tags
    """

    readme = state.get("readme", "")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.4,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

    prompt = f"""
    You are an AI assistant helping improve AI project presentations.

    Based on the following README content, suggest:
    1. One improved project title
    2. 5 concise relevant tags

    README:
    {readme}
    """

    response = llm.invoke([HumanMessage(content=prompt)])

    # Simple parsing (keep it robust)
    content = response.content.strip()

    keywords = extract_keywords(readme)

    state["suggested_title"] = content.split("\n")[0]
    state["suggested_tags"] = keywords

    return state

