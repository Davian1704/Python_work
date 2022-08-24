FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore=0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level=1
        self.goto(-280,260)
        self.write(f"Level: {self.level}",FONT)

    def increase(self):
        self.clear()
        self.level+=1
        self.write(f"Level: {self.level}",FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!", FONT)
