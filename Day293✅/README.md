# Day 293 - MyApp - Docker + Kubernetes Example

A simple Python Flask app deployed using Docker and Kubernetes.

---

## 1️⃣ Project Structure

```

myapp/
├── app.py                 # Main Flask app
├── requirements.txt       # Python dependencies
├── Dockerfile             # Build Docker image
├── .dockerignore          # Optional: ignore unnecessary files
├── deployment.yaml        # Kubernetes deployment
├── service.yaml           # Kubernetes service
└── README.md              # This file

````

---

## 2️⃣ Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- kubectl installed ([Install kubectl](https://kubernetes.io/docs/tasks/tools/))
- Kubernetes cluster ready (Minikube / Kind / Docker Desktop K8s)

---

## 3️⃣ Local Docker Run (Test App)

```bash
# Build Docker image
docker build -t myapp:1.0 .

# Run Docker container
docker run -p 5000:5000 myapp:1.0
````

* Open browser: `http://localhost:5000`

---

## 4️⃣ Kubernetes Deployment

**Step 1: Apply Deployment**

```bash
kubectl apply -f deployment.yaml
```

**Step 2: Apply Service**

```bash
kubectl apply -f service.yaml
```

**Step 3: Check Status**

```bash
kubectl get pods
kubectl get svc
```

* NodePort example: `http://localhost:<PORT>`

**Step 4: Scale Pods (Optional)**

```bash
kubectl scale deployment myapp --replicas=5
```

**Step 5: Cleanup**

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
```

---

## 5️⃣ Notes / Tips

* Fix dependency versions in `requirements.txt` → avoid production errors
* Use `.dockerignore` → smaller, faster builds
* Map container port correctly → host access possible
* Kubernetes health checks recommended for production

---

## 6️⃣ Optional Enhancements

* ConfigMaps & Secrets for environment variables
* Ingress / LoadBalancer for production traffic
* CI/CD pipeline for automated build and deploy

---
