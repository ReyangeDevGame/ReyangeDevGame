# config.py — Chargement de la configuration depuis le fichier .env
# Ce module centralise l'accès aux variables d'environnement du projet.

import os
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env situé à la racine du projet
load_dotenv()


def get_api_key() -> str:
    """
    Récupère la clé API Gemini depuis les variables d'environnement.

    Returns:
        str: La clé API Gemini, ou une chaîne vide si non définie.
    """
    return os.getenv("GEMINI_API_KEY", "")
