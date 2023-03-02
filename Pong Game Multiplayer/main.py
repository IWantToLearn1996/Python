import random
from turtle import Screen
from paddles import Parallelogram
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen configurations
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer()

# Create Paddles
parallelogram = Parallelogram()

# Move Paddles Up and Down
screen.listen()

# Move Up and Down the Right Paddles
screen.onkey(parallelogram.up, "Up")
screen.onkey(parallelogram.down, "Down")

# Move Up and Down the Left Paddles
screen.onkey(parallelogram.up2, "w")
screen.onkey(parallelogram.down2, "s")

# Ball Creation
ball = Ball()

# Scoreboard Creation
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.xcor() > 320 and ball.distance(parallelogram.paddles[0]) < 50 or ball.xcor() < -320 and ball.distance(parallelogram.paddles[1]) < 50:
        ball.bounce_x()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 380:
        scoreboard.increase_score_left()
        ball.reset_position()
        print("Left")
    if ball.xcor() < -380:
        scoreboard.increase_score_right()
        ball.reset_position()
        print("Right")

screen.exitonclick()