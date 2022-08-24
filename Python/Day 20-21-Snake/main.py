from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()

scoreboard=Scoreboard()

game_on = True



while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Collision
    if snake.head.distance(food) < 15:
        food.move()
        snake.add_segment()
        scoreboard.score_increase()

    #Detect collision with wall
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        scoreboard.reset()
        snake.reset()

    #Detect collisions with tail
    for segments in snake.snake[1:]:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments)<10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
