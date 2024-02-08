from AnkiCardSaver import AnkiCardSaver
from abc import ABC, abstractmethod 

class BaseAnkiCardGenerator(ABC):
    def __init__(self) -> None:
        pass

    def run(self) -> []:
        self.__notes = []
        self._readFiles()
        return self.__notes

    @abstractmethod
    def _readFiles(self):
        pass

    @abstractmethod
    def _modelName(self) -> str:
        pass

    def _initCard(self, deckName: str, fields: any):
        self.__notes.append({
            "deckName": deckName,
                    "modelName": self._modelName(),
                    "fields": fields,
                    "tags": [],
                    "options": {
                        "allowDuplicate": True,
                    }
        })