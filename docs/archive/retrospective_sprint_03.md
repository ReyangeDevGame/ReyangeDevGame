# Synthèse Globale — Sprint 03 (Intégration LLM & Résilience)

> **Rapport de Clôture**  
> **Auteur :** Business Analyst  
> **Statut :** Archivé ✅

## 📊 Résumé Exécutif

Le Sprint 3 marque la véritable transformation de l'outil en un **Générateur de CV IA**. La connexion réussie à l'API Gemini apporte une analyse sémantique pointue et l'introduction d'un Chatbot interactif (US-04) ouvre de nouvelles perspectives d'accompagnement pour l'utilisateur.

## 🎖️ Succès Clés

1. **Intégration de l'API Gemini :** Le défi de structurer les données en JSON strict sans hallucinations a été relevé. L'équipe a dû s'adapter avec agilité aux versions de modèles (découverte dynamique `v1beta` / `flash`).
2. **Robustesse Exemplaire :** Bien que l'IA soit au cœur du sprint, l'approche locale par Regex (`cv_parser_service.py`) a été conservée de manière brillante comme **système de secours** (Fallback). Si le réseau coupe ou si la clé expire, l'outil continue de fonctionner. La librairie `tenacity` assure de son côté une absorption fluide des micro-coupures et limites de quotas (Erreur 429).
3. **Sécurisation des Secrets :** L'usage du fichier `.env` est maîtrisé par toute l'équipe, assurant qu'aucun credential n'est compromis.

## ⚠️ Points de Vigilance & Défis rencontrés

* **Instinct Automatisé "vs" Dépendance API :** L'externalisation du parsing pose de nouveaux enjeux QA (stochastique vs déterministe). L'équipe QA a souligné la complexité d'écrire des tests validant des données qui peuvent subtilement varier d'un appel à l'autre.
* **Complexification du `app.py` :** L'intégration conjointe du parseur IA et de l'interface du Chatbot commence à peser sur le fichier principal. 

## 💡 Recommandations pour le Sprint 4

* Refactorisation logicielle pour déléguer la logique UI du Chatbot dans un composant séparé (`src/components/chat.py`).
* Poursuivre la feuille de route vers l'**US-03 (Génération de Résumé Professionnel par IA)** qui bénéficiera directement du socle posé ce sprint.

---
*Fin de rapport — Sprint 03 clôturé le 20 Mars 2026.*
