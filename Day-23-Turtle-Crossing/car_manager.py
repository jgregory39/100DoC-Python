from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MAX_CARS = 30
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.rate = 1.0

    def decide_cars(self):
        if len(self.cars) >= MAX_CARS:
            return
        make_decide = random.randint(1, 10)
        if make_decide <= int(self.rate):
            rand_y = random.randint(-250, 280)
            while not self.is_clear(rand_y):
                rand_y = random.randint(-250, 280)
            self.make_car(rand_y)

    def make_car(self, ycor):
        new_car = Turtle('square')
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(280, ycor)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for i in range(len(self.cars) - 1, -1, -1):
            car = self.cars[i]
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
            else:
                car.forward(self.speed)

    def inc_speed(self):
        self.speed += MOVE_INCREMENT
        self.rate = self.rate + 1

    def is_clear(self, y_pos, check_player=False):
        x_pos = 260
        if check_player:
            x_pos = 0
        for car in self.cars:
            if car.ycor() - 10 < y_pos < car.ycor() + 10 and car.xcor() - 20 < x_pos < car.xcor() + 20:
                return False
        return True
