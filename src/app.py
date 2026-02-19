# app.py — Point d'entrée principal de l'application « Générateur de CV IA »
# Lance la page d'accueil avec un design professionnel et un bouton CTA.

import streamlit as st
import sys
import os

# Ajoute le dossier 'src' au chemin Python pour les imports locaux
sys.path.insert(0, os.path.dirname(__file__))
from components.sidebar import render_sidebar

# ── Configuration de la page ──
st.set_page_config(
    page_title="Générateur de CV IA",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Initialisation de l'état de session ──
st.session_state.setdefault("cv_data", {
    "personal_info": {
        "name": "", "email": "", "phone": "",
        "address": "", "linkedin": ""
    },
    "experiences": [],
    "education": [],
    "skills": []
})
st.session_state.setdefault("api_key", "")

# ── Injection de CSS personnalisé ──
st.markdown("""
<style>
    /* ── Typographie et fond ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero Section ── */
    .hero-container {
        text-align: center;
        padding: 4rem 2rem 2rem 2rem;
    }

    .hero-container h1 {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }

    .hero-container .subtitle {
        font-size: 1.3rem;
        color: #555;
        margin-bottom: 1rem;
    }

    .hero-container .description {
        font-size: 1rem;
        color: #777;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }

    /* ── Feature Cards ── */
    .features-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        max-width: 900px;
        margin: 2rem auto;
        padding: 0 1rem;
    }

    .feature-card {
        background: linear-gradient(145deg, #f8f9ff 0%, #f0f2ff 100%);
        border: 1px solid #e2e6ff;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.15);
    }

    .feature-card .icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .feature-card h3 {
        font-size: 1rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.3rem;
    }

    .feature-card p {
        font-size: 0.85rem;
        color: #777;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# ── Barre latérale ──
render_sidebar()

# ── Hero Section ──
st.markdown("""
<div class="hero-container">
    <h1>📄 Générateur de CV IA</h1>
    <p class="subtitle">Créez un CV professionnel, optimisé et prêt à l'emploi.</p>
    <p class="description">
        Notre outil intelligent vous guide pas à pas dans la création de votre curriculum vitae.
        Saisissez vos informations, laissez l'IA optimiser vos contenus
        et exportez un CV percutant compatible avec les systèmes ATS.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Bouton CTA centré ──
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Créer mon CV", use_container_width=True, type="primary"):
        st.switch_page("pages/01_creer_cv.py")

# ── Fonctionnalités clés ──
st.markdown("""
<div class="features-grid">
    <div class="feature-card">
        <div class="icon">✏️</div>
        <h3>Saisie Guidée</h3>
        <p>Formulaire structuré pour ne rien oublier</p>
    </div>
    <div class="feature-card">
        <div class="icon">🤖</div>
        <h3>IA Assistante</h3>
        <p>Optimisation automatique de vos descriptions</p>
    </div>
    <div class="feature-card">
        <div class="icon">🌍</div>
        <h3>Multilingue</h3>
        <p>Traduction et adaptation internationale</p>
    </div>
    <div class="feature-card">
        <div class="icon">📊</div>
        <h3>Optimisé ATS</h3>
        <p>Compatible avec les systèmes de recrutement</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Pied de page ──
st.markdown("---")
st.caption("💡 Propulsé par l'IA Gemini · Sprint 1 — Échafaudage")
