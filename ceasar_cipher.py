alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

val = 'yes'
def encode(text,shift):
    cipher=''
    for ch in text:
            if ch in alphabet:
                idx = (alphabet.index(ch)+shift)%len(alphabet)
                cipher += alphabet[idx]
            else:
                cipher += ch    
    print(cipher)

def decode(text,shift):
    cipher=''
    for ch in text:
        if ch in alphabet:
            idx = (alphabet.index(ch)-shift)%len(alphabet)
            cipher += alphabet[idx]
        else:
            cipher += ch
        
    print(cipher)


print('Welcome to Ceaser_cipher')
while(val == 'yes'):
    code = input('Choose E for encoding or D for decoding your message: ').lower()
    text = input("Enter the Word: ").lower()
    shift = int(input("Tell me with my the number for shift: "))
    match code:
        case 'e':
            encode(text,shift)
        case 'd':
            decode(text,shift)
        case _:
            print('Invalid code')
            break
  
    print('Do you want to continue?')
    val = input('Enter YES for continue or NO for exit: ').lower()

