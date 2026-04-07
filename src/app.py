# app.py — Point d'entrée principal de l'application « Générateur de CV IA »
# Lance la page d'accueil avec un design professionnel et un bouton CTA.

import streamlit as st
import sys
import os

# Ajoute le dossier 'src' au chemin Python pour les imports locaux
sys.path.insert(0, os.path.dirname(__file__))
from components.sidebar import render_sidebar
from document_processor import process_pdf
from services.cv_parser_service import parse_cv_text
from services.llm_service import call_llm_api
from services.voice_service import text_to_audio_bytes

# ── Configuration de la page ──
st.set_page_config(
    page_title="Générateur de CV IA",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Initialisation de l'état de session ──
st.session_state["app_init"] = True

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

# ── Barre latérale (Injecte aussi le thème global) ──
render_sidebar()

# ── Corps de la page d'accueil ──
st.markdown(f'''
<div class="hero-container">
    <h1>L'IA au service de votre carrière</h1>
    <div class="subtitle">Créez un CV percutant en quelques minutes.</div>
    <div class="description">
        Importez votre ancien CV ou laissez notre IA vous guider pas à pas pour générer un profil professionnel qui attire l'attention des recruteurs.
    </div>
</div>
''', unsafe_allow_html=True)

# Features Grid
st.markdown('''
<div class="features-grid">
    <div class="feature-card">
        <div class="icon">⚡</div>
        <h3>Rapidité</h3>
        <p>Générez un CV complet en moins de 5 minutes grâce à l'IA.</p>
    </div>
    <div class="feature-card">
        <div class="icon">🎨</div>
        <h3>Personnalisation</h3>
        <p>Choisissez parmi nos modèles premium conçus par des experts.</p>
    </div>
    <div class="feature-card">
        <div class="icon">🤖</div>
        <h3>Conseils IA</h3>
        <p>Recevez des suggestions pour améliorer votre score de recrutement.</p>
    </div>
    <div class="feature-card">
        <div class="icon">🎙️</div>
        <h3>Assistant Vocal</h3>
        <p>Interagissez naturellement avec notre coach IA intégré.</p>
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Bouton de démarrage manuel (sans emoji rocket)
    if st.button("Commencer mon CV", use_container_width=True, type="primary"):
        st.switch_page("pages/01_creer_cv.py")
    
    st.markdown("<div style='text-align:center; margin: 10px 0; opacity: 0.7;'>— OU —</div>", unsafe_allow_html=True)
    
    # Nouvel espace pour télécharger un PDF (US-04 Integration)
    uploaded_file = st.file_uploader("📥 Importer mon CV (PDF)", type="pdf", help="Analysez votre CV existant pour gagner du temps.")
    if uploaded_file:
        with st.spinner("Analyse de votre CV en cours..."):
            raw_text = process_pdf(uploaded_file)
            if raw_text:
                st.session_state["pdf_text"] = raw_text
                parsed_data = parse_cv_text(raw_text)
                if parsed_data:
                    st.session_state["cv_data"] = parsed_data
                    st.success("CV analysé avec succès !")
                    st.switch_page("pages/01_creer_cv.py")
    
    with st.expander("ℹ️ Comment ça marche ?"):
        st.write("""
        1. **Importation** : Téléchargez votre CV actuel au format PDF.
        2. **Analyse** : Notre IA extrait automatiquement vos compétences et expériences.
        3. **Optimisation** : Échangez avec le chatbot pour affiner vos descriptions.
        4. **Export** : Choisissez un modèle et téléchargez votre nouveau CV.
        """)

# Section Chat interactive (Home)
st.markdown("---")
st.subheader("💬 Parlez à votre coach carrière")
st.info("Besoin d'un conseil rapide pour votre CV ou un entretien ? Posez votre question ici.")

# Logique de Chat simplifiée pour l'accueil
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sentiment" in message:
            s = message["sentiment"]
            st.caption(f"{s['emoji']} {s.get('tone', s.get('label', ''))}")

prompt = st.chat_input("Ex: Comment décrire mon expérience de chef de projet ?")

if prompt:
    from services.llm_service import analyze_sentiment
    user_sentiment = analyze_sentiment(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt, "sentiment": user_sentiment})
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(f"{user_sentiment['emoji']} {user_sentiment['label']}")

    with st.chat_message("assistant"):
        with st.spinner("Réflexion..."):
            try:
                # Intégration du contexte du CV s'il existe
                cv_context = ""
                if "cv_data" in st.session_state and st.session_state["cv_data"]:
                    import json
                    cv_info = st.session_state["cv_data"]
                    raw_text = st.session_state.get("pdf_text", "")
                    cv_context = f"\n\nCONTEXTE DU CV DE L'UTILISATEUR :\n{json.dumps(cv_info, indent=2, ensure_ascii=False)}"
                    if raw_text:
                        cv_context += f"\n\nTEXTE BRUT DU PDF :\n{raw_text}"

                full_prompt = f"""Tu es un coach carrière expert et bienveillant. 
                Utilise le contexte du CV de l'utilisateur ci-dessous pour répondre de manière précise et personnalisée à sa question.
                C'est très important : utilise son nom, ses expériences et ses compétences réelles si elles sont présentes.
                Si le contexte est vide, réponde de façon générale.

                {cv_context}
                
                QUESTION DE L'UTILISATEUR :
                {prompt}"""
                
                response = call_llm_api(full_prompt)
                
                sentiment = analyze_sentiment(response)
                st.markdown(f"*{sentiment['emoji']} {sentiment['tone']}*")
                
                audio_bytes = text_to_audio_bytes(response)
                if audio_bytes:
                    st.audio(audio_bytes, format='audio/mp3', autoplay=True)
                
                # Streaming
                import time
                def stream_data():
                    for word in response.split(" "):
                        yield word + " "
                        time.sleep(0.04)
                st.write_stream(stream_data())
                
                st.session_state.messages.append({"role": "assistant", "content": response, "sentiment": sentiment})
            except Exception as e:
                st.error(f"Erreur : {e}")

st.markdown("---")
st.markdown('''
<div class="footer-custom">
    © 2026 Générateur de CV IA Premium • Propulsé par Google Gemini & Streamlit
</div>
''', unsafe_allow_html=True)
