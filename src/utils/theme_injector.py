import streamlit as st

def apply_app_theme():
    """
    Injecte le CSS correspondant au thème sélectionné dans st.session_state["app_theme"].
    Cette version unifie TOUTE l'interface de l'application (Accueil, Création, etc.).
    """
    theme = st.session_state.get("app_theme", "🌍 Minimal")
    
    # Base CSS commune (Masquer nav, scrollbar, etc.)
    base_css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
        
        [data-testid="stSidebarNav"] { display: none; }
        
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(100, 100, 100, 0.2); border-radius: 3px; }

        /* Styles transverses pour les composants personnalisés */
        .hero-container { text-align: center; padding: 2.5rem 1rem; }
        .hero-container h1 { font-size: 3rem; font-weight: 700; margin-bottom: 0.5rem; }
        .hero-container .subtitle { font-size: 1.2rem; opacity: 0.8; }
        .hero-container .description { font-size: 0.9rem; opacity: 0.6; max-width: 600px; margin: 0 auto; }

        .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 1rem; margin-top: 2rem; }
        .feature-card { padding: 1.5rem; border-radius: 16px; text-align: center; transition: transform 0.3s ease; border: 1px solid rgba(255,255,255,0.1); }
        .feature-card:hover { transform: translateY(-5px); }
        .feature-card .icon { font-size: 2rem; margin-bottom: 0.5rem; }

        .footer-custom { text-align: center; padding: 2rem; opacity: 0.5; font-size: 0.8rem; border-top: 1px solid rgba(255,255,255,0.05); margin-top: 3rem; }
    </style>
    """
    st.markdown(base_css, unsafe_allow_html=True)

    css = ""
    
    if theme == "🌍 Minimal":
        # Le design original Premium (Bleu Marine / Indigo)
        css = """
        <style>
            html, body, [class*="st-"]:not(span):not(i) { font-family: 'Outfit', sans-serif !important; }
            [data-testid="stAppViewContainer"] { background: linear-gradient(160deg, #0f0c29 0%, #1a1a2e 40%, #16213e 100%) !important; }
            [data-testid="stSidebar"] { background: linear-gradient(180deg, #0f0c29 0%, #1a1a2e 100%) !important; border-right: 1px solid rgba(99, 102, 241, 0.15) !important; }
            
            .hero-container h1 { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .feature-card { background: rgba(255, 255, 255, 0.03); }
            
            /* UI Elements */
            div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea { background-color: rgba(255, 255, 255, 0.05) !important; border: 1px solid rgba(255, 255, 255, 0.1) !important; color: white !important; }
            div[data-testid="stExpander"] { background-color: rgba(255, 255, 255, 0.03) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 12px; }
            button[data-baseweb="tab"] { border-radius: 8px 8px 0 0 !important; }
            .stButton>button[kind="primary"] { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important; border: none !important; border-radius: 10px !important; color: white !important; }
        </style>
        """
    
    elif theme == "💻 Hacker":
        css = """
        <style>
            html, body, [class*="st-"]:not(span):not(i) { font-family: 'Courier New', monospace !important; }
            .stApp { background-color: #000000 !important; color: #0bd10b !important; background-image: radial-gradient(#0bd10b 0.5px, transparent 0.5px) !important; background-size: 24px 24px !important; }
            [data-testid="stSidebar"] { background-color: #050505 !important; border-right: 1px solid #0bd10b !important; }
            
            .hero-container h1 { color: #0bd10b !important; text-shadow: 0 0 10px #0bd10b; -webkit-text-fill-color: #0bd10b; background: none; }
            .feature-card { background: #000; border: 1px solid #0bd10b; }
            
            /* UI Elements */
            h1, h2, h3, h4, h5, h6, label, p, span, small { color: #0bd10b !important; }
            .stButton>button { background-color: #000 !important; color: #0bd10b !important; border: 1px solid #0bd10b !important; border-radius: 0px !important; }
            div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea { background-color: #000 !important; color: #0bd10b !important; border: 1px solid #0bd10b !important; border-radius: 0 !important; }
            div[data-testid="stExpander"] { border: 1px solid #0bd10b !important; background: #000 !important; border-radius: 0 !important; }
        </style>
        """
    
    elif theme == "💖 Love":
        css = """
        <style>
            html, body, [class*="st-"]:not(span):not(i) { font-family: 'Outfit', sans-serif !important; }
            .stApp { background: linear-gradient(135deg, #ffafbd 0%, #ffc3a0 100%) !important; color: #881337 !important; }
            .stApp::after { content: "❤️ 💗"; position: fixed; top: 0; left: 0; width: 100%; height: 100%; font-size: 60px; opacity: 0.03; pointer-events: none; display: flex; flex-wrap: wrap; justify-content: space-around; }
            [data-testid="stSidebar"] { background-color: rgba(255, 255, 255, 0.4) !important; backdrop-filter: blur(10px); border-right: 1px solid #fda4af !important; }
            
            .hero-container h1 { color: #fb7185 !important; -webkit-text-fill-color: #fb7185; background: none; text-shadow: 2px 2px 4px rgba(255,255,255,0.5); }
            .feature-card { background: rgba(255, 255, 255, 0.5); border: 1px solid #fecdd3; }
            
            /* UI Elements */
            h1, h2, h3, h4, h5, h6, label, p, span, small { color: #881337 !important; }
            .stButton>button { background-color: #fb7185 !important; color: white !important; border: none !important; border-radius: 20px !important; }
            div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea { background-color: rgba(255, 255, 255, 0.6) !important; border: 1px solid #fecdd3 !important; border-radius: 12px !important; color: #881337 !important; }
            div[data-testid="stExpander"] { background: rgba(255,255,255,0.3) !important; border: 1px solid #fecdd3 !important; border-radius: 15px !important; }
        </style>
        """
        
    elif theme == "⚔️ Anime":
        css = """
        <style>
            html, body, [class*="st-"]:not(span):not(i) { font-family: 'Outfit', sans-serif !important; }
            .stApp { 
                background: linear-gradient(135deg, #050505 0%, #1a2e2e 50%, #050505 100%) !important; 
                color: #a5f3fc !important;
            }
            .stApp::before {
                content: "⚔️ 🏮 🌊 🌸";
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                font-size: 50px;
                opacity: 0.04;
                pointer-events: none;
                display: flex;
                flex-wrap: wrap;
                justify-content: space-around;
                z-index: 0;
            }
            [data-testid="stSidebar"] { 
                background: linear-gradient(180deg, #111827 0%, #064e4b 100%) !important; 
                border-right: 2px solid #2dd4bf !important; 
            }
            
            .hero-container h1 { 
                background: linear-gradient(90deg, #2dd4bf 0%, #fb923c 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 20px rgba(45, 212, 191, 0.3);
            }
            .feature-card { 
                background: rgba(17, 24, 39, 0.8); 
                border: 1px solid #14b8a6;
                box-shadow: 0 0 15px rgba(20, 184, 166, 0.1);
            }
            
            /* UI Elements */
            h1, h2, h3, h4, h5, h6, label, p, span, small { color: #ccfbf1 !important; }
            .stButton>button { 
                background: linear-gradient(135deg, #0d9488 0%, #065f46 100%) !important; 
                color: white !important; 
                border: 1px solid #2dd4bf !important; 
                border-radius: 8px !important;
                box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important;
            }
            div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea { 
                background-color: #0f172a !important; 
                color: #5eead4 !important; 
                border: 1px solid #0d9488 !important; 
                border-radius: 8px !important; 
            }
            div[data-testid="stExpander"] { 
                background: rgba(13, 148, 136, 0.05) !important; 
                border: 1px solid #0d9488 !important; 
                border-radius: 10px !important; 
            }
            
            /* Scrollbar Demon Slayer Style */
            ::-webkit-scrollbar-thumb { background: #2dd4bf !important; }
        </style>
        """

    st.markdown(css, unsafe_allow_html=True)
