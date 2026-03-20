import chromadb
from langchain_community.vectorstores import Chroma
from app.rag.embedder import get_embeddings
from langchain.schema import Document
from typing import List

client = chromadb.PersistentClient(path="./chroma_db")

def _collection_name(user_id: str, doc_id: str) -> str:
    return f"pm_{user_id[:8]}_{doc_id[:8]}"

def store_chunks(
    chunks: List[Document],
    user_id: str,
    doc_id: str
) -> Chroma:
    collection_name = _collection_name(user_id, doc_id)
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        client=client,
        collection_name=collection_name,
    )
    return vectorstore

def get_vectorstore(user_id: str, doc_id: str) -> Chroma:
    collection_name = _collection_name(user_id, doc_id)
    return Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=get_embeddings(),
    )

def delete_vectorstore(user_id: str, doc_id: str):
    collection_name = _collection_name(user_id, doc_id)
    try:
        client.delete_collection(collection_name)
    except Exception:
        pass
