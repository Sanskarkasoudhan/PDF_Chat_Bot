# import fitz  

# def extract_text_from_pdf(pdf_path):
#     """Extracts text from a PDF file."""
#     doc = fitz.open(pdf_path)
#     text = "\n".join([page.get_text("text") for page in doc])
#     return text

# import fitz  

# def extract_text_from_pdf(uploaded_file):
#     """Extracts text from an uploaded PDF file."""
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = "\n".join([page.get_text("text") for page in doc])
#     return text
import fitz  

def extract_text_from_pdf(uploaded_file):
    """Extracts text from an uploaded PDF file."""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = "\n".join([page.get_text("text") for page in doc])
    return text
