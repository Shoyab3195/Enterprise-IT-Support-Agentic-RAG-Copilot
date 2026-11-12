from app.core.config import get_settings

settings = get_settings()

print("Embedding model:", settings.embedding_model)
print("Embedding dimension:", settings.embedding_dimension)
print("LLM model:", settings.llm_model)
print("Ollama URL:", settings.ollama_base_url)

print("Pinecone index:", settings.pinecone_index_name)
print("Pinecone namespace:", settings.pinecone_namespace)

print("Pinecone API key configured:", bool(settings.pinecone_api_key))
print("Tavily API key configured:", bool(settings.tavily_api_key))