

# Day 280 - 🌸 Iris Flower Predictor — ML Model + FastAPI + React

This project is a simple **Machine Learning + Web App** that predicts the type of Iris flower based on its sepal and petal measurements.  
I built it to learn how to **serve an ML model using FastAPI** and connect it to a **React (Vite) frontend**.

---

## 🚀 Tech Stack

| Layer | Technology |
|-------|-------------|
| 🧠 Machine Learning | scikit-learn (Logistic Regression Model) |
| ⚙️ Backend API | FastAPI + Pydantic + Uvicorn |
| 🎨 Frontend | React (Vite) + Axios + Tailwind CSS |
| 📦 Model Handling | joblib + numpy |

---

## 🧩 Project Structure

```

iris-project/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   └── model/
│   │       └── model.pkl
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/IrisForm.jsx
│   │   └── main.jsx
│   └── package.json

````

---

## ⚙️ Backend Setup (FastAPI)

1. Go to backend folder:
   ```bash
   cd backend
   pip install fastapi uvicorn joblib scikit-learn numpy

2. Run the server:

   ```bash
   uvicorn app.main:app --reload
   ```
3. Check API:

   * Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   * Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 💻 Frontend Setup (React + Vite)

1. Go to frontend folder:

   ```bash
   cd frontend
   npm install
   npm run dev
   ```
2. Open in browser: [http://localhost:5173/](http://localhost:5173/)

---

## 🔄 How It Works

1. User inputs **sepal & petal length/width**
2. React sends data → FastAPI endpoint `/predict`
3. FastAPI loads ML model (`model.pkl`) and returns the result
4. Frontend displays prediction (e.g., `"Setosa"` or `"Not Setosa"`)

---

## 📚 What I Learned

✅ How to build & serve a Machine Learning model
✅ How to use **FastAPI** for creating REST APIs
✅ Input validation using **Pydantic BaseModel**
✅ How to connect **React frontend with FastAPI backend** using **Axios**
✅ Handling **CORS** in FastAPI
✅ Structuring real-world projects properly
✅ Using **Vite** for fast React setup
✅ Creating clean UI using **Tailwind CSS**

---

## 💡 Next Steps (Future Upgrades)

* [ ] Add multiple species prediction (Setosa, Versicolor, Virginica)
* [ ] Add loading spinner and better error handling
* [ ] Deploy backend on Render or Railway
* [ ] Deploy frontend on Netlify or Vercel
* [ ] Add charts or confidence scores

---

## 🧠 Author

**Maroof** — Python Developer (ML + Backend + Arduino)
GitHub: [maroof2424](https://github.com/maroof2424)

---

## 🌟 Quick Demo Flow

```
User Inputs → FastAPI API → ML Model → Prediction → Display Result
```

---

> 📝 **Tip:**
> Har project ke end pe aisa README likhna tumhe “job-ready developer” banata hai — because recruiters aur hackathon judges sabse pehle README hi dekhte hain 🚀
