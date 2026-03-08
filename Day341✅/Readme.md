# Day341 - AI Text Generator

A simple **Generative AI project** that generates text from a user-provided prompt using a pretrained language model (GPT-2).

This project demonstrates the **core mechanism of text generation** used in modern LLMs without using retrieval or external documents.

---

## Features

* Generate coherent text from any prompt
* Control creativity with `temperature`, `top_k`, and `top_p` parameters
* Supports multiple return sequences
* Easy to extend to web or CLI applications

---

## Demo

Input:

```
Prompt: Artificial Intelligence is
```

Output:

```
Artificial Intelligence is transforming industries by enabling machines to learn from data and make intelligent decisions.
```

---

## Installation

Install the required libraries using pip:

```bash
pip install transformers torch
```

---

## Usage

```python
from transformers import pipeline

# Load GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Generate text
prompt = "Artificial Intelligence is"
output = generator(
    prompt,
    max_length=50,
    temperature=0.8,
    top_k=50,
    top_p=0.95
)

print(output[0]["generated_text"])
```

---

## Parameters

| Parameter     | Description                                  |
| ------------- | -------------------------------------------- |
| `prompt`      | Input text for the model                     |
| `max_length`  | Maximum number of tokens to generate         |
| `temperature` | Controls creativity (higher → more creative) |
| `top_k`       | Limits token choices to top-k candidates     |
| `top_p`       | Cumulative probability for nucleus sampling  |

---
