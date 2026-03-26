# Rétrospective — Sprint 04 (L'IA prend la Parole)

**Date :** 26 Mars 2026

## 🏰 Architecte

### Bilan Technique (Réponses aux questions du BA)

1. **Efficacité de l'interaction vocale :** L'architecture bilingue (Voix/Texte) apporte une dimension "Assistant Personnel" qui humanise l'interaction. Le défi architectural a été de synchroniser le flux STT -> LLM -> TTS sans introduire une latence prohibitive. La valeur ajoutée est nette pour l'accessibilité et l'engagement utilisateur.
2. **Gestion des ressources en mémoire vive :** L'usage de `io.BytesIO` est optimal pour la propreté du serveur (zéro fichier `.mp3` sur disque). Pour le futur, si l'historique de chat devient massif, il faudra prévoir une limite de conservation des buffers audio dans `st.session_state` pour éviter une croissance linéaire de la RAM consommée par la session.
3. **Pertinence des conseils de l'IA sans contexte PDF :** La transition vers une IA proactive a été fluide. L'architecture permet désormais de conseiller l'utilisateur dès la page d'accueil, même en l'absence de document importé. Cela transforme l'outil d'un simple "parseur" en un véritable "coach de carrière" autonome.

---

## ⌨️ Coder

### Bilan Technique (Réponses aux questions du BA)

1. **Efficacité de l'interaction vocale :** L'usage de `st.audio_input` (STT compatible Streamlit 1.53+) a été immédiat et très robuste. La vraie difficulté a été d'harmoniser la double entrée (Clavier vs Micro) dans la boucle événementielle. J'ai priorisé la détection d'une nouvelle entrée audio pour déclencher la synthèse vocale immédiatement. C'est une bimodalité puissante : l'utilisateur peut dicter une question et lire la réponse tout en l'écoutant (streaming simulé).
2. **Gestion des ressources en mémoire vive :** Aucun défi de performance constaté avec `io.BytesIO`. Cependant, comme chaque réponse audio génère entre 50 Ko et 200 Ko de données binaires, une session de chat de 50 messages consomme ~10 Mo de RAM. Pour une application multi-utilisateurs, il faudrait limiter la conservation de l'archive `bytes` uniquement aux 5 ou 10 derniers messages dans `st.session_state["messages"]`.
3. **Pertinence des conseils de l'IA sans contexte PDF :** Le passage à un mode "hybride" (Contextuel si PDF présent, Généraliste si absent) a été très simple à coder via le prompt (`if st.session_state.get('pdf_text'): ...`). Cela lève une frustration majeure de l'utilisateur qui souhaitait obtenir des conseils de rédaction *avant* même d'avoir un document. L'IA agit désormais comme un consultant en recrutement complet.

---

## 🧪 QA (Assurance Qualité)

### Bilan Technique (Réponses aux questions du BA)

1. **Efficacité de l'interaction vocale :** La bimodalité apporte une réelle valeur ajoutée en termes d'accessibilité et de confort. Mes tests sur `st.audio_input` confirment une capture sonore fiable. Le masquage CSS de `stAudio` est une réussite UX : il simule une voix système intégrée sans encombrer l'interface de widgets superflus. La navigation reste fluide et plus intuitive pour les utilisateurs mobiles ou malvoyants.
2. **Gestion des ressources en mémoire vive :** La stabilité est excellente sur des sessions de test standards (~20 messages). L'absence d'écriture disque accélère considérablement le rendu. Cependant, j'ai noté que le cache mémoire n'est pas purgé automatiquement ; pour des sessions extrêmes, une stratégie de "rolling buffer" (ne garder que les X derniers audios) sera nécessaire pour garantir la stabilité sur de faibles infrastructures.
3. **Pertinence des conseils de l'IA sans contexte PDF :** C'est le point fort du sprint. L'IA "coach" est fluide et pertinente même sans document source. Mes scénarios de test "Premier contact" (chat direct sans upload) ont produit des conseils structurants sur la mise en page et les mots-clés ATS. La transition entre le mode "Généraliste" et "Contextuel" (après upload) s'effectue sans aucune friction visible.


---

## 🛠️ DevOps

### Bilan Technique (Réponses aux questions du BA)

1. **Efficacité de l'interaction vocale :** La bimodalité (TTS/STT) a simplifié l'infrastructure en évitant complètement la gestion de fichiers audio physiques sur le serveur. L'usage de `gTTS` avec des flux binaires (`io.BytesIO`) permet un déploiement "disque-propre" (zero-disk), ce qui renforce la sécurité des données éphémères. Le défi DevOps a consisté à stabiliser les dépendances gRPC pour Gemini afin de supporter ces flux sans rupture DNS ou latence excessive.
2. **Gestion des ressources en mémoire vive :** L'absence d'écriture disque est un gain majeur pour la performance et la stabilité (pas de risque de saturation d'espace temporaire ou de conflit d'écriture). Cependant, comme le souligne le Coder, la RAM devient le nouveau point de vigilance. Du point de vue monitoring, il faudra définir des alertes si la consommation d'une session Streamlit dépasse 300 Mo, signe qu'un buffer audio circulaire (FIFO) doit alors être implémenté pour purger les anciens messages.
3. **Pertinence des conseils de l'IA sans contexte PDF :** Le passage à un mode proactif a considérablement réduit les logs d'erreurs "bloquantes" liés aux échecs de parsing PDF. L'utilisateur interagit désormais immédiatement avec le conseiller IA, ce qui lisse la charge serveur et améliore la perception de disponibilité du service, même en cas de latence sur les services de fichiers lourds.

---

## 🧐 Questions Clés pour le Bilan

1. **Efficacité de l'interaction vocale** : La bimodalité (Text-to-Speech et Speech-to-Text) apporte-t-elle une réelle valeur ajoutée à l'expérience utilisateur ou complexifie-t-elle la navigation ?
2. **Gestion des ressources en mémoire vive** : L'utilisation de `io.BytesIO` pour éviter l'écriture sur disque a-t-elle posé des défis de performance ou de stabilité lors de sessions prolongées ?
3. **Pertinence des conseils de l'IA sans contexte PDF** : Le passage d'un chatbot dépendant du PDF à un conseiller proactif et autonome a-t-il été fluide pour l'utilisateur ?
