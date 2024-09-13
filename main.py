import streamlit as st
import pdfplumber as pdp
from gtts import gTTS
import os

# Display the image as the title
st.image("LearnMax.png", caption=None, use_column_width=True)

# Mapping of language options for gTTS
language_options = {
    'English': 'en',
    'French': 'fr',
    'Spanish': 'es',
    'Arabic': 'ar'
}

# Language selection
language = st.selectbox("Select language for audio", list(language_options.keys()))

# File uploader with PDF check
uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])

if uploaded_file is not None:
    
    if uploaded_file.type == "application/pdf":
        with st.spinner('Generating audio file...'):
            # Extract text from PDF
            pdf_file = ''
            with pdp.open(uploaded_file) as pdf:
                for page in pdf.pages:
                    pdf_file += page.extract_text()

            # Convert extracted text to speech
            if pdf_file.strip():
                # Use selected language for audio conversion
                audio = gTTS(text=pdf_file, lang=language_options[language])
                audio.save('generated_audio.mp3')
                st.success(f"Audio file has been generated in {language}!")

                # Provide a download link for the audio file
                with open('generated_audio.mp3', 'rb') as audio_file:
                    st.download_button('Download audio', audio_file, 'audio.mp3')

            else:
                st.error("The PDF appears to be empty, or contains no readable text.")
    else:
        st.error("Invalid file format. Please upload a PDF file.")
else:
    st.info("Please upload a PDF file to begin.")
