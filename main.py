from src.rag.knowledge_base import create_knowledge_base

collection = create_knowledge_base()
print("Documents ajoutés:", collection.count())

# teste la recherche
results = collection.query(query_texts=["comment battre darius"], n_results=2)
print(results["documents"])