import random

def asci_graph(val):
        match val:
            case 0:
                print("""ROCK
                                _______
                            ---'   ____)
                                  (_____)
                                  (_____)
                                  (____)
                            ---.__(___)
                            """)
            case 1:
                print("""PAPER
                            _______
                        ---'    ____)____
                                    ______)
                                    _______)
                                   _______)
                        ---.__________)
                        """)
            case 2:
                print("""SCISSORS
                            _______
                        ---'   ____)____
                                  ______)
                             __________)
                              (____)
                        ---.__(___)
                        """)
            case _:
                print('Invalid Input')
                exit()

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
asci_graph(user)
print('Computer Choose:')
com = random.randint(0,2)
asci_graph(com)
match user:     
     case 0:
          if com == 2:
               print('You Won!')
          elif com == 0:
               print('Draw')
               exit()
          else:
               print('You loose')
     case 1:
          if com == 0:
               print('You Won!')
          elif com == 1:
               print('Draw')
               exit()
          else:
               print('You Lose!')
     case 2:
          if com == 1:
               print('You Won!')
          elif com == 2:
               print('Draw')
               exit()
          else:
               print('You Lose!')