# Spécification Technique — US-02 : Analyse de CV par IA (Généralisation)

> **Auteur :** Architecte IA  
> **Sprint :** Sprint 3 — Intégration LLM & Résilience  
> **Statut :** 📐 En cours

---

## 1. Objectif

Remplacer le moteur de parsing heuristique (Regex) de la page `01_creer_cv.py` par l'analyse intelligente basée sur le LLM (Gemini). L'objectif est d'améliorer la précision de l'extraction des données complexes (descriptions d'expériences, dates variées, compétences implicites) et d'harmoniser le comportement de l'application.

---

## 2. Architecture de Fichiers

| Fichier | Action | Rôle |
|---|---|---|
| `src/pages/01_creer_cv.py` | Modifier | Remplacer l'appel à `cv_parser_service.py` par `llm_service.py`. |
| `src/services/llm_service.py` | Existant | Fournit déjà `parse_cv_with_ai` avec Retry. |
| `task.md` | Modifier | Suivi de l'état d'avancement. |

---

## 3. Détails d'Implémentation

### 3.1 Migration vers l'IA dans `01_creer_cv.py`
- **Changement d'import :** Supprimer `from services.cv_parser_service import parse_cv_text` et ajouter `from services.llm_service import parse_cv_with_ai`.
- **Logique de déclenchement :**
  - Conserver le `st.file_uploader` et le bouton "Analyser le CV".
  - Remplacer `parsed_data = parse_cv_text(text)` par `parsed_data = parse_cv_with_ai(text)`.
- **Gestion des Secrets :**
  - Vérifier la présence de `GEMINI_API_KEY` via `llm_service.get_api_key()`.
  - Si absente, afficher un message d'erreur invitant l'utilisateur à configurer son fichier `.env` ou sa sidebar.

### 3.2 Harmonisation des données
- S'assurer que le format JSON retourné par l'IA correspond exactement aux clés attendues par `st.session_state["cv_data"]`.
- Ajouter une étape de nettoyage pour convertir les listes de compétences en chaînes séparées par des virgules pour le widget `text_area`.

---

## 4. Stratégie de Test & Vérification

### 4.1 Tests unitaires
- Vérifier que `parse_cv_with_ai` gère les PDF volumineux ou avec un texte mal extrait (fallback vers dictionnaire vide).

### 4.2 Tests manuels
1. **Importation Complexe :** Uploader un CV avec des sections entremêlées. Vérifier que l'IA identifie correctement les dates de début/fin des expériences.
2. **Absence de Clé :** Supprimer temporairement la clé du `.env` et vérifier que l'UI affiche une erreur gracieuse au lieu de crash.
3. **Persistance :** Vérifier que les données analysées par l'IA apparaissent bien dans les onglets "Expériences" et "Formations" après le rechargement de la page.
