from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

model = joblib.load('clf_model.pkl')

app = FastAPI()

@app.post("/predict")
def predict_iris(data: IrisRequest):
    features = np.array([[data.sepal_length,data.sepal_width,data.petal_length,data.petal_width]])
    prediction = model.predict(features)
    class_name = ["setosa", "versicolor", "virginica"][prediction[0]]

    return {"Prediction":int(prediction[0]),"class_name":class_name}