import pandas as pd

# words = pd.read_csv('comprehensions/word_bank.csv')
# print(words)

# symbol =
name =  input('Tell me you Name!!: ')
name_list = [letter for letter in name.upper()]

def todo(name_list):
    word = pd.read_csv('comprehensions/word_bank.csv')
    words = pd.DataFrame(word)
    # for (index,row) in words.iterrows():
    #     if row.letter in name_list:
    #         print(row.code)
    for letter in name_list:
        row = words[words['letter'] == letter]
        if not row.empty:
            print(row.iloc[0]['code'])

todo(name_list)
# print(name_list)
# word = pd.read_csv('comprehensions/word_bank.csv')
# words = pd.DataFrame(word)
# print(words)
