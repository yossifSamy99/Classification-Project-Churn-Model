# 📉 Customer Churn Prediction API

An end-to-end Machine Learning project for predicting customer churn using multiple trained classification models. The application exposes secure RESTful APIs built with **FastAPI**, performs automated data preprocessing, and returns both churn predictions and confidence probabilities.

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

```text
.
├── Dockerfile
├── README.md
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

---

## 🚀 Getting Started

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

---

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

> Add screenshot here.

---

### Prediction Interface

> Add screenshot here.

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
