import os
import shutil
import pdfplumber
import docx

def save_upload_file(upload_file,destination):
    with open(destination,"wb") as buffer:
        shutil.copyfileobj(upload_file.file,buffer)
    upload_file.file.close()

def extract_text_auto(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return extract_pdf(path)
    elif ext in [".docx"]:
        return extract_docx(path)
    else:
        try:
            return open(path,"r",encoding= "utf-8",errors="ignore").read()
        except:
            return ""
        
def extract_pdf(path):
    text_parts = []
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text_parts.append(t)
    except:
        pass
    return "\n".join(text_parts)

def extract_docx(path):
    try:
        doc = docx.Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
    except:
        return ""
    
COMMON_SKILLS = [
    "python","fastapi","sql","javascript","react",
    "django","flask","aws","docker","ml","pytorch"
]

def simple_tag_extraction(text:str):
    text_lower = text.lower()
    tags = []
    for skill in COMMON_SKILLS:
        if skill in text_lower:
            tags.append(skill)
    return tags