# Audio_to_text

Audio-to-PDF is a utility program to convert speech in English language into text in the PDF format.

## Run locally

```sh
git clone https://github.com/Cheesecake-mafia/Audio_to_text.git
# or clone your own fork

cd Audio_to_text

pip install PyPDF2 gtts pyttsx3

```

<br />
Call function tts from Audiobook.py or Audiobook.ipynb. Pass parameters filepath(str) and speak(Boolean). 

```py
from Audiobook import tts
tts("filepath", speak=False)

```
