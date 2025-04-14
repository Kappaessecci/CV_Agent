
def generate_pdf(response):
    """
    Function to generate a PDF from the response.
    """
    # Assuming response is a dictionary with 'content' key containing the text
    content = response.get('content', '')
    
    # Create a PDF file from the content
    pdf_file = f"CV_Ottimizzato.pdf"
    
    # Here you would use a library like FPDF or ReportLab to create the PDF
    # For simplicity, let's just write the content to a text file for now
    with open(pdf_file, 'w') as f:
        f.write(content)
    
    return pdf_file