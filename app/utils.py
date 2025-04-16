import torch
from PIL import Image
import io
from generator_architecture.architecture import Generator


def load_generator(path, generator_class):
    """

    :param path: The path of the .pth file containing the state dict of the generator
    :param generator_class: Class inheriting from torch.nn.Module containing the architecture of the generator
    :return: Generator object from the generator class loaded with the given state dict
    """
    checkpoint = torch.load(path)
    generator = generator_class()  # You need to define the generator architecture
    generator.load_state_dict(checkpoint['model_state_dict'])
    return generator


def generate_noise_vector(batch_size=1, dim=100):
    """
    Generates a random noise vector of dimension dim
    :param dim: The dimension of the noise vector
    :return: A random pytorch tensor of dimension dim
    """
    return torch.rand(batch_size, dim, 1, 1, dtype=torch.float32)


def generate_image_tensor_from_noise_vector(noise_vector, generator):
    """
    Passes the noise vector to the generator resulting in a  generates the image from the noise vector
    :param noise_vector: A random noise vector expressed as a pytorch tensor
    :param generator: Generator object from the generator class
    :return: A pytorch tensor of shape (batch_size, 3, 256, 256) representing the generated images
    """
    with torch.no_grad():
        generated_image = generator(noise_vector)
    return generated_image

# def tensor_to_webp(tensor):
#     # Ensure the tensor is on CPU and detached from the computation graph
#     tensor = tensor.cpu().detach()
#
#     # Rescale from [-1, 1] to [0, 255]
#     tensor = (tensor + 1) / 2 * 255
#     tensor = tensor.clamp(0, 255).byte()
#
#     # Convert to PIL Image
#     image = Image.fromarray(tensor.permute(1, 2, 0).numpy())
#
#     # Save as WebP
#     webp_buffer = io.BytesIO()
#     image.save(webp_buffer, format="WebP", quality=80)  # Adjust quality as needed
#     webp_buffer.seek(0)
#
#     return webp_buffer.getvalue()


def batch_tensor_to_webp(tensor_batch):
    # Ensure the tensor is on CPU and detached from the computation graph
    tensor_batch = tensor_batch.cpu().detach()

    # Rescale from [-1, 1] to [0, 255]
    tensor_batch = (tensor_batch + 1) / 2 * 255
    tensor_batch = tensor_batch.clamp(0, 255).byte()

    webp_buffers = []
    for tensor in tensor_batch:
        # Convert to PIL Image
        image = Image.fromarray(tensor.permute(1, 2, 0).numpy())

        # Save as WebP
        webp_buffer = io.BytesIO()
        image.save(webp_buffer, format="WebP", quality=80)  # Adjust quality as needed
        webp_buffer.seek(0)
        webp_buffers.append(webp_buffer.getvalue())

    return webp_buffers
