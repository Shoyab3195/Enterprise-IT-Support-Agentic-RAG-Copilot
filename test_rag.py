
from app.core.config import get_settings
from app.rag.vectorstore import get_retriever
from langchain_ollama import ChatOllama

settings = get_settings()

# Initialize retriever
retriever = get_retriever()

# Initialize local LLM
llm = ChatOllama(
    model=settings.llm_model,
    base_url=settings.ollama_base_url,
    temperature=0
)

# Ask a question
query = "What is the company's policy for software installation?"

# Retrieve relevant documents
docs = retriever.invoke(query)

# Include source information in the context
context = "\n\n".join(
    f"Source: {doc.metadata.get('source', 'Unknown')}\n"
    f"Content: {doc.page_content}"
    for doc in docs
)

# Strict grounding prompt
prompt = f"""
You are an Enterprise IT Support Assistant.

Your task is to answer the user's question using ONLY the
retrieved company knowledge-base context.

STRICT RULES:
1. Use only facts explicitly stated in the context.
2. Never use outside knowledge or assumptions.
3. Never invent steps, procedures, policies, or instructions.
4. Preserve all important conditions, restrictions, and exceptions.
5. If the context does not contain enough information to answer,
   respond exactly:
   "I could not find this information in the company knowledge base.
   Please contact the IT Service Desk."
6. Keep your answer concise and factual.

RETRIEVED CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:
"""

# Generate answer
response = llm.invoke(prompt)

print("\nQuestion:", query)
print("\nRetrieved documents:", len(docs))
print("\nRAG Answer:\n", response.content)
