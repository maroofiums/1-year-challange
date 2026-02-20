# Day 325


## 1. The Connection Flow

In a FastAPI app, the database interaction usually follows this flow:

1. **The Model:** A class defining how the data looks in the database.
2. **The Schema (Pydantic):** A class defining how the data looks in the API (JSON).
3. **The Session:** A temporary connection to the database.

---

## 2. Setting Up SQLAlchemy

SQLAlchemy is the industry standard. To use it, you generally create a `database.py` file to handle the engine and session.

```python
from sqlalchemy import create_url, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" # Using SQLite for simplicity

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

```

---

## 3. Creating Database Models

These models define your tables. Notice they look similar to Pydantic models, but they inherit from `Base`.

```python
from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

```

---

## 4. Connecting it to FastAPI (using the Step 3 Dependency)

This is where the **Dependency Injection** from Step 3 pays off. We create a dependency that provides a database session to our endpoints.

```python
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

# Create the tables (usually done with migrations like Alembic in real projects)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, hashed_password="fakehashedpassword")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

```

---

## 5. Why do we need both Pydantic and SQLAlchemy models?

It can feel redundant at first, but it's a "Best Practice" called **Separation of Concerns**:

| Feature | SQLAlchemy Model | Pydantic Model (Schema) |
| --- | --- | --- |
| **Purpose** | Defines the database table structure. | Defines what the user sends/receives (JSON). |
| **Logic** | Includes things like `hashed_password`. | Filters out sensitive data (e.g., returns `user_id` but not `password`). |
| **Validation** | Database constraints (Unique, Not Null). | Data types, email formats, string lengths. |

---
