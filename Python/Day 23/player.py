STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
    def move(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)