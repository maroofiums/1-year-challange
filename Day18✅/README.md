# Day 18

Welcome to Day 18 of the 365 Days of Code Challenge!
Sure Maroof! Here's a **basic explanation** of **API Development (REST + JWT)** in **simple language**:

---

## 🔹 What is an API?

**API** means **Application Programming Interface**.
It lets two apps talk to each other.

Example:

* Your **frontend (HTML/JS)** asks the **backend (Django)**:
  ➤ “Hey, give me all products.”
  ➤ Backend sends the data in **JSON** format.

---

## 🔹 What is a REST API?

**REST** = a style of building APIs using simple rules:

* **GET** → Get data
* **POST** → Send data
* **PUT/PATCH** → Update data
* **DELETE** → Delete data

So your API will have routes like:

* `GET /api/products/` → Get all products
* `POST /api/products/` → Add a new product
* `GET /api/products/2/` → Get product with ID 2
* `PUT /api/products/2/` → Update product 2
* `DELETE /api/products/2/` → Delete product 2

---

## 🔹 What is JWT?

**JWT** means **JSON Web Token**
It is a way to **log in** users and keep them **authenticated**.

### Example:

1. User logs in → You give a **token**
2. User sends the token in every request:

   ```
   Authorization: Bearer <token>
   ```
3. Backend checks the token → If it’s valid, user is allowed.

---

## 🔹 What is Django REST Framework (DRF)?

DRF is a Django library that helps you create REST APIs easily.

With DRF you can:

* Create endpoints (routes)
* Convert models into JSON (using **serializers**)
* Add authentication (like **JWT**)
* Protect APIs so only logged-in users can access them

---

## 🔹 Summary Flow

1. Create a Django model (e.g., Product)
2. Use DRF to build an API to view/add/edit/delete products
3. Use JWT to log in users and protect routes

---

Do you want me to **show code step-by-step** for building this using Django and JWT?
