import pytest
from fastapi.testclient import TestClient
from division_service.division_service import app

client = TestClient(app)

def test_division():
    response = client.post("/div", json={"a": 30, "b": 10})
    assert response.status_code == 200
    assert response.json() == {"result": 3}
