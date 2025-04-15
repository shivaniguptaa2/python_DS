import random
from word_list import words_lib
from hangman_art import Stages, logo

word = random.choice(words_lib)
gameover = False
display = "_" * len(word)
live_stage = 6
guessed_word = []

print(logo)
print("Welcome to Hangman's World!!")
print(display)

while not gameover:
    guess = input('Guess the letter: \n').lower()

    if guess in guessed_word:
        print('You already guessed this letter. Try a different one.')
        continue

    guessed_word.append(guess)

    if guess in word:
        print('You guessed it correct')

        for i in range(len(word)):
            if word[i] == guess:
                display = display[:i] + guess + display[i+1:]

        print(display)
        print(Stages[live_stage])

        if '_' not in display:
            gameover = True
            print('********* You Won ***********')

    else:
        live_stage -= 1
        print(Stages[live_stage])
        print(f'*************** You have {live_stage} more chances ***************')

        if live_stage == 0:
            gameover = True
            print(f'*********** It was "{word}". You Lose ***********')


