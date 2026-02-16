# Day 321


## **Step 1: Model Evaluation (Supervised Learning)**

Machine learning me sirf model banana kaafi nahi hai — aapko **evaluate** bhi karna hota hai ki model kitna acha kaam kar raha hai.

### **1.1 Regression Metrics** (predict continuous values)

* **Mean Absolute Error (MAE)** → Average absolute difference between predicted & actual.
  Formula:
  [
  MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
  ]
* **Mean Squared Error (MSE)** → Square differences, gives more penalty for big errors.
* **Root Mean Squared Error (RMSE)** → Square root of MSE, in same scale as target.
* **R² Score** → How well model explains variance in data (0–1).

**Python Example:**

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

print("MAE:", mean_absolute_error(y_true, y_pred))
print("MSE:", mean_squared_error(y_true, y_pred))
print("RMSE:", mean_squared_error(y_true, y_pred, squared=False))
print("R2:", r2_score(y_true, y_pred))
```

---

### **1.2 Classification Metrics** (predict categories)

* **Accuracy** → Correct predictions / total predictions
* **Precision** → Of predicted positives, how many are actually positive
* **Recall** → Of actual positives, how many predicted correctly
* **F1-Score** → Harmonic mean of precision & recall
* **Confusion Matrix** → Counts TP, FP, TN, FN

**Python Example:**

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 0, 0, 1, 1]

print("Accuracy:", accuracy_score(y_true, y_pred))
print("Precision:", precision_score(y_true, y_pred))
print("Recall:", recall_score(y_true, y_pred))
print("F1 Score:", f1_score(y_true, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
```

**Tip:** Classification me **imbalanced data** ke liye accuracy se mat judge karo, precision, recall aur F1 use karo.

---

## **Step 2: Ensemble Learning**

Ensemble learning ka matlab: **multiple models ko combine karke ek strong model banana**.
Agar ek model weak hai, ensembles usko strong bana dete hain.

### **2.1 Bagging (Bootstrap Aggregation)**

* Idea: multiple models train on random subsets of data
* Example: **Random Forest** → multiple decision trees, vote for majority
* Good for: reducing **variance** (overfitting)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### **2.2 Boosting**

* Idea: models sequentially train, focusing on errors of previous models
* Examples: **AdaBoost, Gradient Boosting, XGBoost, LightGBM**
* Good for: reducing **bias** (underfitting)

```python
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### **2.3 Stacking**

* Idea: multiple different models → outputs combined using **meta-model**
* Example: use Logistic Regression to combine Random Forest + XGBoost + SVM

**Tip:**

* Bagging → reduce variance
* Boosting → reduce bias
* Stacking → combine strengths

---
