# Day166

---

## 🐳 Docker Basics

Think of Docker as a way to package your app + all its dependencies (libraries, runtime, configs) into a single lightweight container that can run anywhere.
No more *“it works on my machine”* nonsense.

Key concepts you need:

* **Image** → blueprint of your app (like a class).
* **Container** → running instance of an image (like an object).
* **Dockerfile** → recipe that tells Docker how to build an image.
* **Docker Hub** → public app store for Docker images.

Common commands you’ll actually use:

```bash
# build an image from Dockerfile
docker build -t myapp .

# run a container from the image
docker run -d -p 8000:8000 myapp

# list running containers
docker ps

# stop a container
docker stop <container_id>

# remove container/image
docker rm <container_id>
docker rmi <image_id>
```

---

## 🌐 Hosting APIs with Docker

Let’s say you built a Python FastAPI app (same steps for Flask, Django, Node.js, etc.).

1. **Create a Dockerfile**

   ```dockerfile
   # base image
   FROM python:3.10

   # set working directory
   WORKDIR /app

   # install dependencies
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # copy app files
   COPY . .

   # expose port
   EXPOSE 8000

   # run app
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Build the image**

   ```bash
   docker build -t fastapi-app .
   ```

3. **Run the container**

   ```bash
   docker run -d -p 8000:8000 fastapi-app
   ```

4. **Test the API**
   Go to 👉 `http://localhost:8000`

---

## 🚀 Deploying the Container

You’ve got options:

* **Cheap & simple** → [Render](https://render.com), [Railway](https://railway.app), [Fly.io](https://fly.io)
* **DevOps big boy route** → AWS ECS/EKS, Azure, GCP
* **DIY** → VPS (like DigitalOcean, Linode) with Docker installed

In production, you’d usually:

* Use **docker-compose** to run app + DB + caching layers.
* Add **NGINX reverse proxy** for HTTPS.
* Automate builds with CI/CD (GitHub Actions, GitLab CI).

---

⚡ TL;DR:

* Docker = package once, run anywhere.
* Dockerfile = instructions to build your app image.
* `docker run -p` = expose API to outside world.
* For hosting, start small with Render/Fly.io before jumping into AWS/GCP hell.

---
