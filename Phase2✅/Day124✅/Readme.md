# **Day 124**

# 📦 **Docker Basics & API Hosting**

---

## 🧠 **Goal:**

1. Docker ka basic concept samajhna
2. Django API ko Docker container me chalana
3. Localhost pe `localhost:8000` pe accessible API

---

## ✅ Step-by-Step Roadmap

### 🔹 Step 1: **Install Docker**

* Download: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
* Install karke `docker -v` command se verify karo.

---

### 🔹 Step 2: **Create Django REST API (if not already)**

```bash
django-admin startproject docker_api_demo
cd docker_api_demo
python manage.py startapp api
```

### 🔹 Step 3: **Make Simple API View**

Inside `api/views.py`:

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Dockerized Django API!"})
```

In `api/urls.py`:

```python
from django.urls import path
from .views import hello

urlpatterns = [
    path('', hello),
]
```

In `docker_api_demo/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

Also don't forget in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]
```

---

### 🔹 Step 4: **Create Dockerfile**

In root folder (`docker_api_demo/`), create a file named `Dockerfile`:

```Dockerfile
# Use official Python image
FROM python:3.11

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run migrations and start server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
```

---

### 🔹 Step 5: **Create requirements.txt**

```txt
Django>=4.0
djangorestframework
```

Run:

```bash
pip freeze > requirements.txt
```

---

### 🔹 Step 6: **Create docker-compose.yml**

```yaml
version: '3.9'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/code
```

---

### 🔹 Step 7: **Build & Run Docker**

```bash
docker-compose up --build
```

---

### ✅ Test

Open browser:

```
http://localhost:8000/api/
```

Should return:

```json
{ "message": "Hello from Dockerized Django API!" }
```

---

## 🧪 Practice Ideas

| Task                     | Skill                  |
| ------------------------ | ---------------------- |
| Add model to API         | Django ORM + Docker    |
| Connect PostgreSQL       | Multi-container Docker |
| Dockerize React Frontend | Full-Stack Docker      |
| Push Image to Docker Hub | Hosting skills         |
| Deploy to Render/VPS     | Real hosting           |

---

## 🔥 Summary

| Concept               | Status |
| --------------------- | ------ |
| Dockerfile Creation   | ✅      |
| Docker Compose        | ✅      |
| Django REST API Setup | ✅      |
| API Running in Docker | ✅      |
| Hosting Ready         | ✅      |

---

Agar tum chaho toh:

* React + Django dono ko dockerize karna sikha doon
* Ya `PostgreSQL` + Django with Docker bana doon
* Ya Dockerized app ko **Render**, **Railway**, ya **DigitalOcean** pe host karwana sikha doon
