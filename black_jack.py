import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # J=10, Q=10, K=10
logo = r"""
    //   ) )                                       / /                         
   //___/ /  //  ___      ___     / ___           / /  ___      ___     / ___  
  / __  (   // //   ) ) //   ) ) //\ \           / / //   ) ) //   ) ) //\ \   
 //    ) ) // //   / / //       //  \ \         / / //   / / //       //  \ \  
//____/ / // ((___( ( ((____   //    \ \  ((___/ / ((___( ( ((____   //    \ \ 
"""

def deal_card():
    card = random.choice(cards)
    return card

def cal_score(cards):
    if sum(cards) == 21 and len(cards)== 2:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return 'You lose, Opponent has BlackJack'
    elif u_score == 0:
        return 'You won with BlackJack'
    elif u_score>21:
        return 'You went over, You lose'
    elif c_score>21:
        return 'Opponnet went over, You win'
    elif u_score>c_score:
        return 'You Won'
    else:
        return 'You lose'

def play_game():
    print(logo)
    is_game_over = False
    player_cards=[]
    computer_card=[]
    player_score = -1
    computer_score = -1

    for i in range(2):
        player_cards.append(deal_card())
        computer_card.append(deal_card())
        
    # players_card = list(random.sample(cards,2))
    # delears_card = list(random.sample(cards,2))
    """For selecting multiple random elements from list we can use random.sample method"""

    while not is_game_over:
        player_score = cal_score(player_cards)
        computer_score = cal_score(computer_card)
        print('Your cards : ',player_cards, 'Current Score:',player_score)
        print('Computer first card: ',computer_card[0])

        if player_score == 0 or computer_score == 0 or player_score >21:
            is_game_over = True
        else:
            val = input('Type "y" to get another card or "n" to pass :')
            if val == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = cal_score(computer_card)

    print('Your final hand : ',player_cards, 'Final Score: ',player_score)
    print('Opponent final hand : ',computer_card, 'Final Score: ',computer_score)
    print(compare(player_score,computer_score))

while input("Do you want to play BlackJack. Type 'Y' or 'N'  ") == 'y' or 'Y':
    print("\n" * 20)
    play_game()
else:
    exit()



