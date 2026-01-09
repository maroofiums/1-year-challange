import joblib

model = joblib.load("best_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
model_columns = joblib.load("model_columns.pkl")
