import pdfplumber
import docx
import email
import io

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_eml(file):
    msg = email.message_from_bytes(file.read())
    return msg.get_payload(decode=True).decode(errors='ignore') if msg else ""

def load_documents(files):
    docs = []
    for f in files:
        if f.name.endswith('.pdf'):
            text = extract_text_from_pdf(f)
        elif f.name.endswith('.docx'):
            text = extract_text_from_docx(f)
        elif f.name.endswith('.eml'):
            text = extract_text_from_eml(f)
        else:
            continue
        chunks = [text[i:i+300] for i in range(0, len(text), 300)]
        docs.append({'name': f.name, 'text': text, 'chunks': chunks})
    return docs
