from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.color('white')
        self.speed("fastest")
        self.goto(side,0)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
