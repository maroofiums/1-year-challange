from fastapi import APIRouter
from app.schemas import IrisInput
import joblib
import numpy as np

router = APIRouter()

model = joblib.load("model/model.pkl")

@router.post("/predict")
def predict_species(data: IrisInput):
    X = np.array([[data.sepal_length,data.sepal_width,data.petal_length,data.petal_width]])
    prediction = model.predict(X)[0]
    result = "Setosa" if prediction == 1 else "Not Setosa"
    return {"prediction":result}