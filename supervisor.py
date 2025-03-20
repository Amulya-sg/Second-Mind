# from ai_agents import generation_agent, reflection_agent, ranking_agent, evolution_agent, meta_review_agent, store_research, get_related_research

# # ✅ Supervisor Agent (Manages AI workflow)
# def supervisor_agent(query):
#     print("\n🔹 Step 1: Generating Research Ideas...")
#     ideas = generation_agent(query)
#     print(f"Generated Ideas: {ideas}")

#     print("\n🔹 Step 2: Validating & Refining Ideas...")
#     refined_ideas = reflection_agent(ideas)
#     print(f"Refined Ideas: {refined_ideas}")

#     print("\n🔹 Step 3: Ranking Ideas Using Llama 3.2...")
#     ranked_ideas = ranking_agent(refined_ideas)
#     print(f"Ranked Ideas: {ranked_ideas}")

#     print("\n🔹 Step 4: Improving Research Idea...")
#     improved_idea = evolution_agent(ranked_ideas)
#     print(f"Final Improved Idea: {improved_idea}")

#     print("\n🔹 Step 5: Storing Research in JSON Memory...")
#     store_research(improved_idea, "AI-generated refined research")
#     print(f"Stored in JSON: {improved_idea}")

#     print("\n🔹 Step 6: Checking Related Research...")
#     related_topic = get_related_research(query)
#     print(f"Similar Past Research: {related_topic}")

#     print("\n🔹 Step 7: Reviewing Process for Optimization...")
#     logs = f"Cycle 1: {ideas}, Cycle 2: {refined_ideas}, Cycle 3: {improved_idea}"
#     review = meta_review_agent(logs)
#     print(f"Optimization Suggestion: {review}")

# # ✅ Example Run
# if __name__ == "__main__":
#     supervisor_agent("Best energy solutions for cities")
from ai_agents import (
    generation_agent,
    reflection_agent,
    ranking_agent,
    evolution_agent,
    meta_review_agent,
)
from graph_memory import store_research, get_related_research

# ✅ Supervisor Agent (Manages AI workflow)
def supervisor_agent(query):
    print("\n🔹 Step 1: Generating Research Ideas... using generation agent")
    ideas = generation_agent(query)
    print(f"Generated Ideas: {ideas}")

    print("\n🔹 Step 2: Validating & Refining Ideas... using reflectio agent")
    refined_ideas = reflection_agent(ideas)
    print(f"Refined Ideas: {refined_ideas}")

    print("\n🔹 Step 3: Ranking Ideas Based on Feasibility... using ranking agent")
    ranked_ideas = ranking_agent(refined_ideas)
    print(f"Ranked Ideas: {ranked_ideas}")

    print("\n🔹 Step 4: Improving Research Idea... using evolution agent")
    improved_idea = evolution_agent(ranked_ideas)
    print(f"Final Improved Idea: {improved_idea}")

    print("\n🔹 Step 5: Storing Research in JSON Memory...")
    store_research(query, improved_idea)
    print(f"Stored in JSON: {improved_idea}")

    print("\n🔹 Step 6: Checking Related Research...")
    related_topic = get_related_research(query)
    print(f"Similar Past Research: {related_topic}")

    print("\n🔹 Step 7: Reviewing Process for Optimization...")
    logs = f"Cycle 1: {ideas}, Cycle 2: {refined_ideas}, Cycle 3: {improved_idea}"
    review = meta_review_agent(logs)
    print(f"Optimization Suggestion: {review}")
    return improved_idea


# # ✅ Example Run
# if __name__ == "__main__":
#     supervisor_agent("Best energy solutions for cities")
