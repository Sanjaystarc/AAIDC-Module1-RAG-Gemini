# 📚 AAIDC Module 1 – RAG Assistant (Gemini + LangChain)

## 🔍 Project Overview
This project is a **Retrieval-Augmented Generation (RAG) assistant** developed as part of **Module 1: Foundations of Agentic AI** in the **Agentic AI Developer Certification (AAIDC)** by Ready Tensor.

The assistant answers user questions by retrieving relevant information from a custom document set stored in a vector database and generating grounded responses using **Google Gemini**.

---

## 🧠 System Architecture
```
User Query
   ↓
Retriever (Chroma Vector Database)
   ↓
Relevant Document Chunks
   ↓
Prompt + Context
   ↓
Gemini LLM
   ↓
Final Answer
```

---

## 🛠️ Technologies Used
- Python
- LangChain (LCEL – LangChain Expression Language)
- langchain-google-genai
- Chroma Vector Database
- Google Gemini (gemini-2.5-flash)
- GitHub Codespaces

---

## 📂 Project Structure
```
AAIDC-Module1-RAG-Gemini/
├── main.py
├── ingest.py
├── data/
│   └── docs.txt
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AAIDC-Module1-RAG-Gemini.git
cd AAIDC-Module1-RAG-Gemini
```

---

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 3️⃣ Environment Variable Configuration

#### 🔐 GitHub Codespaces (Recommended)
Add a **Codespaces Secret**:
- **Name:** GEMINI_API_KEY
- **Value:** your Gemini API key

Restart the Codespace after adding the secret.

#### 🖥️ Local Setup
Create a `.env` file:
```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

### Step 1: Ingest Documents
```bash
python ingest.py
```

### Step 2: Run the RAG Assistant
```bash
python main.py
```

Type `exit` to stop the assistant.

---

## 💬 Example Usage
```
You: What is RAG?
Bot: RAG stands for Retrieval-Augmented Generation. It combines document retrieval with language models to generate grounded responses.
```

```
You: What is LangChain?
Bot: LangChain is a framework for building applications powered by language models, including tools for retrieval, memory, and agents.
```

---

## 📌 Limitations
- Uses a small static document dataset
- No reranking or retrieval evaluation
- No persistent conversational memory

---

## 🚀 Future Improvements
- Add conversational memory
- Expand document corpus
- Add retrieval evaluation and reranking
- Introduce logging and observability

---

## 🎓 Certification Context
This project fulfills the requirements for **AAIDC Module 1: Foundations of Agentic AI** by demonstrating:
- Retrieval-Augmented Generation (RAG)
- Vector database integration
- LLM-grounded question answering
- Clean, secure, and reproducible implementation

---

## 🧾 License
This project is intended for **educational purposes** as part of the Ready Tensor Agentic AI Developer Certification program.

