import requests

# Étape 1 : récupérer la dernière version
versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
# convertis en json, prends le premier élément de la liste -> c'est la dernière version
last_version = versions.json()[0]
# Étape 2 : construire l'URL des champions avec cette version
champions = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{last_version}/data/fr_FR/champion.json")
# remplace VERSION par la variable que t'as récupérée (utilise un f-string)

# Étape 3 : appeler cette URL et convertir en json
champions = champions.json()
# Étape 4 : boucler sur les champions et afficher leurs noms
# les champions sont dans la clé "data" du json
for element in champions["data"]:
    print(element)