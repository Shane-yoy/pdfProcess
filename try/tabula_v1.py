import tabula
import pandas as pd

# Extraire le tableau du fichier PDF et le convertir en DataFrame
df = tabula.read_pdf('01.pdf', pages=1, multiple_tables=True)

# Afficher les résultats
print(df)
                              