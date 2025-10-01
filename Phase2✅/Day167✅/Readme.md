

# Day167 – Django (ViewSets + Admin) + FastAPI (Docs)

## 🚀 Project Setup

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 2. Install dependencies

```bash
pip install django djangorestframework fastapi uvicorn
```

---

## 🟢 Django Setup

### 1. Create Django project + app

```bash
django-admin startproject myproject
cd myproject
python manage.py startapp app
```

### 2. Add `rest_framework` and `app` in **myproject/settings.py**

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "app",
]
```

### 3. Define a model – **app/models.py**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
```

### 4. Create serializer – **app/serializers.py**

```python
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
```

### 5. Create ViewSet – **app/views.py**

```python
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
```

### 6. Register routes – **myproject/urls.py**

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
```

---

## 🟢 FastAPI Setup

### Create **main.py**

```python
from fastapi import FastAPI

app = FastAPI(title="FastAPI Docs Example")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/ping")
def ping():
    return {"pong": True}
```

---

## ▶️ Run Servers

### 1. Run Django (Port 8000)

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser   # for admin login
python manage.py runserver 8000
```

👉 Open:

* Django Admin → `http://127.0.0.1:8000/admin/`
* Django API (ViewSet) → `http://127.0.0.1:8000/api/books/`

---

### 2. Run FastAPI (Port 8001)

```bash
uvicorn main:app --reload --port 8001
```

👉 Open:

* Swagger Docs → `http://127.0.0.1:8001/docs`
* ReDoc → `http://127.0.0.1:8001/redoc`

---

## ✅ Final Result

* Django Admin → `/admin/`
* Django API (DRF ViewSet) → `/api/books/`
* FastAPI Docs (Swagger + ReDoc) → `/docs`, `/redoc`

👉 **Django handle karega Admin + REST APIs**
👉 **FastAPI handle karega Docs + apne routes**

---

⚡ Simple, clean, aur best practice development ke liye.
