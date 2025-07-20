import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("heart_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🫀 Heart Disease Prediction App")
st.write("Enter patient data to predict the risk of heart disease.")

# User input
age = st.number_input("Age", 20, 100, 45)
sex = st.selectbox("Sex", [0, 1])  # 0: Female, 1: Male
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.slider("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.slider("Max Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.slider("ST depression", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of peak", [0, 1, 2])
ca = st.selectbox("Major vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thal", [0, 1, 2])

# Prediction
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]])
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("❌ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk / No Heart Disease")
