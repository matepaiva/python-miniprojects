from pydash import deburr

class Word:
    def __init__(self, name, category, level):
        self.name = name.upper()
        self.category = category
        self.level = level

    def getMask(self, answers):
        return ' '.join(self._charMask(char, answers) for char in self.name)

    def appendMaskToLabel(self, mask, label):
        return label.format(mask=mask)

    def _charMask(self, char, answers):
        if (char == ' ' or (deburr(char) in answers)):
            return char
        else:
            return '_'