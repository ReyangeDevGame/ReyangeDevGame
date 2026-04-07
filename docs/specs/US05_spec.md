# Spécification Technique — US-07 : La Touche Finale (Polissage UI/UX)

> **Auteur :** Architecte  
> **Sprint :** Sprint 6 — La Touche Finale  
> **Statut :** 📐 Prêt pour développement

---

## 1. Objectif

Transformer l'interface utilisateur actuelle pour lui donner un aspect "Premium" et professionnel. L'application doit séduire visuellement dès la première seconde grâce à un design soigné, des animations fluides et une typographie moderne, sans altérer la logique métier existante.

---

## 2. Architecture et Approche

Streamlit étant un framework initialement orienté Data Science, la personnalisation UI avancée passe majoritairement par l'injection de CSS personnalisé via `st.markdown(unsafe_allow_html=True)`.

### 2.1 Éléments Visés

1.  **Typographie :** Remplacement de la police système par une Google Font moderne (ex: *Inter*, *Outfit* ou *Plus Jakarta Sans*).
2.  **Couleurs et Fonds :** Utilisation de dégradés (gradients) subtils pour le fond de page principal et/ou la bannière d'accueil, rompant avec le fond uni classique.
3.  **Composants (Cartes & Boutons) :** 
    *   Ajout d'ombres portées douces (box-shadow).
    *   Bords arrondis (border-radius: 12px ou 16px).
    *   Micro-animations au survol (transform: translateY et modification du box-shadow).
4.  **Bannière (Hero Section) :** Un en-tête visuellement fort pour accueillir l'utilisateur cliqué.

---

## 3. Détails d'Implémentation

### Fichier cible : `src/app.py` et `src/pages/01_creer_cv.py`

*   **Bloc CSS Global :** Regrouper toutes les règles CSS dans une balise `<style>` injectée tôt dans le rendu de la page.

**Exemple de ciblage CSS (Vanilla) :**
```css
/* Import de la police */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

/* Application globale */
html, body, [class*="st-"] {
    font-family: 'Outfit', sans-serif !important;
}

/* Customisation des boutons Streamlit par défaut */
button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
    border: none !important;
    box-shadow: 0 4px 14px 0 rgba(99, 102, 241, 0.39) !important;
    transition: all 0.3s ease !important;
}

button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4) !important;
}
```

---

## 4. Contraintes et Risques

1.  **Sélecteurs Streamlit :** Les classes CSS générées par Streamlit (ex: `.st-emotion-cache-1wivap2`) changent à chaque mise à jour de la librairie. 
    *   *Mitigation :* Privilégier le ciblage des balises génériques (`button`, `div[data-testid="..."]`) ou injecter nos propres `<div>` avec des classes explicites via `st.markdown` (comme c'est déjà en partie le cas pour la `.hero-container`).
2.  **Performance :** Ne pas surcharger d'animations, rester sur un "Wow effect" subtil.
3.  **Accessibilité :** Veiller à garder un contraste suffisant entre le texte et les nouveaux fonds dégradés.

---

## 5. Critères de Validation pour le Développeur

- [ ] L'application utilise une typo Google Fonts personnalisée en production.
- [ ] Le bouton d'action principal ("Créer mon CV de zéro") possède un effet de survol moderne.
- [ ] Le conteneur principal a un design plus "aéré" (marges, ombres).
- [ ] Aucune régression fonctionnelle sur l'upload PDF ou le chatbot.
