# Day 111

---

## ✅ Step-by-Step Guide to Run Streamlit in Google Colab

---

### 🔹 Step 1: Setup — Install Required Packages

```python
!pip install streamlit
!pip install pyngrok
```

---

### 🔹 Step 2: Create the Streamlit App (`app.py`)

You can write the app code in a cell and save it:

```python
%%writefile app.py
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
```

---

### 🔹 Step 3: Train & Save Model (`heart_model.pkl`)

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Download dataset from GitHub or manually upload
url = "https://raw.githubusercontent.com/dataprofessor/data/master/heart_disease.csv"
df = pd.read_csv(url)

# Train model
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open("heart_model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

### 🔹 Step 4: Run Streamlit with `pyngrok`

```python
from pyngrok import ngrok

# Open tunnel
public_url = ngrok.connect(port=8501)
print("🌐 Streamlit URL:", public_url)

# Run Streamlit
!streamlit run app.py &>/dev/null &
```

---

## ✅ Output

You’ll get a public URL like:
