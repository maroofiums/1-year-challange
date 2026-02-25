# Day329 - MNIST Digit Classifier (CNN + Streamlit)

A simple yet powerful **digit recognition app** built using **Convolutional Neural Networks (CNN)** trained on the **MNIST dataset**, and deployed using **Streamlit**.
You can **draw a digit (0–9)** on the canvas, and the model will predict it instantly!

---

## 🚀 Features

* 🖌️ Draw any digit (0–9) on screen
* 🤖 CNN-based prediction using TensorFlow/Keras
* ⚡ Real-time inference with Streamlit UI
* 💾 Model saved and loaded in `.keras` format
* 🌐 Ready for Streamlit Cloud deployment

---

## 🧩 Tech Stack

| Component      | Tool                              |
| -------------- | --------------------------------- |
| Model Training | TensorFlow / Keras                |
| Frontend UI    | Streamlit                         |
| Visualization  | Matplotlib                        |
| Dataset        | MNIST (70,000 handwritten digits) |

---

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the repo

```bash
git clone https://github.com/maroofiums/mnist-digit-classifier.git
cd mnist-digit-classifier
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit app

```bash
streamlit run main.py
```

### 4️⃣ Draw and predict!

A canvas will appear — draw a number (0–9), and the model will show its prediction.

---

## 🧠 Model Summary

| Layer     | Type               | Output Shape |
| --------- | ------------------ | ------------ |
| Conv2D    | Feature Extraction | (28,28,32)   |
| MaxPool2D | Downsampling       | (14,14,32)   |
| Conv2D    | Deep Features      | (14,14,64)   |
| Flatten   |                    | (12544)      |
| Dense     | Hidden Layer       | (128)        |
| Dense     | Output (Softmax)   | (10)         |

---

## 🧾 Requirements

```
streamlit
tensorflow
numpy
matplotlib
streamlit-drawable-canvas
```

---

