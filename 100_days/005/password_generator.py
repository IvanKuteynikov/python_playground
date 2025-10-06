import random
import string

def get_valid_input(prompt, valid_options):
  while True:
    user_input = input(prompt).lower()
    if user_input in valid_options:
      return user_input
    else:
      print(f"Invalid input. Please enter one of {valid_options}.")

def get_password_len(prompt):
  while True:
    try:
      user_input = int(input(prompt))
      if user_input > 0 and user_input <= 100:
        return user_input
      elif user_input == 0:
        print("Length must be greater than 0.")
      elif user_input < 0:
        print("Length must be a positive number.")
      elif user_input > 100:
        print("Length must be less than or equal to 100.")
    except ValueError:
      print("That's not a valid number. Please enter a digit.")

print("Welcome to the PyPassword Generator\n")

# --- 1. GATHER USER REQUIREMENTS ---
password_len = get_password_len('What len of the password do you want? ')
include_letters = get_valid_input('Should it contain letters (Y/N)? ',['y','n'])
include_digits = get_valid_input('Should it contain digits (Y/N)? ',['y','n'])
include_symbols = get_valid_input('Should it contain symbols (Y/N)? ',['y','n'])

# --- 2. BUILD THE CHARACTER POOL ---
character_pool = []
if include_letters == 'y':
  character_pool.extend(string.ascii_letters)
if include_digits == 'y':
  character_pool.extend(string.digits)
if include_symbols == 'y':
    character_pool.extend(string.punctuation)

# --- 3. GENERATE THE PASSWORD ---
if not character_pool:
  print("Cannot generate a password. You must select at least one character type.")
else:
  password_list = [random.choice(character_pool) for _ in range(password_len)]
  random.shuffle(password_list)
  final_password = "".join(password_list)
  print("-" * 20)
  print(f"Your new password is: {final_password}")
  print("-" * 20)