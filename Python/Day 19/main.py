from turtle import Turtle, Screen
import random
# timmy = Turtle()
screen=Screen()


# def move_forwards():
#     timmy.forward(10)


screen.listen()
# screen.onkey(key="w",fun=move_forwards)
# screen.exitonclick()

#Etch a sketch

# def move_backwards():
#     timmy.backward(10)
#
# def move_counter_clockwise():
#     timmy.left(10)
#
# def move_clockwise():
#     timmy.right(10)
#
# def clear_drawing():
#     timmy.home()
#     timmy.clear()
#
#
# screen.onkeypress(fun=move_forwards,key="w")
# screen.onkeypress(fun=move_backwards,key="s")
# screen.onkeypress(fun=move_counter_clockwise,key="a")
# screen.onkeypress(fun=move_clockwise,key="d")
# screen.onkey(key="c",fun=clear_drawing)
#

#Turtle race



screen.setup(width=500,height=400)
bet=screen.textinput("Winner", "Choose the winner.")
colors = ["red", "orange", "yellow", "blue", "green", "pink"]
positions=[-70, -40, -10, 20, 50, 80]
all_turtles=[]

timmy=Turtle()
timmy.penup()
timmy.goto(230,-80)
timmy.pendown()
timmy.goto(230,90)
timmy.hideturtle()

for index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=positions[index])
    all_turtles.append(new_turtle)


if bet:
    found_winner=False

while found_winner==False:

    for turtle in all_turtles:
        distance=random.randint(0,10)
        turtle.forward(distance)
        if turtle.xcor()>=230 and found_winner==False:
            found_winner=True
            winner=turtle.color()[1]

if winner==bet:
    print("Congratulations, you guessed right!")
else:
    print("Wrong guess, try again!")


screen.exitonclick()