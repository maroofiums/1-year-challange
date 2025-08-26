# Day 148

# FastAPI Resume Manager with JWT Authentication

This is a simple FastAPI application to manage resumes with JWT-based user authentication.

## Features

* User authentication with JWT access tokens
* CRUD operations on resumes (create, read one, read all, update, delete)
* Password hashing with bcrypt
* Protected API endpoints requiring valid JWT token

---

## Requirements

* Python 3.8+
* FastAPI
* `python-jose` for JWT handling
* `passlib[bcrypt]` for password hashing
* `uvicorn` for running the server

Install dependencies:

```bash
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt]
```

---

## How to Run

1. Save the FastAPI code in a file, e.g. `main.py`.

2. Run the FastAPI app with:

```bash
uvicorn main:app --reload
```

3. The API docs will be available at:

* Swagger UI: `http://localhost:8000/docs`
* ReDoc: `http://localhost:8000/redoc`

---

## Authentication

### Obtain JWT Token

Send a POST request to `/token` with form data:

* `username`: your username (default user is `maroof`)
* `password`: your password (default is `password123`)

Example using `curl`:

```bash
curl -X POST "http://localhost:8000/token" -d "username=maroof&password=password123"
```

You will receive a JSON response containing the JWT access token:

```json
{
  "access_token": "<your_token_here>",
  "token_type": "bearer"
}
```

---

### Use the Token

For all protected endpoints, include the token in the HTTP Authorization header:

```
Authorization: Bearer <your_token_here>
```

---

## API Endpoints

| Method | Endpoint           | Description              | Protected |
| ------ | ------------------ | ------------------------ | --------- |
| POST   | `/token`           | Obtain JWT token         | No        |
| POST   | `/resumes/`        | Create a new resume      | Yes       |
| GET    | `/resumes/{email}` | Get a resume by email    | Yes       |
| GET    | `/resumes/`        | Get all resumes          | Yes       |
| PUT    | `/resumes/{email}` | Update a resume by email | Yes       |
| DELETE | `/resumes/{email}` | Delete a resume by email | Yes       |

---

## Default User Credentials

| Username | Password    |
| -------- | ----------- |
| maroof   | password123 |

> **Note:** For production, use a secure secret key and manage users properly.

---

## Security Notes

* Change the `SECRET_KEY` to a strong, random value before deploying.
* Store hashed passwords securely.
* Consider adding refresh tokens and user registration.
