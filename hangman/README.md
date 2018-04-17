# Game: command line hangman

## Example of usage
In command line, user will call the game and it will happen as the following example:

```
$ python3 hangman.py
|-
Guess the word: _ _ _ _ _ _  => a
|-
Guess the word: _ _ a _ _ _  => b
|-
Guess the word: b _ a _ _ _  => q
|-o
Guess the word: b _ a _ _ _  => l
|-o
Guess the word: b _ a _ _ l  => w
|-o-
Guess the word: b _ a _ _ l  => x
|-o-/
Guess the word: b _ a _ _ l  => s
|-o-<
Guess the word: b _ a _ _ l  => c
|-o-<-
Guess the word: b _ a _ _ l  => v
|-o-<-<
Guess the word: b _ a _ _ l  => m
|-do-<-< DEAD!
Peh. Game over.
```

## Requirements
- User can input one letter or the entire word.
- If user input one letter, program should verify if word contains letter.
    - If so, program should fill in the letter.
    - If not, user should lose one point and the body is going to be draw
    according to the quantity of lost points
- If user input a word, program should verify if word matches with expected word.
    - If so, user wins.
    - If not, user loses.
- If user lose more than 6 points, user loses the game: `|-do-<-<`.
- If all the letters match, user wins the game.
- In any case, program exits.


## Steps of development
- [ ] Basic implementation with general scenario coverage.
- [ ] Unity tests
- [ ] Fetch words information from database
- [ ] Create webservice to provide that info to be consumed

_(To be completed)_

