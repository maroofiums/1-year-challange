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