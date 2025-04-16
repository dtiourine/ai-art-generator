import base64
from fastapi import APIRouter

from utils import generate_noise_vector, generate_image_tensor_from_noise_vector, batch_tensor_to_webp
import app_state

# Create a router instance
router = APIRouter()


@router.post("/generate-art")
async def generate_art():
    noise_vector = generate_noise_vector()
    image_tensors = generate_image_tensor_from_noise_vector(noise_vector, app_state.generator)
    images = batch_tensor_to_webp(image_tensors)
    return {"image": base64.b64encode(images[0]).decode('utf-8')}