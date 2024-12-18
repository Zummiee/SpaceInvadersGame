from turtle import Turtle


class Alien(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("peace-alien-small.gif")
        self.penup()
        self.goto(x, y)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


