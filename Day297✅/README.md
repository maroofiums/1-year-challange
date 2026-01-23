# Day 297

## 🔹 BASIC DJANGO INTERVIEW QUESTIONS

### 1️⃣ Django kya hai?

**Answer:**
Django ek **high-level Python web framework** hai jo **fast, secure aur scalable** web applications banane ke liye use hota hai.

**Key features:**

* MVT architecture
* Built-in Admin Panel
* ORM (database easy ho jata hai)
* Security (CSRF, SQL injection protection)

**Honest advice:**
Interview mein sirf definition mat bolo — **1 real use-case** zaroor add karo.

🧠 **Tip:**

> “Django helps build production-ready apps faster with less boilerplate.”

---

### 2️⃣ Django vs Flask?

| Django              | Flask                     |
| ------------------- | ------------------------- |
| Full-featured       | Lightweight               |
| Batteries included  | You choose libraries      |
| Best for large apps | Best for small/micro apps |

**Best practice:**
Agar project **complex & scalable** ho → Django
Agar **simple API / microservice** → Flask

---

### 3️⃣ Django Architecture kya hai?

**MVT (Model View Template)**

* **Model** → Database logic
* **View** → Business logic
* **Template** → HTML / frontend

👉 Django ka **View**, MVC ke **Controller** jaisa hota hai.

**Common mistake:**
Log View ko sirf HTML samajh lete hain ❌

---

## 🔹 DJANGO MODELS & ORM

### 4️⃣ Django ORM kya hai?

ORM = **Object Relational Mapping**

```python
class User(models.Model):
    name = models.CharField(max_length=100)
```

Iska matlab:

* SQL likhne ki zarurat nahi
* Python objects se DB handle

**Why interviewers like ORM?**

* Cleaner code
* DB independent (PostgreSQL, MySQL, SQLite)

⚠️ **Avoid:**
Raw SQL jab tak bohot zaroori na ho.

---

### 5️⃣ Migrations kya hoti hain?

Migrations = **database schema ka version control**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Workflow samjho:**

1. Model change
2. Makemigrations
3. Migrate

🧠 **Tip:**
Production mein migration bina check kiye run mat karna.

---

## 🔹 DJANGO VIEWS

### 6️⃣ Function-Based View vs Class-Based View?

**FBV**

* Simple
* Easy to understand

**CBV**

* Reusable
* Clean & scalable

**Interview-ready line:**

> “FBVs are simple, CBVs are powerful for large applications.”

---

### 7️⃣ Django request-response cycle?

**Flow:**

1. URL hit hota hai
2. URL dispatcher
3. View call hoti hai
4. Model se data
5. Template render
6. Response return

🧠 Interviewers ko **flow clarity** bohot pasand hoti hai.

---

## 🔹 DJANGO AUTH & SECURITY

### 8️⃣ Authentication vs Authorization?

* **Authentication** → Who are you?
* **Authorization** → What can you access?

Django provides:

* Login
* Logout
* Permissions
* Groups

**Best practice:**
Custom auth likhne se pehle Django ka built-in system use karo.

---

### 9️⃣ CSRF kya hai?

CSRF = **Cross Site Request Forgery**

Django protect karta hai using:

```html
{% csrf_token %}
```

⚠️ **Interview trap:**
Agar tum CSRF disable karte ho without reason → ❌

---

## 🔹 DJANGO REST FRAMEWORK (VERY IMPORTANT)

### 🔟 Django REST Framework kya hai?

DRF = **API banane ka powerful toolkit**

Features:

* Serializers
* ViewSets
* Authentication
* Pagination

**Real-world use:**
Mobile apps, React / Vue frontend ke liye APIs

---

### 1️⃣1️⃣ Serializer kya hota hai?

Serializer =
**Python object ⇄ JSON**

```python
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
```

**Best practice:**
Sensitive fields expose mat karo (passwords).

---

### 1️⃣2️⃣ ViewSet vs APIView?

* **APIView** → Full control
* **ViewSet** → Less code, clean

🧠 Interview tip:

> “I prefer ViewSets for CRUD APIs and APIView for custom logic.”

---

## 🔹 ADVANCED QUESTIONS

### 1️⃣3️⃣ Middleware kya hota hai?

Middleware = request aur response ke beech ka layer

Use cases:

* Logging
* Authentication
* Request modification

---

### 1️⃣4️⃣ Django scalability kaise handle karta hai?

* Caching (Redis)
* Database indexing
* Load balancers
* Async views (Django 3.1+)

**Honest advice:**
Django slow nahi hota — **bad design slow hota hai**.

---

### 1️⃣5️⃣ Celery kya hai?

Celery = **background tasks**

Use cases:

* Email sending
* Notifications
* Long-running tasks

👉 Django + Celery + Redis = 🔥 combo

---

## 🔹 QUICK INTERVIEW RAPID-FIRE

* `select_related` vs `prefetch_related`
* `settings.py` ka role
* `manage.py` kya karta hai?
* `signals` kya hoti hain?
* `JWT vs Session auth`

---

## ✅ FINAL FRIENDLY SUMMARY

🔑 **Yaad rakhne wali baatein:**

* Django = speed + security
* ORM & DRF bohot important
* Concepts samajho, ratta nahi
* Real examples do
* Trade-offs explain karo
