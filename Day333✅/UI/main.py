import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL")

st.title("URL Shortener (FastAPI + TinyURL)")

url_input = st.text_input("Enter URL to shorten:")

if st.button("Shorten URL"):
    if url_input:
        try:
            response = requests.post(BACKEND_URL, json={"url": url_input})
            if response.status_code == 200:
                data = response.json()
                st.success("URL shortened successfully!")
                st.write("Original URL:", data["original_url"])
                st.write("Short URL:", data["short_url"])
                st.markdown(f"[Open Short URL]({data['short_url']})")
            else:
                st.error(f"Error: {response.json().get('detail')}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
    else:
        st.warning("Please enter a URL to shorten.")