import io
from gtts import gTTS
import logging

def text_to_audio_bytes(text: str, lang: str = 'fr') -> bytes:
    """
    Convertit du texte en audio (MP3) en mémoire vive (RAM).
    Retourne les données binaires brutes (bytes).
    """
    if not text:
        return b""
        
    try:
        # Création de l'objet gTTS
        tts = gTTS(text=text, lang=lang)
        
        # Utilisation d'un buffer en mémoire (BytesIO) au lieu d'un fichier physique
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        
        # Retour au début du buffer pour lire les données
        audio_buffer.seek(0)
        return audio_buffer.read()
            
    except Exception as e:
        logging.error(f"Erreur lors de la synthèse vocale : {e}")
        return b""
