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

    def get_word_index(self, letter):

        spots = []
        for char in self.word:
            if char == letter:
                spots.append(char)
    
    def update(self, idx, letter):
        if letter in self.word:
            self.display[idx] = letter

    def check_guess(self, guess):
        if guess in self.word:
            idx = self.get_word_index(guess)
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
    response = input("want to play a game?")
    while active:
        if response == 'no':
            active = False
        response = input("want to play a game?")
        game()

loop()
