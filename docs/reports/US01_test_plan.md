# Plan de Test Manuel — US-01 : Importation de CV au format PDF

## Critères d'acceptation (Checklist)

### 1. Upload & Parsing Global
- [ ] **Test 1.1 :** Uploader le fichier PDF de test. Le système affiche "Extraction et analyse en cours...".
- [ ] **Test 1.2 :** L'application ne crashe pas et renvoie un message de succès (ou d'erreur polie si PDF illisible).

### 2. Informations Personnelles
- [ ] **Test 2.1 :** Le champ `Nom complet` est rempli avec la première ligne pertinente.
- [ ] **Test 2.2 :** Le champ `Email` est extrait et le champ est rempli automatiquement au rafraîchissement.
- [ ] **Test 2.3 :** Le champ `Téléphone` contient le numéro extrait.
- [ ] **Test 2.4 :** Le champ `LinkedIn (URL)` contient le profil extrait (si présent).

### 3. Parcours / Expériences
- [ ] **Test 3.1 :** Les différentes expériences sont séparées (pas tout dans un seul gros bloc).
- [ ] **Test 3.2 :** Mappage correct : `Poste`, `Entreprise`, `Date de début`, `Date de fin`.
- [ ] **Test 3.3 :** La description contient le reste des responsabilités du poste correspondamment.

### 4. Formations
- [ ] **Test 4.1 :** Les lignes de formation sont récupérées.
- [ ] **Test 4.2 :** Mappage : `Diplôme`, `Établissement`, `Année` au moins très globalement en respectant la date de fin.

### 5. Compétences
- [ ] **Test 5.1 :** Les compétences sont listées et séparées par des virgules dans l'espace "Compétences".
