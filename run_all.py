import subprocess
import signal
import sys
import time
import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, "envs", ".env.ports")

if os.path.exists(DOTENV_PATH):
    load_dotenv(dotenv_path=DOTENV_PATH)

PORT_ADD = os.getenv("PORT_ADD", "8001")
PORT_SUB = os.getenv("PORT_SUB", "8002")
PORT_MUL = os.getenv("PORT_MUL", "8003")
PORT_DIV = os.getenv("PORT_DIV", "8004")
PORT_CALC = os.getenv("PORT_CALC", "8000")
PORT_FRONTEND = os.getenv("PORT_FRONTEND", "3000")

services = [
    ("addition_service/addition_service.py", int(PORT_ADD)),
    ("substraction_service/substraction_service.py", int(PORT_SUB)),
    ("multiplication_service/multiplication_service.py", int(PORT_MUL)),
    ("division_service/division_service.py", int(PORT_DIV)),
    ("calculator_service/calculator_service.py", int(PORT_CALC)),
    ("frontend/frontend.py", int(PORT_FRONTEND)),
]

processes = []

def start_services():
    for script, port in services:
        print(f"🚀 Starting {script} on port {port}...")
        p = subprocess.Popen([sys.executable, script])
        processes.append(p)
        time.sleep(0.5)

def stop_services():
    print("\n🛑 Stopping all services...")
    for p in processes:
        try:
            p.terminate()
        except Exception:
            pass

if __name__ == "__main__":
    try:
        start_services()
        print(f"\n✅ All services started. Open http://localhost:{PORT_FRONTEND} in your browser.\n")
        signal.pause()
    except KeyboardInterrupt:
        stop_services()
    finally:
        stop_services()
