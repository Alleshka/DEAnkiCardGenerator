from BaseAnkiCardGenerator import BaseAnkiCardGenerator

class ENAnkiCardGenerator(BaseAnkiCardGenerator):
    def _readFiles(self):
        pathes = ["EN_MyWords", "EN_SkyengWords"]
        for path in pathes:
            with open(f'.\\EN\\{path}.csv', "r+", encoding='utf-8') as file:            
                lines = file.readlines()
                for line in lines:
                    _, en, definition, example, ru , img, _ = line.split('|')

                    img = img.strip()
                    en = en.strip()
                    definition = definition.strip()
                    ru = ru.strip()

                    replace_to = '_' * len(en)
                    examples = f'<ul>{"".join([f"<li>{i.strip().replace(en, replace_to)}</li>" for i in example.split(";")])}</ul>'

                    self._initCard(path, {
                        "EN": en,
                        "Definition": definition,
                        "Translation": ru,
                        "Example": examples,
                        "Img": img
                    })

                file.seek(0)
                file.write('')
                file.truncate()

    def _modelName(self) -> str:
        return 'AGEnglishWordsWithExamples'

