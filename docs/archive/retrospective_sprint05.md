# Synthèse Globale — Sprint 05 (Analyse de Sentiment & Feedback Visuel)

> **Rapport de Clôture**  
> **Auteur :** Business Analyst  
> **Statut :** Archivé ✅

## 📊 Résumé Exécutif

Le Sprint 5 a doté l'application d'une **intelligence émotionnelle**. Le conseiller IA ne se contente plus de répondre : il *comprend* le ton de l'utilisateur et adapte ses réponses en conséquence, tout en affichant un feedback visuel (emoji, label, jauge de score) sous chaque message du chat.

## 🎖️ Succès Clés

1. **Feedback Émotionnel Discret & Efficace** : L'utilisation de `st.caption` + `st.progress` offre un retour immédiat sans polluer l'interface. L'emoji dynamique choisi par Gemini rend le dialogue vivant.
2. **Empathie Adaptive** : L'injection du label de sentiment dans le prompt du conseiller produit des réponses perceptiblement différentes selon l'humeur détectée (encourageant si triste, dynamique si enthousiaste).
3. **Architecture Privacy-by-Design** : Toute la mémoire émotionnelle reste dans `st.session_state` (RAM), aucune donnée sensible n'est persistée sur disque.

## ⚠️ Points de Vigilance (Consensus Équipe)

* **Triple Appel API** : Chaque interaction génère 3 appels Gemini (sentiment user → réponse → sentiment réponse), ce qui triple la latence et l'exposition aux erreurs 429. **Recommandation unanime** : migrer vers du *Structured Output* (un seul appel retournant réponse + sentiment) dans un futur sprint.
* **Fallback Robuste** : Le retour `{"score": 0, "label": "Analyse indisponible", "emoji": "❔"}` en cas d'échec empêche tout crash, validé par le QA.

## 💡 Recommandations pour la suite (Backlog)

* **Sprint Z — La Touche Finale** : Polissage UI/UX (bannière, couleurs, ergonomie) pour une application prête à être montrée.
* **Optimisation API** : Fusionner les appels sentiment + réponse en un seul prompt structuré.

---
*Fin de rapport — Sprint 05 clôturé le 30 Mars 2026.*
