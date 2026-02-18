import pdfplumber

def extract_text_from_pdf(uploaded_file):

    with pdfplumber.open(uploaded_file) as pdf:

        all_text = []

        for page in pdf.pages:

            all_text.append(page.extract_text())

    return "\n".join(all_text)