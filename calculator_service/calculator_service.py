from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import httpx
import ast

app = FastAPI()

services = {
    ast.Add: "http://localhost:8001/add",
    ast.Sub: "http://localhost:8002/sub",
    ast.Mult: "http://localhost:8003/mul",
    ast.Div: "http://localhost:8004/div",
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
    uvicorn.run("calculator_service:app", host="0.0.0.0", port=8000, reload=True)
