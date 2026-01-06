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