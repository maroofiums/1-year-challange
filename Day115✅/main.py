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
