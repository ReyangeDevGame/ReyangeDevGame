# sidebar.py — Barre latérale de l'application
# Fournit la navigation entre les pages et le chat IA conseiller CV.

import streamlit as st
import sys
import os

# Ajoute le dossier 'src' au chemin Python pour permettre les imports locaux
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import get_api_key
from utils.theme_injector import apply_app_theme
import re


def clean_session_data():
    """
    Nettoie récursivement les données du CV pour supprimer les ligatures d'icônes indésirables.
    """
    if "cv_data" not in st.session_state:
        return

    ligatures = [
        "keyboard_double_arrow_right", "keyboard_arrow_right", "arrow_right",
        "chevron_right", "arrow_forward", "arrow_right_alt", "done", "check", 
        "check_circle", "email", "phone", "location_on", "work", "school",
        "info", "file_change", "person", "contact_mail", "credit_card",
        "description", "star", "language"
    ]
    
    def _clean(text):
        if not isinstance(text, str): return text
        for lit in ligatures:
            # On utilise une regex pour supprimer le mot clé isolé ou entouré de tirets bas
            text = re.sub(rf'[_]*\b{lit}\b[_]*', '', text, flags=re.IGNORECASE)
        # On nettoie les espaces en trop et les underscores résiduels
        return re.sub(r'\s+', ' ', text).replace("__", " ").strip()

    # Nettoyage des infos personnelles
    for k, v in st.session_state["cv_data"].get("personal_info", {}).items():
        st.session_state["cv_data"]["personal_info"][k] = _clean(v)

    # Nettoyage des expériences
    for exp in st.session_state["cv_data"].get("experiences", []):
        for k, v in exp.items():
            exp[k] = _clean(v)

    # Nettoyage de l'éducation
    for edu in st.session_state["cv_data"].get("education", []):
        for k, v in edu.items():
            edu[k] = _clean(v)

    # Nettoyage des compétences
    st.session_state["cv_data"]["skills"] = [_clean(s) for s in st.session_state["cv_data"].get("skills", [])]


def render_sidebar():
    """
    Affiche la barre latérale contenant :
    - Le titre de l'application
    - Les liens de navigation vers les différentes pages
    - Le chat IA conseiller (si un PDF a été importé)
    """
    # Nettoyage des données (sécurité contre les ghost strings d'icônes)
    clean_session_data()
    
    # Application du thème global
    apply_app_theme()
    
    with st.sidebar:
        # ── Titre de l'application ──
        st.title("📄 CV IA")
        st.markdown("---")

        # ── Navigation ──
        st.page_link("app.py", label="🏠 Accueil")
        st.page_link("pages/01_creer_cv.py", label="📝 Créer mon CV")
        st.page_link("pages/02_templates.py", label="🎨 Modèles CV")
        st.markdown("---")
        
        # ── Thème de l'Application ──
        st.subheader("🎨 Apparence")
        theme_options = ["🌍 Minimal", "💻 Hacker", "💖 Love", "⚔️ Anime"]
        
        # Initialisation de l'état
        if "app_theme" not in st.session_state:
            st.session_state["app_theme"] = "🌍 Minimal"
            
        selected_theme = st.selectbox(
            "Thème de l'app",
            options=theme_options,
            index=theme_options.index(st.session_state["app_theme"]),
            key="theme_selector"
        )
        
        if selected_theme != st.session_state["app_theme"]:
            st.session_state["app_theme"] = selected_theme
            st.rerun()
        st.markdown("---")
