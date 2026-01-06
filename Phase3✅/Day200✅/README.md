# Day200

---

## 🚢 Titanic Survival Prediction API

FastAPI + Scikit-learn based API jo Titanic dataset ke upar trained model ka use karke **survival prediction** karta hai.

---

### 📂 Project Structure

```
Day186/
│── app/
│   │── main.py              # FastAPI app
│   │── best_model.pkl       # Saved pipeline (model + preprocessing)
│   │── __init__.py
│── requirements.txt
│── README.md
```

---

### ⚡ Features

* REST API built with **FastAPI**
* Input features based on Titanic dataset:

  * `pclass` → Ticket class (1, 2, 3)
  * `sex` → "male" / "female"
  * `age` → Passenger age
  * `sibsp` → Number of siblings/spouses aboard
  * `parch` → Number of parents/children aboard
  * `fare` → Ticket fare
  * `embarked` → Port of embarkation (`C`, `Q`, `S`)
  * `who` → "man" / "woman" / "child"
* Returns:

  * `prediction` → 0 = Did not survive, 1 = Survived
  * `probability` → Survival probability (if available)

---

### 🔧 Installation

1. Clone repo / copy project:

   ```bash
   git clone <repo-url>
   cd Day186/app
   ```

2. Create & activate virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate # Linux/Mac
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### 🚀 Run API

Start server with Uvicorn:

```bash
uvicorn main:app --reload
```

API will run at:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)
👉 Interactive Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 📌 Example Request (via Swagger UI or Postman)

#### Request (JSON)

```json
{
  "pclass": 3,
  "sex": "male",
  "age": 22,
  "sibsp": 1,
  "parch": 0,
  "fare": 7.25,
  "embarked": "S",
  "who": "man"
}
```

#### Response

```json
{
  "prediction": 0,
  "probability": 0.08
}
```

---

### 🛠 Training & Model Pipeline

* Model trained on Titanic dataset using **Scikit-learn**
* Preprocessing (`OneHotEncoder`, `StandardScaler`) + ML model combined in **Pipeline**
* Saved using:

  ```python
  import joblib
  joblib.dump(best_pipeline, "best_model.pkl")
  ```

---
