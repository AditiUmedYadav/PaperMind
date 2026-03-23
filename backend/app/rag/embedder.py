from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.config import settings

_embeddings = None

def get_embeddings() -> GoogleGenerativeAIEmbeddings:
    global _embeddings
    if _embeddings is None:
        _embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=settings.GOOGLE_API_KEY
        )
    return _embeddings
