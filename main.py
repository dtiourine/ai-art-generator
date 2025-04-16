from src.config import MODELS_DIR
import gdown
from loguru import logger


def download_model_file():
    logger.info("Downloading model...")
    file_id = '1T0nRe-wlsRxmog-SwRKy5m2UWMmmjrM2'
    url = f"https://drive.google.com/uc?id={file_id}"

    output_path = MODELS_DIR / "generator.pth"
    gdown.download(url, str(output_path), quiet=False)


if __name__ == '__main__':
    download_model_file()

