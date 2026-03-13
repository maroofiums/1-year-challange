# Day345 

---

# Step 1 — Install FastAPI

If not installed:

```bash
pip install fastapi uvicorn
```

Run server:

```bash
uvicorn main:app --reload
```

---

# Step 2 — Basic FastAPI App

Create **main.py**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}
```

Run:

```
http://127.0.0.1:8000/docs
```

---

# Step 3 — Import Security Tools

We need **OAuth2PasswordBearer**.

```python
from fastapi.security import OAuth2PasswordBearer
```

Add this:

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

Full code:

```python
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

Meaning:

```
OAuth2PasswordBearer
        │
Extracts token from request header
        │
Authorization: Bearer <token>
```

---

# Step 4 — Create Login Endpoint

User sends username + password.

```python
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    username = form_data.username
    password = form_data.password

    if username == "admin" and password == "123":
        return {
            "access_token": "mysecrettoken",
            "token_type": "bearer"
        }

    return {"error": "invalid credentials"}
```

Now Swagger will show **login form automatically**.

---

# Step 5 — Create Protected Route

Now we require the token.

```python
@app.get("/profile")
async def profile(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Protected route accessed",
        "token": token
    }
```

Flow:

```
Request → oauth2_scheme
        → extract Bearer token
        → pass token to route
```

---

# Step 6 — Test in Swagger

Open:

```
http://127.0.0.1:8000/docs
```

### 1 Login

```
POST /token
username = admin
password = 123
```

Response:

```
{
  "access_token": "mysecrettoken",
  "token_type": "bearer"
}
```

---

### 2 Click "Authorize"

Paste token:

```
mysecrettoken
```

Swagger automatically sends:

```
Authorization: Bearer mysecrettoken
```

---

### 3 Call Protected Route

```
GET /profile
```

Response:

```
{
 "message": "Protected route accessed",
 "token": "mysecrettoken"
}
```

---

# Step 7 — Full Working Code

```python
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    if form_data.username == "admin" and form_data.password == "123":
        return {
            "access_token": "mysecrettoken",
            "token_type": "bearer"
        }

    return {"error": "invalid credentials"}


@app.get("/profile")
async def profile(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Protected route accessed",
        "token": token
    }
```

---

# What Actually Happened (Important)

```
Client → POST /token
       → get token

Client → GET /profile
       Authorization: Bearer token

OAuth2PasswordBearer
       ↓
Extract token
       ↓
Pass token to route
```

---