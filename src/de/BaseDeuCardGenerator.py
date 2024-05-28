from hashlib import sha256
from gtts import gTTS
from re import sub
from ..BaseCardGenerator import BaseCardGenerator


class BaseDeuCardGenerator(BaseCardGenerator):
    def __init__(self, deckName, modelName, separator='|', allowDuplicate=False) -> None:
        super().__init__(deckName, modelName, separator, allowDuplicate)

    def _normalize_text_to_speech(self, text: str) -> str:
        text = text.replace("==", "")
        text = text.replace("**", "")
        text = sub(r'\([^)]*\)', '', text)
        text = sub(r'<.*?>', '', text)
        return text
    
    def _normalize_text_to_file_name(self, text: str) -> str:
        text = self._normalize_text_to_speech(text)
        text = text.strip()
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("/", "")
        text = text.replace("\\", "")
        text = text.replace(" ", "_")
        text = text.replace(",", "")
        return text
    
    def _calculate_hash(self, input_string):
        input_bytes = input_string.encode('utf-8')
        sha256_hash = sha256(input_bytes).hexdigest()
        return sha256_hash
    
    def _generate_audio_name(self, text: str, string_hash: str) -> str:
        text = self._normalize_text_to_file_name(text)
        fileName = f'__ag_{text}_{string_hash}.mp3'
        return fileName
    
    def _generate_audio(self, text: str, string_hash: str) -> str:
        aud = gTTS(text=text, lang='de', slow=False)
        fileName = self._generate_audio_name(text, string_hash) # f'ag_{string_hash}.mp3'
        filepath = f'C:\\Users\\alles\\AppData\\Roaming\\Anki2\\Alleshka\\collection.media\\{fileName}'
        aud.save(filepath)
        return fileName