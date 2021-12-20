from turtle import Turtle
from conf import PADDLE_X_SIZE, PADDLE_Y_SIZE


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        # Create a paddle
        self.shape("square")
        self.speed(0)
        self.penup()
        self.goto(cor)
        self.shapesize(PADDLE_Y_SIZE, PADDLE_X_SIZE)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + (PADDLE_X_SIZE * 20)
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - (PADDLE_X_SIZE * 20)
        self.goto(self.xcor(), new_y)
