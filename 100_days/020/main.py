import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard




screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

def play_game():
    score.start_game_display()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            score.increase_score()
            snake.extend()
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset_score()
            snake.reset_snake()
        for part in snake.body[1:]:
            if snake.head.distance(part) < 15:
                score.reset_score()
                snake.reset_snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(play_game, "space")



screen.exitonclick()