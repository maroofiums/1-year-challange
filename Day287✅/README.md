# Day287 => 🎬 Content-Based Movie Recommendation System

## 📌 Project Overview

This project implements a **Content-Based Movie Recommendation System** using **Natural Language Processing (NLP)** and **Machine Learning** techniques.
It recommends movies based on **textual similarity** between movie descriptions, genres, and taglines.

The system uses **TF-IDF Vectorization** and **Cosine Similarity** to find movies that are most similar to a given movie.

---

## 🧠 How It Works (High-Level)

User ek movie ka naam deta hai →
System us movie ke **text features** ko baqi movies se compare karta hai →
Most similar movies recommend ho jati hain.

👉 No user history required (pure content-based).

---

## 📂 Dataset

* **Source:** TMDB Movies Metadata
* **Size:** ~45,000 movies
* **Key Features Used:**

  * `title`
  * `overview`
  * `genres`
  * `tagline`
  * `vote_average`
  * `popularity`

---

## 🔧 Data Preprocessing Steps

Step-by-step workflow:

### 1. Data Cleaning

* Removed duplicate rows
* Dropped rows with missing `title`
* Filled missing `overview` and `tagline` with empty strings

### 2. Genre Parsing

* `genres` column was stored as stringified dictionaries
* Converted into readable text using `ast.literal_eval`

Example:

```
[{'id': 16, 'name': 'Animation'}]
→ Animation
```

### 3. Feature Engineering (Tags Creation)

Combined important text fields:

```
tags = overview + genres + tagline
```

This creates a **single semantic representation** per movie.

---

## 🧹 Text Preprocessing (NLP)

Applied standard NLP pipeline using **NLTK**:

* Lowercasing
* Removing punctuation & special characters
* Stopword removal
* Lemmatization

Why?

> Taake words ka **actual meaning retain** rahe aur noise kam ho.

---

## 📐 Vectorization

Used **TF-IDF Vectorizer**:

```python
TfidfVectorizer(
  max_features=50000,
  ngram_range=(1,2),
  stop_words='english'
)
```

### Why TF-IDF?

* Common words ka weight kam
* Important words ko zyada importance
* Scales well for large text data

---

## 📊 Similarity Measure

Used **Cosine Similarity** to measure closeness between movies:

* Value range: `0 → 1`
* Higher value = more similar content

---

## 🎯 Recommendation Logic

```python
def recommend(title, n=10):
```

### Workflow:

1. Movie title ka index find karo
2. Us movie ka vector baqi sab se compare
3. Similarity score sort karo
4. Top `n` most similar movies return karo

---

## 🧪 Example Output

```python
recommend("Avatar", 5)
```

**Output:**

* Avatar 2
* The Inhabited Island
* Thor: Ragnarok
* Moontrap: Target Earth
* The Three Musketeers

---

## 💾 Model Persistence

For reusability & deployment, saved objects using `pickle`:

* `tfidf_matrix.pkl`
* `tfidf.pkl`
* `indices.pkl`
* `df.pkl`

This allows **fast inference** without retraining.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas & NumPy**
* **NLTK**
* **Scikit-learn**
* **Pickle**

---

## 🚀 Possible Improvements

Honest mentor advice 👇

✅ What’s Good:

* Clean pipeline
* Industry-standard NLP steps
* Scalable approach
* Deployment-ready artifacts

⚠️ What Can Be Improved:

* Add **stemming vs lemmatization comparison**
* Weight genres higher than overview
* Combine with **collaborative filtering**
* Use **Sentence Transformers / BERT**
* Add FastAPI / Streamlit frontend

---

## 🧠 Learning Outcome

By building this project, you learned:

* Real-world NLP preprocessing
* Feature engineering for recommender systems
* TF-IDF & cosine similarity
* Model persistence for production use
