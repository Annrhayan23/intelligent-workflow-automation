"""Document processing utilities with offline heuristics."""
import os
import re
from typing import Dict, List

# Optional heavy deps
try:
    import pytesseract
    from PIL import Image
except Exception:
    pytesseract = None
    Image = None

try:
    import fitz
except Exception:
    fitz = None

def extract_text_from_image(image_path: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    if pytesseract is None or Image is None:
        raise RuntimeError('pytesseract or PIL not installed. Install them to extract text from images.')
    return pytesseract.image_to_string(Image.open(image_path))

def extract_text_from_pdf(pdf_path: str) -> str:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    if fitz is None:
        raise RuntimeError('PyMuPDF (fitz) is not installed. Install it to extract text from PDFs.')
    doc = fitz.open(pdf_path)
    text = []
    for page in doc:
        text.append(page.get_text())
    doc.close()
    return "\n".join(text)

def extract_entities(text: str) -> Dict[str, List[str]]:
    entities = {'MONEY': [], 'DATE': [], 'ORG': [], 'EMAIL': [], 'PHONE': [], 'MISC': []}
    if not text:
        return entities

    money_re = re.compile(r'(?:\$|₹)?\s?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?')
    entities['MONEY'] = list(set(money_re.findall(text)))

    date_re = re.compile(r'\b(?:\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{2,4})', re.I)
    entities['DATE'] = list(set([m for m in date_re.findall(text) if m.strip()]))

    email_re = re.compile(r'[\w\.-]+@[\w\.-]+')
    entities['EMAIL'] = list(set(email_re.findall(text)))

    phone_re = re.compile(r'\b\+?\d[\d\-\s]{7,}\d\b')
    entities['PHONE'] = list(set(phone_re.findall(text)))

    org_re = re.compile(r'\b([A-Z][a-zA-Z0-9&]+(?:\s+[A-Z][a-zA-Z0-9&]+){0,3})\b')
    orgs = org_re.findall(text)
    orgs_filtered = [o for o in orgs if len(o) > 2 and not o.isupper()]
    entities['ORG'] = list(set(orgs_filtered))

    # MISC heuristics: keywords
    misc_keywords = ['termination', 'invoice', 'due', 'overdue', 'confidential']
    lower = text.lower()
    for kw in misc_keywords:
        if kw in lower:
            entities['MISC'].append(kw)

    return entities
