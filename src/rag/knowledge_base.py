import chromadb
from chromadb.utils import embedding_functions

def create_knowledge_base():
    client = chromadb.Client()
    
    # utiliser sentence-transformers pour les embeddings
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )
    
    collection = client.create_collection(
        name="matchups",
        embedding_function=ef
    )
    
    collection.add(
        documents=["wukong gagne niv 1 contre darius avec ignite", "darius vulnérable quand il a plus son e"],
        ids=["id1", "id2"]
    )
    
    return collection