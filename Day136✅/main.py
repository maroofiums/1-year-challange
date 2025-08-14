# Full Text Processing & Tokenization Example in Python

import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

# Example raw text
text = "Hello world! NLP is amazing. I'm learning how to process text with Python, and it's fun."

# -----------------------------
# 1. Lowercase text
text = text.lower()

# -----------------------------
# 2. Remove punctuation
text_no_punct = text.translate(str.maketrans('', '', string.punctuation))

# -----------------------------
# 3. Remove numbers
text_no_numbers = re.sub(r'\d+', '', text_no_punct)

# -----------------------------
# 4. Remove extra whitespace
text_clean = re.sub(r'\s+', ' ', text_no_numbers).strip()

print("Cleaned Text:")
print(text_clean)
print("\n")

# -----------------------------
# 5. Tokenization

# Word Tokenization
word_tokens = word_tokenize(text_clean)
print("Word Tokens:")
print(word_tokens)
print("\n")

# Sentence Tokenization
sent_tokens = sent_tokenize(text)
print("Sentence Tokens:")
print(sent_tokens)
print("\n")

# -----------------------------
# 6. Remove stopwords
stop_words = set(stopwords.words('english'))
words_no_stopwords = [w for w in word_tokens if w not in stop_words]
print("Words without Stopwords:")
print(words_no_stopwords)
print("\n")

# -----------------------------
# 7. Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(w) for w in words_no_stopwords]
print("Stemmed Words:")
print(stemmed_words)
print("\n")

# -----------------------------
# 8. Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(w, pos='v') for w in words_no_stopwords]  # 'v' for verb
print("Lemmatized Words:")
print(lemmatized_words)
print("\n")

# -----------------------------
# Summary
print("Original Text:")
print(text)
print("\nCleaned Text for NLP Processing:")
print(text_clean)
