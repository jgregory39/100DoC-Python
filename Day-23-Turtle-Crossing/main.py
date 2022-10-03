import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

for i in range(100):
    cars.decide_cars()
    cars.move_cars()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.decide_cars()
    cars.move_cars()
    if player.ycor() > player.get_finish():
        player.reset_pos()
        scoreboard.inc_score()
        cars.inc_speed()
    if not cars.is_clear(player.ycor(), True):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
