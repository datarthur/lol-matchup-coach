import requests


versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")

last_version = versions.json()[0]

champions = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{last_version}/data/fr_FR/champion.json")

champions = champions.json()

for element in champions["data"]:
    print(element)


champion_detail = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{last_version}/data/fr_FR/champion/Darius.json")
champion_detail = champion_detail.json()

spells = champion_detail["data"]["Darius"]["spells"]
for spell in spells:
    print(spell["name"])