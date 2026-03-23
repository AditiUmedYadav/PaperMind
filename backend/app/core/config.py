from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY: str          = os.getenv("GROQ_API_KEY", "")
    GOOGLE_API_KEY: str        = os.getenv("GOOGLE_API_KEY", "")
    SUPABASE_URL: str          = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str          = os.getenv("SUPABASE_KEY", "")
    CLERK_SECRET_KEY: str      = os.getenv("CLERK_SECRET_KEY", "")
    FRONTEND_URL: str          = os.getenv("FRONTEND_URL", "http://localhost:3000")
    CODESPACE_NAME: str        = os.getenv("CODESPACE_NAME", "")

settings = Settings()
