# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-19

### Added
- **US-00 : Page d'Accueil et Structure de Base**
  - Mise en place de l'arborescence du projet (`src/`, `docs/`).
  - Page d'accueil Streamlit (`src/app.py`).
  - Formulaire de saisie de CV multi-pages/sections (`src/pages/01_creer_cv.py`).
  - Barre latérale de navigation avec gestion de la clé API Gemini (`src/components/sidebar.py`).
  - Composant d'aperçu du CV en temps réel (`src/components/cv_preview.py`).
  - Gestion de la configuration via `.env` et `src/config.py`.
  - Liste des dépendances dans `requirements.txt`.
