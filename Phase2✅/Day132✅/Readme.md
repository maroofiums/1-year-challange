# Day 132

---

## **📌 Project Overview**

We’ll train a **simple ML model** (e.g., predicting house prices or classifying iris flowers) using `scikit-learn`, save it, and then create a **FastAPI** app to serve predictions via an API endpoint.

---

## **📂 Folder Structure**

```
ml_fastapi_project/
├── model/
│   ├── train_model.py
│   └── model.pkl
├── app/
│   ├── main.py
│   ├── schemas.py
│   └── requirements.txt
└── README.md
```

---

## **🔹 Step 1 — Train & Save Model (`model/train_model.py`)**

```python
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
```

---

## **🔹 Step 2 — FastAPI App (`app/main.py`)**

```python
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model
with open("model/model.pkl", "rb") as f:
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
```

---

## **🔹 Step 3 — Requirements (`app/requirements.txt`)**

```
fastapi
uvicorn
scikit-learn
numpy
pydantic
```

---

## **🔹 Step 4 — Run API**

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload
```

Visit:

* **Docs** → `http://127.0.0.1:8000/docs`
* **Prediction** → Use `POST /predict`

---

## **🔹 Step 5 — Test with JSON**

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:

```json
{
  "prediction": 0
}
```

---

✅ **Skills Practiced**

* ML Model training & serialization (`pickle`)
* FastAPI request validation with `pydantic`
* REST API endpoint creation
* Testing via `/docs` or Postman

