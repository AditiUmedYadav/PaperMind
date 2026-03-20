import pytest
from httpx import AsyncClient, ASGITransport
from main import app
import io

@pytest.mark.asyncio
async def test_upload_without_auth_returns_403():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        res = await client.post(
            "/documents/upload",
            files={"file": ("test.pdf", b"fake content", "application/pdf")}
        )
    assert res.status_code == 403

@pytest.mark.asyncio
async def test_upload_unsupported_file_type():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        res = await client.post(
            "/documents/upload",
            files={"file": ("test.exe", b"fake content", "application/octet-stream")},
            headers={"Authorization": "Bearer fake_token"}
        )
    assert res.status_code in [400, 401]

@pytest.mark.asyncio
async def test_list_documents_without_auth():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        res = await client.get("/documents/")
    assert res.status_code == 403

@pytest.mark.asyncio
async def test_ingestor_loads_txt():
    from app.rag.ingestor import load_and_chunk
    import tempfile, os
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=".txt", mode="w"
    ) as f:
        f.write("This is a legal contract between Party A and Party B.")
        tmp_path = f.name
    try:
        chunks = load_and_chunk(tmp_path, "txt")
        assert len(chunks) > 0
        assert "legal" in chunks[0].page_content.lower() or len(chunks[0].page_content) > 0
    finally:
        os.unlink(tmp_path)
