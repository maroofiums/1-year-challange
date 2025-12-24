# Day 268 - 🚀 FastAPI + MySQL + phpMyAdmin Starter Project

A simple FastAPI project connected with MySQL (via SQLAlchemy & PyMySQL), fully compatible with **phpMyAdmin**.  
This project demonstrates how to perform **CRUD operations (Create, Read, Update, Delete)** using FastAPI.

---

## 🧩 Features

- FastAPI for high-performance backend
- MySQL Database (via XAMPP / phpMyAdmin)
- SQLAlchemy ORM models
- CRUD API for managing users
- Pydantic validation schemas
- Auto-generated Swagger Docs (`/docs`)

---

## ⚙️ Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- PyMySQL
- XAMPP (for MySQL + phpMyAdmin)

---

## 🧰 Installation

### 1️⃣ Clone the Project

```bash
git clone https://github.com/yourusername/fastapi-mysql-starter.git
cd fastapi-mysql-starter
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql
```

---

## 🗃️ Database Setup (phpMyAdmin)

1. Open **XAMPP Control Panel**

   * Start **Apache** and **MySQL**

2. Go to **phpMyAdmin**

   * Create new database: `fastapi_db`

3. Update connection URL in `database.py` if needed:

   ```python
   DB_URL = "mysql+pymysql://root:@localhost/fastapi_db"
   ```

---

## 🧱 Project Structure

```
app/
 ┣ main.py         # FastAPI routes
 ┣ database.py     # DB engine & session
 ┣ models.py       # SQLAlchemy models
 ┗ schemas.py      # Pydantic schemas
```

---

## 🚦 Run the Server

```bash
uvicorn app.main:app --reload
```

Then visit:

* Swagger Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* phpMyAdmin → [http://localhost/phpmyadmin](http://localhost/phpmyadmin)

---

## 🧠 API Endpoints

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| POST   | `/users/`     | Create new user  |
| GET    | `/users/`     | Get all users    |
| GET    | `/users/{id}` | Get user by ID   |
| PUT    | `/users/{id}` | Update user info |
| DELETE | `/users/{id}` | Delete a user    |

---

## ✅ Example JSON (Create User)

```json
{
  "name": "Maroof",
  "email": "maroof@example.com"
}
```

---

## 🧩 Tips

* Always start MySQL server before running the app.
* If you get `Unknown database 'fastapi_db'` → create DB manually in phpMyAdmin.
* For production, add `.env` file to hide DB credentials.

---

## 🧑‍💻 Author

**Maroof**
Python Developer (ML, Backend, Arduino)
GitHub: [@maroof2424](https://github.com/maroof2424)

---

## ⭐ Future Improvements

* JWT Authentication (Login/Register)
* Relationships (User ↔ Posts)
* Docker Compose for FastAPI + MySQL
* Deployment on Render / Railway

---

### 💬 Summary

This project is the perfect starting point to learn how FastAPI interacts with a real SQL database using phpMyAdmin for management.
Once CRUD is clear, authentication and relationships become super easy to add next.


