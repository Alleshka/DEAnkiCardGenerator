from DeuAnkiCardGenerator import DeuAnkiCardGenerator
from ENAnkiCardGenerator import ENAnkiCardGenerator
from AnkiCardSaver import AnkiCardSaver

saver = AnkiCardSaver()

de = DeuAnkiCardGenerator()
en = ENAnkiCardGenerator()

notes = [*de.run(), *en.run()]
print(saver.save_anki_cards(notes))