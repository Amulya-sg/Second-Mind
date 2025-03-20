# import ollama  # Import Ollama package
# import json
# import os
# import requests
# from bs4 import BeautifulSoup

# # 🔹 File to store research memory (replaces Neo4j/FAISS)
# DATA_FILE = "data/research_memory.json"

# # ✅ Function to store research topics in JSON
# def store_research(topic, details):
#     data = {}
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as file:
#             data = json.load(file)

#     data[topic] = details

#     with open(DATA_FILE, "w") as file:
#         json.dump(data, file, indent=4)

# # ✅ Function to retrieve similar research topics
# def get_related_research(query):
#     if not os.path.exists(DATA_FILE):
#         return "No related research found."

#     with open(DATA_FILE, "r") as file:
#         data = json.load(file)

#     for key in data:
#         if query.lower() in key.lower():
#             return data[key]

#     return "No related research found."

# # ✅ Generation Agent (Llama 3.2 generates research ideas)
# def generation_agent(query):
#     prompt = f"You are an AI researcher. Generate 3 research ideas for '{query}'."
#     response = ollama.chat(model="llama3", messages=[{"role": "system", "content": prompt}])
#     return response["message"]["content"]

# # ✅ Reflection Agent (Llama 3.2 validates and refines ideas)
# def reflection_agent(idea):
#     prompt = f"Assess the validity and relevance of this research idea: '{idea}'. Provide reasoning and improvements."
#     response = ollama.chat(model="llama3", messages=[{"role": "system", "content": prompt}])
#     return response["message"]["content"]

# # ✅ Ranking Agent (Ranks ideas based on feasibility)
# def ranking_agent(idea):
#     prompt = f"Rank the research idea: '{idea}' based on feasibility, cost, and impact. Provide a score out of 10."
#     response = ollama.chat(model="llama3", messages=[{"role": "system", "content": prompt}])
#     return response["message"]["content"]

# # ✅ Evolution Agent (Llama 3.2 refines research ideas)
# def evolution_agent(idea):
#     prompt = f"Refine the research idea: '{idea}' by incorporating the latest trends."
#     response = ollama.chat(model="llama3", messages=[{"role": "system", "content": prompt}])
#     return response["message"]["content"]

# # ✅ Meta-Review Agent (Llama 3.2 evaluates & optimizes process)
# def meta_review_agent(logs):
#     prompt = f"Review AI research workflow logs and suggest improvements. Logs: {logs}"
#     response = ollama.chat(model="llama3", messages=[{"role": "system", "content": prompt}])
#     return response["message"]["content"]

from openai import OpenAI
import json
import os

# 🔹 OpenRouter API Client Setup
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# 🔹 File to store research memory
DATA_FILE = "data/research_memory.json"

# ✅ Function to store research topics in JSON
def store_research(topic, details):
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r",encoding="utf-8") as file:
            data = json.load(file)
    data[topic] = details

    with open(DATA_FILE, "w",encoding="utf-8") as file:
        json.dump(data, file,indent=4)

# ✅ Function to retrieve similar research topics
def get_related_research(query):
    if not os.path.exists(DATA_FILE):
        return json.dumps({"message": "No related research found."},indent=4)

    with open(DATA_FILE, "r",encoding="utf-8") as file:
        data = json.load(file)

    for key in data:
        if query.lower() in key.lower():
            return json.dumps({"topic": key, "details": data[key]},indent=4)

    return json.dumps({"message": "No related research found."},indent=4)

# ✅ OpenAI Completion Request Function
def openai_chat(prompt):
    response = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "",  # Optional: For rankings
            "X-Title": "hehe",  # Optional: For rankings
        },
        model="deepseek/deepseek-r1-zero:free",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content

# ✅ Generation Agent (Research idea generation)
def generation_agent(query):
    prompt = f"You are an AI researcher. Generate 3 research ideas for '{query}'."
    return json.dumps({"query": query, "ideas": openai_chat(prompt)})

# ✅ Reflection Agent (Idea validation & refinement)
def reflection_agent(idea):
    prompt = f"Assess the validity and relevance of this research idea: '{idea}'. Provide reasoning and improvements."
    return json.dumps({"idea": idea, "assessment": openai_chat(prompt)})

# ✅ Ranking Agent (Ranks ideas based on feasibility)
def ranking_agent(idea):
    prompt = f"Rank the research idea: '{idea}' based on feasibility, cost, and impact. Provide a score out of 10."
    return json.dumps({"idea": idea, "ranking": openai_chat(prompt)})

# ✅ Evolution Agent (Refines research ideas with latest trends)
def evolution_agent(idea):
    prompt = f"Refine the research idea: '{idea}' by incorporating the latest trends."
    return json.dumps({"idea": idea, "refined": openai_chat(prompt)})

# ✅ Meta-Review Agent (Evaluates & optimizes workflow)
def meta_review_agent(logs):
    prompt = f"Review AI research workflow logs and suggest improvements. Logs: {logs}"
    return json.dumps({"logs": logs, "review": openai_chat(prompt)})

