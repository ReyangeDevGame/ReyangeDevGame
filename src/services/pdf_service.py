import pypdf

def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extrait le texte d'un fichier PDF uploadé via Streamlit.
    """
    try:
        reader = pypdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
                
        if not text.strip():
            raise ValueError("Le PDF ne contient pas de texte lisible (possiblement scanné sans OCR).")
            
        return text
    except Exception as e:
        if isinstance(e, ValueError):
            raise e
        raise ValueError(f"Erreur lors de la lecture du PDF: {str(e)}")
