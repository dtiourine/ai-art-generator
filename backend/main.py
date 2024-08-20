from fastapi import FastAPI
import torch
from torchvision import transforms
from PIL import Image

app = FastAPI()

@app.get("/")
async def root(image_tensor):
    img = transform(image_tensor)
    return img

ones = torch.ones(3, 256, 256, dtype=torch.float32)
transform = transforms.ToPILImage()