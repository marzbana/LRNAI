from docx import Document
from reportlab.pdfgen import canvas

    
class Doc:
    def __init__(self):
        pass

    def create_pdf(self, text, filename):
        c = canvas.Canvas(filename)
        c.drawString(100, 750, text)
        c.save()
    
    def create_docx(self, text, filename):
        doc = Document()
        doc.add_paragraph(text)
        doc.save(filename)

