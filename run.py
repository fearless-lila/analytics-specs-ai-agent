import os
import ollama
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model for embeddings
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load history files
history_dir = "history"
history_texts = []
for file in os.listdir(history_dir):
    if file.endswith(".md"):
        with open(os.path.join(history_dir, file), "r") as f:
            history_texts.append(f.read())

# Create embeddings
embeddings = embed_model.encode(history_texts, convert_to_numpy=True)

# Build FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Function to get relevant history
def get_relevant_history(query, top_k=3):
    query_vec = embed_model.encode([query], convert_to_numpy=True)
    D, I = index.search(query_vec, top_k)
    return "\n\n".join([history_texts[i] for i in I[0]])

# Load prompt template
with open("prompts/base_prompt.txt") as f:
    base_prompt = f.read()

# Example user input
user_request = "Track user interactions for the new checkout page"

# Retrieve relevant history
relevant_history = get_relevant_history(user_request)

# Prepare final prompt
final_prompt = base_prompt.format(history_md=relevant_history, user_request=user_request)

# Call Ollama
response = ollama.chat(model="llama3.2:latest", messages=[{"role": "user", "content": final_prompt}])
print(response["message"]["content"])

# Optionally save output
with open("generated/generated_requirement.md", "w") as f:
    f.write(response["message"]["content"])
