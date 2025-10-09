import random
from art import logo

def draw_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10 
    return score

continue_game = True
number_of_games = 0
player_score = 0
computer_score = 0

while continue_game == True:
    print(logo)
    try:
        player = [draw_a_card(), draw_a_card()]
        computer = [draw_a_card(), draw_a_card()]
        while calculate_score(player) < 21:
            print("="*77)
            print(f"You have {player} in total: {calculate_score(player)}. Dealer got: [{computer[0]}, ?]")
            print("="*77)
            players_decision = input(f"Hit (H) or Stand (S)? ").lower()
            if players_decision == 'h':
                player.append(draw_a_card())
            elif players_decision == 's':
                break
            else:
                print("Invalid input. Please enter 'H' or 'S'.")
        if calculate_score(player) < 21:
            while calculate_score(computer) <= 16:
                computer.append(draw_a_card())
        if calculate_score(player) == 21 and calculate_score(computer) == 21:
            result = "It's a tie"
        elif calculate_score(player) > 21:
            result = "You busted, Dealer wins"
            computer_score += 1
        elif calculate_score(computer) > 21:
            result = "You win, Dealer busted"
            player_score += 1
        elif calculate_score(player) > 21 and calculate_score(computer) > 21:
            result = "It's a tie"
        elif calculate_score(player) > calculate_score(computer):
            result = "You win"
            player_score += 1
        elif calculate_score(player) < calculate_score(computer):
            result = "Dealer wins"
            computer_score += 1
        elif calculate_score(player) == calculate_score(computer):
            result = "It's a tie"
        number_of_games += 1
        print(f"\nGame #{number_of_games}\nYou got: {player} in total: {calculate_score(player)} \nDealer got: {computer} in total {calculate_score(computer)} \n{result}\n")
        print("-"*30)
        while True:
            ask_to_continue_game = input("Do you want to continue? (Y/N)? ")
            if ask_to_continue_game in ['y','n']:
                break
            else:
                print("Please enter Y or N")
        print("\n"*100)
        print(logo)
        print(f"\nCurrent result is:\n # of games played: {number_of_games}\nYou wins: {player_score} time(-s)\nDealer wins: {computer_score} time(-s)")
        if ask_to_continue_game == 'n':
            final_winner = ""
            if player_score > computer_score:
                final_winner = "You!"
            elif player_score == computer_score:
                final_winner = "Nobody, it's a tie!"
            else:
                final_winner = "Dealer!"
            print("\n"*100)
            print(logo)
            print(f"\nFinal result is:\n# of games played: {number_of_games}\nYou win: {player_score} time(-s)\nDealer wins: {computer_score} time(-s)\nWinner is {final_winner}")
            print("Thanks for playing! Goodbye!")
            break
    except KeyboardInterrupt:
        print("\nBye")

