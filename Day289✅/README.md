# Day289 - Neural Network From Scratch (Using NumPy)

A step-by-step implementation of a basic Neural Network without using any deep learning framework.
This project helps understand the **core logic behind forward propagation, loss calculation, and backpropagation**.

---

## 1. Overview

A Neural Network is a mathematical model inspired by the human brain.  
It learns patterns by adjusting **weights** and **biases** using data.

This implementation includes:
- 1 Hidden Layer
- ReLU Activation
- Sigmoid Output
- Gradient Descent

---

## 2. Dependencies

Only NumPy is used to keep things transparent and beginner-friendly.

```python
import numpy as np
````

> Best Practice:
> If NumPy matrix operations are not clear, revise NumPy before moving forward.

---

## 3. Activation Functions

### Sigmoid (Output Layer)

```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
```

### Sigmoid Derivative

```python
def sigmoid_derivative(x):
    return x * (1 - x)
```

> Tip:
>
> * Sigmoid → Binary Classification
> * ReLU → Hidden Layers (faster learning)

---

## 4. Neural Network Architecture

```python
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.w1 = np.random.randn(input_size, hidden_size)
        self.b1 = np.zeros((1, hidden_size))

        self.w2 = np.random.randn(hidden_size, output_size)
        self.b2 = np.zeros((1, output_size))
```

**Why random weights?**
Zero weights → no learning ❌
Random weights → symmetry break ✔️

---

## 5. Forward Propagation

```python
def forward(self, X):
    self.z1 = np.dot(X, self.w1) + self.b1
    self.a1 = np.maximum(0, self.z1)  # ReLU

    self.z2 = np.dot(self.a1, self.w2) + self.b2
    self.output = sigmoid(self.z2)

    return self.output
```

Flow:

```
Input → Linear → ReLU → Linear → Sigmoid → Output
```

---

## 6. Loss Function

Mean Squared Error (MSE):

```python
def loss(y, y_hat):
    return np.mean((y - y_hat) ** 2)
```

> Industry Note:
> Cross-Entropy is preferred in real-world models, but MSE is easier to understand.

---

## 7. Backpropagation

```python
def backward(self, X, y, lr=0.01):
    error = y - self.output
    d_output = error * sigmoid_derivative(self.output)

    d_w2 = np.dot(self.a1.T, d_output)
    d_b2 = np.sum(d_output, axis=0, keepdims=True)

    d_hidden = np.dot(d_output, self.w2.T)
    d_hidden[self.z1 <= 0] = 0  # ReLU derivative

    d_w1 = np.dot(X.T, d_hidden)
    d_b1 = np.sum(d_hidden, axis=0, keepdims=True)

    self.w2 += lr * d_w2
    self.b2 += lr * d_b2
    self.w1 += lr * d_w1
    self.b1 += lr * d_b1
```

**Backprop ka simple matlab:**
Galti measure karo → peeche jao → weights improve karo.

---

## 8. Training the Model (XOR Problem)

```python
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

for epoch in range(10000):
    output = nn.forward(X)
    nn.backward(X, y)

    if epoch % 1000 == 0:
        print("Loss:", loss(y, output))
```

> XOR is a classic test to verify if a Neural Network actually learns.

---

## 9. Key Learnings

* Neural Networks are **pure math + logic**
* Forward pass → Prediction
* Backward pass → Learning
* Gradient Descent → Optimization

---

## 10. Common Mistakes to Avoid

* Jumping directly to TensorFlow/PyTorch
* Ignoring matrix dimensions
* Using very high learning rates
* Memorizing code instead of understanding flow

---

## 11. Conclusion

Understanding Neural Networks from scratch builds a **strong ML foundation**.
Once this is clear, frameworks become tools — not magic.

> **Golden Rule:**
> Forward → Loss → Backward → Update → Repeat

---
