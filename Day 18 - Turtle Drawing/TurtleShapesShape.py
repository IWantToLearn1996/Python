from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "red", "LightSeaGreen", "black", "SlateGray", "purple"]

tim.penup()
tim.left(90)
tim.forward(300)
tim.right(90)
tim.pendown()

def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape in range(3, 100):
    tim.color(random.choice(colors))
    draw(shape)










#In the bottom because it's the Last thing we want to do.
screen = Screen()
screen.exitonclick()
