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
  
Vous pouvez installer ces dépendances avec pip :

```bash
pip install pytesseract pdf2image opencv-python Pillow pandas
Assurez-vous également d'avoir Tesseract OCR installé sur votre système. Vous pouvez le télécharger ici et suivre les instructions d'installation pour votre plateforme.

Structure du Projet

/pdfProcess
    ├── utils
    │   ├── text_extract_v2.py  # Code pour extraire le texte des PDF
    │   ├── reg_ex.py            # Code pour rechercher des motifs dans le texte extrait
    │   ├── main.py                  # Script principal pour exécuter le traitement
    └── README.md                # Documentation du projet


Utilisation
Convertir le PDF en images et extraire le texte : Le fichier text_extract_v2.py contient une fonction qui applique l'OCR sur chaque page d'un PDF converti en images.

Rechercher des motifs dans le texte extrait : Le fichier reg_ex.py contient des expressions régulières pour extraire les informations clés des textes extraits.

Exécuter le script principal : Exécutez le fichier main.py pour lancer le traitement complet.

bash
Copier le code
python main.py
Exemple de Sortie
Après l'exécution, les informations extraites seront affichées et stockées dans un DataFrame, ce qui facilite leur manipulation ultérieure. Voici un exemple de ce à quoi pourrait ressembler la sortie :

Nom de l'entreprise: PAIE & RH SOLUTIONS
Adresse de l'entreprise: 12, rue Gambetta
Code postal et ville: 64000 PAU
Employeur: PRH
Établissement: 00001
SIRET: 45216380100031
NAF: 6311Z
Période du: ('08/01/2024', '31/01/2024')
Bulletin numéro: 001
Nom du salarié: CARRERE
Prénom du salarié: Shaney
Numéro de sécurité sociale: 198033324331091
Date d'entrée: 08/01/2024
Section: Support
Emploi: Data Analyst Junior
Adresse de l'employé: 6 rue argenterie
Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à ouvrir une issue ou soumettre une pull request.

License
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus de détails.




