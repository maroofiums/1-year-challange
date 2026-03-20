# Day 352

# 🌸 Iris Classification API (FastAPI + Machine Learning)

A simple Machine Learning API built using **FastAPI** that predicts the species of an iris flower based on input features.

---

## 🚀 Features

* Trained on the Iris dataset
* FastAPI-based REST API
* Input validation using Pydantic
* Returns predicted class with label
* Easy to extend and deploy

---

## 🧠 Model Details

* Algorithm: Random Forest Classifier
* Dataset: Iris Dataset
* Features:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width

---

## 📁 Project Structure

```
Day352
├── app
│   ├── clf_model.pkl
│   └── main.py
└── README.md
```

---
## 🏋️ Train the Model

Run the training script to generate the model file:

```
python train_model.py
```

This will create:

```
iris_model.pkl
```

---

## ▶️ Run the API

Start the FastAPI server:

```
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Usage

### Endpoint: `/predict`

**POST Request**

#### Request Body:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

#### Response:

```json
{
  "prediction": 0,
  "class_name": "setosa"
}
```

---

## 🧪 Example using cURL

```
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{"sepal_length":5.1,"sepal_width":3.5,"petal_length":1.4,"petal_width":0.2}'
```

---

## 📦 Requirements

```
fastapi
uvicorn
scikit-learn
numpy
joblib
pydantic
```

---

