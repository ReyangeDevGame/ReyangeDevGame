# sidebar.py — Barre latérale de l'application
# Fournit la navigation entre les pages et le chat IA conseiller CV.

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
    - Le chat IA conseiller (si un PDF a été importé)
    """
    with st.sidebar:
        # ── Titre de l'application ──
        st.title("📄 CV IA")
        st.markdown("---")

        # ── Navigation ──
        st.page_link("app.py", label="🏠 Accueil")
        st.page_link("pages/01_creer_cv.py", label="📝 Créer mon CV")
        st.markdown("---")

        # ── Chat IA Conseiller ──
        if st.session_state.get("pdf_text"):
            st.subheader("💬 Conseiller IA")
            st.caption("Posez-moi des questions sur votre CV.")

            # Initialisation de l'historique
            if "messages" not in st.session_state:
                st.session_state["messages"] = []

            # Affichage des messages avec hauteur limitée
            chat_container = st.container(height=300)
            with chat_container:
                for msg in st.session_state["messages"]:
                    with st.chat_message(msg["role"]):
                        st.markdown(msg["content"])

            # Zone de saisie
            user_input = st.chat_input("Votre question...", key="sidebar_chat_input")
            if user_input:
                # Ajout message utilisateur
                st.session_state["messages"].append({"role": "user", "content": user_input})

                # Appel à l'IA
                try:
                    from services.llm_service import call_llm_api
                    prompt = f"""
Tu es un conseiller de carrière expert et bienveillant.
Utilise les informations du CV suivant pour répondre à l'utilisateur de manière précise et professionnelle.
Si la question est hors-sujet (non liée au CV ou à la carrière), refuse poliment.

CV :
---
{st.session_state['pdf_text']}
---

Question : {user_input}
"""
                    with st.spinner("Réflexion..."):
                        response = call_llm_api(prompt)
                    st.session_state["messages"].append({"role": "assistant", "content": response})
                    st.rerun()
                except Exception as e:
                    st.error(f"Erreur IA : {e}")

            # Bouton pour vider l'historique
            if st.session_state.get("messages"):
                if st.button("🗑️ Effacer la conversation", use_container_width=True):
                    st.session_state["messages"] = []
                    st.rerun()
        else:
            pass
