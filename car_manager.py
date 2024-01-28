from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.speed=STARTING_MOVE_DISTANCE

    def create(self):
        num=random.randint(1,6)
        if num==4:
            newcar=Turtle("square")
            newcar.shapesize(stretch_wid=1,stretch_len=2)
            newcar.penup()
            newcar.color(random.choice(COLORS))
            newcar.goto(310,random.randint(-230,230))
            self.all_cars.append(newcar)


        
    def move_cars(self):
        for car in (self.all_cars):
            car.backward(self.speed)

    def levelup(self):
        self.speed+=MOVE_INCREMENT


