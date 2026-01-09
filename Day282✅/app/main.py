from fastapi import FastAPI
import pandas as pd
from schemas import HouseInput
from models import model, label_encoders, model_columns

app = FastAPI(title="House Price Prediction API")

@app.post("/predict")
def predict_price(data: HouseInput):
    input_dict = data.dict()

    df = pd.DataFrame([input_dict])

    for col, encoder in label_encoders.items():
        df[col] = encoder.transform(df[col])

    df = df[model_columns]

    prediction = model.predict(df)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }
