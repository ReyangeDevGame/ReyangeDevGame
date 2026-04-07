import re
from typing import Any, Dict

def parse_cv_text(text: str) -> Dict[str, Any]:
    """
    Analyse le texte brut d'un CV et extrait une structure de base par heuristique/regex.
    """
    # 0. Nettoyage global du texte (Suppression des ligatures d'icônes Material/Canva)
    icon_ligatures = [
        "keyboard_double_arrow_right", "keyboard_arrow_right", "arrow_right",
        "chevron_right", "arrow_forward", "arrow_right_alt", "done", "check", 
        "check_circle", "email", "phone", "location_on", "work", "school",
        "_arrow_right_", "_chevron_right_", "info", "file_change", "person", 
        "contact_mail", "credit_card", "description", "star", "language"
    ]
    for ligature in icon_ligatures:
        text = re.sub(rf'[_]*\b{ligature}\b[_]*', '', text, flags=re.IGNORECASE)
        text = text.replace(f"_{ligature}_", "").replace(ligature, "")
    
    # Nettoyage des éventuels résidus
    text = re.sub(r'[_]+', ' ', text)
    text = text.replace("  ", " ").strip()

    parsed_data: Dict[str, Any] = {
        "personal_info": {
            "name": "", "email": "", "phone": "",
            "address": "", "linkedin": ""
        },
        "experiences": [],
        "education": [],
        "skills": []
    }
    
    # 1. Extraction par Regex (email et téléphone)
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    if email_match:
        parsed_data["personal_info"]["email"] = email_match.group(0)
        
    phone_match = re.search(r"(?:(?:\+|00)33|0)\s*[1-9](?:[\s.-]*\d{2}){4}", text)
    if not phone_match:
        # Recherche plus large de téléphone (ex: +1 123 456 7890)
        phone_match = re.search(r"\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}", text)
        
    if phone_match:
        parsed_data["personal_info"]["phone"] = phone_match.group(0)
        
    linkedin_match = re.search(r"(?:https?://)?(?:www\.)?linkedin\.com/in/[\w\-\%]+/?", text, re.IGNORECASE)
    if linkedin_match:
        parsed_data["personal_info"]["linkedin"] = linkedin_match.group(0)
        
    # Extraction de l'adresse
    # Pour éviter d'englober email et téléphone, on les retire temporairement d'une copie du texte
    address_search_text = text
    if parsed_data["personal_info"]["email"]:
        address_search_text = address_search_text.replace(parsed_data["personal_info"]["email"], " [EMAIL_REMOVED] ")
    if parsed_data["personal_info"]["phone"]:
        address_search_text = address_search_text.replace(parsed_data["personal_info"]["phone"], " [PHONE_REMOVED] ")

    # 1. Format US/International avec Code postal 5 chiffres
    address_match = re.search(
        r"[\w\s\-\.,']+,?\s*[A-Z]{2}\s*\d{5}(?:[-\s]\d{4})?", 
        address_search_text
    )
    if not address_match:
        # 2. Code postal canadien (ex: H3B 1A1)
        address_match = re.search(
            r"[\w\s\-\.,']+,?\s*[A-Z]{2}\s*[A-Z]\d[A-Z]\s*\d[A-Z]\d",
            address_search_text
        )
    if not address_match:
        # 3. Ville, Province/Pays (ex: Montréal, Québec ou Paris, France)
        address_match = re.search(
            r"(?:Adresse\s*:?\s*)?([A-ZÀ-Ö][\w\s\-']+,\s*[A-ZÀ-Ö][\w\s\-']{2,}(?:,\s*[A-ZÀ-Ö][\w\-']+)?)",
            address_search_text
        )
    if not address_match:
        # 4. Ligne commençant par "Adresse" ou "Address"
        address_line = re.search(
            r"(?:Adresse|Address)\s*[:\-]?\s*(.+)",
            address_search_text, re.IGNORECASE
        )
        if address_line:
            parsed_data["personal_info"]["address"] = address_line.group(1).strip()
    if address_match and not parsed_data["personal_info"]["address"]:
        parsed_data["personal_info"]["address"] = address_match.group(0).strip()
        
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    
    # Extraction du nom très basique (1ère ligne ou 2ème)
    if lines:
        first_line = lines[0]
        if first_line.lower() not in ["curriculum vitae", "cv", "resume"] and len(first_line) < 50:
            parsed_data["personal_info"]["name"] = first_line
        elif len(lines) > 1 and len(lines[1]) < 50:
             parsed_data["personal_info"]["name"] = lines[1]

    # 2. Séparation par sections
    section_lines: Dict[str, list] = {
        "experiences": [],
        "education": [],
        "skills": []
    }
    current_section = None
    
    for line in lines:
        line_lower = line.lower()
        
        # Détection de section via mots-clés
        if any(line_lower.startswith(kw) or line_lower == kw for kw in ["expérience", "experience", "parcours professionnel", "work history", "emploi"]):
            current_section = "experiences"
            continue
        elif any(line_lower.startswith(kw) or line_lower == kw for kw in ["formation", "education", "diplôme", "diplome", "études", "etudes"]):
            current_section = "education"
            continue
        elif any(line_lower.startswith(kw) or line_lower == kw for kw in [
            "compétence", "competence", "skill", "aptitude",
            "outils", "technologies", "logiciels", "languages",
            "langages", "hard skills", "soft skills", "savoir-faire", "savoir faire"
        ]):
            current_section = "skills"
            continue
            
        if current_section:
            section_lines[current_section].append(line)
            
    # Pattern de date (ex: 11/2022 - Current, 2020 - 2021)
    date_range_pattern = re.compile(
        r'((?:(?:0?[1-9]|1[0-2])[/\-])?\d{4})\s*[-–—]\s*((?:(?:0?[1-9]|1[0-2])[/\-])?\d{4}|Current|Present|Présent|Aujourd\'hui|Now)', 
        re.IGNORECASE
    )
    
    # --- Parsing Expériences ---
    exp_lines = section_lines["experiences"]
    current_exp = None
    
    for i, line in enumerate(exp_lines):
        date_match = date_range_pattern.search(line)
        if date_match:
            start_date = date_match.group(1).strip()
            end_date = date_match.group(2).strip()
            
            # On retire la date de la ligne pour avoir l'entreprise
            company_str = line[:date_match.start()] + line[date_match.end():]
            company_str = re.sub(r'^[|\s,\-:]+|[|\s,\-:]+$', '', company_str).strip()
            
            # La ligne précédente est souvent le titre du poste
            title_str = exp_lines[i-1] if i > 0 else "Expérience"
            
            # Si on crée une nouvelle expérience, on enlève le `title_str` de la fin de la description précédente
            if current_exp:
                desc_lines = current_exp["description"].split("\n")
                if desc_lines and desc_lines[-1].strip() == title_str.strip():
                    desc_lines.pop()
                    current_exp["description"] = "\n".join(desc_lines).strip()
            
            current_exp = {
                "title": title_str,
                "company": company_str,
                "start": start_date,
                "end": end_date,
                "description": ""
            }
            parsed_data["experiences"].append(current_exp)
        else:
            if current_exp:
                # Accumuler dans la description
                if current_exp["description"]:
                    current_exp["description"] += "\n" + line
                else:
                    current_exp["description"] = line
            else:
                # Si on n'a pas encore de date, on crée une expérience par défaut
                if not parsed_data["experiences"]:
                    current_exp = {
                        "title": "Expérience sans date",
                        "company": "",
                        "start": "",
                        "end": "",
                        "description": line
                    }
                    parsed_data["experiences"].append(current_exp)
                else:
                    parsed_data["experiences"][-1]["description"] += "\n" + line

    # --- Parsing Formations ---
    edu_lines = section_lines["education"]
    for i, line in enumerate(edu_lines):
        date_match = date_range_pattern.search(line)
        single_year_match = re.search(r'\b(19\d{2}|20\d{2})\b', line)
        
        if date_match or single_year_match:
            year_str = date_match.group(0) if date_match else single_year_match.group(1)
            
            school_str = line.replace(year_str, "")
            school_str = re.sub(r'^[|\s,\-:]+|[|\s,\-:]+$', '', school_str).strip()
            
            degree_str = edu_lines[i-1] if i > 0 else "Diplôme"
            
            parsed_data["education"].append({
                "degree": degree_str,
                "school": school_str,
                "year": year_str
            })
            
    # Remplissage par défaut si on n'a trouvé aucune date pour les formations
    if not parsed_data["education"] and edu_lines:
        parsed_data["education"].append({
             "degree": edu_lines[0],
             "school": "",
             "year": ""
        })

    # --- Parsing Compétences ---
    skill_lines = section_lines["skills"]
    noise_words = {"de", "la", "le", "les", "et", "ou", "un", "une", "des", "du", "en", "à", "au", "par", "pour"}
    
    # Noms ou emails potentiels déjà extraits pour ne pas les remettre en compétences
    name_extracted = parsed_data["personal_info"]["name"].lower().replace(" ", "")

    for line in skill_lines:
        # Puces étendues : ajout de \u25cf (●), \u25a0 (■), etc.
        parts = re.split(r'[,|\u2022/;\u00b7\u2013\u2014\t\u25cf\u25a0\u25aa]+', line)
        for part in parts:
            # Nettoyage des puces restantes au début ET à la fin
            skill = re.sub(r'^[\s\-\*\>\u2022\u25cf\u25aa\u2013]+', '', part)
            skill = re.sub(r'[\s\-\*\>\u2022\u25cf\u25aa\u2013]+$', '', skill).strip()
            
            if not skill or len(skill) < 2 or skill.lower() in noise_words:
                continue
                
            # Filtre : Trop long (plus de 40 caractères)
            if len(skill) > 40:
                continue
                
            # Filtre : C'est une phrase (plus de 4 mots)
            if len(skill.split()) > 4:
                continue
                
            # Filtre : Ressemble à un email
            if "@" in skill or re.search(r"[\w\.-]+@[\w\.-]+\.\w+", skill):
                continue
                
            # Filtre : Ressemble à un téléphone
            if re.search(r"\d{4,}", skill) or re.search(r"(?:\+?\d{1,3}[\s-]?)?(?:\d{2,3}[\s-]?){3,}", skill):
                continue
                
            # Filtre : Ressemble au nom de l'utilisateur (ex: ReyanneN'Guessan collé)
            skill_clean = skill.lower().replace(" ", "")
            if name_extracted and (name_extracted in skill_clean or skill_clean in name_extracted):
                continue

            parsed_data["skills"].append(skill)

    # Si rien n'est trouvé après filtrage
    if not parsed_data["skills"] and skill_lines:
        for line in skill_lines:
            skill = line.strip()
            if skill and len(skill.split()) <= 4 and "@" not in skill and len(skill) < 40:
                parsed_data["skills"].append(skill)

    if parsed_data["skills"]:
        parsed_data["skills"] = list(dict.fromkeys(parsed_data["skills"]))

    return parsed_data
