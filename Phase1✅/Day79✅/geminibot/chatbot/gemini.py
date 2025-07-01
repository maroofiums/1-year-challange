import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyCiHqnBsIisjJXvQm2A9mThcLy_DvyBN4Y")

# Use the correct model name
model = genai.GenerativeModel("gemini-2.0-flash")

# Function to stream and combine Gemini response
def get_gemini_response(prompt):
    response = model.generate_content(prompt, stream=True)
    full_reply = ""
    for chunk in response:
        if chunk.text:
            full_reply += chunk.text
    return full_reply
