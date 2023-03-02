from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import Scoreboard
import random, time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.squares[0].distance(food) < 15:
        food.new_food()
        scoreboard.increase_score()
        snake.increase_snake()

    for turtle in snake.squares[1:]:
        # if snake.squares[0] == turtle:
        #     pass
        if snake.squares[0].distance(turtle) < 10:
            scoreboard.reset()
            snake.reset()

    if snake.squares[0].xcor() > 299 or snake.squares[0].xcor() < -299 or snake.squares[0].ycor() > 299 or snake.squares[0].ycor() < -299:
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
