from typing import Dict
from src.AnkiCardSaver import AnkiCardSaver
from src.de.SimpleDeuCardGenerator import SimpleDeuCardGenerator
from src.en.EnCardGenerator import EnCardGenerator
from src.MapInfo import MapInfo
from os import path

mapped: Dict[str, MapInfo] = {
    "DE_AllWords": MapInfo('data\DE\DE_AllWords.csv', SimpleDeuCardGenerator("DE_AllWords", "AGBasicAndReversedWithAudio", '|', False)),
    "DE_AllPhrases": MapInfo('data\DE\DE_AllPhrases.csv', SimpleDeuCardGenerator("DE_AllPhrases", "AGBasicAndReversedWithAudio", '|', False)),
    "EN_AllMyWords": MapInfo('data\EN\EN_AllMyWords.csv', EnCardGenerator("EN_AllMyWords", "AGEnglishWordsWithExamples", "|", False)),
    "EN_SkyengWords": MapInfo('data\EN\EN_SkyengWords.csv', EnCardGenerator("EN_SkyengWords", "AGEnglishWordsWithExamples", "|", False))
}

saver = AnkiCardSaver()

cards = []
for k, info in mapped.items():
    path = info.filePath
    print(f'File {info.filePath} start')
    with open(path, "r+", encoding='utf-8') as file:
        lines = file.readlines()
        cards.extend(info.generator.createCards(lines))
    print(f'File {info.filePath} end')
    print(f'=========================')

res = saver.save_anki_cards(cards)

## Clear file if no errors
if (res['error'] is None):
    print(res)
    for k, info in mapped.items():
        path = info.filePath
        with open(path, "r+", encoding='utf-8') as file:
            file.seek(0)
            file.write('')
            file.truncate()
else:
    print(res['error'])