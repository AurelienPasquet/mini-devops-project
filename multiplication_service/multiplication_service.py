from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/mul")
async def mul(request: Request):
    data = await request.json()
    a = data["a"]
    b = data["b"]
    
    return JSONResponse({"result": a * b})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("multiplication_service:app", host="0.0.0.0", port=8003, reload=True)
