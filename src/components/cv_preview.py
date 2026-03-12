# cv_preview.py — Composant d'aperçu du CV
# Affiche un rendu visuel structuré du CV à partir des données de session.

import streamlit as st


def render_preview():
    """
    Affiche un aperçu en temps réel du CV basé sur les données
    stockées dans st.session_state["cv_data"].

    Si aucune donnée n'est saisie, affiche un message d'invitation.
    """
    # Récupération des données du CV depuis la session
    cv_data = st.session_state.get("cv_data", {})

    personal = cv_data.get("personal_info", {})
    experiences = cv_data.get("experiences", [])
    education = cv_data.get("education", [])
    skills = cv_data.get("skills", [])

    # Vérifie si des données substantielles ont été saisies
    has_data = (
        personal.get("name", "").strip()
        or len(experiences) > 0
        or len(education) > 0
        or len(skills) > 0
    )

    if not has_data:
        # ── Message par défaut quand le formulaire est vide ──
        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 3rem 1rem;
                color: #888;
                border: 2px dashed #ddd;
                border-radius: 12px;
                margin-top: 1rem;
            ">
                <h3>📝 Aperçu du CV</h3>
                <p>Remplissez le formulaire pour voir l'aperçu apparaître ici.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    # ── Rendu du CV ──
    st.markdown("---")

    # ── En-tête : Informations personnelles ──
    name = personal.get("name", "").strip()
    if name:
        st.markdown(f"## {name}")

    # Ligne de contact
    contact_parts = []
    if personal.get("email", "").strip():
        contact_parts.append(f"📧 {personal['email'].strip()}")
    if personal.get("phone", "").strip():
        contact_parts.append(f"📱 {personal['phone'].strip()}")
    if personal.get("address", "").strip():
        contact_parts.append(f"📍 {personal['address'].strip()}")
    if personal.get("linkedin", "").strip():
        contact_parts.append(f"🔗 {personal['linkedin'].strip()}")

    if contact_parts:
        st.markdown(" | ".join(contact_parts))

    # ── Section Expériences ──
    if experiences:
        st.markdown("### 💼 Expériences Professionnelles")
        for exp in experiences:
            title = exp.get("title", "Poste non défini")
            company = exp.get("company", "")
            start = exp.get("start", "")
            end = exp.get("end", "Présent")
            description = exp.get("description", "")

            st.markdown(f"**{title}** — {company}")
            st.caption(f"{start} → {end}")
            if description:
                st.markdown(f"> {description}")
            st.markdown("")

    # ── Section Formations ──
    if education:
        st.markdown("### 🎓 Formations")
        for edu in education:
            degree = edu.get("degree", "Diplôme non défini")
            school = edu.get("school", "")
            year = edu.get("year", "")

            st.markdown(f"**{degree}** — {school} ({year})")

    # ── Section Compétences ──
    if skills:
        st.markdown("### 🛠️ Compétences")
        # Affiche les compétences sous forme de badges inline
        badges = " &nbsp; ".join(
            [f"`{skill.strip()}`" for skill in skills if skill.strip()]
        )
        if badges:
            st.markdown(badges)
