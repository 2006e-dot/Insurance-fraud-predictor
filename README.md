#  Insurance Fraud Detection System using XGBoost

An end-to-end Machine Learning application that predicts whether an insurance claim is fraudulent using a tuned XGBoost model. The project includes data preprocessing, model comparison, hyperparameter tuning, FastAPI backend, and a Streamlit frontend.

---

##  Project Overview

Insurance fraud causes significant financial losses every year. This project aims to automatically identify potentially fraudulent insurance claims using supervised machine learning.

The project follows a complete ML lifecycle:

- Data Exploration (EDA)
- Data Preprocessing
- Model Training
- Hyperparameter Tuning
- Model Evaluation
- Model Serialization
- FastAPI Deployment
- Streamlit User Interface

---

##  Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Backend
- FastAPI
- Pydantic
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Joblib
- Git
- GitHub

---

#  Project Structure

```
Insurance-Fraud-Detection/
│
├── app.py                     # FastAPI Backend
├── frontend.py                # Streamlit Frontend
├── train.ipynb                # Complete ML Pipeline
├── insurance_fraud_xgb.pkl    # Trained XGBoost Model
├── cols.pkl                   # Saved Feature Columns
├── requirements.txt
├── README.md
└── fraud_oracle.csv
```

---

#  Machine Learning Pipeline

### Data Preprocessing

- Removed identifier columns
- Rare category merging
- One-Hot Encoding
- Train-Test Split
- Stratified Sampling
- Feature Alignment for Deployment

---

### Models Implemented

- Logistic Regression
- Decision Tree
- Random Forest
- Tuned Random Forest
- XGBoost
- Tuned XGBoost (Final Model)

---

##  Hyperparameter Tuning

Hyperparameter optimization was performed using **RandomizedSearchCV** with **5-Fold Stratified Cross Validation**.

Best Parameters:

```python
{
    'subsample': 0.8,
    'n_estimators': 500,
    'min_child_weight': 5,
    'max_depth': 5,
    'learning_rate': 0.05,
    'gamma': 0,
    'colsample_bytree': 0.6
}
```

---

#  Model Comparison

| Model | CV F1 Score | ROC-AUC |
|--------|------------:|---------:|
| Decision Tree | 0.228 | 0.817 |
| Random Forest | 0.238 | 0.821 |
| Tuned Random Forest | 0.276 | 0.825 |
| XGBoost | 0.289 | 0.848 |
| **Tuned XGBoost** | **0.294** | **0.850** |

The tuned XGBoost model achieved the best overall performance and was selected as the final production model.

---

#  FastAPI Backend

The backend exposes a REST API for fraud prediction.

### Endpoint

```
POST /predict
```

### Input

Insurance claim details in JSON format.

### Output

```json
{
    "prediction": "Fraud",
    "fraud_probability": 0.849
}
```

---

#  Streamlit Dashboard

The project also includes an interactive Streamlit interface where users can:

- Enter insurance claim details
- Submit claims
- Receive fraud prediction
- View fraud probability instantly

---

#  Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/Insurance-Fraud-Detection.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Project

Start FastAPI

```bash
uvicorn app:app --reload
```

FastAPI Docs

```
http://127.0.0.1:8000/docs
```

Start Streamlit

```bash
streamlit run front.py
```

---

#  Concepts Applied

- Exploratory Data Analysis
- Handling Imbalanced Data
- One-Hot Encoding
- Stratified Train-Test Split
- Decision Trees
- Random Forest
- XGBoost
- RandomizedSearchCV
- Cross Validation
- ROC-AUC
- Precision
- Recall
- F1 Score
- Model Serialization
- REST API Development
- ML Model Deployment

---

#  Future Improvements

- SHAP Explainability
- Feature Importance Visualization
- Threshold Tuning
- Docker Support
- AWS Deployment
- CI/CD Pipeline

---
