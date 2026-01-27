import pandas as pd
import joblib

model = joblib.load("Models/churn_model.pkl")

# Example input with manual labels
data_dict = {
    "tenure": 12,
    "MonthlyCharges": 70.35,
    "TotalCharges": 845.5,
    "Contract": 0,
    "PaymentMethod": 2,
    "OnlineSecurity": 0,
    "TechSupport": 0,
    "InternetService": 0,
    "OnlineBackup": 2,
    "PaperlessBilling": 1,
    "MultipleLines": 0,
    "gender": 0,
    "DeviceProtection": 2,
    "Partner": 0,
    "Dependents": 0,
    "StreamingMovies": 0,
    "StreamingTV": 2
}

df = pd.DataFrame([data_dict])

# Fix: order features
FEATURE_ORDER = ['TotalCharges', 'MonthlyCharges', 'tenure', 'Contract', 
                 'OnlineSecurity', 'PaymentMethod', 'TechSupport', 'InternetService',
                 'OnlineBackup', 'PaperlessBilling', 'MultipleLines', 'gender',
                 'DeviceProtection', 'Partner', 'Dependents', 'StreamingMovies',
                 'StreamingTV']
df = df[FEATURE_ORDER]

pred = model.predict(df)[0]
prob = model.predict_proba(df)[0][1]

print(f"Prediction: {'Churn' if pred==1 else 'No Churn'}")
print(f"Churn Probability: {prob:.2f}")
