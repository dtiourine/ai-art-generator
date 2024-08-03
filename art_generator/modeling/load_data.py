from torchvision.datasets import ImageFolder
from torchvision import transforms

root = "temp"
image_size = "temp"
def load_data():
    dataset = ImageFolder(root=root,
                          transform=transforms.Compose([
                              transforms.Resize(image_size),
                              transforms.CenterCrop(image_size),
                              transforms.ToTensor(),
                              transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                          ]))
    

