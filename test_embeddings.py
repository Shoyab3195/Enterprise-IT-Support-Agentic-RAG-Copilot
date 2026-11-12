
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector = embeddings.embed_query(
    "How can I reset my company password?"
)

print("Embedding dimension:", len(vector))
print("First 5 values:", vector[:5])
print("Embedding test successful!")
