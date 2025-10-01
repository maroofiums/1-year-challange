# Day139

* Django use hoga **admin panel ke liye** aur database models ke liye.
* FastAPI use hoga **API endpoints ke liye**.
* Dono same database share karenge.

---

### 1️⃣ Django Setup

```bash
# Django project create karo
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

**myapp/models.py**:

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

**myapp/admin.py**:

```python
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```

**myproject/settings.py** me `INSTALLED_APPS` me add karo:

```python
INSTALLED_APPS = [
    ...,
    'myapp',
]
```

```bash
# migrations
python manage.py makemigrations
python manage.py migrate
```

```bash
# admin user create karo
python manage.py createsuperuser
```

Run karo Django admin:

```bash
python manage.py runserver
```

Admin panel chalega: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

### 2️⃣ FastAPI Setup

```bash
pip install fastapi uvicorn django
```

**fastapi\_app.py**:

```python
import os
import django
from fastapi import FastAPI
from pydantic import BaseModel

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Item

app = FastAPI(title="FastAPI + Django Example")

class ItemSchema(BaseModel):
    id: int
    name: str
    description: str

@app.get("/items")
def get_items():
    items = Item.objects.all()
    return [ItemSchema(id=item.id, name=item.name, description=item.description) for item in items]

@app.post("/items")
def create_item(item: ItemSchema):
    obj = Item.objects.create(name=item.name, description=item.description)
    return {"id": obj.id, "name": obj.name, "description": obj.description}

```

Run FastAPI:

```bash
uvicorn fastapi_app:app --reload
```

Swagger docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

✅ **Result:**

* Django admin se data manage karo.
* FastAPI endpoints se same data read/write karo.
* Dono **same database** use kar rahe hain.

---


