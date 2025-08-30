import subprocess
import signal
import sys
import time

services = [
    ("addition_service/addition_service.py", 8001),
    ("substraction_service/substraction_service.py", 8002),
    ("multiplication_service/multiplication_service.py", 8003),
    ("division_service/division_service.py", 8004),
    ("calculator_service/calculator_service.py", 8000),
    ("frontend/frontend.py", 8080),
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
        print("\n✅ All services started. Open http://localhost:8080 in your browser.\n")
        signal.pause()
    except KeyboardInterrupt:
        stop_services()
    finally:
        stop_services()
