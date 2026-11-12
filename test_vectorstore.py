from app.rag.vectorstore import get_vectorstore

print("Connecting to Pinecone...")

store = get_vectorstore()

print("Pinecone vector store initialized!")

print("Testing similarity search...")

results = store.similarity_search(
    "How can I reset my company password?",
    k=2
)

print("Search successful!")
print("Retrieved documents:", len(results))