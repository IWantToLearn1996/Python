import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:

    def __init__(self):
        self.turtle = []
        self.create_turtle()

    def create_turtle(self):
        turtle = Turtle()
        turtle.shape("turtle")
        turtle.penup()
        turtle.color("black")
        turtle.left(90)
        self.turtle.append(turtle)
        self.turtle[0].goto(STARTING_POSITION)

    def move_turtle(self):
        new_y = self.turtle[0].ycor() + MOVE_DISTANCE
        self.turtle[0].goto(self.turtle[0].xcor(), new_y)

    def reset_position(self):
        self.turtle[0].goto(STARTING_POSITION)

