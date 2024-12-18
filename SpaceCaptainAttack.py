from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(x, y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)



