import os
import platform
import subprocess
from pathlib import Path
import time
import webbrowser

ROOT_DIR = Path(__file__).resolve().parent
STATIC_DIR = ROOT_DIR / "static"
APP_MAIN = "app/main.py"

def set_pythonpath():
    if platform.system() == "Windows":
        os.environ["PYTHONPATH"] = str(ROOT_DIR)
    else:
        os.environ["PYTHONPATH"] = str(ROOT_DIR)

def run_fastapi():
    print("🚀 Starting FastAPI server...")
    subprocess.Popen(["fastapi", "dev", APP_MAIN])

def run_http_server():
    print("🌐 Starting frontend server at http://localhost:3000 ...")
    subprocess.run(["python", "-m", "http.server", "3000"], cwd=str(STATIC_DIR))

def open_browser():
    # Delay a bit to make sure the server is up
    time.sleep(2)
    print("🧭 Opening http://localhost:3000 in your browser...")
    webbrowser.open("http://localhost:3000")

if __name__ == "__main__":
    set_pythonpath()
    run_fastapi()
    open_browser()
    run_http_server()  # blocks so runs after FastAPI starts in background
