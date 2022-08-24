from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt","r") as file:
            self.high_score=int(file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font="Arial")

    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font="Arial")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", False, align="center", font="Arial")

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("highscore.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font="Arial")
