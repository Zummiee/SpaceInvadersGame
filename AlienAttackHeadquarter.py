from turtle import Turtle


class Attack(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("drone-small.gif")
        self.penup()
        self.goto(x, y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)