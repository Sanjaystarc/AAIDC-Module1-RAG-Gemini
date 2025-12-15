import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set")

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GEMINI_API_KEY
)

# Vector DB
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)
retriever = vectorstore.as_retriever()

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.2-flash",
    temperature=0,
    google_api_key=GEMINI_API_KEY
)

# Prompt
prompt = ChatPromptTemplate.from_template(
    """Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}
"""
)

# RAG Chain (modern LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("🤖 Gemini RAG Assistant (type 'exit' to quit)")

while True:
    q = input("\nYou: ")
    if q.lower() == "exit":
        break
    answer = rag_chain.invoke(q)
    print("Bot:", answer)
