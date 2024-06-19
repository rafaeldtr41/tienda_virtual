from pathlib import Path 
from pypdf import PdfReader, PdfWriter
import fitz
from PIL import Image

DIR = Path(__file__).resolve().parent.parent / 'Local'


def write_preview(file, name):
# crea el pdf preview
    input_pdf = PdfReader(file)
    output_pdf = PdfWriter()

    for i in range(10):

        page = input_pdf.pages[i]
        output_pdf.add_page(page)

    name = name + ".pdf"
    dir = DIR / name
    output_pdf.write(dir)
    return dir._str



def write_image(file, name):
    
    # Abre el archivo PDF
    doc = fitz.open(file)

    # Extrae la primera página
    page_number = 0
    page = doc[page_number]

    # Convierte la página a una imagen
    pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))  # Ajusta la resolución según tus necesidades
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Guarda la imagen
    dir = DIR + name + ".png"
    img.save(dir)
    return dir._str
