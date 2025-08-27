import pytest
from fastapi.testclient import TestClient
from substraction_service.substraction_service import app

client = TestClient(app)

def test_substraction():
    response = client.post("/add", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6}
