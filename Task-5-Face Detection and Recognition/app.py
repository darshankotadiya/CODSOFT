import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
import os

# --- Page Configuration ---
st.set_page_config(page_title="AI Face Intelligence | Codsoft", layout="centered")
st.title("🛡️ AI-Powered Face Detection Hub")
st.markdown("### Developed by: **Darshan Kotadiya**")

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Professional path handling for Streamlit Cloud
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 8)
    return image, len(faces)

def main():
    uploaded_file = st.file_uploader("Upload Image or Video...", type=["jpg", "png", "jpeg", "mp4"])

    if uploaded_file is not None:
        file_details = uploaded_file.type.split('/')

        if file_details[0] == 'image':
            img = np.array(Image.open(uploaded_file))
            # Convert RGB (PIL) to BGR (OpenCV)
            img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            result_bgr, count = detect_faces(img_bgr)
            # Convert back to RGB for Streamlit
            result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("Original")
                st.image(uploaded_file, use_column_width=True)
            with col2:
                st.success(f"Detected {count} Face(s) ✅")
                st.image(result_rgb, caption='AI Output', use_column_width=True)

        elif file_details[0] == 'video':
            st.warning("Analyzing first frame...")
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            vf = cv2.VideoCapture(tfile.name)
            ret, frame = vf.read()
            if ret:
                result_frame, count = detect_faces(frame)
                result_rgb = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
                st.image(result_rgb, caption="First Frame Analysis", width=500)
            vf.release()

if __name__ == "__main__":
    main()
