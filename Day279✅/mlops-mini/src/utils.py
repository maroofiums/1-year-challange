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