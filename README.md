# PaperMind
AI document intelligence platform for legal and finance
# PaperMind

> AI document intelligence platform for legal and finance

PaperMind lets you upload legal contracts, financial reports, NDAs, and
audit documents, then ask natural language questions and get cited,
accurate answers — powered by RAG, LangGraph, and Groq.

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14, TypeScript, Tailwind, Clerk |
| Backend | FastAPI, Python 3.11 |
| RAG | LangChain, LangGraph, ChromaDB |
| LLM | Groq (Llama 3) — free |
| Embeddings | Google Gemini embedding-001 — free |
| Auth | Clerk — free tier |
| Database | Supabase (PostgreSQL) — free tier |
| Deployment | Vercel + Render.com — free |

## Getting started

### 1. Clone and open in Codespaces
Click the green Code button → Codespaces → Create codespace on main

### 2. Set environment variables
Copy `.env.example` to `backend/.env` and fill in your free API keys.
Copy `.env.local.example` to `frontend/.env.local` and fill in Clerk keys.

### 3. Run backend
cd backend && uvicorn main:app --reload --port 8000

### 4. Run frontend
cd frontend && npm run dev

## Project phases
- Phase 1: Auth foundation (Clerk JWT)
- Phase 2: Document ingestion (PDF, DOCX, TXT, CSV)
- Phase 3: Document management dashboard
- Phase 4: RAG pipeline + LangGraph agent
- Phase 5: Chat memory + history
- Phase 6: UI polish + legal/finance UX
- Phase 7: Testing + deployment

## Disclaimer
PaperMind is a portfolio project. Answers generated are not legal or
financial advice. Always consult a qualified professional.