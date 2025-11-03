import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()}

def generate_phonetic():
    try:
        users_input = input("Enter a word: ").upper()
        users_input_letters = [letter for letter in users_input]
        phonetic = [alphabet_dict[letter] for letter in users_input_letters]
    except KeyError:
        print("Sorry, I didn't understand your input. Please try again.")
        generate_phonetic()
    else:
        print(phonetic)

generate_phonetic()