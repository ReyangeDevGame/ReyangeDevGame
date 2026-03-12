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
- **Ce qui a fonctionné :** L'initialisation du dépôt Git en fin de sprint a permis de sécuriser le travail accompli sur l'US-00. La structure de documentation (CHANGELOG, Backlog) est opérationnelle et permet un suivi rigoureux.
- **Défis :** Le retard dans l'initialisation du dépôt Git a masqué l'historique des premiers développements. La configuration du `.gitignore` a dû être vérifiée a posteriori pour ne pas committer de données sensibles (clés API).
- **Amélioration (Sprint 2) :** Automatiser la vérification du `requirements.txt` via un hook ou un script de build pour s'assurer que l'environnement de développement reste synchronisé avec la production.

---

## ❓ Questions Clés du Bilan

1. **Qu'est-ce qui a bien fonctionné pendant ce premier sprint de mise en place ?**
   - La clarté des spécifications techniques de l'architecte a permis de coder "en une seule passe" sans zones d'ombre.
   - La structure modulaire proposée permet d'ajouter des pages très facilement.
   - Le passage de relais entre les rôles (Planification -> Dev -> QA -> DevOps) est fluide.

2. **Quels ont été les principaux défis ou points de blocage rencontrés ?**
   - La persistance des données lors de la navigation entre les pages : résolu via `st.session_state` initialisé dans `app.py` et `01_creer_cv.py`.
   - L'alignement de l'aperçu dynamique à droite avec un formulaire complexe à gauche.
   - L'installation des dépendances Streamlit qui différait selon l'environnement local.

3. **Comment pouvons-nous améliorer notre collaboration ou notre processus technique pour le Sprint 2 ?**
   - Automatiser un premier test de "build" ou de "lint" pour vérifier que les imports entre modules fonctionnent toujours après une modification.
   - Définir plus précisément le format JSON attendu par l'IA pour l'US-01.
   - Commencer chaque nouvelle US sur une branche dédiée dès le début de la phase de développement.

---

## 📋 Actions d'Amélioration (Pour le Sprint 2)

- [ ] Créer un script `check_env.py` pour valider l'environnement de test (QA)
- [ ] Mettre en place un script ou un hook pour valider la synchronisation de `requirements.txt` (DevOps)

---

## 🏆 Synthèse Globale (Business Analyst)

L'objectif du Sprint 1 (Échafaudage) est **100% atteint**. L'application dispose d'une structure solide, d'une navigation fonctionnelle, d'un formulaire de saisie dynamique et d'un aperçu en temps réel.

### Points Forts
- **Collaboration Multi-Rôles :** Le passage de relais entre les rôles a été fluide et efficace.
- **Qualité Technique :** L'utilisation de Streamlit et la séparation des responsabilités assurent une base saine.

### Recommandations pour le Sprint 2
1. **State Management :** Créer un `state_manager.py` pour centraliser la manipulation de `cv_data`.
2. **Support QA :** Automatiser la vérification de l'environnement local avec `check_env.py`.
3. **Flux Git :** Utiliser des branches dédiées dès le début de chaque nouvelle fonctionnalité.
