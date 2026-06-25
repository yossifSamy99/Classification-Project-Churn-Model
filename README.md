# Customer Churn Prediction

A machine learning project that predicts customer churn using tuned **Random Forest** and **XGBoost** models. The project includes a training/inference pipeline, a FastAPI backend (`main.py`), a Streamlit UI (`app_ui.py`), and Docker support for easy deployment.

> ⚠️ Some details below (framework choices, endpoint names, env vars) are inferred from the project structure. Please update any section marked **TODO** to match your actual implementation.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Running the UI](#running-the-ui)
  - [Running with Docker](#running-with-docker)
- [Models](#models)
- [Dataset](#dataset)
- [Notebooks](#notebooks)
- [Configuration](#configuration)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This project predicts whether a customer is likely to churn based on historical customer data. It covers the full ML lifecycle:

1. **Data preparation & EDA** — `notebooks/notebook.ipynb`
2. **Model training & tuning** — Random Forest and XGBoost, with a saved preprocessing pipeline
3. **Inference** — `utils/inference.py` loads the trained models and processor to score new customer data
4. **Serving** — a FastAPI app (`main.py`) exposes predictions as an API, and a Streamlit app (`app_ui.py`) provides an interactive UI
5. **Deployment** — containerized via `DockerFile`

---

## Project Structure

```
.
├── DockerFile                  # Container build definition
├── Models/                     # Serialized models & preprocessing artifacts
│   ├── RandomForestTuned.pkl
│   ├── processor.pkl
│   └── xgb_tuned.pkl
├── README.md
├── app_ui.py                   # Streamlit front-end
├── main.py                     # FastAPI app entry point
├── datasets/
│   └── churn-data.csv          # Raw/training dataset
├── notebooks/
│   ├── notebook.ipynb          # EDA / model training & tuning
│   └── passGenerator.ipynb     # TODO: describe purpose
├── requirements.txt            # Python dependencies
└── utils/
    ├── CustomerData.py         # Request/response schema for customer records
    ├── __init__.py
    ├── config.py                # App configuration / constants
    └── inference.py             # Model loading & prediction logic
```

> Note: `churnProject/` (virtual environment) and `__pycache__/` directories are excluded from version control — see [`.gitignore`](#development).

---

## Getting Started

### Prerequisites

- Python 3.13+
- pip
- (Optional) Docker, if you want to run the containerized version

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the API

Start the FastAPI server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Once running, the interactive API docs are available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

**Example request** *(TODO: confirm against your actual `/predict` schema in `CustomerData.py`)*:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "tenure": 12,
        "MonthlyCharges": 70.5,
        "Contract": "Month-to-month"
      }'
```

### Running the UI

The Streamlit app provides a simple interface for entering customer details and viewing churn predictions:

```bash
streamlit run app_ui.py
```

By default this opens at `http://localhost:8501`.

### Running with Docker

Build the image:

```bash
docker build -t churn-prediction -f DockerFile .
```

Run the container:

```bash
docker run -p 8000:8000 churn-prediction
```

> If `app_ui.py` and `main.py` need to run simultaneously inside the same container, make sure your `DockerFile`/entrypoint starts both processes (e.g. via a process manager or a startup script), or build/run two separate containers — one per service.

---

## Models

| File | Description |
|---|---|
| `Models/RandomForestTuned.pkl` | Hyperparameter-tuned Random Forest classifier |
| `Models/xgb_tuned.pkl` | Hyperparameter-tuned XGBoost classifier |
| `Models/processor.pkl` | Fitted preprocessing pipeline (encoding/scaling) used at inference time |

Both models are trained on the same preprocessing pipeline (`processor.pkl`) to ensure consistent feature transformation between training and inference. Model selection/ensembling logic lives in `utils/inference.py`.

---

## Dataset

- **Location:** `datasets/churn-data.csv`
- **Description:** Historical customer records used for training, including demographic, account, and usage features along with a churn label.

> TODO: Add column descriptions, size, and source/licensing info for the dataset.

---

## Notebooks

| Notebook | Purpose |
|---|---|
| `notebooks/notebook.ipynb` | Exploratory data analysis, feature engineering, model training and hyperparameter tuning |
| `notebooks/passGenerator.ipynb` | TODO: describe purpose (e.g. credential/test data generation) |

---

## Configuration

Application settings (paths, thresholds, feature lists, etc.) are centralized in `utils/config.py`. Update this file to point to different model artifacts or change runtime behavior without touching the core logic.

If your app reads secrets or environment-specific values, consider adding a `.env` file (not committed to version control) and loading it with a library such as `python-dotenv`.

---

## Development

Recommended `.gitignore` entries for this project:

```
__pycache__/
*.pyc
churnProject/
*.ipynb_checkpoints/
.env
```

Cleanup utilities (`utils/tempCodeRunnerFile.py`, `utils/tempCodeRunnerFile.ipynb`, `utils/t.ipynb`) appear to be editor scratch files — safe to remove or add to `.gitignore` if not part of the core pipeline.

---

## Troubleshooting

- **Model file not found at inference time:** Confirm `Models/` paths in `utils/config.py` are correct relative to where `main.py`/`app_ui.py` is run from.
- **Pickle version mismatch:** Models pickled with one version of `scikit-learn`/`xgboost` may fail to load with another. Ensure `requirements.txt` versions match those used during training.
- **Port already in use:** Change the `--port` flag for `uvicorn` or the Streamlit `--server.port` option.

---

## License

TODO: Add a license (e.g. MIT, Apache 2.0) or specify usage restrictions.
