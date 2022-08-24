import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()

cars=CarManager()

scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.new_car()
    cars.move()

    # Car Collision
    if cars.collision(player):
        game_is_on=False
        scoreboard.gameover()

    #reached end of screen
    if player.ycor()>280:
        cars.increase_speed()
        player.reset()
        scoreboard.increase()
    screen.update()

screen.exitonclick()