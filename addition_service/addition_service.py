from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, "envs", ".env.ports")

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)

PORT_ADD = os.getenv("PORT_ADD", "8001")

app = FastAPI()

@app.post("/add")
async def add(request: Request):
    data = await request.json()
    a = data["a"]
    b = data["b"]
    
    return JSONResponse({"result": a + b})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("addition_service:app", host="0.0.0.0", port=int(PORT_ADD), reload=True)
