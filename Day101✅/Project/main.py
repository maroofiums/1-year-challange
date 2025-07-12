import pandas as pd
import string
import nltk
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()



nltk.download('punkt')
nltk.download('stopwords')

data = {
    'label': ['ham', 'spam', 'ham', 'spam', 'ham'],
    'text': [
        "Hey, are we still meeting today?",
        "WINNER!! Claim your prize now by clicking this link!",
        "I'm running late. Be there soon.",
        "You’ve won a free vacation. Call now!",
        "Let’s catch up sometime next week."
    ]
}

df = pd.DataFrame(data)

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = tokenizer.tokenize(text)  # 🔁 Replaces nltk.word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    return " ".join(tokens)

df['clean_text'] = df['text'].apply(preprocess)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['clean_text'])

y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

def predict_message(msg):
    cleaned = preprocess(msg)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)
    return prediction[0]

custom_text = input("Enter The email to test spam or not.\nMail:")
print("\n🔮 Custom Prediction:", predict_message(custom_text))
