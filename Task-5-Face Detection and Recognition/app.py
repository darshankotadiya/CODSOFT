
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile

# --- Page Configuration ---
st.set_page_config(page_title="AI Face Intelligence | Codsoft Task 5", layout="centered")
st.title("🛡️ AI-Powered Face Detection Hub")
st.markdown("### Developed by: **Darshan Kotadiya** | Full Stack Developer")

def detect_faces(image):
    """Detects faces in an image using Haar Cascade."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Using built-in OpenCV data path to avoid file upload issues
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 8)
    return image, len(faces)

def main():
    uploaded_file = st.file_uploader("Upload Image or Video for Face Analysis...", type=["jpg", "png", "jpeg", "mp4"])

    if uploaded_file is not None:
        file_details = uploaded_file.type.split('/')

        # --- IMAGE PROCESSING ---
        if file_details[0] == 'image':
            img = np.array(Image.open(uploaded_file))
            # Create a copy to keep original clean
            process_img = img.copy()
            result_img, count = detect_faces(process_img)
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("Original Image")
                st.image(uploaded_file, use_column_width=True)
            with col2:
                st.success(f"AI Detected {count} Face(s) ✅")
                st.image(result_img, caption='Detection Output', use_column_width=True)

        # --- VIDEO PROCESSING ---
        elif file_details[0] == 'video':
            st.warning("Analyzing Video Frames... Please wait.")
            tfile = tempfile.NamedTemporaryFile(delete=False)
            tfile.write(uploaded_file.read())
            vf = cv2.VideoCapture(tfile.name)
            
            ret, frame = vf.read()
            if ret:
                # Convert BGR to RGB for Streamlit display
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result_frame, count = detect_faces(frame_rgb)
                st.success(f"Face Detection Complete! ✅")
                st.image(result_frame, caption="Initial Frame Analysis", width=600)
            vf.release()

if __name__ == "__main__":
    main()
