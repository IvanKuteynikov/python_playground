from turtle import Turtle as t
import random as rnd


class Food(t):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_random = rnd.randint(-260,260)
        y_random = rnd.randint(-260,260)
        self.goto(x_random, y_random)
