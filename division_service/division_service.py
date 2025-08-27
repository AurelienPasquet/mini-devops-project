from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/div")
async def div(request: Request):
    data = await request.json()
    a = data["a"]
    b = data["b"]
    
    print(f"DIV {a} / {b} = {"err" if b == 0 else a / b}")
    
    if b == 0:
        return JSONResponse({"result": "Error: Division by zero"})
    return JSONResponse({"result": a / b})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("division_service:app", host="0.0.0.0", port=8004, reload=True)
