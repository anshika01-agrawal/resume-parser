import re
import spacy
import pandas as pd
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

skills_dataset = pd.read_csv("data/skills.csv", header=None)
skills_list = skills_dataset[0].tolist()

def parse_resume(file_path):

    text = extract_text(file_path)

    doc = nlp(text)

    name = ""
    email = ""
    phone = ""
    found_skills = []

    # Extract name
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
            break

    # Extract email
    emails = re.findall(r'\S+@\S+', text)
    if emails:
        email = emails[0]

    # Extract phone
    phones = re.findall(r'\d{10}', text)
    if phones:
        phone = phones[0]

    # Extract skills
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return name, email, phone, found_skills