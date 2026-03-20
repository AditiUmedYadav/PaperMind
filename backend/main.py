from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, documents

app = FastAPI(
    title="PaperMind API",
    description="AI document intelligence for legal and finance",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(documents.router)

@app.get("/health")
async def health():
    return {"status": "ok", "project": "PaperMind", "phase": 2}
