from pathlib import Path 
from pypdf import PdfReader, PdfWriter
import fitz
from PIL import Image




def write_preview(path, dirpath, value):
# crea el pdf preview
    input_pdf = PdfReader(path)
    output_pdf = PdfWriter()

    for i in range(10):

        page = input_pdf.pages[i]
        output_pdf.add_page(page)

    dir = dirpath + value + ".pdf"
    output_pdf.write(dir)
    return dir



def write_image(dir, dirpath, name):
    
    # Abre el archivo PDF
    doc = fitz.open(dir)

    # Extrae la primera página
    page_number = 0
    page = doc[page_number]

    # Convierte la página a una imagen
    pix = page.get_pixmap(matrix=fitz.Matrix(300/72, 300/72))  # Ajusta la resolución según tus necesidades
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Guarda la imagen
    dir = dirpath + name + ".png"
    img.save(dir)
    return dir

    

