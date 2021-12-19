from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from settings import WIDTH, HEIGHT, SNAKE_SPEED, SEGMENT_SIZE

MAX_SPEED = 0.1

snake_is_alive = True
snake_speed = SNAKE_SPEED
change_game_speed = True

# Set the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title(f"Snake v1 | Speed = {round(snake_speed, 2)}")

# Stop the refresh of the screen
screen.tracer(0)

# Create a snake object
snake = Snake()

# Create food object
food = Food()

# Print the score
scoreboard = Scoreboard()

# Check for keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while snake_is_alive:
    time.sleep(snake_speed)
    # Refresh the screen
    screen.update()
    snake.move()
    # print(f"Position = {snake.segments[0].position()}")

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if abs(int(snake.segments[0].xcor())) > (int(WIDTH / 2) - SEGMENT_SIZE) or \
            abs(int(snake.segments[0].ycor())) > (int(HEIGHT / 2) - SEGMENT_SIZE):
        print(f"Wall collision at snake{snake.segments[0].position()} > "
              f"wall{(WIDTH / 2 - SEGMENT_SIZE), (HEIGHT / 2 - SEGMENT_SIZE)}.")
        scoreboard.game_over()
        snake_is_alive = False

    # Detect collision with tail
    for snake_segment in snake.segments[1:]:
        if snake.segments[0].distance(snake_segment) < int(SEGMENT_SIZE / 2):
            print("Tail collision")
            scoreboard.game_over()
            snake_is_alive = False

    if scoreboard.score > 0 and scoreboard.score % 10 == 0 and change_game_speed and (snake_speed - 0.05 > MAX_SPEED):
        snake_speed -= 0.05
        snake_speed = abs(snake_speed)
        change_game_speed = False
        screen.title(f"Snake v1 | Speed = {round(snake_speed, 2)}")
        # print(f"\t >>> Game speed updated to {snake_speed} at level {scoreboard.score}")
    elif scoreboard.score % 10 != 0 and not change_game_speed:
        change_game_speed = True

screen.exitonclick()
