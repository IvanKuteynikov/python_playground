import random
from art import logo, wrong
from gamedata import data

contunue_game = True
entry_A = 0
results_entry_number = -1
result = ""
rounds = 0
data_game = data.copy()


def validate_input(prompt, valid_options):
    while True:
        users_input = input(prompt).lower()
        if users_input in valid_options:
            return users_input
        else:
            print(f"Please enter: {" or ".join(valid_options)}")
            
def describe_contestants(position, entry):
    return print(f"{position} - {data_game[entry]["name"]}: {data_game[entry]["description"]}, from: {data_game[entry]["country"]}")


while contunue_game:
    data_max = len(data_game) - 1
    if len(data_game) < 2:
        print(f"You correctly guessed: {rounds} times")
        print("Goodbye, thanks for playing!")
        break
    print("\n"*30)
    print(logo)
    print(len(data_game))
    if results_entry_number == -1:
        entry_A = random.randint(0,data_max)
    else:
        entry_A = results_entry_number
    entry_B = random.randint(0,data_max)
    while entry_A == entry_B:
        entry_B = random.randint(0,data_max)
    followers_A = int(data_game[entry_A]["follower_count"])
    followers_B = int(data_game[entry_B]["follower_count"])
    print("="*100)
    describe_contestants("A", entry_A)
    print("-"*100)
    describe_contestants("B", entry_B)
    print("="*100)
    if followers_A > followers_B:
        result = 'a'
        results_entry_number = entry_A
        data_game.pop(entry_B)
    else:
        result = 'b'
        results_entry_number = entry_B
        data_game.pop(entry_A)
    guess = validate_input("\nWho is higher? A or B? ", ['a','b'])
    if guess == result:
        print("right")
        entry_A = results_entry_number
        rounds += 1
        print("\n"*30)
    else:
        print("."*100)
        print(wrong)
        print("."*100)
        print(f"You correctly guessed: {rounds} times")
        print(f"I know! You could better!")
        try_again = validate_input("Try again? (Y/N)", ['y','n'])
        if try_again == 'y':
            rounds = 0
            print(len(data_game))
            print(len(data))
            data_game = data.copy()
            print(len(data_game))
            continue
        else:
            print("Goodbye, thanks for playing!")
            contunue_game = False