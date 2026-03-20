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
# Garde : si la session est toute nouvelle (aucun PDF ni saisie), rediriger vers l'accueil
if not st.session_state.get("pdf_text") and not st.session_state.get("cv_started"):
    cv_data = st.session_state.get("cv_data", {})
    personal = cv_data.get("personal_info", {})
    has_data = any([
        personal.get("name"), personal.get("email"),
        cv_data.get("experiences"), cv_data.get("skills")
    ])
    if not has_data:
        st.switch_page("app.py")

# ── Barre latérale ──
render_sidebar()

# ── Masquer la navigation automatique Streamlit ──
st.markdown("""
<style>
    [data-testid="stSidebarNav"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Titre de la page ──
st.markdown("## 📝 Créer mon CV")
st.caption("Remplissez les sections ci-dessous. L'aperçu se met à jour en temps réel.")



# ── Layout 2 colonnes : Formulaire | Aperçu ──
col_form, col_preview = st.columns([3, 2], gap="large")

# =====================================================================
# COLONNE GAUCHE — Formulaire
# =====================================================================
with col_form:
    # Utilisation de tabs pour organiser les sections du formulaire
    tab_info, tab_exp, tab_edu, tab_skills = st.tabs([
        "👤 Infos personnelles",
        "💼 Expériences",
        "🎓 Formations",
        "🛠️ Compétences"
    ])

    # ── Onglet 1 : Informations personnelles ──
    with tab_info:
        st.markdown("#### Informations personnelles")
        personal = st.session_state["cv_data"]["personal_info"]

        personal["name"] = st.text_input(
            "Nom complet", value=personal.get("name", ""), key="input_name"
        )
        # Deux colonnes pour email et téléphone
        c1, c2 = st.columns(2)
        with c1:
            personal["email"] = st.text_input(
                "Email", value=personal.get("email", ""), key="input_email"
            )
        with c2:
            personal["phone"] = st.text_input(
                "Téléphone", value=personal.get("phone", ""), key="input_phone"
            )
        personal["address"] = st.text_input(
            "Adresse", value=personal.get("address", ""), key="input_address"
        )
        personal["linkedin"] = st.text_input(
            "LinkedIn (URL)", value=personal.get("linkedin", ""), key="input_linkedin"
        )

    # ── Onglet 2 : Expériences professionnelles (liste dynamique) ──
    with tab_exp:
        st.markdown("#### Expériences professionnelles")

        experiences = st.session_state["cv_data"]["experiences"]

        # Affichage des expériences existantes avec possibilité de supprimer
        for i, exp in enumerate(experiences):
            with st.expander(f"🔹 {exp.get('title', 'Expérience')} — {exp.get('company', '')}", expanded=False):
                exp["title"] = st.text_input(
                    "Poste", value=exp.get("title", ""), key=f"exp_title_{i}"
                )
                exp["company"] = st.text_input(
                    "Entreprise", value=exp.get("company", ""), key=f"exp_company_{i}"
                )
                c1, c2 = st.columns(2)
                with c1:
                    exp["start"] = st.text_input(
                        "Date de début", value=exp.get("start", ""), key=f"exp_start_{i}"
                    )
                with c2:
                    exp["end"] = st.text_input(
                        "Date de fin", value=exp.get("end", "Présent"), key=f"exp_end_{i}"
                    )
                exp["description"] = st.text_area(
                    "Description", value=exp.get("description", ""), key=f"exp_desc_{i}"
                )
                # Bouton de suppression
                if st.button(f"🗑️ Supprimer cette expérience", key=f"del_exp_{i}"):
                    experiences.pop(i)
                    st.rerun()

        # Bouton pour ajouter une nouvelle expérience
        if st.button("➕ Ajouter une expérience"):
            experiences.append({
                "title": "", "company": "", "start": "", "end": "Présent", "description": ""
            })
            st.rerun()

    # ── Onglet 3 : Formations (liste dynamique) ──
    with tab_edu:
        st.markdown("#### Formations")

        education = st.session_state["cv_data"]["education"]

        for i, edu in enumerate(education):
            with st.expander(f"🎓 {edu.get('degree', 'Formation')} — {edu.get('school', '')}", expanded=False):
                edu["degree"] = st.text_input(
                    "Diplôme", value=edu.get("degree", ""), key=f"edu_degree_{i}"
                )
                edu["school"] = st.text_input(
                    "Établissement", value=edu.get("school", ""), key=f"edu_school_{i}"
                )
                edu["year"] = st.text_input(
                    "Année", value=edu.get("year", ""), key=f"edu_year_{i}"
                )
                if st.button(f"🗑️ Supprimer cette formation", key=f"del_edu_{i}"):
                    education.pop(i)
                    st.rerun()

        if st.button("➕ Ajouter une formation"):
            education.append({"degree": "", "school": "", "year": ""})
            st.rerun()

    # ── Onglet 4 : Compétences ──
    with tab_skills:
        st.markdown("#### Compétences")
        st.caption("Séparez chaque compétence par une virgule (ex : Python, SQL, Gestion de projet)")

        # Convertit la liste en chaîne pour l'affichage dans le text_area
        current_skills = st.session_state["cv_data"]["skills"]
        skills_str = ", ".join(current_skills)

        new_skills_str = st.text_area(
            "Vos compétences",
            value=skills_str,
            key="input_skills",
            height=120,
        )

        # Met à jour la liste de compétences à partir de la saisie
        st.session_state["cv_data"]["skills"] = [
            s.strip() for s in new_skills_str.split(",") if s.strip()
        ]

# =====================================================================
# COLONNE DROITE — Aperçu en temps réel
# =====================================================================
with col_preview:
    st.markdown("#### 👁️ Aperçu")
    render_preview()
