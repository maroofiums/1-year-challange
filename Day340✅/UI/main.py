import streamlit as st
from transformers import pipeline

st.title("Fake News Detector")
st.write("Paste any news text below to check if it's REAL or FAKE.")

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="hamzab/roberta-fake-news-classification"
    )

detector = load_model()

user_input = st.text_area("Enter News Text Here:", height=150)

if st.button("Check News"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        result = detector(user_input)
        # Map TRUE → REAL
        label = result[0]['label']
        if label.upper() == "TRUE":
            label = "REAL"
        score = result[0]['score']
        st.success(f"Prediction: {label} ({score:.2f})")