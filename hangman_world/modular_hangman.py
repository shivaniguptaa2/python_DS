import random
from word_list import words_lib
from hangman_art import Stages, logo

class HangmanGame:
    def __init__(self):
        self.word = random.choice(words_lib)
        self.display = "_" * len(self.word)
        self.live_stage = 6
        self.guessed_word = []
        self.gameover = False

    def print_intro(self):
        print(logo)
        print("Welcome to Hangman's World!!")
        print(self.display)
        print(self.word)  # For debugging purposes, remove in production

    def get_guess(self):
        return input('Guess the letter: \n').lower()

    def process_guess(self, guess):
        if guess in self.guessed_word:
            print('You already guessed this letter. Try a different one.')
            return

        self.guessed_word.append(guess)

        if guess in self.word:
            print('You guessed it correct')
            self.update_display(guess)
        else:
            self.live_stage -= 1
            print(Stages[self.live_stage])
            print(f'*************** You have {self.live_stage} more chances ***************')

    def update_display(self, guess):
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.display = self.display[:i] + guess + self.display[i+1:]
        print(self.display)
        print(Stages[self.live_stage])

    def check_game_status(self):
        if '_' not in self.display:
            self.gameover = True
            print('********* You Won ***********')
        elif self.live_stage == 0:
            self.gameover = True
            print(f'*********** It was "{self.word}". You Lose ***********')

    def play(self):
        self.print_intro()
        while not self.gameover:
            guess = self.get_guess()
            self.process_guess(guess)
            self.check_game_status()

# Run the game
if __name__ == "__main__":
    game = HangmanGame()
    game.play()
