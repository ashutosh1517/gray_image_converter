import streamlit as st
from PIL import Image
import io

st.title("Colour Image to Grayscale Converter")

# upload the file
uploaded_file = st.file_uploader("Upload an image (File Type: JPG, PNG, JPEG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # OPening the image
    original_image = Image.open(uploaded_file)

    # converting to grayscale
    gray_image = original_image.convert("L")

    # showing the original and the grayscale images side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Image")
        st.image(original_image, use_container_width=True)
    with col2:
        st.header("Grayscale Image")
        st.image(gray_image, use_container_width=True)

    # download button for grayscale image
    buffer = io.BytesIO()
    gray_image.save(buffer, format="PNG")
    st.download_button(
        label="Download Grayscale Image",
        data=buffer.getvalue(),
        file_name="grayscale.png",
        mime="image/png"
    )
