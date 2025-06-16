# Day 76

Supervised Learning is a type of Machine Learning where the model is **trained on labeled data**—that means the input data already has the correct output (target).

---

## 🧠 Supervised Learning Overview

| Feature      | Description                                          |
| ------------ | ---------------------------------------------------- |
| **Input**    | Features (X)                                         |
| **Output**   | Labels/Targets (y)                                   |
| **Goal**     | Learn a mapping from inputs to outputs               |
| **Examples** | Spam detection, price prediction, sentiment analysis |

---

## 📊 Two Main Types:

### 1. **Regression**

Used when the **output is continuous** (real numbers).

#### ✅ Examples:

* Predicting house prices
* Estimating car mileage (km/l)
* Forecasting sales

#### 📈 Algorithms:

* **Linear Regression**
* **Ridge/Lasso Regression**
* **Polynomial Regression**
* **Decision Tree Regressor**
* **Random Forest Regressor**

#### 📏 Metrics:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

---

### 2. **Classification**

Used when the **output is categorical** (labels or classes).

#### ✅ Examples:

* Email Spam or Not Spam
* Classifying images of cats vs dogs
* Predicting diseases (Yes/No)

#### 📊 Algorithms:

* **Logistic Regression**
* **K-Nearest Neighbors (KNN)**
* **Support Vector Machine (SVM)**
* **Decision Tree / Random Forest**
* **Naive Bayes**
* **Neural Networks**

#### 📏 Metrics:

* Accuracy
* Precision, Recall, F1-Score
* Confusion Matrix
* ROC-AUC

---

## ⚙️ Workflow of Supervised Learning

```text
1. Collect and prepare labeled dataset (X, y)
2. Split into training and test sets
3. Choose an algorithm
4. Train the model on training set
5. Evaluate on test set
6. Improve with hyperparameter tuning or better features
```

---

## 🧪 Simple Example: Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]  # y = 2 * x

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, predictions))
```

---

## 🧪 Simple Example: Classification

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]  # Binary classes

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
```
