# Day180

---

## 🚀 Docker Basics

Think of Docker as a **mini virtual computer** that runs only what you need (your app + its dependencies).
Instead of “it works on my machine” chaos, you can ship a container and it’ll run the same way anywhere.

Key stuff:

* **Image** → Recipe for your app (what to install, what to run).
* **Container** → A running instance of an image (your app actually alive).
* **Dockerfile** → Instructions to build your image.
* **Docker Hub / Registry** → Where you store/share your images (like GitHub but for containers).
* **Volumes** → Persist data (so your stuff doesn’t vanish when the container stops).
* **Ports** → Map your container’s app to your host machine so the outside world can hit it.

---

## 🔌 Hosting APIs with Docker

Let’s say you’ve built a Python API with **FastAPI** or **Flask**. Here’s the workflow:

1. **Write a Dockerfile**
   Example (FastAPI):

   ```dockerfile
   # Base image
   FROM python:3.11-slim

   # Set working dir
   WORKDIR /app

   # Install dependencies
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy app files
   COPY . .

   # Run app
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Build your image**

   ```bash
   docker build -t my-api .
   ```

3. **Run your container**

   ```bash
   docker run -d -p 8000:8000 my-api
   ```

   * `-d` → detached mode
   * `-p 8000:8000` → maps container port 8000 to host port 8000

4. **Check it works**
   Open: [http://localhost:8000](http://localhost:8000)

---

## 🌍 Hosting Options

Once you’ve got your container running locally, you need to put it somewhere people can reach.

* **Cheap/Easy:**

  * Render, Railway, Fly.io → Free tiers, great for quick APIs.
* **Cloud Big Boys:**

  * AWS ECS/EKS, GCP Cloud Run, Azure Container Apps.
  * More power but more setup.
* **DIY VPS:**

  * Rent a server (e.g. DigitalOcean, Hetzner) → install Docker → run your container.
  * Good balance of cost + control.

---

## 🧠 Pro Tips

* Always `.dockerignore` stuff like `venv/`, `.git/`, and `__pycache__`.
* Use **multi-stage builds** if your container’s getting chunky.
* Expose healthchecks (so hosting providers know your app’s alive).
* For production: slap **Nginx** or a reverse proxy in front.

---

