from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.pensize()
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def circles(num_of_circles):
    angle = 360 / num_of_circles
    for _ in range(num_of_circles):
        tim.color(random_color())
        tim.circle(100)
        tim.left(angle)

number = int(input("Number of cirlces: "))
circles(number)






#In the bottom because it's the Last thing we want to do.
screen = Screen()
screen.exitonclick()
