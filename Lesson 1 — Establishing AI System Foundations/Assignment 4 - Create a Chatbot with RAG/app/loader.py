import os
import docx
from pypdf import PdfReader

def read_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(path):
    text = ""

    reader = PdfReader(path)

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def read_docx(path):
    doc = docx.Document(path)

    return "\n".join(
        [p.text for p in doc.paragraphs]
    )

def load_document(path):

    ext = os.path.splitext(path)[1]

    if ext == ".txt":
        return read_txt(path)

    elif ext == ".pdf":
        return read_pdf(path)

    elif ext == ".docx":
        return read_docx(path)

    else:
        raise Exception("Unsupported file")