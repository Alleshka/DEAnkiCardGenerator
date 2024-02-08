from DeuAnkiCardGenerator import DeuAnkiCardGenerator
from AnkiCardSaver import AnkiCardSaver

saver = AnkiCardSaver()
de = DeuAnkiCardGenerator(saver)
de.run()