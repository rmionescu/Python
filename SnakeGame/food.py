from turtle import Turtle
import random
from settings import FOOD_SIZE, FOOD_SHAPE, FOOD_COLOUR, WIDTH, HEIGHT, SEGMENT_SIZE


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=(FOOD_SIZE/20), stretch_len=(FOOD_SIZE/20))
        self.color(FOOD_COLOUR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-1 * (int(WIDTH / 2)) + 15, int(WIDTH / 2) - 15)
        y = random.randint(-1 * (int(HEIGHT / 2)) + 15, int(HEIGHT / 2) - 15)
        # Make (x, y) multiple of SEGMENT_SIZE
        if x > 0:
            x = x - (x % SEGMENT_SIZE)
        else:
            x = x + (abs(x) % SEGMENT_SIZE)
        if y > 0:
            y = y - (y % SEGMENT_SIZE)
        else:
            y = y + (abs(y) % SEGMENT_SIZE)
        print(f"Food updated position at {x, y}")
        self.goto(x, y)
