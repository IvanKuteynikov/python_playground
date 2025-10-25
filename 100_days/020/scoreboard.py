from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

with open("high_score.txt", 'r') as file:
    high_score = file.read()
    if high_score == '':
        high_score = 0
    else:
        high_score = int(high_score)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.print_game_start()

    def print_game_start(self):
        self.goto(0, 0)
        self.write(f"Press SPACE button to START", align=ALIGNMENT, font=FONT)

    def start_game_display(self):
        self.clear()
        self.goto(0, 270)
        self.update_score()

    def print_game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", 'w') as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()