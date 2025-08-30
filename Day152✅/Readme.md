# Day152

---

## 1. FastAPI App (`main.py`)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI & Docker!"}
```

---

## 2. `requirements.txt`

```
fastapi
uvicorn[standard]
```

---

## 3. Dockerfile

```dockerfile
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 4. `.dockerignore` (optional but recommended)

```
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
.env
```

---

## 5. Build & Run

```bash
# Build image
docker build -t fastapi-app .

# Run container
docker run -d -p 8000:8000 fastapi-app
```

Now visit 👉 `http://localhost:8000`
Docs available at 👉 `http://localhost:8000/docs`

---

## 6. (Optional) `docker-compose.yml`

If you want to use Docker Compose:

```yaml
version: "3.9"

services:
  fastapi:
    build: .
    container_name: fastapi_app
    ports:
      - "8000:8000"
    volumes:
      - .:/app  # hot reload during development
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Then run:

```bash
docker-compose up --build
```

---
