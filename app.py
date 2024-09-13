import pdfplumber as pdp
from gtts import gTTS

pdf_file = ''

with pdp.open('Tale_of_Python.pdf') as pdf:
    for page in pdf.pages:
        pdf_file += page.extract_text()
        

audio = gTTS(text=pdf_file, lang='en')
audio.save('grade_audio.mp3')