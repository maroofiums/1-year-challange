## 1. **Perceptron (Single-Layer Neural Network)**

The **perceptron** is the simplest type of artificial neural network, introduced by **Frank Rosenblatt (1958)**.

### Structure:

* **Inputs**: $x_1, x_2, ..., x_n$
* **Weights**: $w_1, w_2, ..., w_n$ (learned during training)
* **Bias**: $b$ (helps shift the decision boundary)
* **Activation Function**: Decides output (e.g., step function, sigmoid, ReLU, etc.)

### Formula:

$$
y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)
$$

Where:

* $f$ = activation function
* $y$ = output

### Limitation:

* A single perceptron can only solve **linearly separable problems** (like AND, OR).
* Cannot solve **XOR problem** (not linearly separable).

---

## 2. **Multi-Layer Perceptron (MLP)**

To overcome perceptron limitations, **MLP** introduces **hidden layers**.

### Structure:

* **Input layer** → accepts features.
* **Hidden layers** → multiple neurons stacked in layers, each applying nonlinear transformations.
* **Output layer** → final prediction.

Each neuron is a perceptron itself but connected in layers.

### Formula (for hidden layer neuron):

$$
h_j = f\left(\sum_{i=1}^{n} w_{ij} x_i + b_j\right)
$$

For output neuron:

$$
y_k = f\left(\sum_{j=1}^{m} v_{jk} h_j + c_k\right)
$$

Where:

* $h_j$ = hidden neuron output
* $y_k$ = final output

### Learning (Backpropagation):

* **Forward pass**: Input → Hidden → Output
* **Loss calculation**: Compare output with actual target
* **Backward pass**: Update weights using **gradient descent** and **chain rule**

---

## 3. **Activation Functions**

MLPs rely on nonlinear functions so they can approximate complex functions:

* **Sigmoid**: $\sigma(x) = \frac{1}{1+e^{-x}}$
* **Tanh**: squashes values between \[-1, 1]
* **ReLU**: $f(x) = \max(0, x)$
* **Softmax**: for classification

---

## 4. **Key Differences**

| Feature             | Perceptron         | MLP                       |
| ------------------- | ------------------ | ------------------------- |
| Layers              | 1                  | Multiple (≥2)             |
| Solves XOR?         | ❌                  | ✅                         |
| Nonlinear functions | No (step function) | Yes (ReLU, sigmoid, etc.) |
| Power               | Linear classifier  | Universal approximator    |

---

✅ **Summary**:

* **Perceptron** = single neuron, linear separator.
* **MLP** = multiple neurons in layers, powerful enough to approximate **any function** (given enough neurons and data).

---
