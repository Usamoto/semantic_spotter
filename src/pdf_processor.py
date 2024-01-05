import pdfplumber

def read_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=500):
    # Teilt den Text in kleinere Abschnitte
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
