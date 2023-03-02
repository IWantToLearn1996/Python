import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_turtle, "Up")

car_manager = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    # Issue with distance function.
    # if player.turtle[0].distance(car_manager.cars) < 20:
    #   print("Shit")
    #   scoreboard.game_over()
    if player.turtle[0].ycor() > 260:
        print("WIN")
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_move()

