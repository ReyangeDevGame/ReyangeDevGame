# Plan de Test Manuel — US-07 : La Touche Finale (Polissage UI/UX)

**Sprint :** Sprint 6 — La Touche Finale  
**Fonctionnalité :** Refonte visuelle complète (Design System, Animations, Typographie)  
**Approbateur (QA) :** Product Owner / QA

---

## 🛠 Pré-requis Technico-Fonctionnels
- [x] L'application Streamlit démarre sans erreur (`streamlit run src/app.py`).
- [x] Le navigateur utilisé pour le test est moderne (Chrome, Firefox, Safari ou Edge).
- [x] Le fichier `app.py` et les fichiers des pages (`01_creer_cv.py`) intègrent bien le CSS métier.

---

## 🧪 Scénarios de Test (Checklist)

### 1. Typographie & Fond Global
- [x] **Google Fonts** : La police globale utilisée par l'application est bien `Outfit`.
- [x] **Background Dégradé** : Le fond de l'application affiche un dégradé élégant de teintes sombres (Dark Mode) au lieu du fond uni par défaut.
- [x] **Lisibilité** : Le contraste entre les textes (titres, paragraphes, labels) et le nouveau fond sombre est suffisant.

### 2. Animations & Hero Section
- [x] **Animation d'Entrée** : Au chargement de la page d'accueil, le bloc principal (Hero Section) bénéficie d'une animation douce d'apparition (ex: `fadeInDown`).
- [x] **Titre Gradient** : Le titre principal s'affiche avec un dégradé de couleur harmonieux (tri-couleur).

### 3. Composants Interactifs (Boutons & Inputs)
- [x] **Survol des Boutons (Hover)** : Le passage de la souris sur le bouton principal ("Créer mon CV de zéro") provoque une légère élévation (`translateY`) et l'apparition d'une ombre lumineuse (glow shadow).
- [x] **Inputs & Textareas** : Les champs de saisie de texte ont des bords arrondis et s'illuminent (glow indigo/violet) lorsqu'ils ont le focus (clic à l'intérieur).
- [x] **Glassmorphism** : Les cartes ou conteneurs principaux possèdent un effet de verre dépoli (`backdrop-filter: blur`) avec une légère transparence.

### 4. Composants Métier (Feedback IA & Chat)
- [x] **Jauge de Progression** : La barre de progression du score de l'IA (Analyse de sentiment) respecte le design "Gradient" et s'intègre bien au fond sombre.
- [x] **Métrique de Sentiment** : Les badges/composants affichant l'humeur et l'emoji ont un fond translucide et une bordure délicate.
- [x] **Scrollbars** : La barre de défilement globale (scrollbar) est personnalisée (ex: aux couleurs de l'application, indigo).

### 5. Polissage et Non-Régression
- [x] **Pied de page (Footer)** : Le pied de page est présent en bas de l'écran, est dédupliqué, ne gêne pas la saisie, et affiche correctement la mention "Sprint 6".
- [x] **Navigation Transverse** : Le thème graphique persiste et est cohérent lors du passage de l'Accueil à la page "Créer mon CV".
- [x] **Redirection Automatique (Nouveau)** : Lors de l'upload d'un PDF valide sur l'accueil, l'application analyse le document puis redirige automatiquement vers la page 'Créer mon CV'.
- [x] **Non-Régression Fonctionnelle Chat** : L'interaction textuelle avec le Chatbot IA fonctionne toujours parfaitement (Analyse de sentiment présente).
- [x] **Non-Régression Fonctionnelle Voix** : La synthèse vocale (gTTS) et la saisie vocale (STT) sont toujours opérationnelles et intégrées au design (audio masqué/stylisé).

---

## 🏁 Bilan d'Exécution
- **Date du test :** 02/04/2026
- **Version testée :** Sprint 6 + Redirection Fix
- **Résultat global :** [x] ✅ VALIDE - [ ] ❌ ÉCHEC
- **Commentaires / Bugs constatés :**
  - La partie 5 (Polissage & Non-Régression) a été entièrement validée par le QA. L'unité visuelle est maintenue, la redirection automatique après upload PDF fluidifie l'expérience, et le bimodal (Chat/Voix) reste stable avec le nouveau design.

