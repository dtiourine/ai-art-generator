from src.config import MODELS_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR
import gdown
from loguru import logger

from src.data.dataset import download_dataset, move_images


def download_model():
    MODELS_DIR.mkdir(exist_ok=True)
    logger.info("Downloading model...")
    file_id = '1T0nRe-wlsRxmog-SwRKy5m2UWMmmjrM2'
    url = f"https://drive.google.com/uc?id={file_id}"

    output_path = MODELS_DIR / "generator.pth"
    gdown.download(url, str(output_path), quiet=False)

def download_and_organize_data():
    logger.info(f"Downloading the raw dataset from Kaggle to {RAW_DATA_DIR}")
    download_dataset()

    logger.info(f"Moving art image data to {PROCESSED_DATA_DIR}")
    move_images()



if __name__ == '__main__':
    download_model()
    download_and_organize_data()

