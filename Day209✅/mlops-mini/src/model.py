from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler




def build_model():
pipe = Pipeline([
("scaler", StandardScaler()),
("clf", RandomForestClassifier(n_estimators=100, random_state=42))
])
return pipe