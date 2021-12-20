from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.x_increment = 5
        self.y_increment = 5

    def move(self):
        x_pos = self.xcor() + self.x_increment
        y_pos = self.ycor() + self.y_increment
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_increment *= -1

    def bounce_x(self):
        self.x_increment *= -1
        self.goto(self.xcor() + self.x_increment * 2, self.ycor() + self.y_increment)
