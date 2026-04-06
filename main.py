from src.rag.knowledge_base import create_knowledge_base
from src.engine.coach import generate_matchup_advice
from src.engine.cache import get_cached_matchup, save_to_cache

champion = "Darius"
enemy = "Mordekaiser"

# vérifier le cache d'abord
cached = get_cached_matchup(champion, enemy)
if cached:
    print("(depuis le cache)")
    print(cached["advice"])
else:
    # pas en cache, on génère
    collection = create_knowledge_base()
    results = collection.query(query_texts=[f"{champion} vs {enemy}"], n_results=2)
    rag_results = results["documents"][0]
    
    advice = generate_matchup_advice(champion, enemy, rag_results)
    save_to_cache(champion, enemy, advice)
    print(advice)