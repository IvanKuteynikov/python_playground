from turtle import Turtle


class Ball(Turtle):
    def __init__(self, move_speed):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color('white')
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 350/300
        self.y_move = 300/350
        self.move_speed = move_speed

    def move(self):
        new_y = self.ycor() + self.y_move * self.move_speed
        new_x = self.xcor() + self.x_move * self.move_speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.move_speed <= 3:
            self.move_speed *= 1.1
        else:
            self.move_speed = 3

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 1
        self.bounce_x()

