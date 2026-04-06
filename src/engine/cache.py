import json
import os

CACHE_DIR = "cache"

def get_cached_matchup(champion, enemy):
    path = f"{CACHE_DIR}/{champion.lower()}_vs_{enemy.lower()}.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

def save_to_cache(champion, enemy, advice):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = f"{CACHE_DIR}/{champion.lower()}_vs_{enemy.lower()}.json"
    with open(path, "w") as f:
        json.dump({"champion": champion, "enemy": enemy, "advice": advice}, f)