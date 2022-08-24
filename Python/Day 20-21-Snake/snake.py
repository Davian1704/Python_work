from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            timmy = Turtle()
            timmy.goto(0 - 10 * (i - 1), 0)
            timmy.shape("square")
            timmy.color("white")
            timmy.penup()
            self.snake.append(timmy)
        self.head = self.snake[0]

    def add_segment(self):
        timmy = Turtle()
        timmy.penup()
        timmy.shape("square")
        timmy.color("white")
        timmy.goto(self.snake[len(self.snake) - 1].xcor(), self.snake[len(self.snake) - 1].ycor())
        self.snake.append(timmy)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].xcor(), self.snake[segment - 1].ycor())
        self.snake[0].forward(20)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def reset(self):
        for segment in self.snake:
            segment.hideturtle()
        self.snake.clear()
        self.__init__()
