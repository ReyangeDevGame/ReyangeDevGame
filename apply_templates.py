import sys

with open('src/components/cv_preview.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_content = "".join(lines[:74])

new_content += """
    template_id = st.session_state.get('selected_template', 'Template 1')

    # ========== TEMPLATE 1 : MODERNE (JAUNE & NOIR) ==========
    if template_id == 'Template 1':
        css = '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        body { margin: 0; padding: 0; background: transparent; }
        .cv-container { display: flex; background-color: white; color: #333; font-family: 'Outfit', sans-serif; border-radius: 6px; overflow: hidden; position: relative; min-height: 850px; text-align: left; }
        .cv-left { width: 32%; background-color: #f3f4f6; padding: 2rem 1.5rem; position: relative; z-index: 3; border-right: 1px solid #e5e7eb; }
        .cv-right { width: 68%; padding: 2rem; position: relative; z-index: 3; }
        .geom-yellow { position: absolute; top: 0; left: 0; width: 100%; height: 240px; background-color: #facc15; clip-path: polygon(0 0, 100% 0, 100% 50%, 0 100%); z-index: 1; }
        .geom-black { position: absolute; top: 0; left: 0; width: 55%; height: 190px; background-color: #111; clip-path: polygon(0 0, 100% 0, 40% 100%, 0 100%); z-index: 2; }
        .cv-name { font-size: 2.3rem; font-weight: 900; color: #111; margin-top: 110px; margin-bottom: 2px; letter-spacing: 1px; text-transform: uppercase; line-height: 1.1; }
        .cv-job-title { font-size: 1rem; color: #666; margin-bottom: 1.5rem; letter-spacing: 1.5px; text-transform: uppercase; }
        .cv-bio { font-size: 0.8rem; color: #666; line-height: 1.6; margin-bottom: 2.5rem; }
        .cv-section-title-right { font-size: 0.95rem; font-weight: 800; color: #ca8a04; margin-bottom: 1.5rem; margin-top: 2rem; text-transform: uppercase; letter-spacing: 0.5px; }
        .cv-left-section-title { font-size: 0.95rem; font-weight: 800; color: #111; margin-bottom: 1.2rem; margin-top: 2rem; text-transform: uppercase; letter-spacing: 0.5px; }
        .cv-contact-item { margin-bottom: 1.2rem; }
        .cv-contact-label { font-weight: 800; font-size: 0.8rem; color: #111; margin-bottom: 0.1rem; }
        .cv-contact-value { font-size: 0.8rem; color: #555; word-wrap: break-word; }
        .cv-skill-item { font-size: 0.85rem; color: #555; margin-bottom: 0.4rem; display: block; }
        .cv-exp-grid { display: grid; grid-template-columns: 70px 1fr; gap: 1.5rem; margin-bottom: 1.8rem; }
        .cv-date { font-size: 0.8rem; color: #555; font-weight: 600; line-height: 1.4;}
        .cv-content-title { font-weight: 800; font-size: 0.85rem; color: #111; margin-bottom: 0.3rem; text-transform: uppercase;}
        .cv-content-desc { font-size: 0.8rem; color: #555; line-height: 1.5; }
        </style>
        '''
        
        html_content = f'''
        {css}
        <div class="cv-container">
            <div class="geom-yellow"></div>
            <div class="geom-black"></div>
            <div class="cv-left">
                <div style="margin-top: 8rem;"></div>
                <div class="cv-left-section-title">PROFILE</div>
                {contact_html}
                <div class="cv-left-section-title">SKILLS</div>
                {skills_html}
            </div>
            <div class="cv-right">
                <h1 class="cv-name">{name}</h1>
                <div class="cv-job-title">{job_title}</div>
                <div class="cv-bio">Professionnel dévoué avec une expérience prouvée. Capable de travailler en équipe et de s'adapter rapidement.</div>
                {f'<div class="cv-section-title-right">PROFESSIONAL EXPERIENCE</div>{xp_html}' if experiences else ''}
                {f'<div class="cv-section-title-right">EDUCATION</div>{edu_html}' if education else ''}
            </div>
        </div>
        '''

    # ========== TEMPLATE 2 : CORPORATE BLEU ==========
    elif template_id == 'Template 2':
        css = '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        body { margin: 0; padding: 0; background: transparent; }
        .cv-container { font-family: 'Outfit', sans-serif; background: white; color: #333; display: flex; flex-direction: column; min-height: 850px; border-radius: 6px; overflow: hidden;}
        .cv-header { background-color: #1e3a8a; color: white; padding: 3rem 2rem; text-align: center; }
        .cv-name { font-size: 2.5rem; font-weight: 800; margin: 0; text-transform: uppercase; letter-spacing: 2px; }
        .cv-job-title { font-size: 1.2rem; color: #93c5fd; margin-top: 0.5rem; text-transform: uppercase; letter-spacing: 1px; }
        .cv-contact-row { display: flex; justify-content: center; gap: 2rem; margin-top: 1.5rem; font-size: 0.9rem; color: #e5e7eb; flex-wrap: wrap; }
        .cv-body { display: flex; flex: 1; padding: 2rem; gap: 2.5rem; }
        .cv-left { width: 30%; }
        .cv-right { width: 70%; }
        .cv-section-title-left { font-size: 1.1rem; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #e5e7eb; padding-bottom: 0.5rem; margin-bottom: 1rem; margin-top: 0; text-transform: uppercase;}
        .cv-section-title-right { font-size: 1.2rem; font-weight: 800; color: #1e3a8a; border-bottom: 2px solid #e5e7eb; padding-bottom: 0.5rem; margin-bottom: 1.5rem; text-transform: uppercase;}
        .cv-skill-item { display: inline-block; background-color: #f3f4f6; padding: 6px 10px; border-radius: 4px; font-size: 0.8rem; margin: 0 4px 6px 0; color: #374151;}
        .cv-exp-grid { display: grid; grid-template-columns: 80px 1fr; gap: 1rem; margin-bottom: 1.5rem; }
        .cv-date { font-size: 0.85rem; color: #6b7280; font-weight: 600; line-height: 1.4; }
        .cv-content-title { font-weight: 800; font-size: 0.95rem; color: #111; margin-bottom: 0.2rem; text-transform: uppercase;}
        .cv-content-desc { font-size: 0.85rem; color: #4b5563; line-height: 1.5; }
        .cv-bio { font-size: 0.85rem; line-height: 1.6; color: #4b5563; margin-bottom: 2rem; }
        </style>
        '''
        contact_items = [f"<span>{personal[k]}</span>" for _, k in mapping_contact if personal.get(k)]
        contact_row = "<div class='cv-contact-row'>" + " &bull; ".join(contact_items) + "</div>" if contact_items else ""
        skills_pills = ''.join([f'<span class="cv-skill-item">{s}</span>' for s in skills]) if skills else '-'
        
        html_content = f'''
        {css}
        <div class="cv-container">
            <div class="cv-header">
                <h1 class="cv-name">{name}</h1>
                <div class="cv-job-title">{job_title}</div>
                {contact_row}
            </div>
            <div class="cv-body">
                <div class="cv-left">
                    <div class="cv-section-title-left">PROFILE</div>
                    <div class="cv-bio">Professionnel rigoureux avec un fort sens de l'équipe et des responsabilités. Cherche constamment à s'améliorer.</div>
                    <div class="cv-section-title-left">SKILLS</div>
                    {skills_pills}
                </div>
                <div class="cv-right">
                    {f'<div class="cv-section-title-right">PROFESSIONAL EXPERIENCE</div>{xp_html}' if experiences else ''}
                    {f'<div class="cv-section-title-right">EDUCATION</div>{edu_html}' if education else ''}
                </div>
            </div>
        </div>
        '''

    # ========== TEMPLATE 3 : MINIMALISTE EPURE ==========
    elif template_id == 'Template 3':
        css = '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;600&display=swap');
        body { margin: 0; padding: 0; background: transparent; }
        .cv-container { font-family: 'Inter', sans-serif; background: white; color: #222; padding: 3rem 4rem; min-height: 850px; }
        .cv-header { text-align: center; margin-bottom: 3rem; }
        .cv-name { font-family: 'Playfair Display', serif; font-size: 2.5rem; font-weight: 700; margin: 0 0 0.5rem 0; letter-spacing: 1px; color: #111; text-transform: uppercase;}
        .cv-job-title { font-size: 1rem; color: #555; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1rem; }
        .cv-contact-row { font-size: 0.85rem; color: #666; display: flex; justify-content: center; gap: 1.5rem; flex-wrap: wrap; }
        .cv-section-title { font-family: 'Playfair Display', serif; font-size: 1.2rem; font-weight: 700; color: #111; margin-top: 2rem; margin-bottom: 1.5rem; text-transform: uppercase; border-bottom: 1px solid #ddd; padding-bottom: 0.5rem; }
        .cv-exp-grid { display: grid; grid-template-columns: 120px 1fr; gap: 2rem; margin-bottom: 1.5rem; }
        .cv-date { font-size: 0.85rem; color: #777; line-height: 1.5; font-style: italic; }
        .cv-content-title { font-weight: 600; font-size: 1rem; color: #111; margin-bottom: 0.3rem; }
        .cv-content-desc { font-size: 0.85rem; color: #444; line-height: 1.6; }
        .cv-skills-flex { display: flex; flex-wrap: wrap; gap: 10px; }
        .cv-skill-item { font-size: 0.85rem; color: #333; padding: 2px 0; border-bottom: 1px dashed #eee; margin-right: 15px;}
        </style>
        '''
        contact_items = [f"<span>{personal[k]}</span>" for _, k in mapping_contact if personal.get(k)]
        contact_row = "<div class='cv-contact-row'>" + " | ".join(contact_items) + "</div>" if contact_items else ""
        skills_pills = "<div class='cv-skills-flex'>" + ''.join([f'<div class="cv-skill-item">{s}</div>' for s in skills]) + "</div>" if skills else '-'
        
        html_content = f'''
        {css}
        <div class="cv-container">
            <div class="cv-header">
                <h1 class="cv-name">{name}</h1>
                <div class="cv-job-title">{job_title}</div>
                {contact_row}
            </div>
            {f'<div class="cv-section-title">PROFESSIONAL EXPERIENCE</div>{xp_html}' if experiences else ''}
            {f'<div class="cv-section-title">EDUCATION</div>{edu_html}' if education else ''}
            <div class="cv-section-title">SKILLS</div>
            {skills_pills}
        </div>
        '''

    # ========== TEMPLATE 4 : CREATIF DEGRADE ==========
    elif template_id == 'Template 4':
        css = '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        body { margin: 0; padding: 0; background: transparent; }
        .cv-container { display: flex; font-family: 'Outfit', sans-serif; background: white; color: #333; min-height: 850px; border-radius: 8px; overflow: hidden; }
        .cv-sidebar { width: 35%; background: linear-gradient(135deg, #8b5cf6 0%, #f97316 100%); padding: 3rem 2rem; color: white; }
        .cv-main { width: 65%; padding: 3rem 2.5rem; background: #fafafa; }
        .cv-name { font-size: 2.5rem; font-weight: 800; margin: 0; line-height: 1.1; color: white; text-transform: uppercase; }
        .cv-job-title { font-size: 1.1rem; color: rgba(255,255,255,0.9); margin-top: 1rem; margin-bottom: 2rem; font-weight: 600; letter-spacing: 1px; }
        .cv-contact-item { margin-bottom: 1rem; font-size: 0.85rem; color: rgba(255,255,255,0.8); word-break: break-all;}
        .cv-contact-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: rgba(255,255,255,0.5); margin-bottom: 0.2rem; }
        .cv-section-title-main { font-size: 1.2rem; font-weight: 800; color: #8b5cf6; margin-bottom: 1.5rem; margin-top: 2rem; text-transform: uppercase; letter-spacing: 1px;}
        .cv-section-title-side { font-size: 1rem; font-weight: 800; color: white; margin-bottom: 1rem; margin-top: 2.5rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid rgba(255,255,255,0.2); padding-bottom: 0.5rem;}
        .cv-exp-grid { display: grid; grid-template-columns: 80px 1fr; gap: 1.5rem; margin-bottom: 1.5rem; }
        .cv-date { font-size: 0.8rem; color: #f97316; font-weight: 800; line-height: 1.4; }
        .cv-content-title { font-weight: 800; font-size: 0.95rem; color: #111; margin-bottom: 0.2rem; text-transform: uppercase;}
        .cv-content-desc { font-size: 0.85rem; color: #555; line-height: 1.5; }
        .cv-skill-item { display: inline-block; border: 1px solid rgba(255,255,255,0.4); border-radius: 20px; padding: 4px 12px; font-size: 0.8rem; margin: 0 4px 6px 0; color: white;}
        </style>
        '''
        contact_sidebar = ""
        for label, key in mapping_contact:
            if personal.get(key): contact_sidebar += f'<div class="cv-contact-item"><div class="cv-contact-label">{label}</div>{personal[key]}</div>'
        skills_pills = ''.join([f'<span class="cv-skill-item">{s}</span>' for s in skills]) if skills else '-'
        
        html_content = f'''
        {css}
        <div class="cv-container">
            <div class="cv-sidebar">
                <h1 class="cv-name">{name}</h1>
                <div class="cv-job-title">{job_title}</div>
                <div style="margin-top: 3rem;"></div>
                <div class="cv-section-title-side">CONTACT</div>
                {contact_sidebar}
                <div class="cv-section-title-side">SKILLS</div>
                {skills_pills}
            </div>
            <div class="cv-main">
                <div class="cv-section-title-main" style="margin-top: 0;">PROFILE</div>
                <div class="cv-content-desc" style="margin-bottom: 2rem;">Attiré par des défis ambitieux, je combine créativité technique et pragmatisme professionnel.</div>
                {f'<div class="cv-section-title-main">PROFESSIONAL EXPERIENCE</div>{xp_html}' if experiences else ''}
                {f'<div class="cv-section-title-main">EDUCATION</div>{edu_html}' if education else ''}
            </div>
        </div>
        '''

    # ========== TEMPLATE 5 : PREMIUM SOMBRE ==========
    elif template_id == 'Template 5':
        css = '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        body { margin: 0; padding: 0; background: transparent; }
        .cv-container { font-family: 'Outfit', sans-serif; background: #111827; color: #e5e7eb; min-height: 850px; padding: 3rem; border-radius: 8px; }
        .cv-header { border-bottom: 1px solid #374151; padding-bottom: 2rem; margin-bottom: 2rem; }
        .cv-name { font-size: 2.8rem; font-weight: 800; color: #ffffff; margin: 0 0 0.5rem 0; letter-spacing: 2px; text-transform: uppercase;}
        .cv-job-title { font-size: 1.1rem; color: #ca8a04; font-weight: 600; text-transform: uppercase; letter-spacing: 3px;}
        .cv-contact-row { display: flex; gap: 2rem; margin-top: 1.5rem; font-size: 0.85rem; color: #9ca3af; flex-wrap: wrap; }
        .cv-grid { display: grid; grid-template-columns: 1.5fr 1fr; gap: 3rem; }
        .cv-section-title { font-size: 1.1rem; font-weight: 800; color: #ca8a04; margin-bottom: 1.5rem; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1px solid #374151; padding-bottom: 0.5rem;}
        .cv-exp-grid { display: grid; grid-template-columns: 80px 1fr; gap: 1rem; margin-bottom: 1.5rem; }
        .cv-date { font-size: 0.85rem; color: #9ca3af; font-weight: 600; line-height: 1.4; }
        .cv-content-title { font-weight: 800; font-size: 0.95rem; color: #f3f4f6; margin-bottom: 0.2rem; text-transform: uppercase;}
        .cv-content-desc { font-size: 0.85rem; color: #9ca3af; line-height: 1.5; }
        .cv-skills-grid { display: flex; flex-wrap: wrap; gap: 8px;}
        .cv-skill-item { font-size: 0.85rem; color: #111827; background-color: #ca8a04; padding: 4px 10px; border-radius: 4px;}
        </style>
        '''
        contact_items = [f"<span>{personal[k]}</span>" for _, k in mapping_contact if personal.get(k)]
        contact_row = "<div class='cv-contact-row'>" + "".join([f"<div>{c}</div>" for c in contact_items]) + "</div>" if contact_items else ""
        skills_pills = "<div class='cv-skills-grid'>" + ''.join([f'<div class="cv-skill-item">{s}</div>' for s in skills]) + "</div>" if skills else '-'
        
        html_content = f'''
        {css}
        <div class="cv-container">
            <div class="cv-header">
                <h1 class="cv-name">{name}</h1>
                <div class="cv-job-title">{job_title}</div>
                {contact_row}
            </div>
            <div class="cv-grid">
                <div class="cv-main">
                    {f'<div class="cv-section-title">PROFESSIONAL EXPERIENCE</div>{xp_html}' if experiences else ''}
                    {f'<div class="cv-section-title">EDUCATION</div>{edu_html}' if education else ''}
                </div>
                <div class="cv-side">
                    <div class="cv-section-title" style="margin-top: 0;">PROFILE</div>
                    <div class="cv-content-desc" style="margin-bottom: 2rem;">Fort d'une expérience variée dans mon domaine, je suis rigoureux, orienté solutions, et en quête d'excellence.</div>
                    <div class="cv-section-title">SKILLS</div>
                    {skills_pills}
                </div>
            </div>
        </div>
        '''

    components.html(html_content, height=880, scrolling=True)
"""

with open('src/components/cv_preview.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
