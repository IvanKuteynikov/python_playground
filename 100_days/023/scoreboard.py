from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.color('black')
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
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()
