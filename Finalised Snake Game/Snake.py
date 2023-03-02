from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for x_position in range(0, -41, -20):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=x_position, y=0)
            self.squares.append(new_turtle)

    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
            print(new_x, new_y)
        self.squares[0].forward(MOVE_DISTANCE)

    def increase_snake(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        self.squares.append(new_turtle)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()

    def up(self):
        self.squares[0].setheading(90)
    def down(self):
        self.squares[0].setheading(270)
    def right(self):
        self.squares[0].setheading(0)
    def left(self):
        self.squares[0].setheading(180)