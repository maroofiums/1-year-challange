# Day286 FastAPI x React Full-Stack App

A simple full-stack web application using **FastAPI** for the backend and **React** for the frontend.  
This project demonstrates **clean architecture, Dockerized backend, and API integration** with a responsive UI.

---

## 🔹 Features

- Backend
  - FastAPI REST API
  - Health check endpoint `/health`
  - Modular structure (`api/`, `core/`, `tests/`)
  - Dockerized for consistent development & deployment
  - Unit tests with `pytest`
  
- Frontend
  - React with React Router
  - Axios for API calls
  - Responsive and simple UI
  - Pages: Home, Backend Health Check

- Deployment Ready
  - Frontend → Vercel / Netlify
  - Backend → Render / Railway
  - CI/CD ready with GitHub Actions

---

## 🧱 Project Structure

```

backend/
├── app/
│    ├── main.py
│    ├── api/
│    ├── core/
│    └── tests/
├── requirements.txt
└── Dockerfile

frontend/
├── src/
│    ├── components/
│    ├── pages/
│    ├── App.js
│    └── index.js
└── package.json

````

---

## ⚡ Setup Instructions

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
````

* Open `http://127.0.0.1:8000/docs` for Swagger UI
* Run tests:

```bash
pytest app/tests
```

* Docker:

```bash
docker build -t fastapi-backend .
docker run -p 8000:8000 fastapi-backend
```

---

### 2. Frontend

```bash
cd frontend
npm install
npm start
```

* Open `http://localhost:3000/`

* Navigate to **Check Backend Health** page

* Production build:

```bash
npm run build
```

---

## 🌐 Environment Variables

* Backend: Use `.env` for secrets

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://user:pass@host/db
```

* Frontend: API URL

```env
REACT_APP_API_URL=http://localhost:8000
```

> **Important:** Do not commit `.env` file

---

## 🛠️ CI/CD

* GitHub Actions for CI:

  * Run backend tests
  * Build frontend
* Deployment:

  * Backend → Render / Railway
  * Frontend → Vercel / Netlify

---

