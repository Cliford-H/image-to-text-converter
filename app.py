import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

# Set the Tesseract OCR path (Update if installed in a different location)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Streamlit App Title
st.title("🖼️ AI-Powered Diagram to Text Converter")

st.write("Upload an image containing a **2D drawing or diagram**, and this tool will extract any readable text.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert image to OpenCV format
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)  # Convert to grayscale

    # Apply thresholding to improve text detection
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Perform OCR (Extract Text)
    extracted_text = pytesseract.image_to_string(gray)

    # Display extracted text
    st.subheader("📄 Extracted Text:")
    if extracted_text.strip():
        st.text_area("Detected Text", extracted_text, height=200)
    else:
        st.warning("⚠️ No text detected. Try another image!")

    # Optional: Save extracted text to a file
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    st.download_button("⬇ Download Extracted Text", "extracted_text.txt", "text/plain")

