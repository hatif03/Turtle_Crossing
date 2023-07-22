import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

playr = Player()
lvl = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(playr.move, "Up")

count = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    lvl.display()

    if playr.ycor() >= 270:
        playr.start()
        lvl.win()
        car.speed_inc()

    if count % 6 == 0:
        car.create_car()

    car.move_car()

    for i in car.cars:
        if i.distance(playr) <= 22:
            lvl.over()
            game_is_on = False
    count += 1
screen.exitonclick()
