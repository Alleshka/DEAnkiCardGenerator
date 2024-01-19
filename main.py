from gtts import gTTS
from hashlib import sha256
from re import sub
import requests
import json

ANKI_CONNECT_URL = "http://localhost:8765"

def normalize_text_to_speech(text: str) -> str:
    text = text.replace("==", "")
    text = text.replace("**", "")
    text = sub(r'\([^)]*\)', '', text)
    text = sub(r'<.*?>', '', text)
    return text

def normalize_text_to_file_name(text: str) -> str:
    text = normalize_text_to_speech(text)
    text = text.strip()
    text = text.replace(".", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace("/", "")
    text = text.replace("\\", "")
    text = text.replace(" ", "_")
    text = text.replace(",", "")

    return text

def calculate_hash(input_string):
    input_bytes = input_string.encode('utf-8')
    sha256_hash = sha256(input_bytes).hexdigest()
    return sha256_hash

def generate_audio_name(text: str, string_hash: str) -> str:
    text = normalize_text_to_file_name(text)
    fileName = f'__ag_{text}_{string_hash}.mp3'
    return fileName

def generate_audio(text: str, string_hash: str) -> str:
    aud = gTTS(text=text, lang='de', slow=False)
    fileName = generate_audio_name(text, string_hash) # f'ag_{string_hash}.mp3'
    filepath = f'C:\\Users\\alles\\AppData\\Roaming\\Anki2\\Alleshka\\collection.media\\{fileName}'
    aud.save(filepath)
    return fileName

def init_card(deck, de, ru, audio, notes):
    notes.append({
        "deckName": deck,
                "modelName": "AGBasicAndReversedWithAudio",
                "fields": {
                    "DE": de,
                    "RU": ru,
                    "Audio": f'[sound:{audio}]'
                },
                "tags": []
    })

def add_anki_card(notes):
    data = {
        "action": "addNotes",
        "version": 6,
        "params": {
            "notes": notes
        }
    }
    response = requests.post(ANKI_CONNECT_URL, json.dumps(data))
    return response.json()

def generate_CSV(pathes):
    notes = []

    for path in pathes:
        with open(f'{path}.csv', "r+", encoding='utf-8') as file:
            
            lines = file.readlines()
            cur = 1
            print(path)

            for line in lines:
                _, de, ru, _ = line.split('|')
                normalizedDe = normalize_text_to_speech(de)
                mp3file = generate_audio(normalizedDe, calculate_hash(line))
                init_card(path, de, ru, mp3file, notes)
                print(f'{de} - {ru} ({cur}/{len(lines)})')
                cur = cur + 1

            file.seek(0)
            file.write('')
            file.truncate()

    add_anki_card(notes)

pathes = ["DE_AllPhrases", "DE_AllVerbs", "DE_AllWords"]
generate_CSV(pathes)
