# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
