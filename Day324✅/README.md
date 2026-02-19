# Day 324


## **Step 1: Understand the Components of a Neural Network**

A neural network has:

1. **Inputs (features)** – your data.
2. **Weights** – parameters that determine importance of inputs.
3. **Bias** – allows shifting of the activation function.
4. **Activation Function** – introduces non-linearity (like Sigmoid, ReLU).
5. **Output** – final prediction.
6. **Loss Function** – measures error.
7. **Optimization / Gradient Descent** – updates weights and biases to minimize loss.

For our first model, we’ll do a **binary classification problem**, e.g., predicting if a student passes (1) or fails (0) based on hours studied.

---

## **Step 2: Initialize Libraries and Data**

```python
import numpy as np

# Example dataset: Hours studied vs Pass(1)/Fail(0)
X = np.array([[1], [2], [3], [4], [5], [6]])  # Hours studied
y = np.array([[0], [0], [0], [1], [1], [1]])  # Pass or Fail
```

---

## **Step 3: Initialize Parameters**

We need **weights** and **bias**. For now, we initialize randomly:

```python
# Initialize weights and bias
np.random.seed(42)
weights = np.random.rand(1, 1)  # 1 input, 1 output
bias = np.random.rand(1)
```

---

## **Step 4: Define Activation Function**

We’ll use **Sigmoid** first:

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    return z * (1 - z)
```

---

## **Step 5: Forward Propagation**

```python
def forward(X):
    return sigmoid(np.dot(X, weights) + bias)
```

Check prediction:

```python
output = forward(X)
print(output)
```

---

## **Step 6: Compute Loss (Binary Cross-Entropy)**

```python
def compute_loss(y_true, y_pred):
    m = y_true.shape[0]
    loss = -1/m * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return loss

loss = compute_loss(y, output)
print("Initial Loss:", loss)
```

---

## **Step 7: Backpropagation**

Update weights and bias using **gradient descent**:

```python
learning_rate = 0.1
epochs = 1000

for i in range(epochs):
    # Forward pass
    output = forward(X)
    
    # Compute loss
    loss = compute_loss(y, output)
    
    # Backward pass
    error = output - y
    d_weights = np.dot(X.T, error * sigmoid_derivative(output))
    d_bias = np.sum(error * sigmoid_derivative(output))
    
    # Update parameters
    weights -= learning_rate * d_weights
    bias -= learning_rate * d_bias
    
    if i % 100 == 0:
        print(f"Epoch {i}, Loss: {loss}")
```

---

## **Step 8: Make Predictions**

```python
def predict(X):
    pred = forward(X)
    return [1 if i > 0.5 else 0 for i in pred]

predictions = predict(X)
print("Predictions:", predictions)
print("Actual:", y.flatten())
```

---

✅ This is a **complete neural network from scratch**, with:

* One input
* One output
* Sigmoid activation
* Binary cross-entropy loss
* Gradient descent

