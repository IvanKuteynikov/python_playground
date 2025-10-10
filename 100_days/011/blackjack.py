import random
from art import logo
import textwrap 

def create_deck(n):
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = []
  while n > 0:
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    n -= 1
  return deck

def extract_value_of_card(hand):
    value = []
    for full_card in hand:
        if full_card[1] in ['J','Q','K']:
            value.append(10)
        elif full_card[1] == 'A':
            value.append(11)
        else:
            value.append(int(full_card[1]))
    return value

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        score -= 10 
    return score

def draw_a_card(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        hand.append(deck.pop())
    return hand

def show_card(card):
  space = " "
  if len(card[1]) == 2:
    space = ""
  return textwrap.dedent(f"""
    +-------+
    |{card[1]}     {space}|
    |       |
    |   {card[0]}   |
    |       |
    |{space}     {card[1]}|
    +-------+
  """)
  
def display_hand(hand_name, hand):
    print(f"{hand_name}:")
    card_strings = [show_card(card) for card in hand]
    split_cards = [card.strip().split('\n') for card in card_strings]
    for i in range(len(split_cards[0])):
        row = "   ".join([card[i] for card in split_cards])
        print(row)

continue_game = True
number_of_games = 0
player_wins = 0
computer_wins = 0

print("\n"*100)
print(logo)
deck = create_deck(5)
random.shuffle(deck)
    
while continue_game == True:
    if len(deck) < 260:
        while True:
            reset_deck = input(f"In deck now is: {len(deck)} cards, do you want to reset deck? (Y/N) ").lower()
            if reset_deck in ('y', 'n'):
                break
            else:
                print("Please enter Y or N")
        if reset_deck == 'y':
            deck = create_deck(5)
            random.shuffle(deck)
        else:
            print(f"Ok, we continue with {len(deck)} cards in a deck")
    print(f"Cards in deck: {len(deck)}")
    try:
        player = draw_a_card(deck, 2)
        computer = draw_a_card(deck, 2)
        player_score = calculate_score(extract_value_of_card(player))
        computer_score = calculate_score(extract_value_of_card(computer))
        while player_score < 21:
            print("="*77)
            display_hand("Your Hand", player)
            print(f"You have in total: {player_score}.\n")
            display_hand("Dealer's Hand", [computer[0], (' ', '?')])
            print("="*77)
            players_decision = input(f"Hit (H) or Stand (S)? ").lower()
            if players_decision == 'h':
                player.extend(draw_a_card(deck, 1))
                player_score = calculate_score(extract_value_of_card(player))
                print("\n"*30)
            elif players_decision == 's':
                print("\n"*30)
                break
            else:
                print("Invalid input. Please enter 'H' or 'S'.")
        if player_score < 21:
            while computer_score <= 16:
                computer.extend(draw_a_card(deck, 1))
                computer_score = calculate_score(extract_value_of_card(computer))
        if player_score == 21 and computer_score == 21:
            result = "It's a tie"
        elif player_score > 21:
            result = "You busted, Dealer wins"
            computer_wins += 1
        elif computer_score > 21:
            result = "You win, Dealer busted"
            player_wins += 1
        elif player_score > 21 and computer_score > 21:
            result = "It's a tie"
        elif player_score > computer_score:
            result = "You win"
            player_wins += 1
        elif player_score < computer_score:
            result = "Dealer wins"
            computer_wins += 1
        elif player_score == computer_score:
            result = "It's a tie"
        number_of_games += 1
        print(f"\nGame #{number_of_games}")
        display_hand("Your Hand", player)
        print(f"You have in total: {player_score}.\n")
        display_hand("Dealer's Hand", computer)
        print(f"Dealer have in total: {computer_score}.\n")
        print(f"{result}\n")
        print("-"*30)
        while True:
            ask_to_continue_game = input("Do you want to continue? (Y/N)? ")
            if ask_to_continue_game in ['y','n']:
                break
            else:
                print("Please enter Y or N")
        print("\n"*100)
        print(logo)
        print(f"\nCurrent result is:\n# of games played: {number_of_games}\nYou wins count: {player_wins} time(-s)\nDealer wins count: {computer_wins} time(-s)\n")
        if ask_to_continue_game == 'n':
            final_winner = ""
            if player_wins > computer_wins:
                final_winner = "You!"
            elif player_wins == computer_wins:
                final_winner = "Nobody, it's a tie!"
            else:
                final_winner = "Dealer!"
            print("\n"*100)
            print(logo)
            print(f"\nFinal result is:\n# of games played: {number_of_games}\nYou win: {player_wins} time(-s)\nDealer wins: {computer_wins} time(-s)\nWinner is {final_winner}")
            print("Thanks for playing! Goodbye!")
            break
    except KeyboardInterrupt:
        print("\nBye")