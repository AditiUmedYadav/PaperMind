from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api import auth, documents
import os

app = FastAPI(
    title="PaperMind API",
    description="AI document intelligence for legal and finance",
    version="2.0.0"
)

codespace = os.getenv("CODESPACE_NAME", "")
allowed_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
if codespace:
    allowed_origins.append(f"https://{codespace}-3000.app.github.dev")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(documents.router)

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "project": "PaperMind",
        "phase": 2,
        "allowed_origins": allowed_origins
    }
