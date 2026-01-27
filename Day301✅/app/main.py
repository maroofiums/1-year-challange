import streamlit as st
import pandas as pd
import joblib
import os

# --- Load model ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "Models")
model = joblib.load(os.path.join(MODEL_DIR, "churn_model.pkl"))

# --- Manual label mappings ---
manual_label_mappings = {
    'gender': ['Female', 'Male'],
    'Partner': ['No', 'Yes'],
    'Dependents': ['No', 'Yes'],
    'MultipleLines': ['No', 'No phone service', 'Yes'],
    'InternetService': ['DSL', 'Fiber optic', 'No'],
    'OnlineSecurity': ['No', 'No internet service', 'Yes'],
    'OnlineBackup': ['No', 'No internet service', 'Yes'],
    'DeviceProtection': ['No', 'No internet service', 'Yes'],
    'TechSupport': ['No', 'No internet service', 'Yes'],
    'StreamingTV': ['No', 'No internet service', 'Yes'],
    'StreamingMovies': ['No', 'No internet service', 'Yes'],
    'Contract': ['Month-to-month', 'One year', 'Two year'],
    'PaperlessBilling': ['No', 'Yes'],
    'PaymentMethod': ['Bank transfer (automatic)', 'Credit card (automatic)', 'Electronic check', 'Mailed check']
}

# --- Column order for the model ---
model_features = [
    'TotalCharges', 'MonthlyCharges', 'tenure', 'Contract',
    'OnlineSecurity', 'PaymentMethod', 'TechSupport', 'InternetService',
    'OnlineBackup', 'PaperlessBilling', 'MultipleLines', 'gender',
    'DeviceProtection', 'Partner', 'Dependents', 'StreamingMovies',
    'StreamingTV'
]

# --- Mapping function ---
mapping_numbers = {
    'gender': {'Female': 0, 'Male': 1},
    'Partner': {'No': 0, 'Yes': 1},
    'Dependents': {'No': 0, 'Yes': 1},
    'MultipleLines': {'No': 0, 'No phone service': 1, 'Yes': 2},
    'InternetService': {'DSL': 0, 'Fiber optic': 1, 'No': 2},
    'OnlineSecurity': {'No': 0, 'No internet service': 1, 'Yes': 2},
    'OnlineBackup': {'No': 0, 'No internet service': 1, 'Yes': 2},
    'DeviceProtection': {'No': 0, 'No internet service': 1, 'Yes': 2},
    'TechSupport': {'No': 0, 'No internet service': 1, 'Yes': 2},
    'StreamingTV': {'No': 0, 'No internet service': 1, 'Yes': 2},
    'StreamingMovies': {'No': 0, 'No internet service': 1, 'Yes': 2},
    'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
    'PaperlessBilling': {'No': 0, 'Yes': 1},
    'PaymentMethod': {'Bank transfer (automatic)': 0, 'Credit card (automatic)': 1,
                      'Electronic check': 2, 'Mailed check': 3}
}

def map_manual_labels(data_dict):
    """Convert categorical text to numbers based on manual mapping."""
    for col, mapping in mapping_numbers.items():
        if col in data_dict:
            data_dict[col] = mapping[data_dict[col]]
    return data_dict

# --- Streamlit UI ---
st.title("Customer Churn Prediction 🚀")
st.write("Fill in the details below to predict if a customer will churn.")

# --- Numeric Inputs ---
col1, col2, col3 = st.columns(3)
tenure = col1.number_input("Tenure (months)", min_value=0, value=12)
MonthlyCharges = col2.number_input("Monthly Charges", min_value=0.0, value=70.0)
TotalCharges = col3.number_input("Total Charges", min_value=0.0, value=845.0)

# --- Categorical Inputs ---
inputs = {}
for col, options in manual_label_mappings.items():
    inputs[col] = st.selectbox(col, options)

# --- Predict Button ---
if st.button("Predict Churn"):
    # Prepare data
    data_dict = {
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        **inputs
    }

    # Map labels to numbers
    data_dict = map_manual_labels(data_dict)

    # Convert to DataFrame and order features
    df = pd.DataFrame([data_dict])
    df = df[model_features]

    # Predict
    try:
        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]
        st.success(f"Prediction: {'Churn' if pred == 1 else 'No Churn'}")
        st.info(f"Churn Probability: {prob:.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
    