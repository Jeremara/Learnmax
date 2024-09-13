# LearnMax: PDF to Audio Converter

**LearnMax** is a simple web-based tool that allows users to upload a PDF file, extract the text from it, and convert the text into an audio file. The application supports multiple languages (English, French, Spanish, Arabic) for audio output and is built using Streamlit, PDFPlumber, and Google Text-to-Speech (gTTS) libraries.

## Features

- **PDF Upload**: Users can upload a PDF file, and the tool will extract readable text from the document.
- **Multiple Languages**: Users can choose from four different languages for the audio conversion:
  - English
  - French
  - Spanish
  - Arabic
- **Audio File Generation**: The extracted text is converted into an audio file using the selected language.
- **Download Audio**: After the audio file is generated, the user can download the `.mp3` file directly.

## Requirements

To run this project, you'll need the following dependencies:

- Python 3.8 or higher
- Streamlit
- PDFPlumber
- Google Text-to-Speech (gTTS) or pyttsx3 (for offline mode)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/learnmax-pdf-to-audio.git
    cd learnmax-pdf-to-audio
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Dependencies

- `streamlit`: For building the web-based user interface.
- `pdfplumber`: For extracting text from PDF files.
- `gTTS`: For converting text to audio (online, requires internet connection).
- `pyttsx3`: (Optional) For offline text-to-speech functionality.

Install the dependencies using the `requirements.txt`:

```bash
streamlit==1.0.0
pdfplumber==0.5.28
gtts==2.2.3
pyttsx3==2.90  # Optional, for offline text-to-speech
