# Day 118
---

### ✅ **Use Case Example:**

* Django handles: Auth system, Admin, Database models
* FastAPI handles: High-performance APIs (e.g., for ML, async endpoints)

---

## 🔧 Integration Options:

### 🔹 **Approach 1: Run both servers independently**

**Structure:**

```
project/
├── django_app/   (e.g., mysite/)
├── fastapi_app/  (main.py)
```

**How it works:**

* Django runs at `localhost:8000`
* FastAPI runs at `localhost:8001`
* React or Frontend calls whichever backend it needs
* You can deploy both under **Nginx reverse proxy** or use **API Gateway**

---

### 🔹 **Approach 2: Embed FastAPI in Django via ASGI**

**Requires:**

* Use **ASGI** (not WSGI) in Django
* Mount FastAPI app inside Django’s `asgi.py`

```python
# myproject/asgi.py
import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myproject.wsgi import application as django_app

fastapi_app = FastAPI()

@fastapi_app.get("/fastapi/")
def read_root():
    return {"message": "Hello from FastAPI"}

# Mount Django inside FastAPI
fastapi_app.mount("/django", WSGIMiddleware(django_app))
```

Now FastAPI will run and serve `/fastapi/`, and `/django/admin/` etc.

---

### 🔹 **Why Combine Them?**

| Feature       | Django              | FastAPI      |
| ------------- | ------------------- | ------------ |
| ORM & Admin   | ✅ Yes               | ❌ No         |
| Async Support | ❌ Limited (via DRF) | ✅ Excellent  |
| Performance   | 🚫 Slower           | 🚀 Very Fast |
| ML APIs       | 🟡 OK (via DRF)     | ✅ Ideal      |

---

## ✅ Deployment Tip:

Use `uvicorn` for FastAPI and `gunicorn` or `daphne` for Django (ASGI).
On production: setup **Nginx reverse proxy** to route traffic correctly.

---
