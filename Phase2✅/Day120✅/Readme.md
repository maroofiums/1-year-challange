# Day 92
## 🚀 What is FastAPI?

**FastAPI** is a modern, fast (high-performance), web framework for building APIs with **Python 3.7+** based on standard Python type hints.
It’s built on **Starlette** (for the web parts) and **Pydantic** (for data validation).

### ✅ Key Features:

* Fast performance (comparable to NodeJS & Go)
* Automatic interactive API docs (Swagger UI / ReDoc)
* Built-in validation using Python type hints
* Async support using `async` / `await`

---

## 🛠️ 1. FastAPI Setup

### 🔹 Step 1: Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 🔹 Step 2: Install FastAPI and Uvicorn (ASGI server)

```bash
pip install fastapi uvicorn
```

---

## 🧭 2. Create Your First FastAPI App

### 📄 File: `main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
```

---

## 🚦 3. Run the FastAPI Server

Use **uvicorn** to run your FastAPI app:

```bash
uvicorn main:app --reload
```

* `main`: your Python file name (without `.py`)
* `app`: the FastAPI instance (`app = FastAPI()`)
* `--reload`: auto-reload on file changes (dev only)

---

## 📑 4. Auto-Generated API Docs

After running the server, open these in your browser:

* Swagger UI (default): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Example Routes

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

* `item_id`: path parameter (required)
* `q`: query parameter (optional)

Example:

```
GET /items/5?q=test
→ {"item_id": 5, "query": "test"}
```

---

## 🗂 Folder Structure (Simple Example)

```
fastapi_app/
├── main.py
├── requirements.txt
└── README.md
```

---

## ✅ Summary

| Feature    | Description                           |
| ---------- | ------------------------------------- |
| Setup      | `pip install fastapi uvicorn`         |
| Create App | `app = FastAPI()`                     |
| Routes     | Use `@app.get()`, `@app.post()`, etc. |
| Run App    | `uvicorn main:app --reload`           |
| Docs       | `/docs` and `/redoc`                  |

---

