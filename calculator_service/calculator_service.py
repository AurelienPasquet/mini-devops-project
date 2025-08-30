from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

import httpx
import ast
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, "envs", ".env.ports")

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)


PORT_ADD = os.getenv("PORT_ADD", "8001")
PORT_SUB = os.getenv("PORT_SUB", "8002")
PORT_MUL = os.getenv("PORT_MUL", "8003")
PORT_DIV = os.getenv("PORT_DIV", "8004")
PORT_CALC = os.getenv("PORT_CALC", "8000")

app = FastAPI()

services = {
    ast.Add: f"http://localhost:{PORT_ADD}/add",
    ast.Sub: f"http://localhost:{PORT_SUB}/sub",
    ast.Mult: f"http://localhost:{PORT_MUL}/mul",
    ast.Div: f"http://localhost:{PORT_DIV}/div",
}

async def eval_expr(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        left = await eval_expr(node.left)
        right = await eval_expr(node.right)
        url = services[type(node.op)]
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json={"a": left, "b": right})
            return resp.json()["result"]
    if isinstance(node, ast.Expression):
        return await eval_expr(node.body)
    raise ValueError("Unsupported expression")

@app.post("/calculate")
async def calculate(request: Request):
    data = await request.json()
    expr = data.get("expression", "")
    try:
        tree = ast.parse(expr, mode="eval")
        result = await eval_expr(tree)
    except Exception as e:
        return JSONResponse({"result": f"Error: {e}"})
    return JSONResponse({"result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("calculator_service:app", host="0.0.0.0", port=int(PORT_CALC), reload=True)
