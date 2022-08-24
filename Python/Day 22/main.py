from turtle import  Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

left_paddle=Paddle()
left_paddle.goto(-360, 0)

right_paddle=Paddle()
right_paddle.goto(360,0)

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

ball=Ball()

scoreboard=ScoreBoard()

game_on=True

while game_on:


    #Collision with walls
    if ball.ycor() >= 280 or ball.ycor() <=-280:
        ball.bounce(ball.x_direction,ball.y_direction*(-1))

    #Collision with paddles

    if (ball.distance(right_paddle)<50 and ball.xcor()>350) or (ball.distance(left_paddle)<50 and ball.xcor()<-350):
        ball.bounce(ball.x_direction*(-1),ball.y_direction)

    elif ball.xcor()>370:
        #Goes past paddle
        ball.bounce(ball.x_direction*(-1), ball.y_direction)
        ball.reset()
        scoreboard.left_point()
    elif ball.xcor()<-370:
        ball.bounce(ball.x_direction * (-1), ball.y_direction)
        ball.reset()
        scoreboard.right_point()



    ball.move()
    screen.update()

screen.exitonclick()
