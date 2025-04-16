from pathlib import Path

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parent.parent
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")

DATA_DIR = PROJ_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = PROJ_ROOT / "models"


# # If tqdm is installed, configure loguru with tqdm.write
# # https://github.com/Delgan/loguru/issues/135
# try:
#     from tqdm import tqdm
#
#     logger.remove(0)
#     logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
# except ModuleNotFoundError:
#     pass


"""Training Hyperparameters"""

batch_size = 128
image_size = 64
nc = 3  # Number of channels
nz = 100  # Size of z latent vector
ngf = 64  # Size of feature maps in generator
ndf = 64  # Size of feature maps in discriminator

num_epochs = 4000
lr = 0.0002
beta1 = 0.5  # Beta1 hyperparameter for Adam optimizer
ngpu = 1
