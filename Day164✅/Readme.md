# **Day164**

---

## **1. Why Text Processing?**

Raw text is messy. Computers don’t understand `"I LOVE NLP!!! 😍🔥"`.
We need to **clean** and **normalize** it into something a model can handle.

**Text processing usually includes:**

* Lowercasing → `"I LOVE NLP"` → `"i love nlp"`
* Removing punctuation → `"hello!!!"` → `"hello"`
* Removing numbers / symbols if not needed
* Removing stopwords (common words like *is, the, and*)
* Lemmatization/Stemming → `"studies" → "study"`

---

## **2. Tokenization**

**Tokenization = splitting text into smaller units (tokens).**

### ✂️ Types:

* **Word Tokenization** → `"I love NLP"` → `["I", "love", "NLP"]`
* **Sentence Tokenization** → `"I love NLP. It's fun."` → `["I love NLP.", "It's fun."]`
* **Subword Tokenization** (used in BERT, GPT) → `"unhappiness"` → `["un", "happiness"]`

---

## **3. Hands-on (NLTK)**

```python
import nltk
nltk.download("punkt")

from nltk.tokenize import word_tokenize, sent_tokenize

text = "Natural Language Processing is awesome! Let's learn fast."

# Sentence tokenization
print("Sentences:", sent_tokenize(text))

# Word tokenization
print("Words:", word_tokenize(text))
```

➡️ Output:

```
Sentences: ['Natural Language Processing is awesome!', "Let's learn fast."]
Words: ['Natural', 'Language', 'Processing', 'is', 'awesome', '!', 'Let', "'s", 'learn', 'fast', '.']
```

---

## **4. Hands-on (spaCy — faster & smarter)**

```python
!pip install spacy
!python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("NLP makes machines understand text better.")

print([token.text for token in doc])   # Word tokens
```

➡️ Output:

```
['NLP', 'makes', 'machines', 'understand', 'text', 'better', '.']
```

---

## **5. Real Use**

* Feeding tokens into **vectorizers (TF-IDF, Word2Vec, embeddings)**
* Cleaning search queries
* Splitting sentences for **chatbots & summarizers**
* Breaking down text before **classification, sentiment, NER, translation**

---

⚡ **Summary:**
👉 Text processing cleans your text.
👉 Tokenization splits it into chunks (words/sentences/subwords).
👉 Without this step, **no NLP model works.**

---
