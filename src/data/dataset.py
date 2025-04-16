import typer
from loguru import logger
from tqdm import tqdm
import kaggle
import zipfile
import os
import shutil

from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


def download_dataset(competition_name="gan-getting-started", path=RAW_DATA_DIR):
    """
    Download the dataset from Kaggle.
    Note: You need to have a kaggle.json file in ~/.kaggle/ with your API credentials.
    """
    kaggle.api.authenticate()
    with tqdm(total=1, desc="Downloading dataset", unit="file") as pbar:
        kaggle.api.competition_download_files(competition_name, path=path)
        pbar.update(1)
    logger.info(f"Dataset downloaded to {path}")

    # Find the zip file
    zip_file = next(file for file in os.listdir(path) if file.endswith('.zip'))
    zip_path = os.path.join(path, zip_file)

    # Extract the contents
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        total_files = len(zip_ref.infolist())
        with tqdm(total=total_files, desc="Extracting files", unit="file") as pbar:
            for file in zip_ref.infolist():
                zip_ref.extract(file, path)
                pbar.update(1)
    logger.info(f"Dataset extracted to {path}")

    # Remove the zip file after extraction
    os.remove(zip_path)
    logger.info(f"Removed zip file: {zip_file}")


def move_images(source_dir=RAW_DATA_DIR / 'monet_jpg', destination_dir=PROCESSED_DATA_DIR / 'real_art_images'):
    """
    Organizes the dataset by moving images from raw/monet_jpg to processed/
    """
    os.makedirs(destination_dir, exist_ok=True)

    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    for filename in tqdm(files, desc="Moving images", unit="file"):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        shutil.copy2(source_file, destination_file)


@app.command()
def main():
    logger.info(f"Downloading the dataset to {RAW_DATA_DIR}")
    download_dataset()

    logger.info(f"Moving art image data to {PROCESSED_DATA_DIR}")
    move_images()


if __name__ == "__main__":
    app()
