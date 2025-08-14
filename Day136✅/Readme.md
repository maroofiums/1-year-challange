# Day136

## **1. Text Processing in NLP**

Text processing is the **preparation of raw text** so that it can be analyzed by NLP models or algorithms. Raw text is messy—it can have punctuation, numbers, different cases, extra spaces, emojis, etc. The goal of text processing is to **clean and standardize** text data.

**Common Steps in Text Processing:**

1. **Lowercasing**
   Convert all text to lowercase so that words like `"Apple"` and `"apple"` are treated the same.

   ```python
   text = "Hello World"
   text = text.lower()  # "hello world"
   ```

2. **Removing Punctuation & Special Characters**

   ```python
   import string
   text = "Hello, world!"
   text = text.translate(str.maketrans('', '', string.punctuation))  # "Hello world"
   ```

3. **Removing Stopwords**
   Stopwords are common words like "the", "is", "and", which usually do not add meaning.

   ```python
   from nltk.corpus import stopwords
   from nltk.tokenize import word_tokenize

   stop_words = set(stopwords.words('english'))
   words = word_tokenize("This is an example sentence")
   words = [w for w in words if w not in stop_words]  # ['example', 'sentence']
   ```

4. **Stemming / Lemmatization**
   Reduce words to their root form.

   ```python
   from nltk.stem import PorterStemmer
   from nltk.stem import WordNetLemmatizer

   stemmer = PorterStemmer()
   stemmer.stem("running")  # "run"

   lemmatizer = WordNetLemmatizer()
   lemmatizer.lemmatize("running", pos='v')  # "run"
   ```

5. **Removing Numbers / Extra Whitespace**
   Regular expressions are often used:

   ```python
   import re
   text = "There are 123 apples"
   text = re.sub(r'\d+', '', text)  # "There are  apples"
   text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
   ```

---

## **2. Tokenization**

Tokenization is the process of **splitting text into smaller units called tokens**. Tokens can be:

* **Words**: `"Hello world"` → `["Hello", "world"]`
* **Subwords / Characters**: `"Hello"` → `["H", "e", "l", "l", "o"]`
* **Sentences**: `"Hello world. How are you?"` → `["Hello world.", "How are you?"]`

Tokenization is **one of the first steps** in NLP pipelines because most algorithms cannot work with raw strings—they need tokens.

### **Word Tokenization**

```python
from nltk.tokenize import word_tokenize

text = "I love NLP!"
tokens = word_tokenize(text)  # ['I', 'love', 'NLP', '!']
```

### **Sentence Tokenization**

```python
from nltk.tokenize import sent_tokenize

text = "Hello world. How are you?"
sentences = sent_tokenize(text)  # ['Hello world.', 'How are you?']
```

### **Subword / Byte-Pair Encoding (BPE)**

Modern NLP models like **GPT, BERT** use subword tokenization to handle unknown words:

* `"unhappiness"` → `["un", "##happy", "##ness"]`
* Benefits: Handles rare words and reduces vocabulary size.

---

## **3. Why Tokenization Matters**

* Tokenization affects **model performance**—poor tokenization may split words incorrectly or keep unwanted characters.
* It’s the **bridge between raw text and embeddings**, which are numerical representations models use.

---

## **4. Python Tools for Tokenization**

* **NLTK** – classic, good for learning
* **spaCy** – fast and modern, handles sentences, words, POS tagging
* **Hugging Face Tokenizers** – for subword and transformer models
* **TextBlob** – simple tokenization

Example with spaCy:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I love natural language processing!")
tokens = [token.text for token in doc]  # ['I', 'love', 'natural', 'language', 'processing', '!']
```

---

✅ **Summary**

1. **Text processing** cleans and normalizes raw text.
2. **Tokenization** splits text into units (words, subwords, sentences) for analysis.
3. Proper text processing and tokenization are **crucial for NLP model accuracy**.


