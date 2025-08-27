import pytest
import respx
import httpx
from calculator_service.calculator_service import app
from fastapi.testclient import TestClient

client = TestClient(app)

@respx.mock
def test_calculator_integration_mocked():
    # Mocks
    respx.post("http://localhost:8001/add").mock(return_value=httpx.Response(200, json={"result": 5}))
    respx.post("http://localhost:8002/sub").mock(return_value=httpx.Response(200, json={"result": 3}))
    respx.post("http://localhost:8003/mul").mock(return_value=httpx.Response(200, json={"result": 15}))
    respx.post("http://localhost:8004/div").mock(return_value=httpx.Response(200, json={"result": 5}))

    expr = "((2+3)*(7-4))/3"
    response = client.post("/calculate", json={"expression": expr})

    assert response.status_code == 200
    assert "result" in response.json()
    result = response.json()["result"]
    assert result == 5
    print("Integration test passed with mocked services:", response.json())

