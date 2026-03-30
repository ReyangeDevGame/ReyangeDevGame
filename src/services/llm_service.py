import streamlit as st
import os
import json
import google.generativeai as genai
from tenacity import retry, wait_exponential, stop_after_attempt
from dotenv import load_dotenv

# Chargement des variables d'environnement (recherche récursive vers le haut pour .env)
load_dotenv(override=True)

def get_api_key():
    """Récupère la clé API depuis le fichier .env"""
    key = os.getenv("GEMINI_API_KEY")
    # Si la clé en session existe, elle prime
    if "api_key" in st.session_state and st.session_state["api_key"]:
        key = st.session_state["api_key"]
        
    if not key or "votre_cle_api" in key:
        return None
    return key

def get_best_model(api_key: str) -> str:
    """
    Retourne le meilleur modèle disponible pour cette clé API.
    Essaie les modèles préférés en ordre et liste les disponibles si nécessaire.
    """
    # Modèles à essayer dans l'ordre de préférence
    preferred = [
        "gemini-1.5-flash",
        "gemini-1.5-pro",
        "gemini-1.0-pro",
        "gemini-pro",
    ]

    genai.configure(api_key=api_key)

    # Récupère les modèles réellement disponibles pour cette clé
    try:
        available = [
            m.name.replace("models/", "")
            for m in genai.list_models()
            if "generateContent" in m.supported_generation_methods
        ]
        for pref in preferred:
            if pref in available:
                return pref
        # Fallback au premier modèle disponible
        if available:
            return available[0]
    except Exception:
        pass

    # Dernier recours : gemini-1.5-flash
    return "gemini-1.5-flash"


@retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(5),
    reraise=True
)
def call_llm_api(prompt: str):
    """
    Appelle l'API Gemini avec une logique de Retry (Exponential Backoff).
    Gère les erreurs de quota (429) et les micro-coupures réseau.
    """
    api_key = get_api_key()
    if not api_key:
        raise ValueError("Clé API manquante. Assurez-vous d'avoir un fichier .env avec GEMINI_API_KEY.")

    selected_model = get_best_model(api_key)
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(selected_model)
    
    try:
        # Appel à l'IA
        response = model.generate_content(prompt)
        
        if not response or not hasattr(response, 'text') or not response.text:
            raise Exception(f"L'API IA ({selected_model}) a renvoyé une réponse vide ou invalide.")
            
        return response.text
    except Exception as e:
        # Tenacity capturera cette exception et retentira si configuré
        raise e

def parse_cv_with_ai(cv_text: str):
    """
    Envoie le texte brut du CV à l'IA pour extraction structurée en JSON.
    """
    prompt = f"""
    Tu es un expert en recrutement. Analyse le texte brut du CV suivant et extrais les informations au format JSON strict.
    
    STRUCTURE JSON ATTENDUE :
    {{
      "personal_info": {{
        "name": "Nom complet",
        "email": "Email",
        "phone": "Téléphone",
        "address": "Adresse",
        "linkedin": "Lien LinkedIn"
      }},
      "experiences": [
        {{
          "title": "Poste",
          "company": "Entreprise",
          "start": "Date début",
          "end": "Date fin",
          "description": "Description des missions"
        }}
      ],
      "education": [
        {{
          "degree": "Diplôme",
          "school": "École/Université",
          "year": "Année"
        }}
      ],
      "skills": ["Compétence 1", "Compétence 2"]
    }}

    TEXTE DU CV :
    ---
    {cv_text}
    ---

    RETOURNE UNIQUEMENT LE JSON SANS TEXTE AUTOUR NI BACKTICKS MARKDOWN.
    """
    
    raw_response = call_llm_api(prompt)
    
    # Nettoyage si l'IA a mis des backticks ```json ... ```
    clean_json = raw_response.strip()
    if clean_json.startswith("```"):
        clean_json = clean_json.split("```")[1]
        if clean_json.startswith("json"):
            clean_json = clean_json[4:]
    
    try:
        data = json.loads(clean_json)
        return data
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON : {e}")
        # En cas d'erreur, on retourne une structure vide propre
        return {
            "personal_info": {},
            "experiences": [],
            "education": [],
            "skills": []
        }

def analyze_sentiment(text: str) -> dict:
    """
    Analyse le sentiment, le ton et le professionnalisme du texte.
    Retourne un dictionnaire {score, label, tone}.
    """
    prompt = f"""
    Tu es un expert en analyse de discours et en recrutement. 
    Évalue le texte suivant sur une échelle de 0 à 100 en termes d'impact professionnel et de clarté.
    Identifie également le ton dominant, un label court et un EMOJI représentatif.

    RETOURNE UNIQUEMENT UN JSON STRICT AU FORMAT SUIVANT :
    {{
        "score": 85,
        "label": "Très Professionnel",
        "tone": "Confident",
        "emoji": "🚀"
    }}

    TEXTE À ANALYSER :
    ---
    {text}
    ---
    """
    
    try:
        raw_response = call_llm_api(prompt)
        
        # Nettoyage JSON
        clean_json = raw_response.strip()
        if clean_json.startswith("```"):
            clean_json = clean_json.split("```")[1]
            if clean_json.startswith("json"):
                clean_json = clean_json[4:]
        
        return json.loads(clean_json)
    except Exception as e:
        # Fallback silencieux avec structure par défaut
        return {"score": 0, "label": "Analyse indisponible", "tone": "Inconnu", "emoji": "❔"}
