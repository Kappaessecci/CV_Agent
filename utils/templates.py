
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_txt(result):
    try:
        contents = result.get("contents", [])
        if not contents:
            return "⚠️ Nessun contenuto restituito dall'API."

        parts = contents[0].get("parts", [])
        if not parts:
            return "⚠️ Nessuna parte trovata nei contenuti."

        text = parts[0].get("text", "")
        if not text:
            return "⚠️ Testo vuoto."
        buffer = io.BytesIO()  # crea un buffer in memoria
        c = canvas.Canvas(buffer, pagesize=A4)
        c.setFont("Helvetica", 10)

        y = 800
        for line in text:
            c.drawString(50, y, line)
            y -= 15

        c.save()

        buffer.seek(0)  # torna all'inizio del buffer
        return buffer.read()  # restituisce il contenuto binario del PDF

    

    except Exception as e:
        return f"❌ Errore imprevisto: {e}"

   