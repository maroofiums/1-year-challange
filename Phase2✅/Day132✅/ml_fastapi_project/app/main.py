from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model
with open("./model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Create FastAPI instance
app = FastAPI(title="Iris Flower Classifier")

# Request schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Routes
@app.get("/")
def home():
    return {"message": "Welcome to Iris Prediction API"}

@app.post("/predict")
def predict(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}
