import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

game_is_on = True
LEFT = -350
RIGHT = 350

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(RIGHT)
left_paddle = Paddle(LEFT)
ball = Ball(1)
score = Scoreboard()
screen.listen()


def play_game():
    score.start_game_display()
    while game_is_on:
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
            ball.bounce_x()
            ball.move_speed *= 1.01
            print(f"ball move speed: {ball.move_speed}")
        if ball.xcor() < -380:
            score.increase_score_right()
            ball.ball_reset()
        if ball.xcor() > 380:
            score.increase_score_left()
            ball.ball_reset()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(play_game, "space")

screen.exitonclick()