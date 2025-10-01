import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

with open("iris_model.pkl","rb") as f:
    model = pickle.load(f)

class IrisFeature(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI(title="Iris Flower Classifier API")

@app.get("/")
def root():
    return {"message":"Welcome to the Iris Classifier API"}

@app.post("/predict")
def predict(features:IrisFeature):
    data = np.array([[features.sepal_length,features.sepal_width,
                      features.petal_length,features.petal_width]])
    prediction = model.predict(data)[0]
    return {"prediction":int(predict)}