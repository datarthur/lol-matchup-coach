from src.data.champions import get_champions, get_champion_detail

champions = get_champions()
for champ in champions:
    print(champ)

spells = get_champion_detail("Darius")
for spell in spells:
    print(spell["name"])