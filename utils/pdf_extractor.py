import PyPDF2

def extract_text_from_pdf(pdf_file):

    text = ""

    # Read PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Loop through all pages
    for page in pdf_reader.pages:

        # Extract text from page
        text += page.extract_text()

    return text