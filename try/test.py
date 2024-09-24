import pytesseract
from pdf2image import convert_from_path
import cv2
from PIL import Image

# Spécifier le chemin vers l'exécutable de Tesseract si nécessaire
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Convertir le PDF en images (chaque page sera une image)
pages = convert_from_path('01.pdf')

# Parcourir chaque page convertie en image
for page_number, page_image in enumerate(pages):
    # Sauvegarder l'image temporairement (ou la manipuler directement en mémoire)
    page_image.save(f'page_{page_number}.jpg', 'JPEG')

    # Charger l'image pour OpenCV
    img = cv2.imread(f'page_{page_number}.jpg')

    # Appliquer l'OCR avec Tesseract et récupérer les données avec position
    ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    # Parcourir les données extraites et afficher la position et le texte
    for i in range(len(ocr_data['text'])):
        if int(ocr_data['conf'][i]) > 0:  # Exclure les textes non reconnus ou avec faible confiance
            x, y, w, h = ocr_data['left'][i], ocr_data['top'][i], ocr_data['width'][i], ocr_data['height'][i]
            text = ocr_data['text'][i]
            print(f"Page {page_number + 1}, Texte: '{text}', Position: ({x}, {y}), Taille: ({w}x{h})")
