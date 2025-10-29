

import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}
#print(alphabet_dict)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

users_input = input("Enter a word: ").upper()

users_input_letters = [letter for letter in users_input]

#phonetic = [word for (key, word) in alphabet_dict.items() if key == users_input_letters[0]]

phonetic = [alphabet_dict[letter] for letter in users_input_letters]
print(phonetic)