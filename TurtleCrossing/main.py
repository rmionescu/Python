import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def exit_game():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing v1")
screen.bgcolor("grey")
screen.tracer(0)
screen.listen()


# Create the player
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Check for keystrokes
screen.onkey(exit_game, "Escape")
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    # print(f"Generated a new car at {car_manager.all_cars[-1].position()}.")
    car_manager.move_car()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if (abs(car.xcor() - player.xcor()) <= 25) and (abs(car.ycor() - player.ycor()) <= 19):
            print(f"Collision with car detected at player position: {player.position()} and car {car.position()}")
            scoreboard.game_over()
            game_is_on = False

    # Check if player crossed the road
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        # Increase the speed for all the cars
        car_manager.increase_speed()

screen.exitonclick()
