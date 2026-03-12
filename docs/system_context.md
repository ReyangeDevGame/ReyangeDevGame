# System Context — Générateur de CV IA

## 1. Vision

Créer un **générateur de CV intelligent** qui permet à tout utilisateur de concevoir, optimiser et exporter un curriculum vitae professionnel, avec l'assistance de l'intelligence artificielle.

> **En une phrase :** Permettre à chacun de créer un CV percutant, multilingue et optimisé pour les systèmes ATS, grâce à une interface simple et à l'IA.

## 2. Utilisateurs Cibles

| Persona | Description |
|---|---|
| 🎓 **Étudiant** | Peu d'expérience, a besoin d'aide pour structurer et rédiger son premier CV. |
| 👔 **Professionnel en reconversion** | Possède un CV existant à moderniser ou adapter pour un nouveau secteur. |
| 🌍 **Candidat international** | A besoin de traduire et adapter son CV pour des marchés étrangers. |
| 👤 **Tout public** | Toute personne souhaitant créer ou améliorer son CV rapidement. |

## 3. Fonctionnalités Clés (MVP)

1. **Importation & Parsing de CV existant** — Charger un CV (PDF, DOCX) et en extraire automatiquement les informations structurées.
2. **Traduction & Adaptation multilingue** — Traduire le contenu du CV dans différentes langues et adapter la mise en forme aux conventions locales.
3. **Modèles personnalisables** — Proposer plusieurs templates de CV professionnels que l'utilisateur peut personnaliser (couleurs, polices, disposition).
4. **Rédaction assistée par IA** — Suggérer des formulations, améliorer les descriptions d'expériences et générer des résumés professionnels via un LLM.
5. **Optimisation ATS & Export** — Analyser le CV pour sa compatibilité avec les systèmes de suivi des candidatures (ATS) et exporter en PDF/DOCX.

## 4. Contraintes Techniques

| Élément | Choix |
|---|---|
| **Langage** | Python |
| **Interface** | Streamlit |
| **IA** | API LLM (à définir : Gemini, OpenAI…) |
| **Formats supportés** | Import : PDF, DOCX — Export : PDF, DOCX |

## 5. Diagramme de Contexte

```
┌─────────────┐         ┌──────────────────────────┐         ┌─────────────┐
│ Utilisateur │────────▶│  Générateur de CV IA      │────────▶│ CV exporté  │
│ (navigateur)│         │  (Streamlit + Python)     │         │ (PDF/DOCX)  │
└─────────────┘         └──────────┬───────────────┘         └─────────────┘
                                   │
                          ┌────────▼────────┐
                          │   API LLM       │
                          │ (Gemini/OpenAI) │
                          └─────────────────┘
```
