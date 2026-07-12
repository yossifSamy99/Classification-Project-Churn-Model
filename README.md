
# Customer Churn Prediction

A machine learning project that predicts customer churn using tuned **Random Forest** and **XGBoost** models. The project includes a training/inference pipeline, a FastAPI backend (`main.py`), a Streamlit UI (`app_ui.py`), and Docker support for easy deployment.

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

.
├── DockerFile                  
├── Models/                     
│   ├── RandomForestTuned.pkl
│   ├── processor.pkl
│   └── xgb_tuned.pkl
├── README.md
├── app_ui.py                   
├── main.py                     
├── datasets/
│   └── churn-data.csv          
├── notebooks/
│   ├── notebook.ipynb          
│   └── passGenerator.ipynb     
├── requirements.txt            
└── utils/
├── CustomerData.py         
├── init.py
├── config.py              
└── inference.py            


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
Create and activate a virtual environment

Bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
Install dependencies

Bash
pip install -r requirements.txt
Usage
Running the API
Start the FastAPI server:

Bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Once running, the interactive API docs are available at:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Example request (Aligned with the CustomerData schema):

Bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
        "CreditScore": 650,
        "Geography": "France",
        "Gender": "Female",
        "Age": 35,
        "Tenure": 5,
        "Balance": 12500.50,
        "NumOfProducts": 2,
        "HasCrCard": 1,
        "IsActiveMember": 1,
        "EstimatedSalary": 50000.00
      }'
Running the UI
The Streamlit app provides a simple interface for entering customer details and viewing churn predictions:

Bash
streamlit run app_ui.py
By default this opens at http://localhost:8501.

Running with Docker
Build the image:

Bash
docker build -t churn-prediction -f DockerFile .
Run the container:

Bash
docker run -p 8000:8000 churn-prediction
Models
Models/RandomForestTuned.pkl: Hyperparameter-tuned Random Forest classifier.

Models/xgb_tuned.pkl: Hyperparameter-tuned XGBoost classifier.

Models/processor.pkl: Fitted preprocessing pipeline (encoding/scaling) used at inference time.

Both models are trained on the same preprocessing pipeline (processor.pkl) to ensure consistent feature transformation between training and inference. Model selection/ensembling logic lives in utils/inference.py.

Dataset
Location: datasets/churn-data.csv

Description: Historical bank customer records used for predicting customer churn. It includes a blend of demographic details, transactional behavior, and account status indicators.

Features breakdown (from CustomerData.py)
CreditScore: Integer (>= 0) - The customer's calculated creditworthiness.

Geography: String ('France', 'Spain', 'Germany') - Country of residence.

Gender: String ('Female', 'Male') - Biological sex.

Age: Integer (18 to 100) - Customer age in years.

Tenure: Integer (0 to 10) - Number of years dealing with the bank.

Balance: Float (>= 0.0) - Current total balance on account.

NumOfProducts: Integer (1 to 4) - Total number of bank items/services used.

HasCrCard: Integer (0 for No, 1 for Yes) - Does the client hold a credit card.

IsActiveMember: Integer (0 for No, 1 for Yes) - Active status based on account engagement.

EstimatedSalary: Float (>= 0.0) - Approximated salary of the client.

Notebooks
notebooks/notebook.ipynb: Exploratory data analysis, feature engineering, model training and hyperparameter tuning.

notebooks/passGenerator.ipynb: Utility script for generating/hashing user passwords, access tokens, or secure test credentials.

Configuration
Application settings (paths, thresholds, feature lists, etc.) are centralized in utils/config.py. Update this file to point to different model artifacts or change runtime behavior without touching the core logic.

If your app reads secrets or environment-specific values, consider adding a .env file (not committed to version control) and loading it with a library such as python-dotenv.

Development
Recommended .gitignore entries for this project:

__pycache__/
*.pyc
churnProject/
*.ipynb_checkpoints/
.env
Cleanup utilities (utils/tempCodeRunnerFile.py, utils/tempCodeRunnerFile.ipynb, utils/t.ipynb) appear to be editor scratch files — safe to remove or add to .gitignore if not part of the core pipeline.

Troubleshooting
Model file not found at inference time: Confirm Models/ paths in utils/config.py are correct relative to where main.py/app_ui.py is run from.

Pickle version mismatch: Models pickled with one version of scikit-learn/xgboost may fail to load with another. Ensure requirements.txt versions match those used during training.

Port already in use: Change the --port flag for uvicorn or the Streamlit --server.port option.

License
This project is open source and available under the MIT License.
