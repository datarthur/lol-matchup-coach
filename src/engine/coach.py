import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

def generate_matchup_advice(champion, enemy, rag_results):
    context = "\n".join(rag_results)
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": f"""Tu es un coach League of Legends expert. 
Voici des informations sur le matchup {champion} vs {enemy} :
{context}

Donne un briefing structuré pour jouer {champion} contre {enemy} :
- Résumé du matchup (1-2 lignes)
- Power spikes (niveaux clés)
- Quand engager
- Sorts à surveiller
- 3 tips concrets"""
            }
        ]
    )
    
    return message.content[0].text