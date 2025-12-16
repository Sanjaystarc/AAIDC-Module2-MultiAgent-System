from graph.workflow import build_graph

if __name__ == "__main__":
    graph = build_graph()

    result = graph.invoke({})

    print("\n📘 MULTI-AGENT OUTPUT\n")
    print("Suggested Title:", result.get("suggested_title"))
    print("Suggested Tags:", result.get("suggested_tags"))
    print("Review Feedback:", result.get("review_feedback"))

