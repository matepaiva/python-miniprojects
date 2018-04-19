#!/usr/bin/env python3

from words import words
from answer import Answer
from constants import DRAWLIST, LABEL, LOSE_MESSAGE, WIN_MESSAGE
from random import choice

def main():
    randomWord = choice(words)
    maxNumberOfMistakes = len(DRAWLIST) - 1
    userAnswer = Answer(randomWord.name, maxNumberOfMistakes)

    while not userAnswer.end:
        print(DRAWLIST[userAnswer.mistakes])
        maskedWord = randomWord.getMask(userAnswer.guesses)
        question = randomWord.appendMaskToLabel(maskedWord, LABEL)
        userAnswer.last = input(question)

    if userAnswer.win:
        print(randomWord.getMask(userAnswer.guesses))
        print(WIN_MESSAGE)
    else:
        print(DRAWLIST[userAnswer.mistakes])
        print(LOSE_MESSAGE)

if __name__ == "__main__":
    # execute only if run as a script
    main()