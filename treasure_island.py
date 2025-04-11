print('Welcome to the Treasure Island!')
print('Your mission is to find the treasure..')
choice = input('Tell me where you wanna go: Left or Right?\n')
if choice.upper()== 'LEFT':
    c2 = input('Do you wanna swim or wait?\n')
    if c2.upper() == 'WAIT':
        c3 = input('Choose the Door: Red, Blue or Yellow\n')
        if c3.upper() == 'YELLOW':
            print('You Win!')
        else:
            print('Game Over')
    else :
        print('Game Over')
else :
    print('Game Over')