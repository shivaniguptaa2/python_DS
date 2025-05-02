output = 0
cond = 'new'

def add(n1, n2):
    val = n1+n2
    print(f'{n1}+{n2} = ',val)
    return val

def sub(n1, n2):
    val = n1-n2
    print(f'{n1}-{n2} = ',val)
    return val

def mul(n1,n2):
    val = n1*n2
    print(f'{n1}*{n2} = ',val)
    return val

def div(n1, n2):
    val = n1/n2
    print(f'{n1}/{n2} = ',val)
    return val

def run(n1):  
    operator = input('Choose operation: \n+\n-\n*\n/\n' )
    n2 = int(input('Enter second number: '))

    match operator:
        case '+':
            output = add(n1, n2)
        case '-':
            output = sub(n1, n2)
        case '*':
            output = mul(n1, n2)
        case '/':
            output = div(n1, n2)
        case _:
            print('Invalid operation')
    return output

while True:
    if cond == 'new':
        n1 = int(input('Enter first number: '))
        res = run(n1)
        
    elif cond == 'yes':
        n1 = res
        res = run(res)
    
    else:
        print('Thanks for using the calculator')
        exit()

    cond = input('If you want to continue calculating, type "yes" \n If you want to start new caluclation type "new" \n'
             'If you want to exit type "exit" \n')