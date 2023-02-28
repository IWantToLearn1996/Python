from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.pensize(15)
tim.speed(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

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
    tim.color(random_color())
    random_walk()








#In the bottom because it's the Last thing we want to do.
screen = Screen()
screen.exitonclick()
