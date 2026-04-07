# 🎮 LoL Matchup Coach

> Coaching tactique pour League of Legends, généré par IA. Choisis ton matchup, reçois un briefing structuré : power spikes, sorts à surveiller, quand engager, tips concrets.

🚀 **[Tester l'app en ligne](https://lol-matchup-coach.streamlit.app)**

---

## 📖 Description

**LoL Matchup Coach** est une application web qui génère des briefings tactiques personnalisés pour chaque matchup de League of Legends. L'utilisateur sélectionne son champion et celui de l'adversaire, et l'app produit un guide structuré combinant données statistiques, base de connaissances et synthèse par LLM.

Le projet illustre une architecture **RAG (Retrieval-Augmented Generation)** appliquée à un cas d'usage gaming : récupération de données depuis l'API Riot, recherche sémantique dans une base de connaissances vectorisée, et génération contextuelle via un LLM.

---

## ✨ Fonctionnalités

- 🎯 **Briefings tactiques personnalisés** par matchup (résumé, power spikes, timings, tips, items)
- ⚡ **Système de cache** pour servir les matchups déjà générés instantanément
- 🖼️ **Interface visuelle** avec icônes des champions
- 🔄 **Données toujours à jour** via Data Dragon (champions, sorts, patches automatiques)
- 🧠 **RAG sémantique** pour enrichir les briefings avec du contexte qualitatif

---

## 🛠️ Stack technique

| Couche | Outil |
|---|---|
| **Langage** | Python 3.13 |
| **Données** | Riot API (Data Dragon) |
| **Vector DB** | ChromaDB |
| **Embeddings** | sentence-transformers (HuggingFace, `all-MiniLM-L6-v2`) |
| **LLM** | Claude Sonnet (Anthropic API) |
| **Interface** | Streamlit |
| **Cache** | JSON local |
| **Déploiement** | Streamlit Cloud |
| **Versionning** | Git + GitHub |

---

## 🏗️ Architecture

```
Utilisateur
    │
    ▼
┌─────────────────┐
│   Streamlit UI  │ ◄── Sélection du matchup
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Cache (JSON)   │ ── Si matchup déjà généré → retour instantané
└────────┬────────┘
         │ (cache miss)
         ▼
┌─────────────────┐     ┌──────────────────┐
│  Data Dragon    │     │   ChromaDB RAG   │
│  (Riot API)     │     │   (embeddings)   │
└────────┬────────┘     └────────┬─────────┘
         │                       │
         └───────────┬───────────┘
                     ▼
            ┌─────────────────┐
            │  Claude Sonnet  │  ◄── Synthèse contextuelle
            │  (Anthropic)    │
            └────────┬────────┘
                     │
                     ▼
              Briefing structuré
                     │
                     ▼
              Sauvegarde cache
```

---

## 🚀 Installation locale

### Prérequis

- Python 3.13+
- Une clé API Anthropic (récupérable sur [console.anthropic.com](https://console.anthropic.com))

### Étapes

```bash
# Cloner le repo
git clone https://github.com/datarthur/lol-matchup-coach.git
cd lol-matchup-coach

# Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer la clé API
echo "ANTHROPIC_API_KEY=ta_clé_ici" > .env

# Lancer l'app
streamlit run app.py
```

L'app sera accessible sur `http://localhost:8501`.

---

## 📁 Structure du projet

```
lol-matchup-coach/
├── app.py                    # Interface Streamlit
├── main.py                   # Script de test en ligne de commande
├── requirements.txt          # Dépendances Python
├── .env                      # Variables d'environnement (non versionné)
├── .gitignore
├── cache/                    # Briefings générés (cache JSON)
└── src/
    ├── data/
    │   └── champions.py      # Récupération données Riot Data Dragon
    ├── rag/
    │   └── knowledge_base.py # Initialisation de la base ChromaDB
    └── engine/
        ├── coach.py          # Génération des briefings via Claude
        └── cache.py          # Système de cache
```

---

## 🧠 Comment ça fonctionne

1. **Récupération des données** — Au démarrage, l'app interroge Data Dragon (API publique de Riot) pour récupérer la liste des champions et leurs sorts du patch en cours.

2. **Recherche RAG** — Quand un matchup est demandé, ChromaDB cherche dans sa base de connaissances vectorisée les fragments textuels les plus pertinents (similarité sémantique via embeddings).

3. **Génération LLM** — Les fragments récupérés + les noms des champions sont envoyés à Claude Sonnet via un prompt structuré. Le modèle synthétise un briefing tactique personnalisé.

4. **Cache** — Le résultat est sauvegardé dans un fichier JSON. Les requêtes suivantes pour le même matchup sont servies instantanément, sans nouvel appel API.

---

## ⚠️ Limitations connues

- **Wukong** apparaît sous le nom interne `MonkeyKing` dans le sélecteur. C'est le nom utilisé par l'API Riot historiquement. Un mapping pourra être ajouté dans une version future.
- **Coût des appels LLM** — Chaque génération de briefing consomme des crédits API Anthropic. Le système de cache limite ce coût en évitant de régénérer les matchups déjà demandés.
- **Base RAG initiale réduite** — La base de connaissances qualitative est en cours d'enrichissement. Pour les matchups peu documentés, l'app s'appuie principalement sur les connaissances pré-entraînées du LLM.

---

## 🗺️ Améliorations prévues

- [ ] Pré-génération en batch des matchups via Ollama (Llama 3 local) pour réduire les coûts
- [ ] Sélecteur de rôle (top, mid, jungle, bot, support)
- [ ] Enrichissement de la base RAG avec des guides scrapés
- [ ] Affichage des stats de matchup (win rate, gold diff)
- [ ] Mapping des noms internes Riot (MonkeyKing → Wukong, etc.)
- [ ] Mode "live" avec récupération automatique du matchup en cours

---

## 📄 Licence

Ce projet est un projet personnel à but pédagogique. League of Legends est une marque déposée de Riot Games, Inc. Ce projet n'est pas affilié à Riot Games.