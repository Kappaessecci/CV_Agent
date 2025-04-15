from fpdf import FPDF

def generate_pdf(response):
    """
    Function to generate a PDF from the response.
    """
    # Estrai il testo dalla risposta JSON
    text = response['candidates'][0]['content']['parts'][0]['text']
    
    # Crea un oggetto PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Imposta il font
    pdf.set_font("Arial", size=12)

    # Aggiungi il testo al PDF
    pdf.multi_cell(0, 10, text)

    # Salva il PDF
    pdf_file = "CV_Ottimizzato.pdf"