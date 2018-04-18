
class Word:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level

    def getMask(self, answers):
        return ' '.join(letter if (letter in answers) else '_' for letter in self.name)

    def appendMaskToLabel(self, mask, label):
        return label.format(mask=mask)
