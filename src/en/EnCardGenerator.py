from typing import Dict, List
from ..BaseCardGenerator import BaseCardGenerator

class EnCardGenerator(BaseCardGenerator):
    def __init__(self, deckName, modelName, separator='|', allowDuplicate=False) -> None:
        super().__init__(deckName, modelName, separator, allowDuplicate)

    def _initFields(self, line: str) -> Dict[str, str]:
         _, en, definition, example, ru , img, _ = line.lower().split(self._separator)
         
         img = img.strip()
         en = en.strip()
         definition = definition.strip()
         ru = ru.strip()

         replace_to = '_' * len(en)
         examples = f'<ul>{"".join([f"<li>{i.strip().replace(en, replace_to)}</li>" for i in example.split(";")])}</ul>' 

         return { 
             "EN": en, 
             "Definition": definition, 
             "Translation": ru, 
             "Example": examples, 
             "Img": img }