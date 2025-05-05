import random
logo = r'''
     
    >>>>>----------------------->

    <<<<<-----------------------<
     
'''

top_bollywood_movies = {
    "Dangal": 2000,
    "Jawan": 1150,
    "Pathaan": 1050,
    "Animal": 910,
    "Bajrangi Bhaijaan": 920,
    "Stree 2": 860,
    "Secret Superstar": 900,
    "Chhaava": 795,
    "PK": 760,
    "Gadar 2": 690,
    "Sultan": 620,
    "Sanju": 580,
    "Tiger Zinda Hai": 565,
    "Padmaavat": 570,
    "Dhoom 3": 557,
    "War": 475,
    "Dunki": 471,
    "Tiger 3": 467,
    "Andhadhun": 450,
    "Brahmāstra: Part One – Shiva": 425,
    "Chennai Express": 410,
    "Bhool Bhulaiyaa 3": 400,
    "3 Idiots": 400,
    "Simmba": 400,
    "Kabir Singh": 375
}

score = 0
is_game_over = False

print('Welcome to the Game world')

def compare_amt(choice, amount):
    global score, is_game_over  # Fix variable scoping
    if choice[1] == amount:
        print('Correct Answer')
        score += 1
    else:
        print('Incorrect Answer')
        print(f'Your final score is: {score}')
        is_game_over = True
    

while not is_game_over:
    choice_1 = random.choice(list(top_bollywood_movies.items()))
    choice_2 = random.choice(list(top_bollywood_movies.items()))
    while choice_1 == choice_2:  # Ensure choices are not the same
        choice_2 = random.choice(list(top_bollywood_movies.items()))
    amount = max(choice_1[1], choice_2[1])  # Simplify logic for determining the larger amount
    print(f'Whose Box office collection is bigger?')
    print(f'A. {choice_1[0]}')
    print('Vs')
    print(f'B. {choice_2[0]}')
    choice = input('Choose A or B: ').strip().lower()
    if choice == 'a':
        compare_amt(choice_1, amount)
    elif choice == 'b':
        compare_amt(choice_2, amount)
    else:
        print('Invalid choice. Please choose A or B.')
    print('Box office Collection:')
    print(f'{choice_1[0]} made {choice_1[1]}')
    print(f'{choice_2[0]} made {choice_2[1]}')
    print(logo)