import subprocess
import time
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def start_backend():
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "backend.main:app",
            "--reload",
            "--host",
            "127.0.0.1",
            "--port",
            "8000"
        ],
        cwd=BASE_DIR
    )

def start_electron():
    return subprocess.Popen(
        "npx electron .",
        cwd=os.path.join(BASE_DIR, "frontend"),
        shell=True
    )

if __name__ == "__main__":
    print("🚀 Finairis Launcher starting...")

    backend = start_backend()
    time.sleep(3)

    electron = start_electron()

    print("✅ All services running!")

    try:
        backend.wait()
        electron.wait()
    except KeyboardInterrupt:
        backend.terminate()
        electron.terminate()
        sys.exit(0)