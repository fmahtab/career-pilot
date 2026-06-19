from pathlib import Path
from pypdf import PdfReader
from docx import Document

def extract_text_from_resume(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        return extract_text_from_pdf(file_path)
    
    if path.suffix.lower() == ".docx":
        return extract_text_from_docx(file_path)
    
    return ""

def extract_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text +=page.extract_text() or ""

    return text

def extract_text_from_docx(file_path: str) -> str:
    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text