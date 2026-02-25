import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import matplotlib.pyplot as plt
import os
st.write("Files in directory:", os.listdir())
# --------------------------
# 🎯 Load the trained model
# --------------------------
model = load_model("model/mnist_cnn_model.keras", compile=False)
# --------------------------
# 🖼️ Streamlit UI Setup
# --------------------------
st.set_page_config(page_title="Digit Recognizer", page_icon="🧠", layout="centered")

st.title("🖌️ Handwritten Digit Recognizer")
st.markdown("Draw a digit (0–9) below and click **Predict** to see what the model thinks!")

# Sidebar info
st.sidebar.title("⚙️ Settings")
st.sidebar.write("Use your mouse (or finger on touchscreen) to draw a digit.")
stroke_width = st.sidebar.slider("✏️ Pen thickness", 5, 20, 10)

# --------------------------
# 🎨 Drawing Canvas
# --------------------------
canvas_result = st_canvas(
    fill_color="#000000",
    stroke_width=stroke_width,
    stroke_color="#FFFFFF",
    background_color="#000000",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# --------------------------
# 🔮 Prediction
# --------------------------
if st.button("Predict"):
    if canvas_result.image_data is not None:
        # Preprocess the drawn image
        img = Image.fromarray((canvas_result.image_data[:, :, 0]).astype('uint8'))
        img = img.resize((28, 28)).convert('L')
        img = np.array(img) / 255.0
        img = img.reshape(1, 28, 28, 1)

        # Predict using the model
        prediction = model.predict(img)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.success(f"### 🧠 Predicted Digit: {predicted_class}")
        st.write(f"**Confidence:** {confidence:.2f}%")

        # Show bar chart for all probabilities
        fig, ax = plt.subplots()
        ax.bar(range(10), prediction[0])
        ax.set_xticks(range(10))
        ax.set_xlabel("Digit")
        ax.set_ylabel("Probability")
        ax.set_title("Prediction Confidence")
        st.pyplot(fig)

    else:
        st.warning("Please draw a digit first.")

# --------------------------
# 🧹 Footer
# --------------------------
st.markdown("---")
st.caption("Made with ❤️ by Maroof | CNN + Streamlit")
