from langchain_groq import ChatGroq
from app.core.config import settings
from app.rag.legal_prompts import DOMAIN_CLASSIFIER_PROMPT

def classify_domain(text_excerpt: str) -> str:
    try:
        llm = ChatGroq(
            model="llama3-8b-8192",
            groq_api_key=settings.GROQ_API_KEY,
            max_tokens=5,
        )
        prompt = DOMAIN_CLASSIFIER_PROMPT.format(excerpt=text_excerpt[:1000])
        result = llm.invoke(prompt)
        domain = result.content.strip().lower()
        return domain if domain in ["legal", "finance"] else "legal"
    except Exception:
        return "legal"
