COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager():

    def __init__(self):
        self.cars = []
        self.counter = 0
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        if self.counter == 6:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.uniform(-250, 250))
            car.shape("square")
            car.shapesize(1.0,2.0)
            self.cars.append(car)
            self.counter=0
        else:
            self.counter += 1

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.speed, car.ycor())
            if car.xcor()<-320:
                self.cars.remove(car)
                car.hideturtle()

    def increase_speed(self):
        self.speed+=MOVE_INCREMENT

    def collision(self, timmy):
        collided=False

        for car in self.cars:
            if car.distance(timmy)<20:
                collided=True
            if car.distance(timmy)<30 and abs(car.ycor()-timmy.ycor()<=20):
                collided = True

        return collided