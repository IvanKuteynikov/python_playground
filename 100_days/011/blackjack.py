import random

def draw_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #11 stands for Ace and counts as 11 or 1, King, Queen and Valer counts as 10
    card = random.choice(cards)
    return card

def count_first_round(gamer):
    score = 0
    if gamer == 'player':
        n = 0
    else:
        n = 1
    while n < 2:
        score += draw_a_card()
        n += 1
    return score

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10 
    return score
    

player_hand = []
computer_hand = []

player_hand.append(draw_a_card())
computer_hand.append(draw_a_card())
player_hand.append(draw_a_card())
computer_hand.append(draw_a_card())
player_total = calculate_score(player_hand)
computer_total = calculate_score(computer_hand)


print(f"player got: {player_hand[0]} and {player_hand[1]} total is {player_total}")
print(f"computer got: {computer_hand[0]} total is {computer_total}")


continue_game = True
number_of_games = 0
player_score = 0
computer_score = 0

while continue_game == True:
    try:
        player = count_first_round("player")
        computer = count_first_round("computer")
        while player < 21:
            print("="*30)
            players_decision = input(f"You have {player}. Dealer got: {computer}. Hit (H) or Stand (S)? ").lower()
            if players_decision == 'h':
                player += draw_a_card()
            elif players_decision == 's':
                break
            else:
                print("Invalid input. Please enter 'H' or 'S'.")
        computer += draw_a_card()
        if player_score < 21:
            while computer <= 16:
                computer += draw_a_card()
        if player == 21 and computer == 21:
            result = "It's a tie"
        elif player > 21:
            result = "You busted, computer wins"
            computer_score += 1
        elif computer > 21:
            result = "You win, computer busted"
            player_score += 1
        elif player > 21 and computer > 21:
            result = "It's a tie"
        elif player > computer:
            result = "You win"
            player_score += 1
        elif player < computer:
            result = "Computer wins"
            computer_score += 1
        elif player == computer:
            result = "It's a tie"
        number_of_games += 1
        print(f"\nGame #{number_of_games}\nYou got: {player} \nDealer got: {computer} \n{result}\n")
        print("-"*30)
        while True:
            ask_to_continue_game = input("Do you want to continue? (Y/N)? ")
            if ask_to_continue_game in ['y','n']:
                break
            else:
                print("Please enter Y or N")
        print(f"\nCurrent result is:\n # of games played: {number_of_games}\nYou wins: {player_score} times\nComputer wins: {computer_score} times")
        if ask_to_continue_game == 'n':
            final_winner = ""
            if player_score > computer_score:
                final_winner = "You!"
            elif player_score == computer_score:
                final_winner = "Nobody, it's a tie!"
            else:
                final_winner = "Dealer!"
            print("\n"*100)
            print(f"\nFinal result is:\n# of games played: {number_of_games}\nYou wins: {player_score} times\nComputer wins: {computer_score} time(s)\nWinner is {final_winner}")
            print("Thanks for playing! Goodbye!")
            break
    except KeyboardInterrupt:
        print("\nBye")

