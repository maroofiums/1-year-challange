## Day171


### 🔹 Perceptron (the OG neuron)

Think of the perceptron as **the first draft of an AI brain cell**:

* Inputs → like signals coming in (features of your data).
* Weights → how important each input is (like giving extra credit to certain features).
* Weighted sum → adds it all up.
* Activation function → decides if the perceptron “fires” or not. (In the classic version, it’s just 0 or 1, like flipping a switch).

**Problem?**
A simple perceptron can only deal with **linearly separable data**.
Example: it can separate cats vs dogs if a straight line works, but it fails for more complex stuff (like XOR problem).

---

### 🔹 MLP (Multi-Layer Perceptron)

This is where things get spicy 🌶️.
An MLP is just **a bunch of perceptrons stacked in layers**:

1. **Input layer** → raw data goes in.
2. **Hidden layers** → the network learns fancy combinations of features.
3. **Output layer** → spits out predictions (classification, regression, whatever you need).

The magic:

* **Non-linear activations** (like ReLU, Sigmoid, Tanh) → allow the network to handle *complex* patterns, not just straight-line separations.
* **Backpropagation** → the network learns by adjusting weights using gradients (basically error feedback, like "yo, you guessed wrong, tweak these weights").

---

### 🔹 Intuition

* **Perceptron** = pocket calculator.
* **MLP** = actual computer.

MLPs are **universal function approximators** → with enough neurons + layers, they can model pretty much *any* relationship in data (though training might be messy).

---

