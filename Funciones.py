import pymupdf
from pypdf import PdfWriter

def conv_epub(a, b, c):
    a = pymupdf.open(a)
    conver = a.convert_to_pdf()
    pdf = pymupdf.open("pdf", conver)
    pdf.save(f"{c}{b}.pdf")


