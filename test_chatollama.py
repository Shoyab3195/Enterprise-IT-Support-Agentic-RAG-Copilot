from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:1.5b",
    base_url="http://localhost:11434",
    temperature=0,
    num_predict=50,
    num_ctx=2048
)

response = llm.invoke(
    "Reply with exactly one word: Hello"
)

print("LLM response:", response.content)