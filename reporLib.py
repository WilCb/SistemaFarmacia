from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

cnv = canvas.Canvas('PDFlab.pdf')

rows = 10

for row in rows:
    cnv.drawString(rows, 450, 'teste')
cnv.save()