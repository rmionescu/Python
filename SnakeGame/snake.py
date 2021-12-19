from turtle import Turtle
from settings import SEGMENT_SIZE, SNAKE_LENGTH, NORTH, SOUTH, WEST, EAST


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # Create the snake, 3 quare beginning from (0, 0)
        # Each square have 20x20 pixels default
        initial_x_position = 0
        for _ in range(SNAKE_LENGTH):
            self.add_segment((initial_x_position, 0))
            initial_x_position -= SEGMENT_SIZE

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.turtlesize(stretch_wid=SEGMENT_SIZE/20, stretch_len=SEGMENT_SIZE/20)
        t.goto(position)
        t.speed("fastest")
        self.segments.append(t)

    def move(self):
        # Move the snake
        for segment in range(len(self.segments) - 1, -1, -1):
            if segment == 0:
                self.segments[segment].forward(SEGMENT_SIZE)
            else:
                self.segments[segment].goto(self.segments[segment - 1].position())

    def extend(self):
        # Add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def up(self):
        # Change direction to North
        if self.segments[0].heading() != SOUTH:
            self.segments[0].setheading(NORTH)

    def down(self):
        # Change direction to South
        if self.segments[0].heading() != NORTH:
            self.segments[0].setheading(SOUTH)

    def left(self):
        # Change direction to West
        if self.segments[0].heading() != EAST:
            self.segments[0].setheading(WEST)

    def right(self):
        # Change direction to East
        if self.segments[0].heading() != WEST:
            self.segments[0].setheading(EAST)
