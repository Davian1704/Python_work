from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_direction = 0.2
        self.y_direction = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.goto(self.xcor() +self.x_direction, self.ycor() +self.y_direction)

    def bounce(self, x_direction, y_direction):
        self.x_direction = x_direction
        self.y_direction = y_direction


    def reset(self):
        self.hideturtle()
        self.goto(0,0)
        self.showturtle()
        self.y_direction = random.uniform(-0.2, 0.2)