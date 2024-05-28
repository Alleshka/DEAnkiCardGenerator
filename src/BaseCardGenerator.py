from abc import ABC, abstractmethod 
from typing import List, Dict

class BaseCardGenerator(ABC):
    def __init__(self, deckName, modelName, separator = '|', allowDuplicate = False) -> None:
        self._deckName = deckName
        self._modelName = modelName
        self._allowDuplicate = allowDuplicate
        self._separator = separator

    def createCards(self, lines: List[str]) -> List[Dict[str, any]]:
        cards = [self._initCard(line) for line in lines]
        return cards
    
    def _initCard(self, line: str) -> List[Dict[str, any]]:
        fields = self._initFields(line)
        return {
            "deckName": self._deckName,
                    "modelName": self._modelName,
                    "fields": fields,
                    "tags": [],
                    "options": {
                        "allowDuplicate": self._allowDuplicate,
                    }
        }
      
    @abstractmethod
    def _initFields(self, line: str) -> Dict[str, str]:
        pass