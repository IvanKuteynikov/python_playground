import random
from art import logo

def chosen_number():
    n = random.randint(1,100)
    return n

def check_a_guess(num_to_guess, users_guess):
    if users_guess > num_to_guess:
        return f"Your guess: {users_guess} is too high!\n"
    elif users_guess < num_to_guess:
        return f"Your guess: {users_guess} is too low!\n"
    else:
        return "You guessed!"

def number_of_guesses(users_choice_of_level_difficulty):
    while True:
        if users_choice_of_level_difficulty in ['easy', 'hard']:
            break
        else:
            print("Print 'easy' or 'hard'!")
    if users_choice_of_level_difficulty == 'easy':
        return 10
    else:
        return 5
    
def game(n):
    while n > 0:
        print(f"You have {n} attempts remaining to guess the number!")
        try:
            users_guess = int(input("Make a guess: "))
        except ValueError:
            print("\nThat's not a valid number. Please try again.")
            continue
        result = check_a_guess(num_to_guess, users_guess)
        if result == 'You guessed!':
            print(result)
            break
        else:
            print(result)
        print("Guess again!")
        n -= 1
    return n

def restart_game():
    restart = validate_input("Want to play again? Y/N ",['y','n'])
    if restart == 'y':
        return True
    else:
        print("Goodbye!")
        return False

def games_intro():
    print("\n"*30)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
def validate_input(prompt, options):
    while True:
        user_input = input(f"{prompt}").lower()
        if user_input in options:
            return user_input
        else:
            print(f"Please enter: {" or ".join(options)}")
    
game_restart = True

try:
    while game_restart:
        games_intro()
        num_to_guess = chosen_number()
        users_choice_of_level_difficulty = validate_input("Choose a difficulty. Type 'easy' or 'hard: ",['easy', 'hard'])
        n = number_of_guesses(users_choice_of_level_difficulty)
        n = game(n)
        if n > 0:
            print("Congratulations! You won!")
        else:
            print("Game over! You lose!")
            print(f"I was thinking about {num_to_guess}")
        game_restart = restart_game()
except KeyboardInterrupt:
    print("\nGoodbye")
