from .BaseDeuCardGenerator import BaseDeuCardGenerator
from typing import Dict

class SimpleDeuCardGenerator(BaseDeuCardGenerator):
    def __init__(self, deckName, modelName, separator='|', allowDuplicate=False) -> None:
        super().__init__(deckName, modelName, separator, allowDuplicate)

    def _initFields(self, line: str) -> Dict[str, str]:
        _, de, ru, _ = line.split(self._separator)
        normalizedDe = self._normalize_text_to_speech(de)
        mp3file = self._generate_audio(normalizedDe, self._calculate_hash(line))
        return {
            "DE": de,
            "RU": ru,
            "Audio": f'[sound:{mp3file}]'
        }
        