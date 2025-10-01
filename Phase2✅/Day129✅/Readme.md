# **Day 129**

---

## 🔹 1. What Is a Neural Network?

A **Neural Network** is a computational model inspired by the human brain, used primarily in machine learning and artificial intelligence to recognize patterns and solve problems like classification, regression, and more.

---

## 🔹 2. Perceptron (The Simplest Neural Network)

### 🧠 What is a Perceptron?

* A **Perceptron** is the **basic building block** of neural networks.
* It takes multiple inputs, applies **weights**, adds a **bias**, and passes the result through an **activation function** to produce an output.

### 🧮 Formula:

$$
\text{output} = \text{activation}(w_1x_1 + w_2x_2 + \cdots + w_nx_n + b)
$$

Where:

* $x_i$ = input features
* $w_i$ = weights
* $b$ = bias
* activation = usually a **step function** in a basic perceptron

### 🔍 Use Case:

* Solves **linearly separable** problems (e.g., AND, OR)
* **Cannot** solve non-linearly separable problems (e.g., XOR)

---

## 🔹 3. Multilayer Perceptron (MLP)

### 🧠 What is an MLP?

* An **MLP** is a type of **feedforward neural network** that contains one or more **hidden layers** between the input and output layers.
* Each neuron in one layer is connected to **every neuron** in the next layer (fully connected).

### 🎯 Key Features:

* Solves **non-linear** problems
* Can approximate any function given enough hidden neurons (Universal Approximation Theorem)

### 🔗 Architecture:

```
Input Layer → Hidden Layer(s) → Output Layer
```

### ⚙️ Components:

* **Weights** and **biases** (learnable parameters)
* **Activation Functions** like:

  * ReLU (Rectified Linear Unit)
  * Sigmoid
  * Tanh

### 🧠 Forward Propagation:

Each neuron processes inputs using:

$$
z = w \cdot x + b \\
a = \text{activation}(z)
$$

### 🔁 Backpropagation:

* Used to **update weights** by minimizing the **loss function** using **gradient descent**
* Uses the **chain rule** to compute gradients

---

## 🔍 Comparison: Perceptron vs MLP

| Feature             | Perceptron      | MLP                       |
| ------------------- | --------------- | ------------------------- |
| Layers              | Single layer    | Multiple layers           |
| Problem Type        | Linear          | Non-linear                |
| Learning Algorithm  | Perceptron rule | Backpropagation           |
| Activation Function | Step function   | ReLU, Sigmoid, Tanh, etc. |

---

## 🧪 Example Use Cases

* **Perceptron:** Binary classification (e.g., spam vs. not spam)
* **MLP:** Image classification, speech recognition, text generation

---
