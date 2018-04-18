class Word:
    def __init__(self, name, category, level):
        self.name = name
        self.category = category
        self.level = level

    def getMask(self, answers):
        mask = ''
        for letter in self.name:
            mask += (letter + ' ') if letter in answers else '_ '
        return mask

    def appendMaskToLabel(self, mask, label):
        return label.format(mask=mask)