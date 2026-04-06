from src.rag.knowledge_base import create_knowledge_base
from src.engine.coach import generate_matchup_advice

# créer la base de connaissances
collection = create_knowledge_base()

# chercher dans le RAG
results = collection.query(query_texts=["Darius vs Mordekaiser"], n_results=2)
rag_results = results["documents"][0]

# générer le briefing avec le LLM
advice = generate_matchup_advice("Darius", "Mordekaiser", rag_results)
print(advice)