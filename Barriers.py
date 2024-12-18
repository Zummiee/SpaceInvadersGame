from turtle import Turtle


class Barrier(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("grey")
        self.shape("square")
        self.goto(x, y)