from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, "envs", ".env.ports")

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)

PORT_MUL = os.getenv("PORT_MUL", "8003")

app = FastAPI()

@app.post("/mul")
async def mul(request: Request):
    data = await request.json()
    a = data["a"]
    b = data["b"]
    
    return JSONResponse({"result": a * b})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("multiplication_service:app", host="0.0.0.0", port=int(PORT_MUL), reload=True)
