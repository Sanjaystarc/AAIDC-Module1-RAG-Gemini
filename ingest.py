import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# =========================
# RAG Chunking Configuration
# =========================
CHUNK_SIZE = 500        # Number of characters per chunk
CHUNK_OVERLAP = 50      # Overlapping characters between chunks



# Load Gemini API Key from Codespaces Secret
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found. Set it in Codespaces Secrets.")

# Load documents
loader = TextLoader("data/docs.txt")
documents = loader.load()

# Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = splitter.split_documents(documents)

# Create embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY
)

# Store in Chroma DB
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

vectorstore.persist()
print("✅ Documents successfully ingested into Chroma")
