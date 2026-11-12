
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    app_name: str = "Enterprise IT Support Agentic RAG Copilot"
    app_env: str = "development"

    # Local Ollama configuration
    embedding_model: str = "nomic-embed-text"
    embedding_dimension: int = 768
    llm_model: str = "qwen2.5:1.5b"
    ollama_base_url: str = "http://localhost:11434"

    # Pinecone configuration
    pinecone_api_key: str = ""
    pinecone_index_name: str = "fde-it-support-rag-nomic"
    pinecone_namespace: str = "company-it-kb-nomic"
    

    # Tavily configuration
    tavily_api_key: str = ""

    # Application configuration
    top_k: int = 4
    max_retries: int = 1
    admin_api_key: str = "change-me"

    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
