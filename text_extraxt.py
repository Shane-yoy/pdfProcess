import pytesseract
from pdf2image import convert_from_path

# Convertir le PDF en images (chaque page sera une image)
pages = convert_from_path('01.pdf')

def tess_(pages):
    for page_number, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        print(f"---  Page number {page_number + 1} ---")
        print(text)
        print("\n")
    return text

tess_(pages)