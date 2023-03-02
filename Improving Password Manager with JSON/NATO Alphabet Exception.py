import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

try_again = True
while try_again:
    try:
        word = input("Enter a word: ").upper()
        word_list = [phonetic_dict[letter] for letter in word]
        print(word_list)
        try_again = False
    except KeyError:
        print("Please put only letters that exist in the Alphabet!")
        try_again = True
