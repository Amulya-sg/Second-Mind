# from py2neo import Graph
# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # 🔹 Set up Neo4j Connection (Make sure Neo4j is running!)
# graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# # 🔹 Initialize FAISS for fast retrieval
# model = SentenceTransformer("all-MiniLM-L6-v2")
# index = faiss.IndexFlatL2(384)

# # ✅ Function to store research ideas in Neo4j
# def store_research(topic, details):
#     query = f"""
#     MERGE (r:Research {{topic: '{topic}'}})
#     SET r.details = '{details}'
#     """
#     graph.run(query)

# # ✅ Function to retrieve related research topics
# def get_related_research(query):
#     faiss_vector = np.array([model.encode(query)])
#     _, I = index.search(faiss_vector, 1)
#     return research_topics[I[0][0]]

# # ✅ Store research topics in FAISS
# research_topics = ["Solar Panels", "Solar Windows", "Wind Energy"]
# embeddings = np.array([model.encode(topic) for topic in research_topics])
# index.add(embeddings)

# # Example Run
# if __name__ == "__main__":
#     store_research("Solar Panels", "Efficiency: 20%, Cost: $200/unit")
#     print(get_related_research("Best urban energy solution"))

# import faiss
# import numpy as np
# from sentence_transformers import SentenceTransformer

# # ✅ Initialize FAISS
# model = SentenceTransformer("all-MiniLM-L6-v2")
# index = faiss.IndexFlatL2(384)
# research_topics = ["Solar Panels", "Solar Windows", "Wind Energy"]
# embeddings = np.array([model.encode(topic) for topic in research_topics])
# index.add(embeddings)

# # ✅ Function to retrieve similar topics using FAISS
# def get_related_research(query):
#     query_vector = np.array([model.encode(query)])
#     _, I = index.search(query_vector, 1)
#     return research_topics[I[0][0]]

# # ✅ Example Run
# if __name__ == "__main__":
#     print(get_related_research("Best urban energy solution"))


# import json
# import os

# # ✅ File to store research data
# DATA_FILE = "data/research_memory.json"

# # ✅ Function to store research topics
# def store_research(topic, details):
#     data = {}
#     if os.path.exists(DATA_FILE):
#         with open(DATA_FILE, "r") as file:
#             data = json.load(file)

#     data[topic] = details

#     with open(DATA_FILE, "w") as file:
#         json.dump(data, file, indent=4)

# # ✅ Function to retrieve related research topics
# def get_related_research(topic):
#     if not os.path.exists(DATA_FILE):
#         return "No related research found."

#     with open(DATA_FILE, "r") as file:
#         data = json.load(file)

#     for key in data:
#         if topic.lower() in key.lower():
#             return data[key]

#     return "No related research found."

# # ✅ Example Run
# if __name__ == "__main__":
#     store_research("Solar Panels", "Efficiency: 20%, Cost: $200/unit")
#     print(get_related_research("Solar"))

import json
import os

# ✅ File to store research data
DATA_FILE = "data/research_memory.json"

# ✅ Function to store research topics
def store_research(topic, details):
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r",encoding="utf-8") as file:
            data = json.load(file)

    data[topic] = details

    with open(DATA_FILE, "w",encoding="utf-8") as file:
        json.dump(data, file, indent=4,ensure_ascii=False)

# ✅ Function to retrieve related research topics
def get_related_research(topic):
    if not os.path.exists(DATA_FILE):
        return json.dumps({"message": "No related research found."})

    with open(DATA_FILE, "r",encoding="utf-8") as file:
        data = json.load(file)

    for key in data:
        if topic.lower() in key.lower():
            return json.dumps({"topic": key, "details": data[key]})

    return json.dumps({"message": "No related research found."})

# ✅ Example Run
if __name__ == "__main__":
    store_research("Solar Panels", "Efficiency: 20%, Cost: $200/unit")
    print(get_related_research("Solar"))
