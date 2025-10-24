import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

def play_game():
    game_is_on = True
    score.start_game_display()
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car.create_car()
        car.move()
        for i in car.all_cars:
            if player.distance(i) < 20:
                score.print_game_over()
                game_is_on = False
        if player.ycor() > 270:
            score.increase_level()
            player.reset_pos()
            car.move_increase()

play_game()
screen.exitonclick()