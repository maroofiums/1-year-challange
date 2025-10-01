# Day141

## 🚀 1. What is FastAPI?

FastAPI is a modern, high-performance web framework for building APIs with **Python 3.7+** based on **type hints**.

* Built on **Starlette** (for web parts) and **Pydantic** (for data validation).
* Features: Automatic docs (Swagger & ReDoc), async support, fast execution.

---

## ⚙️ 2. Setup

### Install FastAPI and Uvicorn (ASGI server)

```bash
pip install fastapi uvicorn
```

### Create a basic app (`main.py`)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}
```

### Run the server

```bash
uvicorn main:app --reload
```

* `main` → filename (`main.py`)
* `app` → FastAPI instance
* `--reload` → Auto-reload when code changes

👉 Visit:

* **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** → API response
* **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** → Swagger UI
* **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)** → ReDoc

---

## 🛣️ 3. Routing in FastAPI

FastAPI provides decorators for HTTP methods:

### Example routes

```python
from fastapi import FastAPI

app = FastAPI()

# GET request
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# POST request
@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

# PUT request
@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item}

# DELETE request
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

---

## 📖 4. Path & Query Parameters

* **Path Parameter**: Comes from the URL path (`/items/{item_id}`)
* **Query Parameter**: Comes after `?` in the URL (`/items/5?q=hello`)

Example:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int, active: bool = True):
    return {"user_id": user_id, "active": active}
```

Call: `http://127.0.0.1:8000/users/1?active=false`

---