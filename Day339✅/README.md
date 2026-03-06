# Day339 - FastAPI Deployment on Replit

This is a simple FastAPI project deployed on **Replit**.

👉 **Live API Link:**  
https://fast-api-deploy-simple--maroof96965.replit.app

---

## 🚀 Endpoints

### Root
```

GET /

````
Returns:
```json
{
  "message": "FastAPI is running on Replit!"
}
````

---

### Hello

```
GET /hello/{name}
```

Example:
[https://fast-api-deploy-simple--maroof96965.replit.app/hello/Maroof](https://fast-api-deploy-simple--maroof96965.replit.app/hello/Maroof)

Returns:

```json
{
  "message": "Hello, Maroof!"
}
```

---

## 📂 Project Structure

```
fastapi-replit/
├── main.py
├── requirements.txt
└── .replit
```

---

## 🧠 How It Works

* **FastAPI** creates the API endpoints.
* **Uvicorn** runs the server on Replit.
* The app runs at the public Replit URL automatically after clicking **Run**.

---

## 📦 Dependencies

Listed in `requirements.txt`:

```
fastapi
uvicorn
```

---

## 📌 Notes

* This setup works on Replit Free tier (no card required).
* The server may sleep after being idle — wake it by visiting the link.
* You can add more routes by editing `main.py`.

---
