from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score_left = 0
        self.score_right = 0
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
        self.write(f"{self.score_left}:{self.score_right}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.score_left += 1
        self.update_score()

    def increase_score_right(self):
        self.score_right += 1
        self.update_score()