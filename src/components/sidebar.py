# sidebar.py — Barre latérale de l'application
# Fournit la navigation entre les pages et le champ de saisie de la clé API Gemini.

import streamlit as st
import sys
import os

# Ajoute le dossier 'src' au chemin Python pour permettre les imports locaux
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import get_api_key


def render_sidebar():
    """
    Affiche la barre latérale contenant :
    - Le titre de l'application
    - Les liens de navigation vers les différentes pages
    - Le champ de saisie sécurisé pour la clé API Gemini
    """
    with st.sidebar:
        # ── Titre de l'application ──
        st.title("📄 CV IA")
        st.markdown("---")

        # ── Navigation ──
        st.page_link("app.py", label="🏠 Accueil")
        st.page_link("pages/01_creer_cv.py", label="📝 Créer mon CV")
        st.markdown("---")

        # ── Configuration API ──
        st.subheader("⚙️ Configuration")

        # Récupère la clé API depuis .env ou session_state comme valeur par défaut
        default_key = st.session_state.get("api_key", get_api_key())

        api_key = st.text_input(
            "🔑 Clé API Gemini",
            type="password",
            value=default_key,
            help="Entrez votre clé API Gemini pour activer les fonctionnalités IA."
        )

        # Sauvegarde la clé dans la session pour une utilisation ultérieure
        if api_key:
            st.session_state["api_key"] = api_key
            st.success("Clé API enregistrée ✅", icon="🔑")
        else:
            st.info("Ajoutez votre clé API pour activer l'IA.", icon="ℹ️")
