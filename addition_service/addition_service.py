from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/add")
async def add(request: Request):
    data = await request.json()
    a = data["a"]
    b = data["b"]
    
    print(f"ADD {a} + {b} = {a + b}")
    
    return JSONResponse({"result": a + b})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("addition_service:app", host="0.0.0.0", port=8001, reload=True)
