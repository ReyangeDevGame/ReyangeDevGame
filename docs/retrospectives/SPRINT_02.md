# Rétrospective — Sprint 02 (Import PDF - Heuristique)

**Date :** 19 Mars 2026

## 🏰 Architecte

### Bilan Technique (Réponses aux questions du BA)

1. **Défis Techniques :** Le défi majeur a été de gérer la diversité sémantique des titres de sections (ex: "Expériences", "Projets", "Parcours professionnel") et la structure non linéaire de certains PDF. Là où l'IA aurait "compris" l'intention du candidat, les Regex ont nécessité une logique de "fail-safe" et de nettoyage de texte plus poussée pour éviter les faux positifs.
2. **Impact Architectural :** Le passage en local a simplifié le flux de données (plus besoin de gestion de clés API ou de quotas dans les services de base). `pdf_service.py` est resté simple, mais `cv_parser_service.py` porte désormais une logique métier complexe. L'architecture est plus "prévisible" mais moins "intelligente".
3. **Amélioration Continue :** La limitation principale réside dans les CV à colonnes multiples ou avec des formats très originaux (ex: compétences sous forme de graphiques). Pour le futur, il faudra surveiller le taux d'échec de parsing ; si la frustration utilisateur monte, un retour à l'IA (Gemini) comme "moteur de secours" sera à privilégier.

## ⌨️ Coder

### Bilan Technique (Réponses aux questions du BA)

1. **Défis Techniques :** Le principal défi a été la synchronisation de l'état (state) avec les widgets de Streamlit. L'extraction de texte brute est simple, mais forcer les champs de saisie à se mettre à jour instantanément après l'analyse a nécessité une gestion précise des clés (`st.session_state["input_xxx"]`). De plus, parser les dates pour séparer proprement l'entreprise du poste a été itératif pour couvrir les formats comme "11/2022 - Current".
2. **Impact Architectural :** Le passage en local a transformé `cv_parser_service.py` en un moteur de règles (`re`, split, strip). C'est plus rapide pour l'utilisateur car il n'y a pas de latence réseau, mais c'est plus fragile. La maintenabilité est correcte pour l'instant grâce à la modularité, mais ajouter de nouvelles règles de détection deviendra vite complexe sans une approche plus sémantique.
3. **Amélioration Continue :** Le parsing souffre sur les CV qui n'utilisent pas de mots-clés standards (ex: juste des icônes) ou qui mélangent les colonnes. À l'avenir, une approche hybride serait idéale : utiliser les Regex pour les données simples (Email, Tel) et une passe d'IA légère pour structurer les blocs d'expériences complexes si les Regex échouent.

## 🧪 QA (Assurance Qualité)

### Bilan Technique (Réponses aux questions du BA)

1. **Défis Techniques :** Le principal défi a été la validation d'une logique "fragile" par nature (Regex). Contrairement à l'IA qui gère la sémantique, l'heuristique demande une couverture de tests très large pour les différents délimiteurs (•, -, |) et formats de dates. La création de PDFs de tests variés (`dummy_valid.pdf`, `dummy_corrupted.pdf`) a été essentielle pour valider les fallbacks (mécanismes de secours).
2. **Impact Architectural :** L'approche locale a rendu les tests plus rapides, stables et déterministes (pas d'effet "boîte noire" de l'IA). En revanche, cela déplace la complexité vers la maintenance des cas de tests : chaque nouvelle règle de parsing ajoutée nécessite un nouveau scénario de validation pour éviter les régressions sur les autres formats.
3. **Amélioration Continue :** Le système de test a révélé que les CV multi-colonnes sont le point faible actuel. Pour le prochain sprint, il serait pertinent d'ajouter un "Score de Confiance" au parsing : si trop peu de sections sont détectées, l'application pourrait suggérer automatiquement une passe via Gemini pour garantir la qualité des données extraites.

## 🛠️ DevOps

### Bilan Technique (Réponses aux questions du BA)

1. **Défis Techniques :** Le principal défi a été l'ajout et la gestion de la nouvelle dépendance locale `pypdf`. Contrairement à l'IA qui déporte la charge sur un service tiers (Gemini), le parsing local impose que l'environnement d'exécution de chaque contributeur soit immédiatement synchronisé via le `requirements.txt` pour éviter toute erreur d'importation au lancement de l'application Streamlit.
2. **Impact Architectural :** La transition d'un service API externe vers une librairie locale (`pypdf`) a allégé les contraintes de connectivité et de quotas, mais a exigé une gestion plus rigoureuse des branches (`main` comme tronc actif pour l'US-01). L'architecture est plus robuste car elle est autonome localement, mais elle demande un contrôle plus strict de l'environnement de développement.
3. **Amélioration Continue :** On sent que la gestion manuelle des dépendances commence à atteindre ses limites si le projet grossit. Pour le prochain sprint, l'automatisation de la vérification de l'environnement ou l'usage de conteneurs (Docker) permettrait de garantir une reproductibilité parfaite entre l'Architecte, le Coder et les tests du QA, surtout si on réintroduit l'IA comme moteur hybride.

---

## 🧐 Questions Clés pour le Bilan

1. **Défis Techniques :** Quels ont été les principaux défis techniques liés au parsing par Regex (heuristique) comparé à l'approche IA initialement prévue ?
2. **Impact Architectural :** Comment le passage d'une extraction via API LLM à une extraction locale a-t-il impacté la complexité et la maintenabilité des services `pdf_service.py` et `cv_parser_service.py` ?
3. **Amélioration Continue :** Quelles sont les limitations majeures du parsing actuel (ex: structures complexes de CV) qui nécessiteront une attention particulière ou un retour à l'IA lors des prochains sprints ?
