import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        res = await client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "ok"
    assert res.json()["project"] == "PaperMind"

@pytest.mark.asyncio
async def test_me_without_token_returns_403():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        res = await client.get("/auth/me")
    assert res.status_code == 403

@pytest.mark.asyncio
async def test_me_with_invalid_token_returns_401():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        res = await client.get(
            "/auth/me",
            headers={"Authorization": "Bearer fake_token"}
        )
    assert res.status_code == 401
