
# Day305 => Pretrained ML Models Project

This project demonstrates the use of **pretrained machine learning models** for **Natural Language Processing (NLP)** and **Computer Vision (CV)** tasks.  
It leverages the power of models already trained on large datasets to perform predictions **without training from scratch**.

---

## Features

### NLP – Sentiment Analysis
- Uses **BERT** from Hugging Face Transformers library
- Predicts **sentiment** of input text: POSITIVE / NEGATIVE
- Handles **single and batch text input**
- Example:
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I love learning Machine Learning!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]
````

### Computer Vision – Image Classification

* Uses **ResNet18** pretrained on **ImageNet**
* Predicts **class of input image**
* Includes proper **image preprocessing and normalization**
* Example:

```python
from torchvision import models, transforms
from PIL import Image
import torch

# Load model
model = models.resnet18(pretrained=True)
model.eval()

# Preprocess image
image = Image.open("dog.jpg")
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485,0.456,0.406], std=[0.229,0.224,0.225])
])
img_tensor = preprocess(image).unsqueeze(0)

# Prediction
with torch.no_grad():
    outputs = model(img_tensor)
    _, predicted = torch.max(outputs, 1)
print(predicted.item())
```

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install torch torchvision transformers datasets scikit-learn pillow
```

---

---

## How to Use

1. **NLP:**

   * Open `nlp/sentiment_analysis.ipynb`
   * Run the notebook and input your own text
2. **CV:**

   * Open `cv/image_classification.ipynb
   * Replace sample image with your own image file
   * Run the notebook to get the predicted label

---

## Notes

* Pretrained models **do not require training** for inference
* Proper **preprocessing** is necessary for accurate predictions
* Fine-tuning is optional for custom datasets

---

## References

* Hugging Face Transformers: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
* Torchvision Pretrained Models: [https://pytorch.org/vision/stable/models.html](https://pytorch.org/vision/stable/models.html)
* ImageNet Classes: [https://github.com/pytorch/hub/blob/master/imagenet_classes.txt](https://github.com/pytorch/hub/blob/master/imagenet_classes.txt)

---
