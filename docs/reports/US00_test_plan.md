# Plan de Test Manuel — US-00 : Page d'Accueil et Structure de Base

> **Sprint :** Sprint 1 — Échafaudage  
> **Statut :** 🧪 Prêt pour Test  
> **ID du Test :** US00-M-01

## 1. Objectif
Valider que la structure de base du Générateur de CV IA est fonctionnelle, que la navigation est fluide et que la persistance des données dans le formulaire est assurée.

## 2. Pré-requis
1. Le projet est installé localement.
2. Les dépendances sont installées (`pip install -r requirements.txt`).
3. Un fichier `.env` est présent à la racine avec `GEMINI_API_KEY=votre_clé_ici` (ou vous la saisirez dans l'app).

## 3. Checklist de Test (Pas à pas)

| # | Action effectuée | Résultat attendu | Validé (✅/❌) |
|---|---|---|---|
| **1** | Lancer l'app : `python -m streamlit run src/app.py` | Le navigateur s'ouvre sur `http://localhost:8501`. | |
| **2** | Vérifier la page d'accueil | Titre "Générateur de CV IA" visible, design propre. | |
| **3** | Cliquer sur le bouton **"🚀 Créer mon CV"** | L'URL change vers `/01_creer_cv` et le formulaire apparaît. | |
| **4** | Saisir vos "Infos personnelles" | Le nom saisi apparaît instantanément dans l'aperçu à droite. | |
| **5** | Ajouter une expérience via l'onglet 💼 | Un volet s'ouvre. Saisissez un poste. L'aperçu se met à jour. | |
| **6** | Cliquer sur "🏠 Accueil" dans la sidebar | Retour à la page principale. | |
| **7** | Revenir à "📝 Créer mon CV" | **Critique :** Les données saisies précédemment doivent être encore là. | |
| **8** | Saisir une clé fictive dans la sidebar | Un message de succès vert "Clé API enregistrée ✅" apparaît. | |

## 4. Résultats & Signature
- **Verdict :** [À COMPLÉTER : PASSED / FAILED]
- **Date :** 19/02/2026
- **Testeur :** Product Owner
