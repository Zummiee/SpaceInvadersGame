from turtle import Turtle


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("spaceship-small.gif")
        self.color("orange")
        #self.speed(10)
        self.penup()
        self.goto(0, -220)

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())