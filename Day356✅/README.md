# Day 356

---

## **Step 1: Understand the Basics**

**Goal:** Learn what CI/CD is and why it matters.

* **Read/Watch:**

  * “What is CI/CD?” articles or videos (search “CI/CD explained for beginners”)
  * Learn the difference between **Continuous Integration, Continuous Delivery, and Continuous Deployment**.
* **Hands-on Exercise:**

  * Make a small Python project (even a “Hello World” FastAPI app).
  * Push it to GitHub.

---

## **Step 2: CI with GitHub Actions**

**Goal:** Automatically run tests whenever you push code.

* **Learn:**

  * How GitHub Actions works
  * Writing a simple workflow YAML file
  * Jobs, steps, triggers (`on: push`)
* **Hands-on Exercise:**

  * Add a `pytest` test for your Python project.
  * Set up GitHub Actions to automatically run tests when you push code.

---

## **Step 3: CD Basics**

**Goal:** Deploy your app automatically to a server.

* **Learn:**

  * Difference between staging and production
  * Deployment triggers (after CI passes)
* **Hands-on Exercise:**

  * Use a free service like **Render**, **Railway**, or **Heroku** to deploy your FastAPI app.
  * Connect deployment to GitHub Actions: whenever code passes tests, it gets deployed.

---

## **Step 4: Build a Full CI/CD Pipeline**

**Goal:** Combine CI + CD for a complete workflow.

* **Learn:**

  * Environment variables and secrets in GitHub Actions
  * Conditional deployments (staging vs production)
  * Notifications on build/deploy failures
* **Hands-on Exercise:**

  * Extend your FastAPI project:

    1. Run tests (CI)
    2. Build Docker image
    3. Deploy Docker image to Render/Railway (CD)

---

## **Step 5: Advanced CI/CD Topics**

* Rollbacks & versioning
* Blue/Green or Canary deployments
* Multi-environment pipelines
* Integrating code quality tools: linting, coverage, static analysis

---
