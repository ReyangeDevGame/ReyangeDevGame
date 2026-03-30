# Rétrospective — Sprint 05 (Analyse de Sentiment & Feedback Visuel)

**Date :** 30 Mars 2026

## 🏰 Architecte

### Bilan Technique (Réponses aux questions du BA)

1. **Valeur ajoutée du feedback émotionnel :** L'approche visuelle avec jauge/emoji offre un retour immédiat sur la "température" de l'échange. Si le design reste discret (comme c'est le cas avec le composant UI intégré), cela ajoute une couche d'intelligence perceptible sans polluer l'interface principale. L'utilisateur se sent "compris" au-delà du simple texte.
2. **Coût en tokens et latence :** Doubler les appels (un pour la réponse, un pour l'analyse) n'est effectivement pas très scalable en l'état. Pour la production, nous devrions explorer le *Structured Prompting* (demander à Gemini de renvoyer *simultanément* sa réponse narrative ET le JSON de sentiment dans un seul appel) afin d'optimiser les coûts et réduire de moitié la latence réseau.
3. **Adaptation du ton de l'IA :** Le fait d'injecter dynamiquement l'état émotionnel de l'utilisateur dans le prompt du conseiller est une belle avancée systémique. Du point de vue architectural, cela confirme la viabilité de notre `st.session_state` comme véritable "mémoire de travail" qui influence le comportement de l'Agent.

---

## ⌨️ Coder

### Bilan Technique (Réponses aux questions du BA)

1. **Valeur ajoutée du feedback émotionnel :** L'implémentation d'`analyze_sentiment()` dans `llm_service.py` avec retour JSON (`score`, `label`, `tone`, `emoji`) permet un affichage riche et immédiat via `st.metric` et `st.progress`. Le choix d'un emoji dynamique (choisi par Gemini selon le contexte) plutôt qu'un emoji statique rend le feedback plus naturel et engageant. L'intégration dans la boucle de messages (`for message in st.session_state.messages`) assure que le sentiment est visible à la relecture, pas seulement au moment de la réponse.
2. **Coût en tokens et latence :** En l'état, chaque interaction utilisateur déclenche **3 appels API** : (1) analyse du sentiment utilisateur, (2) génération de la réponse du conseiller, (3) analyse du sentiment de la réponse. Le mécanisme `tenacity` avec Exponential Backoff protège contre les erreurs 429 mais n'élimine pas la latence cumulée (~3-5s supplémentaires). Pour un prochain sprint, fusionner les appels via du *Structured Output* (un seul prompt retournant réponse + sentiment) diviserait la latence et les coûts par 2.
3. **Adaptation du ton de l'IA :** L'injection de `HUMEUR DE L'UTILISATEUR : {label} ({tone})` directement dans le prompt du conseiller produit des résultats très perceptibles. Lors des tests, un message triste (*"je suis découragé"*) génère une réponse encourageante et empathique, tandis qu'un message enthousiaste produit une réponse dynamique avec des emojis. Le `st.session_state` sert de mémoire émotionnelle inter-messages, ce qui est une base solide pour une future personnalisation plus fine.


---

## 🧪 QA (Assurance Qualité)

### Bilan Technique (Réponses aux questions du BA)

1. **Valeur ajoutée du feedback émotionnel :** Le feedback émotionnel enrichit indéniablement l'expérience sans la polluer. Lors de mes tests, l'emoji et le label sous chaque message donnent un sentiment de "dialogue vivant" — l'utilisateur perçoit que l'IA le comprend au-delà des mots. Le risque de distraction est maîtrisé grâce à la discrétion des composants (`st.caption` + `st.progress`), qui restent secondaires par rapport au contenu textuel du conseil. Le plan de test US-06 confirme que l'indicateur visuel ne perturbe pas la lisibilité du chat.
2. **Coût en tokens et latence :** C'est le point de vigilance principal identifié durant la validation. Le triptyque d'appels API (sentiment utilisateur → réponse conseiller → sentiment réponse) introduit un délai perceptible (~3-5s supplémentaires). Le fallback silencieux (`"Analyse indisponible"`) fonctionne parfaitement en cas d'échec, empêchant tout crash. Pour la production, la recommandation de l'Architecte de fusionner les appels via du *Structured Output* est fortement soutenue par le QA — cela réduirait la fenêtre de risque d'erreur réseau de 66%.
3. **Adaptation du ton de l'IA :** Les résultats sont probants et vérifiables. En testant un message anxieux ("J'ai peur de ne pas être à la hauteur"), l'IA a produit une réponse empathique avec un vocabulaire rassurant. Un message enthousiaste a généré une réponse dynamique avec des emojis de célébration. L'injection du label de sentiment dans le prompt est transparente et efficace. Le nettoyage JSON (backticks) dans `analyze_sentiment` est robuste et a passé tous les cas de test.


---

## 🛠️ DevOps

### Bilan Technique (Réponses aux questions du BA)

1. **Valeur ajoutée du feedback émotionnel :** D'un point de vue infrastructure, l'ajout de métadonnées légères (JSON de quelques octets) n'a aucun impact négatif sur la bande passante. C'est une amélioration logicielle "gratuite" en termes de ressources système pures, apportant une grande valeur perçue sans nécessiter de base de données complexe ou de serveurs supplémentaires.
2. **Coût en tokens et latence :** C’est le point critique pour le DevOps. Multiplier les appels API (jusqu'à 3 par interaction) multiplie par trois la probabilité d'échec réseau ou de dépassement de quota (Erreur 429). Bien que `tenacity` protège le code, l'expérience utilisateur en pâtit par une latence cumulée. La recommandation DevOps pour le passage à l'échelle est impérative : migrer vers un appel unique via *Structured Output* (JSON mode) pour garantir la stabilité et diviser par trois l'exposition aux pannes API.
3. **Adaptation du ton de l'IA :** L'approche "Prompt Injection" basée sur le `st.session_state` est excellente car elle reste "stateless" côté serveur (rien n'est stocké de manière persistante sur disque). Cela simplifie énormément la gestion de la confidentialité et de la conformité (RGPD), tout en offrant une expérience ultra-personnalisée. C'est une architecture "Privacy-by-Design" que nous devons conserver.

---

## 🧐 Questions Clés pour le Bilan

1. **Valeur ajoutée du feedback émotionnel** : L'affichage d'un score de sentiment et d'un emoji sous chaque message enrichit-il réellement l'expérience utilisateur, ou risque-t-il de distraire du conseil de carrière ?
2. **Coût en tokens et latence** : L'ajout d'un appel supplémentaire à Gemini (`analyze_sentiment`) après chaque interaction double le nombre d'appels API. Ce compromis performance/fonctionnalité est-il acceptable en production ?
3. **Adaptation du ton de l'IA** : L'injection de l'humeur détectée de l'utilisateur dans le prompt du conseiller (« sois encourageant s'il est triste ») produit-elle des réponses perceptiblement différentes et pertinentes ?
