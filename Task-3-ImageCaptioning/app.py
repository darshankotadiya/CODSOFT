import streamlit as st
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from gtts import gTTS
import os
import warnings

# Optimization: Cleaning UI logs
warnings.filterwarnings("ignore")

class VisionIntelEngine:
    def __init__(self):
        self.model_id = "Salesforce/blip-image-captioning-base"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
    
    @st.cache_resource
    def load_resources(_self):
        processor = BlipProcessor.from_pretrained(_self.model_id)
        model = BlipForConditionalGeneration.from_pretrained(_self.model_id).to(_self.device)
        return processor, model

    def generate_insight(self, image):
        processor, model = self.load_resources()
        inputs = processor(image, return_tensors="pt").to(self.device)
        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=50)
        return processor.decode(output[0], skip_special_tokens=True)

    def text_to_speech(self, text):
        """Generates audio for the caption."""
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        return "output.mp3"

def main():
    st.set_page_config(page_title="Visual Intelligence | CodSoft", layout="wide")
    st.title("👁️ AI-Powered Visual Intelligence")
    st.markdown("---")
    
    engine = VisionIntelEngine()
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📷 Input Source")
        file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        if file:
            img = Image.open(file).convert('RGB')
            st.image(img, use_container_width=True)

    with col2:
        st.subheader("🤖 AI Insights")
        if file and st.button("Generate Descriptive Caption"):
            with st.spinner("Analyzing pixels..."):
                caption = engine.generate_insight(img)
                st.info(f"**Description:** {caption.capitalize()}")
                
                # --- Audio Implementation ---
                audio_path = engine.text_to_speech(caption)
                audio_file = open(audio_path, "rb")
                st.audio(audio_file.read(), format="audio/mp3")
                st.success("Analysis and Audio Synthesis Complete.")

if __name__ == "__main__":
    main()