from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from generator_architecture.architecture import Generator
from utils import load_generator
import app_state
from routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = None


@app.on_event("startup")
async def startup_event():
    """Initialize the generator when the application starts"""
    app_state.generator = load_generator('generator.pth', Generator)
    app_state.generator.eval()
    print("Generator loaded successfully!")

app.include_router(router)