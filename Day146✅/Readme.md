# Day146

## 🧑‍💻 Project Idea: **Iris Flower Classifier API**

We’ll train a simple ML model (e.g., RandomForestClassifier) on the Iris dataset and deploy it with FastAPI so users can send flower features via an API and get the predicted species.

---

### 1. **Set Up Environment**

```bash
mkdir iris_api && cd iris_api
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)
pip install fastapi uvicorn scikit-learn pydantic
```

---

### 2. **Train and Save Model**

Create a file `train_model.py`:

```python
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved!")
```

Run it once:

```bash
python train_model.py
```

---

### 3. **Build FastAPI App**

Create a file `main.py`:

```python
import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# Load trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Input schema
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Initialize FastAPI
app = FastAPI(title="Iris Flower Classifier API")

@app.get("/")
def root():
    return {"message": "Welcome to the Iris Classifier API"}

@app.post("/predict")
def predict(features: IrisFeatures):
    data = np.array([[features.sepal_length, features.sepal_width,
                      features.petal_length, features.petal_width]])
    prediction = model.predict(data)[0]
    return {"prediction": int(prediction)}
```

---

### 4. **Run the API**

```bash
uvicorn main:app --reload
```

Visit:

* Swagger docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Root endpoint → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 5. **Test the API (Example cURL)**

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

Response:

```json
{"prediction": 0}
```

---

### 🔥 Possible Extensions

* ✅ Add model accuracy in `/metrics` endpoint
* ✅ Deploy to **Render**, **Railway**, or **Docker + AWS EC2**
* ✅ Add logging with `logging` module
* ✅ Support multiple models (e.g., Logistic Regression, SVM)

---

