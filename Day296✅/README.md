# Day296
---

## 1️⃣ How do you design a scalable FastAPI backend?

### 💡 Answer (Concept)

FastAPI scalable hota hai because:

* **ASGI-based** (async support)
* Works well with **Uvicorn / Gunicorn**
* Easy integration with **DB, cache, queues**

### 🧠 Design Thinking

```
Client
  ↓
Load Balancer
  ↓
FastAPI (multiple workers)
  ↓
PostgreSQL + Redis
```

### ✅ Best Practices

* Use `async def` **only** when I/O bound ho (DB, API calls)
* Multiple workers: `gunicorn -k uvicorn.workers.UvicornWorker`
* Use **connection pooling** (SQLAlchemy)

❌ Avoid:

* Heavy CPU tasks inside API (use background workers)

---

## 2️⃣ How do you handle database connections in FastAPI?

### 💡 Answer

Use **Session per request** pattern.

### 🧩 Example (SQLAlchemy)

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 🧠 Why?

* Har request ka apna DB session
* Memory leak nahi hota
* Thread-safe

❌ Avoid:

* Global DB session
* Manual open/close inside routes

---

## 3️⃣ SQL vs NoSQL — kab kya use karna chahiye?

### 📊 Simple Rule

| Use Case         | Choose |
| ---------------- | ------ |
| Relations        | SQL    |
| Transactions     | SQL    |
| Analytics        | SQL    |
| Logs / cache     | NoSQL  |
| High write scale | NoSQL  |

### 🧠 Real Example

* **User, Orders, Payments** → PostgreSQL
* **Sessions, OTPs** → Redis

💬 Advice:

> 90% backend apps = SQL first, NoSQL later

---

## 4️⃣ How do you design authentication system?

### 🔐 Typical Flow

```
User → Login
     → Verify Password
     → Generate JWT
     → Return Token
```

### 🧩 JWT Structure

* Header
* Payload (user_id)
* Signature

### ✅ Best Practice

* Short-lived access token
* Long-lived refresh token
* Store refresh token in DB

❌ Avoid:

* Storing password in JWT
* Long expiry access tokens

---

## 5️⃣ How do you optimize SQL queries?

### ⚡ Techniques

1. **Indexes**

```sql
CREATE INDEX idx_user_email ON users(email);
```

2. Avoid `SELECT *`
3. Use pagination (`LIMIT OFFSET`)
4. Proper joins

### 🧠 Rule

> Query slow hai → index lagao
> Still slow → query redesign

---

## 6️⃣ How do you handle migrations?

### 💡 Answer

Use **Alembic**

### 🧩 Workflow

```
Model change
→ alembic revision --autogenerate
→ alembic upgrade head
```

### ✅ Best Practice

* Never edit migration files randomly
* Production mein manual DB changes ❌

---

## 7️⃣ How do you design background tasks?

### Options

| Task Type | Tool                    |
| --------- | ----------------------- |
| Small     | FastAPI BackgroundTasks |
| Heavy     | Celery + Redis          |
| Async     | Task queue              |

### Example

```python
background_tasks.add_task(send_email, user.email)
```

❌ Avoid:

* Long tasks inside request-response cycle

---

## 8️⃣ How do you handle concurrency issues in SQL?

### Problem

Two users update same row → race condition 😬

### Solution

* Transactions
* Row-level locking

```sql
SELECT ... FOR UPDATE
```

### Advice

> Financial / stock systems → always transaction-first thinking

---

## 9️⃣ How do you design pagination?

### ❌ Bad

```sql
OFFSET 100000
```

### ✅ Good (Cursor-based)

* Use `id > last_id`
* Faster at scale

---

## 🔟 How do you secure FastAPI app?

### 🔒 Checklist

* HTTPS
* JWT
* Rate limiting
* Input validation (Pydantic)
* SQL Injection prevention (ORM)

---