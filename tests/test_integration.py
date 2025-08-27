import pytest
import httpx
import asyncio

BASE_CALC = "http://localhost:8000/calculate"

@pytest.mark.asyncio
async def test_full_calculation():
    expr = "((3+2)*(10-4))/2"
    async with httpx.AsyncClient() as client:
        resp = await client.post(BASE_CALC, json={"expression": expr})
        assert resp.status_code == 200
        result = resp.json()["result"]
        assert result == 15
