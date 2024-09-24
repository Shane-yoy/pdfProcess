# Projet de Traitement de PDF

Ce projet a pour but d'extraire des informations spécifiques à partir de documents PDF, en particulier des bulletins de paie, à l'aide de l'OCR (Reconnaissance Optique de Caractères) et des expressions régulières (Regex).

## Fonctionnalités

- Conversion de fichiers PDF en images pour traitement OCR.
- Extraction d'informations clés telles que :
  - Nom de l'entreprise
  - Adresse de l'entreprise
  - Code postal et ville
  - Employeur
  - Établissement
  - SIRET
  - NAF
  - Période de paie
  - Numéro de bulletin
  - Informations sur le salarié (nom, prénom, numéro de sécurité sociale, date d'entrée, section, emploi, adresse)

## Prérequis

- Python 3.x
- Bibliothèques Python requises :
  - `pytesseract`
  - `pdf2image`
  - `opencv-python`
  - `Pillow`
  - `pandas`
  
Vous pouvez installer avec pip :

pip install pytesseract pdf2image opencv-python Pillow pandas

Assurez-vous également d'avoir Tesseract OCR installé sur votre système.

Structure du Projet

/pdfProcess
    ├── utils
    │   ├── text_extract_v2.py   # Code pour extraire le texte des PDF
    │   ├── reg_ex.py            # Code pour rechercher des motifs dans le texte extrait
    │   ├── main.py              # Script principal pour exécuter le traitement
    └── README.md                # Documentation du projet


wip
