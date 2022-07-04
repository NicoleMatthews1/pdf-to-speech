import requests
import shutil
import fitz # install using: pip install PyMuPDF

with fitz.open("sample.pdf") as pdf_file:
    text = ""
    for page in pdf_file:
        text += page.get_text()

print(text)


API_KEY = "YOUR API KEY"
tts_endpoint = "http://api.voicerss.org/"

parameters = {
    "key": API_KEY,
    "hl": "en-us",
    "src": text,
    "c": "MP3"
}
headers = {
    'content-type': 'audio/wav'
}


local_filename = "download.mp3"
with requests.get(tts_endpoint, params=parameters, stream=True) as r:
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
