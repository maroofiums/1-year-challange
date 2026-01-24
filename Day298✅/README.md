# Day298

---

## Part 1: API Security 🔐 (Sab se pehle yeh samjho)

Socho API = tumhara ghar
Security = lock, gate, guard, CCTV

Agar security weak hui → koi bhi aa ke data chura lega 😬

---

### 1️⃣ Authentication (Tum kaun ho?)

**Purpose:** User ki identity verify karna

#### Common methods:

* **JWT (JSON Web Token)** ✅ (Most popular)
* OAuth2
* API Keys (simple but risky)

**JWT Flow (simple words):**

1. User login karta hai (email + password)
2. Server JWT token deta hai
3. Har request ke sath token jata hai
4. Server token verify karta hai → allow / deny

**FastAPI example (concept):**

```python
Authorization: Bearer <token>
```

✅ **Best Practice**

* Token short-lived rakho (15–30 min)
* Refresh token alag rakho

❌ **Avoid**

* Token URL mein pass karna
* Token frontend ke localStorage mein blindly store karna

---

### 2️⃣ Authorization (Tum kya kar sakte ho?)

**Authentication ≠ Authorization**
Yeh mistake log interviews mein kar dete hain ⚠️

* **AuthN:** Tum kaun ho?
* **AuthZ:** Tumhe kya allowed hai?

#### Example:

* Admin → delete user
* Normal user → sirf apna data

**Role-based access (RBAC):**

```text
role = admin | user | manager
```

✅ Best Practice:

* Roles / permissions clearly define karo
* Backend pe enforce karo (frontend pe trust mat karo)

---

### 3️⃣ Input Validation (Sabse underrated but powerful)

User input = sab se bada attack surface 😈

#### Attacks:

* SQL Injection
* XSS
* Invalid data crash

**FastAPI ka faida:**

* Pydantic automatically validate karta hai

```python
class UserCreate(BaseModel):
    email: EmailStr
    age: int = Field(gt=0, lt=120)
```

✅ Best Practice:

* Har input validate
* Type + range check

❌ Avoid:

* Direct request body ko DB mein daal dena

---

### 4️⃣ Rate Limiting (Overuse se protection)

Agar koi 1 second mein 10,000 requests bhej de? 💥

**Solution:** Rate limiting

Examples:

* 100 requests / minute / IP
* Login endpoint strict limit

Tools:

* Redis + rate limiter
* Nginx
* Cloudflare

✅ Best Practice:

* Auth endpoints pe strict limits
* Public endpoints pe soft limits

---

### 5️⃣ HTTPS & Secrets Management

❌ HTTP = open diary
✅ HTTPS = locked diary

Also:

* `.env` files
* Secrets kabhi GitHub pe push mat karna ❌

Use:

* Environment variables
* Vaults (later stage)

---

## Part 2: API Optimization ⚡ (Fast & Scalable banane ke liye)

Secure API slow ho sakti hai, optimized API **secure + fast** hoti hai.

---

### 1️⃣ Database Optimization 🗄️

**Common mistakes:**

* Har request pe heavy query
* No indexes

✅ Best Practices:

* Index lagao (foreign keys, search fields)
* `SELECT *` avoid karo
* Pagination use karo

```sql
LIMIT 20 OFFSET 0
```

---

### 2️⃣ Caching (Game changer 🚀)

Jo data baar baar change nahi hota → cache karo

Examples:

* User profile
* Dashboard stats

Tools:

* Redis
* In-memory cache

Flow:

```
Request → Cache check
        → If hit → return fast
        → If miss → DB → store → return
```

❌ Avoid:

* Cache without expiration
* Sensitive data cache karna

---

### 3️⃣ Async & Background Tasks

FastAPI ka strong point 💎

Use async when:

* I/O heavy task
* External API call
* File operations

Background tasks:

* Email sending
* Logging
* Notifications

✅ Best Practice:

* User ko wait mat karwao
* Heavy kaam background mein bhejo

---

### 4️⃣ Response Optimization

* Extra data mat bhejo
* Proper status codes use karo

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
```

❌ Avoid:

* Always returning 200
* Huge JSON responses

---

### 5️⃣ Monitoring & Logging 📊

Production mein blind mat raho 👀

Track:

* Errors
* Slow endpoints
* Failed logins

Tools:

* Logs
* Metrics
* Alerts

---