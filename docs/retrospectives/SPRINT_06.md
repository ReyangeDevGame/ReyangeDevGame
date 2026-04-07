# Rétrospective — Sprint 06 (La Touche Finale / UI-UX)

**Date :** 07 Avril 2026

## 🏰 Architecte

### Bilan Technique (Réponses aux questions du BA)

1. **Impact visuel et performance :** L'approche CSS Vanilla via Streamlit est redoutable d'efficacité. Nous avons réussi à instiller des composantes premium (typographie Google Fonts, ombres, backgrounds dynamiques) moyennant un surcoût en bande passante et en CPU client virtuellement nul. Visuellement, le rendu fait passer l'outil d'un simple tableau de bord data à une application web finie, sans pénaliser la réactivité du modèle IA derrière.
2. **Maintenabilité du CSS :** Injecter le CSS depuis un fichier Python (`st.markdown`) s'est bien passé jusqu'ici car notre champ d'action était ciblé. Cependant, c'est un point de fragilité potentiel pour l'avenir : si nous multiplions les règles CSS complexes basées sur les classes générées de Streamlit, chaque montée de version majeure du framework pourrait casser la charte graphique. Pour le moment, notre ciblage générique ("button[kind='primary']" ou `html, body`) limite ce risque technique de maintenance.
3. **Cohérence de la "Bannière/Thème" :** La nouvelle harmonie de couleurs et de polices est constante de l'accueil jusqu'aux pages de chat. L'isolation des composants, particulièrement l'encapsulation de la jauge de sentiment et de la timeline des échanges, a grandement bénéficié de ce nouveau cadre unifié.
---

## ⌨️ Coder

1. **Impact visuel et performance** : L'expérience est métamorphosée. L'utilisation de CSS Vanilla pour les micro-animations et les dégradés a permis d'effacer le côté "brut" de Streamlit pour un rendu digne d'une application professionnelle haut de gamme. Côté performance, c'est totalement transparent pour l'utilisateur car le navigateur gère nativement ces styles sans surcharger le serveur.
2. **Maintenabilité du CSS** : Le choix d'un `theme_injector.py` centralisé est la clé de voûte de notre architecture. Cela nous a permis de basculer d'un thème Vampire à un thème Anime de manière chirurgicale sans polluer les fichiers de page (`app.py`, `01_creer_cv.py`). La vigilance reste de mise sur l'indentation des chaînes HTML/CSS pour éviter les faux-positifs Markdown, mais la structure globale est saine.
3. **Cohérence de la "Bannière/Thème"** : L'unification est réussie. Que ce soit sur la page d'accueil ou dans l'éditeur de CV, l'utilisateur baigne dans la même ambiance visuelle. L'intégration de la barre de sentiments et du chatbot au sein de ce thème renforce l'idée d'un outil "tout-en-un" cohérent et intuitif.
---

## 🧪 QA (Assurance Qualité)

1. **Impact visuel et performance** : ✅ Validé. Tous les tests de rendus manuels et (via subagent) ont prouvé qu'aucune latence perceptible n'a été introduite par le CSS personnalisé. L'expérience est visiblement amélioée et nettement plus fluide, agréable, créant un effet 'Wow' tout en ne pénalisant aucunement le temps de chargement de l'application ou la réactivité globale.
2. **Maintenabilité du CSS** : ✅ Validé. L'exécution répétée des tests fonctionnels de non-régression confirme que l'injection des styles visuels globaux n'interfère pas avec les mécanismes natifs de Streamlit comme l'upload de PDF ou le Chatbot. Néanmoins, un plan de test rigoureux demeure capital à chaque mise à jour de version du framework.
3. **Cohérence de la "Bannière/Thème"** : ✅ Validé. La vérification de la navigation transversale entre les pages a démontré l'excellente persistance du thème premium. L'intégration de la barre latérale, des badges de sentiment et du formulaire "Créer mon CV" est particulièrement réussie au sein du Dark Mode et unifiée par la typographie globale.

---

## 🛠️ DevOps

### Bilan Technique (Réponses aux questions du BA)

1. **Impact visuel et performance :** Du point de vue infrastructure, un sprint purement CSS/UI est un scénario idéal : aucune nouvelle dépendance Python n'a été ajoutée à `requirements.txt`, aucun nouvel appel API n'a été introduit. L'empreinte sur le serveur reste identique. Les styles CSS sont servis directement dans le HTML généré par Streamlit en mémoire vive — il n'y a pas de fichiers statiques supplémentaires à gérer ou déployer. C'est un sprint à risque opérationnel quasi-nul.
2. **Maintenabilité du CSS :** La décision architecturale de centraliser l'injection CSS dans un module dédié (`theme_injector.py`) est une excellente pratique DevOps. Cela crée un point de contrôle unique pour les changements visuels. Pour anticiper les mises à jour de Streamlit qui pourraient casser nos sélecteurs CSS, je recommande d'ajouter au moins un test de non-régression visuel (ex: capture d'écran de référence) dans la procédure de déploiement avant toute montée de version de `streamlit>=X.X.X` dans `requirements.txt`.
3. **Cohérence de la "Bannière/Thème" :** L'uniformité visuelle entre toutes les pages confirme que notre structure de fichiers (séparation `pages/`, `components/`, `services/`) a bien résisté à ce sprint d'intégration finale. La branche `main` est propre, stable, et prête pour une présentation ou une évaluation finale. Ce sprint marque la maturité du projet.


---

## 🧐 Questions Clés pour le Bilan

1. **Impact visuel et performance** : L'ajout de styles CSS personnalisés et de micro-animations (La Touche Finale) a-t-il enrichi l'expérience visuelle sans introduire de latence au rendu de l'interface Streamlit ?
2. **Maintenabilité du CSS** : L'injection de code Vanilla CSS via les composants natifs Streamlit (au lieu d'utiliser des composants front-end séparés) reste-t-elle gérable d'un point de vue de la propreté du code ?
3. **Cohérence de la "Bannière/Thème"** : La nouvelle palette graphique (premium, moderne) garde-t-elle une bonne cohérence entre toutes les parties de l'application (Sidebar, Chatbot, Extraction PDF) ?
