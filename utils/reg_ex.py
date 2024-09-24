import re

def search_patterns(texts):
    """
    Recherche des motifs spécifiques dans le texte extrait.

    Parameters:
    texts (list): Liste des textes extraits de chaque page.
    """
    
    # check tous les nombres : int
    """for i, text in enumerate(texts):
        print(f"---  Patterns in Page {i + 1} ---")
        # Exemple de recherche d'un motif
        matches = re.findall(r'\b\d+\b', text)  # Par exemple, tous les nombres
        print("Matches found:", matches)
        print("\n")"""


    

    # 1. Nom de l'entreprise
    company_pattern = r'^(.*?)(?=\s\(.*?\)\sBULLETIN DE PAIE)'
    company = re.search(company_pattern, text, re.MULTILINE)
    company_name = company.group(0).strip() if company else None

    # 2. Adresse de l'entreprise
    address_pattern = r'^\d{1,3}.*?(\n\d{5}\s\w+)?'
    address = re.search(address_pattern, text, re.MULTILINE)
    address_entry = address.group(0).strip() if address else None

    # 3. Code postal et ville
    postal_city_pattern = r'\b\d{5}\s\w+\b'
    postal_city = re.search(postal_city_pattern, text)
    postal_city_entry = postal_city.group(0).strip() if postal_city else None

    # 4. Employeur
    employer_pattern = r'Employeur:\s*(.*?)(?=\sEtablissement:)'
    employer = re.search(employer_pattern, text)
    employer_name = employer.group(1).strip() if employer else None

    # 5. Établissement
    establishment_pattern = r'Etablissement:\s*(\d+)'
    establishment = re.search(establishment_pattern, text)
    establishment_number = establishment.group(1).strip() if establishment else None

    # 6. SIRET
    siret_pattern = r'SIRET:\s*(\d{14})'
    siret = re.search(siret_pattern, text)
    siret_number = siret.group(1).strip() if siret else None

    # 7. NAF
    naf_pattern = r'NAF:\s*(\w{5})'
    naf = re.search(naf_pattern, text)
    naf_code = naf.group(1).strip() if naf else None

    # 8. Période du
    period_pattern = r'Période du:\s*(\d{2}/\d{2}/\d{4})\s*au:\s*(\d{2}/\d{2}/\d{4})'
    period = re.search(period_pattern, text)
    period_start = period.group(1).strip() if period else None
    period_end = period.group(2).strip() if period else None

    # 9. Bulletin numéro
    bulletin_number_pattern = r'BulletinN°:\s*(\d+)'
    bulletin_number = re.search(bulletin_number_pattern, text)
    bulletin_num = bulletin_number.group(1).strip() if bulletin_number else None

    # 10. Nom et prénom du salarié
    employee_pattern = r'Salarié :\s*(\d+)\s+(\w+)\s+(\w+)'
    employee = re.search(employee_pattern, text)
    employee_id = employee.group(1).strip() if employee else None
    employee_last_name = employee.group(2).strip() if employee else None
    employee_first_name = employee.group(3).strip() if employee else None

    # 11. Numéro de sécurité sociale
    ssn_pattern = r'N°S\.S\.: (\d{15})'
    ssn = re.search(ssn_pattern, text)
    ssn_number = ssn.group(1).strip() if ssn else None

    # 12. Date d'entrée
    entry_date_pattern = r'Date d\'entrée:\s*(\d{2}/\d{2}/\d{4})'
    entry_date = re.search(entry_date_pattern, text)
    entry_date_entry = entry_date.group(1).strip() if entry_date else None

    # 13. Section
    section_pattern = r'Section:\s*(.*)'
    section = re.search(section_pattern, text)
    section_entry = section.group(1).strip() if section else None

    # 14. Emploi
    job_pattern = r'Emploi:\s*(.*)'
    job = re.search(job_pattern, text)
    job_entry = job.group(1).strip() if job else None

    # 15. Adresse de l'employé
    employee_address_pattern = r'^\d{1,3}.*?(\n\d{5}\s\w+)?'
    employee_address = re.search(employee_address_pattern, text)
    employee_address_entry = employee_address.group(0).strip() if employee_address else None

    # Afficher les résultats
    results = {
        "Nom de l'entreprise": company_name,
        "Adresse de l'entreprise": address_entry,
        "Code postal et ville": postal_city_entry,
        "Employeur": employer_name,
        "Établissement": establishment_number,
        "SIRET": siret_number,
        "NAF": naf_code,
        "Période du": (period_start, period_end),
        "Bulletin numéro": bulletin_num,
        "Nom du salarié": employee_last_name,
        "Prénom du salarié": employee_first_name,
        "Numéro de sécurité sociale": ssn_number,
        "Date d'entrée": entry_date_entry,
        "Section": section_entry,
        "Emploi": job_entry,
        "Adresse de l'employé": employee_address_entry,
    }

    for key, value in results.items():
        print(f"{key}: {value}")
