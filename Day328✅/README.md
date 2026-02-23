

# Day328 - MNIST Handwritten Digit Classifier

A Convolutional Neural Network (CNN) model that recognizes handwritten digits (0–9) from user drawings. Built with TensorFlow/Keras and deployed as an interactive web application using Streamlit.

---

## **Project Overview**

This project demonstrates the full workflow of a machine learning model: data preprocessing, CNN model training, evaluation, and deployment. Users can draw digits on a canvas and get real-time predictions with confidence scores and probability distributions.

---

## **Features**

* Draw digits (0–9) using a mouse or touchscreen
* Real-time predictions with confidence score
* Probability distribution visualization for all digits
* Fully interactive web interface via Streamlit

---

## **Model Details**

* **Dataset:** MNIST (handwritten digits)
* **Architecture:**

  * Conv2D + MaxPooling layers
  * Flatten + Dense layers
  * Softmax output for 10 classes
* **Optimizer:** Adam
* **Loss Function:** Categorical Crossentropy
* **Test Accuracy:** 99.02%

---

## **Tech Stack**

* Python
* TensorFlow / Keras
* NumPy, Matplotlib, Seaborn
* Streamlit
* PIL



## **Usage**

1. Open the web app in your browser (Streamlit will provide a local link).
2. Use the drawing canvas to draw a digit (0–9).
3. Click **Predict** to see the predicted digit and confidence.
4. View the probability distribution bar chart to understand model certainty.


---

## **Live Demo**

[https://mnist-digit-classifier-by-maroofiums.streamlit.app/](https://mnist-digit-classifier-by-maroofiums.streamlit.app/)

---

## **Repository**

[https://github.com/maroofiums/MNIST-Digit-Classifier/](https://github.com/maroofiums/MNIST-Digit-Classifier/)

---

## **Kaggle Notebook**

[https://www.kaggle.com/code/maroofiums/digit-classification-using-cnn](https://www.kaggle.com/code/maroofiums/digit-classification-using-cnn)

---
