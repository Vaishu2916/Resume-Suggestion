import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text

def extract_entities(text):
    doc = nlp(text)
    skills = []
    education = []
    experience = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            education.append(ent.text)
        elif ent.label_ == "DATE":
            experience.append(ent.text)
        elif ent.label_ in ["SKILL", "PRODUCT"]:
            skills.append(ent.text)
    
    return {
        "education": list(set(education)),
        "experience": list(set(experience)),
        "skills": list(set(skills))
    }

def suggest_improvements(entities):
    suggestions = []
    
    if not entities["skills"]:
        suggestions.append("Add more specific technical skills.")
    if not entities["education"]:
        suggestions.append("Include your educational background clearly.")
    if len(entities["experience"]) < 2:
        suggestions.append("List more job experience or internship details.")
    
    return suggestions
