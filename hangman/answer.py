from pydash import deburr

class Answer(object):
    def __init__(self, referenceWord, maxNumberOfMistakes):
        self.referenceWord = deburr(referenceWord)
        self.referenceSet = set(self._removeWhiteSpaces(self.referenceWord))
        self.maxNumberOfMistakes = maxNumberOfMistakes
        self._last = ''
        self.guesses = set()
        self.mistakes = 0
        self.win = False
        self.end = False

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        if value:
            self._last = self._normalize(value)
            self.guesses.update(self._removeWhiteSpaces(self._last))
            self._validate()

    def _normalize(self, value):
        return deburr(value.upper())

    def _isSingleLetter(self):
        return len(self.last) < 2

    def _validate(self):
        if (self._isSingleLetter()):
            self.win = not (self.referenceSet - self.guesses)
            self.mistakes = len(self.guesses - self.referenceSet)
            self.end = self.win or (self.mistakes == self.maxNumberOfMistakes)
        else:
            self.win = (self.last == self.referenceWord)
            self.mistakes = self.maxNumberOfMistakes
            self.end = True

    def _removeWhiteSpaces(self, value):
        return value.replace(' ', '')