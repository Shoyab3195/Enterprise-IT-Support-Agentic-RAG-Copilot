#from app.core.config import get_settings

#settings = get_settings()

#print(f"App Name: {settings.app_name}")
#print(f"App Environment: {settings.openai_api_key}")

from app.services.ingestion import chunk_documents, load_file
from pathlib import Path
from app.rag.vectorstore import add_documents


docs = load_file(Path("data/sample_kb/company_it_handbook.md"))

chunks = chunk_documents(docs)


add_documents(chunks)