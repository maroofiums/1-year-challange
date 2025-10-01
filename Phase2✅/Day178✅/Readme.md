# Day 178

## Features

- **Sentence Tokenization**: Split text into sentences.
- **Word Tokenization**: Split sentences into words or tokens.
- **Stop Word Removal**: Filter out common words like "the", "and", etc.
- **Stemming & Lemmatization**: Reduce words to their root form.
- **Modern NLP Support**: Uses `spaCy` for more advanced tokenization and preprocessing.

---

## Requirements

- Python 3.8+
- `nltk`
- `spacy`
- `en_core_web_sm` model for spaCy

Install dependencies:

```bash
pip install nltk spacy
python -m spacy download en_core_web_sm
````

---

## Usage

### NLTK Example

```python
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

text = "I love pizza! It's the best food in the world, don't you agree?"

# Sentence Tokenization
sentences = sent_tokenize(text)

# Word Tokenization
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w.lower() not in stop_words and w.isalpha()]

# Stemming
ps = PorterStemmer()
stemmed_words = [ps.stem(w) for w in filtered_words]

print(stemmed_words)
```

### spaCy Example

```python
import spacy

nlp = spacy.load("en_core_web_sm")
text = "I love pizza! It's the best food in the world, don't you agree?"

doc = nlp(text)

# Tokens
tokens = [token.text for token in doc]

# Lemmatization + remove stopwords/punctuation
processed_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

print(processed_tokens)
```

---

## Output Example

```
Tokens: ['I', 'love', 'pizza', '!', 'It', "'s", 'the', 'best', 'food', 'in', 'the', 'world', ',', 'do', "n't", 'you', 'agree', '?']
Processed Tokens: ['love', 'pizza', 'good', 'food', 'world', 'agree']
```

---

## References

* [NLTK Documentation](https://www.nltk.org/)
* [spaCy Documentation](https://spacy.io/)

---
 