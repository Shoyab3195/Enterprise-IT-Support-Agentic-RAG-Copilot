from app.rag.vectorstore import get_retriever

retriever = get_retriever()

query = "How can I reset my company password?"

results = retriever.invoke(query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print("Source:", doc.metadata.get("source"))
    print("Content:", doc.page_content)