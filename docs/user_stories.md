# User Stories — Générateur de CV IA

> Priorité : 🔴 Haute | 🟡 Moyenne | 🟢 Basse

---

## US-00 : Page d'Accueil et Structure de Base 🔴

> **Sprint :** Sprint 1 — Échafaudage

### User Story

**En tant qu'** utilisateur,
**je veux** accéder à une page d'accueil claire et professionnelle du Générateur de CV,
**afin de** comprendre immédiatement ce que l'application propose et commencer à créer mon CV.

### Critères d'Acceptation

1. **Structure de l'application**
   - [ ] L'application Streamlit démarre sans erreur avec `streamlit run`.
   - [ ] Le projet suit une structure de fichiers organisée (`src/`, config, etc.).
   - [ ] Les dépendances sont listées dans un `requirements.txt` fonctionnel.

2. **Page d'accueil**
   - [ ] La page affiche un titre, un sous-titre et une brève description de l'application.
   - [ ] Un bouton ou lien **"🚀 Créer mon CV"** est visible et mène vers le formulaire de saisie.
   - [ ] Le design est soigné et professionnel (couleurs, typographie, espacement).

3. **Navigation de base**
   - [ ] Une barre latérale (sidebar) ou un menu permet de naviguer entre les sections futures.
   - [ ] La configuration API (clé Gemini) est accessible via la sidebar ou un fichier `.env`.

4. **Formulaire de saisie (structure de base)**
   - [ ] Une page "Créer mon CV" contient un formulaire avec les sections : Informations personnelles, Expériences, Formations, Compétences.
   - [ ] Les données saisies sont conservées dans `st.session_state`.
   - [ ] Un aperçu basique du CV est visible à côté du formulaire.

### Scénarios de test

| # | Scénario | Résultat attendu |
|---|---|---|
| 1 | `streamlit run src/app.py` | L'application démarre et affiche la page d'accueil |
| 2 | Clic sur "Créer mon CV" | Navigation vers le formulaire de saisie |
| 3 | Saisie de données dans le formulaire | Les données persistent dans la session |
| 4 | Visualisation de l'aperçu | L'aperçu reflète les données saisies |

### Notes techniques

- **Framework :** Streamlit (Python)
- **Structure :** `src/app.py` (point d'entrée), pages Streamlit pour la navigation
- **État :** `st.session_state` pour la persistance des données
- **Config :** `.env` pour la clé API, `requirements.txt` pour les dépendances

---

## US-01 : Importation de CV au format PDF 🔴

> **Sprint :** Sprint 2 — Importation & Parsing

### User Story

**En tant qu'** utilisateur,
**je veux** pouvoir charger mon CV existant au format PDF,
**afin de** pré-remplir automatiquement le formulaire avec mes informations sans avoir à tout retaper manuellement.

### Critères d'Acceptation

1. **Upload de fichier**
   - [x] L'interface propose une zone d'upload de fichier (`st.file_uploader`) n'acceptant que les fichiers PDF.
   - [x] L'application indique lorsque le fichier est chargé correctement.

2. **Extraction du texte**
   - [x] Le texte du PDF est extrait en utilisant une bibliothèque Python appropriée (ex: `PyPDF2` ou `pdfplumber`).

3. **Parsing heuristique (Regex)**
   - [x] Le texte extrait est analysé localement à l'aide de Regex et de mots-clés.
   - [x] Les données sont extraites au format JSON correspondant à l'état attendu (Informations personnelles, Expériences, Formations, Compétences).

4. **Pré-remplissage du formulaire**
   - [x] Les données structurées remplacent ou fusionnent avec l'état `st.session_state["cv_data"]`.
   - [x] L'aperçu du CV et le formulaire se mettent à jour avec les informations trouvées.

### Scénarios de test

| # | Scénario | Résultat attendu |
|---|---|---|
| 1 | Upload d'un PDF valide | Le système lit le fichier et affiche un indicateur de chargement (spinner) |
| 2 | Extraction et Parsing réussis | Les valeurs des champs du formulaire se mettent à jour et le preview change |
| 3 | Fichier invalide/corrompu | Un message d'erreur indique que le fichier ne peut être lu |
| 4 | Échec du parsing | Le texte est brut, invitant l'utilisateur à ajuster manuellement |

### Notes techniques

- **Éléments UI :** `st.file_uploader` (Streamlit).
- **Backend/Parsing :** `PyPDF2` pour l'extraction brute, puis algorithmes de parsing Regex/mots-clés en Python pur pour isoler les sections.
