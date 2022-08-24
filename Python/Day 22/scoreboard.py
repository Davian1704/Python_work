from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.write(f" {self.score_left} : {self.score_right} ", False, align="center", font="Arial")

    def left_point(self):
        self.clear()
        self.score_left+=1
        self.write(f"{self.score_left} : {self.score_right}", False, align="center", font="Arial")

    def right_point(self):
        self.clear()
        self.score_right+=1
        self.write(f"{self.score_left} : {self.score_right}", False, align="center", font="Arial")