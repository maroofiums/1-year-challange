# Day 334 - Mock Technical Interviews 

Focus: Backend + ML + System Design

---

# 1️⃣ FastAPI Core Concepts

## 🔹 Request Lifecycle

1. Client sends request  
2. Uvicorn (ASGI server) receives it  
3. Route matching happens  
4. Dependency Injection runs  
5. Pydantic validates request  
6. Endpoint function executes  
7. Response serialized to JSON  
8. Returned to client  

---

## 🔹 ASGI

ASGI = Asynchronous Server Gateway Interface

- Successor of WSGI  
- Supports async and concurrency  
- Handles multiple requests efficiently  
- Ideal for IO-bound operations  

---

## 🔹 FastAPI vs Flask

| Feature | Flask | FastAPI |
|----------|--------|----------|
| Protocol | WSGI | ASGI |
| Async | Limited | Native |
| Validation | Manual | Pydantic |
| Performance | Moderate | High |

---

# 2️⃣ JWT Authentication

## 🔹 JWT Structure

Header.Payload.Signature

### Flow:
1. User logs in  
2. Server verifies credentials  
3. Server generates token  
4. Client stores token  
5. Client sends token in Authorization header  
6. Server verifies signature  

---

## 🔹 Why JWT is Stateless

- No session stored on server  
- All user data inside token  
- Server only verifies signature  
- Easy to scale across services  

---

## 🔹 Secure Implementation

- Short-lived access token (15–30 min)  
- Long-lived refresh token  
- Store refresh token in HTTP-only cookie  
- Hash refresh tokens in database  
- Rotate refresh tokens  
- Blacklist on logout  

---

# 3️⃣ API Optimization Strategy

## Step 1: Measure First
- Logs  
- Profiling  
- APM tools  

## Step 2: Database Optimization
- Add indexes  
- Avoid N+1 queries  
- Use select_related / prefetch_related  
- Optimize joins  

## Step 3: Async Issues
- Avoid blocking calls inside async routes  
- Use async DB drivers  
- Use httpx instead of requests  

## Step 4: Scaling
- Increase workers  
- Use Gunicorn with Uvicorn workers  
- Add load balancer  

## Step 5: Caching
- Use Redis  
- Cache heavy queries  
- Add pagination  

---

# 4️⃣ Django Core Concepts

## MVT Architecture
- Model → Database logic  
- View → Business logic  
- Template → Presentation  

## Middleware
- Runs before/after view  
- Used for logging, auth, security  

## Signals
- post_save  
- pre_delete  
- Used for decoupled event handling  

---

# 5️⃣ Database Fundamentals

## Index
- Speeds up SELECT  
- Slows INSERT slightly  
- Use on frequently filtered columns  

## ACID Properties
- Atomicity  
- Consistency  
- Isolation  
- Durability  

## Normalization
- Reduce redundancy  
- Improve integrity  

---

# 6️⃣ Machine Learning Core

## Bias vs Variance
- High Bias → Underfitting  
- High Variance → Overfitting  

## Regularization
- L1 → Feature selection  
- L2 → Weight shrinking  

## Evaluation Metrics
Classification:
- Accuracy  
- Precision  
- Recall  
- F1  

Regression:
- MAE  
- MSE  
- RMSE  

---

# 7️⃣ ML System Design (Deployment)

If asked to deploy ML model:

1. Data ingestion  
2. Preprocessing pipeline  
3. Model training  
4. Model versioning  
5. API deployment (FastAPI)  
6. Monitoring  
7. Logging predictions  
8. Retraining strategy  

Mention:
- Model drift  
- Data validation  
- Monitoring metrics  

---

# 8️⃣ DSA Must-Know Patterns

- Two Pointers  
- Sliding Window  
- HashMap Frequency  
- Stack / Queue  
- Binary Search  
- BFS / DFS  
- Recursion  

---