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