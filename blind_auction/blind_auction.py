import random
from items import artwork

more = True
bidder = {}
n = random.randint(0,6)  # Fixed to select a random artwork from the list
art = artwork[n]["art"]
cost = artwork[n]["cost"]  # Added to get the cost of the selected artwork
print('Welcome to Blind Auction')
while more:
    print(art)
    name = input('Enter your name: ')
    bid = int(input('\nEnter your bid: $ '))
    bidder[name] = bid
    more = input('\nAre there any other bidders? Type "yes" or "no": ').lower()
    if more != 'yes':
        more = False
    else:
        print("\n" * 75)

max_bid = max(bidder, key=bidder.get)
print(f'\nThe winner is {max_bid} with a bid of ${bidder[max_bid]}')
print(f'\nThe artwork is worth ${cost}')  # Updated to reflect the correct structure
print('Thank you for participating in the Blind Auction!')