from langgraph.graph import StateGraph
from agents.repo_analyzer import repo_analyzer_agent
from agents.metadata_agent import metadata_agent
from agents.reviewer_agent import reviewer_agent

def build_graph():
    workflow = StateGraph(dict)

    workflow.add_node("repo_analyzer", repo_analyzer_agent)
    workflow.add_node("metadata", metadata_agent)
    workflow.add_node("reviewer", reviewer_agent)

    workflow.set_entry_point("repo_analyzer")
    workflow.add_edge("repo_analyzer", "metadata")
    workflow.add_edge("metadata", "reviewer")
    workflow.set_finish_point("reviewer")

    return workflow.compile()
