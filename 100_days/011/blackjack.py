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

player = count_first_round("player")
computer = count_first_round("computer")

players_decision = input(f"You've got got: {player}, computer got: {computer}. HIT or STAND ").lower()
if players_decision == 'hit':
    player += draw_a_card()
    computer += draw_a_card()
while computer <= 16:
    computer += draw_a_card()
if player == 21 and computer == 21:
    result = "tie"
elif player > 21:
    result = "player busted, computer wins"
elif computer > 21:
    result = "computer busted, player wins"
elif player > computer:
    result = "player wins"
elif player < computer:
    result = "computer wins"
elif player == computer:
    result = "it's a tie"
    
print(f"player got: {player} \ncomputer got: {computer}\n {result}")

