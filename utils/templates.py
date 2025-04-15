
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_txt(result):
    # Estrai il testo dal dizionario (adatta alla tua struttura)
    text = result["candidates"][0]["content"]["parts"][0]["text"]

    buffer = io.BytesIO()  # crea un buffer in memoria
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica", 10)

    y = 800
    for line in text.split("\n"):
        c.drawString(50, y, line)
        y -= 15

    c.save()

    buffer.seek(0)  # torna all'inizio del buffer
    return buffer.read()  # restituisce il contenuto binario del PDF
