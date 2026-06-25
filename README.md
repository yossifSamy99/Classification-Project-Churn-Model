

Markdown
# Customer Churn Prediction API & Dashboard

An end-to-end Machine Learning solution designed to predict customer churn. This repository provides a robust backend API built with **FastAPI**, an interactive frontend dashboard powered by **Streamlit** (or your UI framework of choice via `app_ui.py`), and full **Docker** containerization for seamless deployment.

---

## 📂 Project Structure

```text
├── DockerFile                  # Docker configuration for containerization
├── Models/                     # Serialized ML models and preprocessing pipelines
│   ├── RandomForestTuned.pkl   # Tuned Random Forest Classifier
│   ├── xgb_tuned.pkl           # Tuned XGBoost Classifier
│   └── processor.pkl           # Data preprocessing/scaling pipeline
├── datasets/                   # Raw or sample datasets
│   └── churn-data.csv          # Customer churn dataset
├── main.py                     # FastAPI backend application entry point
├── app_ui.py                   # Frontend UI interface (Streamlit / UI layer)
├── utils/                      # Helper modules and core logic
│   ├── CustomerData.py         # Pydantic models for data validation
│   ├── inference.py            # Prediction pipeline logic
│   └── config.py               # Application configuration and environment variables
├── notebooks/                  # Jupyter notebooks for EDA and experimentation
│   ├── notebook.ipynb          # Model training and evaluation notebook
│   └── passGenerator.ipynb     # Utility notebook (e.g., password/token generation)
└── requirements.txt            # Python dependencies
🚀 Features
Dual-Model Inference: Supports predicting churn using tuned versions of Random Forest and XGBoost.

Strict Data Validation: Utilizes Pydantic via CustomerData.py to ensure incoming API payloads strictly match expected data types.

Interactive UI: A dedicated dashboard (app_ui.py) to easily input customer attributes and visualize churn probability instantly.

Production Ready: Fully containerized using Docker, allowing rapid deployment to cloud environments.

🛠️ Installation & Setup
Prerequisites
Python 3.11+

Anaconda or venv virtual environment manager

1. Local Environment Setup
Clone this repository to your local machine and navigate into the project directory:

Bash
# Create a virtual environment
python -m venv churnProject

# Activate the environment
# On Windows:
churnProject\Scripts\activate
# On macOS/Linux:
source churnProject/bin/activate

# Install the required packages
pip install -r requirements.txt
💻 Running the Application
1. Start the FastAPI Backend
Run the backend server using uvicorn. The API handles the data validation and passes inputs to the serialized models in the Models/ directory.

Bash
uvicorn main:app --reload
API Documentation: Once running, navigate to http://127.0.0.1:8000/docs to view the interactive Swagger UI and test endpoints directly.

2. Start the Frontend UI
In a separate terminal window (with your virtual environment activated), launch your UI application:

Bash
streamlit run app_ui.py
Access the interface in your browser at http://localhost:8501.

🐳 Docker Deployment
To build and run the entire application inside an isolated Docker container:

1. Build the Docker Image
Bash
docker build -t churn-prediction-app .
2. Run the Docker Container
Bash
docker run -p 8000:8000 churn-prediction-app
This maps port 8000 of the container to port 8000 on your host machine, making the FastAPI application accessible locally.

📊 Core Workflow & Endpoints
Data Ingestion: The client sends customer details matching the schema defined in utils/CustomerData.py.

Preprocessing: The raw input data is passed through Models/processor.pkl to scale and encode features.

Inference (utils/inference.py): The processed data is fed into either xgb_tuned.pkl or RandomForestTuned.pkl to calculate the churn probability.

Response: The API returns a JSON response specifying whether the customer is likely to churn, alongside the calculated probability percentage.


### 💡 Quick Tip for Cleanliness
Before committing this to your repository, you might want to add a `.gitignore` file to avoid pushing compiled files and local environments. Here are a few paths from your structure that you should ideally exclude from git tracking:
```text
__pycache__/
churnProject/
utils/__pycache__/
utils/tempCodeRunnerFile*
utils/t.ipynb