# Spécification Technique — US-05 : Synthèse Vocale (Text-To-Speech)

> **Auteur :** Architecte IA  
> **Sprint :** Sprint 4 — L'Application prend la Parole  
> **Statut :** 📐 Prêt pour développement

---

## 1. Objectif

Ajouter une fonctionnalité de synthèse vocale au Chatbot pour permettre à l'utilisateur d'écouter les réponses de l'IA. Pour des raisons de performance et de propreté du système de fichiers, l'audio doit être généré et consommé entièrement en mémoire (RAM).

---

## 2. Architecture de Fichiers

| Fichier | Action | Rôle |
|---|---|---|
| `requirements.txt` | Modifier | Ajouter `gTTS`. |
| `src/services/voice_service.py` | Créer | Service de conversion texte -> audio (BytesIO). |
| `src/app.py` | Modifier | Appel du service et affichage du widget `st.audio`. |
| `task.md` | Modifier | Suivi de l'état d'avancement. |

---

## 3. Détails d'Implémentation

### 3.1 Service de Voix (`src/services/voice_service.py`)
- **Bibliothèque :** `gTTS` (Google Text-to-Speech).
- **Méthode :** `text_to_audio_bytes(text: str) -> bytes`
  - Utilise `io.BytesIO` pour capturer le flux audio.
  - Retourne les données binaires brutes (`.read()`).
  - Gère les exceptions réseau (timeout) pour éviter de bloquer l'interface.

### 3.2 Intégration Streamlit (`src/app.py`)
- **Stockage :** Ajouter une clé `"audio"` dans les dictionnaires de messages de `st.session_state["messages"]`.
- **Logique :** 
  - Juste après la génération de la réponse par Gemini, appeler le service de voix.
  - Stocker les bytes audio dans l'état de session avec le message.
- **Affichage :**
  - Dans la boucle d'affichage du chat, si `message["audio"]` est présent, afficher `st.audio(data, format="audio/mp3")`.

---

## 4. Stratégie de Test & Vérification

### 4.1 Tests manuels
1. **Génération Audio :** Poser une question au chat, vérifier qu'un lecteur audio apparaît sous la réponse.
2. **Qualité :** S'assurer que la langue est bien réglée sur 'fr' (Français).
3. **Hygiène Disque :** Vérifier qu'aucun fichier `.mp3` n'est créé à la racine du projet après plusieurs interactions.
4. **Performance :** Vérifier que le délai de génération audio n'impacte pas trop l'expérience utilisateur (spinner actif durant la phase de synthèse).
