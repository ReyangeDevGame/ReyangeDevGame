# Rétrospective Automatisée — Sprint 03 (Intégration LLM)

**Date :** 20 Mars 2026

## 🏰 Architecte

### Bilan Technique (Réponses aux questions du BA)

1. **Intégration API :** La difficulté principale a résidé dans la conception du prompt initial et la garantie d'un retour au format JSON strictement valide. Il a fallu structurer le service `llm_service.py` pour encapsuler soigneusement les appels à `google.generativeai` et nettoyer la réponse brute (suppression des backticks Markdown) avant le décodage JSON en `parse_cv_with_ai`.
2. **Robustesse :** Le choix de la librairie `tenacity` a grandement facilité l'implémentation du Backoff exponentiel. Le décorateur `@retry` a permis d'isoler cette logique sans polluer le code métier. Nous avons validé l'absorption des micro-coupures et des erreurs de quota 429 de manière transparente pour l'interface utilisateur.
3. **Sécurité :** L'architecture s'appuyant sur `python-dotenv` a été imposée dès le départ. La règle de récupération des variables (`os.getenv("GEMINI_API_KEY")`) est centralisée et stricte. L'équipe a bien respecté l'exclusion du `.env` du gestionnaire de sources, garantissant la sécurité des credentials du LLM.

## ⌨️ Coder

### Bilan Technique (Réponses aux questions du BA)

1. **Intégration API :** La plus grande difficulté a été la gestion des versions de modèles Gemini (`v1beta` vs `v1`). Les nouvelles clés Google AI Studio génèrent des erreurs 404 sur les modèles obsolètes ou limités (comme `gemini-pro`). Il a fallu implémenter une logique de **découverte dynamique du meilleur modèle disponible** (`get_best_model`) via `genai.list_models()` pour s'assurer que l'application fonctionne avec n'importe quelle clé, ancienne ou nouvelle. De plus, la mise à jour de la librairie `google-generativeai` vers la version `0.8.6` a été requise pour supporter pleinement les modèles de la famille "flash".
2. **Robustesse :** Le mécanisme de Retry avec `tenacity` s'est avéré très simple à mettre en place grâce à son décorateur élégant. Il capte parfaitement les instabilités réseau. Cependant, le vrai test de robustesse s'est fait sur le fallback de l'extraction de base du CV : nous avons conservé l'extraction par Regex (`cv_parser_service.py`) pour remplir le formulaire par défaut, garantissant que l'application reste utilisable même si l'API IA est indisponible (quota dépassé ou clé expirée). L'IA est désormais réservée à la valeur ajoutée (le Chatbot Conseiller).
3. **Sécurité :** L'usage du fichier `.env` est maîtrisé. Nous avons également ajouté des messages d'erreur clairs dans l'UI pour guider l'utilisateur ("Clé API expirée", "Clé manquante") sans exposer les détails techniques de l'implémentation, tout en gardant une interface épurée en retirant la saisie manuelle de clé depuis l'interface Streamlit.

## 🧪 QA (Assurance Qualité)

### Bilan Technique (Réponses aux questions du BA)

1. **Intégration API :** La validation des résultats de l'IA a été plus complexe qu'avec l'heuristique (Regex) car l'IA peut parfois "halluciner" de l'information. J'ai dû mettre en place une stratégie de tests aléatoires (`dummy_valid.pdf`) pour m'assurer que les clés retournées par Gemini sont bien exactes et ne divergent pas de la vérité du document. L'ajout des Spinners Streamlit a également requis mon attention pour l'UX (vérifier qu'ils disparaissent bien après l'appel).
2. **Robustesse :** Le mécanisme de Retry a été très difficile à tester dans un cadre nominal car Gemini 1.5 Flash répondait rapidement. Pour forcer l'échec et vérifier l'efficacité de `tenacity`, j'ai dû couper temporairement le réseau au sein de l'environnement de test ou modifier artificiellement la clé API en cours d'exécution. Les fallbacks (passage à l'heuristique si la clé est absente sur la home) ont bien fonctionné.
3. **Sécurité :** Le test des fichiers cachés a confirmé que la clé n'est pas exposée (validation de la structure `.gitignore`). J'ai spécifiquement testé l'introduction d'une mauvaise clé dans `.env` et le logiciel ne s'est pas effondré, confirmant le succès de l'US-02 sur l'aspect résilience en affichant un message de type "GEMINI_API_KEY manquante ou invalide".

## 🛠️ DevOps

### Bilan Technique (Réponses aux questions du BA)

1. **Intégration API :** Du point de vue infrastructure, l'ajout de `google-generativeai` s'est fait sans friction via `requirements.txt`. Le défi a été de s'assurer que la dépendance (et celles liées comme gRPC) s'installe correctement sur tous les environnements locaux de l'équipe sans conflit de version Python.
2. **Robustesse :** L'ajout de `tenacity` a fluidifié la gestion des erreurs côté réseau. Pour valider ce mécanisme de retry (Exponential Backoff) d'un point de vue DevOps sans épuiser les quotas réels, l'équipe a dû simuler électroniquement des réponses `429 Too Many Requests`.
3. **Sécurité :** Le processus est robuste : le `.env` en local est strictement ignoré par Git. Le nettoyage d'un fichier potentiel `.env.example` lors du dernier commit montre que nous avons clarifié la démarche de template pour les secrets, sans jamais risquer de push la clé `GEMINI_API_KEY`. L'équipe a acquis le bon réflexe.

---

## 🧐 Questions Clés pour le Bilan

1. **Intégration API :** Qu'est-ce qui a été le plus difficile lors de la connexion initiale avec l'API (ex: format de données, authentification) ?
2. **Robustesse :** Le mécanisme de Retry a-t-il été facile à implémenter et avez-vous réussi à le tester concrètement ?
3. **Sécurité :** L'usage du fichier `.env` est-il bien compris par l'ensemble de l'équipe pour éviter les fuites de clés ?
