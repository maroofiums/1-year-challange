# Day 342 - PyTorch Neural Network 

## Overview

This project demonstrates a simple **feedforward neural network built with PyTorch**.
The model takes **10 input features** and predicts **one output value** using fully connected layers.

The goal of this demo is to understand:

* How to define a neural network using `nn.Module`
* How the **forward pass** works
* How to generate **demo data**
* How to run a **basic training loop**

---

## Model Architecture

The neural network consists of three fully connected layers.

```
Input (10 features)
      ↓
Linear Layer (10 → 32)
      ↓
ReLU Activation
      ↓
Linear Layer (32 → 16)
      ↓
ReLU Activation
      ↓
Linear Layer (16 → 1)
      ↓
Output
```

### Mathematical Representation

Each linear layer computes:

[
y = Wx + b
]

Where:

* (W) = weights
* (x) = input
* (b) = bias

The **ReLU activation function** introduces non-linearity:

[
ReLU(x) = \max(0, x)
]

---

## Model Implementation

```python
import torch
import torch.nn as nn

class NeuralNet(nn.Module):

    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(10, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 1)

    def forward(self, x):

        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)

        return x
```

---

## Creating Demo Data

The model expects **10 input features**, so the input tensor must have shape:

```
(batch_size, 10)
```

Example demo data:

```python
X = torch.randn(8, 10)   # 8 samples, 10 features
y = torch.randn(8, 1)    # target values
```

---

## Forward Pass

The forward pass sends input data through the network.

```python
model = NeuralNet()

predictions = model(X)

print(predictions.shape)
```

Output shape:

```
torch.Size([8, 1])
```

This means the model generates **one prediction for each sample**.

---

## Training the Model

To train the model we need:

* Loss function
* Optimizer
* Training loop

### Loss Function

We use **Mean Squared Error (MSE)** for regression tasks.

```python
criterion = nn.MSELoss()
```

### Optimizer

The optimizer updates the model weights.

```python
import torch.optim as optim

optimizer = optim.Adam(model.parameters(), lr=0.01)
```

---

## Training Loop

```python
for epoch in range(50):

    pred = model(X)

    loss = criterion(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print("Loss:", loss.item())
```

Training steps:

1. Forward pass
2. Compute loss
3. Backpropagation
4. Update weights

---

## Expected Workflow

```
Input Data
    ↓
Model Forward Pass
    ↓
Prediction
    ↓
Loss Calculation
    ↓
Backpropagation
    ↓
Optimizer Updates Weights
```

---

## Key PyTorch Concepts

| Concept       | Description                                   |
| ------------- | --------------------------------------------- |
| Tensor        | Multi-dimensional array used in PyTorch       |
| nn.Module     | Base class for all neural networks            |
| Linear Layer  | Fully connected neural network layer          |
| ReLU          | Activation function introducing non-linearity |
| Loss Function | Measures prediction error                     |
| Optimizer     | Updates model parameters                      |

---

## Purpose of This Demo

This example demonstrates the **basic PyTorch pipeline** used in most deep learning projects:

```
Data → Model → Prediction → Loss → Backpropagation → Optimization
```

Understanding this pipeline is essential before building more advanced models such as:

* Convolutional Neural Networks (CNNs)
* Recurrent Neural Networks (RNNs)
* Transformers
* Large Language Models

---
