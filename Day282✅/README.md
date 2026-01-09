

# Day 282 -- House Price Prediction API (FastAPI + Machine Learning)

This project demonstrates a **production-style integration of a Machine Learning model with FastAPI**.
The model predicts **house prices** based on property features using supervised regression techniques.

---

## 🚀 Project Overview

* Trained multiple regression models using **scikit-learn**
* Used **GridSearchCV** to select the best-performing model
* Exported the trained model and encoders as `.pkl` files
* Built a **FastAPI backend** to serve real-time predictions via REST API

This project follows **industry best practices**:

* Training and serving are separated
* Input validation with Pydantic
* Clean project structure
* Ready for deployment

---

## 🧠 Machine Learning Details

**Dataset:** Housing.csv
**Target Variable:** `price`

### Models Trained

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regressor
* Gradient Boosting Regressor

**Model Selection:**
Best model selected using **5-Fold Cross Validation (R² score)** via GridSearchCV.

---

## 🧪 Model Evaluation

* **Metric Used:**

  * R² Score
  * RMSE (Root Mean Squared Error)

* The best model is saved as:

  ```
  best_model.pkl
  ```

---

## 📁 Project Structure

```
house_price_api/
│── app/
│   ├── main.py          # FastAPI entry point
│   ├── model.py         # Load ML model & encoders
│   ├── schemas.py       # Pydantic request schema
│── best_model.pkl
│── label_encoders.pkl
│── model_columns.pkl
│── requirements.txt
│── README.md
```

---

## 🔌 FastAPI Integration

### API Endpoint

**POST** `/predict`

### Sample Request

```json
{
  "area": 3500,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": "yes",
  "guestroom": "no",
  "basement": "yes",
  "hotwaterheating": "no",
  "airconditioning": "yes",
  "parking": 2,
  "prefarea": "yes"
}
```

### Sample Response

```json
{
  "predicted_price": 12450000.75
}
```

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

### 3️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Joblib

---

## 📌 Key Learnings

* ML model serving using FastAPI
* Proper preprocessing at inference time
* Handling categorical data with encoders
* Clean API-based ML deployment approach

---

## 📈 Future Improvements

* Use `Pipeline` & `ColumnTransformer`
* Replace `LabelEncoder` with `OneHotEncoder`
* Add Docker support
* Model versioning (MLflow)
* Frontend integration

---