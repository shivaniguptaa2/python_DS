import random

d=s=l=''
letters = [chr(i) for i in range(97, 123)]
digits = [str(i) for i in range(10)]
symbols = [ '$', '¢', '£', '€', '¥', '₹','@', '#', '&', '|', '\\', '/', '_', '~', '`']

print('Welcome to Py_Password Generator!')
val1 = int(input('Tell me how many characters you want in your password\n'))
val2 = int(input('How many numbers you want in your password\n'))
val3 = int(input('How many symbols would you prefer\n'))

for i in range(val2):
    d+= str(random.choice(digits))

for i in range(val3):
    s+= str(random.choice(symbols))

val1 = val1-(val2+val3)
for i in range(val1):
    l+= str(random.choice(letters))

password = l+s+d
password = password.capitalize()

print('Here is your strong password: ',password)