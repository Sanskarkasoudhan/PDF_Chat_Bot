# PDF Chatbot - AI Powered Q&A with Data Visualization

This is a **Streamlit-based GenAI application** that allows users to upload a **PDF document** and ask questions. The application processes the PDF, stores embeddings in **ChromaDB**, and generates responses using **Google's Gemini 2.0 Flash API**. Additionally, it provides **data visualization** for reports, financial documents, or statistical data.

---

## 🚀 Features

- 📄 **Upload a PDF document**
- ⚡ **Store text embeddings in ChromaDB** (avoids re-uploading the PDF every time)
- 🤖 **Answer user queries based on the document** using the **Gemini 2.0 Flash API**
- 📊 **Generate Data Visualizations** (Graphs, Charts, Pie Charts) for numerical insights
- 🎯 **Fast and efficient retrieval** of relevant text

---

## 📂 Folder Structure

```
📁 pdfchatbot/
│── 📜 app.py                  # Main Streamlit application
│── 📜 README.md               # Project documentation
│── 📜 requirements.txt        # Required dependencies
│── 📜 config.py               # API keys & paths (using dotenv)
│── 📂 data/                   # Uploaded PDFs (stored temporarily)
│── 📂 chroma/                 # ChromaDB
│── 📂 scripts/                # Core logic
│   ├── 📜 pdf_processor.py    # Extracts text from PDF
│   ├── 📜 embedding_store.py  # Stores & retrieves embeddings from ChromaDB
│   ├── 📜 query_handler.py    # Calls Gemini API to generate responses
│   ├── 📜 visualization.py    # Generates charts & graphs dynamically
│── 📂 venv/                   # (Optional) Virtual environment
```

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/Sanskarkasoudhan/PDF_Chat_Bot
cd pdfchatbot
```

### **2️⃣ Create a Virtual Environment (Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up API Keys (Using `.env`)**

Create a `.env` file in the `config/` folder and add your **Google Gemini API Key**:

```env
GEMINI_API_KEY=your_google_gemini_api_key
CHROMA_DB_PATH=./chroma_db
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

This will start the Streamlit app in your browser.

---

## 🏗️ How It Works (Step by Step)

### ✅ **1. Upload PDF**

- The user uploads a **PDF document**.
- The app extracts text from the PDF and splits it into **small chunks**.

### ✅ **2. Store Text Embeddings in ChromaDB**

- The app **checks if embeddings already exist**.
- If **no embeddings are found**, it generates embeddings using Gemini and stores them in **ChromaDB**.

### ✅ **3. Ask a Question**

- User enters a query about the document.
- The app **retrieves relevant text** from ChromaDB.
- The query + retrieved text is sent to **Gemini 2.0 Flash API**.

### ✅ **4. Get AI-Generated Response & Visualization**

- The AI generates an answer **based on the retrieved document text**.
- If the response includes **numerical or statistical data**, a **graph, pie chart, or bar chart** is dynamically generated.
- The response and **data visualization** are displayed in the Streamlit app.

---

## 📝 Example Usage

1️⃣ Upload a **PDF document**.  
2️⃣ Ask: *"What are the key financial trends in this report?"*  
3️⃣ The app retrieves relevant text and answers:  

   - **"The document discusses key financial growth in 2024..."**
   - 📊 **Displays a bar chart of revenue growth over time**

---

## 📌 TODOs & Future Improvements

✅ Improve response quality using **prompt engineering**.  
✅ Add **multi-PDF support** to analyze multiple documents.  
✅ Improve **UI design** using Streamlit components.  
✅ Enhance **data visualization with advanced analytics**.

---

## 💡 Contributing

If you find any bugs or have feature requests, feel free to **open an issue** or submit a **pull request**! 😊

---

## 📧 Contact

For any queries, reach out or create an issue in the repository!

🚀 **Happy Coding!** 🎉

