from fastapi import FastAPI
import torch
from torchvision import transforms
from PIL import Image
import io
import base64

app = FastAPI()

@app.post("/")
async def root():
    ones = torch.ones(3, 256, 256, dtype=torch.float32)
    img = image_array_to_PIL_image(ones)
    img_str = PIL_image_to_image_string(img)
    return {"image": img_str}

def image_array_to_PIL_image(image_array):
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