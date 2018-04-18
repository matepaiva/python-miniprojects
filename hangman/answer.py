class Answer(object):
    def __init__(self, referenceWord, maxNumberOfMistakes):
        self.referenceWord = referenceWord
        self.maxNumberOfMistakes = maxNumberOfMistakes
        self._last = ''
        self.all = []
        self.mistakes = 0
        self.sucesses = 0
        self.win = False
        self.end = False

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        if value:
            self._last = value
            if self._isSingleLetter():
                self.all += [value]
                self._setMistakesAndSuccesses()
            else:
                self.all = list(value)
                self.mistakes = self.maxNumberOfMistakes
                self.win = (value == self.referenceWord)
                self.end = True

    def _isSingleLetter(self):
        return len(self.last) < 2

    def _setMistakesAndSuccesses(self):
        successes = 0
        mistakes = 0
        for letter in self.all:
            occurrence = self.referenceWord.count(letter)
            if (occurrence == 0):
                mistakes += 1
            else:
                successes += occurrence
        self.successes = successes
        self.mistakes = mistakes
        self.win = (successes == len(self.referenceWord))
        self.end = self.win or (mistakes == self.maxNumberOfMistakes)
