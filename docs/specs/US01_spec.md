# Spécification Technique — US-01 : Importation de CV au format PDF

> **Auteur :** Architecte IA  
> **Sprint :** Sprint 2 — Importation & Parsing  
> **Statut :** 📐 En review

---

## 1. Objectif

Permettre à l'utilisateur d'importer un CV existant au format PDF, d'en extraire le texte, et de le parser via des règles (Regex, mots-clés) pour extraire les données textuelles et pré-remplir automatiquement le formulaire de l'application, sans recourir à l'IA.

---

## 2. Architecture de Fichiers

### Fichiers concernés

| Fichier | Action | Rôle |
|---|---|---|
| `requirements.txt` | Modifier | Ajouter `pypdf` |
| `src/services/pdf_service.py` | Créer | Extraction texte depuis PDF |
| `src/services/cv_parser_service.py` | Créer | Parsing Regex/Heuristique pour structuration JSON |
| `src/pages/01_creer_cv.py` | Modifier | Ajout de l'UI d'upload et appel des services |
| `task.md` | Modifier | Suivi de l'état d'avancement |

---

## 3. Détails d'Implémentation

### 3.1 `requirements.txt`
Ajouter la librairie de parsing PDF :
```text
pypdf>=5.0.0
```

### 3.2 `src/services/pdf_service.py`
- **Fonction** `extract_text_from_pdf(uploaded_file) -> str` :
  - Prend l'objet `UploadedFile` de Streamlit.
  - Initialise `pypdf.PdfReader`.
  - Itère sur chaque page et concatène le texte extrait.
  - Lève une exception claire (ex: `ValueError`) si le PDF ne contient pas de texte lisible ou est corrompu.

### 3.3 `src/services/cv_parser_service.py`
- **Fonction** `parse_cv_text(text: str) -> dict` :
  - Découpe le texte extrait en sections grâce à la détection de mots-clés (ex: "Expérience", "Formation", "Contact").
  - Extrait les entités standard (E-mails, téléphones) via des Regex (`re` en Python).
  - Organise les expériences et formations identifiées selon une structure basique.
  - Retourne un dictionnaire prêt à être injecté respectant le format défini de `cv_data` de l'US-00 (contenant `personal_info`, `experiences`, `education`, `skills`).

### 3.4 `src/pages/01_creer_cv.py`
- **Interface UI :**
  - Tout en haut de la page (avant le formulaire), ajouter un `st.file_uploader("Importer un CV existant (PDF)", type=["pdf"])`.
  - Ajouter un bouton `st.button("Analyser le CV")`.
- **Logique :**
  - Afficher `<st.spinner("Extraction et analyse du CV en cours...")>`.
  - Extraire le texte : `text = pdf_service.extract_text_from_pdf(...)`.
  - Parser le texte : `parsed_data = cv_parser_service.parse_cv_text(text)`.
  - Mettre à jour `st.session_state["cv_data"]` (soit on remplace, soit on fusionne précautionneusement).
  - Rafraîchir l'interface : `st.rerun()`.

---

## 4. Stratégie de Test & Vérification

### 4.1 Tests automatisés ou de base
- `pip install -r requirements.txt` fonctionne et installe pypdf.
- L'application Streamlit démarre sans erreurs d'importation.

### 4.2 Tests manuels
1. **Cas Nominal :** Lancer l'app, uploader un fichier PDF contenant un CV standard. Constater le pré-remplissage du formulaire (emails, tel, et sections isolables).
2. **Parsing Partiel :** Uploader un PDF avec une structure complexe ; vérifier que le framework ne crashe pas et remplit ce qu'il peut (fallbacks).
3. **Erreur Fichier :** Uploader un fichier scanné vide (pas d'OCR), vérifier que le système avertit poliment l'utilisateur que le texte est introuvable.
