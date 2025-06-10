# Day 38

Welcome to Day 38 of the 365 Days of Code Challenge!

Chalo simple aur asaan Urdu mein samajhte hain: **JWT** aur **REST API** kya hotay hain, aur inka **use** kyun aur kaise hota hai.

---

## 🔹 1. **REST API Kya Hai?**

**REST API** ka matlab hai:
**"Representational State Transfer - Application Programming Interface"**

### 🔧 Samjho:

Aapka **frontend** (jaise ek website ya mobile app) agar backend (server/database) se data lena chahta hai, to woh **API** ka use karta hai.

### ✅ REST API mein:

* **GET** – Data lo (e.g., products list)
* **POST** – Naya data bhejo (e.g., naya product add karo)
* **PUT** – Purana data update karo
* **DELETE** – Data delete karo

**Example:**

* `GET /api/products/` → sab products dekhna
* `POST /api/products/` → naya product add karna

---

## 🔹 2. **JWT Kya Hai?**

**JWT** ka full form hai: **JSON Web Token**

### 🔐 Samjho:

JWT ek **token (chhota encrypted message)** hota hai jo user ke **login** hone ke baad diya jata hai. Ye token proof hota hai ke user ne login kiya hai.

Isse:

* Har request ke saath token bhejna padta hai
* Server check karta hai token valid hai ya nahi
* Agar valid ho to access milta hai

### ✅ JWT 3 parts mein hota hai:

1. **Header** – Algorithm ki info
2. **Payload** – User ki info (jaise user ID)
3. **Signature** – Token ki safety ke liye seal

---

## 🔹 3. Use Kahan Hota Hai?

JWT ka use **authentication** ke liye hota hai.
Yani kisi bhi **protected API** ko access karne ke liye aapko JWT chahiye hota hai.

### 🔁 Flow:

1. User login karta hai (username + password)
2. Server user ko JWT token deta hai
3. Aap har API request ke saath token bhejte ho
4. Server token check karke data deta hai

---

## 🔹 4. JWT + REST Together?

Aap jab Django me REST API banate ho, to agar wo **login ke baad access hone wali cheez hai**, to aap **JWT authentication** lagate ho.

Yani:

| Action            | Kya Hota Hai                  |
| ----------------- | ----------------------------- |
| Register          | User account banata hai       |
| Login             | JWT Token milta hai           |
| Token ke sath GET | Products ki list milti hai    |
| Bina token ke GET | "Unauthorized" error aata hai |

---

## 🔸 Ek Simple Example:

1. User → `/api/token/` → **Login** karta hai
2. Server → JWT Token deta hai
3. User → `/api/products/` par **token ke sath request** bhejta hai
4. Server → User ko **authorized data** deta hai

---

Agar chaho to main ek chhota **Django REST + JWT** ka working example bana kar de sakta hoon.

Kya aap chahte ho main aapko ek ready project link ya zip banakar du?
