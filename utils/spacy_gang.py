import spacy

# Charger le modèle français
nlp = spacy.load("fr_core_news_sm")

# Exemple de texte extrait d'un PDF
text = """PAIE & RH SOLUTIONS (Pau) BULLETIN DE PAIE
12, rue Gambetta
64000 PAU
Employeur: PRH Etablissement: 00001
SIRET: 452163801 00031 NAF: 6311Z
Période du: 08/01/2024 au: 31/01/2024
BulletinN°: 001
Salarié : 00000280 CARRERE Shaney
N°S.S.: 198033324331091
Date d'entrée: 08/01/2024
Section: Support
Emploi: Data Analyst Junior
6 rue argenterie
64100 Bayonne"""

# Appliquer le modèle NER sur le texte
doc = nlp(text)

# Afficher les entités détectées
for ent in doc.ents:
    print(f"Texte: {ent.text}, Label: {ent.label_}")
