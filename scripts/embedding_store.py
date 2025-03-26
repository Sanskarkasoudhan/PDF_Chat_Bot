# # # import chromadb
# # # from google.generativeai import configure, embed_content
# # # from config import GEMINI_API_KEY, CHROMA_DB_PATH

# # # # Configure Gemini API
# # # configure(api_key=GEMINI_API_KEY)

# # # # Initialize ChromaDB
# # # chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# # # collection = chroma_client.get_or_create_collection("pdf_embeddings")

# # # def delete_existing_embeddings(pdf_name):
# # #     """Deletes embeddings associated with a specific PDF to avoid duplicates."""
# # #     existing_data = collection.get()
# # #     existing_ids = [doc_id for doc_id in existing_data["ids"] if pdf_name in doc_id]

# # #     if existing_ids:
# # #         collection.delete(existing_ids)
# # #         print(f"🗑 Deleted existing embeddings for {pdf_name}")

# # # def store_embeddings(text_chunks, pdf_name, chunk_size=1000):
# # #     """Stores embeddings of text chunks in ChromaDB while avoiding duplicates."""
# # #     combined_chunks = []
# # #     current_chunk = ""

# # #     for chunk in text_chunks:
# # #         if len(current_chunk) + len(chunk) <= chunk_size:
# # #             current_chunk += " " + chunk if current_chunk else chunk
# # #         else:
# # #             combined_chunks.append(current_chunk)
# # #             current_chunk = chunk

# # #     if current_chunk:
# # #         combined_chunks.append(current_chunk)

# # #     # Get existing IDs to avoid duplicates
# # #     existing_data = collection.get()
# # #     existing_ids = set(existing_data["ids"]) if existing_data else set()

# # #     # Delete old embeddings before inserting new ones
# # #     delete_existing_embeddings(pdf_name)

# # #     for idx, chunk in enumerate(combined_chunks):
# # #         embedding_id = f"{pdf_name}_{idx}"

# # #         if embedding_id in existing_ids:
# # #             print(f"⚠️ Skipping existing embedding ID: {embedding_id}")
# # #             continue

# # #         embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
# # #         collection.add(ids=[embedding_id], embeddings=[embedding], metadatas=[{"text": chunk}])

# # # def retrieve_relevant_text(query):
# # #     """Retrieves relevant text chunks from ChromaDB based on query."""
# # #     query_embedding = embed_content(model="models/embedding-001", content=query)["embedding"]
# # #     results = collection.query(query_embeddings=[query_embedding], n_results=3)
# # #     return [r["text"] for r in results["metadatas"][0]]

# # # def check_existing_embeddings():
# # #     """Checks if embeddings already exist in ChromaDB."""
# # #     return collection.count() > 0  # Returns True if embeddings exist

# # # import chromadb
# # # from google.generativeai import configure, embed_content
# # # from config import GEMINI_API_KEY, CHROMA_DB_PATH

# # # configure(api_key=GEMINI_API_KEY)

# # # chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# # # collection = chroma_client.get_or_create_collection("pdf_embeddings")

# # # def store_embeddings(text_chunks, chunk_size=1000):
# # #     """Stores embeddings for multiple PDFs in ChromaDB."""
# # #     combined_chunks = []
# # #     current_chunk = ""

# # #     for chunk in text_chunks:
# # #         if len(current_chunk) + len(chunk) <= chunk_size:
# # #             current_chunk += " " + chunk if current_chunk else chunk
# # #         else:
# # #             combined_chunks.append(current_chunk)
# # #             current_chunk = chunk

# # #     if current_chunk:
# # #         combined_chunks.append(current_chunk)

# # #     for idx, chunk in enumerate(combined_chunks):
# # #         embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
# # #         collection.add(ids=[str(idx)], embeddings=[embedding], metadatas=[{"text": chunk}])

# # # def retrieve_relevant_text(query):
# # #     """Retrieves relevant text chunks from multiple PDFs."""
# # #     query_embedding = embed_content(model="models/embedding-001", content=query)["embedding"]
# # #     results = collection.query(query_embeddings=[query_embedding], n_results=3)
# # #     return [r["text"] for r in results["metadatas"][0]]

# # # def check_existing_embeddings():
# # #     """Checks if embeddings already exist in ChromaDB."""
# # #     return collection.count() > 0  # Returns True if embeddings exist
# # import chromadb
# # import os
# # from google.generativeai import configure, embed_content
# # from config import GEMINI_API_KEY, CHROMA_DB_PATH

# # configure(api_key=GEMINI_API_KEY)

# # chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# # collection = chroma_client.get_or_create_collection("pdf_embeddings")

# # def store_embeddings(text_chunks, chunk_size=1000):
# #     """Stores embeddings for multiple PDFs in ChromaDB, only if not already stored."""
    
# #     # If embeddings already exist, skip the process
# #     if check_existing_embeddings():
# #         print("Embeddings already exist. Skipping embedding process.")
# #         return
    
# #     combined_chunks = []
# #     current_chunk = ""

# #     for chunk in text_chunks:
# #         if len(current_chunk) + len(chunk) <= chunk_size:
# #             current_chunk += " " + chunk if current_chunk else chunk
# #         else:
# #             combined_chunks.append(current_chunk)
# #             current_chunk = chunk

# #     if current_chunk:
# #         combined_chunks.append(current_chunk)

# #     for idx, chunk in enumerate(combined_chunks):
# #         embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
# #         collection.add(ids=[str(idx)], embeddings=[embedding], metadatas=[{"text": chunk}])

# # def retrieve_relevant_text(query):
# #     """Retrieves relevant text chunks from multiple PDFs."""
# #     query_embedding = embed_content(model="models/embedding-001", content=query)["embedding"]
# #     results = collection.query(query_embeddings=[query_embedding], n_results=3)
# #     return [r["text"] for r in results["metadatas"][0]]

# # def check_existing_embeddings():
# #     """Checks if embeddings already exist in ChromaDB."""
# #     return collection.count() > 0  # Returns True if embeddings exist
# import chromadb
# import os
# from google.generativeai import configure, embed_content
# from config import GEMINI_API_KEY, CHROMA_DB_PATH

# configure(api_key=GEMINI_API_KEY)

# chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# collection = chroma_client.get_or_create_collection("pdf_embeddings")

# def check_existing_embeddings(pdf_name):
#     """Checks if embeddings for a specific PDF already exist in ChromaDB."""
#     existing_data = collection.get()
#     existing_ids = {doc_id for doc_id in existing_data["ids"] if pdf_name in doc_id}
#     return len(existing_ids) > 0  # Returns True if embeddings exist for the PDF

# def store_embeddings(text_chunks, pdf_name, chunk_size=1000):
#     """Stores embeddings for a PDF only if they don’t already exist in ChromaDB."""
    
#     if check_existing_embeddings(pdf_name):
#         print(f"✅ Embeddings for {pdf_name} already exist. Skipping embedding process.")
#         return
    
#     combined_chunks = []
#     current_chunk = ""

#     for chunk in text_chunks:
#         if len(current_chunk) + len(chunk) <= chunk_size:
#             current_chunk += " " + chunk if current_chunk else chunk
#         else:
#             combined_chunks.append(current_chunk)
#             current_chunk = chunk

#     if current_chunk:
#         combined_chunks.append(current_chunk)

#     for idx, chunk in enumerate(combined_chunks):
#         embedding_id = f"{pdf_name}_{idx}"
#         embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
#         collection.add(ids=[embedding_id], embeddings=[embedding], metadatas=[{"text": chunk}])

#     print(f"✅ Successfully stored embeddings for {pdf_name}")

# def retrieve_relevant_text(query):
#     """Retrieves relevant text chunks from multiple PDFs."""
#     query_embedding = embed_content(model="models/embedding-001", content=query)["embedding"]
#     results = collection.query(query_embeddings=[query_embedding], n_results=3)
# #     return [r["text"] for r in results["metadatas"][0]]
# import chromadb
# from google.generativeai import configure, embed_content
# from config import GEMINI_API_KEY, CHROMA_DB_PATH

# configure(api_key=GEMINI_API_KEY)

# chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# collection = chroma_client.get_or_create_collection("pdf_embeddings")

# def check_existing_embeddings(pdf_name):
#     """Checks if embeddings for a specific PDF already exist in ChromaDB."""
#     existing_data = collection.get()
#     existing_ids = {doc_id.split("_")[0] for doc_id in existing_data["ids"]}

#     return pdf_name in existing_ids  # ✅ Returns True if the PDF is already embedded

# def store_embeddings(text_chunks, pdf_name, chunk_size=1000):
#     """Stores embeddings for multiple PDFs in ChromaDB, only if not already stored."""
    
#     if check_existing_embeddings(pdf_name):
#         print(f"✅ Embeddings already exist for {pdf_name}. Skipping embedding process.")
#         return
    
#     combined_chunks = []
#     current_chunk = ""

#     for chunk in text_chunks:
#         if len(current_chunk) + len(chunk) <= chunk_size:
#             current_chunk += " " + chunk if current_chunk else chunk
#         else:
#             combined_chunks.append(current_chunk)
#             current_chunk = chunk

#     if current_chunk:
#         combined_chunks.append(current_chunk)

#     for idx, chunk in enumerate(combined_chunks):
#         embedding_id = f"{pdf_name}_{idx}"  # Ensure unique ID for each PDF
#         embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
#         collection.add(ids=[embedding_id], embeddings=[embedding], metadatas=[{"text": chunk}])

#     print(f"✅ Embeddings stored successfully for {pdf_name}.")

# def retrieve_relevant_text(query):
#     """Retrieves relevant text chunks from multiple PDFs."""
#     query_embedding = embed_content(model="models/embedding-001", content=query)["embedding"]
#     results = collection.query(query_embeddings=[query_embedding], n_results=3)
#     return [r["text"] for r in results["metadatas"][0]]
# import chromadb
# from google.generativeai import configure, embed_content
# from config import GEMINI_API_KEY, CHROMA_DB_PATH

# configure(api_key=GEMINI_API_KEY)

# chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
# collection = chroma_client.get_or_create_collection("pdf_embeddings")

# def check_existing_embeddings(pdf_name):
#     """Checks if embeddings for a specific PDF already exist in ChromaDB."""
#     existing_data = collection.get()
#     existing_ids = {doc_id for doc_id in existing_data["ids"] if pdf_name in doc_id}
#     return existing_ids  # ✅ Returns a set of existing embedding IDs for the given PDF

# def store_embeddings(text_chunks, pdf_name, chunk_size=1000):
#     """Stores embeddings for multiple PDFs in ChromaDB, avoiding duplicate chunk embeddings."""
    
#     existing_ids = check_existing_embeddings(pdf_name)  # Get existing chunk IDs
    
#     combined_chunks = []
#     current_chunk = ""

#     for chunk in text_chunks:
#         if len(current_chunk) + len(chunk) <= chunk_size:
#             current_chunk += " " + chunk if current_chunk else chunk
#         else:
#             combined_chunks.append(current_chunk)
#             current_chunk = chunk

#     if current_chunk:
#         combined_chunks.append(current_chunk)

#     for idx, chunk in enumerate(combined_chunks):
#         embedding_id = f"{pdf_name}_{idx}"  # Unique ID for each chunk
        
#         if embedding_id in existing_ids:
#             print(f"⚠️ Skipping existing embedding ID: {embedding_id}")
#             continue  # ✅ Skip duplicate embeddings

#         embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
#         collection.add(ids=[embedding_id], embeddings=[embedding], metadatas=[{"text": chunk}])

#     print(f"✅ Embeddings stored successfully for {pdf_name}.")
import chromadb
import os
from google.generativeai import configure, embed_content
from config import GEMINI_API_KEY, CHROMA_DB_PATH

configure(api_key=GEMINI_API_KEY)

chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_or_create_collection("pdf_embeddings")

def delete_existing_embeddings(pdf_name):
    """Deletes embeddings associated with a specific PDF to avoid duplicates."""
    existing_data = collection.get()
    existing_ids = [doc_id for doc_id in existing_data["ids"] if pdf_name in doc_id]

    if existing_ids:
        collection.delete(existing_ids)
        print(f"🗑 Deleted existing embeddings for {pdf_name}")

def store_embeddings(text_chunks, pdf_name, chunk_size=1000):
    """Stores embeddings of text chunks in ChromaDB while avoiding duplicates."""
    
    # Check if embeddings already exist
    if check_existing_embeddings(pdf_name):
        print(f"✅ Embeddings already exist for {pdf_name}. Skipping embedding process.")
        return
    
    combined_chunks = []
    current_chunk = ""

    for chunk in text_chunks:
        if len(current_chunk) + len(chunk) <= chunk_size:
            current_chunk += " " + chunk if current_chunk else chunk
        else:
            combined_chunks.append(current_chunk)
            current_chunk = chunk

    if current_chunk:
        combined_chunks.append(current_chunk)

    # Delete old embeddings before inserting new ones
    delete_existing_embeddings(pdf_name)

    for idx, chunk in enumerate(combined_chunks):
        embedding_id = f"{pdf_name}_{idx}"

        embedding = embed_content(model="models/embedding-001", content=chunk)["embedding"]
        collection.add(ids=[embedding_id], embeddings=[embedding], metadatas=[{"text": chunk}])

def retrieve_relevant_text(query):
    """Retrieves relevant text chunks from ChromaDB based on query."""
    query_embedding = embed_content(model="models/embedding-001", content=query)["embedding"]
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    return [r["text"] for r in results["metadatas"][0]]

def check_existing_embeddings(pdf_name):
    """Checks if embeddings already exist for a specific PDF in ChromaDB."""
    existing_data = collection.get()
    return any(pdf_name in doc_id for doc_id in existing_data["ids"])
