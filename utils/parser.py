import pdfplumber

def extract_text(pdf_path):
    """
    Extract text from a PDF file using pdfplumber.
    
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a string.
    """
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text.strip()
