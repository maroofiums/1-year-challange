# Day 36


Supervised learning is a type of machine learning where the model is trained on a **labeled dataset**, meaning each input data point is associated with the correct output. The goal is to learn a mapping from inputs to outputs so the model can predict outputs for new, unseen inputs.

There are two main types of supervised learning:

---

### ✅ 1. **Regression**

* **Definition**: Predicts a **continuous** numerical value.
* **Examples**:

  * Predicting house prices based on features (size, location).
  * Predicting temperature, salary, or stock prices.

#### 📌 Common Regression Algorithms:

* **Linear Regression**
* **Ridge/Lasso Regression**
* **Polynomial Regression**
* **Decision Tree Regressor**
* **Random Forest Regressor**
* **Support Vector Regressor (SVR)**
* **K-Nearest Neighbors (KNN) Regressor**

---
# Basic Linear Regression
Great! Let’s use a **built-in dataset** from `scikit-learn` for **Linear Regression**. One of the most common ones is the **California Housing dataset**, which is perfect for regression tasks.

---

## ✅ Linear Regression using California Housing Dataset

### 🔹 Step-by-Step Code

```python
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load California Housing dataset
housing = fetch_california_housing()

# Convert to DataFrame for easy understanding
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['Target'] = housing.target  # Median house value

# Display the first few rows
print(df.head())

# Select one feature (e.g., MedInc = median income)
X = df[['MedInc']]   # Feature
y = df['Target']     # Target: Median house value

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))
print("Slope (m):", model.coef_[0])
print("Intercept (b):", model.intercept_)

# Visualization
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Prediction')
plt.xlabel('Median Income')
plt.ylabel('Median House Value ($100,000s)')
plt.title('Linear Regression: Median Income vs House Value')
plt.legend()
plt.show()
```

---

## 📌 Dataset Info

* **Feature used**: `MedInc` – Median income in a neighborhood.
* **Target**: `Target` – Median house value in \$100,000s.
* **Type**: Real-world regression dataset.

---


### ✅ 2. **Classification**

* **Definition**: Predicts a **category or class label** (discrete value).
* **Examples**:

  * Email spam detection (Spam or Not Spam).
  * Tumor classification (Benign or Malignant).
  * Handwriting recognition (A, B, C...).

#### 📌 Common Classification Algorithms:

* **Logistic Regression**
* **K-Nearest Neighbors (KNN)**
* **Support Vector Machine (SVM)**
* **Decision Trees**
* **Random Forest Classifier**
* **Naive Bayes**
* **Neural Networks**

---

### 🧠 Key Concepts in Supervised Learning:

* **Features (X)**: Input variables (e.g., age, height, temperature).
* **Labels (y)**: Target/output values.
* **Training Set**: Used to train the model.
* **Test Set**: Used to evaluate model performance.
* **Evaluation Metrics**:

  * For Regression: MSE, RMSE, MAE, R² score.
  * For Classification: Accuracy, Precision, Recall, F1 Score, ROC-AUC.

---

### 📊 Visual Summary:

| Task Type      | Output Type       | Example Use Case        | Algorithm Example        |
| -------------- | ----------------- | ----------------------- | ------------------------ |
| Regression     | Continuous value  | Predicting house prices | Linear Regression        |
| Classification | Categorical label | Spam vs Non-spam email  | Logistic Regression, SVM |

---

Would you like a small practical example in Python (using scikit-learn) for regression and classification?
