# FastAPI\_X\_ML 🚀

A simple **Machine Learning Prediction API** built with **FastAPI**.
This project uses a trained **Random Forest model** on the **Iris dataset** to classify flower species.

---

## 📂 Project Structure

```
FastAPI_X_ML/
│── app/
│   ├── main.py        # FastAPI app
│   ├── model.pkl      # Trained ML model
│── train_model.py     # Script to train & save model
│── README.md
```

---

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/FastAPI_X_ML.git
   cd FastAPI_X_ML
   ```

2. Create virtual environment & install requirements:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows

   pip install fastapi uvicorn scikit-learn numpy pydantic
   ```

---

## 🧠 Train Model

Run the training script to generate `model.pkl`:

```bash
python train_model.py
```

---

## 🚀 Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server will run at:
👉 `http://127.0.0.1:8000`

---

## 📌 API Endpoints

### 1. Root Endpoint

`GET /`
**Response:**

```json
{"message": "Welcome to Iris Prediction API 🚀"}
```

---

### 2. Predict Endpoint

`POST /predict`

**Request Body:**

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**

```json
{
  "prediction": "setosa"
}
```

---

## 🛠️ Technologies Used

* Python 🐍
* FastAPI ⚡
* scikit-learn 🤖
* Pydantic 📝
* Uvicorn 🔥

---

## 🌟 Future Improvements

* Add **confidence score** with predictions
* Log predictions in a file
* Deploy API to **Render / Railway / HuggingFace Spaces**

---

💡 **Pro Tip:** Use [Swagger UI](http://127.0.0.1:8000/docs) or [Redoc](http://127.0.0.1:8000/redoc) for interactive API testing.

---
