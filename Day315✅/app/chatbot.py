from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

# FLAN-T5 is text2text
generator = pipeline("text2text-generation", model=MODEL_NAME)

def ask_bot(prompt: str) -> str:
    try:
        result = generator(prompt, max_new_tokens=128)
        return result[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"
