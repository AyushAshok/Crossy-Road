import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player=Player()
score=Scoreboard()
cars=CarManager()

screen.listen()
screen.onkeypress(player.move,"Up")

game_is_on = True



while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create()
    cars.move_cars()

    for caru in cars.all_cars:
        if caru.distance(player)<21:
            score.ended()
            game_is_on=False

    if player.end_reach():
        player.end()
        cars.levelup()
        score.levelup()


screen.exitonclick()