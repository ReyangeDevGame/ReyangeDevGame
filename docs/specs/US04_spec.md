# Spécification Technique — US-06 : Analyse de Sentiment & Feedback Visuel

> **Auteur :** Architecte IA  
> **Sprint :** Sprint 5 — Analyse & Perception  
> **Statut :** 📐 Prêt pour développement

---

## 1. Objectif

Enrichir l'expérience utilisateur en fournissant un feedback émotionnel et tonal sur les interactions avec l'IA. L'objectif est de quantifier le "sentiment" (professionnalisme, confiance, enthousiasme) des réponses générées ou du contenu du CV.

---

## 2. Architecture de Fichiers

| Fichier | Action | Rôle |
|---|---|---|
| `src/services/llm_service.py` | Modifier | Ajout de la fonction d'analyse via Gemini. |
| `src/app.py` | Modifier | Intégration visuelle des jauges/scores. |
| `task.md` | Modifier | Suivi de l'état d'avancement. |

---

## 3. Détails Techniques

### 3.1 Analyse via LLM (`src/services/llm_service.py`)
- **Fonction :** `analyze_sentiment(text: str) -> dict`
- **Méthode :** Utilisation d'un prompt "Zero-shot" ou "Few-shot" demandant un format JSON strict :
  ```json
  {
    "score": 85,
    "label": "Très Professionnel",
    "tone": "Confident"
  }
  ```
- **Prompt Système :**
  *"Tu es un expert en analyse de discours. Évalue le texte suivant sur une échelle de 0 à 100 en termes d'impact professionnel. Identifie également le ton dominant."*

### 3.2 Rendu Visuel (`src/app.py`)
- Utilisation de `st.progress` pour le score global.
- Utilisation de colonnes Streamlit (`st.columns`) pour afficher des badges de couleur (ex: `info`, `success`) selon le label détecté.
- L'analyse est déclenchée de manière asynchrone (optionnel) ou séquentielle après la génération de texte.

---

## 4. Stratégie de Test

1. **Validation Format :** S'assurer que le LLM retourne toujours un JSON valide pour éviter les crashs de l'UI.
2. **Cohérence :** Tester avec des textes intentionnellement malpolis ou ultra-professionnels pour valider la sensibilité du score.
3. **UX :** Vérifier que l'affichage de la jauge n'alourdit pas visuellement le chat.
