import random

num = random.randint(1,100)

def guessing_game(n):
    if n>num:
        print('Too High')
    elif n<num:
        print('Too Low')
    else:
        print('You guessed it correct')
        exit()

print('Welcome to the Guessing Number Game')
dif_lvl = input('Choose the difficulty level. Type "Easy" or "Hard"\n')

if dif_lvl.lower() == 'easy':
    for i in range(10,0,-1):
        print(f'You have {i} chances remaining')
        n = int(input('Guess the Number: '))
        guessing_game(n)
elif dif_lvl.lower() == 'hard':
    for i in range(5,0,-1):
        print(f'You have {i} chances remaining')
        n = int(input('Guess the Number: '))
        guessing_game(n)
else:
    print('Invalid Input')
    
