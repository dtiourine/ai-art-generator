from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from src.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main():
    pass


if __name__ == "__main__":
    app()
