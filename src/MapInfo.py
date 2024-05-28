from .BaseCardGenerator import BaseCardGenerator

class MapInfo:
    def __init__(self, filePath: str, generator: BaseCardGenerator) -> None:
        self.filePath = filePath
        self.generator = generator