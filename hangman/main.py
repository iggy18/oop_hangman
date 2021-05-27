import random
from words import words


class Go:

    def __init__(self):
        self.word = random.choice(words)
        self.display = ["_" for letter in self.word]
        self.guesses = 0

    def show(self):
        display = ' '.join(self.display)
        print(f' the word is, {display}')

    def get_word_index(self, guess):
        spots = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                spots.append(index)
        print('spots:', spots)
        return(spots)

    def update(self, idx, letter):
        for number in idx:
            self.display[number] = letter

    def check_guess(self, guess):
        if guess in self.word:
            idx = self.get_word_index(guess)
            print('check guess:', idx)
            self.update(idx, guess)

    def check_for_win(self):
        display = ''.join(self.display)
        word = self.word
        if display == word:
            print('you win!')
            return True


def game():
    active = True
    word = Go()
    while active:
        guess = input("guess a letter\n>>> ")
        word.check_guess(guess)
        word.show()
        word.guesses += 1
        if word.check_for_win():
            print(f'you won in {word.guesses} guesses.')
            active = False


def loop():
    active = True
    while active:
        response = input("want to play a game?")
        if response == 'no':
            active = False
        game()

loop()
