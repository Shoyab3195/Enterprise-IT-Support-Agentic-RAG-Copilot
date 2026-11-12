
import time

from pinecone import Pinecone, ServerlessSpec
from langchain_ollama import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore

from app.core.config import get_settings

settings = get_settings()

_embeddings = None
_vectorstore = None


def get_embeddings():
    """Initialize local Ollama embeddings."""

    global _embeddings

    if _embeddings is None:
        _embeddings = OllamaEmbeddings(
            model=settings.embedding_model,
            base_url=settings.ollama_base_url
        )

    return _embeddings


def ensure_index():
    """Create a Pinecone index if it does not exist.
    Never delete an existing index automatically.
    """

    if not settings.pinecone_api_key:
        raise RuntimeError("PINECONE_API_KEY is missing")

    pc = Pinecone(api_key=settings.pinecone_api_key)

    index_names = [item["name"] for item in pc.list_indexes()]

    if settings.pinecone_index_name in index_names:

        index_info = pc.describe_index(
            settings.pinecone_index_name
        )

        current_dimension = index_info.dimension

        if current_dimension != settings.embedding_dimension:
            raise RuntimeError(
                f"Pinecone dimension mismatch! "
                f"Existing: {current_dimension}, "
                f"Required: {settings.embedding_dimension}. "
                "Use a separate index for this embedding model."
            )

    else:
        pc.create_index(
            name=settings.pinecone_index_name,
            dimension=settings.embedding_dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

        while not pc.describe_index(
            settings.pinecone_index_name
        ).status["ready"]:
            time.sleep(1)

    return pc.Index(settings.pinecone_index_name)


def get_vectorstore():
    """Initialize Pinecone vector store."""

    global _vectorstore

    if _vectorstore is None:
        index = ensure_index()

        _vectorstore = PineconeVectorStore(
            index=index,
            embedding=get_embeddings(),
            namespace=settings.pinecone_namespace
        )

    return _vectorstore


def get_retriever():
    """Return document retriever."""

    return get_vectorstore().as_retriever(
        search_kwargs={"k": settings.top_k}
    )


def add_documents(chunks):
    """Generate embeddings and store document chunks."""

    store = get_vectorstore()

    return store.add_documents(chunks)
