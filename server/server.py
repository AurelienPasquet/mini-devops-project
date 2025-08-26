from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input schema for the request
class Numbers(BaseModel):
    a: int
    b: int

@app.post("/sum")
def calculate_sum(numbers: Numbers):
    """
    Endpoint that receives two integers (a, b),
    computes their sum and returns it as JSON.
    """
    result = numbers.a + numbers.b
    return {"sum": result}
