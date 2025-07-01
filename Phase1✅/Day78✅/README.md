# Day 77

Welcome to Day 77 of the 365 Days of Code Challenge!

### API Development Overview (REST & JWT)

---

#### 🔹 **What is an API?**

An **API (Application Programming Interface)** allows two software systems to communicate with each other. APIs define how requests should be made, what data should be used, and what kind of responses you can expect.

---

### 🔸 REST API (Representational State Transfer)

#### ✅ **Key Features:**

* Stateless: Each request contains all information needed
* Uses HTTP methods: GET, POST, PUT, DELETE
* Data typically exchanged in JSON
* Resource-based URLs: `/users/1`, `/products`

#### 🌐 **Common HTTP Methods:**

| Method | Description           | Example        |
| ------ | --------------------- | -------------- |
| GET    | Read data             | `/api/users`   |
| POST   | Create data           | `/api/users`   |
| PUT    | Update entire record  | `/api/users/1` |
| PATCH  | Update part of record | `/api/users/1` |
| DELETE | Delete data           | `/api/users/1` |

---

### 🔸 JWT (JSON Web Token)

#### 🔐 **Purpose:**

JWT is used for **authentication** and **authorization** in APIs.

#### 🧱 **Structure of JWT:**

```
xxxxx.yyyyy.zzzzz
|     |     |
|     |     └─ Signature
|     └─────── Payload (data like user_id, role)
└───────────── Header (algorithm & type)
```

#### 🔁 **How JWT works:**

1. **Login** – User logs in with credentials.
2. **Token Generation** – Server sends back a JWT.
3. **Client Stores Token** – Usually in localStorage or cookies.
4. **Authenticated Requests** – Client includes JWT in headers (`Authorization: Bearer <token>`).
5. **Server Verifies Token** – Using a secret key.

---

### 🔧 Example Flow in API

1. **User registers**: `POST /api/register`
2. **User logs in**: `POST /api/login`

   * Server returns JWT
3. **User gets profile**: `GET /api/profile`

   * JWT is sent in header for access

---

### 💡 Tech Stack Example (for REST & JWT)

* **Backend:** Node.js (Express) / Python (Flask or Django)
* **JWT Library:**

  * Node.js: `jsonwebtoken`
  * Python: `PyJWT`
* **Database:** MongoDB / PostgreSQL / MySQL

---

### 🛡 Best Practices

* Use HTTPS
* Set token expiry (e.g., 15 min access token, refresh token)
* Store secrets securely (env files)
* Validate & sanitize all inputs
* Implement rate limiting & logging
