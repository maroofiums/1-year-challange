# Day 307
# 🧠 PyTorch One-Page Cheat Sheet (Data Science)

## 📦 Import Basics

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
```

---

## 🔢 Tensor (Core of PyTorch)

```python
x = torch.tensor([1,2,3], dtype=torch.float32)
x = torch.randn(10, 3)
x = torch.zeros(5)
```

✔ Like NumPy array
✔ Supports GPU
✔ Supports gradients

```python
x.device          # cpu / cuda
x.shape
x.dtype
```

---

## 🔁 NumPy ↔ Tensor

```python
import numpy as np

t = torch.from_numpy(np_array)
n = t.numpy()
```

⚠️ Same memory share — be careful

---

## 🧮 Autograd (Gradient)

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2
y.backward()
print(x.grad)
```

👉 No manual calculus needed
👉 Used in backpropagation

---

## 🗂️ Dataset & DataLoader

```python
class MyDataset(Dataset):
    def __len__(self): ...
    def __getitem__(self, idx): ...
```

```python
loader = DataLoader(dataset, batch_size=32, shuffle=True)
```

✔ Batch training
✔ Memory efficient

---

## 🧠 Model (Neural Network)

```python
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)
```

🧩 `__init__` → layers
🧩 `forward()` → data flow

---

## 📉 Loss Functions

```python
nn.MSELoss()              # Regression
nn.CrossEntropyLoss()     # Classification
nn.BCELoss()              # Binary
```

Loss = model kitna ghalat hai

---

## ⚙️ Optimizers

```python
optim.SGD(model.parameters(), lr=0.01)
optim.Adam(model.parameters(), lr=0.001)
```

Adam = default best choice 👍

---

## 🔁 Training Loop (🔥 MOST IMPORTANT)

```python
for x, y in loader:
    pred = model(x)
    loss = loss_fn(pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

### Yaad Rakho Order:

1. Forward
2. Loss
3. Zero grad
4. Backward
5. Step

---

## 🧪 Train vs Eval Mode

```python
model.train()
model.eval()

with torch.no_grad():
    output = model(x)
```

⚠️ Testing mein gradients off karo

---

## 🚀 GPU Usage

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
x = x.to(device)
```

---

## 📊 Common Data Science Tasks

| Task           | PyTorch                |
| -------------- | ---------------------- |
| Regression     | Linear / NN            |
| Classification | Softmax + CE           |
| NLP            | Embedding, Transformer |
| CV             | CNN                    |
| Time Series    | LSTM / GRU             |

---

## ❌ Common Mistakes

❌ Forget `zero_grad()`
❌ Training full data at once
❌ Mixing NumPy & Tensor
❌ No `model.eval()` in testing

---
