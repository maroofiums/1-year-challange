# Day 94

## 🚀 1. What is a Perceptron?

A **Perceptron** is the simplest neural network — basically a **linear binary classifier**.

### 🔹 Formula:

$$
y = \text{activation}(w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b)
$$

Where:

* $x_1, x_2, \dots$ = Inputs
* $w_1, w_2, \dots$ = Weights
* $b$ = Bias
* **Activation** = usually `step` or `sigmoid` function

---

### 🔸 Perceptron Logic Gate Example (AND gate)

| x1 | x2 | Output |
| -- | -- | ------ |
| 0  | 0  | 0      |
| 0  | 1  | 0      |
| 1  | 0  | 0      |
| 1  | 1  | 1      |

```python
import numpy as np

def perceptron(x1, x2):
    w1, w2 = 1, 1
    bias = -1.5
    x = w1 * x1 + w2 * x2 + bias
    return 1 if x > 0 else 0

# Test AND gate
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(f"{x1} AND {x2} = {perceptron(x1, x2)}")
```

---

## 🧠 2. What is an MLP (Multi-Layer Perceptron)?

An **MLP** is a **deep neural network** — made of:

* **Input layer**
* **Hidden layers (1 or more)**
* **Output layer**

> Each layer has **neurons (nodes)** connected with weights and activation functions.

---

### 🔹 Architecture Example:

```
Input (x1, x2) →
   [Hidden Layer]
      ⬇️
   [Output Layer (y)]
```

---

### 🔸 Simple MLP with Scikit-learn

```python
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create MLP model
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 🔧 Activation Functions (Used in Perceptron & MLP)

| Name    | Formula                           | Use in                     |
| ------- | --------------------------------- | -------------------------- |
| Step    | $1 \text{ if } x > 0$             | Perceptron                 |
| Sigmoid | $\frac{1}{1 + e^{-x}}$            | MLP                        |
| ReLU    | $\max(0, x)$                      | MLP                        |
| Softmax | Converts outputs to probabilities | Output layer (multi-class) |

---

## 🎯 Summary

| Concept    | Description                         |
| ---------- | ----------------------------------- |
| Perceptron | Single-layer binary classifier      |
| MLP        | Multi-layer NN for complex problems |
| Activation | Adds non-linearity                  |
| Training   | Weights updated using backprop      |

---

## 🧪 Want Notebook + Visual?

I can give you a **Google Colab notebook** with:

* Logic gate examples
* MLP training
* Interactive visuals

---

Bol do:

* `YES` to get the **Colab notebook** 🔗
* Or want to build your **own mini neural network** from scratch using NumPy?

Main tumhara full support hon Maroof 💪
