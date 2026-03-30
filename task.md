# Suivi de Projet — Générateur de CV IA

## Phase actuelle : 🚀 Sprint 3 - Intégration LLM & Résilience (Conception)

---

### ✅ Phase 10 : Archivage & Synthèse (Fin de Sprint 2)
- [x] Compilation de la synthèse globale (`docs/reports/SPRINT_02_summary.md`)
- [x] Déplacement des spécifications US-01 vers `./docs/archive/`
- [x] Déplacement de la rétrospective SPRINT_02 vers `./docs/archive/`

### ✅ Phase 11 : Raffinage Sprint 3 (Chatbot IA — US-04)
- [x] Rôle **[BA]** : Définition de l'US-04 (Chatbot) dans `docs/user_stories.md`
- [x] Rôle **[ARCHITECT]** : Mise à jour de la spec `docs/specs/003_llm_integration.md`
- [x] Rôle **[CODER]** : Implémentation du Chatbot dans `app.py`
- [x] Rôle **[QA]** : Mise à jour du Test Plan `docs/reports/US02_test_plan.md`

### ✅ Phase 12 : Généralisation de l'Analyse IA (US-02)
- [x] Rôle **[ARCHITECT]** : Rédaction de la spec technique `docs/specs/US02_spec.md`
- [x] Rôle **[CODER]** : Migration de `01_creer_cv.py` du Regex vers le `llm_service`
- [x] Rôle **[CODER]** : Harmonisation de la gestion des erreurs et de l'état (st.session_state)
- [x] Rôle **[QA]** : Validation finale UI/IA réussie.

### ✅ Phase 13 : Archivage & Synthèse (Fin de Sprint 3)
- [x] Compilation de la synthèse globale (`docs/reports/SPRINT_03_summary.md`)
- [x] Déplacement des spécifications techniques vers `./docs/archive/`
- [x] Déplacement de la rétrospective SPRINT_03 vers `./docs/archive/`

---

*Sprint 3 clôturé et archivé par le Business Analyst le 2026-03-20. L'application est désormais propulsée par l'Intelligence Artificielle !*

## Phase actuelle : 🚀 Sprint 4 — Intégration de La Voix (gTTS)

---

### ✅ Phase 14 : Cadrage & Planification US-05 (Voix)
- [x] Rôle **[BA]** : Vérification de `docs/system_context.md`
- [x] Rôle **[BA]** : Mise à jour de l'Icebox dans `backlog.md`
- [x] Rôle **[BA]** : Rédaction détaillée de l'US-05 dans `docs/user_stories.md`
- [x] Rôle **[ARCHITECT]** : Rédaction de la spec technique `docs/specs/US05_spec.md`

### ✅ Phase 15 : DevOps (Activation Sprint 4)
- [x] Validation de la branche `main` pour la feature active.
- [x] Vérification des `requirements.txt` (`gTTS` présent et doublons nettoyés).
- [x] Feu vert donné au **[CODER]**.

### [x] Phase 16 : Développement & QA (Voix)
- [x] Rôle **[CODER]** : Implémentation de `src/services/voice_service.py`
- [x] Rôle **[CODER]** : Intégration de `st.audio` dans `app.py`
- [ ] Rôle **[QA]** : Tests de synthèse vocale en mémoire (RAM)

### [x] Phase 17 : IA Vocale Avancée (STT) & Navigation
- [x] Rôle **[CODER]** : Désactivation de l'IA pour l'import PDF (retour au Regex local)
- [x] Rôle **[CODER]** : Rendre le Chatbot accessible en permanence (même sans PDF)
- [x] Rôle **[CODER]** : Implémentation de `st.audio_input` (STT) dans `app.py`
- [x] Rôle **[QA]** : Validation des interactions bi-modales (Voix/Texte)

### ✅ Phase 18 : Clôture & Rétrospective (Sprint 4)
- [x] Rôle **[BA/QA]** : Initialisation et remplissage de la rétrospective (`docs/retrospectives/SPRINT_04.md`)
- [x] Rôle **[DEVOPS]** : Archivage des documents et mise à jour du CHANGELOG.md
- [x] Rôle **[PO]** : Validation finale du sprint

### ✅ Phase 18.1 : DevOps (Activation Sprint 5)
- [x] Validation de la branche `main` pour la feature active.
- [x] Vérification des `requirements.txt` (OK, `google-generativeai` déjà présent).
- [x] Feu vert donné au **[CODER]**.

---

*Sprint 4 clôturé le 29 Mars 2026. L'interaction vocale est stable.*

## Phase actuelle : 🚀 Sprint 5 — Analyse de Sentiment & Feedback

---

### ✅ Phase 19 : Planification US-06 (Analyse de Sentiment)
- [x] Rôle **[BA]** : Rédaction de l'US-06 dans `docs/user_stories.md`
- [x] Rôle **[BA]** : Mise à jour du `backlog.md`
- [x] Rôle **[BA]** : Validation de la vision du sprint (Sentiment & Feedback)
- [x] Rôle **[ARCHITECT]** : Rédaction de la spec technique `docs/specs/US06_spec.md`

### [x] Phase 20 : Développement & QA (Sentiment)
- [x] Rôle **[CODER]** : Implémentation d' `analyze_sentiment` dans `llm_service.py`
- [x] Rôle **[CODER]** : Intégration de l'indicateur visuel dans `app.py`
- [x] Rôle **[QA]** : Validation fonctionnelle des scores et feedback visuel effectuée.

### ✅ Phase 21 : Clôture & Synthèse (Sprint 5)
- [x] Rôle **[DEVOPS]** : Mise à jour des User Stories et du CHANGELOG.md
- [x] Rôle **[BA]** : Rédaction de la synthèse globale (`docs/archive/retrospective_sprint_05.md`)
- [x] Rôle **[PO]** : Validation finale du sprint

---

*Sprint 5 clôturé le 30 Mars 2026. L'application est désormais capable d'empathie analytique !*
