from fastapi import FastAPI
import torch
from torchvision import transforms
import io
import base64

from utils import load_generator, generate_noise_vector, generate_image_tensor_from_noise_vector, tensor_to_webp
from generator_architecture.architecture import Generator

app = FastAPI()

generator = load_generator('generator.pth', Generator)
generator.eval()
print("Generator loaded successfully!")

noise_vector = generate_noise_vector()
image_tensor = generate_image_tensor_from_noise_vector(noise_vector, generator)
image = tensor_to_webp(image_tensor)

@app.post("/")
async def root():
    noise_vector = generate_noise_vector()
    image_tensor = generate_image_tensor_from_noise_vector(noise_vector, generator)
    image = tensor_to_webp(image_tensor)
    return {"image": image}

def generate_noise_vector():
    return torch.rand(3, 256, 256, dtype=torch.float32)

def generate_image_from_noise_vector(noise_vector):
    with torch.no_grad():
        generated_image = generator(noise_vector)
    return generated_image

def image_arr_to_PIL_image(image_array):
    """
    Converts a tensor array (expecting shape (3, 256, 256)) into a PIL Image object.
    :param image_array: Tensor array representing image (expecting shape (3, 256, 256))
    :return: PIL Image object
    """
    transform = transforms.ToPILImage()
    img = transform(image_array)
    return img

def PIL_image_to_image_string(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str