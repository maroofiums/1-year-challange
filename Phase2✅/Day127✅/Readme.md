# Day 127

## 🔹 What is FastAPI?

**FastAPI** is a modern, fast (high-performance) web framework for building APIs with **Python 3.7+** based on standard **Python type hints**.

### ✅ Key Features:

* Fast (built on **Starlette** and **Pydantic**)
* Automatic interactive API docs (Swagger UI, ReDoc)
* Type checking & validation using Python type hints
* Asynchronous support with `async`/`await`

---

## 📦 1. Installation

Create a virtual environment and install FastAPI and Uvicorn:

```bash
# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # On Linux: source venv/bin/activate

# Install FastAPI and Uvicorn (ASGI server)
pip install fastapi uvicorn
```

---

## 🚀 2. Your First FastAPI App

**main.py**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

### ▶️ Running the App

```bash
uvicorn main:app --reload
```

* `main` is the filename (main.py)
* `app` is the FastAPI instance
* `--reload` enables auto-reload on code changes

---

## 🌐 3. Routing Basics

### 📥 HTTP Methods: `GET`, `POST`, `PUT`, `DELETE`

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### 📝 Path Parameters

* `item_id: int` → type checked
* FastAPI converts and validates the type

### ✅ Query Parameters

* `q: str = None` → optional query param

---

## 📄 4. Automatic Documentation

Once the server is running, visit:

* **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

FastAPI generates these from type hints and route definitions.

---

## 📁 5. Directory Structure (Basic Example)

```
project/
├── main.py
├── venv/
└── requirements.txt
```

---
