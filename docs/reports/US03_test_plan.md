# Plan de Test Manuel — US-05 : L'Application prend la Parole (Voix)

**Sprint :** Sprint 4 — Interaction Vocale & Support IA  
**Fonctionnalités :** Synthèse Vocale (TTS), Saisie Vocale (STT) et Chatbot Proactif  
**Approbateur (QA) :** Product Owner / QA

---

## 🛠 Pré-requis Technico-Fonctionnels
- [x] La bibliothèque `gTTS` est installée (`pip install gTTS`).
- [x] L'application démarre sans erreur (`streamlit run src/app.py`).
- [x] Le fichier `.env` contient une clé `GEMINI_API_KEY` valide pour le Chatbot.

---

## 🧪 Scénarios de Test (Checklist)

### 1. Synthèse Vocale (Text-To-Speech - US-05)
- [x] **Déclenchement Automatique** : Après chaque réponse textuelle du Chatbot, un lecteur audio (`st.audio`) apparaît sous le message.
- [x] **Lecture Audio** : En cliquant sur "Play", le texte de l'assistant est lu à voix haute.
- [x] **Langue & Qualité** : La voix est intelligible et la langue est bien le Français (fr).
- [x] **Stockage en Mémoire (RAM)** : Vérifier (via l'explorateur de fichiers) qu'aucun fichier `.mp3` n'est généré à la racine du projet lors de l'écoute.
- [x] **Persistance** : En changeant de page et en revenant sur l'Accueil, le lecteur audio reste présent dans l'historique de chat pour les messages précédents.

### 2. Saisie Vocale (Speech-To-Text / STT)
- [x] **Visibilité du Widget** : Le composant `st.audio_input` ("Parlez à votre conseiller") est visible sous l'historique du chat.
- [x] **Enregistrement** : L'utilisateur peut enregistrer un message vocal.
- [x] **Envoi** : L'envoi du message vocal affiche une bulle utilisateur nommée "🎤 [Message Vocal]" dans le chat.
- [x] **Traitement IA** : L'IA répond au message vocal (Note : la logique actuelle utilise un prompt de transcription simulé).

### 3. Chatbot Proactif (US-04 Refined)
- [x] **Accessibilité sans PDF** : Le Chatbot est visible et utilisable dès l'ouverture de l'application, même si aucun CV n'est importé.
- [x] **Conseils Proactifs** : En demandant "Comment faire un bon CV ?", l'IA donne des conseils généraux basés sur son expertise (même sans contexte PDF).
- [x] **Consigne de Style** : Les réponses du Chatbot restent concises, professionnelles et encourageantes.

### 4. Robustesse & UX
- [x] **Indicateur de Chargement** : Le spinner "Réflexion en cours..." est visible durant toute la phase de génération (IA + Synthèse).
- [x] **Gestion des Erreurs** : Si la synthèse vocale échoue (ex: pas d'Internet), le message textuel s'affiche tout de même.

---

## 🏁 Bilan d'Exécution
- **Date du test :** 26/03/2026
- **Version testée :** Sprint 4 (Final)
- **Résultat global :** [x] ✅ VALIDE - [ ] ❌ ÉCHEC
- **Commentaires / Bugs constatés :**
  - Tout fonctionne parfaitement. La bimodalité apporte une vraie valeur ajoutée et l'IA Coach est très pertinente sans document.

