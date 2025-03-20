# from ai_agents import generation_agent, reflection_agent, ranking_agent, evolution_agent
# from graph_memory import store_research, get_related_research
# from voting_system import compute_final_score

# # ✅ Full AI Research Pipeline
# def research_pipeline(query):
#     print("\n🔹 Step 1: Generating Initial Research Ideas...")
#     ideas = generation_agent(query)
#     print(f"Generated Ideas: {ideas}")

#     print("\n🔹 Step 2: Validating & Refining Ideas...")
#     refined_ideas = reflection_agent(ideas)
#     print(f"Refined Ideas: {refined_ideas}")

#     print("\n🔹 Step 3: Ranking Ideas Using Real-World Data...")
#     ranked_ideas = ranking_agent(refined_ideas)
#     print(f"Ranked Ideas: {ranked_ideas}")

#     print("\n🔹 Step 4: Improving Research Idea...")
#     improved_idea = evolution_agent(ranked_ideas)
#     print(f"Final Improved Idea: {improved_idea}")

#     print("\n🔹 Step 5: Storing Research in Graph Memory...")
#     store_research(improved_idea, "AI-generated refined research")
#     print(f"Stored in Graph Memory: {improved_idea}")

#     print("\n🔹 Step 6: Checking Related Research...")
#     related_topic = get_related_research(query)
#     print(f"Similar Past Research: {related_topic}")

#     print("\n🔹 Step 7: Voting-Based Selection of Best Idea...")
#     votes = {
#         ideas.split("\n")[0]: {"score": 8, "confidence": 70},
#         refined_ideas.split("\n")[0]: {"score": 9, "confidence": 85},
#         improved_idea: {"score": 9.5, "confidence": 90},
#     }
#     final_score = compute_final_score(votes)
#     print(f"Final Decision Score: {final_score:.2f}")

#     return improved_idea

# # ✅ Example Run
# if __name__ == "__main__":
#     user_query = input("Enter a research query: ")
#     best_idea = research_pipeline(user_query)
#     print(f"\n🎯 FINAL RESEARCH RECOMMENDATION: {best_idea}")
from ai_agents import generation_agent, reflection_agent, ranking_agent, evolution_agent
from graph_memory import store_research, get_related_research
from voting_system import compute_final_score

# ✅ Full AI Research Pipeline
def research_pipeline(query):
    print("\n🔹 Step 1: Generating Initial Research Ideas...")
    ideas = generation_agent(query)
    print(f"Generated Ideas using geneartion agent : {ideas}")

    print("\n🔹 Step 2: Validating & Refining Ideas...")
    refined_ideas = reflection_agent(ideas)
    print(f"Refined Ideas using reflection agent: {refined_ideas}")

    print("\n🔹 Step 3: Ranking Ideas Using Feasibility...")
    ranked_ideas = ranking_agent(refined_ideas)
    print(f"Ranked Ideas using ranking agent: {ranked_ideas}")

    print("\n🔹 Step 4: Improving Research Idea...")
    improved_idea = evolution_agent(ranked_ideas)
    print(f"Final Improved Idea using evolution agent: {improved_idea}")

    print("\n🔹 Step 5: Storing Research in JSON Memory...")
    store_research(query, improved_idea)
    print(f"Stored in JSON: {improved_idea}")

    print("\n🔹 Step 6: Checking Related Research...")
    related_topic = get_related_research(query)
    print(f"Similar Past Research: {related_topic}")

    print("\n🔹 Step 7: Voting-Based Selection of Best Idea...")
    votes = {
        ideas: {"score": 8, "confidence": 70},
        refined_ideas: {"score": 9, "confidence": 85},
        improved_idea: {"score": 9.5, "confidence": 90},
    }
    final_score = compute_final_score(votes)
    print(f"Final Decision Score: {final_score:.2f}")

    return improved_idea

# ✅ Example Run
if __name__ == "__main__":
    user_query = input("Enter a research query: ")
    best_idea = research_pipeline(user_query)
    print(f"\n🎯 FINAL RESEARCH RECOMMENDATION: {best_idea}")
