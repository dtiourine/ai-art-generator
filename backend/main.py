import base64

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from utils import load_generator, generate_noise_vector, generate_image_tensor_from_noise_vector, batch_tensor_to_webp
from generator_architecture.architecture import Generator

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    # Allow requests from these origins (your frontend URL)
    allow_origins=["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:5500"],
    # Allow cookies and credentials to be sent with the request
    allow_credentials=True,
    # Allow these HTTP methods
    allow_methods=["*"],  # You can list specific methods: ["GET", "POST"]
    # Allow these headers in the request
    allow_headers=["*"],  # You can list specific headers
)

def get_generator():
    generator = load_generator('generator.pth', Generator)
    generator.eval()
    print("Generator loaded successfully!")
    return generator

@app.post("/generate-art")
async def root():
    generator = get_generator()
    noise_vector = generate_noise_vector()
    image_tensors = generate_image_tensor_from_noise_vector(noise_vector, generator)
    images = batch_tensor_to_webp(image_tensors)
    return {"image": base64.b64encode(images[0]).decode('utf-8')}