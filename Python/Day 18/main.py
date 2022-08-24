from turtle import Turtle, Screen,colormode,delay
import random

timmy=Turtle()
timmy.shape("turtle")
timmy.color("green")

# timmy.forward(200)
# timmy.right(45)
# timmy.backward(120)


#Square

# for i in range(1,5):
#     timmy.forward(100)
#     timmy.right(90)

#Dotted line
# for i in range(20):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


#Different shapes

# sides=3
#
# for _ in range(8):
#     for i in range(sides):
#         timmy.right(360/sides)
#         timmy.forward(100)
#
#     sides+=1
#     timmy.color(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)


#Random walk

# timmy.pensize(10)
# timmy.speed(10)
# direction = [1.0, 90.0, 180.0, 270.0]
#
# for _ in range (150):
#     timmy.forward(20)
#     timmy.setheading(random.choice(direction))
#     timmy.pencolor(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)



#Spirograph

# timmy.setheading(180)
#
# number=200
#
# timmy.speed(0)
#
# for _ in range(number):
#     timmy.circle(200)
#     timmy.pencolor(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
#     timmy.left(360/number)


#Hirst Painting

# from colorgram import extract
#
# extr = extract("image.jpg",6)
#
# colors=[]
#
# for color in extr:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.g
#     colors.append((r,g,b))
#
# y=0
# timmy.speed(0)
# colormode(255)
# timmy.color(random.choice(colors))
# timmy.penup()
# for _ in range(10):
#     timmy.sety(y)
#     x=0
#     for _ in range(10):
#         timmy.setx(x)
#         timmy.dot(50)
#         timmy.color(random.choice(colors))
#         x+=50
#     y+=50












screen = Screen()
screen.exitonclick()