from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")

#  Colors list after Running the ExtractRGBColors Module.
color_list = [(249, 248, 244), (250, 245, 248), (243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71),
              (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168),
              (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132),
              (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232),
              (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34), (11, 97, 52),
              (169, 181, 232), (241, 169, 155), (252, 7, 40), (10, 84, 100), (63, 98, 8), (14, 51, 250), (250, 11, 8)]

tim.penup()
tim.right(90)
tim.forward(250)
tim.right(90)
tim.forward(300)
tim.right(180)
tim.hideturtle()


def paint():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()


def go_back():
    for _ in range(1):
        tim.penup()
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)


for _ in range(10):
    paint()
    go_back()


screen = Screen()
screen.exitonclick()
