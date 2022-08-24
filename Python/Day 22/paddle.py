from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(5.0, 1.0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)