import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

st.title("Title Example")
st.header("Header Example")
st.subheader("Subheader Example")
st.text("Text Example")
st.write("Write Example")
st.markdown("# Markdown Example")
st.markdown("- Markdown Example")
st.markdown("- Markdown Example")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
submit = st.button("Submit")
if submit:
    st.write(f"Hello, {name}! You are {age} years old.")

col1,col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")

st.sidebar.title("Menu")
options = st.sidebar.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"You selected: {options}")

file = st.file_uploader("Upload a file:")
if file:
    st.write(f"File name: {file.name}")
    st.write(f"File type: {file.type}")
    st.write(f"File size: {file.size} bytes")

st.line_chart([1, 2, 3, 4, 5])
st.bar_chart([1, 2, 3, 4, 5])
