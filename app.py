
# import streamlit as st
# import os

# from scripts.pdf_processor import extract_text_from_pdf
# from scripts.embedding_store import store_embeddings, check_existing_embeddings
# from scripts.query_handler import generate_answer_with_visualization

# st.title("📄 PDF Chatbot with Data Visualization 📊")

# # Upload PDF Section
# uploaded_files = st.file_uploader("Upload one or more PDFs", type=["pdf"], accept_multiple_files=True)

# # Check if PDFs are already processed
# if not check_existing_embeddings():
#     if uploaded_files:
#         all_text = ""
        
#         for uploaded_file in uploaded_files:
#             file_path = os.path.join("uploads", uploaded_file.name)
#             with open(file_path, "wb") as f:
#                 f.write(uploaded_file.read())

#             pdf_text = extract_text_from_pdf(file_path)
#             all_text += pdf_text + "\n"

#         # Process and store embeddings
#         store_embeddings(all_text.split("\n"))  
#         st.success("✅ PDFs processed! You can now ask questions.")
#     else:
#         st.warning("⚠️ Please upload at least one PDF before proceeding.")
#         st.stop()  # Prevent further execution if no PDFs

# # Query Input Section
# query = st.text_input("Ask a question:")

# if query:
#     answer, temp_file = generate_answer_with_visualization(query)

#     # Display textual answer
#     st.write("### 📝 Answer:")
#     st.write(answer)

#     # ✅ Check if temp file exists before executing it
#     if os.path.exists(temp_file):
#         st.write("### 📊 Visualization:")
#         exec(open(temp_file).read())  # Dynamically execute Matplotlib code
#     else:
#         st.write("No visualization available for this query.")
# import streamlit as st
# import os
# from scripts.pdf_processor import extract_text_from_pdf
# from scripts.embedding_store import store_embeddings, check_existing_embeddings
# from scripts.query_handler import generate_answer_with_visualization

# st.title("PDF Chatbot with Data Visualization")

# uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# if uploaded_file:
#     pdf_name = uploaded_file.name  # Get the uploaded file name
#     pdf_path = os.path.join("uploaded_pdfs", pdf_name)  # Define save path

#     # Save PDF file
#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.read())

#     # Extract text
#     text = extract_text_from_pdf(pdf_path)
#     text_chunks = text.split("\n")  # Split into chunks

#     # ✅ Check if embeddings exist before storing
#     if not check_existing_embeddings(pdf_name):
#         store_embeddings(text_chunks, pdf_name)

#     st.success(f"✅ {pdf_name} processed successfully!")

# # User input query
# query = st.text_input("Ask a question:")

# if query:
#     answer, temp_file = generate_answer_with_visualization(query)

#     # Display textual answer
#     st.write("### Answer:")
#     st.write(answer)

#     # ✅ Check if temp file exists before executing it
#     if os.path.exists(temp_file):
#         st.write("### Visualization:")
#         exec(open(temp_file).read())  # Dynamically execute Matplotlib code
#     else:
#         st.write("No visualization available for this query.")
import streamlit as st
import os
import sys

# Ensure Streamlit finds the 'scripts' directory
sys.path.append(os.path.abspath("scripts"))

from scripts.query_handler import generate_answer_with_visualization
from scripts.embedding_store import check_existing_embeddings

st.title("PDF Chatbot with Data Visualization")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    pdf_name = uploaded_file.name
    
    # Check if embeddings exist for this PDF
    if not check_existing_embeddings(pdf_name):
        st.write(f"Generating embeddings for: {pdf_name}")
        from scripts.pdf_processor import extract_text_from_pdf
        from scripts.embedding_store import store_embeddings

        pdf_text = extract_text_from_pdf(uploaded_file)
        text_chunks = pdf_text.split("\n\n")  # Simple chunking
        store_embeddings(text_chunks, pdf_name)
    else:
        st.write(f"Embeddings already exist for: {pdf_name}")

# User input query
query = st.text_input("Ask a question:")

if query:
    answer, temp_file = generate_answer_with_visualization(query)

    # Display textual answer
    st.write("### Answer:")
    st.write(answer)

    # ✅ Check if temp file exists before executing it
    if os.path.exists(temp_file):
        st.write("### Visualization:")
        exec(open(temp_file).read())  # Dynamically execute Matplotlib code
    else:
        st.write("No visualization available for this query.")
