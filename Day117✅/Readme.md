Here's a beginner-friendly guide to **Docker Basics & Hosting an API using Docker**, tailored especially for backend development with tools like **Django**, **FastAPI**, or **Flask**.

---

## 🚢 Docker Basics

### ❓ What is Docker?

Docker is a platform that allows you to **package** your application along with its **dependencies** into a **container**. This ensures your app runs the same in any environment (local, staging, production).

---

### 🧱 Key Concepts

| Term           | Meaning                                                               |
| -------------- | --------------------------------------------------------------------- |
| **Image**      | A blueprint of your app (like a class). Built from a `Dockerfile`.    |
| **Container**  | A running instance of an image (like an object).                      |
| **Dockerfile** | A text file with instructions to build a Docker image.                |
| **Docker Hub** | A repository of pre-built Docker images (like GitHub for containers). |
| **Volume**     | A way to persist data outside the container.                          |
| **Port**       | Used to expose app running inside Docker to outside (like 8000:8000). |


---

## 🗂️ Project Structure (Example)

```
myproject/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/  ← your Django app
│   └── ...
└── ...
```

---

## 📄 1. `Dockerfile`

```Dockerfile
# Use official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run Django app
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## 📄 2. `docker-compose.yml`

```yaml
version: '3.9'

services:
  web:
    build: .
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword

volumes:
  postgres_data:
```

---

## 📄 3. `requirements.txt`

```txt
Django>=4.2
djangorestframework
gunicorn
psycopg2-binary
```

> Add any other dependencies you're using.

---

## ⚙️ 4. `settings.py` Changes for PostgreSQL

In `settings.py`, update:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

And allow all hosts (for development):

```python
ALLOWED_HOSTS = ['*']
```

---

## 🚀 5. Run It All

1. Build and run containers:

```bash
docker-compose up --build
```

2. Run migrations:

```bash
docker-compose exec web python manage.py migrate
```

3. Create superuser (optional):

```bash
docker-compose exec web python manage.py createsuperuser
```

4. Access Django:

* Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)
* API: [http://localhost:8000/](http://localhost:8000/)

---

## 🧼 Optional Improvements

* ✅ Add `.dockerignore` to speed up build:

```txt
__pycache__
*.pyc
*.pyo
*.pyd
*.db
*.sqlite3
.env
```

* ✅ Use `.env` file + `python-decouple` or `dj-database-url` for production.

---

## 🛫 Want to Deploy?

Use [Render](https://render.com/) or [Railway](https://railway.app/) for free Docker hosting.

