def func(name, place):
    print(f'Hello {name}')
    print(f'This is {place}')
    print(f'{name}, you will definetely love {place}')

# func('Shivani', 'Kolkata')
def Love_calculator(name1, name2):
    name = name1+name2
    l1 = ['T', 'R', 'U', 'E']
    l2 = ['L', 'O', 'V', 'E']
    count1 = count2 = 0
    for char in l1:
        count1 += name.upper().count(char)
    count1 = str(count1)
    for char in l2:
        count2 += name.upper().count(char)
    count2 = str(count2)
    print('True Love Score is:', count1+count2) 

Love_calculator("Kanye West", "Kim Kardashian")    
