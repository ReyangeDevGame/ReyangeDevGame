import streamlit as st
import os
import sys

# Ajout du dossier 'src' pour les imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from components.sidebar import render_sidebar

st.set_page_config(
    page_title="Modèles de CV",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation
if "selected_template" not in st.session_state:
    st.session_state["selected_template"] = "Template 1"

# Sidebar
render_sidebar()

# --- Interface globale ---
st.title("🎨 Choisissez votre modèle de CV")
st.markdown("Faites défiler et sélectionnez le design qui mettra le mieux en valeur votre profil.")
st.markdown("---")

if st.button("🔙 Retour à l'éditeur", type="primary"):
    st.switch_page("pages/01_creer_cv.py")
    
st.markdown("<br>", unsafe_allow_html=True)

# Définition des templates
templates = [
    {
        "id": "Template 1", 
        "name": "Moderne (Jaune & Noir)", 
        "desc": "Le modèle par défaut, dynamique et percutant avec ses formes géométriques audacieuses et biseautées.",
        "colors": ["#facc15", "#111111", "#f3f4f6"]
    },
    {
        "id": "Template 2", 
        "name": "Corporate Bleu", 
        "desc": "Un design classique et sérieux avec un large bandeau bleu marine en en-tête. Parfait pour les profils plus institutionnels.",
        "colors": ["#1e3a8a", "#ffffff", "#e5e7eb"]
    },
    {
        "id": "Template 3", 
        "name": "Minimaliste Épuré", 
        "desc": "Aller à l'essentiel avec énormément d'espace blanc, une sépration fine des colonnes, et une typographie sobre.",
        "colors": ["#ffffff", "#333333", "#fafafa"]
    },
    {
        "id": "Template 4", 
        "name": "Créatif Dégradé", 
        "desc": "Idéal pour les milieux artistiques ou tech. Une barre latérale à dégradé vibrant et un agencement audacieux des compétences.",
        "colors": ["#8b5cf6", "#f97316", "#111827"]
    },
    {
        "id": "Template 5", 
        "name": "Premium Sombre", 
        "desc": "Très élégant, se base sur un fond noir bleuté mat et des polices claires luxueuses avec des accents dorés.",
        "colors": ["#111827", "#ca8a04", "#1f2937"]
    }
]

# Affichage des cartes (Grille 3 colonnes)
row1 = st.columns(3)
for i in range(3):
    with row1[i]:
        st.markdown(f"### {templates[i]['name']}")
        
        # Aperçu mock (barres de couleurs pour illustrer l'ambiance)
        c0, c1, c2 = templates[i]['colors']
        st.markdown(
            f'''
            <div style="width: 100%; height: 10px; display: flex; border-radius: 4px; overflow: hidden; margin-bottom: 15px;">
                <div style="flex: 1; background-color: {c0};"></div>
                <div style="flex: 1; background-color: {c1};"></div>
                <div style="flex: 1; background-color: {c2};"></div>
            </div>
            ''', unsafe_allow_html=True
        )
        
        st.caption(templates[i]['desc'])
        if st.session_state["selected_template"] == templates[i]['id']:
            st.success("✓ Modèle actuel")
        else:
            if st.button("Choisir ce design", key=f"btn_{i}", use_container_width=True):
                st.session_state["selected_template"] = templates[i]['id']
                st.switch_page("pages/01_creer_cv.py")

st.markdown("<br>", unsafe_allow_html=True)
row2 = st.columns(3)
for i in range(3, 5):
    with row2[i-3]:
        st.markdown(f"### {templates[i]['name']}")
        
        # Aperçu mock
        c0, c1, c2 = templates[i]['colors']
        st.markdown(
            f'''
            <div style="width: 100%; height: 10px; display: flex; border-radius: 4px; overflow: hidden; margin-bottom: 15px;">
                <div style="flex: 1; background-color: {c0};"></div>
                <div style="flex: 1; background-color: {c1};"></div>
                <div style="flex: 1; background-color: {c2};"></div>
            </div>
            ''', unsafe_allow_html=True
        )
        
        st.caption(templates[i]['desc'])
        if st.session_state["selected_template"] == templates[i]['id']:
            st.success("✓ Modèle actuel")
        else:
            if st.button("Choisir ce design", key=f"btn_{i}", use_container_width=True):
                st.session_state["selected_template"] = templates[i]['id']
                st.switch_page("pages/01_creer_cv.py")
