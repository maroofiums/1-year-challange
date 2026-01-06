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