# Day 310 - FastAPI OAuth2 Authentication (JWT)

This project demonstrates **basic authentication in FastAPI** using **OAuth2 Password Flow** with **JWT (JSON Web Tokens)**.

It covers:

* Login using username & password
* JWT access token generation
* Protecting routes using OAuth2
* Testing via Swagger UI

---

## 🚀 Tech Stack

* Python
* FastAPI
* OAuth2 (Password Bearer)
* JWT (python-jose)

---

## 📂 Project Structure

```
├── app
│   └── main.py
└── README.md
```

---

## 🔐 Authentication Flow (Simple Explanation)

1. User sends **username & password** to `/token`
2. Server verifies credentials
3. Server generates a **JWT access token**
4. Client sends token in headers:

   ```
   Authorization: Bearer <token>
   ```
5. Protected routes verify the token before allowing access

---

## ⚙️ Setup & Installation

### 1. Create virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 2. Install dependencies

```
pip install fastapi uvicorn python-jose[cryptography]
```

---

### 3. Run the application

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation (Swagger UI)

Open in browser:

```
http://127.0.0.1:8000/docs
```

FastAPI provides interactive Swagger UI for testing authentication.

---

## 🔑 Login (Get Access Token)

### Endpoint

```
POST /token
```

### Credentials (Demo)

```
username: admin
password: password
```

### Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

## 🔒 Access Protected Route

### Endpoint

```
GET /protected
```

### Header

```
Authorization: Bearer <your_access_token>
```

### Response

```json
{
  "message": "Hello admin, you are authenticated!"
}
```

If token is missing or invalid, API returns **401 Unauthorized**.

---

## 🧪 Testing with Swagger UI

1. Call `/token` and copy the token
2. Click **Authorize** (top-right)
3. Paste:

   ```
   Bearer <token>
   ```
4. Access `/protected`

---

## ⚠️ Important Notes

* Passwords are **hardcoded** (for learning only)
* Secret key is **not secure** (use `.env` in production)
* No database is used in this demo

---