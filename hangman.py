import random

Stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',r'''
  +---+
  |   |
      |
      |
      |
      |
=========''',]

words_lib = ['apple','bathroom','court','donkey','elevator','fridge','garden','henry','inkpot','jungle']
word = random.choice(words_lib)
gameover = False
display = "_"*len(word)
live_stage = 6

print("Welcome to Hangman's World!!")
# print(word)
print(display)

while gameover is not True:
    guess = input('Guess the letter: \n')
    if guess in word:
        print('You gussed it correct')
        for i in range(len(word)):
            if word[i] == guess.lower():
                display = display[0:i]+guess+display[i+1:]
                print(display)
                print(Stages[live_stage])
            
            if '_' not in display:
                gameover = True
                print('You Won')
    else:
        live_stage-=1
        print(Stages[live_stage])
        if live_stage==0:
            gameover = True
            print('You Lose')








# while gameover!= 'True':
#     guess_letter = input("Guess the letter :")
#     for i in range(len(word)):
#         if word[i] == guess_letter.lower():
#             display = display[0:i]+guess_letter+display[i+1:]
#             print(display)
#             print(Stages[n])
#         else:
#             n-=1
#             print(Stages[n])
#         if n==0:
#             gameover=='True'
# print("You won!")






# while display.lower()!=word.lower() :
#     guess_letter = input("Guess the letter :")
#     for i in range(len(word)):
#         if word[i] == guess_letter.lower():
#             display = display[0:i]+guess_letter+display[i+1:]
#             print(display)
#     if guess_letter not in word:
#         lives+=1    
# print("You won!")



# for i in range(len(word)):
#     print('_',end=" ")

# guess = input("Guess a letter: \n").lower()
# for letter in word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


