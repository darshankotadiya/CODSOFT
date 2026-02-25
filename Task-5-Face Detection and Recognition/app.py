
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile


st.set_page_config(page_title="AI Face Intelligence | Codsoft", layout="centered")
st.title("🛡️ AI-Powered Face Detection Hub")
st.markdown("### Developed by: **Darshan Kotadiya**")

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 8)
    return image, len(faces)

def main():
    uploaded_file = st.file_uploader("Upload Image or Video...", type=["jpg", "png", "jpeg", "mp4"])

    if uploaded_file is not None:
        file_details = uploaded_file.type.split('/')

        # --- IMAGE PROCESSING ---
        if file_details[0] == 'image':
            img = np.array(Image.open(uploaded_file))
            result_img, count = detect_faces(img)
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("Original")
                st.image(uploaded_file, width=330)
            with col2:
                st.success(f"Detected {count} Face(s) ✅")
                st.image(result_img, caption='AI Output', width=330)

        # --- VIDEO PROCESSING ---
        elif file_details[0] == 'video':
            st.warning("Processing Video Frames... Please wait.")
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            vf = cv2.VideoCapture(tfile.name)
            
            ret, frame = vf.read()
            if ret:
                result_frame, count = detect_faces(frame)
                st.success(f"Face Detected in Video! ✅")
                st.image(result_frame, caption="First Frame Analysis", width=500)
            vf.release()

if __name__ == "__main__":
    main()
