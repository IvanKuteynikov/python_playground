import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)

display = []
#print(chosen_word)
for i in range(len(chosen_word)):
    display.append("_")
print("\nWelcome to hangman game")
print("word was chosen, try to guess:\n")    
print("".join(display))
lives = 6
game_over = False

print(f"\nYou've got: {lives} attempts")
while not game_over:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        print(f"There is no letter - {guess}!")
        lives -= 1
    print(stages[lives])
    print("".join(display))
    print(f"attempts remain: {lives}\n")
    
    if lives == 0 and "".join(display) != chosen_word:
        game_over = True
        print("You lose")
        print(f"Word was: {chosen_word}")
    elif lives != 0 and "".join(display) == chosen_word:
        game_over = True
        print("You won!")
        print(stage_7)