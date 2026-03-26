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

# ── Injection de CSS personnalisé ──
st.markdown("""
<style>
    /* ── Masquer la navigation automatique de Streamlit (app / creer cv) ── */
    [data-testid="stSidebarNav"] {
        display: none;
    }

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

    /* ── Masquer les lecteurs audio (IA invisible) ── */
    div[data-testid="stAudio"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Barre latérale ──
render_sidebar()

# ── Hero Section ──
st.markdown("""
<div class="hero-container">
    <h1>📄 Générateur de CV IA</h1>
    <p class="subtitle">Créez ou importez votre CV en un clic.</p>
</div>
""", unsafe_allow_html=True)

# ── Bouton CTA centré ──
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Créer mon CV de zéro", use_container_width=True, type="primary"):
        st.switch_page("pages/01_creer_cv.py")
        
    st.markdown("<div style='text-align: center; margin: 15px 0;'><strong>— OU —</strong></div>", unsafe_allow_html=True)
    
    uploaded_pdf = st.file_uploader("📥 Importer un CV existant (PDF)", type=["pdf"], key="home_upload")
    if uploaded_pdf:
        with st.spinner("Analyse du CV en cours..."):
            try:
                text = process_pdf(uploaded_pdf)
                # Utilisation du moteur Regex local (non-IA) pour l'import
                parsed_data = parse_cv_text(text)
                
                # Mise à jour du state
                for key in ["name", "email", "phone", "address", "linkedin"]:
                    val = parsed_data.get("personal_info", {}).get(key)
                    if val:
                        st.session_state["cv_data"]["personal_info"][key] = val
                        st.session_state[f"input_{key}"] = val
                        
                if parsed_data.get("experiences"):
                    for k in list(st.session_state.keys()):
                        if k.startswith(("exp_", "del_exp_")):
                            del st.session_state[k]
                    st.session_state["cv_data"]["experiences"] = parsed_data["experiences"]
                    
                if parsed_data.get("education"):
                    for k in list(st.session_state.keys()):
                        if k.startswith(("edu_", "del_edu_")):
                            del st.session_state[k]
                    st.session_state["cv_data"]["education"] = parsed_data["education"]
                    
                if parsed_data.get("skills"):
                    st.session_state["cv_data"]["skills"] = parsed_data["skills"]
                    st.session_state["input_skills"] = ", ".join(parsed_data["skills"])
                
                # Sauvegarde du texte brut pour le Chatbot
                st.session_state["pdf_text"] = text
                    
                st.success("✅ CV analysé avec succès !")
                st.rerun()
            except Exception as e:
                st.error(f"Erreur lors de l'analyse : {e}")

# ── Zone Chatbot IA (Sprints 3 & 4) ──
# Toujours visible pour permettre le chat même en création de zéro
st.markdown("---")
st.subheader("💬 Votre Conseiller IA Vocal")
st.info("Posez vos questions par écrit ou par la voix ! 🎙️")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio" in message and message["audio"]:
            st.audio(message["audio"], format='audio/mp3')

# Saisie Vocale (STT)
audio_input = st.audio_input("Parlez à votre conseiller")

# Saisie Textuelle
text_input = st.chat_input("Ou tapez votre question ici...")

# Traitement de l'entrée (voix prioritaire si nouvelle)
prompt = None
if audio_input:
    # Pour simplifier et rester efficace, on délègue la transcription à Gemini
    prompt = "Transcris et réponds à cet audio"
    
if text_input:
    prompt = text_input

if prompt:
    user_msg = {"role": "user", "content": prompt}
    if audio_input and not text_input:
        user_msg["content"] = "🎤 [Message Vocal]"
        
    st.session_state.messages.append(user_msg)
    with st.chat_message("user"):
        st.markdown(user_msg["content"])

    with st.chat_message("assistant"):
        with st.spinner("Réflexion en cours..."):
            try:
                from services.llm_service import call_llm_api
                # Préparation du contexte
                cv_context = st.session_state.get('pdf_text', 'Aucun CV importé pour le moment. L\'utilisateur crée un CV de zéro.')
                
                full_prompt = f"""Tu es un conseiller de carrière expert et proactif. 
                
                RÈGLES IMPORTANTES :
                1. Utilise les informations du CV ci-dessous comme base de travail.
                2. UTILISE TES CONNAISSANCES GÉNÉRALES sur le recrutement, les standards de l'industrie et les meilleures pratiques pour aider l'utilisateur à améliorer son CV, même si ces détails ne sont pas présents dans le document.
                3. Si aucun CV n'est fourni, base-toi sur ton expertise pour conseiller l'utilisateur sur la rédaction d'un CV attractif.
                4. Sois concis, professionnel et encourageant.

                Contexte (CV) : {cv_context}
                ---
                Question de l'utilisateur : {prompt if not audio_input else 'L\'utilisateur a envoyé un message vocal.'}
                """
                
                response = call_llm_api(full_prompt)
                
                from services.voice_service import text_to_audio_bytes
                audio_bytes = text_to_audio_bytes(response)
                
                # Affichage de l'audio d'abord pour l'immédiateté
                if audio_bytes:
                    st.audio(audio_bytes, format='audio/mp3', autoplay=True)
                
                # Effet de streaming/écriture progressive en "background"
                import time
                def stream_data():
                    for word in response.split(" "):
                        yield word + " "
                        time.sleep(0.05)
                
                st.write_stream(stream_data)
                
                # Sauvegarde finale
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": response, 
                    "audio": audio_bytes if audio_bytes else None
                })
            except Exception as e:
                st.error(f"Erreur : {e}")

# ── Pied de page ──
st.markdown("---")
st.caption("💡 Propulsé par l'IA Gemini & gTTS · Sprints 3-4")
