import re
from typing import Any, Dict

def parse_cv_text(text: str) -> Dict[str, Any]:
    """
    Analyse le texte brut d'un CV et extrait une structure de base par heuristique/regex.
    """
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
        elif any(line_lower.startswith(kw) or line_lower == kw for kw in ["compétence", "competence", "skill", "aptitude"]):
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
    for line in skill_lines:
        skills = [s.strip() for s in re.split(r'[,|•\-]', line) if s.strip()]
        parsed_data["skills"].extend(skills)
        
    # Déduplication
    if parsed_data["skills"]:
        parsed_data["skills"] = list(dict.fromkeys(parsed_data["skills"]))
        
    return parsed_data
