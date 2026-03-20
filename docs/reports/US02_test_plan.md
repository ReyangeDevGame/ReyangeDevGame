# Plan de Test Manuel — US-02 & US-04 : Intégration LLM & Chatbot

**Sprint :** Sprint 3  
**Fonctionnalité :** Analyse de CV (Heuristique sur Home / IA sur page Créer) et Chatbot de Carrière  
**Approbateur (QA) :** Product Owner / QA  
**Mis à jour le :** 2026-03-20

---

## 🛠 Pré-requis Technico-Fonctionnels
- [ ] L'application démarre sans erreurs d'importation (`streamlit run src/app.py`).
- [ ] La sidebar n'affiche **pas** la navigation automatique Streamlit (nœuds `app` / `creer cv`).

## 🧪 Scénarios de Test (Checklist)

### 1. Interface (UX)
- [ ] **Navigation masquée** : La sidebar ne présente que le menu personnalisé (Accueil, Créer mon CV, Configuration).
- [ ] **Bouton "de zéro"** : Le clic sur "🚀 Créer mon CV de zéro" redirige directement vers le formulaire vide.
- [ ] **Upload PDF (Home)** : La zone d'upload est visible sous le bouton CTA et n'accepte que les `.pdf`.

### 2. Analyse PDF par Heuristique (Page d'Accueil — `cv_parser_service`)
- [ ] **Upload valide** : L'upload d'un PDF déclenche un spinner "Analyse du CV en cours...".
- [ ] **Redirection directe** : Après l'analyse, l'app bascule directement vers `01_creer_cv.py` (sans message de succès intermédiaire).
- [ ] **Pré-remplissage** : Les champs Email et Téléphone sont pré-remplis si présents dans le PDF.
- [ ] **PDF illisible** : Un PDF scanné (sans OCR) affiche un message d'erreur sans crasher l'application.

### 3. Analyse IA (Page "Créer mon CV" — `llm_service`)
- [ ] **Upload valide** : L'upload délenche un spinner "Analyse intelligente du CV par l'IA en cours...".
- [ ] **Clé API absente** : Un message d'erreur `GEMINI_API_KEY manquante` s'affiche, l'app s'arrête proprement (pas de crash).
- [ ] **Précision** : Les données complexes (descriptions, dates, sections) sont mieux structurées que le parsing heuristique.

### 4. Chatbot de Conseil de Carrière (US-04)
- [ ] **Visibilité conditionnelle** : Le Chatbot n'apparaît qu'après qu'un PDF a été extrait avec succès.
- [ ] **Contexte** : En posant une question sur le CV, l'IA cite des éléments réels du document importé.
- [ ] **Hors-sujet** : En demandant "Quel temps fait-il ?", l'IA refuse et redirige vers le sujet carrière.
- [ ] **Historique** : Les messages persistant durant toute la session.

---

## 🏁 Bilan d'Exécution
- **Date du test :** 2026-03-20
- **Version testée :** Sprint 3
- **Résultat global :** [ ] ✅ VALIDE - [ ] ❌ ÉCHEC
- **Commentaires / Bugs constatés :**
  - *(À compléter après validation)*
