# Day 58

Welcome to Day 58 of the 365 Days of Code Challenge!
Wah Maroof bhai! Ab tum **API development** pe aa gaye ho — that’s a **pro-level move** 🔥

Chalo isay bhi **usi simple aur clear tareeqay se** seekhte hain jaise supervised learning samjhi thi — step by step. 👇

---

# 🧠 **What is an API?**

### 🔧 API = Application Programming Interface

> 📞 “Ek tarika jiske zariye do apps ya systems **baat karte hain**.”

---

## 🎯 Real Life Example:

Tumhara frontend (HTML, JS) Django backend se data maangta hai:

🧑‍💻 Frontend:

```http
GET /products
```

🧠 Backend:

```json
[
  {"id": 1, "name": "Ice Cream", "price": 300},
  {"id": 2, "name": "Cookies", "price": 150}
]
```

Yeh exchange jo ho raha hai — isi ko **REST API** kehte hain.

---

# 🔍 **REST API Basics** (Step 1)

| Method   | Kaam Kya Hai | Example                         |
| -------- | ------------ | ------------------------------- |
| `GET`    | Data lena    | `/products/` (sab products)     |
| `POST`   | Naya create  | `/products/` (naya product)     |
| `PUT`    | Update karna | `/products/1/` (product update) |
| `DELETE` | Delete karna | `/products/1/`                  |

---

# 🚀 **Django REST API Example (with Django REST Framework)**

### 🔨 Step-by-step banana seekhna hai toh ye karenge:

### ✅ Phase 1: REST API

1. Django + REST Framework install
2. Product model banana
3. API views (GET, POST, PUT, DELETE)
4. JSON Response check karna

---

### ✅ Phase 2: JWT Auth

1. User login/register API
2. JWT token generate
3. Token ke sath secure endpoints
4. Logout + Refresh token

---

# 🧑‍🍳 Quick Taste of Code (Example)

```python
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello, Maroof bhai!"})
```

---

# ✅ Ab Batao Bhai:

Tum chahte ho:

* [ ] Django REST API banaana from scratch?
* [ ] JWT Auth setup karna?
* [ ] Dono combined ek mini-project mein?
* [ ] Ya pehle concept ko deep explain karun?

**Tum bolo — main ready hoon samjhaane ko! 💪**
