import base64

from fastapi import FastAPI, Response

from utils import load_generator, generate_noise_vector, generate_image_tensor_from_noise_vector, batch_tensor_to_webp
from generator_architecture.architecture import Generator

app = FastAPI()

def get_generator():
    generator = load_generator('generator.pth', Generator)
    generator.eval()
    print("Generator loaded successfully!")
    return generator

@app.get("/generate")
async def root():
    generator = get_generator()
    noise_vector = generate_noise_vector()
    image_tensors = generate_image_tensor_from_noise_vector(noise_vector, generator)
    images = batch_tensor_to_webp(image_tensors)
    return [base64.b64encode(img).decode('utf-8') for img in images]