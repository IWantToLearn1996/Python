from turtle import Turtle

class Parallelogram:

    def __init__(self):
        self.paddles = []
        self.create_paddles()

    def create_paddles(self):
        for i in range (2):
            turtle = Turtle()
            turtle.shape("square")
            turtle.penup()
            turtle.shapesize(stretch_wid=8, stretch_len=2)
            turtle.color("white")
            self.paddles.append(turtle)
        self.paddles[0].goto(x=350, y=0)
        self.paddles[1].goto(x=-350, y=0)

    def up(self):
        new_y = self.paddles[0].ycor() + 40
        self.paddles[0].goto(self.paddles[0].xcor(), new_y)

    def up2(self):
        new_y = self.paddles[1].ycor() + 40
        self.paddles[1].goto(self.paddles[1].xcor(), new_y)

    def down(self):
        new_y = self.paddles[0].ycor() - 40
        self.paddles[0].goto(self.paddles[0].xcor(), new_y)

    def down2(self):
        new_y = self.paddles[1].ycor() - 40
        self.paddles[1].goto(self.paddles[1].xcor(), new_y)