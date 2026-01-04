# Day 279 - MLOps Project (FastAPI + CI/CD + Docker + Simple ML)

**Short:** Ye repo ek minimal, realistic MLOps pipeline ka skeleton provide karta hai — training, model saving, FastAPI serving, unit tests, Dockerfile, aur GitHub Actions CI. Tu is repo ko locally run kar ke samajh sakta hai, phir DVC/MLflow add karna asaan hoga.

---

## Project structure

```
mlops-mini/
├─ README.md
├─ requirements.txt
├─ Dockerfile
├─ .github/workflows/ci.yml
├─ src/
│  ├─ data_utils.py
│  ├─ train.py
│  ├─ model.py
│  └─ utils.py
├─ app/
│  └─ main.py
└─ tests/
   └─ test_train_and_api.py
```

---

## What I included (files with code)

> Note: code blocks below are the actual files. Copy them into your project files.

---

### `requirements.txt`

```text
fastapi==0.95.2
uvicorn[standard]==0.22.0
scikit-learn==1.3.2
joblib==1.3.2
pydantic==1.10.9
pytest==7.4.2
requests==2.33.0
python-multipart==0.0.6
```

---

### `src/data_utils.py`

```python
from sklearn.datasets import make_classification
import pandas as pd
import os

def generate_dummy_data(n_samples=1000, n_features=10, out_path=None):
    X, y = make_classification(n_samples=n_samples, n_features=n_features, n_informative=6, random_state=42)
    cols = [f"f{i}" for i in range(X.shape[1])]
    df = pd.DataFrame(X, columns=cols)
    df["target"] = y
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        df.to_csv(out_path, index=False)
    return df
```

---

### `src/utils.py`

```python
import joblib
from sklearn.model_selection import train_test_split
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")

def save_model(model, name="best_model.joblib"):
    path = os.path.abspath(os.path.join(MODEL_DIR, name))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    return path


def load_model(path):
    return joblib.load(path)


def make_splits(df, target_col="target", test_size=0.2, random_state=42):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
```

---

### `src/model.py`

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_model():
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    return pipe
```

---

### `src/train.py`

```python
import argparse
from data_utils import generate_dummy_data
from utils import make_splits, save_model
from model import build_model
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


def train(run_save=True, data_path=None):
    # 1) load or generate data
    if data_path:
        df = pd.read_csv(data_path)
    else:
        df = generate_dummy_data(n_samples=500)

    # 2) train/test split
    X_train, X_test, y_train, y_test = make_splits(df)

    # 3) build and train
    model = build_model()
    model.fit(X_train, y_train)

    # 4) eval
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)

    print(f"Accuracy: {acc:.4f}")
    print(report)

    # 5) save model
    if run_save:
        path = save_model(model)
        print("Saved model to:", path)
        return {"acc": float(acc), "model_path": path}
    return {"acc": float(acc), "model": model}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default=None)
    parser.add_argument("--no-save", dest="save", action="store_false")
    args = parser.parse_args()
    train(run_save=args.save, data_path=args.data)
```

---

### `app/main.py` (FastAPI)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import os
import sys

# make sure src package is importable when running via `uvicorn app.main:app`
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.append(ROOT)

from src.utils import load_model

MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models", "best_model.joblib"))

class PredictRequest(BaseModel):
    features: list

app = FastAPI(title="ML Model API")

# lazy load
_model = None

def get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise RuntimeError(f"Model not found at {MODEL_PATH} — run training first")
        _model = load_model(MODEL_PATH)
    return _model


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: PredictRequest):
    model = get_model()
    X = [req.features]
    pred = model.predict(X).tolist()[0]
    return {"prediction": int(pred)}
```

---

### `Dockerfile`

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

---

### `.github/workflows/ci.yml` (GitHub Actions)

```yaml
name: CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest -q

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          push: true
          tags: ${{ secrets.DOCKERHUB_USERNAME }}/mlops-mini:latest
```

> Note: For deployment to Render / Railway / GCP you can instead push the Docker image or use their GitHub integration.

---

### `tests/test_train_and_api.py`

```python
import os
import tempfile
from src.train import train
from fastapi.testclient import TestClient

# This test trains a tiny model and checks the predict endpoint

def test_train_and_api():
    res = train(run_save=True)
    assert "acc" in res
    model_path = res["model_path"]
    assert os.path.exists(model_path)

    # start fastapi app via TestClient
    from app.main import app
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

    # prepare a dummy feature vector (size must match the training features)
    # our generated data uses 10 features
    sample = [0.0] * 10
    r2 = client.post("/predict", json={"features": sample})
    assert r2.status_code == 200
    assert "prediction" in r2.json()
```

---

## How to run locally (step-by-step)

1. Create virtualenv and install

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Train and save model

```bash
python src/train.py
# this prints accuracy and writes models/best_model.joblib
```

3. Run the API

```bash
uvicorn app.main:app --reload --port 8000
# then open http://localhost:8000/docs to test
```

4. Run tests

```bash
pytest -q
```

5. Build Docker image

```bash
docker build -t mlops-mini:local .
docker run -p 8000:80 mlops-mini:local
```

---

## Next steps (recommended)

1. Add **DVC** for data versioning (dvc init; dvc add data/raw.csv; push to remote storage).
2. Add **MLflow** or Weights & Biases for experiment tracking and model registry.
3. Add **staging** & **production** environments in CI; separate model promotion.
4. Add monitoring: Prometheus for API + EvidentlyAI for data/model drift.

---

## Final notes

Main goal: ye skeleton tujhe ek working end-to-end pipeline dikhata hai jise tu aage extend kar sakta hai. Agar tu chaahe, main ab is repo ko step-by-step GitHub repo format mein push karne ka exact `git` commands aur `dvc`/`mlflow` integration code bhi likh dunga.

Good luck — bolo kahan se start karna hai next?

<!-- end of document -->
