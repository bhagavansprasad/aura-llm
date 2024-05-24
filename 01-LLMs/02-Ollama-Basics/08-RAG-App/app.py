# # from llama_index.llms import Ollama
# from llama_index.llms.ollama import Ollama

# # from llama_index import VectorStoreIndex, ServiceContext, download_loader
# from llama_index.core import VectorStoreIndex, ServiceContext, download_loader

# # from llama_index.storage.storage_context import StorageContext
# from llama_index.core.storage.storage_context import StorageContext

##############

# from llama_index.llms import Ollama
from llama_index.llms.ollama import Ollama

from pathlib import Path
import qdrant_client

# from llama_index import VectorStoreIndex, ServiceContext, download_loader
from llama_index.core import VectorStoreIndex, ServiceContext, download_loader
# import llama_hub.file
# print(dir(llama_hub.file))
# import llama_hub.file.json
# from llama_hub.file.json import JSONReader



# from llama_index.storage.storage_context import StorageContext
from llama_index.core.storage.storage_context import StorageContext

from llama_index.vector_stores.qdrant import QdrantVectorStore


# Load JSON
JSONReader = download_loader("JSONReader")
loader = JSONReader()
documents =  loader.load_data(Path('tinytweets.json'))
# print(type(documents))
# print(documents)

# Create Qdrant client and store
client = qdrant_client.QdrantClient(path="./qdrant_data")
vector_store = QdrantVectorStore(client=client, collection_name="tweets")
storage_context = StorageContext.from_defaults(vector_store=vector_store)


llm = Ollama(model="mistral")
# service_context = ServiceContext.from_defaults(llm=llm)
service_context = ServiceContext.from_defaults(llm=llm, embed_model="local")

index = VectorStoreIndex.from_documents(documents, service_context=service_context, storage_context=storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("What does the author think about Start Treak? In one line")
print(response)



