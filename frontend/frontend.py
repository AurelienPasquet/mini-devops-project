from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
import httpx
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, "envs", ".env.ports")

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)

PORT_FRONTEND = os.getenv("PORT_FRONTEND", "3000")
PORT_CALC = os.getenv("PORT_CALC", "8000")

app = FastAPI()

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        .calculator { display: inline-grid; grid-template-columns: repeat(4, 60px); gap: 5px; }
        button { padding: 15px; font-size: 18px; border-radius: 8px; cursor: pointer; }
        input { grid-column: span 4; padding: 10px; font-size: 20px; text-align: right; border-radius: 8px; }
    </style>
</head>
<body>
    <h2>Calculator</h2>
    <div class="calculator">
        <input type="text" id="expression" autofocus>
        <button onclick="append('7')">7</button>
        <button onclick="append('8')">8</button>
        <button onclick="append('9')">9</button>
        <button onclick="append('/')">/</button>
        <button onclick="append('4')">4</button>
        <button onclick="append('5')">5</button>
        <button onclick="append('6')">6</button>
        <button onclick="append('*')">*</button>
        <button onclick="append('1')">1</button>
        <button onclick="append('2')">2</button>
        <button onclick="append('3')">3</button>
        <button onclick="append('-')">-</button>
        <button onclick="append('0')">0</button>
        <button onclick="append('.')">.</button>
        <button onclick="append('(')">(</button>
        <button onclick="append(')')">)</button>
        <button onclick="clearInput()">C</button>
        <button onclick="calculate()" style="grid-column: span 2; background: #4CAF50; color: white;">=</button>
        <button onclick="append('+')">+</button>
    </div>
    <h3 id="result"></h3>

    <script>
        function append(value) {
            document.getElementById("expression").value += value;
        }
        function clearInput() {
            document.getElementById("expression").value = "";
            document.getElementById("result").innerText = "";
        }
        async function calculate() {
            let expr = document.getElementById("expression").value;
            const response = await fetch("/send", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ expression: expr })
            });
            const data = await response.json();
            document.getElementById("result").innerText = "Result: " + data.result;
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def get_page():
    return html_page

@app.post("/send")
async def send_to_calculator(request: Request):
    body = await request.json()
    expr = body.get("expression", "")
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(f"http://localhost:{PORT_CALC}/calculate", json={"expression": expr})
            result = resp.json().get("result", "Error")
        except Exception as e:
            result = f"Error: {e}"
    return JSONResponse({"result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("frontend:app", host="0.0.0.0", port=int(PORT_FRONTEND), reload=True)
