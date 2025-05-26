
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os

# Build a retriever from a transcript file

def build_retriever(transcript_path: str, collection_name: str = "panel-agent"):
    """
    Reads a transcript, splits into lines, embeds with OllamaEmbeddings,
    and returns a LangChain retriever over a Chroma vector store.
    """
    # Read transcript lines
    lines = open(transcript_path, "r", encoding="utf-8").read().splitlines()

    # Initialize embeddings and vector store
    embeddings = OllamaEmbeddings(model="llama3.1:8b")
    db_path = "./chromadb_langchain"
    add_docs = not os.path.exists(db_path)

  

    # Add documents to db
    if add_docs:
        docs, ids = [], []
        for i, line in enumerate(lines):
            docs.append(Document(page_content=line, metadata={}, id=str(i)))
            ids.append(str(i))
    
    vector_store = Chroma(
        collection_name=collection_name,
        persist_directory=db_path,
        embedding_function=embeddings
        )
    if add_docs:
        vector_store.add_documents(documents=docs, ids=ids)

    # Return a retriever (top-5)
    return vector_store.as_retriever(search_kwargs={"k": 25})