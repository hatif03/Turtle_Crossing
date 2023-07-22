from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()

    def display(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"LEVEL: {self.level}", font=FONT)

    def win(self):
        self.level += 1
        self.display()

    def over(self):
        self.goto(-80, 0)
        self.write("Game Over", font=FONT)
