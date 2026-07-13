````markdown
# Titanic Survival Prediction API

A production-ready Machine Learning inference service that predicts Titanic passenger survival using a **TensorFlow/Keras** neural network deployed with **FastAPI**.

The project demonstrates the complete deployment workflow of a Deep Learning model, including data preprocessing, feature engineering, request validation, secure API access, and batch inference through RESTful APIs.

---

## Features

- 🚀 Deep Learning model built with TensorFlow/Keras
- ⚡ High-performance REST API using FastAPI
- 📦 Batch prediction support
- ✅ Automatic request validation with Pydantic
- 🔐 API Key authentication
- 🔄 Scikit-Learn preprocessing pipeline
- 🧠 Automatic feature engineering during inference
- 📁 Modular and scalable project architecture
- 💻 Interactive frontend (Streamlit/Gradio)

---

## Tech Stack

- Python
- TensorFlow / Keras
- Scikit-Learn
- FastAPI
- Pydantic
- Pandas
- Uvicorn
- Streamlit / Gradio

---

## Project Structure

```text
.
├── README.md
├── app_ui.py
├── main.py
├── requirements.txt
└── src/
    ├── __init__.py
    ├── inference.py
    ├── artifacts/
    │   ├── best_model.keras
    │   └── preprocessor.joblib
    └── utils/
        ├── __init__.py
        ├── config.py
        ├── request.py
        └── response.py
```

---

## How It Works

1. Receive passenger information through the REST API.
2. Validate incoming data using **Pydantic**.
3. Generate additional features:
   - Family Size
   - Is Alone
4. Apply the saved Scikit-Learn preprocessing pipeline.
5. Load the trained TensorFlow model.
6. Generate predictions.
7. Return structured JSON responses.

---

## API Endpoints

### Health Check

**GET /**

Response

```json
{
    "message": "up & running"
}
```

---

### Predict Passenger Survival

**POST /Classify**

#### Headers

```http
X-API-KEY: your_api_key
```

#### Request Body

```json
[
    {
        "passenger_id": 1,
        "pclass": 3,
        "parch": 0,
        "sibsp": 1,
        "sex": "male",
        "embarked": "S",
        "age": 22,
        "fare": 7.25
    }
]
```

#### Response

```json
{
    "predictions": [
        {
            "passenger_id": 1,
            "predicted": "not survived"
        }
    ]
}
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/titanic-survival-api.git

cd titanic-survival-api
```

---

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

---

### 3. Activate the Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## Security

All endpoints are protected using **API Key Authentication**.

Include the following header in every request:

```http
X-API-KEY: your_api_key
```

Unauthorized requests return:

```http
403 Forbidden
```

---

## Machine Learning Pipeline

```
Input Data
     │
     ▼
Pydantic Validation
     │
     ▼
Feature Engineering
(Family Size & Is Alone)
     │
     ▼
Preprocessor
(Joblib)
     │
     ▼
TensorFlow Model
(.keras)
     │
     ▼
Prediction
     │
     ▼
JSON Response
```

---

## Future Improvements

- Docker containerization
- Cloud deployment
- Prediction probability scores
- Model monitoring
- Logging
- Unit testing
- CI/CD pipeline

---

