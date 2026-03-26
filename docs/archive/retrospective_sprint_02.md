# Synthèse Globale — Sprint 02 (Importation PDF)

> **Rapport de Clôture**  
> **Auteur :** Business Analyst  
> **Statut :** Archivé ✅

## 📊 Résumé Exécutif

Le Sprint 2 a permis d'implémenter avec succès l'importation de CV au format PDF. Malgré un pivot architectural majeur (abandon du LLM au profit d'un parsing heuristique local par Regex), la valeur métier est délivrée : l'utilisateur peut désormais pré-remplir son profil en un clic.

## 🎖️ Succès Clés

1. **Autonomie Technique :** Le parsing local élimine la dépendance aux clés API Gemini et aux quotas, offrant une expérience utilisateur instantanée et gratuite.
2. **Qualité & Tests :** L'approche déterministe par Regex a permis au QA de mettre en place une batterie de tests stable sur des fichiers PDF de référence.
3. **Logique Métier Centralisée :** Le service `cv_parser_service.py` constitue une base solide pour l'extraction de données structurées.

## ⚠️ Points de Vigilance & Risques

* **Fragilité des Formats :** Les CV avec des structures non conventionnelles (multi-colonnes, icônes sans texte) restent le point faible de l'approche heuristique.
* **Complexité Croissante :** La maintenance des Regex pourrait devenir coûteuse si le nombre de cas particuliers à gérer augmente significativement.

## 💡 Recommandations pour le Sprint 3

Il est fortement recommandé d'adopter une **approche hybride** :
- Conserver le parsing par Regex pour les entités simples (E-mail, Téléphone, Liens).
- Réintroduire l'IA (Gemini) uniquement comme **"mécanisme de secours" (fallback)** pour structurer les blocs d'expériences et de formations complexes lorsque le taux de confiance du parsing local est trop bas.

---
*Fin de rapport — Sprint 02 clôturé le 19 Mars 2026.*
