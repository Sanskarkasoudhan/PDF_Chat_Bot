# import google.generativeai as genai
# import os

# from scripts.embedding_store import retrieve_relevant_text
# from config import GEMINI_API_KEY

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# TEMP_FILE = "temp.py"

# def generate_answer_with_visualization(query):
#     """Generates an answer along with Matplotlib code for visualization."""
    
#     # Retrieve relevant text from ChromaDB
#     relevant_texts = retrieve_relevant_text(query)

#     # Prepare prompt with retrieved context
#     context = "\n".join(relevant_texts)
#     prompt = f"""
#     Based on the following reports:\n\n{context}\n\nQuestion: {query}
    
#     Answer the question first in text.
#     Then, if the answer contains numerical trends, generate **only** valid Python Matplotlib code for visualization.
    
#     **Matplotlib code rules:**
#     - Use `matplotlib.pyplot`
#     - Define a figure and axis using `fig, ax = plt.subplots()`
#     - Label axes, set titles, and include a legend if necessary
#     - **No explanations—return only the code**
#     - End with `plt.show()`

#     Ensure the code is properly formatted within triple backticks.
#     """

#     # Use Gemini AI to generate a response
#     model = genai.GenerativeModel("gemini-2.0-flash")
#     response = model.generate_content(prompt)

#     if hasattr(response, "text"):
#         response_text = response.text
#     else:
#         response_text = response.candidates[0].content  # Fallback for response format

#     # Extract answer and Matplotlib code
#     parts = response_text.split("```")
#     answer = parts[0].strip()
    
#     # Extract and clean the Matplotlib code
#     if len(parts) > 1:
#         matplotlib_code = parts[1].replace("python", "").strip()
        
#         # Ensure `plt.show()` is included
#         if "plt.show()" not in matplotlib_code:
#             matplotlib_code += "\nplt.show()"
#     else:
#         matplotlib_code = ""

#     # **Handle cases where no visualization is generated**
#     if not matplotlib_code.strip():
#         print("\n⚠️ No visualization code generated!")
#         empty_file = "empty_temp.py"
#         with open(empty_file, "w") as f:
#             f.write("# No visualization generated.\n")
#         return answer, empty_file  # ✅ Return a valid empty file

#     # **Write Matplotlib code to a temp file**
#     with open(TEMP_FILE, "w") as f:
#         f.write("import streamlit as st\n")
#         f.write("import matplotlib.pyplot as plt\n\n")  
#         f.write("st.title('Dynamic Matplotlib Execution')\n\n")
#         f.write("code_from_gemini = '''\n")  
#         f.write(matplotlib_code)
#         f.write("\n'''\n\n")  
#         f.write("exec(code_from_gemini, globals())\n")
#         f.write("st.pyplot(fig)\n")

#     return answer, TEMP_FILE  # ✅ Returns the valid file path
# import google.generativeai as genai
# import os

# from scripts.embedding_store import retrieve_relevant_text
# from config import GEMINI_API_KEY

# # Configure Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# TEMP_FILE = "temp.py"

# def generate_answer_with_visualization(query):
#     """Generates an answer along with Matplotlib code for visualization."""
    
#     # Retrieve relevant text from ChromaDB
#     relevant_texts = retrieve_relevant_text(query)

#     # Prepare prompt with retrieved context
#     context = "\n".join(relevant_texts)
#     prompt = f"""
#     Based on the following reports:\n\n{context}\n\nQuestion: {query}
    
#     Answer the question first in text.
#     Then, if the answer contains numerical trends, generate **only** valid Python Matplotlib code for visualization.
    
#     **Matplotlib code rules:**
#     - Use `matplotlib.pyplot`
#     - Define a figure and axis using `fig, ax = plt.subplots()`
#     - Label axes, set titles, and include a legend if necessary
#     - **No explanations—return only the code**
#     - End with `plt.show()`

#     Ensure the code is properly formatted within triple backticks.
#     """

#     # Use Gemini AI to generate a response
#     model = genai.GenerativeModel("gemini-2.0-flash")
#     response = model.generate_content(prompt)

#     if hasattr(response, "text"):
#         response_text = response.text
#     else:
#         response_text = response.candidates[0].content  # Fallback for response format

#     # Extract answer and Matplotlib code
#     parts = response_text.split("```")
#     answer = parts[0].strip()
    
#     # Extract and clean the Matplotlib code
#     if len(parts) > 1:
#         matplotlib_code = parts[1].replace("python", "").strip()
        
#         # Ensure `plt.show()` is included
#         if "plt.show()" not in matplotlib_code:
#             matplotlib_code += "\nplt.show()"
#     else:
#         matplotlib_code = ""

#     # **Handle cases where no visualization is generated**
#     if not matplotlib_code.strip():
#         print("\n⚠️ No visualization code generated!")
#         empty_file = "empty_temp.py"
#         with open(empty_file, "w") as f:
#             f.write("# No visualization generated.\n")
#         return answer, empty_file  # ✅ Return a valid empty file

#     # **Write Matplotlib code to a temp file**
#     with open(TEMP_FILE, "w") as f:
#         f.write("import streamlit as st\n")
#         f.write("import matplotlib.pyplot as plt\n\n")  
#         f.write("st.title('Dynamic Matplotlib Execution')\n\n")
#         f.write("code_from_gemini = '''\n")  
#         f.write(matplotlib_code)
#         f.write("\n'''\n\n")  
#         f.write("exec(code_from_gemini, globals())\n")
#         f.write("st.pyplot(fig)\n")

#     return answer, TEMP_FILE  # ✅ Returns the valid file path
import google.generativeai as genai
import os

from scripts.embedding_store import retrieve_relevant_text
from config import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

TEMP_FILE = "temp.py"

def generate_answer_with_visualization(query):
    """Generates an answer along with Matplotlib code for visualization."""
    
    # Retrieve relevant text from ChromaDB
    relevant_texts = retrieve_relevant_text(query)

    # Prepare prompt with retrieved context
    context = "\n".join(relevant_texts)
    prompt = f"""
    Based on the following reports:\n\n{context}\n\nQuestion: {query}
    
    Answer the question first in text.
    Then, if the answer contains numerical trends, generate **only** valid Python Matplotlib code for visualization.
    
    **Matplotlib code rules:**
    - Use `matplotlib.pyplot`
    - Define a figure and axis using `fig, ax = plt.subplots()`
    - Label axes, set titles, and include a legend if necessary
    - **No explanations—return only the code**
    - End with `plt.show()`

    Ensure the code is properly formatted within triple backticks.
    """

    # Use Gemini AI to generate a response
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    if hasattr(response, "text"):
        response_text = response.text
    else:
        response_text = response.candidates[0].content  # Fallback for response format

    # Extract answer and Matplotlib code
    parts = response_text.split("```")
    answer = parts[0].strip()
    
    # Extract and clean the Matplotlib code
    if len(parts) > 1:
        matplotlib_code = parts[1].replace("python", "").strip()
        
        # Ensure `plt.show()` is included
        if "plt.show()" not in matplotlib_code:
            matplotlib_code += "\nplt.show()"
    else:
        matplotlib_code = ""

    # **Handle cases where no visualization is generated**
    if not matplotlib_code.strip():
        print("\n⚠️ No visualization code generated!")
        empty_file = "empty_temp.py"
        with open(empty_file, "w") as f:
            f.write("# No visualization generated.\n")
        return answer, empty_file  # ✅ Return a valid empty file

    # **Write Matplotlib code to a temp file**
    with open(TEMP_FILE, "w") as f:
        f.write("import streamlit as st\n")
        f.write("import matplotlib.pyplot as plt\n\n")  
        f.write("st.title('Dynamic Matplotlib Execution')\n\n")
        f.write("code_from_gemini = '''\n")  
        f.write(matplotlib_code)
        f.write("\n'''\n\n")  
        f.write("exec(code_from_gemini, globals())\n")
        f.write("st.pyplot(fig)\n")

    return answer, TEMP_FILE  # ✅ Returns the valid file path
