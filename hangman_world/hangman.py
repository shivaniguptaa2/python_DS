import random
from word_list import words_lib
from hangman_art import Stages, logo

word = random.choice(words_lib)
gameover = False
display = "_"*len(word)
live_stage = 6
guessed_word = []

print(logo)
print("Welcome to Hangman's World!!")
print(display)
print(word)

while gameover is not True:
  guess = input('Guess the letter: \n').lower()

  # Check if guessed letter is in the word
  if guess in word:
    print('You guessed it correct')
    guessed_word.append(guess)

      # Update the display word with the guessed letter
    for i in range(len(word)):
      if word[i] == guess:
        display = display[:i] + guess + display[i+1:]

    print(display)
    print(Stages[live_stage])

        # Check if the whole word has been guessed
    if '_' not in display:
      gameover = True
      print('********* You Won ***********')

  # Check if the guessed letter was already guessed (correct or incorrect)
  elif guess in guessed_word:
    print('You already guessed this letter')

  # Handle new incorrect guesses
  else:
    live_stage -= 1
    print(Stages[live_stage])
    print(f'*************** You have {live_stage} more chances ***************')

      # End the game if lives are exhausted
    if live_stage == 0:
      gameover = True
      print(f'*********** It was "{word}". You Lose ***********')

# while gameover is not True:
#   guess = input('Guess the letter: \n').lower()

#   if guess in word:
#     print('You guessed it correct')
#     gussed_word.append(guess)

#     for i in range(len(word)):
#         if word[i] == guess:
#             display = display[:i] + guess + display[i+1:]

#     print(display)
#     print(Stages[live_stage])

#     if '_' not in display:
#         gameover = True
#         print('********* You Won ***********')
#   elif guess in gussed_word:
#     print('You already guessed this letter')
#   else:
#     live_stage -= 1
#     print(Stages[live_stage])
#     print(f'*************** You have {live_stage} more chances ***************')

#     if live_stage == 0:
#       gameover = True
#       print(f'*********** It was "{word}". You Lose ***********')





# while gameover is not True:
#     guess = input('Guess the letter: \n')
#     if guess in word:
#         print('You gussed it correct')
#         correct_word.append(guess)
#         for i in range(len(word)):
#             if word[i] == guess.lower():
#                 display = display[0:i]+guess+display[i+1:]
#             print(display)
#             print(Stages[live_stage])
#             if '_' not in display:
#                 gameover = True
#                 print('*********You Won***********')
#     else:
#           if guess in correct_word:
#                print('You already guessed this word')
#           else:
#             live_stage-=1
#             print(Stages[live_stage])
#             print(f'*************** You have {live_stage} more**********')
#           if live_stage==0:
#             gameover = True
#             print(f'***********It was {word}.You Lose****************')





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


