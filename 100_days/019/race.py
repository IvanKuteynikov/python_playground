import turtle as t
import random

is_race_on = False
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'black']
y = -120
i = 0

racers = []
for turtle in range(0,7):
    nit = t.Turtle(shape='turtle')
    nit.color(colors[turtle])
    nit.penup()
    nit.goto(x=-420,y=y)
    y += 40
    racers.append(nit)


screen = t.Screen()
screen.setup(900, 300)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win th race? Enter color: ")
print(user_bet)
if user_bet != '':
    is_race_on = True

while is_race_on:
    for racer in racers:
        if racer.xcor() > 420:
            is_race_on = False
            winner = racer.pencolor()
            if winner == user_bet:
                print("You win!")
            else:
                print(f"You lose! Winner is {winner}")
        rand_dist = random.randint(1, 10)
        racer.forward(rand_dist)



screen.listen()
screen.exitonclick()