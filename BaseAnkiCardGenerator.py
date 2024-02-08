from AnkiCardSaver import AnkiCardSaver
from abc import ABC, abstractmethod 

class BaseAnkiCardGenerator(ABC):
    def __init__(self, saver: AnkiCardSaver) -> None:
        self.__cardSaver = saver

    def run(self):
        self.__notes = []
        self._readFiles(self.__notes)
        self.__cardSaver.save_anki_cards(self.__notes)

    @abstractmethod
    def _readFiles(self, notes: []):
        pass

    @abstractmethod
    def _modelName(self) -> str:
        pass

    def _initCard(self, deckName: str, fields: any):
        self.__notes.append({
            "deckName": deckName,
                    "modelName": self._modelName(),
                    "fields": fields,
                    "tags": []
        })