from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    CSVLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document
import os

SUPPORTED_TYPES = ["pdf", "docx", "txt", "csv"]

def get_loader(file_path: str, file_type: str):
    loaders = {
        "pdf":  PyPDFLoader,
        "docx": Docx2txtLoader,
        "txt":  TextLoader,
        "csv":  CSVLoader,
    }
    loader_class = loaders.get(file_type.lower())
    if not loader_class:
        raise ValueError(f"Unsupported file type: {file_type}")
    return loader_class(file_path)

def load_and_chunk(file_path: str, file_type: str) -> List[Document]:
    loader = get_loader(file_path, file_type)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = splitter.split_documents(docs)

    # tag each chunk with file metadata
    for chunk in chunks:
        chunk.metadata["file_type"] = file_type
        chunk.metadata["source_file"] = os.path.basename(file_path)

    return chunks
