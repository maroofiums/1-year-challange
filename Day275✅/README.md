
## Day275

> **JWT-based authentication** samajhna + **protected API** banana
> 👉 End of day tum confidently explain kar sako:
> **“Login kaise hota hai, token kahan banta hai, aur protected route kaise kaam karta hai”**

---

## 🧠 Step 1: Auth hoti kya cheez hai? (Simple words)

Auth = **Tum kaun ho?**
Authorization = **Tum kya access kar sakte ho?**

Relatable example:

* Gate pe guard poochta hai → *ID card dikhao* = Authentication
* Phir bolta hai → *lab allowed hai / nahi* = Authorization

---

## 🧩 Step 2: OAuth2 ka role (confusion yahin hoti hai)

OAuth2 **login system nahi**,
OAuth2 = **rulebook** 📘
FastAPI kehta hai:

> “Tum OAuth2 follow karo, implementation main handle karwa dunga”

Hum use karenge:

```
OAuth2 Password Flow + JWT
```

⚠️ Google/GitHub login **NOT today**

---

## 🔐 Step 3: JWT samjho (yeh core hai)

JWT = `Header.Payload.Signature`

Socho:

* Header → token type
* Payload → user info (id, email)
* Signature → secret key se lock 🔒

🔥 Important:

* JWT **stateless** hota hai
* Server session store nahi karta

---

## 🏗️ Step 4: Minimal Working FastAPI Auth (FULL FLOW)

### 📁 Project Structure

```
app/
 ├── main.py
 ├── auth.py
 ├── models.py
```

---

### 🔹 main.py

```python
from fastapi import FastAPI
from auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)
```

---

### 🔹 auth.py (Heart of auth)

```python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta

router = APIRouter()
SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_user = {
    "username": "admin",
    "password": "1234"
}
```

---

### 🔹 Token create karna

```python
def create_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=30)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
```

---

### 🔹 Login endpoint

```python
@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username != fake_user["username"] or form.password != fake_user["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}
```

---

### 🔹 Protected Route

```python
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/protected")
def protected(user: str = Depends(get_current_user)):
    return {"message": f"Welcome {user}"}
```

---

## 🧪 Step 5: Testing (Very Important)

1. Swagger open karo `/docs`
2. `/login` → username: admin, password: 1234
3. Token copy
4. **Authorize button** → paste token
5. `/protected` call karo


---