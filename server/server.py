from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Définition du schéma d'entrée
class Numbers(BaseModel):
    a: int
    b: int

@app.post("/sum")
def calculate_sum(numbers: Numbers):
    result = numbers.a + numbers.b
    return {"sum": result}
