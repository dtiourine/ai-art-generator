from fastapi import FastAPI, Response

from utils import load_generator, generate_noise_vector, generate_image_tensor_from_noise_vector, tensor_to_webp
from generator_architecture.architecture import Generator

app = FastAPI()

def get_generator():
    generator = load_generator('generator.pth', Generator)
    generator.eval()
    print("Generator loaded successfully!")
    return generator

@app.get("/")
async def root():
    generator = get_generator()
    noise_vector = generate_noise_vector()
    image_tensor = generate_image_tensor_from_noise_vector(noise_vector, generator)
    image = tensor_to_webp(image_tensor)
    return Response(content=image, media_type="image/webp")