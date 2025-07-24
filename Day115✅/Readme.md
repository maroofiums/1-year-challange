# *Day 115*
**1. Text Processing**

Text Processing means preparing raw text so it can be used in ML models. Common steps include:

### ✅ Basic Steps:

| Step                 | Description                                           | Example                               |
| -------------------- | ----------------------------------------------------- | ------------------------------------- |
| Lowercasing          | Convert text to lowercase                             | "Hello" → "hello"                     |
| Removing punctuation | Eliminate commas, periods, etc.                       | "Hi, there!" → "Hi there"             |
| Removing stopwords   | Remove common words (e.g., "the", "is", "and")        | "This is a cat" → "cat"               |
| Stemming             | Reducing words to root form (aggressive)              | "playing", "played" → "play"          |
| Lemmatization        | Convert word to its base form (smarter than stemming) | "better" → "good", "was" → "be"       |
| Removing digits      | Remove numbers                                        | "There are 2 dogs" → "There are dogs" |
| Removing whitespaces | Strip extra spaces                                    | " Hello  world " → "Hello world"      |

📌 Python libraries: `re`, `nltk`, `spacy`, `string`

---

## 🔹 **2. Tokenization**

Tokenization is splitting text into smaller units: **words**, **subwords**, or **sentences**.

### ✅ Types:

| Type     | Description                     | Example                                                           |
| -------- | ------------------------------- | ----------------------------------------------------------------- |
| Word     | Splitting into individual words | "I love Python" → \["I", "love", "Python"]                        |
| Sentence | Splitting into sentences        | "I love NLP. It's powerful." → \["I love NLP.", "It's powerful."] |
| Subword  | For languages or unknown words  | "unhappiness" → \["un", "happi", "ness"]                          |

📌 Python tools: `nltk.word_tokenize`, `nltk.sent_tokenize`, `spacy`, `transformers` (WordPiece, BPE)

---

## ✅ Example in Python (using NLTK):

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

text = "The quick brown fox jumps over the lazy dog. It's amazing!"

# Lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenize
words = word_tokenize(text)

# Remove stopwords
words = [w for w in words if w not in stopwords.words('english')]

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(w) for w in words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(w) for w in words]

print("Tokens:", words)
print("Stemmed:", stemmed)
print("Lemmatized:", lemmatized)
```

---

## 📘 Use Case in ML

These steps help in:

* Reducing dimensionality
* Normalizing text input
* Improving model performance (especially in NLP tasks like sentiment analysis, classification, chatbots, etc.)

---
