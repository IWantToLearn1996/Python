from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            y_positions = random.randint(-260, 260)
            car.goto(x=300, y=y_positions)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_move(self):
        self.car_speed += MOVE_INCREMENT

