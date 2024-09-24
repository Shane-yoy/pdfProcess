from text_extract_v2 import extract_text_from_pdf
from reg_ex import search_patterns

def main():

    pdf_path = '01.pdf'  

    texts = extract_text_from_pdf(pdf_path)  
    #search_patterns(texts)

if __name__ == "__main__":
    main()
