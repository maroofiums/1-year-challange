# Day 108

---

## 🧠 **1. Perceptron (Single-layer Neural Network)**

### 🔹 Definition:

A **Perceptron** is the **simplest form of a neural network**, used for **binary classification**.

### 🔹 Structure:

* **Inputs (x₁, x₂, ..., xₙ)**
* **Weights (w₁, w₂, ..., wₙ)**
* **Bias (b)**
* **Activation Function** (e.g., step function)

### 🔹 Formula:

$$
y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)
$$

Where:

* $f$ is usually a **step function**:

$$
f(z) =
\begin{cases}
1 & \text{if } z \geq 0 \\
0 & \text{otherwise}
\end{cases}
$$

### 🔹 Working:

1. Compute weighted sum $z = \sum w_i x_i + b$
2. Pass through activation function to get output (0 or 1)

### 🔹 Limitation:

Can only solve **linearly separable** problems (like AND, OR) — **NOT XOR**.

---

## 🧠 **2. Multilayer Perceptron (MLP)**

### 🔹 Definition:

A **Multilayer Perceptron** is a type of **Feedforward Neural Network** with one or more **hidden layers**.

### 🔹 Structure:

* **Input layer**
* **Hidden layer(s)** (one or more)
* **Output layer**

Each layer is made of **neurons (nodes)** connected with **weights**.

```
[Input Layer] → [Hidden Layer(s)] → [Output Layer]
```

### 🔹 Activation Functions:

Instead of a step function, we use non-linear activations:

* ReLU: $f(x) = \max(0, x)$
* Sigmoid: $f(x) = \frac{1}{1 + e^{-x}}$
* Tanh: $f(x) = \tanh(x)$

### 🔹 Forward Pass:

Each neuron computes:

$$
z = \sum w_i x_i + b,\quad a = \text{activation}(z)
$$

### 🔹 Backpropagation:

Used for **training**:

* Computes **loss** (e.g., MSE, Cross-Entropy)
* Uses **gradient descent** to adjust weights via **chain rule** (partial derivatives)

---

## 🔁 Summary Table:

| Feature               | Perceptron      | MLP (Multilayer Perceptron) |
| --------------------- | --------------- | --------------------------- |
| Layers                | 1               | 2 or more                   |
| Can solve XOR?        | ❌ No            | ✅ Yes                       |
| Activation Function   | Step            | ReLU, Sigmoid, etc.         |
| Learning Algorithm    | Perceptron Rule | Backpropagation             |
| Non-linearity support | ❌               | ✅                           |

