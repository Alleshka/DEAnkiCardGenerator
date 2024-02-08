from BaseAnkiCardGenerator import BaseAnkiCardGenerator
from hashlib import sha256
from gtts import gTTS
from re import sub

class DeuAnkiCardGenerator(BaseAnkiCardGenerator):
    def _readFiles(self, notes: []):
        pathes = ["DE_AllPhrases", "DE_AllVerbs", "DE_AllWords", "DE_TEST"]
        for path in pathes:
            with open(f'.\\DE\\{path}.csv', "r+", encoding='utf-8') as file:            
                lines = file.readlines()
                cur = 1
                print(path)

                for line in lines:
                    _, de, ru, _ = line.split('|')
                    normalizedDe = self.__normalize_text_to_speech(de)
                    mp3file = self.__generate_audio(normalizedDe, self.__calculate_hash(line))
                    self._initCard(path, {
                        "DE": de,
                        "RU": ru,
                        "Audio": f'[sound:{mp3file}]'
                    })
                    print(f'{de} - {ru} ({cur}/{len(lines)})')
                    cur = cur + 1

                file.seek(0)
                file.write('')
                file.truncate()

    def _modelName(self) -> str:
        return 'AGBasicAndReversedWithAudio'

    def __normalize_text_to_speech(self, text: str) -> str:
        text = text.replace("==", "")
        text = text.replace("**", "")
        text = sub(r'\([^)]*\)', '', text)
        text = sub(r'<.*?>', '', text)
        return text

    def __normalize_text_to_file_name(self, text: str) -> str:
        text = self.__normalize_text_to_speech(text)
        text = text.strip()
        text = text.replace(".", "")
        text = text.replace("?", "")
        text = text.replace("!", "")
        text = text.replace("/", "")
        text = text.replace("\\", "")
        text = text.replace(" ", "_")
        text = text.replace(",", "")

        return text
    
    def __calculate_hash(self, input_string):
        input_bytes = input_string.encode('utf-8')
        sha256_hash = sha256(input_bytes).hexdigest()
        return sha256_hash
    
    def __generate_audio_name(self, text: str, string_hash: str) -> str:
        text = self.__normalize_text_to_file_name(text)
        fileName = f'__ag_{text}_{string_hash}.mp3'
        return fileName
    
    def __generate_audio(self, text: str, string_hash: str) -> str:
        aud = gTTS(text=text, lang='de', slow=False)
        fileName = self.__generate_audio_name(text, string_hash) # f'ag_{string_hash}.mp3'
        filepath = f'C:\\Users\\alles\\AppData\\Roaming\\Anki2\\Alleshka\\collection.media\\{fileName}'
        aud.save(filepath)
        return fileName