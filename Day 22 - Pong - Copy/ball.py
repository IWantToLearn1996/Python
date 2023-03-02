from turtle import Turtle
import random

# Food class has inherited everything from Turtle class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len= .75, stretch_wid=.75)
        self.color("white")
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(x=0, y=0)
        self.x_move *= -1
        num = random.randint(-2, 2)
        if num == 0:
            self.y_move *= -1
        self.move_speed = 0.1

