from json import dumps
from requests import post

class AnkiCardSaver:
    def __init__(self) -> None:
        self.__ANKI_CONNECT_URL = "http://localhost:8765"

    def save_anki_cards(self, cards):
        data = {
            "action": "addNotes",
            "version": 6,
            "params": {
                "notes": cards
            }
        }
        response = post(self.__ANKI_CONNECT_URL, dumps(data))
        return response.json()