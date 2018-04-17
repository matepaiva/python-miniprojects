def isSingleLetter(word):
    return len(word) < 2


def labelWithHiddenWord(label, word, answers):
    return label.format(hiddenWord=getHiddenWord(word, answers))


def getHiddenWord(word, answers):
    hiddenWord = ''
    for letter in word:
        hiddenWord += (letter + ' ') if answers.count(letter) else '_ '
    return hiddenWord


def getMistakesAndSuccesses(word, answers):
    successes = 0
    mistakes = 0
    for letter in answers:
        occurrence = word.count(letter)
        if (occurrence == 0):
            mistakes += 1
        else:
            successes += occurrence
    return {
        'successes': successes,
        'mistakes': mistakes
    }


def isCorrectAnswer(word, success):
    return len(word) == success


word = 'brazil'
success = False
label = 'Guess the word: {hiddenWord} => '
successes = 0
mistakes = 0
answers = []
hangmanDraw = [
    '|-',
    '|-o',
    '|-o-',
    '|-o-/',
    '|-o-<',
    '|-o-<-',
    '|-o-<-<',
    '|-do-<-< DEAD!'
]

while ((not success) and mistakes < (len(hangmanDraw) - 1)):
    print(hangmanDraw[mistakes])
    answer = input(labelWithHiddenWord(label, word, answers))
    if answer:
        if isSingleLetter(answer):
            answers = answers + [answer]
            mistakesAndSuccess = getMistakesAndSuccesses(word, answers)
            mistakes = mistakesAndSuccess['mistakes']
            successes = mistakesAndSuccess['successes']
            success = successes == len(word)
        else:
            answers = list(answer)
            mistakes = len(hangmanDraw)
            success = answer == word

if success:
    print(getHiddenWord(word, answers))
    print('Success!')
else:
    print(hangmanDraw[mistakes])
    print('Peh. Game over.')
