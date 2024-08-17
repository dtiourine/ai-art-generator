from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm
import kaggle
import zipfile
import os
from art_generator.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

def download_kaggle_dataset(competition_name, path):
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
    logger.info(f"Removed zip file: {zip_file}")\


@app.command()
def main():
    logger.info("Downloading the dataset...")
    competition_name = 'gan-getting-started'  # Replace with the actual competition name
    download_kaggle_dataset(competition_name, RAW_DATA_DIR)
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
