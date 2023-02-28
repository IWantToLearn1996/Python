from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
colors = ["CornflowerBlue", "DarkOrchid", "red", "LightSeaGreen", "black", "SlateGray", "purple"]
tim.pensize(15)
tim.speed(10)

choices = ["1", "2", "3", "4"]
def random_walk():
    if walk == "1":
        tim.forward(100)
    elif walk == "2":
        tim.back(100)
    elif walk == "3":
        tim.left(90)
    else:
        tim.right(90)

for _ in range(100):
    walk = random.choice(choices)
    tim.color(random.choice(colors))
    random_walk()








#In the bottom because it's the Last thing we want to do.
screen = Screen()
screen.exitonclick()
