from turtle import Turtle, Screen
import random

is_Race_on = False
# Screen Set-Up
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Please, Enter a Color: ")

# Turtles' colors
colors = ["red", "gray", "yellow", "purple", "black"]

# Y-axis Position
y_position = [-80, -40, 0, 40, 80]
# Turtle Set-Up
all_turtles = []
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_Race_on = True

distance = [10, 20, 30, 40, 50, 100]
while is_Race_on:
    for turtle in all_turtles:
        turtle.forward(random.choice(distance))
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"User WINS with the {winner_color} Turtle")
            else:
                print(f"User LOSES. {winner_color} Turtle wins")
            is_Race_on = False

screen.exitonclick()
