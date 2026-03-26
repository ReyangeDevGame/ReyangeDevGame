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

---

## US-02 : Intégration d'un LLM pour l'Analyse Avancée 🔴

> **Sprint :** Sprint 3 — Connexion IA & Résilience

### User Story

**En tant qu'** utilisateur,
**je veux** que mon CV soit analysé par une véritable Intelligence Artificielle (API),
**afin d'** obtenir une structuration parfaite des données et des conseils d'optimisation (résumés, suggestions de mots-clés) que le parsing simple ne peut offrir.

### Critères d'Acceptation

1. **Connexion API**
   - [x] L'application communique avec une API (Gemini ou OpenAI) via une clé secrète.
   - [x] La clé API est chargée depuis un fichier `.env` (non versionné).

2. **Parsing & Analyse IA**
   - [x] Le texte brut du PDF est envoyé au LLM avec un prompt structuré.
   - [x] Le LLM retourne un JSON structuré ou une analyse textuelle pertinente selon le projet.

3. **Robustesse (Retry Logic)**
   - [x] Une logique de "Retry" (Exponential Backoff) est implémentée pour gérer les erreurs de quota (Rate Limit 429).
   - [x] L'utilisateur est informé en cas d'échec persistant de l'IA.

### Scénarios de test

| # | Scénario | Résultat attendu |
|---|---|---|
| 1 | Envoi au LLM avec clé valide | Réponse structurée reçue et affichée |
| 2 | Envoi avec clé invalide | Message d'erreur clair "Clé API invalide" |
| 3 | Simulation d'erreur 429 (Quota) | Le système attend automatiquement avant de réessayer |
| 4 | État hors-ligne/Pas d'Internet | Message d'erreur de connexion réseau |

### Notes techniques

- **Librairies :** `google-generativeai` (Gemini) ou `openai`.
- **Secrets :** `python-dotenv` pour charger les variables d'environnement.
- **Résilience :** Utilisation de la bibliothèque `tenacity` ou implémentation manuelle du décorateur `retry`.

---

## US-03 : Génération d'un Résumé Professionnel par IA 🟡

> **Sprint :** Sprint 4 — Optimisation de Contenu (Prévu)

### User Story

**En tant qu'** utilisateur,
**je veux** que l'IA génère automatiquement une proposition de résumé professionnel (profil) basée sur mes expériences et compétences,
**afin de** disposer d'une introduction percutante sans avoir à la rédiger moi-même.

### Critères d'Acceptation

1. **Déclenchement de la génération**
   - [ ] Un bouton "✨ Suggérer un résumé" est visible dans la section "Résumé" ou "Profil" du formulaire.
   - [ ] Le bouton n'est actif que si au moins une expérience ou trois compétences sont renseignées.

2. **Qualité du contenu**
   - [ ] L'IA utilise les données de `st.session_state["cv_data"]` pour rédiger un paragraphe de 3 à 5 lignes.
   - [ ] Le ton est professionnel, concis et adapté au profil de l'utilisateur.

3. **Interaction Utilisateur**
   - [ ] Le résumé généré est inséré dans le champ de saisie correspondant.
   - [ ] L'utilisateur peut modifier ou supprimer la proposition manuellement.

### Scénarios de test

| # | Scénario | Résultat attendu |
|---|---|---|
| 1 | Clic sur "Suggérer" (données présentes) | Un texte cohérent apparaît dans le champ "Résumé" |
| 2 | Clic sur "Suggérer" (données absentes) | Un message d'avertissement demande de renseigner des expériences d'abord |
| 3 | Modification manuelle après génération | Le texte modifié est conservé dans la session |

### Notes techniques

- **Prompting :** Utiliser un "System Instruction" spécifique pour le style de rédaction.
- **UI :** `st.button` et `st.text_area` (Streamlit).

---

## US-05 : Synthèse Vocale (Text-To-Speech) 🟡

> **Sprint :** Sprint 4 — L'Application prend la Parole

### User Story

**En tant qu'** utilisateur du Chatbot,
**je veux** pouvoir écouter à voix haute les conseils générés par l'IA,
**afin de** rendre l'expérience plus interactive et accessible.

### Critères d'Acceptation

1. **Génération Audio**
   - [ ] L'application utilise `gTTS` pour convertir le texte de l'IA en voix.
   - [ ] L'application gère l'audio en mémoire pure via un flux binaire, sans écrire de fichiers `.mp3` physiques locaux.
2. **Interface Native**
   - [ ] Un composant `st.audio` natif de Streamlit permet à l'utilisateur de lire le son sous le message.

### Scénarios de test

| # | Scénario | Résultat attendu |
|---|---|---|
| 1 | L'IA donne une réponse | Un lecteur audio apparaît, la voix lit le français correctement |
| 2 | Vérification mémoire locale | Aucun fichier audio temporaire n'est présent à la racine du dossier |

### Notes techniques
- **Librairie :** `gTTS`, `io.BytesIO`.


---

## US-04 : Chatbot de Conseil de Carrière (IA + PDF) 🔴

> **Sprint :** Sprint 3 — Interaction & Support IA

### User Story

**En tant qu'** utilisateur ayant uploadé mon CV,
**je veux** pouvoir discuter avec une IA via un chat,
**afin de** poser des questions sur mon profil, demander des conseils de personnalisation ou préparer une entrevue en me basant sur les informations de mon PDF.

### Critères d'Acceptation

1. **Interface de Chat**
   - [x] Une fenêtre de chat (`st.chat_message`) est accessible après l'upload du PDF.
   - [x] L'historique des messages est conservé pendant la session.

2. **Contexte du Document**
   - [x] L'IA a accès au texte intégral extrait du PDF lors de chaque réponse.
   - [x] L'IA refuse poliment de répondre à des questions hors sujet (non liées à la carrière ou au CV).

3. **Réactivité**
   - [x] Les réponses sont générées via l'API Gemini avec un indicateur de chargement.
   - [x] L'application gère les erreurs de l'IA sans perdre l'historique de discussion.

### Scénarios de test

| # | Scénario | Résultat attendu |
|---|---|---|
| 1 | Question sur l'expérience | L'IA cite des éléments précis du PDF uploadé |
| 2 | Question "Comment améliorer mon CV ?" | L'IA propose des suggestions basées sur le contenu détecté |
| 3 | Question hors-sujet (ex: météo) | L'IA redirige vers le sujet professionnel |

### Notes techniques

- **Modèle :** `gemini-1.5-flash` avec injection de contexte (System Message).
- **Session State :** Stockage de l'historique dans `st.session_state["messages"]`.
