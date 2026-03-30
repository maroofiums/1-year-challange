# Day 363
---
# CNN Image Classification Project (TensorFlow)

## Project Overview

This project implements a Convolutional Neural Network (CNN) using TensorFlow/Keras to classify images from the CIFAR-10 dataset. The model learns hierarchical features from images such as edges, shapes, and object-level patterns to perform multi-class classification.

---

# What I Learned

## Core Concepts

* What CNN is and why it is used
* Convolution operation for feature extraction
* ReLU activation function for non-linearity
* Max Pooling for downsampling and feature retention
* Flatten layer for converting 2D feature maps to 1D vectors
* Dense (fully connected) layers for classification
* Softmax function for probability output
* Basic overfitting understanding
* Model training and evaluation workflow

---

# CNN Workflow

Image → Convolution → ReLU → Pooling → Feature Extraction → Flatten → Dense Layers → Output Prediction

---

# Code Explanation

## 1. Import Libraries

```python
import tensorflow as tf
from tensorflow.keras import layers, models
```

### Explanation

* `tensorflow`: Main deep learning framework used for building and training neural networks.
* `keras`: High-level API inside TensorFlow that simplifies model building.
* `layers`: Contains all neural network layer types (Conv2D, Dense, etc.).
* `models`: Used to define the architecture (Sequential or Functional API).

---

## 2. Load Dataset

```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
```

### Explanation

* CIFAR-10 dataset contains 60,000 images.
* 10 classes such as airplane, car, bird, cat, etc.
* `x_train`: training images
* `y_train`: training labels
* `x_test`: test images
* `y_test`: test labels

---

## 3. Data Normalization

```python
x_train = x_train / 255.0
x_test = x_test / 255.0
```

### Explanation

* Pixel values range from 0 to 255.
* Normalization scales values to 0–1.
* Helps improve training stability and convergence speed.

---

## 4. CNN Model Architecture

```python
model = models.Sequential([
```

### Explanation

* Sequential model means layers are stacked in order (linear flow).

---

## Convolution Layer

```python
layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3))
```

### Parameters

* `32`: Number of filters (feature detectors)
* `(3,3)`: Kernel size (filter window)
* `activation='relu'`: Introduces non-linearity
* `input_shape=(32,32,3)`: Input image size (height, width, channels)

### Purpose

Extracts low-level features such as edges and textures.

---

## Max Pooling Layer

```python
layers.MaxPooling2D((2,2))
```

### Parameters

* `(2,2)`: Pooling window size

### Purpose

Reduces spatial dimensions while keeping important features.

---

## Deeper Convolution Layers

```python
layers.Conv2D(64, (3,3), activation='relu')
```

### Purpose

Learns more complex features like shapes and object parts.

---

## Flatten Layer

```python
layers.Flatten()
```

### Purpose

Converts 2D feature maps into a 1D vector for Dense layers.

---

## Dense Layer

```python
layers.Dense(64, activation='relu')
```

### Parameters

* `64`: Number of neurons
* `activation='relu'`: Non-linearity

### Purpose

Learns high-level patterns and decision boundaries.

---

## Output Layer

```python
layers.Dense(10, activation='softmax')
```

### Parameters

* `10`: Number of classes
* `softmax`: Converts outputs into probability distribution

### Purpose

Produces final class prediction.

---

## 5. Compile Model

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

### Explanation

* `optimizer='adam'`: Efficient weight optimization algorithm
* `loss='sparse_categorical_crossentropy'`: Used for multi-class classification
* `metrics=['accuracy']`: Tracks model performance

---

## 6. Train Model

```python
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
```

### Parameters

* `epochs=10`: Number of training iterations over dataset
* `validation_data`: Evaluates model on unseen data

---

## 7. Evaluate Model

```python
test_loss, test_acc = model.evaluate(x_test, y_test)
print(test_acc)
```

### Purpose

Measures model performance on test dataset.

---

# Final Summary

CNN works in three main stages:

1. Feature Extraction (Conv + ReLU + Pooling)
2. Feature Transformation (Flatten)
3. Classification (Dense + Softmax)

---

# Key Insight

CNN automatically learns spatial features from images without manual feature engineering.

