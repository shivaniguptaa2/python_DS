alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print('Welcome to Ceaser_cipher')
code = input('Choose E for encoding or D for decoding your message: ').lower()
text = input("Enter the Word: ").lower()
shift = int(input("Tell me with my the number for shift: "))

def encode(text,shift):
    cipher=''
    for ch in text:
        idx = (alphabet.index(ch)+shift)%len(alphabet)
        cipher += alphabet[idx]
    print(cipher)

def decode(text,shift):
    cipher=''
    for ch in text:
        idx = (alphabet.index(ch)-shift)%len(alphabet)
        cipher += alphabet[idx]
    print(cipher)

match code:
    case 'e':
        encode(text,shift)
    case 'd':
        decode(text,shift)
    case _:
        print('Invalid code')

# cipher=''
# for ch in text:
#     idx = alphabet.index(ch)-shift
#     cipher += alphabet[idx]
#     print(cipher)
# print(cipher)

