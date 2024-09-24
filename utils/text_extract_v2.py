import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_path):
    """
    Applique l'OCR sur chaque page d'un PDF converti en images.

    Parameters:
    pdf_path (str): Chemin du fichier PDF.

    Returns:
    list: Liste des textes extraits de chaque page.
    """
    pages = convert_from_path(pdf_path)
    extracted_texts = []

    for page_number, page in enumerate(pages):
        text = pytesseract.image_to_string(page)
        extracted_texts.append(text)
        print(f"---  Page number {page_number + 1} ---")
        print(text)
        print("\n")

    return extracted_texts
