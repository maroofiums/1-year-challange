# Day 317

# Loan Prediction API

A production-ready Machine Learning API for predicting loan approval status using multiple classification models with hyperparameter tuning and FastAPI deployment.

---

## Project Overview

This project solves a binary classification problem:
Predict whether a loan application will be approved or rejected based on applicant details.

The pipeline includes:

* Data Cleaning
* Missing Value Handling
* Feature Encoding
* Feature Scaling
* Model Selection using GridSearchCV
* Model Evaluation (Accuracy, F1-Score, AUC)
* FastAPI Deployment

The best performing model was Logistic Regression after cross-validation.

---

## Dataset

Loan Prediction Problem Dataset (Kaggle)

Features include:

* Gender
* Married
* Dependents
* Education
* Self_Employed
* ApplicantIncome
* CoapplicantIncome
* LoanAmount
* Loan_Amount_Term
* Credit_History
* Property_Area

Target:

* Loan_Status (Approved / Rejected)

---

## Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Matplotlib & Seaborn
* FastAPI
* Joblib
* Uvicorn

---

## Model Training Strategy

Multiple models were trained using GridSearchCV:

* Logistic Regression
* Random Forest
* Gradient Boosting
* Decision Tree
* SVM
* KNN
* Naive Bayes

Evaluation Metrics:

* Accuracy
* F1 Score (primary metric)
* ROC AUC

Best Model: Logistic Regression
Best F1 Score: 0.908

---

## Project Structure

```
├── Notebook
│   └── loan-approval-prediction.ipynb
├── app
│   ├── Models
│   │   └── loan_model_pipeline.pkl
│   └── main.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```
git clone https://github.com/maroofiums/loan-prediction-api.git
cd loan-prediction-api
```

Create virtual environment:

```
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the API

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

Interactive Swagger UI will open.

---

## API Endpoint

### POST /predict

Example Request Body:

```
{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 0,
  "LoanAmount": 120,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": "Urban"
}
```

Response:

```
{
  "prediction": 1,
  "approval_probability": 0.87
}
```

---

## Why This Project Is Strong

* Uses proper cross-validation
* Hyperparameter tuning
* Multiple model comparison
* Production-ready API
* Model + Preprocessing saved together
* Clean structure

---