

# 🧠 Day 263 — Model Optimization & Hyperparameter Tuning

---

## 🎯 Goal

Aaj ka aim hai:

* Multiple ML models ko compare karna
* GridSearchCV se best hyperparameters nikalna
* Final tuned model evaluate karna

---

## ⚙️ Step 1 — Imports

```python
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
```

---

## 🧩 Step 2 — Preprocessing + Split

```python
le = LabelEncoder()
y = le.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)
```

📘 *Scaling important hai for SVM, KNN, Logistic Regression.*

---

## 🤖 Step 3 — Models Dictionary

```python
models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "Naive Bayes": GaussianNB(),
    "KNN": KNeighborsClassifier()
}
```

---

## 🧮 Step 4 — Parameter Grids

```python
param_grids = {
    "Logistic Regression": {"C": [0.1, 1, 10], "solver": ["liblinear", "lbfgs"]},
    "SVM": {"C": [0.1, 1, 10], "kernel": ["linear", "rbf"], "gamma": ["scale", "auto"]},
    "Decision Tree": {"criterion": ["gini", "entropy"], "max_depth": [3, 5, 7, None]},
    "Naive Bayes": {"var_smoothing": [1e-9, 1e-8, 1e-7]},
    "KNN": {"n_neighbors": [3, 5, 7, 9], "weights": ["uniform", "distance"]}
}
```

---

## 🔍 Step 5 — GridSearchCV Loop

```python
best_models = {}

for name, model in models.items():
    print(f"\n🔧 Tuning {name}...")
    grid = GridSearchCV(model, param_grids[name], cv=5, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train)

    print(f"✅ Best Params: {grid.best_params_}")
    print(f"⭐ CV Score: {grid.best_score_:.4f}")

    best_models[name] = grid.best_estimator_
```

🧠 *GridSearchCV sab combinations try karta hai aur best parameters return karta hai.*

---

## 🧪 Step 6 — Evaluate on Test Data

```python
for name, model in best_models.items():
    print(f"\n🚀 Evaluating {name}...")
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
```

---

## 📊 Step 7 — Model Ranking

```python
results = [(name, accuracy_score(y_test, model.predict(X_test)))
           for name, model in best_models.items()]

results.sort(key=lambda x: x[1], reverse=True)

print("\n🏆 Final Model Ranking:")
for name, acc in results:
    print(f"{name}: {acc:.4f}")
```

---

## 🧠 Learnings & Tips

| Concept          | Key Idea                          |
| ---------------- | --------------------------------- |
| GridSearchCV     | Tries all parameter combinations  |
| Cross-Validation | Ensures stable performance        |
| Scaling          | Crucial for distance-based models |
| Overfitting      | Prevent using CV & tuning         |
| Model Comparison | Always compare > 3 models         |
| Save Model       | Use `joblib.dump()` for reuse     |

---

## 💡 Summary

> “Model optimization is like fine-tuning a guitar —
> same strings (algorithm), better harmony (performance).” 🎸

---

