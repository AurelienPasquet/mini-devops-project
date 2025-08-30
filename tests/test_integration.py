import pytest
import respx
import httpx
import os

from calculator_service.calculator_service import app
from fastapi.testclient import TestClient
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, "envs", ".env.ports")

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)

PORT_ADD = os.getenv("PORT_ADD", "8001")
PORT_SUB = os.getenv("PORT_SUB", "8002")
PORT_MUL = os.getenv("PORT_MUL", "8003")
PORT_DIV = os.getenv("PORT_DIV", "8004")

client = TestClient(app)

@respx.mock
def test_calculator_integration_mocked():
    
    respx.post(f"http://localhost:{PORT_ADD}/add").mock(return_value=httpx.Response(200, json={"result": 5}))
    respx.post(f"http://localhost:{PORT_SUB}/sub").mock(return_value=httpx.Response(200, json={"result": 3}))
    respx.post(f"http://localhost:{PORT_MUL}/mul").mock(return_value=httpx.Response(200, json={"result": 15}))
    respx.post(f"http://localhost:{PORT_DIV}/div").mock(return_value=httpx.Response(200, json={"result": 5}))

    expr = "((2+3)*(7-4))/3"
    response = client.post("/calculate", json={"expression": expr})

    assert response.status_code == 200
    assert "result" in response.json()
    result = response.json()["result"]
    assert result == 5
    print("Integration test passed with mocked services:", response.json())

