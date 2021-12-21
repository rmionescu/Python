from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
WIDTH = 600
HEIGHT = 600
SEGMENT_SIZE = 20


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            y = random.randint(-1 * (int(HEIGHT / 2 - 50)) + 15, int(HEIGHT / 2 - 50) - 15)
            if y > 0:
                y = y - (y % SEGMENT_SIZE)
            else:
                y = y + (abs(y) % SEGMENT_SIZE)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_distance)
