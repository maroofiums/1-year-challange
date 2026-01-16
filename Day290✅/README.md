# Day 290 - FastAPI Todo API

A simple and clean **Todo REST API** built with **FastAPI**, **SQLAlchemy ORM**, and **SQLite**.  
This project demonstrates **CRUD operations**, clean architecture, and best practices for backend development.

---

## 🚀 Features

- Create Todo
- Read all Todos
- Update Todo (title / completed)
- Delete Todo
- SQLite database
- SQLAlchemy ORM
- FastAPI dependency injection
- Clean project structure

---

## 🛠 Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **SQLite** – Database
- **Uvicorn** – ASGI server
- **Pydantic** – Data validation

---

## 📁 Project Structure

```

todo_app/
└── app/
├── main.py        # FastAPI app & routes
├── database.py    # Database connection
├── models.py      # SQLAlchemy models
├── schemas.py     # Pydantic schemas
└── crud.py        # CRUD logic

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/fastapi-todo.git
cd fastapi-todo
````

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

Swagger UI will open for API testing.

---

## 🔗 API Endpoints

### ➕ Create Todo

`POST /todos`

```json
{
  "title": "Learn FastAPI"
}
```

---

### 📄 Get All Todos

`GET /todos`

---

### ✏️ Update Todo

`PUT /todos/{id}`

```json
{
  "completed": true
}
```

---

### ❌ Delete Todo

`DELETE /todos/{id}`

---

## 🧠 Concepts Covered

* REST API design
* SQLAlchemy ORM
* Dependency Injection
* Data validation with Pydantic
* Clean architecture
* Separation of concerns

---

## 📌 Best Practices Used

* Separate CRUD logic
* Use schemas for request/response
* Database session per request
* Clean and scalable structure

---

## 📈 Future Improvements

* User Authentication (JWT)
* PostgreSQL support
* Async database
* Docker support
* Unit testing with Pytest

---