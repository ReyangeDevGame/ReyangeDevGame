# Rétrospective — Sprint 1 : Échafaudage

> **Date :** 2026-02-19  
> **Objectif :** Faire le bilan de la mise en place de la structure de base (US-00) avant de passer au Sprint 2.

---

## 🏛️ Feedback des Rôles

### 📐 ARCHITECT (L'Architecte)
- **Ce qui a fonctionné :** La structure modulaire (séparation `config`, `components`, `pages`) a permis une base saine et évolutive. L'adoption immédiate de `st.session_state` a sécurisé la gestion des données entre les vues.
- **Défis :** L'organisation des pages Streamlit reste un peu rigide (dépendance au nommage des fichiers). La synchronisation entre la clé API du `.env` et celle saisie manuellement en sidebar a nécessité une logique de "fallback" claire dans la spec.
- **Amélioration (Sprint 2) :** Je recommande de formaliser le schéma de données de l'objet `cv_data` (via un modèle ou dictionnaire typé) pour éviter les incohérences au fur et à mesure que nous ajoutons des fonctionnalités d'IA.

### 🔨 CODER (Le Développeur)
- **Ce qui a fonctionné :** L'implémentation a été très fluide grâce à la spec exhaustive. Streamlit a permis de construire l'interface (formulaire multi-onglets et aperçu live) avec très peu de code par rapport à un framework JS classique. La séparation des styles CSS dans `app.py` a permis de donner un aspect "premium" rapidement.
- **Défis :** La gestion dynamique des listes (expériences/formations) dans `st.session_state` nécessite une attention particulière, notamment l'utilisation de `st.rerun()` pour rafraîchir l'UI après une suppression. Un petit souci de PATH pour lancer Streamlit a été résolu en utilisant `python -m streamlit`.
- **Amélioration (Sprint 2) :** Créer un module helper pour la gestion de l'état `cv_data` (ex: `state_manager.py`) pour centraliser les ajouts/suppressions et éviter de manipuler directement le dictionnaire dans les pages.

### 🕵️‍♀️ QA (Le Testeur)
- **Ce qui a fonctionné :** La mise en place d'un Plan de Test Manuel clair a permis au Product Owner de valider les critères d'acceptation de manière autonome. L'aperçu dynamique a été validé comme étant bien synchronisé avec le formulaire.
- **Défis :** Un blocage environnemental (Streamlit non reconnu par le terminal par défaut) a été rencontré par le PO. Cela a nécessité une mise à jour rapide du walkthrough et du plan de test pour utiliser `python -m streamlit`.
- **Amélioration (Sprint 2) :** Proposer un script de "sanity check" (ex: `check_env.py`) que l'utilisateur peut lancer avant le test manuel pour s'assurer que toutes les dépendances sont installées et fonctionnelles.

### 🚀 DEVOPS (L'Opérateur)
- *À remplir...*

---

## ❓ Questions Clés du Bilan

1. **Qu'est-ce qui a bien fonctionné pendant ce premier sprint de mise en place ?**
   - La clarté des spécifications techniques de l'architecte a permis de coder "en une seule passe" sans zones d'ombre.
   - La structure modulaire proposée permet d'ajouter des pages très facilement.

2. **Quels ont été les principaux défis ou points de blocage rencontrés ?**
   - La persistance des données lors de la navigation entre les pages : résolu via `st.session_state` initialisé dans `app.py` et `01_creer_cv.py`.
   - L'alignement de l'aperçu dynamique à droite avec un formulaire complexe à gauche.

3. **Comment pouvons-nous améliorer notre collaboration ou notre processus technique pour le Sprint 2 ?**
   - Automatiser un premier test de "build" ou de "lint" pour vérifier que les imports entre modules fonctionnent toujours après une modification.
   - Définir plus précisément le format JSON attendu par l'IA pour l'US-01.

---

## 📋 Actions d'Amélioration (Pour le Sprint 2)

- [ ] Créer un script `check_env.py` pour valider l'environnement de test (QA)
- [ ] *Action 2...*
