import pytest
from fastapi.testclient import TestClient
from multiplication_service.multiplication_service import app

client = TestClient(app)

def test_multiplication():
    response = client.post("/mul", json={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 12}
