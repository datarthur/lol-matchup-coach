import streamlit as st
import requests
from src.data.champions import get_champions
from src.rag.knowledge_base import create_knowledge_base
from src.engine.coach import generate_matchup_advice
from src.engine.cache import get_cached_matchup, save_to_cache

st.title("LoL Matchup Coach")

# charger les champions
champions = get_champions()
champion_list = sorted(champions.keys())

# version pour les images
versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
version = versions[0]

# deux dropdowns
col1, col2 = st.columns(2)
with col1:
    my_champ = st.selectbox("Ton champion", champion_list)
with col2:
    enemy_champ = st.selectbox("Champion ennemi", champion_list)

# bouton
if st.button("Générer le briefing"):
    if my_champ == enemy_champ:
        st.warning("Choisis deux champions différents")
    else:
        # afficher les icônes
        col_img1, col_vs, col_img2 = st.columns([1, 0.5, 1])
        with col_img1:
            st.image(f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{my_champ}.png", width=100)
            st.caption(my_champ)
        with col_vs:
            st.markdown("<h2 style='text-align: center; padding-top: 25px;'>VS</h2>", unsafe_allow_html=True)
        with col_img2:
            st.image(f"https://ddragon.leagueoflegends.com/cdn/{version}/img/champion/{enemy_champ}.png", width=100)
            st.caption(enemy_champ)

        # vérifier le cache
        cached = get_cached_matchup(my_champ, enemy_champ)
        if cached:
            st.success("Depuis le cache - instantané")
            st.markdown(cached["advice"])
        else:
            with st.spinner("Génération en cours..."):
                collection = create_knowledge_base()
                results = collection.query(
                    query_texts=[f"{my_champ} vs {enemy_champ}"],
                    n_results=2
                )
                rag_results = results["documents"][0]
                advice = generate_matchup_advice(my_champ, enemy_champ, rag_results)
                save_to_cache(my_champ, enemy_champ, advice)
                st.markdown(advice)