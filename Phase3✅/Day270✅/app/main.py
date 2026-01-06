from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("best_model.pkl")

class TitanicRequest(BaseModel):
    pclass: int
    sex: str         
    age: float
    sibsp: int
    parch: int
    fare: float
    embarked: str    
    who: str          

app = FastAPI(title="Titanic Survival Prediction API")

@app.post("/predict")
def predict(data: TitanicRequest):
    try:
        features = [[
            data.pclass, data.sex, data.age, data.sibsp, data.parch,
            data.fare, data.embarked, data.who
        ]]

        pred = model.predict(features)[0]
        try:
            proba = model.predict_proba(features)[0][1]
        except Exception:
            proba = None

        return {
            "prediction": int(pred),
            "probability": float(proba) if proba is not None else "N/A"
        }
    except Exception as e:
        return {"error": str(e)}
