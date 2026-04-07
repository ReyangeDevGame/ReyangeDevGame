# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Sprint 6] — 2026-04-07 (La Touche Finale)

### Ajouté
- **Design System Premium** : Refonte visuelle globale orientée Dark Mode (fonds dégradés fluides, typographie `Outfit`, glassmorphism, glowing shadows).
- **Injection CSS Centralisée** : Gestion fine de l'UX via `st.markdown` pour outrepasser les limites visuelles natives de Streamlit, avec des micro-animations au survol (`hover` effects) offrant une navigabilité très fluide et moderne.
- **Cohérence UI** : L'ensemble des composants (barre latérale, zone de drop des PDFs, chat IA et jauges de sentiment) est harmonisé graphiquement.

## [Sprint 5] — 2026-03-30 (Analyse & Perception)

### Ajouté
- **Analyse de Sentiment (US-06)** : Le conseiller IA évalue désormais le ton et l'impact professionnel des interactions.
- **Feedback Visuel Dynamique** : Intégration de jauges de score et de labels émotionnels (`score`, `label`, `emoji`) dans l'interface de chat.
- **Moteur d'empathie** : Nouvelle fonction `analyze_sentiment` dans `llm_service.py` utilisant des prompts Zero-shot pour une analyse instantanée.

### Modifié
- Harmonisation de l'interface de chat pour inclure les métadonnées de sentiment sous les réponses de l'assistant.

## [Sprint 4] — 2026-03-26 (L'IA prend la Parole)

### Ajouté
- **Interaction Bimodale (TTS/STT)** : L'IA peut désormais entendre (Micro) et répondre vocalement (Synthèse).
- **Service Voice RAM-Only** : Utilisation de `gTTS` et `io.BytesIO` pour un traitement 100% en mémoire vive (zéro déchet disque).
- **Navigation Proactive** : Le Chatbot est désormais accessible même en l'absence de CV importé, agissant comme un coach dès l'accueil.
- **Support STT** : Intégration de `st.audio_input` pour la saisie vocale.

### Modifié
- **Optimisation Import PDF** : Retour au moteur Regex local pour l'import, garantissant une rapidité maximale et préservant les quotas IA pour le conseil.
- **UI "IA Invisible"** : Masquage CSS des widgets audio pour une immersion totale.

## [Sprint 3] - 2026-03-20

### Ajouté
- Spécification technique pour l'intégration d'une API LLM réelle.
- Plan de Test QA pour la résilience et la sécurité API.
- Nouveau service `src/services/llm_service.py` pour la communication avec Gemini.
- Logique de Retry (Exponential Backoff) pour la robustesse des appels API.

### Modifié
- Sécurisation de l'application via `.env`.
- Mise à jour de l'interface `app.py` pour traiter les CV via l'IA.

## [1.1.0] - 2026-03-19

### ✨ Importation de CV PDF (Sprint 2 / US-01)
- **Upload PDF** : Ajout d'une interface d'importation de CV au format PDF via `pypdf`.
- **Parsing** : Analyse sémantique heuristique (Regex) pour structurer automatiquement les données extraites du texte brut.
- **Pré-remplissage** : Mise à jour automatique du formulaire de création de CV avec les informations trouvées dans le PDF.

---
*Sprint 2 officiellement clos et archivé.*

## [1.0.0] - 2026-02-19

### ✨ Initialisation & Échafaudage (Sprint 1)
- **Structure de base** : Mise en place de l'arborescence du projet (`src/`, `docs/`).
- **Accueil** : Page d'accueil Streamlit avec Hero section premium (`src/app.py`).
- **CV Form** : Formulaire de saisie multi-sections avec persistance de l'état (`src/pages/01_creer_cv.py`).
- **Sidebar** : Navigation et gestion sécurisée de la clé API Gemini (`src/components/sidebar.py`).
- **Aperçu** : Rendu dynamique du CV en temps réel (`src/components/cv_preview.py`).
- **Docs** : Initialisation du système de documentation, backlog et user stories.

---
*Sprint 1 officiellement clos et archivé.*
