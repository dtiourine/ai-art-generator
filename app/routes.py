import base64
from fastapi import APIRouter

from app.utils import tensor_to_base64
from utils import generate_noise_vector, generate_image_tensor_from_noise_vector
import app_state

# Create a router instance
router = APIRouter()


@router.post("/generate-art")
async def generate_art():
    noise_vector = generate_noise_vector()
    image_tensor = generate_image_tensor_from_noise_vector(noise_vector, app_state.generator)
    base64_image = tensor_to_base64(image_tensor)
    return {"image": base64_image}


# @router.post("/generate-art")
# async def generate_art():
#     with open('app/sample_image.txt', 'r') as f:
#         base64_image = f.read()
#     return {"image": base64_image}