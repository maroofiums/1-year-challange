# Day157

---

## 1. **Perceptron (The Building Block)**

The **perceptron** is the simplest type of neural network, proposed by Frank Rosenblatt in 1958.

### Structure:

* **Inputs**: $x_1, x_2, ..., x_n$
* **Weights**: $w_1, w_2, ..., w_n$ (adjustable parameters)
* **Bias**: $b$ (helps shift the decision boundary)
* **Linear combination**:

  $$
  z = w_1x_1 + w_2x_2 + \dots + w_nx_n + b
  $$
* **Activation function**: A step function (originally)

  $$
  y = \begin{cases}
  1 & \text{if } z \geq 0 \\
  0 & \text{if } z < 0
  \end{cases}
  $$

### Limitation:

* Can only solve **linearly separable problems** (e.g., AND, OR).
* Cannot solve **XOR** (non-linear).

---

## 2. **Multilayer Perceptron (MLP)**

To overcome perceptron limitations, we use **multiple layers** and **non-linear activation functions**.

### Structure:

* **Input layer**: Takes features.
* **Hidden layers**: Multiple perceptrons stacked. Each neuron applies a weighted sum + activation function.
* **Output layer**: Produces final predictions (e.g., class probabilities).

### Activation Functions:

* **Sigmoid**: Squashes values into $(0,1)$
* **tanh**: Squashes values into $(-1,1)$
* **ReLU**: $f(x) = \max(0, x)$ → helps with vanishing gradient

### Forward Pass:

1. Input data flows through the network.
2. Each layer computes:

   $$
   a^{(l)} = f(W^{(l)} a^{(l-1)} + b^{(l)})
   $$

   where $f$ = activation function.

### Backpropagation (Learning):

* Compute error (loss function).
* Use **gradient descent** to adjust weights $W$ and biases $b$.
* Gradients are computed using **chain rule** (backprop).

---

## 3. **Why MLP Works Better**

* Multiple layers + non-linear activation allow the network to approximate **any continuous function** (Universal Approximation Theorem).
* Can solve non-linear problems like XOR, image recognition, and more.

---

✅ **Summary Table**

| Feature      | Perceptron           | MLP (Multilayer Perceptron)        |
| ------------ | -------------------- | ---------------------------------- |
| Layers       | Single               | Multiple (≥ 1 hidden)              |
| Activation   | Step                 | Sigmoid, ReLU, tanh, etc.          |
| Problem Type | Linearly separable   | Linear + Non-linear                |
| Training     | Simple rule          | Backpropagation + Gradient Descent |
| Applications | Basic classification | Deep Learning (vision, NLP, etc.)  |

---
