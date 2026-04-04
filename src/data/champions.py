import requests
def get_champions():
    versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")

    last_version = versions.json()[0]

    champions = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{last_version}/data/fr_FR/champion.json")

    champions = champions.json()

    return champions["data"]

def get_champion_detail(name):

    versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")

    last_version = versions.json()[0]

    champion_detail = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{last_version}/data/fr_FR/champion/{name}.json")

    champion_detail = champion_detail.json()

    spells = champion_detail["data"][name]["spells"]
    
    return spells