# Art Generator

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Generative Adversarial Network (GAN) for generating images of art.

## Reference for self

# Next steps:
- **Retrain and adjust model to this time use an input image shape of 224 instead of 64 (so change image size hyperparameter)**
- Add script/instructions for downloading model/data
- Add requirements.txt file
- Finish up READme (both this one and the one remember the one in /src)
- To dependencies mention that a kaggle key is required to download dataset. Alternatively can download dataset at the website. Maybe put some sort of warning in setup_assets.py that there was an issue with downloading data from Kaggle (if there is one), and only model was installed

## 📦 Getting Started 

### 1. Install dependencies 

```bash 
pip install -r requirements.txt
```

### 2. Download assets (pretrained model + dataset) 

```bash 
python setup_assets.py
```

This will: 
- Download the pretrained GAN model into the `models/` folder
- Download and extract the training dataset into `data/`

## 🚀 Running Locally

### 🔄 Quick Start (Recommended)

To launch both the **FastAPI backend** and the **HTML frontend** locally with one command to interact with the art generator:

```
python run_dev.py
```

This will:
- Set the correct `PYTHONPATH` for clean imports
- Start the FastAPI server at [http://localhost:8000](http://localhost:8000)
- Serve the frontend at [http://localhost:3000](http://localhost:3000)

Make sure you are in the **project root** directory when you run the command.

---

### 🛠 Manual Setup (Alternative)

If you prefer to run everything manually, follow the steps below:

#### 1. Start FastAPI Backend

Run this from the **project root directory**:

**On macOS/Linux:**

```bash
PYTHONPATH=. fastapi dev app/main.py
```

**On Windows (PowerShell):**

```bash
$env:PYTHONPATH="." 
fastapi dev app/main.py
```

This starts the backend at:  
[http://localhost:8000](http://localhost:8000)

---

#### 2. Start Frontend (Static HTML)

In a new terminal, navigate to the `static/` folder and run:

```bash
cd static 
python -m http.server 3000
```

This starts the frontend at:  
[http://localhost:3000](http://localhost:3000)

The frontend can now communicate with the FastAPI backend to generate images.

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         art_generator and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── art_generator   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes art_generator a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── visualize.py                <- Code to create visualizations
```

--------

