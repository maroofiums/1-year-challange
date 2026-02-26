# Day 331

# 1️⃣ What is System Design?

It’s the process of designing:

* Architecture
* Components
* Data flow
* Scalability strategy
* Reliability strategy

Example:
Instead of writing just a FastAPI app →
You design:

* How it handles 1M users
* How data is stored
* How failures are handled
* How performance is optimized

---

# 2️⃣ Basic Building Blocks

## 🔹 1. Client

User side:

* Web app
* Mobile app
* React frontend
* Postman

Sends HTTP request to backend.

---

## 🔹 2. Server

Backend server:

* FastAPI
* Django
* Express.js

Handles:

* Authentication
* Business logic
* DB operations

---

## 🔹 3. Database

Stores data.

Types:

### SQL (Relational)

* PostgreSQL
* MySQL

Best for:

* Structured data
* Strong consistency

### NoSQL

* MongoDB
* Redis

Best for:

* Flexible schema
* High speed
* Caching

---

## 🔹 4. Cache

Used to reduce database load.

Example:

* Redis

Flow:
User → Server → Redis → (If miss) → Database

Result:
Faster response
Less DB load

---

## 🔹 5. Load Balancer

Distributes traffic across multiple servers.

Example:

* NGINX
* HAProxy

Without it:
One server crashes = system down

With it:
Traffic split across many servers.

---

# 3️⃣ Scaling Basics

## Vertical Scaling

Upgrade one server:

* More RAM
* Better CPU

Problem: Limited.

---

## Horizontal Scaling

Add more servers.

Server1
Server2
Server3

Requires:

* Load balancer
* Stateless backend

This is how big systems scale.

---

# 4️⃣ CAP Theorem (Very Important)

You can only choose 2 of 3:

* C = Consistency
* A = Availability
* P = Partition tolerance

Example:

* Banking system → Consistency priority
* Social media → Availability priority

---

# 5️⃣ Monolith vs Microservices

## Monolith

Single codebase.

Easy:

* Build
* Deploy

Hard:

* Scale independently

---

## Microservices

Multiple small services:

* Auth Service
* Payment Service
* ML Service

Communicate via:

* REST
* Message queue

Example message broker:

* RabbitMQ
* Apache Kafka

---

# 6️⃣ Basic System Design Flow (Interview Style)

If interviewer says:

"Design Instagram"

You start with:

1. Clarify requirements
2. Estimate scale (users, requests/sec)
3. Design high-level architecture
4. Choose database
5. Add caching
6. Add load balancing
7. Add scaling strategy
8. Handle failures

---

# 7️⃣ Real Backend Example (Your Level)

Let’s say:

You build Smart URL Shortener API

Basic Design:

User → Load Balancer → FastAPI Server → Redis (cache) → PostgreSQL

Later:

* Add rate limiting
* Add analytics service
* Add background worker

Now it becomes production-ready.

---

# 8️⃣ Core Concepts You Must Master

* HTTP & REST
* Database indexing
* Caching strategies
* Horizontal scaling
* Message queues
* Consistency models
* ACID vs BASE
* Basic networking (DNS, TCP/IP)

---
