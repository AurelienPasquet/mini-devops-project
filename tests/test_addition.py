import pytest
from fastapi.testclient import TestClient
from addition_service.addition_service import app

client = TestClient(app)

def test_addition():
    response = client.post("/add", json={"a": 4, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 7}
