
---

# 🚀 Day155

**FastAPI** is a modern, fast (high-performance) web framework for building APIs with Python.
Key features:

* **Fast**: Built on **Starlette** (for web) and **Pydantic** (for data validation).
* **Type-hint friendly**: Uses Python type hints to validate input/output automatically.
* **Async support**: First-class support for `async/await`.
* **Automatic docs**: Generates OpenAPI docs with **Swagger UI** and **ReDoc**.

---

## 🔧 Setup

1. **Install FastAPI** (and Uvicorn as the ASGI server):

```bash
pip install fastapi uvicorn
```

2. **Create a file** `main.py`:

```python
from fastapi import FastAPI

# Initialize app
app = FastAPI()

# Root route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

3. **Run the server**:

```bash
uvicorn main:app --reload
```

* `main` → filename (`main.py`)
* `app` → FastAPI instance
* `--reload` → auto-reload when code changes

4. Open in browser:

* API → `http://127.0.0.1:8000/`
* Swagger Docs → `http://127.0.0.1:8000/docs`
* ReDoc Docs → `http://127.0.0.1:8000/redoc`

---

## 🛣️ Routing in FastAPI

FastAPI supports standard HTTP methods with decorators:

### **1. GET Request**

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}
```

* `item_id` → path parameter (int validated automatically).
* `q` → query parameter (optional).

### **2. POST Request**

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}
```

* Body is parsed and validated with **Pydantic** model.

### **3. PUT Request**

```python
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "updated_item": item}
```

### **4. DELETE Request**

```python
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} deleted"}
```

---

✅ At this point, you’ve:

* Installed and set up FastAPI
* Created routes (`GET`, `POST`, `PUT`, `DELETE`)
* Seen how automatic docs are generated

---

