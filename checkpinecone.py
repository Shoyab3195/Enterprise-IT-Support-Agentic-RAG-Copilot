
from pinecone import Pinecone
from app.core.config import get_settings

settings = get_settings()

pc = Pinecone(api_key=settings.pinecone_api_key)

index_name = settings.pinecone_index_name
index_info = pc.describe_index(index_name)

print("Index name:", index_name)
print("Dimension:", index_info.dimension)
print("Cloud:", index_info.spec.serverless.cloud)
print("Region:", index_info.spec.serverless.region)
print("Host:", index_info.host)
