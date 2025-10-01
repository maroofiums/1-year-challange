# Day 138

## **1. What is Docker?**

Docker is a platform to **package applications with all their dependencies** into a single container.
Think of it like a **portable app**: it runs the same on your laptop, server, or cloud.

**Key concepts:**

* **Image** → Blueprint of your app (read-only)
* **Container** → Running instance of an image
* **Dockerfile** → Instructions to build an image
* **Docker Hub** → Repository to store and share images
* **Volume** → Persistent storage for containers
* **Network** → Communication between containers

---

## **2. Install Docker**

* **Windows/Mac:** Download Docker Desktop
* **Linux:** `sudo apt install docker.io` (Ubuntu example)

Check installation:

```bash
docker --version
docker run hello-world
```

---

## **3. Docker Basics Commands**

```bash
docker pull <image>         # Download image
docker images               # List downloaded images
docker ps                   # List running containers
docker ps -a                # List all containers
docker run -p 8000:80 <image>  # Run container (map port 8000)
docker stop <container_id>  # Stop container
docker rm <container_id>    # Remove container
docker rmi <image>          # Remove image
```

---

## **4. Dockerfile for Python API**

Let’s say you have a **FastAPI** or **Flask** API.

**Directory structure:**

```
my_api/
 ├── app/
 │    └── main.py
 └── requirements.txt
 └── Dockerfile
```

**`main.py`** (FastAPI example):

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Docker!"}
```

**`requirements.txt`**:

```
fastapi
uvicorn[standard]
```

**Dockerfile**:

```dockerfile
# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose port
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## **5. Build & Run Docker Image**

```bash
# Build image
docker build -t my-fastapi-api .

# Run container
docker run -d -p 8000:8000 my-fastapi-api
```

Now your API is accessible at **[http://localhost:8000/](http://localhost:8000/)**.

---

## **6. Hosting API**

### **Option 1: Cloud VM (e.g., AWS EC2 / DigitalOcean)**

1. Install Docker on server
2. Copy your project (via Git or SCP)
3. Build & run the container
4. Open server port in firewall / security group

### **Option 2: Docker Hub + Cloud**

1. Tag and push image to Docker Hub:

```bash
docker tag my-fastapi-api maroof2424/my-fastapi-api:latest
docker push maroof2424/my-fastapi-api:latest
```

2. Pull & run on any server:

```bash
docker pull maroof2424/my-fastapi-api:latest
docker run -d -p 80:8000 maroof2424/my-fastapi-api:latest
```

---

## **7. Optional: Docker Compose**

If your API needs **database or multiple services**, use `docker-compose.yml`:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "8000:8000"
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
```

Run:

```bash
docker-compose up -d
```

---

✅ **Summary**

* Docker packages your API + dependencies → run anywhere
* Use **Dockerfile** to define environment
* Use **docker run** to start API
* Push to Docker Hub to deploy anywhere
* Use **docker-compose** for multi-container apps

---
