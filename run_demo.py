# from supervisor import supervisor_agent

# # ✅ Simple CLI to Run the Research Refinement System
# if __name__ == "__main__":
#     print("\n🎓 Welcome to the AI Research Refinement System! 🎓\n")
    
#     while True:
#         user_query = input("\n🔍 Enter a research topic (or type 'exit' to quit): ")
#         if user_query.lower() == "exit":
#             print("\n🚀 Exiting the system. Thank you! 🚀")
#             break
#         print("\n⏳ Processing your research query...\n")
#         best_idea = supervisor_agent(user_query)
#         print(f"\n🎯 FINAL AI RESEARCH RECOMMENDATION: {best_idea}\n")


from supervisor import supervisor_agent

# ✅ Simple CLI to Run the Research Refinement System
if __name__ == "__main__":
    print("\n🎓 Welcome to the AI Research Refinement System! 🎓\n")
    
    while True:
        user_query = input("\n🔍 Enter a research topic (or type 'exit' to quit): ")
        if user_query.lower() == "exit":
            print("\n🚀 Exiting the system. Thank you! 🚀")
            break
        print("\n⏳ Processing your research query...\n")
        best_idea = supervisor_agent(user_query)
        print(f"\n🎯 FINAL AI RESEARCH RECOMMENDATION: {best_idea}\n")
