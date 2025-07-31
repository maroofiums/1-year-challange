# Day122

### 🔍 Text Processing & Tokenization in NLP (Natural Language Processing)

Text processing and tokenization are the **first steps** in any NLP pipeline. These steps prepare raw text for tasks like classification, translation, or chatbot development.

---

## 🧼 1. Text Preprocessing Steps

Before tokenization, you usually clean the text. Typical steps include:

| Step                         | Description                        | Example                                 |
| ---------------------------- | ---------------------------------- | --------------------------------------- |
| **Lowercasing**              | Converts all text to lowercase     | `"Hello"` → `"hello"`                   |
| **Removing Punctuation**     | Removes symbols like `.`, `,`, `!` | `"hello!"` → `"hello"`                  |
| **Removing Stop Words**      | Removes common but useless words   | `"is", "the", "and"`                    |
| **Stemming / Lemmatization** | Reduces words to root form         | `"running"` → `"run"`                   |
| **Removing Numbers**         | Often optional                     | `"I have 2 apples"` → `"I have apples"` |
| **Whitespace Normalization** | Fixes extra spaces/tabs            | `"  hello   world "` → `"hello world"`  |

---

## 🔪 2. Tokenization

**Tokenization** is the process of breaking down text into smaller units — **tokens**. These can be:

* **Words** → `"I love NLP"` → `["I", "love", "NLP"]`
* **Sentences** → `"Hi. How are you?"` → `["Hi.", "How are you?"]`
* **Subwords** (used in modern NLP models like BERT)

---

## 🛠️ 3. Code Examples (in Python)

### 🔹 Using NLTK

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')

text = "Natural Language Processing is awesome! Let's learn it."

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)
```

### 🔹 Using spaCy

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Natural Language Processing is fun and useful.")

# Tokens
tokens = [token.text for token in doc]
print("Tokens:", tokens)
```

---

## 🧠 4. Advanced Tokenizers

| Library                    | Features                                        |
| -------------------------- | ----------------------------------------------- |
| **NLTK**                   | Classical NLP, customizable                     |
| **spaCy**                  | Fast, modern, supports named entity recognition |
| **HuggingFace Tokenizers** | Subword tokenization for BERT, GPT, etc.        |
| **gensim**                 | Good for word2vec/tokenization with large texts |

---

## 📌 Notes

* Use **subword tokenization** (e.g., BPE) for deep learning models.
* Preprocessing should be **task-dependent**. Don't remove stopwords if you’re doing sentiment analysis (they might carry meaning).
* Always maintain a **consistent pipeline** during training and inference.

---

