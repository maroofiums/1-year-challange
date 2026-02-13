from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path 

BASE_DIR = Path(__file__).resolve().parent  # app folder
MODEL_PATH = BASE_DIR / "Models" / "loan_model_pipeline.pkl"

pipeline = joblib.load(MODEL_PATH)

model = pipeline["model"]
scaler = pipeline["scaler"]
encoders = pipeline["encoders"]

app = FastAPI(title="Loan Prediction API")


class LoanInput(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str


@app.get("/")
def home():
    return {"message": "Loan Prediction API is running"}


@app.post("/predict")
def predict(data: LoanInput):
    
    input_dict = data.dict()
    df = pd.DataFrame([input_dict])

    for col in encoders:
        df[col] = encoders[col].transform(df[col])

    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)[0]
    probability = model.predict_proba(df_scaled)[0][1]

    return {
        "prediction": int(prediction),
        "approval_probability": float(probability)
    }
