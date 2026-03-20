from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from pydantic import BaseModel
from app.core.security import get_current_user
from app.db.supabase_client import get_supabase
from app.rag.ingestor import load_and_chunk, SUPPORTED_TYPES
from app.rag.vectorstore import store_chunks, delete_vectorstore
from app.rag.classifier import classify_domain
import tempfile, os, uuid

router = APIRouter(prefix="/documents", tags=["documents"])

class RenameRequest(BaseModel):
    new_name: str

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    user_id: str = Depends(get_current_user)
):
    # validate file type
    ext = file.filename.split(".")[-1].lower()
    if ext not in SUPPORTED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type .{ext}. Allowed: {SUPPORTED_TYPES}"
        )

    # save to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # chunk the document
        chunks = load_and_chunk(tmp_path, ext)

        if not chunks:
            raise HTTPException(status_code=400, detail="Document appears to be empty")

        # classify domain
        sample_text = chunks[0].page_content if chunks else ""
        domain = classify_domain(sample_text)

        # generate doc id and store in chromadb
        doc_id = str(uuid.uuid4())
        store_chunks(chunks, user_id, doc_id)

        # save metadata to supabase
        collection_name = f"pm_{user_id[:8]}_{doc_id[:8]}"
        supabase = get_supabase()
        supabase.table("documents").insert({
            "id": doc_id,
            "user_id": user_id,
            "name": file.filename.rsplit(".", 1)[0],
            "original_filename": file.filename,
            "file_type": ext,
            "domain": domain,
            "chroma_collection": collection_name,
        }).execute()

        return {
            "doc_id": doc_id,
            "name": file.filename.rsplit(".", 1)[0],
            "file_type": ext,
            "domain": domain,
            "chunks_count": len(chunks),
            "status": "ready"
        }

    finally:
        os.unlink(tmp_path)

@router.get("/")
async def list_documents(user_id: str = Depends(get_current_user)):
    supabase = get_supabase()
    result = supabase.table("documents")\
        .select("*")\
        .eq("user_id", user_id)\
        .order("created_at", desc=True)\
        .execute()
    return {"documents": result.data}

@router.patch("/{doc_id}")
async def rename_document(
    doc_id: str,
    body: RenameRequest,
    user_id: str = Depends(get_current_user)
):
    supabase = get_supabase()
    result = supabase.table("documents")\
        .update({"name": body.new_name})\
        .eq("id", doc_id)\
        .eq("user_id", user_id)\
        .execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"status": "renamed", "new_name": body.new_name}

@router.delete("/{doc_id}")
async def delete_document(
    doc_id: str,
    user_id: str = Depends(get_current_user)
):
    supabase = get_supabase()

    # verify ownership
    result = supabase.table("documents")\
        .select("*")\
        .eq("id", doc_id)\
        .eq("user_id", user_id)\
        .execute()

    if not result.data:
        raise HTTPException(status_code=404, detail="Document not found")

    # delete from chromadb
    delete_vectorstore(user_id, doc_id)

    # delete from supabase
    supabase.table("documents")\
        .delete()\
        .eq("id", doc_id)\
        .execute()

    return {"status": "deleted"}
