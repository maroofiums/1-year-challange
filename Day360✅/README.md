# Day 360

---

# FastAPI + SQLite CRUD Project

## What I Learned (Mapped Understanding)

---

## 1. Database Setup (DB Part)

### Code Location:

```python
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(...)
Base = declarative_base()
```

### Concept:

* Yahan database create aur connect hota hai
* SQLite file (`test.db`) auto generate hoti hai
* SQLAlchemy engine Python ko DB se connect karta hai
* Session database transactions handle karta hai

---

## 2. Database Model (Table Structure)

### Code Location:

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
```

### Concept:

* Ye database table define karta hai
* Python class = Database table
* Har attribute = column

---

## 3. CRUD Logic (Core Database Operations)

### Code Location:

### CREATE

```python
db_user = User(name=user.name, email=user.email)
db.add(db_user)
db.commit()
db.refresh(db_user)
```

### READ

```python
db.query(User).all()
db.query(User).filter(User.id == user_id).first()
```

### UPDATE

```python
user.name = updated.name
user.email = updated.email
db.commit()
```

### DELETE

```python
db.delete(user)
db.commit()
```

### Concept:

* CRUD = database operations
* SQL likhne ki zaroorat nahi (ORM use ho raha hai)
* Python objects se database control hota hai

---

## 4. FastAPI Layer (API Endpoints)

### Code Location:

```python
@app.post("/users/")
@app.get("/users/")
@app.get("/users/{user_id}")
@app.put("/users/{user_id}")
@app.delete("/users/{user_id}")
```

### Concept:

* Ye user se request receive karta hai
* CRUD functions ko call karta hai
* Response return karta hai

---

## 5. DB Connection per Request (Dependency)

### Code Location:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Concept:

* Har request ke liye naya DB session
* Automatically close ho jata hai
* Safe database handling

---

## Final Flow (Very Important)

```
Client Request
      ↓
FastAPI Endpoint
      ↓
CRUD Logic (db operations)
      ↓
SQLAlchemy ORM
      ↓
SQLite Database
      ↓
Response back to client
```

---

## Final Understanding

Main samjha:

* DB setup kahan hota hai
* Tables kaise bante hain
* CRUD kaam kaise karta hai
* API aur DB ka connection kaise hota hai
* FastAPI request → database flow

---

