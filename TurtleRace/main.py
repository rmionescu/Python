from turtle import Turtle, Screen
import random

WIDTH = 800
HEIGHT = 600

screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
turtle_distance = HEIGHT / (len(colors) / 2)
is_game_on = False

screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("grey")

# Create turtles and put them in the start position
for color in colors:
    turtles.append(Turtle("turtle"))
    turtles[-1].penup()
    turtles[-1].color(color)
    turtles[-1].goto(-(WIDTH / 2) + 50, -(HEIGHT / 2) + turtle_distance)
    turtle_distance += 30

# Draw the finish line
margin = WIDTH / 10
finish_line = Turtle()
finish_line.penup()
finish_line.goto(WIDTH / 2 - 15, HEIGHT / 2 - margin)
finish_line.setheading(270)
finish_line.pendown()
finish_line.forward(HEIGHT - margin * 2)
finish_line.hideturtle()

user_choice = screen.textinput("Choose the winner", "Pick a color:")
if user_choice:
    is_game_on = True

while is_game_on:
    fwd_distance = random.randint(0, 5)
    moving_turtle = random.randint(0, len(turtles) - 1)
    turtles[moving_turtle].forward(fwd_distance)
    if turtles[moving_turtle].position()[0] >= (WIDTH / 2) - 30:
        if turtles[moving_turtle].pencolor() == user_choice.lower():
            print("You WIN!")
        else:
            print(f"Turtle '{turtles[moving_turtle].pencolor()}' won and you have chosen '{user_choice}'!")
        is_game_on = False

screen.exitonclick()
