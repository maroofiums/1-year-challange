from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Dict, List, Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# --- Constants for JWT ---
SECRET_KEY = "your-secret-key"  # Change this to a strong secret!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class Resume(BaseModel):
    name: str
    age: int
    email: EmailStr
    skills: Optional[List[str]] = None
    experience: Optional[Dict[str, str]] = None
    linkedin: Optional[HttpUrl] = None
    github: Optional[HttpUrl] = None

class User(BaseModel):
    username: str
    email: EmailStr
    hashed_password: str

class UserInDB(User):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

# In-memory storage (for demo)
resumes_db = {}
users_db = {
    "maroof": {
        "username": "maroof",
        "email": "maroof@example.com",
        "hashed_password": pwd_context.hash("password123")
    }
}

# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    user = users_db.get(username)
    if user:
        return UserInDB(**user)
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

# Token endpoint
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Protected endpoints below (require JWT)

@app.post("/resumes/", status_code=201)
def create_resume(resume: Resume, current_user: User = Depends(get_current_user)):
    if resume.email in resumes_db:
        raise HTTPException(status_code=400, detail="Resume with this email already exists")
    resumes_db[resume.email] = resume
    return resume

@app.get("/resumes/{email}", response_model=Resume)
def read_resume(email: str, current_user: User = Depends(get_current_user)):
    if email not in resumes_db:
        raise HTTPException(status_code=404, detail="Resume not found")
    return resumes_db[email]

@app.get("/resumes/", response_model=List[Resume])
def readall_resume(current_user: User = Depends(get_current_user)):
    return list(resumes_db.values())

@app.put("/resumes/{email}", response_model=Resume)
def update_resume(email: str, resume: Resume, current_user: User = Depends(get_current_user)):
    if email not in resumes_db:
        raise HTTPException(status_code=404, detail="Resume not found")
    resumes_db[email] = resume
    return resume

@app.delete("/resumes/{email}", status_code=204)
def delete_resume(email: str, current_user: User = Depends(get_current_user)):
    if email not in resumes_db:
        raise HTTPException(status_code=404, detail="Resume not found")
    del resumes_db[email]
    return
