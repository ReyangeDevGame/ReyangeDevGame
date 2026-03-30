# Plan de Test Manuel — US-06 : Analyse de Sentiment & Feedback Visuel

**Sprint :** Sprint 5 — Analyse & Perception  
**Fonctionnalités :** Détection de ton, Scores de professionnalisme, Adaptation de réponse.  
**Approbateur (QA) :** Product Owner / QA

---

## 🛠 Pré-requis Technico-Fonctionnels
- [x] Le fichier `.env` contient une clé `GEMINI_API_KEY` valide.
- [x] L'application Streamlit est lancée (`streamlit run src/app.py`).
- [x] Les services `llm_service.py` et les intégrations dans `app.py` sont en place.

---

## 🧪 Scénarios de Test (Checklist)

### 1. Analyse de Sentiment (Utilisateur — Entrée)
- [x] **Détection de l'Humeur** : En tapant un message très enthousiaste (ex: "Je suis super content de mon nouveau poste !"), l'IA détecte un label positif (ex: "Indicateur: Joyeux").
- [x] **Affichage Badge/Emoji** : Un emoji représentatif et un libellé apparaissent sous le message de l'utilisateur dans le chat.
- [x] **Données de Session** : Le sentiment est correctement stocké dans `st.session_state.messages`.

### 2. Adaptation du Ton (Intelligence Artificielle)
- [x] **Réponse Empathique** : Si l'utilisateur exprime de l'anxiété (ex: "J'ai peur de mon entretien"), l'IA répond avec un ton particulièrement encourageant.
- [x] **Réponse Professionnelle** : Si l'utilisateur est formel, l'IA reste strictement professionnelle.
- [x] **Injection du Contexte** : Vérifier (via logs ou debug) que le label de sentiment de l'utilisateur est bien transmis au prompt de l'assistant.

### 3. Analyse de l'Assistant (Sortie)
- [x] **Auto-Analyse** : Chaque réponse générée par l'IA passe par `analyze_sentiment`.
- [x] **Indicateur de Professionnalisme** : Une barre de progression (`st.progress`) et un score (0-100) s'affichent sous la réponse de l'assistant.
- [x] **Label & Ton** : Un label (ex: "Très Professionnel") et un ton (ex: "Confident") sont visibles.

### 4. Robustesse & Formatage
- [x] **Gestion JSON Invalide** : Si Gemini renvoie un texte au lieu d'un JSON, l'application utilise les valeurs par défaut ("Analyse indisponible") sans planter.
- [x] **Nettoyage Backticks** : Le service gère correctement les réponses LLM entourées de ```json ... ```.
- [x] **Performance** : Le délai supplémentaire dû à la deuxième requête IA (analyse de sentiment) reste acceptable pour l'utilisateur.

---

## 🏁 Bilan d'Exécution
- **Date du test :** 29/03/2026
- **Version testée :** Sprint 5
- **Résultat global :** [x] ✅ VALIDE - [ ] ❌ ÉCHEC
- **Commentaires / Bugs constatés :**
  - Les tests sont passés avec succès. L'analyse bidirectionnelle du sentiment (Emoji pour l'utilisateur, Score pour l'IA) fonctionne parfaitement et le chatbot adapte son ton à l'humeur.

