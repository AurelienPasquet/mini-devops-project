from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/sub")
async def sub(request: Request):
    data = await request.json()
    a = data["a"]
    b = data["b"]
    
    return JSONResponse({"result": a - b})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("substraction_service:app", host="0.0.0.0", port=8002, reload=True)
