
# Day162 FastAPI JWT Authentication

A simple FastAPI project demonstrating **JWT (JSON Web Token) authentication** with user login and protected routes.

---

## Features

- User login with username & password
- Password hashing with **bcrypt**
- JWT token creation & verification
- Protected endpoints that require a valid JWT
- Stateless authentication (no server-side sessions)

---

## Tech Stack

- **FastAPI** – Web framework
- **Python-JOSE** – JWT encoding & decoding
- **Passlib (bcrypt)** – Password hashing
- **Uvicorn** – ASGI server

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-jwt-auth.git
cd fastapi-jwt-auth
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt]
```

---

## Usage

1. Run the server:

```bash
uvicorn main:app --reload
```

2. Open the docs at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Endpoints:

| Endpoint    | Method | Description                    |
| ----------- | ------ | ------------------------------ |
| `/token`    | POST   | Login and get JWT token        |
| `/users/me` | GET    | Protected route (requires JWT) |

---

## Example Requests

**Login to get token:**

```bash
curl -X POST "http://127.0.0.1:8000/token" -F "username=maroof" -F "password=maroof123"
```

Response:

```json
{
  "access_token": "<your-jwt-token>",
  "token_type": "bearer"
}
```

**Access protected route:**

```bash
curl -H "Authorization: Bearer <your-jwt-token>" http://127.0.0.1:8000/users/me
```

Response:

```json
{
  "username": "maroof",
  "full_name": "Muhaamad Maroof",
  "hashed_password": "$2b$12$...",
  "disabled": false
}
```

---

## Security Notes

* **Never store plain text passwords** in production. Always use hashed passwords.
* Keep `SECRET_KEY` safe. Use environment variables or a vault.
* JWT tokens are stateless; implement **refresh tokens** for production use.

---
