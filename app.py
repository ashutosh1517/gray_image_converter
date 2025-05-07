import streamlit as st
from PIL import Image
import io

st.title("Image to Grayscale Converter")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open the uploaded image
    original_image = Image.open(uploaded_file)

    # Convert to grayscale
    gray_image = original_image.convert("L")

    # Display original and grayscale images side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Image")
        st.image(original_image, use_column_width=True)
    with col2:
        st.header("Grayscale Image")
        st.image(gray_image, use_column_width=True)

    # Provide a download button for grayscale image
    buffer = io.BytesIO()
    gray_image.save(buffer, format="PNG")
    st.download_button(
        label="Download Grayscale Image",
        data=buffer.getvalue(),
        file_name="grayscale.png",
        mime="image/png"
    )
