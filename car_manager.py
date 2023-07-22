from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new = Turtle("square")
        new.shapesize(1, 3)
        new.penup()
        new.color(COLORS[randint(0, len(COLORS) - 1)])
        new.goto(300, randint(-230, 250))
        self.cars.append(new)

    def move_car(self):
        for car in self.cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())

    def speed_inc(self):
        self.car_speed += MOVE_INCREMENT
