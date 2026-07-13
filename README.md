# 📉 Customer Churn Prediction API

<<<<<<< HEAD
A machine learning project that predicts customer churn using tuned **Random Forest** and **XGBoost** models. The project includes a training/inference pipeline, a FastAPI backend (`main.py`), a Streamlit UI (`app_ui.py`), and Docker support for easy deployment.
=======
An end-to-end Machine Learning project for predicting customer churn using multiple trained classification models. The application exposes secure RESTful APIs built with **FastAPI**, performs automated data preprocessing, and returns both churn predictions and confidence probabilities.
>>>>>>> 39804759c32ff4da0177be58ede016393b737bde

---

## ✨ Features

- Predict customer churn using multiple ML models.
- Supports both **Random Forest** and **XGBoost** classifiers.
- Automatic data preprocessing before inference.
- Strong request validation using **Pydantic**.
- Secure API endpoints with **API Key Authentication**.
- Interactive API documentation via Swagger UI.
- Dockerized for easy deployment.
- Returns both prediction and probability score.

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| API | FastAPI |
| Machine Learning | Scikit-learn, XGBoost |
| Data Processing | Pandas |
| Validation | Pydantic |
| Model Serialization | Joblib |
| Deployment | Docker |
| Documentation | Swagger UI |

---

## 📂 Project Structure

<<<<<<< HEAD
=======
```text
>>>>>>> 39804759c32ff4da0177be58ede016393b737bde
.
├── Dockerfile
├── README.md
<<<<<<< HEAD
├── app_ui.py                   # Streamlit front-end
├── main.py                     # FastAPI app entry point
├── datasets/
│   └── churn-data.csv          # Raw/training dataset
├── notebooks/
│   ├── notebook.ipynb          # EDA / model training & tuning
│   └── passGenerator.ipynb     # Utility for hashing credentials or creating test data passcodes
├── requirements.txt            # Python dependencies
└── utils/
├── CustomerData.py         # Request/response Pydantic schema for customer records
├── init.py
├── config.py               # App configuration / constants
└── inference.py            # Model loading & prediction logic

=======
├── requirements.txt
├── app_ui.py
├── main.py
│
├── Models
│   ├── RandomForestTuned.pkl
│   ├── xgb_tuned.pkl
│   └── processor.pkl
│
├── datasets
│   └── churn-data.csv
│
├── notebooks
│   ├── notebook.ipynb
│   └── passGenerator.ipynb
│
└── utils
    ├── __init__.py
    ├── config.py
    ├── CustomerData.py
    └── inference.py
```
>>>>>>> 39804759c32ff4da0177be58ede016393b737bde

---

## 🚀 Getting Started

<<<<<<< HEAD
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
=======
### 1. Clone the repository

```bash
git clone https://github.com/yossifSamy99/Classification-Project-Churn-Model

cd customer-churn-api
```

---

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the application

```bash
uvicorn main:app --reload
```

The server will start at

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```
>>>>>>> 39804759c32ff4da0177be58ede016393b737bde

Pickle version mismatch: Models pickled with one version of scikit-learn/xgboost may fail to load with another. Ensure requirements.txt versions match those used during training.

<<<<<<< HEAD
Port already in use: Change the --port flag for uvicorn or the Streamlit --server.port option.

License
This project is open source and available under the MIT License.
=======
## 🔐 Authentication

Protected endpoints require an API Key.

Include the following header in every request:

```http
X-API-Key: YOUR_SECRET_KEY
```

---

## 📬 API Endpoints

### Home

```http
GET /
```

Returns the application status.

---

### Random Forest Prediction

```http
POST /predict/forest
```

---

### XGBoost Prediction

```http
POST /predict/XGboost
```

---

## 📝 Sample Request

```json
{
    "CreditScore":650,
    "Geography":"France",
    "Gender":"Male",
    "Age":42,
    "Tenure":5,
    "Balance":120000,
    "NumOfProducts":2,
    "HasCrCard":1,
    "IsActiveMember":1,
    "EstimatedSalary":85000
}
```

---

## ✅ Sample Response

```json
{
    "probability":[
        [
            0.92,
            0.08
        ]
    ],
    "prediction":false
}
```

---

## ⚙️ Machine Learning Pipeline

The prediction workflow follows these steps:

1. Receive customer information.
2. Validate input using Pydantic.
3. Convert request into a Pandas DataFrame.
4. Apply the saved preprocessing pipeline.
5. Load the selected trained model.
6. Generate prediction.
7. Calculate prediction probability.
8. Return results as JSON.

---

## 🤖 Models

The project includes multiple trained models:

- Random Forest (Tuned)
- XGBoost (Tuned)

Both models use the same preprocessing pipeline to ensure consistency between training and inference.

---

## 📊 Input Features

| Feature | Description |
|----------|-------------|
| CreditScore | Customer credit score |
| Geography | Customer country |
| Gender | Customer gender |
| Age | Customer age |
| Tenure | Years with the bank |
| Balance | Current account balance |
| NumOfProducts | Number of products |
| HasCrCard | Credit card ownership |
| IsActiveMember | Active membership |
| EstimatedSalary | Estimated annual salary |

---

## 🐳 Docker

Build the Docker image

```bash
docker build -t churn-api .
```

Run the container

```bash
docker run -p 8000:8000 churn-api
```

---

## 📸 Screenshots

### Swagger API


![Swagger UI](images\sw.png)

---

### Prediction Interface

![Application UI](images\st.png)


---

## 🔮 Future Improvements

- Add model versioning.
- Support batch predictions.
- Add user authentication with JWT.
- Deploy on AWS or Azure.
- Integrate CI/CD pipeline.
- Add monitoring and logging.
- Improve model explainability using SHAP.

---