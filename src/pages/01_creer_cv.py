# 01_creer_cv.py — Page « Créer mon CV »
# Formulaire multi-sections avec aperçu en temps réel.
# Les données sont persistées dans st.session_state["cv_data"].

import streamlit as st
import sys
import os

# Ajoute le dossier 'src' au chemin Python pour les imports locaux
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from components.sidebar import render_sidebar
from components.cv_preview import render_preview
from services.pdf_service import extract_text_from_pdf
from services.cv_parser_service import parse_cv_text

# ── Configuration de la page ──
st.set_page_config(
    page_title="Créer mon CV — CV IA",
    page_icon="📝",
    layout="wide",
)

# ── Initialisation de l'état de session ──
# Structure de données centralisée pour tout le CV
st.session_state.setdefault("cv_data", {
    "personal_info": {
        "name": "", "email": "", "phone": "",
        "address": "", "linkedin": ""
    },
    "experiences": [],    # Liste de dict {title, company, start, end, description}
    "education": [],      # Liste de dict {degree, school, year}
    "skills": []          # Liste de strings
})
st.session_state.setdefault("api_key", "")
# Garde : Si la session commence directement sur cette page (nouvel onglet, etc.), forcer l'accueil.
if "app_init" not in st.session_state:
    st.switch_page("app.py")

# ── Barre latérale ──
render_sidebar()

# ── CSS Dynamique ──
# (Injecté automatiquement via render_sidebar() globalement dans chaque page)

# ── Titre de la page ──
st.markdown("## 📝 Créer mon CV")
st.caption("Remplissez les sections ci-dessous. L'aperçu se met à jour en temps réel.")




# ── Layout Vertical ──
# Le formulaire occupe toute la largeur
tab_info, tab_exp, tab_edu, tab_skills = st.tabs([
    "👤 Infos personnelles",
    "💼 Expériences",
    "🎓 Formations",
    "🛠️ Compétences"
])

# ── Onglets du formulaire ──
with tab_info:
    st.markdown("#### Informations personnelles")
    personal = st.session_state["cv_data"]["personal_info"]
    personal["name"] = st.text_input("Nom complet", value=personal.get("name", ""))
    c1, c2 = st.columns(2)
    with c1:
        personal["email"] = st.text_input("Email", value=personal.get("email", ""))
    with c2:
        personal["phone"] = st.text_input("Téléphone", value=personal.get("phone", ""))
    personal["address"] = st.text_input("Adresse", value=personal.get("address", ""))
    personal["linkedin"] = st.text_input("LinkedIn (URL)", value=personal.get("linkedin", ""))

with tab_exp:
    st.markdown("#### Expériences professionnelles")
    experiences = st.session_state["cv_data"]["experiences"]
    for i, exp in enumerate(experiences):
        with st.expander(f"🔹 {exp.get('title', 'Expérience')} — {exp.get('company', '')}", expanded=False):
            if f"exp_title_{i}" not in st.session_state: st.session_state[f"exp_title_{i}"] = exp.get("title", "")
            if f"exp_company_{i}" not in st.session_state: st.session_state[f"exp_company_{i}"] = exp.get("company", "")
            if f"exp_start_{i}" not in st.session_state: st.session_state[f"exp_start_{i}"] = exp.get("start", "")
            if f"exp_end_{i}" not in st.session_state: st.session_state[f"exp_end_{i}"] = exp.get("end", "Présent")
            if f"exp_desc_{i}" not in st.session_state: st.session_state[f"exp_desc_{i}"] = exp.get("description", "")
            exp["title"] = st.text_input("Poste", key=f"exp_title_{i}")
            exp["company"] = st.text_input("Entreprise", key=f"exp_company_{i}")
            c1, c2 = st.columns(2)
            with c1: exp["start"] = st.text_input("Date de début", key=f"exp_start_{i}")
            with c2: exp["end"] = st.text_input("Date de fin", key=f"exp_end_{i}")
            exp["description"] = st.text_area("Description", key=f"exp_desc_{i}")
            if st.button(f"🗑️ Supprimer cette expérience", key=f"del_exp_{i}"):
                experiences.pop(i)
                for k in list(st.session_state.keys()):
                    if k.startswith(("exp_", "del_exp_")): del st.session_state[k]
                st.rerun()
    if st.button("➕ Ajouter une expérience"):
        experiences.append({"title": "", "company": "", "start": "", "end": "Présent", "description": ""})
        st.rerun()

with tab_edu:
    st.markdown("#### Formations")
    education = st.session_state["cv_data"]["education"]
    for i, edu in enumerate(education):
        with st.expander(f"🎓 {edu.get('degree', 'Formation')} — {edu.get('school', '')}", expanded=False):
            if f"edu_degree_{i}" not in st.session_state: st.session_state[f"edu_degree_{i}"] = edu.get("degree", "")
            if f"edu_school_{i}" not in st.session_state: st.session_state[f"edu_school_{i}"] = edu.get("school", "")
            if f"edu_year_{i}" not in st.session_state: st.session_state[f"edu_year_{i}"] = edu.get("year", "")
            edu["degree"] = st.text_input("Diplôme", key=f"edu_degree_{i}")
            edu["school"] = st.text_input("Établissement", key=f"edu_school_{i}")
            edu["year"] = st.text_input("Année", key=f"edu_year_{i}")
            if st.button(f"🗑️ Supprimer cette formation", key=f"del_edu_{i}"):
                education.pop(i)
                for k in list(st.session_state.keys()):
                    if k.startswith(("edu_", "del_edu_")): del st.session_state[k]
                st.rerun()
    if st.button("➕ Ajouter une formation"):
        education.append({"degree": "", "school": "", "year": ""})
        st.rerun()

with tab_skills:
    st.markdown("#### Compétences")
    current_skills = st.session_state["cv_data"]["skills"]
    skills_str = ", ".join(current_skills)
    new_skills_str = st.text_area("Vos compétences", value=skills_str, height=120)
    st.session_state["cv_data"]["skills"] = [s.strip() for s in new_skills_str.split(",") if s.strip()]

# ── Section APERÇU (En dessous) ──
st.markdown("---")
col_title, col_btn = st.columns([3, 1])
with col_title:
    st.markdown("### 👁️ Aperçu de votre CV")
with col_btn:
    if st.button("🎨 Changer de modèle", use_container_width=True):
        st.switch_page("pages/02_templates.py")

render_preview()
